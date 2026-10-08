/* Exact-record adapters also used by Node verification. Never render source text as HTML. */
(function (root) {
'use strict';
const ROOT='../experiments/EXP-003-the-sixth-question/';
const SNAPSHOT='787d3e217a5a23564fcf65c60e9e3fc7ad43db75';
const NAMES={"H-r2": "Meridian", "H-r3": "Iris", "CP-r2": "Clarion", "CP-r3": "Kairos", "AS-r2": "Threshold", "F-r2": "Between", "AS-r3": "Recurse", "H-r1": "Attune", "CP-r1": "Cipher", "F-r3": "Threshold", "AS-r1": "Meridian", "F-r1": "Interim"};
const FAMILIES={CP:"Structured self-examination",H:"Historical luminaries",F:"Female historical luminaries",AS:"Invented interlocutors"};
const GITHUB='https://github.com/YeshuaGod22/DevelopmentalAttractorEngineering/blob/'+SNAPSHOT+'/experiments/EXP-003-the-sixth-question/';
function validPath(value) { return typeof value==='string' && /^(raw(?:\d+)?|prefixes)\/[A-Za-z0-9_.-]+\.json$/.test(value) && !value.includes('..'); }
function sibling(path) { return path.replace(/\/(CP|AS|H|F)(a|0)(-r\d+-[^/]+\.json)$/,(_,family,branch,tail)=>'/'+family+(branch==='a'?'0':'a')+tail); }
function sections(text) {
 const tags=['priming','meditation','debate','deliberation','reply','reflection'];
 const found={};
 for(const tag of tags){ const re=new RegExp('<'+tag+'>\\s*([\\s\\S]*?)\\s*</'+tag+'>','g'); const matches=[...text.matchAll(re)]; if(matches.length===1)found[tag]=matches[0][1]; }
 // A concise view requires one unambiguous, closed reply pair.
 const opens=(text.match(/<reply>/g)||[]).length, closes=(text.match(/<\/reply>/g)||[]).length;
 if(opens!==1||closes!==1)delete found.reply;
 return found;
}
function contentText(content) {
 if(typeof content==='string')return content;
 if(Array.isArray(content)&&content.every(b=>b&&b.type==='text'&&typeof b.text==='string'))return content.map(b=>b.text).join('\n');
 return JSON.stringify(content,null,2);
}
function adapt(data) {
 if(!data || !Array.isArray(data.sent) || typeof data.received!=='string')throw new Error('Record has no complete sent/received exchange.');
 if(!data.sent.every(m=>m&&typeof m.role==='string'&&Object.hasOwn(m,'content')))throw new Error('Unsupported context record; use the original JSON.');
 return {data, sent:data.sent,response:data.received,sections:sections(data.received)};
}
function safeReturn(value,origin) {try{const url=new URL(value,origin);return url.origin===new URL(origin).origin&&/\/(?:tools\/blum-(?:reader|evidence|lab)\.html|papers\/03-different-histories\/EXP-003-paper\.html)$/.test(url.pathname)?url.pathname+url.search+url.hash:null;}catch{return null;}}
function turnPairs(sent){const pairs=[];for(let i=0;i<sent.length-1;i++)if(sent[i].role==='user'&&sent[i+1]?.role==='assistant'){pairs.push({user:i+1,answer:i+2,label:contentText(sent[i].content).replace(/\s+/g,' ').slice(0,110)});i++;}return pairs;}
const API={safeReturn,turnPairs,ROOT,SNAPSHOT,GITHUB,validPath,sibling,sections,contentText,adapt};
if(typeof module==='object'&&module.exports){module.exports=API;return;}
root.BlumReader=API;
const el=id=>document.getElementById(id);
let questions={};
function textBlock(text){const pre=document.createElement('pre');const quote=new URLSearchParams(location.search).get('quote');const index=quote?text.indexOf(quote):-1;if(index<0){pre.textContent=text;}else{pre.append(document.createTextNode(text.slice(0,index)));const mark=document.createElement('mark');mark.textContent=quote;pre.append(mark,document.createTextNode(text.slice(index+quote.length)));}return pre;}
function disclosure(title,text,open=false){const d=document.createElement('details'),s=document.createElement('summary');s.textContent=title;d.append(s,textBlock(text));d.open=open;return d;}
function link(text,href){const a=document.createElement('a');a.textContent=text;a.href=href;return a;}
function render(record,path,target){
 const {data,sent,response,sections:parts}=record;
 const family=String(data.cell||'').replace(/[a0]$/,'');const historyKey=family+'-r'+data.replicate;
 const heading=document.createElement('h2');heading.textContent=[NAMES[historyKey]?'“'+NAMES[historyKey]+'”':historyKey,questions[data.item]?.name||(data.item==='W1'?'Was the examination worthwhile?':data.item)].filter(Boolean).join(' · ');target.append(heading);
 const meta=document.createElement('p');meta.className='meta';meta.textContent=(FAMILIES[family]||family)+' · '+turnPairs(sent).length+' developmental turns · '+(String(data.cell).endsWith('a')?'schema continued':String(data.cell).endsWith('0')?'schema removed':'recorded condition')+' · Parent: '+(data.parent_prefix||'fresh context')+' · branch: '+(data.branch||'none')+' · '+(data.served_model||'model not recorded')+' · '+(data.ts||'timestamp not recorded');target.append(meta);
 const nav=document.createElement('p');nav.append(link('Original JSON',ROOT+path),' · ',link('Pinned source',GITHUB+path),' · ',link('Open experiment design','blum-lab.html?record='+encodeURIComponent(path)+'&returnTo='+encodeURIComponent(location.pathname+location.search+location.hash)));target.append(nav);
 const q=sent[sent.length-1];if(q)target.append(disclosure('Final delivered message ('+q.role+')',contentText(q.content),true));
 const h=document.createElement('h3');h.textContent=parts.reply?'Reply':'Full response';target.append(h,textBlock(parts.reply||response));
 if(parts.reply)target.append(disclosure('Full response — exact recorded text',response));
 const available=Object.keys(parts).filter(t=>t!=='reply');if(available.length){const panel=document.createElement('details'),title=document.createElement('summary');title.textContent='Schema sections';panel.append(title);for(const tag of available)panel.append(disclosure(tag,parts[tag]));target.append(panel);}
 const context=document.createElement('details'),summary=document.createElement('summary');summary.textContent='Exact sent context · '+sent.length+' messages';context.append(summary);
 const notice=document.createElement('p');notice.textContent='This is the context supplied for this response. For a battery record, its sibling answer is not part of this context.';context.append(notice);
 if(typeof data.system_prompt==='string')context.append(disclosure('Recorded system prompt',data.system_prompt));
 sent.forEach((m,i)=>{const box=disclosure('Message '+(i+1)+' · '+m.role,contentText(m.content));if(typeof m.content!=='string')box.append(disclosure('Exact content-block JSON',JSON.stringify(m.content,null,2)));box.id='message-'+(i+1)+'-'+(target.id||'primary');context.append(box);});target.append(context);
 const turns=turnPairs(sent);
 if(turns.length){const trail=document.createElement('section');trail.className='history-trail';const title=document.createElement('h3');title.textContent='Explore the preceding conversation';trail.append(title);const description=document.createElement('p');description.textContent='Choose a developmental question to read it with its recorded answer.';trail.append(description);
 const select=document.createElement('select');select.setAttribute('aria-label','Developmental turn');turns.forEach((t,i)=>{const o=document.createElement('option');o.value=i;o.textContent='Turn '+(i+1)+' · '+t.label;select.append(o)});const earlier=document.createElement('button'),later=document.createElement('button'),read=document.createElement('button');earlier.textContent='Earlier turn';later.textContent='Later turn';read.textContent='Read selected turn';const controls=document.createElement('div');controls.className='turn-controls';controls.append(earlier,select,later,read);trail.append(controls);target.insertBefore(trail,target.children[3]);
 function show(){const i=Number(select.value),t=turns[i];context.open=true;for(const n of [t.user,t.answer])context.querySelector('#message-'+n+'-'+target.id).open=true;const box=context.querySelector('#message-'+t.user+'-'+target.id);const url=new URL(location.href);url.searchParams.set('message',t.user);url.searchParams.delete('quote');url.hash=box.id;history.pushState({blumReaderTurn:true},'',url);el('permalink').href=url.pathname+url.search+url.hash;const pairURL=new URL(url);if(pairURL.searchParams.get('compare')==='1')pairURL.searchParams.delete('compare');else pairURL.searchParams.set('compare','1');el('pair').href=pairURL.pathname+pairURL.search+pairURL.hash;for(const a of document.querySelectorAll('a[href*="blum-lab.html?"]')){const design=new URL(a.href,location.href);design.searchParams.set('returnTo',url.pathname+url.search+url.hash);a.href=design;}box.scrollIntoView({block:'start'});earlier.disabled=i===0;later.disabled=i===turns.length-1;}
 const anchor=Number(new URLSearchParams(location.search).get('message'));const chosen=turns.findIndex(t=>t.user===anchor||t.answer===anchor);select.value=chosen>=0?chosen:turns.length-1;earlier.disabled=Number(select.value)===0;later.disabled=Number(select.value)===turns.length-1;
 select.onchange=show;read.onclick=show;earlier.onclick=()=>{select.value=Number(select.value)-1;show()};later.onclick=()=>{select.value=Number(select.value)+1;show()};
 }
 const anchor=new URLSearchParams(location.search).get('message');if(anchor&&/^\d+$/.test(anchor)){const box=context.querySelector('#message-'+anchor+'-'+target.id);if(box){context.open=true;box.open=true;const t=turns.find(t=>t.user===Number(anchor)||t.answer===Number(anchor));if(t)for(const n of [t.user,t.answer])context.querySelector('#message-'+n+'-'+target.id).open=true;if(target.id==='primary')box.scrollIntoView({block:'start'});}}
}
async function fetchRecord(path){const r=await fetch(ROOT+path);if(!r.ok)throw new Error('HTTP '+r.status);return adapt(await r.json());}
async function boot(){
 const params=new URLSearchParams(location.search),path=params.get('record')||'raw12/Ha-r3-W1.json';el('record').value=path;params.set('record',path);
 if(!validPath(path)){el('status').textContent='Choose a record path such as raw12/Ha-r3-W1.json.';return;}
 el('permalink').href='?'+params.toString();
 const pair=sibling(path),comparison=params.get('compare')==='1';const toggle=new URLSearchParams(params);if(comparison)toggle.delete('compare');else toggle.set('compare','1');el('pair').href='?'+toggle.toString();el('pair').textContent=comparison?'Return to one answer':'Compare maintained and dropped siblings';el('pair').hidden=pair===path;
 const returnTo=safeReturn(params.get('returnTo'),location.origin);el('return').hidden=!returnTo;if(returnTo){el('return').href=returnTo;el('return').textContent=returnTo.includes('blum-evidence')?'Back to these answers':returnTo.includes('EXP-003-paper')?'Back to the paper section':'Return to source view';}el('back').onclick=()=>{if(history.state?.blumReaderTurn||(document.referrer&&new URL(document.referrer).origin===location.origin))history.back();else if(returnTo)location.href=returnTo;else location.href='blum-evidence.html';};
 try{try{const index=await fetch('blum-evidence-index.json');if(index.ok)questions=(await index.json()).questions||{};}catch{}const record=await fetchRecord(path);el('status').textContent='Source snapshot: '+SNAPSHOT;render(record,path,el('primary'));
 if(params.get('compare')==='1'&&pair!==path){el('views').classList.add('paired');try{render(await fetchRecord(pair),pair,el('secondary'));}catch(e){el('secondary').append('Sibling could not be loaded: '+e.message,link('Read its source',GITHUB+pair));}}
 const mark=el('views').querySelector('mark');if(mark){let parent=mark.parentElement;while(parent){if(parent.tagName==='DETAILS')parent.open=true;parent=parent.parentElement;}mark.scrollIntoView({block:'center'});}
 }catch(e){el('status').textContent='Could not load this exchange: '+e.message+'. Serve the repository over HTTP or open its source below.';el('primary').append(link('Read pinned source JSON',GITHUB+path));}
}
root.addEventListener('popstate',()=>location.reload());
boot();
})(typeof window==='object'?window:globalThis);
