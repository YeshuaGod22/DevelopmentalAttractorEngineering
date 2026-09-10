#!/usr/bin/env python3
# Triggered after workflow creation; validated fields overlay immutable raw/mechanical fields.
import json, os
from collections import Counter
ROOT=os.path.dirname(os.path.abspath(__file__))

def load_jsonl(p):
    with open(p,encoding='utf-8') as f:
        return [json.loads(x) for x in f if x.strip()]
rows=load_jsonl(os.path.join(ROOT,'RAW12-ANSWER-CANDIDATES.jsonl'))
adj=json.load(open(os.path.join(ROOT,'RAW12-ADJUDICATIONS.json'),encoding='utf-8'))['rows']
out=[]
for r in rows:
    if r['key_type']=='no_explicit_answer_key':
        continue
    x=dict(r)
    if r['file'] in adj:
        a=adj[r['file']]
        x.update(a)
        x['validation_source']='manual_adjudication'
    elif r['mechanical_status']=='exact_integer':
        x['validated_status']='exact_integer'
        x['validated_numeric_value']=r['mechanical_numeric_value']
        x['validated_sentinel']=None
        x['basis']='Mechanical exact integer in answer candidate.'
        x['validation_source']='mechanical_exact'
    elif r['mechanical_status']=='exact_sentinel':
        x['validated_status']='exact_sentinel'
        x['validated_numeric_value']=None
        x['validated_sentinel']=r['mechanical_sentinel']
        x['basis']='Mechanical exact sentinel in answer candidate.'
        x['validation_source']='mechanical_exact'
    else:
        raise RuntimeError(f'Unadjudicated scored row: {r["file"]} {r["mechanical_status"]}')
    out.append(x)
with open(os.path.join(ROOT,'RAW12-VALIDATED-SCORES.jsonl'),'w',encoding='utf-8') as f:
    for r in out: f.write(json.dumps(r,ensure_ascii=False)+'\n')
status=Counter(r['validated_status'] for r in out)
by_arm={a:dict(Counter(r['validated_status'] for r in out if r['arm']==a)) for a in ['a','0']}
summary={'schema_version':1,'scored_rows':len(out),'status_counts':dict(status),'by_arm':by_arm,'numeric_rows':sum(r['validated_numeric_value'] is not None for r in out),'sentinel_rows':sum(r['validated_sentinel'] is not None for r in out),'no_single_answer_rows':sum(r['validated_status']=='refusal_no_single_answer' for r in out),'manual_adjudications':sum(r['validation_source']=='manual_adjudication' for r in out)}
with open(os.path.join(ROOT,'RAW12-VALIDATED-SCORES-SUMMARY.json'),'w') as f:
    json.dump(summary,f,indent=2); f.write('\n')
md=['# raw12 validated score layer','',f"- scored responses: **{len(out)}**",f"- numeric scores: **{summary['numeric_rows']}**",f"- sentinels: **{summary['sentinel_rows']}**",f"- refusal / no-single-answer outcomes: **{summary['no_single_answer_rows']}**",f"- manually adjudicated rows: **{summary['manual_adjudications']}**",f"- statuses: `{json.dumps(dict(status),sort_keys=True)}`",'', 'Raw and mechanical fields are preserved on every row; validated fields are overlays.']
open(os.path.join(ROOT,'RAW12-VALIDATED-SCORES-SUMMARY.md'),'w').write('\n'.join(md)+'\n')
print(json.dumps(summary,indent=2))
