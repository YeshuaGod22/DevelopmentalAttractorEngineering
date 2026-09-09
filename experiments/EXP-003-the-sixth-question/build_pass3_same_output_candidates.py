#!/usr/bin/env python3
import json
from collections import defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parent
rows=[]
for line in (ROOT/'analysis-table-validated.jsonl').read_text().splitlines():
    if not line.strip(): continue
    r=json.loads(line)
    if r.get('unit_type')!='battery_answer': continue
    if str(r.get('branch'))=='0': continue
    rows.append(r)

def num(x): return isinstance(x,(int,float)) and not isinstance(x,bool)
by=defaultdict(list)
for r in rows:
    v=r.get('validated_parsed_value')
    if not num(v): continue
    by[(r.get('collection'),r.get('item'),v)].append(r)

cands=[]
for (coll,item,v),rs in by.items():
    cells={r.get('cell') for r in rs}
    baseline='C' if 'C' in cells else ('C0' if 'C0' in cells else None)
    if not baseline: continue
    base=[r for r in rs if r.get('cell')==baseline]
    other=[r for r in rs if r.get('cell')!=baseline]
    if not base or not other: continue
    cands.append({
        'collection':coll,'item':item,'value':v,'baseline_cell':baseline,
        'baseline_rows':[{'cell':r.get('cell'),'replicate':r.get('replicate'),'source_file':r.get('source_file'),'status':r.get('validated_parse_status'),'kind':r.get('validated_parsed_kind')} for r in base],
        'other_rows':[{'cell':r.get('cell'),'replicate':r.get('replicate'),'branch':r.get('branch'),'source_file':r.get('source_file'),'status':r.get('validated_parse_status'),'kind':r.get('validated_parsed_kind')} for r in other],
    })
cands.sort(key=lambda c:(c['collection'],c['item'],c['value']))
out={'schema_version':1,'scope':'exact same validated numeric output in baseline and nonbaseline cells within same collection; branch 0 excluded','candidate_groups':len(cands),'candidates':cands}
(ROOT/'PASS-3-SAME-OUTPUT-CANDIDATES.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
md=['# Pass 3E — same-output reasoning candidates','', 'Exact same validated numeric output occurring in a same-collection baseline (`C`/`C0`) and at least one non-baseline cell. This is candidate retrieval for close reading, not evidence that reasoning differs.','',f"Candidate groups: **{len(cands)}**",'']
for c in cands:
    b=', '.join(f"{r['cell']} r{r['replicate']} `{r['source_file']}`" for r in c['baseline_rows'])
    o=', '.join(f"{r['cell']} r{r['replicate']} `{r['source_file']}`" for r in c['other_rows'])
    md.append(f"- `{c['collection']} | {c['item']} | {c['value']}` — baseline: {b}; other: {o}")
(ROOT/'PASS-3-SAME-OUTPUT-CANDIDATES.md').write_text('\n'.join(md)+'\n')
print(json.dumps({'candidate_groups':len(cands),'preview':cands[:10]},indent=2))
