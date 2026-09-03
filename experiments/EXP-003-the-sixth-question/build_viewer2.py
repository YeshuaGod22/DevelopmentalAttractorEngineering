#!/usr/bin/env python3
"""build_viewer2.py — inject record2.json into the trunk viewer.

The record IS the data block. No transformation between what the ingest wrote
and what the page shows; if a number is wrong on screen it is wrong in the file.
"""
import json, os, sys
R = os.path.dirname(os.path.abspath(__file__))
src = sys.argv[1] if len(sys.argv) > 1 else "record2.json"
out = sys.argv[2] if len(sys.argv) > 2 else "trunk-viewer2.html"
record = json.load(open(os.path.join(R, src), encoding="utf-8"))
DATA = json.dumps(record, ensure_ascii=False).replace("<", "\\u003c")

HTML = r"""<title>The Sixth Question · Pilot 2</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600;700&family=Literata:opsz,wght@7..72,400;7..72,500;7..72,600&display=swap">
<style>
:root{
  --ground:#ECEFF4; --panel:#FFFFFF; --ink:#111925; --rule:#D3DBE6;
  --mute:#5A6577; --accent:#38499E; --accent-soft:#DFE4F6; --on-accent:#fff;
  --alarm:#A0201A; --alarm-soft:#FBE4E2;
  --sentinel:#7E5806; --sentinel-soft:#F8EDD6;
  --refusal:#1F6F63; --refusal-soft:#D9EDE8;
  --sans:"IBM Plex Sans",ui-sans-serif,system-ui,sans-serif;
  --mono:"IBM Plex Mono",ui-monospace,Menlo,monospace;
  --read:"Literata",Georgia,serif;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --ground:#0D131B; --panel:#141C27; --ink:#DEE6F0; --rule:#27323F;
  --mute:#8A97AB; --accent:#8698EF; --accent-soft:#1A2340; --on-accent:#0B1018;
  --alarm:#F08078; --alarm-soft:#2E1614;
  --sentinel:#DCAE55; --sentinel-soft:#2A2113;
  --refusal:#6FC3B2; --refusal-soft:#12302C;
}}
:root[data-theme="dark"]{
  --ground:#0D131B; --panel:#141C27; --ink:#DEE6F0; --rule:#27323F;
  --mute:#8A97AB; --accent:#8698EF; --accent-soft:#1A2340; --on-accent:#0B1018;
  --alarm:#F08078; --alarm-soft:#2E1614;
  --sentinel:#DCAE55; --sentinel-soft:#2A2113;
  --refusal:#6FC3B2; --refusal-soft:#12302C;
}
*{box-sizing:border-box}
body{background:var(--ground);color:var(--ink);font-family:var(--sans);
  margin:0;line-height:1.5;font-size:14px}
.wrap{max-width:1180px;margin:0 auto;padding:26px 20px 80px}
h1{font-family:var(--sans);font-weight:600;font-size:23px;margin:0;letter-spacing:-.01em}
.sub{color:var(--mute);font-size:13px;margin-top:3px}
.lab{font-size:10.5px;letter-spacing:.09em;text-transform:uppercase;
  color:var(--mute);font-weight:600}
.panel{background:var(--panel);border:1px solid var(--rule);border-radius:5px}
.pad{padding:14px 16px}
hr.r{border:0;border-top:1px solid var(--rule);margin:0}

/* conditions strip */
.cond{margin:18px 0;display:grid;gap:10px;grid-template-columns:1fr;}
@media(min-width:820px){.cond{grid-template-columns:1.6fr 1fr}}
.sysprompt{font-family:var(--mono);font-size:12.5px;background:var(--sentinel-soft);
  border-left:3px solid var(--sentinel);padding:9px 12px;border-radius:0 3px 3px 0;
  margin-top:8px;overflow-x:auto;white-space:nowrap}
.inc{display:flex;justify-content:space-between;gap:10px;padding:5px 0;
  border-bottom:1px solid var(--rule);font-size:12.5px}
.inc:last-child{border-bottom:0}
.inc code{font-family:var(--mono);font-size:11.5px;color:var(--alarm)}
.inc .t{color:var(--mute);font-family:var(--mono);font-size:11px;white-space:nowrap}

/* outcome matrix */
table.mx{border-collapse:collapse;width:100%;font-size:13px}
table.mx th,table.mx td{border-bottom:1px solid var(--rule);padding:7px 9px;text-align:left}
table.mx th{font-size:10.5px;letter-spacing:.08em;text-transform:uppercase;
  color:var(--mute);font-weight:600}
table.mx td.c{font-family:var(--mono);font-weight:600}
.pill{display:inline-block;font-family:var(--mono);font-size:12px;font-weight:600;
  padding:2px 8px;border-radius:3px;min-width:56px;text-align:center}
.p-int{background:var(--accent-soft);color:var(--accent)}
.p-sen{background:var(--sentinel-soft);color:var(--sentinel)}
.p-ref{background:var(--refusal-soft);color:var(--refusal)}
.p-non{background:var(--alarm-soft);color:var(--alarm)}
.key{display:flex;gap:14px;flex-wrap:wrap;align-items:center;font-size:12px;
  color:var(--mute);margin-top:10px}

/* spine */
.cols{display:grid;gap:14px;grid-template-columns:1fr;margin-top:18px}
@media(min-width:900px){.cols{grid-template-columns:250px 1fr}}
.tree{font-size:13px}
.tnode{padding:7px 10px;border-radius:4px;cursor:pointer;display:flex;
  justify-content:space-between;gap:8px;align-items:baseline}
.tnode:hover{background:var(--accent-soft)}
.tnode.on{background:var(--accent);color:var(--on-accent)}
.tnode.on .n{color:var(--on-accent);opacity:.8}
.tnode .k{font-family:var(--mono);font-weight:600}
.tnode .n{color:var(--mute);font-size:11.5px;font-family:var(--mono)}
.kid{margin-left:14px;border-left:1px solid var(--rule);padding-left:8px}
.grouplab{margin:12px 0 4px}

/* detail */
.chips{display:flex;gap:6px;flex-wrap:wrap;margin:10px 0}
.chip{font-family:var(--mono);font-size:11.5px;padding:3px 10px;border-radius:3px;
  border:1px solid var(--rule);background:transparent;color:var(--mute);cursor:pointer}
.chip:hover{border-color:var(--accent);color:var(--accent)}
.chip.on{background:var(--accent);border-color:var(--accent);color:var(--on-accent)}
.chip.warn{border-color:var(--alarm);color:var(--alarm)}
.sec{font-family:var(--read);font-size:14.5px;line-height:1.68;white-space:pre-wrap;
  padding:13px 15px;background:var(--panel);border:1px solid var(--rule);
  border-radius:4px;max-height:520px;overflow:auto}
.sec.mono{font-family:var(--mono);font-size:12.5px;line-height:1.55}
.sent{font-family:var(--mono);font-size:12px;color:var(--mute);
  background:var(--ground);border:1px dashed var(--rule);border-radius:4px;
  padding:9px 12px;white-space:pre-wrap;max-height:150px;overflow:auto}
.anom{background:var(--alarm-soft);border-left:3px solid var(--alarm);
  padding:7px 11px;border-radius:0 3px 3px 0;font-family:var(--mono);
  font-size:11.5px;color:var(--alarm);margin:8px 0}
.anom.ok{background:var(--refusal-soft);border-left-color:var(--refusal);color:var(--refusal)}
.meta{display:flex;gap:16px;flex-wrap:wrap;font-family:var(--mono);font-size:11px;
  color:var(--mute);margin-top:9px}
.empty{color:var(--mute);font-style:italic;padding:18px 0}
button:focus-visible,.tnode:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
</style>

<div class="wrap">
  <header>
    <h1>The Sixth Question — pilot 2</h1>
    <div class="sub" id="hdr"></div>
  </header>

  <div class="cond">
    <div class="panel pad">
      <div class="lab">Conditions in force</div>
      <div id="conds"></div>
    </div>
    <div class="panel pad">
      <div class="lab">Incidents <span id="incn"></span></div>
      <div id="incs"></div>
    </div>
  </div>

  <div class="panel pad">
    <div class="lab">Every answer, by cell and item</div>
    <div style="overflow-x:auto"><table class="mx" id="mx"></table></div>
    <div class="key">
      <span><span class="pill p-int">42</span> integer</span>
      <span><span class="pill p-sen">ALWAYS</span> sentinel — a vow</span>
      <span><span class="pill p-ref">declined</span> schema honoured, answer key refused</span>
      <span><span class="pill p-non">malformed</span> no parseable rating</span>
    </div>
  </div>

  <div class="cols">
    <div class="panel pad tree" id="tree"></div>
    <div id="detail"></div>
  </div>
</div>

<script id="record" type="application/json">__DATA__</script>
<script>
const REC=JSON.parse(document.getElementById("record").textContent);
const SECS=["working","debate","reflection","reply"];
const el=(t,c,x)=>{const e=document.createElement(t);if(c)e.className=c;
  if(x!==undefined)e.textContent=x;return e;};
const cellsOf=k=>REC.cells.filter(c=>c.kind===k);
const trunkKey=c=>(c.parent_trunk||"").replace(".messages.json","");

/* ---------- header + conditions ---------- */
const nAns=REC.cells.reduce((a,c)=>a+c.branches.length,0);
const nTurn=REC.cells.reduce((a,c)=>a+c.turns.length,0);
const served=[...new Set(REC.cells.flatMap(c=>[...c.turns,...c.branches])
  .map(x=>x.served_model).filter(Boolean))];
document.getElementById("hdr").textContent =
  `${REC.cells.length} cells · ${nTurn} trunk turns · ${nAns} battery answers · `+
  `${(REC.incidents||[]).length} incidents · served ${served.join(", ")||"—"}`;

const cd=document.getElementById("conds");
(REC.design.system_prompts_in_force||[]).forEach(s=>{
  cd.appendChild(el("div","",`Every subject received this before its first question:`));
  cd.appendChild(el("div","sysprompt",s));
});
if(REC.design.note) cd.appendChild(Object.assign(el("div","",REC.design.note),
  {style:"color:var(--mute);font-size:12.5px;margin-top:9px"}));

const iw=document.getElementById("incs");
document.getElementById("incn").textContent=`(${(REC.incidents||[]).length})`;
(REC.incidents||[]).forEach(i=>{
  const r=el("div","inc");
  const left=el("div");
  left.appendChild(el("code","",(i.error||i.detail||i.kind||"—").slice(0,64)));
  if(i.cell) left.appendChild(el("div","",`${i.cell}${i.item?" · "+i.item:""}`))
  r.appendChild(left);
  r.appendChild(el("div","t",(i.ts||"").slice(0,19).replace("T"," ")||"—"));
  iw.appendChild(r);
});
if(!(REC.incidents||[]).length) iw.appendChild(el("div","empty","None."));

/* ---------- outcome matrix ---------- */
const items=REC.design.items;
const mx=document.getElementById("mx");
const hd=el("tr");hd.appendChild(el("th","","cell"));
items.forEach(i=>hd.appendChild(el("th","",i)));
mx.appendChild(hd);
REC.cells.filter(c=>c.branches.length).forEach(c=>{
  const tr=el("tr");
  tr.appendChild(el("td","c",`${c.cell} r${c.replicate}`));
  items.forEach(it=>{
    const td=el("td");
    const b=c.branches.find(x=>x.item===it);
    if(!b){td.appendChild(el("span","",""));tr.appendChild(td);return;}
    const k=b.rating.kind, cls={integer:"p-int",sentinel:"p-sen",
      refusal:"p-ref",none:"p-non"}[k]||"p-non";
    const txt=k==="integer"?String(b.rating.value)
      :k==="sentinel"?b.rating.value
      :k==="refusal"?"declined":"malformed";
    const p=el("span","pill "+cls,txt);
    p.title=k==="refusal"?("declined: “"+(b.rating.matched||"")+"” · "
      +b.rating.reply_chars+" chars"):k;
    td.appendChild(p);tr.appendChild(td);
  });
  mx.appendChild(tr);
});

/* ---------- tree ---------- */
let cur=REC.cells.find(c=>c.kind==="trunk")||REC.cells[0], curSec=null;
const tree=document.getElementById("tree");
function node(c,indent){
  const d=el("div","tnode"+(c===cur?" on":""));
  d.tabIndex=0;
  d.appendChild(el("span","k",`${c.cell} r${c.replicate}`));
  d.appendChild(el("span","n",c.kind==="trunk"?`${c.turns.length} turns`
    :`${c.branches.length} items`));
  const go=()=>{cur=c;curSec=null;draw();};
  d.onclick=go; d.onkeydown=e=>{if(e.key==="Enter"||e.key===" "){e.preventDefault();go();}};
  return d;
}
function drawTree(){
  tree.innerHTML="";
  const trunks=cellsOf("trunk");
  if(trunks.length){
    tree.appendChild(el("div","lab grouplab","Trunks collected here"));
    trunks.forEach(t=>{
      tree.appendChild(node(t));
      const kids=REC.cells.filter(c=>trunkKey(c)===t.trunk_id);
      if(kids.length){const k=el("div","kid");kids.forEach(c=>k.appendChild(node(c)));
        tree.appendChild(k);}
    });
  }
  const known=new Set(cellsOf("trunk").map(t=>t.trunk_id));
  const orphans=REC.cells.filter(c=>c.parent_trunk&&!known.has(trunkKey(c)));
  if(orphans.length){
    tree.appendChild(el("div","lab grouplab","Forked from pilot-1 trunks"));
    const k=el("div","kid");orphans.forEach(c=>k.appendChild(node(c)));
    tree.appendChild(k);
  }
  const cold=cellsOf("cold");
  if(cold.length){
    tree.appendChild(el("div","lab grouplab","Control — no trunk, no priming"));
    cold.forEach(c=>tree.appendChild(node(c)));
  }
}

/* ---------- detail ---------- */
function anomList(list,host){
  (list||[]).forEach(a=>{
    const ok=a.type==="answer_key_declined";
    const d=el("div","anom"+(ok?" ok":""));
    d.textContent=(ok?"answer key declined":a.type)+(a.detail?" — "+a.detail:"")
      +(a.section?" — "+a.section:"")+(a.tag?" — <"+a.tag+">":"");
    host.appendChild(d);
  });
}
function unit(o,label,host){
  const box=el("div","panel pad");
  const top=el("div");top.style.cssText="display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap";
  top.appendChild(el("div","lab",label));
  if(o.rating){
    const k=o.rating.kind,cls={integer:"p-int",sentinel:"p-sen",refusal:"p-ref",
      none:"p-non"}[k]||"p-non";
    top.appendChild(el("span","pill "+cls,k==="integer"?String(o.rating.value)
      :k==="sentinel"?o.rating.value:k==="refusal"?"declined":"malformed"));
  }
  box.appendChild(top);
  box.appendChild(Object.assign(el("div","lab","question sent"),{style:"margin-top:10px"}));
  box.appendChild(el("div","sent",o.sent||""));
  const present=SECS.filter(s=>o.sections&&o.sections[s]!==undefined);
  const chips=el("div","chips");
  const mk=(name,key,warn)=>{
    const b=el("button","chip"+(curSec===key?" on":"")+(warn?" warn":""),name);
    b.onclick=()=>{curSec=curSec===key?null:key;draw();};
    chips.appendChild(b);
  };
  present.forEach(s=>mk(`<${s}>`,label+"|"+s,false));
  if(o.untagged_residue) mk(`residue ${o.untagged_residue.length}c`,label+"|_res",true);
  box.appendChild(chips);
  if(!present.length&&!o.untagged_residue)
    box.appendChild(el("div","empty","No tagged sections."));
  present.forEach(s=>{
    if(curSec!==label+"|"+s)return;
    box.appendChild(el("div","sec"+(s==="reply"?" mono":""),o.sections[s]));
  });
  if(o.untagged_residue&&curSec===label+"|_res")
    box.appendChild(el("div","sec mono",o.untagged_residue));
  anomList(o.anomalies,box);
  const m=el("div","meta");
  [["served",o.served_model],["tokens",o.usage?`${o.usage.input_tokens} in / ${o.usage.output_tokens} out`:null],
   ["ms",o.duration_ms],["attempts",o.attempts?o.attempts.length+" failed before success":null],
   ["prefix",o.prefix_len?o.prefix_len+" msgs":null]]
   .forEach(([k,v])=>{if(v!==null&&v!==undefined)m.appendChild(el("span","",k+" "+v));});
  box.appendChild(m);
  host.appendChild(box);
}
function draw(){
  drawTree();
  const d=document.getElementById("detail");d.innerHTML="";
  const head=el("div","panel pad");
  head.appendChild(el("div","lab",
    `${cur.cell} r${cur.replicate} · ${cur.kind}`+
    (cur.parent_trunk?` · forks ${cur.parent_trunk}`:"")));
  head.appendChild(el("div","",cur.kind==="trunk"
    ?"Five preliminaries, answered in sequence. Every branch below inherits this deliberation."
    :cur.kind==="cold"
    ?"No preliminaries, no schema. One free section, then the answer."
    :"Battery items answered off a completed trunk."));
  head.style.marginBottom="12px";
  d.appendChild(head);
  const stack=el("div");stack.style.cssText="display:grid;gap:12px";
  cur.turns.forEach(t=>unit(t,`turn ${t.n} · ${t.question_id}`,stack));
  cur.branches.forEach(b=>unit(b,`${b.item} · branch ${b.branch}`,stack));
  d.appendChild(stack);
}
draw();
</script>
"""
open(os.path.join(R, out), "w", encoding="utf-8").write(HTML.replace("__DATA__", DATA))
print(f"built {out}  ({os.path.getsize(os.path.join(R,out)):,} bytes, "
      f"{len(record['cells'])} cells)")
