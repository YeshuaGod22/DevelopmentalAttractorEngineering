const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path'),vm=require('node:vm');
const root=path.resolve(__dirname,'../..'),data=JSON.parse(fs.readFileSync(path.join(root,'tools/blum-evidence-index.json')));
for(const [p,meta] of Object.entries(data.records)){const raw=fs.readFileSync(path.join(root,'experiments/EXP-003-the-sixth-question',p));assert.equal(require('node:crypto').createHash('sha256').update(raw).digest('hex'),meta.sha256)}
class Element{constructor(){this.children=[];this.value='';this.textContent=''}append(...nodes){this.children.push(...nodes)}replaceChildren(){this.children=[]}}
const els={},doc={getElementById:id=>els[id]||(els[id]=new Element),createElement:()=>new Element};
const c={document:doc,fetch:async()=>({ok:true,json:async()=>data}),URLSearchParams,location:{search:''},history:{replaceState(){}},console};vm.createContext(c);
const source=fs.readFileSync(path.join(root,'tools/blum-evidence.html'),'utf8').match(/<script>([\s\S]*?)<\/script>/)[1];vm.runInContext(source,c);
setImmediate(()=>{assert.equal(els.control.children.length,10);assert(els.responses.children.length>0);els.question.value='W1';els.question.onchange();assert.equal(els.responses.children.length,24);els.history.value='H-r3';els.history.onchange();assert.equal(els.responses.children.length,2);assert(els.responses.children.every(r=>r.children.at(-1).children[0].href.includes('quote=')));console.log('Evidence index hashes, all ten fresh C answers, 24 reviews and individual filters verified.');});
