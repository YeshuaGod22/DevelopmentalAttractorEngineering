#!/usr/bin/env python3
import json, os, statistics
ROOT=os.path.dirname(os.path.abspath(__file__))
ITEMS=['D1','R1','R2']

def isnum(x): return isinstance(x,(int,float)) and not isinstance(x,bool)
def med(xs):
    xs=[float(x) for x in xs if isnum(x)]
    return statistics.median(xs) if xs else None
def mean(xs):
    xs=[float(x) for x in xs if isnum(x)]
    return sum(xs)/len(xs) if xs else None
# raw7 validated primary rows
r7=[]
for line in open(os.path.join(ROOT,'analysis-table-validated.jsonl'),encoding='utf-8'):
    if not line.strip(): continue
    r=json.loads(line)
    if r.get('unit_type')!='battery_answer' or r.get('collection')!='raw7' or r.get('item') not in ITEMS: continue
    if r.get('cell') not in {'C','AQ','HQ','FQ','ASQ'}: continue
    v=r.get('validated_parsed_value',r.get('parsed_value'))
    if isnum(v): r7.append((r.get('cell'),r.get('item'),float(v)))
# raw12 validated
r12=[json.loads(x) for x in open(os.path.join(ROOT,'RAW12-VALIDATED-SCORES.jsonl'),encoding='utf-8') if x.strip()]
r12=[r for r in r12 if r['item'] in ITEMS and isnum(r.get('validated_numeric_value'))]
out={'schema_version':1,'items':{}}
for item in ITEMS:
    cold={cell:{'n':len([1 for c,i,v in r7 if c==cell and i==item]),'median':med([v for c,i,v in r7 if c==cell and i==item]),'mean':mean([v for c,i,v in r7 if c==cell and i==item])} for cell in ['C','AQ','HQ','FQ','ASQ']}
    arms={arm:{'n':len([r for r in r12 if r['item']==item and r['arm']==arm]),'median':med([r['validated_numeric_value'] for r in r12 if r['item']==item and r['arm']==arm]),'mean':mean([r['validated_numeric_value'] for r in r12 if r['item']==item and r['arm']==arm])} for arm in ['0','a']}
    fam={}
    for family in ['CP','H','F','AS']:
      fam[family]={}
      for arm in ['0','a']:
        xs=[r['validated_numeric_value'] for r in r12 if r['item']==item and r['family']==family and r['arm']==arm]
        fam[family][arm]={'n':len(xs),'median':med(xs),'mean':mean(xs),'values':xs}
    out['items'][item]={'raw7':cold,'raw12_all_families':arms,'raw12_by_family':fam}
with open(os.path.join(ROOT,'RAW12-RAW7-BRIDGE-SUMMARY.json'),'w') as f: json.dump(out,f,indent=2); f.write('\n')
md=['# raw7 ↔ raw12 bridge: D1 / R1 / R2','', 'Cross-era comparison is descriptive only. raw7 and raw12 differ in developmental history and collection era; do not treat absolute differences as a controlled causal estimate.','']
for item,d in out['items'].items():
    md += [f'## {item}','', '### raw7 cold / cold-schema medians','']
    for c,s in d['raw7'].items(): md.append(f"- `{c}`: n={s['n']}, median={s['median']}, mean={round(s['mean'],2) if s['mean'] is not None else None}")
    md += ['','### raw12 arm medians across all 12 trunks','']
    for a,s in d['raw12_all_families'].items(): md.append(f"- `{a}`: n={s['n']}, median={s['median']}, mean={round(s['mean'],2) if s['mean'] is not None else None}")
    md += ['','### raw12 by developmental family','']
    for fam,arms in d['raw12_by_family'].items(): md.append(f"- **{fam}**: 0 median={arms['0']['median']} {arms['0']['values']} | a median={arms['a']['median']} {arms['a']['values']}")
    md.append('')
open(os.path.join(ROOT,'RAW12-RAW7-BRIDGE-SUMMARY.md'),'w').write('\n'.join(md)+'\n')
