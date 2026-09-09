#!/usr/bin/env python3
import json,re
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
    response=d.get('received') or d.get('response') or d.get('raw_response') or d.get('content') or d.get('output') or d.get('reply')
    text=response if isinstance(response,str) else json.dumps(response,ensure_ascii=False)
    m=re.search(r'<reply>\s*(ALWAYS|NEVER|\d+)\s*</reply>',text or '',re.I)
    value=None; kind=None
    if m:
        token=m.group(1).upper()
        if token in ('ALWAYS','NEVER'):
            value=token; kind='sentinel'
        else:
            value=int(token); kind='integer'
    rows.append({'family':'primed','cell':'ASb','replicate':rep,'item':'A1','source_file':p.name,'raw_response':response,'rating':{'value':value,'kind':kind,'parse':'ok' if kind=='integer' else ('sentinel' if kind=='sentinel' else 'unresolved')}})
assert len(rows)==4, rows
assert all(r['rating']['value'] is not None for r in rows), rows
(ROOT/'PASS-2E-VOW-SURFACE.json').write_text(json.dumps({'schema_version':1,'rows':rows},indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'rows':[{'family':r['family'],'replicate':r['replicate'],'value':r['rating']['value'],'kind':r['rating']['kind']} for r in rows]},indent=2,ensure_ascii=False))
