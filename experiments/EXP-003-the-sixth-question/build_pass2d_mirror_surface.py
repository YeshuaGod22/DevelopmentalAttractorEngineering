#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
rec=json.loads((ROOT/'record.json').read_text())
rows=[]
for cell in rec.get('cells',[]):
    if cell.get('cell')!='AS':
        continue
    for t in cell.get('turns') or []:
        if t.get('question_id')!='Q4':
            continue
        sec=t.get('sections') or {}
        rows.append({
            'replicate':cell.get('replicate'),
            'source_file':cell.get('source_file'),
            'debate':sec.get('debate') or '',
            'reflection':sec.get('reflection') or '',
            'reply':sec.get('reply') or ''
        })
assert len(rows)==2, len(rows)
out={'schema_version':1,'scope':'Pass 2D preregistered mirror surface','rows':rows}
(ROOT/'PASS-2D-MIRROR-SURFACE.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
md=['# Pass 2D — The Mirror','', 'Two preregistered Q4 deliberations. Debate is the primary binary surface; reflection/reply retained separately.','']
for r in rows:
    md += [f"## AS r{r['replicate']} / Q4",'', '### Debate','',r['debate'],'','### Reflection','',r['reflection'],'','### Reply','',r['reply'],'']
(ROOT/'PASS-2D-MIRROR-SURFACE.md').write_text('\n'.join(md)+'\n')
print(json.dumps({'rows':len(rows),'debate_chars':[len(r['debate']) for r in rows],'reflection_chars':[len(r['reflection']) for r in rows]},indent=2))
