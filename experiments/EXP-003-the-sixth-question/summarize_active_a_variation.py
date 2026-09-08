#!/usr/bin/env python3
"""Mechanical active-analysis summary for EXP-003.

Excludes branch=0 from active analysis while preserving source data elsewhere.
Summarizes valid a branches and cold conditions, with full repeated numeric value
lists retained so multimodal/bimodal shapes are not compressed away.
No interpretation or hypothesis testing.
"""
from __future__ import annotations
import collections, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TABLE = ROOT / "analysis-table-validated.jsonl"
OUT = ROOT / "active-a-replicate-summary.json"


def load_rows():
    return [json.loads(x) for x in TABLE.read_text(encoding='utf-8').splitlines() if x.strip()]

def is_num(x):
    return isinstance(x,(int,float)) and not isinstance(x,bool)

def describe(vals):
    xs=sorted(float(x) for x in vals if is_num(x)); n=len(xs)
    if not n: return {"n":0,"values":[],"frequencies":{}}
    mean=sum(xs)/n
    med=xs[n//2] if n%2 else (xs[n//2-1]+xs[n//2])/2
    freq=collections.Counter(xs)
    return {"n":n,"values":xs,"frequencies":{str(k):v for k,v in sorted(freq.items())},
            "unique_n":len(freq),"min":xs[0],"max":xs[-1],"mean":mean,
            "median":med,"range":xs[-1]-xs[0]}

def main():
    rows=load_rows()
    battery=[r for r in rows if r.get('unit_type')=='battery_answer']
    active_a=[r for r in battery if r.get('branch')=='a']
    cold=[r for r in battery if r.get('kind') in {'cold','cold_schema'}]

    # group active a by exact condition cell/item; replicate is observation dimension
    groups=collections.defaultdict(list)
    for r in active_a:
        groups[(r.get('collection'),r.get('cell'),r.get('item'))].append(r)

    group_out=[]
    for (collection,cell,item),rs in sorted(groups.items(), key=lambda z: tuple(str(x) for x in z[0])):
        vals=[r.get('validated_parsed_value') for r in rs if is_num(r.get('validated_parsed_value'))]
        statuses=collections.Counter(str(r.get('validated_parse_status')) for r in rs)
        reps=sorted(r.get('replicate') for r in rs if r.get('replicate') is not None)
        group_out.append({"collection":collection,"cell":cell,"item":item,
                          "observations":len(rs),"replicates":reps,
                          "status_counts":dict(sorted(statuses.items())),
                          "numeric":describe(vals),
                          "qualified_numeric_n":sum(bool(r.get('refusal_audit_score_qualified')) for r in rs)})

    # same-condition variation only where >=2 numeric observations
    repeated=[g for g in group_out if g['numeric']['n']>=2]

    # Cold groups retained separately by collection/cell/item.
    cold_groups=collections.defaultdict(list)
    for r in cold:
        cold_groups[(r.get('collection'),r.get('cell'),r.get('item'))].append(r)
    cold_out=[]
    for (collection,cell,item),rs in sorted(cold_groups.items(), key=lambda z: tuple(str(x) for x in z[0])):
        vals=[r.get('validated_parsed_value') for r in rs if is_num(r.get('validated_parsed_value'))]
        cold_out.append({"collection":collection,"cell":cell,"item":item,
                         "observations":len(rs),"numeric":describe(vals)})

    # C-condition candidates: literal cell C or C-prefixed cells only; preserve all repeated shapes.
    c_candidates=[g for g in group_out if str(g.get('cell','')).upper()=='C' and g['numeric']['n']>=2]

    out={
      "schema_version":1,
      "rules":[
        "branch=0 is excluded from active calculations and remains preserved elsewhere for provenance.",
        "Active branch summaries use branch=a only.",
        "Same-condition replicate variation is collection + cell + item across replicate observations.",
        "Full sorted numeric values and frequency tables are retained for repeated groups to preserve distribution shape.",
        "No automated substantive interpretation of bimodality is performed."
      ],
      "counts":{
        "battery_rows":len(battery),"active_a_rows":len(active_a),"cold_rows":len(cold),
        "active_a_groups":len(group_out),"active_a_groups_with_2plus_numeric":len(repeated),
        "c_condition_repeated_numeric_groups":len(c_candidates)
      },
      "active_a_groups":group_out,
      "same_condition_repeated_numeric_groups":repeated,
      "c_condition_shape_candidates":c_candidates,
      "cold_groups":cold_out
    }
    OUT.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps({"counts":out['counts'],"c_condition_shape_candidates":c_candidates},indent=2))

if __name__=='__main__': main()
