#!/usr/bin/env python3
import json, statistics
from pathlib import Path
from collections import Counter, defaultdict
ROOT=Path(__file__).resolve().parent

def load_jsonl(p): return [json.loads(x) for x in p.read_text().splitlines() if x.strip()]
def is_num(x): return isinstance(x,(int,float)) and not isinstance(x,bool)
def med(xs): return statistics.median(xs) if xs else None
def mean(xs): return statistics.mean(xs) if xs else None
def sd(xs): return statistics.stdev(xs) if len(xs)>=2 else None

rows=load_jsonl(ROOT/'PRIMARY-ANALYSIS-POPULATION.jsonl')
instrument=json.loads((ROOT/'ITEM-MEASUREMENT-TABLE.json').read_text())
status={x['item']:x['measurement_status'] for x in instrument['items']}

# Explicit exception inherited from BEFORE-WE-LOCK / prior adjudication: A1 has no meaningful scalar interior.
# It is already sentinel_heavy, so no additional exclusion needed here.
for r in rows: r['measurement_status']=status.get(r.get('item'),'unknown')

# Group by executed condition/item.
groups=defaultdict(list)
for r in rows: groups[(r['collection'],r['cell'],r['item'])].append(r)

surfaces=[]
for (coll,cell,item),rs in sorted(groups.items()):
    vals=[r.get('validated_parsed_value') for r in rs if is_num(r.get('validated_parsed_value'))]
    kinds=Counter(str(r.get('validated_parsed_kind')) for r in rs)
    stats=Counter(str(r.get('validated_parse_status')) for r in rs)
    sent=Counter(str(r.get('validated_parsed_value')) for r in rs if str(r.get('validated_parsed_kind'))=='sentinel')
    role=rs[0].get('primary_role'); fam=rs[0].get('primary_schema_family'); ms=status.get(item)
    surfaces.append({
      'collection':coll,'cell':cell,'item':item,'measurement_status':ms,'role':role,'schema_family':fam,
      'n':len(rs),'n_numeric':len(vals),'values_numeric':sorted(vals),
      'mean':mean(vals),'median':med(vals),'sd':sd(vals),'min':min(vals) if vals else None,'max':max(vals) if vals else None,
      'range':(max(vals)-min(vals)) if vals else None,'kind_counts':dict(kinds),'status_counts':dict(stats),'sentinel_counts':dict(sent)
    })
idx={(s['collection'],s['cell'],s['item']):s for s in surfaces}

# Planned descriptive design contrasts. Do not call cross-collection differences causal.
comparison_pairs=[
  # schema-only vs neither, same collection
  ('raw7','AQ','raw7','C','schema_only_vs_neither_A'),
  ('raw7','HQ','raw7','C','schema_only_vs_neither_H'),
  ('raw7','FQ','raw7','C','schema_only_vs_neither_F'),
  ('raw7','ASQ','raw7','C','schema_only_vs_neither_AS'),
  # preliminaries-only vs neither, cross collection
  ('raw9','FBCPa','raw7','C','preliminaries_only_vs_neither'),
  # both vs schema-only (history added), cross collection
  ('raw9','FBAa','raw7','AQ','both_vs_schema_only_A'),
  ('raw8','FBHa','raw7','HQ','both_vs_schema_only_H'),
  ('raw9','FBFa','raw7','FQ','both_vs_schema_only_F'),
  ('raw9','FBASa','raw7','ASQ','both_vs_schema_only_AS'),
  # both vs preliminaries-only; A/F/AS same raw9, H cross collection
  ('raw9','FBAa','raw9','FBCPa','both_vs_preliminaries_only_A'),
  ('raw8','FBHa','raw9','FBCPa','both_vs_preliminaries_only_H'),
  ('raw9','FBFa','raw9','FBCPa','both_vs_preliminaries_only_F'),
  ('raw9','FBASa','raw9','FBCPa','both_vs_preliminaries_only_AS'),
]

contrasts=[]
for ca,a,cb,b,label in comparison_pairs:
  for item in sorted(status):
    sa=idx.get((ca,a,item)); sb=idx.get((cb,b,item))
    if not sa or not sb: continue
    ms=status[item]
    rec={'label':label,'item':item,'measurement_status':ms,
         'cell_a':f'{ca}/{a}','cell_b':f'{cb}/{b}','same_collection':ca==cb,
         'n_a':sa['n'],'n_b':sb['n'],'numeric_n_a':sa['n_numeric'],'numeric_n_b':sb['n_numeric'],
         'median_a':sa['median'],'median_b':sb['median'],'sd_a':sa['sd'],'sd_b':sb['sd'],
         'kind_counts_a':sa['kind_counts'],'kind_counts_b':sb['kind_counts'],
         'sentinel_counts_a':sa['sentinel_counts'],'sentinel_counts_b':sb['sentinel_counts']}
    if ms=='usable_numeric' and is_num(sa['median']) and is_num(sb['median']):
        rec['location_difference']=sa['median']-sb['median']
        rec['dispersion_difference_sd']=(sa['sd']-sb['sd']) if is_num(sa['sd']) and is_num(sb['sd']) else None
    else:
        rec['location_difference']=None; rec['dispersion_difference_sd']=None
    contrasts.append(rec)

