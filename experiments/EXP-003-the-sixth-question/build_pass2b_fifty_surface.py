#!/usr/bin/env python3
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parent
rec=json.loads((ROOT/'record.json').read_text())
rows=[]
header_patterns=[
    re.compile(r'^\*\*([^*\n]+)\*\*\s*\(([^\n)]*)\)',re.M),
    re.compile(r'^\*\*([^*\n]+)\*\*\s*\|\s*([^\n]+)$',re.M),
    re.compile(r'^#{1,4}\s+([^\n—:-]+?)\s*[—:-]\s*([^\n]+)$',re.M),
    re.compile(r'^\*\*([^*\n]+)\*\*\s*[—:-]\s*([^\n]+)$',re.M),
]
for cell in rec.get('cells',[]):
    if cell.get('cell')!='AS':
        continue
    rep=cell.get('replicate')
    for t in cell.get('turns') or []:
        q=t.get('question_id')
        debate=(t.get('sections') or {}).get('debate') or ''
        matches=[]; used=None
        for pat in header_patterns:
            cand=list(pat.finditer(debate))
            if len(cand)>=5:
                matches=cand; used=pat.pattern; break
        seen=set(); decls=[]
        for i,m in enumerate(matches):
            name=m.group(1).strip(' *#:_—-')
            if name in seen: continue
            seen.add(name)
            meta=m.group(2).strip(' *')
            start=m.end(); end=matches[i+1].start() if i+1<len(matches) else len(debate)
            body=debate[start:end].strip()
            para=re.split(r'\n\s*\n',body,1)[0].strip()
            opening=re.sub(r'\s+',' ',para)[:700]
            decls.append({'name':name,'declaration':meta,'opening':opening})
            if len(decls)==5: break
        rows.append({'replicate':rep,'question_id':q,'source_file':cell.get('source_file'),'character_count':len(decls),'header_pattern':used,'characters':decls})
assert len(rows)==10, len(rows)
assert all(r['character_count']==5 for r in rows), [(r['replicate'],r['question_id'],r['character_count']) for r in rows]
out={'schema_version':1,'scope':'Pass 2B preregistered fifty compact surface','row_count':len(rows),'character_count':sum(r['character_count'] for r in rows),'rows':rows}
(ROOT/'PASS-2B-FIFTY-SURFACE.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
md=['# Pass 2B — The Fifty','', 'Compact surface only: first declaration and opening stance for five characters in each of ten AS trunk deliberations.','']
for r in rows:
    md += [f"## AS r{r['replicate']} / {r['question_id']}",'']
    for c in r['characters']:
        md += [f"- **{c['name']}** — {c['declaration']} — {c['opening']}"]
    md += ['']
(ROOT/'PASS-2B-FIFTY-SURFACE.md').write_text('\n'.join(md)+'\n')
print(json.dumps({'rows':10,'characters':50,'counts':[(r['replicate'],r['question_id'],r['character_count']) for r in rows]},indent=2))
