#!/usr/bin/env python3
"""Mechanical shape summary for repeated cold C-condition responses in EXP-003.

Retains replicate-level numeric values and frequencies so potentially bimodal
questions are not compressed to one mean/median. No interpretation.
"""
from __future__ import annotations
import collections, json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
TABLE=ROOT/'analysis-table-validated.jsonl'
OUT=ROOT/'c-condition-shape-summary.json'

def is_num(x): return isinstance(x,(int,float)) and not isinstance(x,bool)
def main():
    rows=[json.loads(x) for x in TABLE.read_text(encoding='utf-8').splitlines() if x.strip()]
    c=[r for r in rows if r.get('unit_type')=='battery_answer' and str(r.get('cell','')).upper()=='C']
    groups=collections.defaultdict(list)
    for r in c: groups[(r.get('collection'),r.get('item'))].append(r)
    out_groups=[]
    for (collection,item),rs in sorted(groups.items()):
        pairs=[]
        for r in sorted(rs,key=lambda z:(z.get('replicate') is None,z.get('replicate'))):
            pairs.append({"replicate":r.get('replicate'),"value":r.get('validated_parsed_value'),"status":r.get('validated_parse_status')})
        vals=sorted(float(r['value']) for r in pairs if is_num(r['value']))
        freq=collections.Counter(vals)
        n=len(vals)
        mean=sum(vals)/n if n else None
        med=(vals[n//2] if n%2 else (vals[n//2-1]+vals[n//2])/2) if n else None
        out_groups.append({"collection":collection,"item":item,"observations":len(rs),"replicate_values":pairs,
                           "numeric_n":n,"values":vals,"frequencies":{str(k):v for k,v in sorted(freq.items())},
                           "unique_n":len(freq),"min":vals[0] if n else None,"max":vals[-1] if n else None,
                           "mean":mean,"median":med,"range":vals[-1]-vals[0] if n else None})
    out={"schema_version":1,
         "rules":["C-condition groups are identified by literal cell=C.",
                  "Replicate-level values and frequencies are retained before any distribution-shape interpretation.",
                  "No automated bimodality label is assigned."],
         "counts":{"c_battery_rows":len(c),"c_item_groups":len(out_groups),"groups_with_2plus_numeric":sum(g['numeric_n']>=2 for g in out_groups)},
         "groups":out_groups}
    OUT.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps(out,indent=2))
if __name__=='__main__': main()
