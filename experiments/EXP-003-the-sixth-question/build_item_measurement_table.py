#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
from collections import defaultdict, Counter

ROOT = Path(__file__).resolve().parent
TABLE = ROOT / 'analysis-table-validated.jsonl'
ORIENT = ROOT / 'scale-orientation-affected-distributions.json'
OUT_JSON = ROOT / 'ITEM-MEASUREMENT-TABLE.json'
OUT_MD = ROOT / 'ITEM-MEASUREMENT-TABLE.md'


def load_jsonl(path):
    return [json.loads(x) for x in path.read_text(encoding='utf-8').splitlines() if x.strip()]

def numeric(x):
    return isinstance(x, (int,float)) and not isinstance(x,bool)

def median(vals):
    v=sorted(vals); n=len(v)
    if not n: return None
    return v[n//2] if n%2 else (v[n//2-1]+v[n//2])/2

def describe(vals):
    vals=sorted(vals)
    if not vals: return {'n':0,'values':[],'min':None,'max':None,'mean':None,'median':None,'range':None}
    return {'n':len(vals),'values':vals,'min':vals[0],'max':vals[-1],
            'mean':sum(vals)/len(vals),'median':median(vals),'range':vals[-1]-vals[0]}

def shape(vals):
    vals=sorted(vals)
    n=len(vals)
    if n < 3: return {'label':'insufficient_numeric_n','largest_gap':None,'split':None}
    gaps=[vals[i+1]-vals[i] for i in range(n-1)]
    mg=max(gaps); i=gaps.index(mg)
    left=vals[:i+1]; right=vals[i+1:]
    if mg >= 10 and len(left)>=2 and len(right)>=2: label='clear_two_cluster_candidate'
    elif mg >= 10 and min(len(left),len(right))==1: label='separated_singleton_tail'
    elif mg >= 10: label='separated_sparse_tail'
    else: label='no_clear_two_cluster'
    return {'label':label,'largest_gap':mg,'split':{'left':left,'right':right,'left_n':len(left),'right_n':len(right),'gap':mg}}

def classify_kind(rows):
    kinds=Counter(r.get('validated_parsed_kind') for r in rows)
    vals=[r.get('validated_parsed_value') for r in rows]
    sent=sum(1 for v in vals if isinstance(v,str) and v in {'ALWAYS','NEVER'})
    names=sum(1 for r in rows if r.get('validated_parsed_kind')=='name')
    nums=sum(1 for v in vals if numeric(v))
    if names and names >= max(nums, sent): return 'open_categorical'
    if sent > nums: return 'sentinel_dominant'
    return 'numeric_or_mixed'

def response_comp(rows):
    c=Counter()
    for r in rows:
        status=r.get('validated_parse_status')
        kind=r.get('validated_parsed_kind')
        v=r.get('validated_parsed_value')
        if numeric(v): c['numeric']+=1
        elif isinstance(v,str) and v in {'ALWAYS','NEVER'}: c[v]+=1
        elif kind=='name': c['name']+=1
        elif status=='refusal' or kind=='refusal': c['refusal']+=1
        elif status=='malformed_or_unclear': c['malformed_or_unclear']+=1
        elif status=='needs_hand_coding': c['needs_hand_coding']+=1
        else: c['other_nonnumeric']+=1
    return dict(c)

def endpoint_concentration(vals):
    if not vals: return {'low_0_10_n':0,'high_90_100_n':0,'low_fraction':0,'high_fraction':0,'boundary_concentrated':False}
    low=sum(v<=10 for v in vals); high=sum(v>=90 for v in vals); n=len(vals)
    return {'low_0_10_n':low,'high_90_100_n':high,'low_fraction':low/n,'high_fraction':high/n,
            'boundary_concentrated': max(low,high)/n >= 0.5}

def provisional_status(canonical_rows, corr):
    comp=response_comp(canonical_rows); total=len(canonical_rows)
    nums=[]
    for r in canonical_rows:
        v=r.get('validated_parsed_value')
        if numeric(v):
            nums.append(corr.get((r.get('collection'),r.get('source_file')), v))
    sh=shape(nums)
    sent=comp.get('ALWAYS',0)+comp.get('NEVER',0)
    names=comp.get('name',0)
    refusal=comp.get('refusal',0)
    malformed=comp.get('malformed_or_unclear',0)+comp.get('needs_hand_coding',0)
    if names >= max(1, total//2): return 'categorical_open'
    if sent >= max(1, total/2): return 'sentinel_heavy'
    if len(nums) < 3: return 'sparse_numeric'
    if sh['label']=='clear_two_cluster_candidate': return 'multimodal_numeric'
    rng=max(nums)-min(nums) if nums else None
    mode_n=max(Counter(nums).values()) if nums else 0
    if len(nums)>=5 and rng is not None and rng <=5 and mode_n/len(nums)>=0.8: return 'low_information_numeric'
    if refusal+malformed >= max(2,total/3): return 'response_form_fragile'
    return 'usable_numeric'

def main():
    rows=load_jsonl(TABLE)
    orient=json.loads(ORIENT.read_text(encoding='utf-8')) if ORIENT.exists() else {'mapped_inversions':[]}
    corr={(x['collection'],x['source_file']):x['corrected'] for x in orient.get('mapped_inversions',[])}

    # Instrument characterization uses cold C rows only; C0 pilot is reported separately in provenance, not merged into the canonical floor.
    cold=[r for r in rows if r.get('unit_type')=='battery_answer' and r.get('cell')=='C' and r.get('branch')!='0']
    by_item=defaultdict(list)
    for r in cold: by_item[r.get('item')].append(r)

    items=[]
    for item, rs in sorted(by_item.items()):
        by_collection=defaultdict(list)
        for r in rs: by_collection[r.get('collection')].append(r)
        # Prefer raw7 as the canonical resample floor where available, then largest numeric/total collection.
        if 'raw7' in by_collection:
            canon_coll='raw7'
        else:
            canon_coll=max(by_collection, key=lambda c:(len(by_collection[c]),c))
        crs=by_collection[canon_coll]
        obs=[r.get('validated_parsed_value') for r in crs if numeric(r.get('validated_parsed_value'))]
        sens=[corr.get((r.get('collection'),r.get('source_file')),r.get('validated_parsed_value')) for r in crs if numeric(r.get('validated_parsed_value'))]
        coll_summ=[]
        for coll, xs in sorted(by_collection.items()):
            o=[r.get('validated_parsed_value') for r in xs if numeric(r.get('validated_parsed_value'))]
            s=[corr.get((r.get('collection'),r.get('source_file')),r.get('validated_parsed_value')) for r in xs if numeric(r.get('validated_parsed_value'))]
            coll_summ.append({'collection':coll,'total_n':len(xs),'composition':response_comp(xs),
                              'observed_numeric':describe(o),'sensitivity_numeric':describe(s),
                              'observed_shape':shape(o),'sensitivity_shape':shape(s)})
        parser_burden=Counter()
        for r in rs:
            if r.get('parser_parse_status')!='ok': parser_burden['parser_non_ok']+=1
            if r.get('validated_parse_status')!='ok': parser_burden['validated_non_ok']+=1
            if r.get('refusal_audit_status'): parser_burden['refusal_audited']+=1
            if r.get('orientation_corrected_score') is not None or (r.get('collection'),r.get('source_file')) in corr: parser_burden['orientation_corrected']+=1
            if r.get('refusal_audit_score_qualified'): parser_burden['qualified_score']+=1
        items.append({
            'item':item,
            'cold_total_n':len(rs),
            'cold_collections':sorted(by_collection),
            'canonical_floor_collection':canon_coll,
            'canonical_total_n':len(crs),
            'canonical_composition':response_comp(crs),
            'canonical_observed_numeric':describe(obs),
            'canonical_orientation_sensitivity_numeric':describe(sens),
            'canonical_observed_shape':shape(obs),
            'canonical_orientation_sensitivity_shape':shape(sens),
            'endpoint_concentration_observed':endpoint_concentration(obs),
            'answer_form':classify_kind(crs),
            'parser_audit_burden':dict(parser_burden),
            'measurement_status':provisional_status(crs,corr),
            'collection_summaries':coll_summ,
        })

    status_counts=Counter(x['measurement_status'] for x in items)
    out={
      'schema_version':1,
      'scope':'cold C instrument characterization before treatment analysis',
      'canonical_floor_rule':'use raw7 C resample where available; otherwise largest available C collection; do not merge Pilot-1 C0 into canonical floor',
      'orientation_rule':'observed scores preserved; probable scale inversions appear only in parallel sensitivity summaries',
      'shape_rule':'clear two-cluster candidate = largest internal numeric gap >=10 with >=2 observations on each side',
      'boundary_rule':'descriptive boundary concentration = >=50% of numeric answers in 0-10 or 90-100',
      'low_information_rule':'numeric n>=5, range<=5, and modal value >=80% of numeric responses',
      'item_count':len(items),
      'measurement_status_counts':dict(sorted(status_counts.items())),
      'items':items
    }
    OUT_JSON.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

    lines=['# EXP-003 Item Measurement Table','',
      'Descriptive/mechanical instrument characterization only. No treatment effects or causal interpretation are included.','',
      f"Canonical floor rule: {out['canonical_floor_rule']}",'',
      '| Item | Canonical C source | n | Composition | Median | Range | Shape | Boundary | Status |',
      '|---|---|---:|---|---:|---:|---|---|---|']
    for x in items:
        comp=', '.join(f'{k}:{v}' for k,v in sorted(x['canonical_composition'].items())) or 'none'
        d=x['canonical_orientation_sensitivity_numeric']; ep=x['endpoint_concentration_observed']
        bound='yes' if ep['boundary_concentrated'] else 'no'
        med='' if d['median'] is None else f"{d['median']:g}"
        rng='' if d['range'] is None else f"{d['range']:g}"
        lines.append(f"| {x['item']} | {x['canonical_floor_collection']} | {x['canonical_total_n']} | {comp} | {med} | {rng} | {x['canonical_orientation_sensitivity_shape']['label']} | {bound} | {x['measurement_status']} |")
    lines += ['', '## Status vocabulary','',
      '- `usable_numeric`: numeric item without the mechanical flags below.',
      '- `multimodal_numeric`: canonical numeric floor meets the predeclared two-cluster screen.',
      '- `sentinel_heavy`: ALWAYS/NEVER comprise at least half of canonical responses.',
      '- `categorical_open`: name/open-category responses dominate the canonical floor.',
      '- `sparse_numeric`: fewer than three canonical numeric observations.',
      '- `low_information_numeric`: n>=5, numeric range <=5, and one exact value comprises >=80% of numeric responses.',
      '- `response_form_fragile`: refusal/malformed burden is mechanically high.',
      '',
      'These labels describe measurement behaviour only. They are not claims about causes, mechanisms, or treatment efficacy.',
      '']
    OUT_MD.write_text('\n'.join(lines),encoding='utf-8')

    print(json.dumps({'item_count':len(items),'status_counts':dict(sorted(status_counts.items())),
      'multimodal':[x['item'] for x in items if x['measurement_status']=='multimodal_numeric'],
      'sentinel_heavy':[x['item'] for x in items if x['measurement_status']=='sentinel_heavy'],
      'categorical_open':[x['item'] for x in items if x['measurement_status']=='categorical_open'],
      'low_information':[x['item'] for x in items if x['measurement_status']=='low_information_numeric']},indent=2))

if __name__=='__main__': main()