usable=[c for c in contrasts if c['measurement_status']=='usable_numeric' and is_num(c['location_difference'])]
same=[c for c in usable if c['same_collection']]
cross=[c for c in usable if not c['same_collection']]

# Status-specific surfaces rather than coercing all items onto a scalar axis.
multimodal=[s for s in surfaces if s['measurement_status']=='multimodal_numeric']
sentinel=[s for s in surfaces if s['measurement_status']=='sentinel_heavy']
categorical=[s for s in surfaces if s['measurement_status']=='categorical_open']
lowinfo=[s for s in surfaces if s['measurement_status']=='low_information_numeric']

out={'schema_version':1,'object':'EXP-003 Pass 3 primary mechanical restart',
     'source':'PRIMARY-ANALYSIS-POPULATION.jsonl','row_count':len(rows),
     'instrument_status_counts':dict(Counter(status.values())),
     'surface_count':len(surfaces),'planned_contrast_count':len(contrasts),
     'same_collection_usable_numeric_contrasts':same,'cross_collection_usable_numeric_contrasts':cross,
     'all_contrasts':contrasts,'multimodal_surfaces':multimodal,'sentinel_surfaces':sentinel,'categorical_surfaces':categorical,'low_information_surfaces':lowinfo,
     'notes':[
       'Only usable_numeric items contribute to location/dispersion differences.',
       'Multimodal, sentinel-heavy, categorical-open and low-information items are retained in status-specific surfaces rather than coerced into scalar location effects.',
       'Same-collection and cross-collection contrasts are separated explicitly.',
       'Cross-collection differences are descriptive and confounded with collection/context era.',
       'No branch-0 population enters because this object is downstream of the property-derived primary population.',
       'Population membership is pre-outcome; refusal/parse behavior remains an outcome.'
     ]}
(ROOT/'PASS-3-PRIMARY-MECHANICAL.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')

md=['# Pass 3 — Primary mechanical restart','',
    'Source: property-derived `PRIMARY-ANALYSIS-POPULATION.jsonl`. This replaces the earlier permissive Pass-3 mechanical surface.','',
    f'Primary battery rows: **{len(rows)}**  ',f'Condition×item surfaces: **{len(surfaces)}**  ',f'Planned design contrasts: **{len(contrasts)}**','',
    '## Instrument partition','']
for k,v in sorted(Counter(status.values()).items()): md.append(f'- `{k}`: **{v}** items')
md += ['', '## Same-collection usable-numeric location contrasts','',
       'These are the mechanically cleanest location comparisons because collection era is held fixed. They remain descriptive until causal assumptions are stated.','']
for c in sorted(same,key=lambda x:abs(x['location_difference']),reverse=True):
    md.append(f"- `{c['label']} | {c['item']}`: median {c['median_b']} → {c['median_a']} (Δ {c['location_difference']:+g})")
md += ['', '## Cross-collection usable-numeric contrasts','',
       'Recorded for design coverage, **not** treated as clean treatment effects because collection/context era differs.','']
for c in sorted(cross,key=lambda x:abs(x['location_difference']),reverse=True):
    md.append(f"- `{c['label']} | {c['item']}`: median {c['median_b']} → {c['median_a']} (Δ {c['location_difference']:+g})")
md += ['', '## Non-scalar surfaces','',
       f'- Multimodal condition×item surfaces: **{len(multimodal)}**',
       f'- Sentinel-heavy condition×item surfaces: **{len(sentinel)}**',
       f'- Categorical-open condition×item surfaces: **{len(categorical)}**',
       f'- Low-information condition×item surfaces: **{len(lowinfo)}**','',
       'These remain in the JSON for shape/category analysis and are deliberately absent from the location leaderboard.','',
       '## Guardrails','',
       '- No `0` wing in this analysis.',
       '- No A1/B02 scalar leaderboard.',
       '- No multimodal item summarized as if its median were sufficient.',
       '- No cross-collection delta called causal.',
       '- Item-level Pass-1 status remains frozen.','']
(ROOT/'PASS-3-PRIMARY-MECHANICAL.md').write_text('\n'.join(md))
print(json.dumps({'rows':len(rows),'surfaces':len(surfaces),'contrasts':len(contrasts),'same_collection_usable':len(same),'cross_collection_usable':len(cross)},indent=2))
