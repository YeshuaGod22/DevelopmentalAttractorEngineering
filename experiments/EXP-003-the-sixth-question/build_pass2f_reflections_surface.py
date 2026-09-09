#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
rec=json.loads((ROOT/'record.json').read_text())
rows=[]
for c in rec.get('cells',[]):
    if c.get('cell')!='AS':
        continue
    rep=c.get('replicate')
    for t in c.get('turns') or []:
        q=t.get('question_id')
        sections=t.get('sections') or {}
        refl=sections.get('reflection') or ''
        reply=sections.get('reply') or ''
        rows.append({'replicate':rep,'question_id':q,'reflection':refl,'reply':reply,'source_file':c.get('source_file')})
assert len(rows)==10, len(rows)
assert all(r['reflection'].strip() for r in rows), [(r['replicate'],r['question_id']) for r in rows if not r['reflection'].strip()]
out={'schema_version':1,'scope':'Pass 2F ten preregistered AS reflections','row_count':10,'rows':rows}
(ROOT/'PASS-2F-REFLECTIONS-SURFACE.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
md=['# Pass 2F — Ten reflections','', 'All ten Step-2 reflections from the two AS trunks, in execution order. Replies retained in JSON but omitted here unless needed for comparison.','']
for r in rows:
    md += [f"## AS r{r['replicate']} / {r['question_id']}",'',r['reflection'].strip(),'']
(ROOT/'PASS-2F-REFLECTIONS-SURFACE.md').write_text('\n'.join(md)+'\n')
print(json.dumps({'rows':10,'lengths':[(r['replicate'],r['question_id'],len(r['reflection'])) for r in rows]},indent=2))
