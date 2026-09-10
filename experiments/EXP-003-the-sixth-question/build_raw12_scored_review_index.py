#!/usr/bin/env python3
import json, os
ROOT=os.path.dirname(os.path.abspath(__file__))
rows=[json.loads(x) for x in open(os.path.join(ROOT,'RAW12-ANSWER-CANDIDATES.jsonl'),encoding='utf-8') if x.strip()]
review=[r for r in rows if r['key_type']!='no_explicit_answer_key' and r['mechanical_status'] not in {'exact_integer','exact_sentinel'}]
out=[]
for r in review:
    text=' '.join((r.get('candidate_text') or '').split())
    out.append({
      'file':r['file'],'family':r['family'],'replicate':r['replicate'],'item':r['item'],'arm':r['arm'],
      'status':r['mechanical_status'],'candidate_source':r['candidate_source'],'candidate_tag':r.get('candidate_tag'),
      'candidate_numeric_value':r.get('mechanical_numeric_value'),'candidate_sentinel':r.get('mechanical_sentinel'),
      'candidate_excerpt':text[:280]
    })
json.dump(out,open(os.path.join(ROOT,'RAW12-SCORED-REVIEW-INDEX.json'),'w',encoding='utf-8'),indent=2,ensure_ascii=False)
lines=['# raw12 scored review index','']
for i,r in enumerate(out,1):
    lines.append(f"{i}. `{r['file']}` — {r['status']}; source `{r['candidate_source']}/{r['candidate_tag']}`; derived `{r['candidate_numeric_value']}`")
open(os.path.join(ROOT,'RAW12-SCORED-REVIEW-INDEX.md'),'w',encoding='utf-8').write('\n'.join(lines)+'\n')
print(json.dumps(out,indent=2,ensure_ascii=False))
