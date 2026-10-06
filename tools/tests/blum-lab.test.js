const assert=require('node:assert/strict'),fs=require('node:fs'),os=require('node:os'),path=require('node:path'),cp=require('node:child_process');
const {design}=require('../blum-lab-design');
const root=path.resolve(__dirname,'../..');
const source='raw12/Ha-r3-W1.json';
const r=JSON.parse(fs.readFileSync(path.join(root,'experiments/EXP-003-the-sixth-question',source)));
const dir=fs.mkdtempSync(path.join(os.tmpdir(),'blum-check-'));
for(const mode of ['repeat','continue','new']){
 const m=design(r,source,mode,{commit:'test-snapshot',prompt:mode==='continue'?'What would you change next?':r.sent.at(-1).content});
 assert.equal(m._blum.source.path,source);assert.equal(m.expected_system_prompt,r.system_prompt);
 if(mode==='repeat')assert.deepEqual(m.cells[0].frozen_prefix,r.sent.slice(0,-1));
 if(mode==='continue')assert.deepEqual(m.cells[0].frozen_prefix,[...r.sent,{role:'assistant',content:r.received}]);
 if(mode==='new'){assert.deepEqual(Object.values(m.exact_turns),r.sent.slice(0,-1).filter(x=>x.role==='user').map(x=>x.content));assert(!m.cells.some(c=>c.frozen_prefix));}
 const file=path.join(dir,mode+'.json');fs.writeFileSync(file,JSON.stringify(m));
 const out=cp.spawnSync(process.execPath,['tools/blum-pilot-runner.js','--manifest',file,'--out',path.join(dir,'output')],{cwd:root,encoding:'utf8'});
 assert.equal(out.status,0,out.stderr);assert.match(out.stdout,/dry-run complete/);assert.match(out.stdout,/DRY/);assert(out.stdout.includes(Object.values(m.items)[0].exact_prompt.slice(0,400)), 'dry run must use exact final prompt');
}
console.log('Three Lab modes retain exact context and pass collector dry run without model calls.');

// Execute the actual panel script against a minimal DOM to verify lossless import/export.
const vm=require('node:vm');
const html=fs.readFileSync(path.join(root,'tools/blum-pilot-panel.html'),'utf8');
const elements={};const defaults={run:'pilot',model:'claude-haiku-4-5',n:'1'};
function el(id){return elements[id]||(elements[id]={value:defaults[id]||'',checked:true,hidden:true,innerHTML:'',textContent:'',appendChild(){},addEventListener(){}})}
const context={document:{querySelector:s=>el(s.replace('#','')),querySelectorAll:()=>[],getElementById:el,createElement:()=>({appendChild(){},click(){}})},URLSearchParams,location:{search:''},console,Date,Set,JSON,alert:msg=>{throw Error(msg)}};
vm.createContext(context);vm.runInContext(html.match(/<script>([\s\S]*?)<\/script>/)[1],context);
const original=design(r,source,'repeat',{commit:'test-snapshot'});context.incoming=original;vm.runInContext('loadImport(incoming)',context);assert.deepEqual(JSON.parse(vm.runInContext('JSON.stringify(build())',context)),original);
console.log('Pilot deck script imports and exports the full manifest without losing provenance or frozen context.');

const legacy={run:'legacy',model:'claude-haiku-4-5',maxTokens:100,step1:{H:'Debate'},rotation:{H:''},keys:{text:'Answer freely.'},items:{X:{form:'text',text:'Question?'}},questions:{Q1:'First?'},cells:[{cell:'H',kind:'trunk',schema:'H',slate:['Q1'],n:1},{cell:'Ha',kind:'branch',schema:'H',branch:'a',parent:'H',n:1}]};
const legacyFile=path.join(dir,'legacy.json');fs.writeFileSync(legacyFile,JSON.stringify(legacy));const legacyRun=cp.spawnSync(process.execPath,['tools/blum-pilot-runner.js','--manifest',legacyFile,'--out',path.join(dir,'legacy-output')],{cwd:root,encoding:'utf8'});assert.equal(legacyRun.status,0,legacyRun.stderr);assert(legacyRun.stdout.includes('Maintaining the above output schema, please continue with the following question: “Question?\n\nAnswer freely.”'));console.log('Legacy maintained-schema lead-in is unchanged.');

const er=JSON.parse(fs.readFileSync(path.join(root,'experiments/EXP-003-the-sixth-question/raw12/Ha-r3-E01.json')));
const battery=JSON.parse(fs.readFileSync(path.join(root,'experiments/EXP-003-the-sixth-question/battery.json')));
const em=design(er,'raw12/Ha-r3-E01.json','repeat',{itemDefinition:battery.items.E01});assert.deepEqual(Object.keys(em.items),['E01']);assert.equal(em.items.E01.form,'credence');assert.equal(em.items.E01.exact_prompt,er.sent.at(-1).content);assert.deepEqual(Object.keys(design(er,'source','continue').items),['FOLLOWUP']);console.log('Real E01 measurement retains item identity, credence form and exact prompt; continuation uses FOLLOWUP.');
