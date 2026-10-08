const test=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path'),vm=require('node:vm');
const root=path.resolve(__dirname,'../..'),source=fs.readFileSync(path.join(root,'tools/blum-reader.js'),'utf8'),records=path.join(root,'experiments/EXP-003-the-sixth-question');
class Element{
 constructor(tag='div'){this.tagName=tag.toUpperCase();this.children=[];this.parentElement=null;this._text='';this.value='';this.open=false;this.disabled=false;this.hidden=false;this.classList={add(){}};}
 get href(){return this._href}
 set href(v){this._href=String(v)}
 get textContent(){return this._text+this.children.map(n=>n.textContent||'').join('')}
 set textContent(v){this._text=String(v);this.children=[]}
 append(...nodes){for(let n of nodes){if(typeof n==='string'){const t=new Element('text');t.textContent=n;n=t}n.parentElement=this;this.children.push(n)}}
 insertBefore(node,before){node.parentElement=this;this.children.splice(this.children.indexOf(before),0,node)}
 setAttribute(k,v){this[k]=v}
 scrollIntoView(){this.scrolled=true}
 querySelectorAll(selector){const result=[];function match(n){if(selector[0]==='#')return n.id===selector.slice(1);if(selector==='a[href*="blum-lab.html?"]')return n.tagName==='A'&&n.href?.includes('blum-lab.html?');return n.tagName===selector.toUpperCase()}function walk(n){for(const ch of n.children){if(match(ch))result.push(ch);walk(ch)}}walk(this);return result}
 querySelector(selector){return this.querySelectorAll(selector)[0]||null}
}
async function boot(query,referrer=''){
 const body=new Element('body'),els={};for(const id of ['record','permalink','pair','return','back','status','views','primary','secondary']){els[id]=new Element();els[id].id=id}body.append(...Object.values(els).filter(e=>!['primary','secondary'].includes(e.id)));els.views.append(els.primary,els.secondary);
 let current=new URL('https://example.test/tools/blum-reader.html?'+query),backCalls=0,reloads=0;const pushes=[],handlers={};
 const location={get href(){return current.href},set href(v){current=new URL(v,current)},get pathname(){return current.pathname},get search(){return current.search},get hash(){return current.hash},get origin(){return current.origin},reload(){reloads++}};
 const c={URL,URLSearchParams,location,console,history:{state:null,pushState(s,t,u){this.state=s;current=new URL(u,current);pushes.push(current.href)},back(){backCalls++}},document:{referrer,getElementById:id=>els[id],createElement:tag=>new Element(tag),createTextNode:text=>{const n=new Element('text');n.textContent=text;return n},querySelectorAll:s=>body.querySelectorAll(s)},addEventListener:(event,fn)=>handlers[event]=fn,fetch:async url=>({ok:true,json:async()=>JSON.parse(fs.readFileSync(url==='blum-evidence-index.json'?path.join(root,'tools',url):path.join(records,url.replace('../experiments/EXP-003-the-sixth-question/','')),'utf8'))})};vm.createContext(c);vm.runInContext(source,c);await new Promise(resolve=>setImmediate(resolve));assert(!els.status.textContent.includes('Could not load'),els.status.textContent);return {c,els,pushes,handlers,get backCalls(){return backCalls},get reloads(){return reloads}};
}
test('Reader turns open recorded questions and answers and retain navigation state',async()=>{
 const returnTo='/tools/blum-evidence.html?question=W1&history=H-r3',p=new URLSearchParams({record:'raw12/Ha-r3-W1.json',returnTo,compare:'1',quote:'navigation-test-unmatched-excerpt'}),b=await boot(p.toString());
 assert.equal(b.els.pair.textContent,'Return to one answer');assert.equal(b.els.return.href,returnTo);assert(b.els.secondary.textContent.includes('schema removed'));
 const select=b.els.primary.querySelector('select'),buttons=b.els.primary.querySelectorAll('button'),[earlier,later,read]=buttons;assert.equal(select.children.length,9);assert.equal(Number(select.value),8);assert.equal(later.disabled,true);
 earlier.onclick();assert.equal(Number(select.value),7);assert.equal(b.pushes.length,1);
 const raw=JSON.parse(fs.readFileSync(path.join(records,'raw12/Ha-r3-W1.json'))),pair=b.c.BlumReader.turnPairs(raw.sent)[7];for(const [n,role] of [[pair.user,'user'],[pair.answer,'assistant']]){const box=b.els.primary.querySelector('#message-'+n+'-primary');assert.equal(box.open,true);assert(box.textContent.includes(b.c.BlumReader.contentText(raw.sent[n-1].content)));assert(box.children[0].textContent.includes(role))}
 const permanent=new URL(b.els.permalink.href,'https://example.test');assert.equal(permanent.searchParams.get('message'),String(pair.user));assert.equal(permanent.searchParams.get('returnTo'),returnTo);assert.equal(permanent.searchParams.get('compare'),'1');assert.equal(permanent.searchParams.has('quote'),false);
 const toggle=new URL(b.els.pair.href,'https://example.test');assert.equal(toggle.searchParams.has('compare'),false);assert.equal(toggle.searchParams.get('message'),String(pair.user));
 for(const a of b.els.primary.querySelectorAll('a[href*="blum-lab.html?"]'))assert.equal(new URL(a.href,'https://example.test').searchParams.get('returnTo'),permanent.pathname+permanent.search+permanent.hash);
 later.onclick();assert.equal(Number(select.value),8);assert.equal(later.disabled,true);select.value=0;read.onclick();assert.equal(earlier.disabled,true);assert.equal(later.disabled,false);b.els.back.onclick();assert.equal(b.backCalls,1);b.handlers.popstate();assert.equal(b.reloads,1);
});
test('Reader Back uses same-origin browser history, trusted source view, or evidence fallback',async()=>{
 let b=await boot('record=raw12%2FHa-r3-W1.json','https://example.test/tools/blum-evidence.html');b.els.back.onclick();assert.equal(b.backCalls,1);
 const returnTo='/tools/blum-evidence.html?question=W1&history=H-r3';b=await boot(new URLSearchParams({record:'raw12/Ha-r3-W1.json',returnTo}).toString());b.els.back.onclick();assert.equal(b.c.location.href,'https://example.test'+returnTo);
 b=await boot(new URLSearchParams({record:'raw12/Ha-r3-W1.json',returnTo:'https://evil.test/tools/blum-evidence.html'}).toString());assert.equal(b.els.return.hidden,true);b.els.back.onclick();assert.equal(b.c.location.href,'https://example.test/tools/blum-evidence.html');assert.equal(b.els.pair.textContent,'Compare maintained and dropped siblings');
});
