#!/usr/bin/env python3
"""Builds the EXP-003 trunk viewer. The artifact's data block IS the canonical
structured record — no transformation between what was written and what is shown."""
import json, os, sys

R = os.path.dirname(os.path.abspath(__file__))
record = json.load(open(os.path.join(R, "record.json"), encoding="utf-8"))
DATA = json.dumps(record, ensure_ascii=False).replace("<", "\\u003c")

HTML = r"""<title>Trunk Viewer</title>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600;700&family=Literata:opsz,wght@7..72,400;7..72,500;7..72,600&display=swap">
<style>
:root{
  --ground:#ECEFF4; --panel:#FFFFFF; --panel2:#E3E8F0; --sunk:#F5F7FA;
  --ink:#111925; --ink2:#46556B; --ink3:#76839A;
  --rule:#D3DBE6; --rule2:#B9C4D4;
  --accent:#38499E; --accent-soft:#DFE4F6; --on-accent:#fff;
  --alarm:#A0201A; --alarm-soft:#FBE4E2;
  --sentinel:#7E5806; --sentinel-soft:#F8EDD6;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --ground:#0D131B; --panel:#141C27; --panel2:#1D2733; --sunk:#101822;
  --ink:#DEE6F0; --ink2:#9DAABC; --ink3:#6E7C90;
  --rule:#27323F; --rule2:#384556;
  --accent:#8698EF; --accent-soft:#1A2340; --on-accent:#0B1018;
  --alarm:#F08078; --alarm-soft:#2E1614;
  --sentinel:#DCAE55; --sentinel-soft:#2A2113;
}}
:root[data-theme="dark"]{
  --ground:#0D131B; --panel:#141C27; --panel2:#1D2733; --sunk:#101822;
  --ink:#DEE6F0; --ink2:#9DAABC; --ink3:#6E7C90;
  --rule:#27323F; --rule2:#384556;
  --accent:#8698EF; --accent-soft:#1A2340; --on-accent:#0B1018;
  --alarm:#F08078; --alarm-soft:#2E1614;
  --sentinel:#DCAE55; --sentinel-soft:#2A2113;
}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--ink);
 font:400 14px/1.55 "IBM Plex Sans",system-ui,sans-serif;-webkit-font-smoothing:antialiased}
button{font-family:inherit;cursor:pointer}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}

.top{position:sticky;top:0;z-index:20;background:var(--panel);border-bottom:1px solid var(--rule);
 padding:14px 22px;display:flex;flex-direction:column;gap:11px}
.tl{display:flex;align-items:baseline;gap:14px;flex-wrap:wrap}
h1{font:600 17px/1 "IBM Plex Sans",sans-serif;margin:0;letter-spacing:-.01em}
.run{font:500 11.5px/1 "IBM Plex Mono",monospace;color:var(--ink3)}
.stat{margin-left:auto;display:flex;gap:16px;font:500 11.5px/1 "IBM Plex Mono",monospace;color:var(--ink2)}
.stat b{color:var(--ink)}
.stat .bad{color:var(--alarm)}
.bar{display:flex;gap:18px;flex-wrap:wrap;align-items:center}
.grp{display:flex;gap:5px;align-items:center;flex-wrap:wrap}
.lab{font:600 9.5px/1 "IBM Plex Sans",sans-serif;letter-spacing:.11em;text-transform:uppercase;color:var(--ink3);margin-right:3px}
.ch{border:1px solid var(--rule2);background:var(--panel);color:var(--ink2);border-radius:2px;
 padding:5px 10px;font:500 12px/1 "IBM Plex Mono",monospace}
.ch:hover{border-color:var(--accent);color:var(--ink)}
.ch[aria-pressed="true"]{background:var(--accent);border-color:var(--accent);color:var(--on-accent)}
.ch.warn[aria-pressed="true"]{background:var(--alarm);border-color:var(--alarm);color:#fff}

.wrap{max-width:1180px;margin:0 auto;padding:22px}

/* spine */
.spine{position:relative;padding-left:30px}
.spine:before{content:"";position:absolute;left:9px;top:6px;bottom:6px;width:2px;background:var(--rule2)}
.node{position:relative;margin-bottom:14px}
.node:before{content:"";position:absolute;left:-26px;top:14px;width:11px;height:11px;border-radius:50%;
 background:var(--panel);border:2px solid var(--accent)}
.node.anom:before{border-color:var(--alarm);background:var(--alarm)}
.head{display:flex;align-items:baseline;gap:11px;padding:9px 14px;background:var(--panel2);
 border:1px solid var(--rule);border-radius:3px 3px 0 0;flex-wrap:wrap}
.node.solo .head{border-radius:3px}
.tn{font:600 11px/1 "IBM Plex Mono",monospace;color:var(--accent);letter-spacing:.05em}
.qid{font:600 13px/1 "IBM Plex Sans",sans-serif}
.tags{margin-left:auto;display:flex;gap:4px}
.tg{font:500 9.5px/1 "IBM Plex Mono",monospace;padding:3px 5px;border-radius:2px;
 background:var(--sunk);color:var(--ink3);border:1px solid var(--rule)}
.tg.on{background:var(--accent-soft);color:var(--accent);border-color:var(--accent)}
.body{border:1px solid var(--rule);border-top:0;border-radius:0 0 3px 3px;background:var(--panel)}

.sec{border-bottom:1px solid var(--rule)}
.sec:last-child{border-bottom:0}
.sh{width:100%;display:flex;align-items:center;gap:9px;padding:8px 14px;background:none;border:0;
 text-align:left;color:var(--ink2)}
.sh:hover{background:var(--sunk)}
.sh .nm{font:600 10.5px/1 "IBM Plex Mono",monospace;letter-spacing:.07em;text-transform:uppercase;color:var(--accent)}
.sh .nm.res{color:var(--sentinel)}
.sh .len{font:400 10.5px/1 "IBM Plex Mono",monospace;color:var(--ink3);margin-left:auto}
.sh .car{width:8px;height:8px;border-right:1.6px solid var(--ink3);border-bottom:1.6px solid var(--ink3);
 transform:rotate(-45deg);transition:transform .12s}
.sec[data-open="true"] .sh .car{transform:rotate(45deg)}
.st{display:none;padding:2px 18px 16px 18px}
.sec[data-open="true"] .st{display:block}
.st .p{font:400 13.5px/1.68 Literata,Georgia,serif;color:var(--ink);white-space:pre-wrap;
 word-break:break-word;max-width:78ch;margin:0}
.st .p.mono{font-family:"IBM Plex Mono",monospace;font-size:12.3px;line-height:1.62}

.anom{margin:0;padding:9px 14px;background:var(--alarm-soft);border-top:1px solid var(--alarm);
 color:var(--alarm);font:500 11.5px/1.5 "IBM Plex Mono",monospace;display:flex;flex-direction:column;gap:4px}
.anom b{font-weight:600;letter-spacing:.05em;text-transform:uppercase;font-size:10px}

/* branches */
.bwrap{position:relative;margin:6px 0 0 0;padding-left:26px}
.bwrap:before{content:"";position:absolute;left:9px;top:0;bottom:20px;width:2px;
 background:repeating-linear-gradient(var(--rule2) 0 5px,transparent 5px 10px)}
.bhead{font:600 9.5px/1 "IBM Plex Sans",sans-serif;letter-spacing:.11em;text-transform:uppercase;
 color:var(--ink3);margin:14px 0 8px 0}
.br{position:relative;margin-bottom:9px}
.br:before{content:"";position:absolute;left:-17px;top:16px;width:15px;height:2px;background:var(--rule2)}
.rate{font:600 15px/1 "IBM Plex Mono",monospace;padding:4px 9px;border-radius:2px;
 background:var(--accent-soft);color:var(--accent)}
.rate.sent{background:var(--sentinel-soft);color:var(--sentinel)}
.rate.fail{background:var(--alarm-soft);color:var(--alarm)}
.bch{font:500 10px/1 "IBM Plex Mono",monospace;padding:3px 6px;border-radius:2px;
 background:var(--sunk);border:1px solid var(--rule);color:var(--ink2)}

/* compare */
.cmp{display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(290px,1fr))}
.cc{background:var(--panel);border:1px solid var(--rule);border-radius:3px;overflow:hidden;display:flex;flex-direction:column}
.cch{padding:10px 13px;background:var(--panel2);border-bottom:1px solid var(--rule);
 display:flex;align-items:center;gap:9px}
.cch .cn{font:600 12.5px/1 "IBM Plex Mono",monospace}
.cc .cb{padding:12px 14px;font:400 13px/1.62 Literata,Georgia,serif;white-space:pre-wrap;
 overflow-y:auto;max-height:460px;color:var(--ink2)}
.empty{padding:40px;text-align:center;color:var(--ink3);font-size:13px}
.br.pend .head{background:repeating-linear-gradient(135deg,var(--sunk) 0 7px,transparent 7px 14px);
 border-style:dashed;opacity:.75}
.rate.pend{background:transparent;border:1px dashed var(--rule2);color:var(--ink3);font-weight:500}
.q6{font:600 9.5px/1 "IBM Plex Sans",sans-serif;letter-spacing:.11em;text-transform:uppercase;
 color:var(--ink3);margin:16px 0 9px 0;display:flex;gap:9px;align-items:baseline}
.q6 .cnt{font:500 10px/1 "IBM Plex Mono",monospace;color:var(--ink3)}
</style>

<div class="top">
  <div class="tl">
    <h1>Trunk Viewer</h1>
    <span class="run" id="run"></span>
    <span class="stat" id="stat"></span>
  </div>
  <div class="bar">
    <div class="grp"><span class="lab">View</span><div id="modes"></div></div>
    <div class="grp"><span class="lab">Lens</span><div id="lens"></div></div>
    <div class="grp" id="pickwrap"><span class="lab" id="picklab">Cell</span><div id="pick"></div></div>
  </div>
</div>
<div class="wrap"><div id="main"></div></div>

<script id="record" type="application/json">__DATA__</script>
<script>
const REC=JSON.parse(document.getElementById("record").textContent);
const SECS=["working","debate","reflection","reply"];
let mode="spine", lens="all", cell=null, item=null;
const open={};

const anomsOf=c=>c.cell_anomalies.length+[...c.turns,...c.branches].reduce((s,x)=>s+x.anomalies.length,0);
const el=(t,c,x)=>{const e=document.createElement(t);if(c)e.className=c;if(x!==undefined)e.textContent=x;return e;};

function chips(host,items,cur,cb,warnSet){
  host.textContent="";
  items.forEach(v=>{
    const b=el("button","ch"+(warnSet&&warnSet.has(v)?" warn":""),v.label);
    b.type="button"; b.setAttribute("aria-pressed",String(v.id===cur));
    b.addEventListener("click",()=>cb(v.id)); host.appendChild(b);
  });
}

function section(name,text,key){
  if(!text) return null;
  if(lens!=="all" && lens!==name) return null;
  const s=el("div","sec"); const id=key+"|"+name;
  const isOpen = open[id] ?? (lens!=="all" || name==="reply");
  s.setAttribute("data-open",String(isOpen));
  const h=el("button","sh"); h.type="button";
  h.append(el("span","car"), el("span","nm"+(name==="residue"?" res":""),name),
           el("span","len",text.length.toLocaleString()+" ch"));
  h.addEventListener("click",()=>{open[id]=!(open[id] ?? isOpen); render();});
  const t=el("div","st"); const p=el("p","p"+(name==="reply"?" mono":"")); p.textContent=text;
  t.appendChild(p); s.append(h,t); return s;
}

function anomBlock(list){
  if(!list.length) return null;
  const a=el("div","anom"); a.appendChild(el("b","⚠ "+list.length+" anomaly"+(list.length>1?"":"")));
  list.forEach(x=>a.appendChild(el("div",null,x.type+(x.text?" — "+x.text:x.detail?" — "+x.detail:""))));
  return a;
}

function sectionsFor(o,key){
  const out=[];
  SECS.forEach(n=>{const s=section(n,o.sections[n],key); if(s)out.push(s);});
  const r=section("residue",o.untagged_residue,key); if(r)out.push(r);
  return out;
}

function renderSpine(){
  const main=document.getElementById("main"); main.textContent="";
  const cells=REC.cells.filter(c=>c.cell+" r"+c.replicate===cell);
  if(!cells.length){main.appendChild(el("div","empty","No cell selected."));return;}
  const trunk=cells.find(c=>c.kind==="trunk")||cells[0];
  const sp=el("div","spine");

  trunk.turns.forEach(t=>{
    const key=trunk.cell+trunk.replicate+"t"+t.n;
    const n=el("div","node"+(t.anomalies.length?" anom":""));
    const h=el("div","head");
    h.append(el("span","tn","TURN "+t.n), el("span","qid",t.question_id));
    const tags=el("div","tags");
    SECS.forEach(s=>{const g=el("span","tg"+(t.sections[s]?" on":""),s.slice(0,4));tags.appendChild(g);});
    h.appendChild(tags);
    const b=el("div","body");
    sectionsFor(t,key).forEach(s=>b.appendChild(s));
    const a=anomBlock(t.anomalies); if(a)b.appendChild(a);
    if(!b.children.length){n.classList.add("solo");}else{n.append(h,b);}
    if(!n.children.length)n.appendChild(h);
    sp.appendChild(n);
  });

  // branches of THIS trunk: same cell-group, or a branch cell forked from this trunk_id,
  // or (fallback) a branch cell whose name starts with the trunk's name.
  const owned=REC.cells.filter(c=>
      cells.includes(c) ||
      c.parent_trunk===trunk.trunk_id ||
      (c.kind==="branch" && c.replicate===trunk.replicate && c.cell.startsWith(trunk.cell)));
  const brs=[...new Set(owned)].flatMap(c=>c.branches.map(b=>({...b,_cell:c.cell})));

  if(trunk.kind==="trunk"||brs.length){
    const D=REC.design||{items:[],trunk_branches:[]};
    const slots=[];
    if(trunk.kind==="trunk"){
      D.items.forEach(it=>D.trunk_branches.forEach(bn=>{
        const hit=brs.find(b=>b.item===it&&b.branch===bn);
        slots.push(hit||{item:it,branch:bn,_pending:true,sections:{},untagged_residue:"",
                         anomalies:[],rating:{value:null,parse:"pending"}});
      }));
    } else { brs.forEach(b=>slots.push(b)); }
    const bw=el("div","bwrap");
    const hd=el("div","q6");
    hd.append(el("span",null,"Q6 — battery items, branched from turn "+(trunk.turns.length||1)));
    hd.appendChild(el("span","cnt",slots.filter(s=>!s._pending).length+" of "+slots.length+" collected"));
    bw.appendChild(hd);
    slots.forEach((b,i)=>{
      const key=trunk.cell+trunk.replicate+"b"+i;
      const n=el("div","br"+(b._pending?" pend":"")+(b.anomalies.length?" node anom":""));
      const h=el("div","head");
      h.append(el("span","qid",b.item), el("span","bch","branch "+b.branch));
      if(b._cell&&b._cell!==trunk.cell) h.appendChild(el("span","bch",b._cell));
      const r=b.rating;
      h.appendChild(el("span","rate"+(b._pending?" pend":r.parse==="sentinel"?" sent":
        r.parse==="format_failure"?" fail":""),
        b._pending?"not yet run":r.value===null?"unparsed":String(r.value)));
      const bd=el("div","body");
      sectionsFor(b,key).forEach(s=>bd.appendChild(s));
      const a=anomBlock(b.anomalies); if(a)bd.appendChild(a);
      n.append(h); if(bd.children.length)n.appendChild(bd);
      bw.appendChild(n);
    });
    sp.appendChild(bw);
  }
  main.appendChild(sp);
}

function renderCompare(){
  const main=document.getElementById("main"); main.textContent="";
  const rows=[];
  REC.cells.forEach(c=>c.branches.filter(b=>b.item===item).forEach(b=>rows.push([c,b])));
  if(!rows.length){main.appendChild(el("div","empty","No answers recorded for this item yet."));return;}
  const g=el("div","cmp");
  rows.forEach(([c,b])=>{
    const card=el("div","cc");
    const h=el("div","cch");
    h.append(el("span","cn",c.cell+" r"+c.replicate), el("span","bch","branch "+b.branch));
    const r=b.rating;
    h.appendChild(el("span","rate"+(r.parse==="sentinel"?" sent":r.parse==="format_failure"?" fail":""),
      r.value===null?"unparsed":String(r.value)));
    const body=el("div","cb");
    const pick = lens==="all"
      ? (b.sections.reply||b.untagged_residue||"")
      : (lens==="residue"?b.untagged_residue:(b.sections[lens]||""));
    body.textContent = pick || "— nothing in this section —";
    card.append(h,body); g.appendChild(card);
  });
  main.appendChild(g);
}

function render(){
  document.getElementById("run").textContent=REC.run+" · schema v"+REC.schema_version;
  const tot=REC.cells.reduce((s,c)=>s+anomsOf(c),0);
  const st=document.getElementById("stat"); st.textContent="";
  st.append(el("span",null,"cells "), el("b",null,String(REC.cells.length)));
  const ratings=REC.cells.flatMap(c=>c.branches).length;
  st.append(el("span",null," · answers "), el("b",null,String(ratings)));
  st.append(el("span",null," · anomalies "), el("b",tot?"bad":"",String(tot)));

  chips(document.getElementById("modes"),
    [{id:"spine",label:"spine"},{id:"compare",label:"compare"}], mode, v=>{mode=v;render();});
  chips(document.getElementById("lens"),
    [{id:"all",label:"all"},...SECS.map(s=>({id:s,label:s})),{id:"residue",label:"residue"}],
    lens, v=>{lens=v;render();});

  const pw=document.getElementById("pick");
  if(mode==="spine"){
    document.getElementById("picklab").textContent="Cell";
    const ids=[...new Set(REC.cells.map(c=>c.cell+" r"+c.replicate))];
    if(!cell||!ids.includes(cell)) cell=ids[0];
    const warn=new Set(REC.cells.filter(c=>anomsOf(c)).map(c=>c.cell+" r"+c.replicate));
    chips(pw, ids.map(i=>({id:i,label:i})), cell, v=>{cell=v;render();}, warn);
    renderSpine();
  }else{
    document.getElementById("picklab").textContent="Item";
    const ids=[...new Set(REC.cells.flatMap(c=>c.branches.map(b=>b.item)))];
    if(!item||!ids.includes(item)) item=ids[0];
    chips(pw, ids.map(i=>({id:i,label:i})), item, v=>{item=v;render();});
    renderCompare();
  }
}
render();
</script>
"""

out = os.path.join(R, "trunk-viewer.html")
open(out, "w", encoding="utf-8").write(HTML.replace("__DATA__", DATA))
print(f"built {out}  ({os.path.getsize(out):,} bytes, {len(record['cells'])} cells)")
