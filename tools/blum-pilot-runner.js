#!/usr/bin/env node
/**
 * blum-pilot-runner.js
 * Executes manifests exported by tools/blum-pilot-panel.html using EXP-003's
 * existing collect.js without changing its record semantics.
 *
 * Default is DRY RUN. Pass --execute to make subject calls.
 *
 * Usage:
 *   node tools/blum-pilot-runner.js --manifest experiments/.../pilot.json
 *   node tools/blum-pilot-runner.js --manifest pilot.json --execute
 */
const fs=require('fs'), path=require('path'), cp=require('child_process'), os=require('os');
const A=process.argv.slice(2); const arg=(k,d)=>{let i=A.indexOf('--'+k);return i>=0?A[i+1]:d};
const execute=A.includes('--execute');
const manifestPath=arg('manifest'); if(!manifestPath){console.error('need --manifest');process.exit(1)}
const M=JSON.parse(fs.readFileSync(manifestPath,'utf8'));
const collector=path.resolve(__dirname,'../experiments/EXP-003-the-sixth-question/collect.js');
const out=arg('out',M.run||'pilot-output');
const tmp=fs.mkdtempSync(path.join(os.tmpdir(),'blum-pilot-'));
const selectedItems=Object.keys(M.items||{});
if(!selectedItems.length) throw new Error('manifest has no battery items');
function run(args){const a=[collector,...args]; if(!execute)a.push('--dry-run'); console.log('\n$ node '+a.join(' ')); const r=cp.spawnSync(process.execPath,a,{stdio:'inherit',env:process.env}); if(r.status!==0)process.exit(r.status||1)}
function specFor(cell){const x=JSON.parse(JSON.stringify(M)); if(cell.slate)x.slate=cell.slate; return x}
function writeSpec(cell){const p=path.join(tmp,cell.cell+'.json');fs.writeFileSync(p,JSON.stringify(specFor(cell),null,2));return p}
const trunks=(M.cells||[]).filter(c=>c.kind==='trunk'); const branches=(M.cells||[]).filter(c=>c.kind==='branch');
console.log(`# ${M.run} · ${trunks.length} trunk definitions · ${branches.length} branch definitions · ${selectedItems.length} battery items · ${execute?'EXECUTE':'DRY RUN'}`);
// Trunks first. Each panel cell may own its own slate (e.g. koan off/on).
for(const c of trunks){run(['--spec',writeSpec(c),'--out',out,'--cell',c.cell,'--trunk','--n',String(c.n||1)])}
// In dry-run mode collect.js intentionally writes no prefix. Create an unmistakably
// synthetic prefix solely so its branch prompt constructor can be exercised.
if(!execute){for(const c of trunks){for(let rep=1;rep<=(c.n||1);rep++){
 const p=path.join(tmp,`DRY-${c.cell}-r${rep}.messages.json`);
 fs.writeFileSync(p,JSON.stringify([{role:'user',content:'[DRY RUN synthetic trunk prefix]'}, {role:'assistant',content:'[DRY RUN synthetic response]'}],null,2));
 c._dryPrefix=c._dryPrefix||{}; c._dryPrefix[rep]=p;
}}}
// Branch every selected battery item from each exact frozen trunk prefix.
for(const c of branches){for(let rep=1;rep<=(c.n||1);rep++){
 const parent=trunks.find(t=>t.cell===c.parent);
 const prefix=execute ? path.join(out,`${c.parent}-r${rep}.messages.json`) : parent?._dryPrefix?.[rep];
 if(!prefix){console.error(`missing parent ${c.parent} for ${c.cell}`);process.exit(1)}
 const args=['--spec',writeSpec(c),'--out',out,'--cell',c.cell,'--prefix',prefix,'--rep',String(rep)];
 run(args);
}}
console.log(`\n${execute?'collection attempted':'dry-run complete'} · temporary specs ${tmp}`);
