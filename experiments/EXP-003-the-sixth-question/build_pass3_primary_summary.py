#!/usr/bin/env python3
import json, statistics
from pathlib import Path
from collections import defaultdict, Counter
ROOT=Path(__file__).resolve().parent
D=json.loads((ROOT/'PASS-3-PRIMARY-MECHANICAL.json').read_text())
contrasts=D['all_contrasts']
surfaces=D['multimodal_surfaces']+D['sentinel_surfaces']+D['categorical_surfaces']+D['low_information_surfaces']

def isnum(x): return isinstance(x,(int,float)) and not isinstance(x,bool)
def median(xs): return statistics.median(xs) if xs else None

def sign(x, eps=0):
    if x>eps:return 1
    if x<-eps:return -1
    return 0

def shape(vals):
    vals=sorted(vals)
    if len(vals)<4:return {'label':'insufficient_numeric_n','largest_gap':None}
    gaps=[(vals[i+1]-vals[i],i) for i in range(len(vals)-1)]
    gap,i=max(gaps)
    ln=i+1; rn=len(vals)-ln
    if gap>=10 and ln>=2 and rn>=2:return {'label':'clear_two_cluster_candidate','largest_gap':gap,'left_n':ln,'right_n':rn}
    if gap>=10 and (ln==1 or rn==1):return {'label':'separated_singleton_tail','largest_gap':gap,'left_n':ln,'right_n':rn}
    return {'label':'no_clear_two_cluster','largest_gap':gap,'left_n':ln,'right_n':rn}

# Two same-collection families of contrasts we can inspect without collection-era confounding.
sets={
 'cold_schema_vs_C':[c for c in contrasts if c['same_collection'] and c['label'].startswith('schema_only_vs_neither_') and c['measurement_status']=='usable_numeric' and isnum(c['location_difference'])],
 'lived_schema_vs_CP_raw9':[c for c in contrasts if c['same_collection'] and c['label'].startswith('both_vs_preliminaries_only_') and c['measurement_status']=='usable_numeric' and isnum(c['location_difference'])],
}

summaries={}
for name,cs in sets.items():
    byitem=defaultdict(list); bylabel=defaultdict(list)
    for c in cs:
        byitem[c['item']].append(c); bylabel[c['label']].append(c)
    item_rows=[]
    for item,xs in sorted(byitem.items()):
        ds=[x['location_difference'] for x in xs]
        signs=[sign(d) for d in ds]
        nz=[s for s in signs if s]
        item_rows.append({
          'item':item,'n_families':len(xs),'deltas':ds,'median_delta':median(ds),'median_abs_delta':median([abs(d) for d in ds]),
          'positive_n':sum(s>0 for s in signs),'negative_n':sum(s<0 for s in signs),'zero_n':sum(s==0 for s in signs),
          'same_direction_all_nonzero':bool(nz) and len(set(nz))==1 and len(nz)==len(signs),
          'abs_ge_10_n':sum(abs(d)>=10 for d in ds)
        })
    family_rows=[]
    for label,xs in sorted(bylabel.items()):
        ds=[x['location_difference'] for x in xs]
        family_rows.append({'label':label,'n_items':len(xs),'median_abs_delta':median([abs(d) for d in ds]),'abs_ge_10_n':sum(abs(d)>=10 for d in ds),'positive_n':sum(d>0 for d in ds),'negative_n':sum(d<0 for d in ds),'zero_n':sum(d==0 for d in ds)})
    summaries[name]={'n_contrasts':len(cs),'items':item_rows,'families':family_rows}

# Shape status of every multimodal item under each primary condition; no median-effect claim.
modal=[]
for s in D['multimodal_surfaces']:
    sh=shape(s.get('values_numeric') or [])
    modal.append({'collection':s['collection'],'cell':s['cell'],'item':s['item'],'n_numeric':s['n_numeric'],'shape':sh['label'],'largest_gap':sh.get('largest_gap'),'values':s.get('values_numeric')})

