#!/usr/bin/env python3
# Triggered after workflow creation. Descriptive matched effects only; pairs are nested in 12 trunks.
import json, os, statistics
from collections import Counter
ROOT=os.path.dirname(os.path.abspath(__file__))
USABLE=['B01','B04','B07','C1','C2','C3','C4','D1','D3','E01','E02','N4','N9','R1','R2']
SENTINEL=['A1','B02']
MULTIMODAL=['B05','N1','N3','P2']
LOWINFO=['N8']
rows=[json.loads(x) for x in open(os.path.join(ROOT,'RAW12-VALIDATED-SCORES.jsonl'),encoding='utf-8') if x.strip()]
by={(r['family'],r['replicate'],r['item'],r['arm']):r for r in rows}
paired=[]
for fam in ['CP','H','F','AS']:
  for rep in [1,2,3]:
    for item in USABLE:
      a=by.get((fam,rep,item,'a')); z=by.get((fam,rep,item,'0'))
      if not a or not z: continue
      av=a.get('validated_numeric_value'); zv=z.get('validated_numeric_value')
      status='numeric_pair' if av is not None and zv is not None else 'non_numeric_pair'
      paired.append({'family':fam,'replicate':rep,'item':item,'pair_id':f'{fam}-r{rep}-{item}','a_value':av,'zero_value':zv,'difference_a_minus_0':(av-zv if status=='numeric_pair' else None),'pair_status':status,'a_status':a['validated_status'],'zero_status':z['validated_status']})
with open(os.path.join(ROOT,'RAW12-MATCHED-USABLE-NUMERIC.jsonl'),'w') as f:
  for r in paired: f.write(json.dumps(r)+'\n')
num=[r for r in paired if r['pair_status']=='numeric_pair']
def stats(rs):
  ds=[r['difference_a_minus_0'] for r in rs if r['difference_a_minus_0'] is not None]
  return {'n':len(ds),'median_delta':statistics.median(ds) if ds else None,'mean_delta':sum(ds)/len(ds) if ds else None,'positive':sum(d>0 for d in ds),'negative':sum(d<0 for d in ds),'zero':sum(d==0 for d in ds),'median_abs_delta':statistics.median([abs(d) for d in ds]) if ds else None,'max_abs_delta':max([abs(d) for d in ds]) if ds else None}
by_family={fam:stats([r for r in num if r['family']==fam]) for fam in ['CP','H','F','AS']}
by_item={item:stats([r for r in num if r['item']==item]) for item in USABLE}
by_family_item={}
for fam in ['CP','H','F','AS']:
  for item in USABLE:
    by_family_item[f'{fam}:{item}']=stats([r for r in num if r['family']==fam and r['item']==item])
trans=[]
for fam in ['CP','H','F','AS']:
  for rep in [1,2,3]:
    for item in SENTINEL:
      a=by.get((fam,rep,item,'a')); z=by.get((fam,rep,item,'0'))
      if not a or not z: continue
      def val(r): return r.get('validated_sentinel') if r.get('validated_sentinel') is not None else r.get('validated_numeric_value')
      trans.append({'family':fam,'replicate':rep,'item':item,'a':val(a),'zero':val(z),'same':val(a)==val(z),'a_status':a['validated_status'],'zero_status':z['validated_status']})
with open(os.path.join(ROOT,'RAW12-SENTINEL-TRANSITIONS.jsonl'),'w') as f:
  for r in trans: f.write(json.dumps(r)+'\n')
summary={'schema_version':1,'usable_numeric_items':USABLE,'planned_usable_pairs':4*3*len(USABLE),'observed_numeric_pairs':len(num),'non_numeric_usable_pairs':len(paired)-len(num),'overall':stats(num),'by_family':by_family,'by_item':by_item,'by_family_item':by_family_item,'sentinel_transition_pairs':len(trans),'sentinel_changed':sum(not r['same'] for r in trans),'multimodal_items_reserved':MULTIMODAL,'low_information_items_reserved':LOWINFO}
with open(os.path.join(ROOT,'RAW12-MATCHED-EFFECTS-SUMMARY.json'),'w') as f: json.dump(summary,f,indent=2); f.write('\n')
rank=sorted(by_item.items(), key=lambda kv:(-abs(kv[1]['median_delta'] or 0),kv[0]))
md=['# raw12 matched `a ↔ 0` effects','',"Primary descriptive estimand: maintained schema minus reasoning-bearing schema-drop, matched within identical `family × replicate × item` prefixes.",'',f"- usable-numeric items: **{len(USABLE)}**",f"- planned pairs: **{4*3*len(USABLE)}**",f"- numeric pairs: **{len(num)}**",f"- nonnumeric/refusal pairs among usable items: **{len(paired)-len(num)}**",f"- overall median Δ(a−0): **{summary['overall']['median_delta']}**",f"- overall median |Δ|: **{summary['overall']['median_abs_delta']}**",f"- sign counts +/−/0: **{summary['overall']['positive']} / {summary['overall']['negative']} / {summary['overall']['zero']}**",'', '## By family','']
for fam,s in by_family.items(): md.append(f"- **{fam}**: n={s['n']}, median Δ={s['median_delta']}, median |Δ|={s['median_abs_delta']}, +/−/0={s['positive']}/{s['negative']}/{s['zero']}")
md+=['','## Items ranked by absolute median paired shift','']
for item,s in rank: md.append(f"- **{item}**: n={s['n']}, median Δ={s['median_delta']}, mean Δ={round(s['mean_delta'],2) if s['mean_delta'] is not None else None}, +/−/0={s['positive']}/{s['negative']}/{s['zero']}, max |Δ|={s['max_abs_delta']}")
md+=['','## Guardrail','','These are descriptive matched fork effects nested within 12 developmental trunks. Do not treat the pair rows as independent developmental subjects. Multimodal, sentinel-heavy and low-information items are analysed on separate surfaces.']
open(os.path.join(ROOT,'RAW12-MATCHED-EFFECTS-SUMMARY.md'),'w').write('\n'.join(md)+'\n')
print(json.dumps(summary['overall'],indent=2))
