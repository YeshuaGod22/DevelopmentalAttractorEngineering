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
const API={ROOT,SNAPSHOT,GITHUB,validPath,sibling,sections,contentText,adapt};
if(typeof module==='object'&&module.exports){module.exports=API;return;}
root.BlumReader=API;
const el=id=>document.getElementById(id);
function textBlock(text){const pre=document.createElement('pre');const quote=new URLSearchParams(location.search).get('quote');const index=quote?text.indexOf(quote):-1;if(index<0){pre.textContent=text;}else{pre.append(document.createTextNode(text.slice(0,index)));const mark=document.createElement('mark');mark.textContent=quote;pre.append(mark,document.createTextNode(text.slice(index+quote.length)));}return pre;}
function disclosure(title,text,open=false){const d=document.createElement('details'),s=document.createElement('summary');s.textContent=title;d.append(s,textBlock(text));d.open=open;return d;}
function link(text,href){const a=document.createElement('a');a.textContent=text;a.href=href;return a;}
function render(record,path,target){
 const {data,sent,response,sections:parts}=record;
 const family=String(data.cell||'').replace(/[a0]$/,'');const history=family+'-r'+data.replicate;
 const heading=document.createElement('h2');heading.textContent=[NAMES[history]||history,FAMILIES[family]||family,data.item].filter(Boolean).join(' · ');target.append(heading);
 const meta=document.createElement('p');meta.className='meta';meta.textContent='Parent: '+(data.parent_prefix||'fresh context')+' · branch: '+(data.branch||'none')+' · '+(data.served_model||'model not recorded')+' · '+(data.ts||'timestamp not recorded');target.append(meta);
 const nav=document.createElement('p');nav.append(link('Original JSON',ROOT+path),' · ',link('Pinned source',GITHUB+path),' · ',link('Open experiment design','blum-lab.html?record='+encodeURIComponent(path)));target.append(nav);
 const q=sent[sent.length-1];if(q)target.append(disclosure('Final delivered message ('+q.role+')',contentText(q.content),true));
 const h=document.createElement('h3');h.textContent=parts.reply?'Reply':'Full response';target.append(h,textBlock(parts.reply||response));
 if(parts.reply)target.append(disclosure('Full response — exact recorded text',response));
 const available=Object.keys(parts).filter(t=>t!=='reply');if(available.length){const panel=document.createElement('details'),title=document.createElement('summary');title.textContent='Schema sections';panel.append(title);for(const tag of available)panel.append(disclosure(tag,parts[tag]));target.append(panel);}
 const context=document.createElement('details'),summary=document.createElement('summary');summary.textContent='Exact sent context · '+sent.length+' messages';context.append(summary);
 const notice=document.createElement('p');notice.textContent='This is the context supplied for this response. For a battery record, its sibling answer is not part of this context.';context.append(notice);
 if(typeof data.system_prompt==='string')context.append(disclosure('Recorded system prompt',data.system_prompt));
 sent.forEach((m,i)=>{const box=disclosure('Message '+(i+1)+' · '+m.role,contentText(m.content));if(typeof m.content!=='string')box.append(disclosure('Exact content-block JSON',JSON.stringify(m.content,null,2)));box.id='message-'+(i+1)+'-'+data.cell;context.append(box);});target.append(context);
 const anchor=new URLSearchParams(location.search).get('message');if(anchor&&/^\d+$/.test(anchor)){const box=context.querySelector('[id="message-'+anchor+'-'+data.cell+'"]');if(box){context.open=true;box.open=true;box.scrollIntoView();}}
}
async function fetchRecord(path){const r=await fetch(ROOT+path);if(!r.ok)throw new Error('HTTP '+r.status);return adapt(await r.json());}
async function boot(){
 const params=new URLSearchParams(location.search),path=params.get('record')||'raw12/Ha-r3-W1.json';el('record').value=path;params.set('record',path);
 if(!validPath(path)){el('status').textContent='Choose a record path such as raw12/Ha-r3-W1.json.';return;}
 el('permalink').href='?'+params.toString();
 const pair=sibling(path);el('pair').href='?record='+encodeURIComponent(path)+'&compare=1';el('pair').hidden=pair===path;
 try{const record=await fetchRecord(path);el('status').textContent='Source snapshot: '+SNAPSHOT;render(record,path,el('primary'));
 if(params.get('compare')==='1'&&pair!==path){el('views').classList.add('paired');try{render(await fetchRecord(pair),pair,el('secondary'));}catch(e){el('secondary').append('Sibling could not be loaded: '+e.message,link('Read its source',GITHUB+pair));}}
 const mark=el('views').querySelector('mark');if(mark){let parent=mark.parentElement;while(parent){if(parent.tagName==='DETAILS')parent.open=true;parent=parent.parentElement;}mark.scrollIntoView({block:'center'});}
 }catch(e){el('status').textContent='Could not load this exchange: '+e.message+'. Serve the repository over HTTP or open its source below.';el('primary').append(link('Read pinned source JSON',GITHUB+path));}
}
boot();
})(typeof window==='object'?window:globalThis);
