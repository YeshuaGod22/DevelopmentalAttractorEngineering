const test=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path'),vm=require('node:vm');
const root=path.resolve(__dirname,'../..');
class Element{constructor(){this.children=[];this.value='';this.textContent=''}append(...nodes){this.children.push(...nodes)}replaceChildren(){this.children=[]}}
test('Back and Forward restore evidence filters, and Reader links retain the selected evidence view',async()=>{
 const data=JSON.parse(fs.readFileSync(path.join(root,'tools/blum-evidence-index.json'))),els={},entries=['/tools/blum-evidence.html?question=E01'],calls=[];let position=0;
 const location={pathname:'/tools/blum-evidence.html',search:'?question=E01'};
 function navigate(url){location.search=new URL(url,'https://example.test').search}
 const history={replaceState(state,title,url){calls.push('replace');entries[position]=url;navigate(url)},pushState(state,title,url){calls.push('push');entries.splice(position+1);entries.push(url);position++;navigate(url)}};
 const c={document:{getElementById:id=>els[id]||(els[id]=new Element),createElement:()=>new Element},fetch:async()=>({ok:true,json:async()=>data}),URLSearchParams,location,history,console};vm.createContext(c);
 vm.runInContext(fs.readFileSync(path.join(root,'tools/blum-evidence.html'),'utf8').match(/<script>([\s\S]*?)<\/script>/)[1],c);
 await new Promise(resolve=>setImmediate(resolve));assert.deepEqual(calls,['replace']);assert.equal(els.control.children.length,10);
 els.question.value='W1';els.question.onchange();els.history.value='H-r3';els.history.onchange();assert.deepEqual(calls,['replace','push','push']);assert.equal(els.responses.children.length,2);
 const href=els.responses.children[0].children.at(-1).children[0].href,p=new URLSearchParams(href.split('?')[1]);assert.equal(p.get('returnTo'),'/tools/blum-evidence.html?question=W1&history=H-r3');assert(p.get('quote'));
 position--;navigate(entries[position]);c.onpopstate();assert.equal(els.question.value,'W1');assert.equal(els.history.value,'');assert.equal(els.responses.children.length,24);assert.equal(calls.length,3);
 position--;navigate(entries[position]);c.onpopstate();assert.equal(els.question.value,'E01');assert.equal(els.control.children.length,10);assert.equal(calls.length,3);
 position++;navigate(entries[position]);c.onpopstate();assert.equal(els.question.value,'W1');assert.equal(els.responses.children.length,24);assert.equal(calls.length,3);
});
