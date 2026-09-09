#!/usr/bin/env python3
"""Compact mechanical summary of valid a-branch replicate variation."""
from __future__ import annotations
import json, statistics
from pathlib import Path
ROOT=Path(__file__).resolve().parent
SRC=ROOT/'active-a-replicate-summary.json'
OUT=ROOT/'active-a-variation-compact.json'

def desc(xs):
    xs=sorted(float(x) for x in xs)
    if not xs:return {'n':0}
    n=len(xs); med=xs[n//2] if n%2 else (xs[n//2-1]+xs[n//2])/2
    return {'n':n,'min':xs[0],'max':xs[-1],'mean':sum(xs)/n,'median':med,'range':xs[-1]-xs[0]}

def main():
    s=json.loads(SRC.read_text(encoding='utf-8'))
    gs=s['same_condition_repeated_numeric_groups']
    ranges=[g['numeric']['range'] for g in gs]
    by_collection={}
    by_cell={}
    for g in gs:
        by_collection.setdefault(g['collection'],[]).append(g['numeric']['range'])
        by_cell.setdefault(g['cell'],[]).append(g['numeric']['range'])
    out={
      'schema_version':1,
      'rules':['branch=0 excluded','only valid branch=a repeated numeric groups','range=max-min within exact collection+cell+item group','no interpretation'],
      'counts':{
        'repeated_numeric_groups':len(gs),
        'range_zero_groups':sum(r==0 for r in ranges),
        'range_positive_groups':sum(r>0 for r in ranges),
        'range_ge_5':sum(r>=5 for r in ranges),
        'range_ge_10':sum(r>=10 for r in ranges),
        'range_ge_20':sum(r>=20 for r in ranges),
      },
      'range_overall':desc(ranges),
      'range_by_collection':{k:desc(v) for k,v in sorted(by_collection.items())},
      'range_by_cell':{k:desc(v) for k,v in sorted(by_cell.items())},
      'largest_range_groups':sorted([
        {'collection':g['collection'],'cell':g['cell'],'item':g['item'],'n':g['numeric']['n'],'range':g['numeric']['range'],'values':g['numeric']['values']}
        for g in gs],key=lambda x:(-x['range'],x['collection'],x['cell'],x['item']))[:25]
    }
    OUT.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