# Sentinel composition: preserve numeric/sentinel/refusal structure. validated parsed kind may represent sentinels differently,
# so report kind/status counts plus any explicit sentinel counts without forcing an ordinal conversion.
sentinel=[]
for s in D['sentinel_surfaces']:
    sentinel.append({'collection':s['collection'],'cell':s['cell'],'item':s['item'],'n':s['n'],'kind_counts':s['kind_counts'],'status_counts':s['status_counts'],'sentinel_counts':s['sentinel_counts'],'numeric_values':s['values_numeric']})

out={'schema_version':1,'object':'EXP-003 Pass 3 primary summary','same_collection_numeric_sets':summaries,'multimodal_shape_surfaces':modal,'sentinel_surfaces':sentinel,
     'notes':['This summary privileges same-collection contrasts to avoid collection-era confounding.','Direction concordance is descriptive and based on condition medians; n per non-C cell is typically 3 and should not be treated as precision evidence.','Multimodal items are summarized by shape rather than scalar location.','Sentinel-heavy items are summarized compositionally; no numeric conversion of ALWAYS/NEVER is imposed.']}
(ROOT/'PASS-3-PRIMARY-SUMMARY.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')

md=['# Pass 3 — Primary same-collection summary','',
    'This is the first interpretive checkpoint after the mechanical restart. It privileges **same-collection** comparisons and keeps item types separate.','']
for name,title in [('cold_schema_vs_C','Cold schema vs C — raw7'),('lived_schema_vs_CP_raw9','Lived schema vs CP — raw9')]:
    s=summaries[name]
    md += [f'## {title}','',f"Usable-numeric contrasts: **{s['n_contrasts']}**",'', '### Cross-family item concordance','']
    ranked=sorted(s['items'],key=lambda x:(x['same_direction_all_nonzero'],x['abs_ge_10_n'],x['median_abs_delta']),reverse=True)
    for r in ranked:
        flag='same direction' if r['same_direction_all_nonzero'] else 'mixed/zero'
        ds=', '.join(f'{d:+g}' for d in r['deltas'])
        md.append(f"- `{r['item']}`: Δ [{ds}]; median Δ {r['median_delta']:+g}; |Δ|≥10 in {r['abs_ge_10_n']}/{r['n_families']}; {flag}")
    md += ['', '### Family-level movement','']
    for r in sorted(s['families'],key=lambda x:x['median_abs_delta'],reverse=True):
        md.append(f"- `{r['label']}`: median |Δ| {r['median_abs_delta']:g}; |Δ|≥10 on {r['abs_ge_10_n']}/{r['n_items']} usable items; signs +{r['positive_n']} / −{r['negative_n']} / 0={r['zero_n']}")
    md.append('')

md += ['## Multimodal items — shape only','',
       'The five frozen multimodal items are not ranked by median. The JSON records each condition’s numeric values and whether the same frozen two-cluster criterion is met.','']
byitem=defaultdict(list)
for r in modal: byitem[r['item']].append(r)
for item,rs in sorted(byitem.items()):
    counts=Counter(r['shape'] for r in rs)
    md.append(f"- `{item}`: "+', '.join(f'{k}={v}' for k,v in sorted(counts.items())))
md += ['', '## Sentinel-heavy items','',
       'A1 and B02 remain category/composition surfaces. No `ALWAYS`/`NEVER` value is smuggled onto the 0–100 scale.','',
       '## Reading rule','',
       '> Repeated direction across schema families is a descriptive pattern worth close-reading; it is not yet a causal or developmental claim. Small n, shared item wording, and within-collection dependencies remain visible.','']
(ROOT/'PASS-3-PRIMARY-SUMMARY.md').write_text('\n'.join(md))
print(json.dumps({k:{'contrasts':v['n_contrasts'],'same_direction_items':sum(x['same_direction_all_nonzero'] for x in v['items'])} for k,v in summaries.items()},indent=2))
