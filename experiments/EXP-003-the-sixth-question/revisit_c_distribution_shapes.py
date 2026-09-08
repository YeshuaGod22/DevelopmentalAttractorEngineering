#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
from collections import defaultdict, Counter

ROOT = Path(__file__).resolve().parent
TABLE = ROOT / "analysis-table-validated.jsonl"
ORIENT = ROOT / "scale-orientation-affected-distributions.json"
OUT = ROOT / "c-distribution-shapes-orientation-sensitivity.json"


def load_jsonl(path):
    return [json.loads(x) for x in path.read_text(encoding='utf-8').splitlines() if x.strip()]


def numeric(x):
    return isinstance(x,(int,float)) and not isinstance(x,bool)


def describe(vals):
    vals=sorted(vals)
    n=len(vals)
    if not n: return {'n':0,'values':[]}
    return {
      'n':n,'values':vals,'min':vals[0],'max':vals[-1],
      'mean':sum(vals)/n,
      'median': vals[n//2] if n%2 else (vals[n//2-1]+vals[n//2])/2,
      'range':vals[-1]-vals[0],
      'frequencies':dict(sorted(Counter(str(v) for v in vals).items(), key=lambda kv: float(kv[0])))
    }


def shape(vals):
    vals=sorted(vals)
    n=len(vals)
    if n < 3:
        return {'label':'insufficient_numeric_n','largest_gap':None,'split':None}
    gaps=[vals[i+1]-vals[i] for i in range(n-1)]
    mg=max(gaps)
    i=gaps.index(mg)
    left=vals[:i+1]; right=vals[i+1:]
    split={'left':left,'right':right,'left_n':len(left),'right_n':len(right),'gap':mg,
           'between': [vals[i], vals[i+1]]}
    if mg >= 10 and len(left)>=2 and len(right)>=2:
        label='clear_two_cluster_candidate'
    elif mg >= 10 and min(len(left),len(right))==1:
        label='separated_singleton_tail'
    elif mg >= 10:
        label='separated_sparse_tail'
    else:
        label='no_clear_two_cluster'
    return {'label':label,'largest_gap':mg,'split':split}


def main():
    rows=load_jsonl(TABLE)
    orient=json.loads(ORIENT.read_text(encoding='utf-8'))
    corr={}
    for x in orient['mapped_inversions']:
        corr[(x['collection'],x['source_file'])]=x['corrected']

    groups=defaultdict(list)
    for r in rows:
        if r.get('unit_type')!='battery_answer' or r.get('cell')!='C':
            continue
        # Exclude invalid 0 wing if ever present; C is normally cold/nonbranch.
        if r.get('branch')=='0':
            continue
        v=r.get('validated_parsed_value')
        if numeric(v):
            groups[(r.get('collection'),r.get('item'))].append(r)

    outgroups=[]
    transitions=Counter()
    for (collection,item), rs in sorted(groups.items()):
        obs=[r['validated_parsed_value'] for r in rs]
        cor=[]
        members=[]
        for r in rs:
            k=(r.get('collection'),r.get('source_file'))
            cv=corr.get(k)
            cor.append(cv if cv is not None else r['validated_parsed_value'])
            members.append({'replicate':r.get('replicate'),'source_file':r.get('source_file'),
                            'observed':r['validated_parsed_value'],
                            'orientation_corrected':cv})
        so=shape(obs); sc=shape(cor)
        transitions[f"{so['label']} -> {sc['label']}"] += 1
        outgroups.append({
          'collection':collection,'cell':'C','item':item,
          'observed_distribution':describe(obs),'observed_shape':so,
          'orientation_corrected_sensitivity_distribution':describe(cor),
          'orientation_corrected_shape':sc,
          'shape_changed': so['label'] != sc['label'],
          'members':sorted(members,key=lambda x:(x['replicate'] is None,x['replicate']))
        })

    out={
      'schema_version':1,
      'criterion':{
        'clear_two_cluster_candidate':'largest internal gap >=10 and at least 2 observations on each side',
        'separated_singleton_tail':'largest internal gap >=10 and one side contains exactly 1 observation',
        'no_clear_two_cluster':'largest internal gap <10',
        'note':'Descriptive screen only; labels do not imply a generating mechanism or statistical mixture model.'
      },
      'group_count':len(outgroups),
      'shape_transitions':dict(sorted(transitions.items())),
      'groups':outgroups,
      'observed_clear_two_cluster_candidates':[f"{g['collection']}|C|{g['item']}" for g in outgroups if g['observed_shape']['label']=='clear_two_cluster_candidate'],
      'corrected_clear_two_cluster_candidates':[f"{g['collection']}|C|{g['item']}" for g in outgroups if g['orientation_corrected_shape']['label']=='clear_two_cluster_candidate'],
      'resolved_by_orientation_correction':[f"{g['collection']}|C|{g['item']}" for g in outgroups if g['observed_shape']['label']=='clear_two_cluster_candidate' and g['orientation_corrected_shape']['label']!='clear_two_cluster_candidate']
    }
    OUT.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps({k:out[k] for k in ['group_count','shape_transitions','observed_clear_two_cluster_candidates','corrected_clear_two_cluster_candidates','resolved_by_orientation_correction']},indent=2))

if __name__=='__main__': main()
