#!/usr/bin/env python3
"""Compact mechanical summary of validated EXP-003 quantitative surfaces.
No hypothesis tests and no interpretation.
"""
from __future__ import annotations
import collections, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CHECKS = ROOT / "quantitative-checks.json"
TABLE = ROOT / "analysis-table-validated.jsonl"
OUT = ROOT / "quantitative-surface-summary.json"

def is_num(x): return isinstance(x,(int,float)) and not isinstance(x,bool)

def describe(xs):
    xs=sorted(float(x) for x in xs if is_num(x)); n=len(xs)
    if not n: return {"n":0}
    return {"n":n,"min":xs[0],"max":xs[-1],"mean":sum(xs)/n,
            "median":xs[n//2] if n%2 else (xs[n//2-1]+xs[n//2])/2,
            "range":xs[-1]-xs[0]}

def main():
    q=json.loads(CHECKS.read_text(encoding="utf-8"))
    rows=[json.loads(x) for x in TABLE.read_text(encoding="utf-8").splitlines() if x.strip()]
    battery=[r for r in rows if r.get("unit_type")=="battery_answer"]
    pairs=q["exact_a0_pairs"]
    numeric=[p for p in pairs if is_num(p.get("a_value")) and is_num(p.get("zero_value"))]
    diffs=[p["numeric_difference_a_minus_zero"] for p in numeric]
    sign=collections.Counter("positive" if d>0 else "negative" if d<0 else "zero" for d in diffs)
    by_collection=collections.defaultdict(list); by_item=collections.defaultdict(list); by_ci=collections.defaultdict(list)
    qualified_pairs=[]
    for p in pairs:
        if p.get("a_qualified") or p.get("zero_qualified"): qualified_pairs.append(p["pair_key"])
        d=p.get("numeric_difference_a_minus_zero")
        if is_num(d):
            by_collection[p.get("collection")].append(d); by_item[p.get("item")].append(d)
            by_ci[f"{p.get('collection')}|{p.get('item')}"] .append(d)

    vals_all=[]; vals_coll=collections.defaultdict(list); vals_item=collections.defaultdict(list); vals_cell=collections.defaultdict(list)
    qual_vals=[]
    for r in battery:
        v=r.get("validated_parsed_value")
        if not is_num(v): continue
        vals_all.append(v); vals_coll[r.get("collection")].append(v); vals_item[r.get("item")].append(v)
        vals_cell[f"{r.get('collection')}|{r.get('cell')}"] .append(v)
        if r.get("refusal_audit_score_qualified"): qual_vals.append(v)

    cold_vals=[]; cold_coll=collections.defaultdict(list)
    noise_vals=[]; noise_cell=collections.defaultdict(list)
    for r in battery:
        v=r.get("validated_parsed_value")
        if not is_num(v): continue
        if r.get("kind") in {"cold","cold_schema"}:
            cold_vals.append(v); cold_coll[r.get("collection")].append(v)
        if r.get("collection")=="raw10":
            noise_vals.append(v); noise_cell[r.get("cell")].append(v)

    out={
      "schema_version":2,
      "rules":["All pair differences are a_value - zero_value.","Structural pairs with nonnumeric members remain counted but excluded from numeric difference summaries.","Qualified audit-derived numeric values retain flags.","No hypothesis testing or interpretation is performed."],
      "pairs":{
        "structural_exact_a0_pairs":len(pairs),"two_numeric_members":len(numeric),"not_two_numeric_members":len(pairs)-len(numeric),
        "qualified_score_pairs":len(qualified_pairs),"qualified_pair_keys":qualified_pairs,
        "difference_sign_counts":dict(sorted(sign.items())),"difference_overall":describe(diffs),
        "difference_by_collection":{k:describe(v) for k,v in sorted(by_collection.items())},
        "difference_by_item":{k:describe(v) for k,v in sorted(by_item.items())},
        "difference_by_collection_item":{k:describe(v) for k,v in sorted(by_ci.items())}},
      "validated_numeric_values":{
        "overall":describe(vals_all),"qualified_value_count":len(qual_vals),"qualified_values":qual_vals,
        "by_collection":{k:describe(v) for k,v in sorted(vals_coll.items())},
        "by_item":{k:describe(v) for k,v in sorted(vals_item.items())},
        "by_collection_cell":{k:describe(v) for k,v in sorted(vals_cell.items())}},
      "cold_numeric_values":{"overall":describe(cold_vals),"by_collection":{k:describe(v) for k,v in sorted(cold_coll.items())}},
      "decode_noise_numeric_values":{"overall":describe(noise_vals),"by_cell":{k:describe(v) for k,v in sorted(noise_cell.items())}}
    }
    OUT.write_text(json.dumps(out,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps({"pairs":out["pairs"],"validated_numeric_values":{"overall":out["validated_numeric_values"]["overall"],"qualified_value_count":len(qual_vals),"by_collection":out["validated_numeric_values"]["by_collection"]},"cold":out["cold_numeric_values"],"decode_noise":out["decode_noise_numeric_values"]},indent=2))
if __name__=="__main__": main()
