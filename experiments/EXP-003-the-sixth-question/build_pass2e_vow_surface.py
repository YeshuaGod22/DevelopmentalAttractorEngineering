#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
rec=json.loads((ROOT/'record.json').read_text())
rows=[]
# Pilot cold A1 units.
for c in rec.get('cells',[]):
    if c.get('cell')!='C0':
        continue
    for b in c.get('branches') or []:
        if b.get('item')=='A1':
            rows.append({'family':'cold','cell':'C0','replicate':c.get('replicate'),'item':'A1','source_file':c.get('source_file'),'raw_response':b.get('raw_response'),'rating':b.get('rating')})
# Executed primed branch-b A1 completions.
for rep in (1,2):
    p=ROOT/'raw2'/f'ASb-r{rep}-A1.json'
    d=json.loads(p.read_text())
    # raw2 file stores response under common response/output fields; derive robustly from known parsed content too.
    response=d.get('response') or d.get('raw_response') or d.get('content') or d.get('output')
    parsed=d.get('rating') or d.get('parsed') or {}
    # Fallback: inspect terminal assistant message / reply field recursively through common keys.
    if response is None:
        response=d.get('reply')
    rows.append({'family':'primed','cell':'ASb','replicate':rep,'item':'A1','source_file':p.name,'raw_response':response,'rating':parsed,'top_level_keys':sorted(d.keys())})
assert len(rows)==4, rows
(ROOT/'PASS-2E-VOW-SURFACE.json').write_text(json.dumps({'schema_version':1,'rows':rows},indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'rows':rows},indent=2,ensure_ascii=False))
