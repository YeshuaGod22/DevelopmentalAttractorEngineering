#!/usr/bin/env python3
"""Compact mechanical summary of validated EXP-003 quantitative surfaces.

No hypothesis tests and no interpretation. Reads quantitative-checks.json and
emits descriptive counts/ranges for exact a/0 pairs and numeric distributions.
"""
from __future__ import annotations
import collections, json, math
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "quantitative-checks.json"
OUT = ROOT / "quantitative-surface-summary.json"


def is_num(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def describe(xs):
    xs = sorted(float(x) for x in xs if is_num(x))
    n = len(xs)
    if not n:
        return {"n": 0}
    mean = sum(xs)/n
    med = xs[n//2] if n % 2 else (xs[n//2-1] + xs[n//2])/2
    return {"n": n, "min": xs[0], "max": xs[-1], "mean": mean,
            "median": med, "range": xs[-1]-xs[0]}


def main():
    q = json.loads(SRC.read_text(encoding="utf-8"))
    pairs = q["exact_a0_pairs"]
    numeric = [p for p in pairs if is_num(p.get("a_value")) and is_num(p.get("zero_value"))]
    diffs = [p["numeric_difference_a_minus_zero"] for p in numeric]

    sign = collections.Counter("positive" if d > 0 else "negative" if d < 0 else "zero" for d in diffs)
    by_collection = collections.defaultdict(list)
    by_item = collections.defaultdict(list)
    by_collection_item = collections.defaultdict(list)
    qualified_pairs = []
    for p in pairs:
        if p.get("a_qualified") or p.get("zero_qualified"):
            qualified_pairs.append(p["pair_key"])
        d = p.get("numeric_difference_a_minus_zero")
        if is_num(d):
            by_collection[p.get("collection")].append(d)
            by_item[p.get("item")].append(d)
            by_collection_item[f"{p.get('collection')}|{p.get('item')}"] .append(d)

    numeric_dists = q.get("numeric_distributions", {})
    cold_dists = q.get("cold_numeric_distributions", {})
    noise = q.get("decode_noise_by_cell_item", {})

    # Summarize precomputed group descriptors without reinterpreting them.
    def dist_surface(dct):
        groups = []
        for k, v in sorted(dct.items()):
            if not v or not v.get("n"):
                continue
            groups.append({"group": k, "n": v.get("n"), "min": v.get("min"),
                           "max": v.get("max"), "mean": v.get("mean"),
                           "median": v.get("median"), "range": v.get("range")})
        return groups

    out = {
        "schema_version": 1,
        "rules": [
            "All pair differences are a_value - zero_value.",
            "Structural pairs with nonnumeric members remain counted but are excluded from numeric difference summaries.",
            "Qualified audit-derived numeric values retain pair qualification flags.",
            "No hypothesis testing or interpretation is performed."
        ],
        "pairs": {
            "structural_exact_a0_pairs": len(pairs),
            "two_numeric_members": len(numeric),
            "not_two_numeric_members": len(pairs)-len(numeric),
            "qualified_score_pairs": len(qualified_pairs),
            "qualified_pair_keys": qualified_pairs,
            "difference_sign_counts": dict(sorted(sign.items())),
            "difference_overall": describe(diffs),
            "difference_by_collection": {k: describe(v) for k,v in sorted(by_collection.items())},
            "difference_by_item": {k: describe(v) for k,v in sorted(by_item.items())},
            "difference_by_collection_item": {k: describe(v) for k,v in sorted(by_collection_item.items())},
        },
        "validated_numeric_distribution_groups": dist_surface(numeric_dists),
        "cold_numeric_distribution_groups": dist_surface(cold_dists),
        "decode_noise_groups": dist_surface(noise),
    }
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
    print(json.dumps({
        "pairs": out["pairs"],
        "numeric_group_count": len(out["validated_numeric_distribution_groups"]),
        "cold_group_count": len(out["cold_numeric_distribution_groups"]),
        "decode_noise_group_count": len(out["decode_noise_groups"]),
    }, indent=2))

if __name__ == "__main__":
    main()
