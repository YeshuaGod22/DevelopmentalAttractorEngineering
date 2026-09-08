#!/usr/bin/env node
/** progress.js — status of a v3 run. `--html` writes a self-refreshing page. */
const fs=require('fs'),path=require('path');
const OUT=process.argv.includes('--out')?process.argv[process.argv.indexOf('--out')+1]:'raw12';
const M=JSON.parse(fs.readFileSync('trunk-manifest-v3.json','utf8'));
const CONDS=Object.keys(M.conditions), REPS=3, TURNS=M.conditions.CP.turns.length;
const ITEMS=M.battery_manifest.total_items;
const load=f=>{try{return JSON.parse(fs.readFileSync(f,'utf8'))}catch{return null}};
const files=fs.existsSync(OUT)?fs.readdirSync(OUT):[];
const recs=files.filter(f=>f.endsWith('.json')&&!/\.(name|inject|messages|name\.confirmed)\.json$/.test(f))
  .map(f=>load(path.join(OUT,f))).filter(Boolean);
const turns={},branches={},names={},severed={};
for(const r of recs){
  const k=`${r.cell}-r${r.replicate}`;
  // A trunk turn counts only if it reached the schema's terminal tag. The runner
  // now gates on this too, so a miss here means something slipped past the gate —
  // which is exactly when a dashboard must not report the turn as done.
  if(r.kind==='trunk'){ if(String(r.received||'').includes('</reflection>')) (turns[k]=turns[k]||new Set()).add(r.turn);
                        else (severed[k]=severed[k]||new Set()).add(r.turn); }
  else if(r.item) (branches[k]=branches[k]||new Set()).add(r.item);
}
for(const f of files.filter(f=>f.endsWith('.name.json'))){
  const d=load(path.join(OUT,f)); if(d) names[`${d.condition}-r${d.replicate||1}`]=d;
}
const inc=fs.existsSync('incidents')?fs.readdirSync('incidents').filter(f=>f.endsWith('.json')).length:0;
// Resamples are turns the subject did not finish and was asked again. They are a
// property of the run worth seeing while it happens, not after.
const rejDir=path.join(OUT,'rejected');
const resampled=fs.existsSync(rejDir)?fs.readdirSync(rejDir).filter(f=>f.endsWith('.json')).length:0;
const severedN=Object.values(severed).reduce((a,s)=>a+s.size,0);
const ts=recs.map(r=>r.ts).filter(Boolean).sort();
const span=ts.length>1?(new Date(ts[ts.length-1])-new Date(ts[0]))/1000:0;
const totalCalls=CONDS.length*REPS*(TURNS+ITEMS*2), done=recs.length;
const rate=recs.length>1&&span?span/recs.length:0;
const rows=[];
for(const c of CONDS) for(let p=1;p<=REPS;p++){
  const k=`${c}-r${p}`;
  rows.push({k,t:(turns[k]||new Set()).size,b:(branches[k]||new Set()).size,
             name:names[k]?(names[k].name||'—declined—'):null});
}
const bar=(n,d,w=14)=>{const f=Math.round(n/d*w);return '█'.repeat(f)+'·'.repeat(w-f)};
if(!process.argv.includes('--html')){
  console.log(`\n  ${done}/${totalCalls} calls   ${(100*done/totalCalls).toFixed(0)}%   `+
    `${rate?rate.toFixed(0)+'s/call':''}   incidents ${inc}\n`);
  console.log(`  ${'trunk'.padEnd(8)}${'turns'.padEnd(20)}${'branches'.padEnd(22)}name`);
  for(const r of rows) console.log(`  ${r.k.padEnd(8)}${(bar(r.t,TURNS)+' '+r.t+'/'+TURNS).padEnd(20)}`+
    `${(bar(r.b,ITEMS*2)+' '+r.b+'/'+ITEMS).padEnd(22)}${r.name??''}`);
  console.log();
} else {
  const cell=r=>`<tr><td class=k>${r.k}</td>
    <td><div class=b><i style="width:${100*r.t/TURNS}%"></i></div><span>${r.t}/${TURNS}</span></td>
    <td><div class=b><i class=g style="width:${100*r.b/(ITEMS)}%"></i></div><span>${r.b}/${ITEMS}</span></td>
    <td class=${r.name?(r.name==='—declined—'?'dec':'nm'):''}>${r.name??''}</td></tr>`;
  fs.writeFileSync('progress.html',`<!doctype html><meta charset=utf-8>
<meta http-equiv=refresh content=20><title>EXP-004 run</title><style>
:root{--ink:#111925;--bg:#ECEFF4;--pan:#fff;--rule:#D3DBE6;--acc:#38499E;--g:#1F6F63;--al:#A0201A;--mu:#5A6577}
@media(prefers-color-scheme:dark){:root{--ink:#DEE6F0;--bg:#0D131B;--pan:#141C27;--rule:#27323F;--acc:#8698EF;--g:#6FC3B2;--al:#F08078;--mu:#8A97AB}}
body{background:var(--bg);color:var(--ink);font:14px/1.5 "IBM Plex Sans",ui-sans-serif,system-ui;margin:0;padding:26px}
.w{max-width:760px;margin:0 auto}h1{font-size:19px;margin:0 0 2px;font-weight:600}
.s{color:var(--mu);font-size:12.5px;margin-bottom:16px;font-variant-numeric:tabular-nums}
table{width:100%;border-collapse:collapse;background:var(--pan);border:1px solid var(--rule);border-radius:5px}
td,th{padding:7px 11px;border-bottom:1px solid var(--rule);text-align:left;font-size:13px}
tr:last-child td{border-bottom:0}
th{font-size:10px;letter-spacing:.09em;text-transform:uppercase;color:var(--mu)}
.k{font-family:"IBM Plex Mono",monospace;font-weight:600}
.b{background:var(--rule);height:7px;border-radius:4px;overflow:hidden;min-width:120px;display:inline-block;vertical-align:middle}
.b i{display:block;height:100%;background:var(--acc)}.b i.g{background:var(--g)}
td span{font-family:"IBM Plex Mono",monospace;font-size:11px;color:var(--mu);margin-left:8px}
.nm{font-family:"IBM Plex Mono",monospace;color:var(--g);font-weight:600}
.dec{color:var(--al);font-style:italic}
</style><div class=w><h1>EXP-004 developmental trunks</h1>
<div class=s>${done} / ${totalCalls} calls &middot; ${(100*done/totalCalls).toFixed(0)}% &middot; ${rate?rate.toFixed(0)+'s per call':'—'} &middot; ${inc} incidents &middot; refreshed ${new Date().toLocaleTimeString()}</div>
<table><tr><th>trunk<th>turns<th>battery<th>name</tr>${rows.map(cell).join('')}</table></div>`);
}
