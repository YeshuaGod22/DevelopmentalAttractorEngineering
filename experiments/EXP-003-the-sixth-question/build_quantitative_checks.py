#!/usr/bin/env python3
"""Mechanical descriptive checks for EXP-003 analysis-table.jsonl.

No hypothesis tests, no interpretation, no claim labels. This script only emits
counts, distributions, and exact matched differences that can be recomputed from
the flattened table.
"""

from __future__ import annotations

import collections
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TABLE = ROOT / "analysis-table.jsonl"
OUT = ROOT / "quantitative-checks.json"


def rows():
    with TABLE.open(encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def is_num(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def describe(xs):
    xs = sorted(float(x) for x in xs if is_num(x))
    if not xs:
        return {"n": 0, "values": []}
    n = len(xs)
    mean = sum(xs) / n
    return {
        "n": n,
        "values": xs,
        "min": xs[0],
        "max": xs[-1],
        "mean": mean,
        "median": (xs[n//2] if n % 2 else (xs[n//2 - 1] + xs[n//2]) / 2),
        "range": xs[-1] - xs[0],
    }


def keystr(parts):
    return "|".join("" if x is None else str(x) for x in parts)


def main():
    data = rows()
    battery = [r for r in data if r.get("unit_type") == "battery_answer"]

    # 1. Parse-status census.
    parse_by_collection = collections.defaultdict(collections.Counter)
    parse_by_item = collections.defaultdict(collections.Counter)
    for r in battery:
        parse_by_collection[r.get("collection")][str(r.get("parse_status"))] += 1
        parse_by_item[r.get("item")][str(r.get("parse_status"))] += 1

    # 2. Pure coverage matrix: counts by collection/cell/replicate/item/branch.
    coverage = collections.Counter()
    for r in battery:
        coverage[keystr((r.get("collection"), r.get("cell"), r.get("replicate"),
                         r.get("item"), r.get("branch")))] += 1

    # 3. Numeric distributions by collection/cell/item. Sentinels/names/refusals
    # remain in the parse census rather than being coerced onto numeric scales.
    dist_groups = collections.defaultdict(list)
    for r in battery:
        if is_num(r.get("parsed_value")):
            dist_groups[keystr((r.get("collection"), r.get("cell"), r.get("item")))].append(r["parsed_value"])
    distributions = {k: describe(v) for k, v in sorted(dist_groups.items())}

    # 4. Exact same-prefix a/0 comparisons. Pair only rows sharing collection,
    # parent_prefix, replicate and item. No cross-prefix substitution.
    pair_groups = collections.defaultdict(dict)
    for r in battery:
        if r.get("branch") not in {"a", "0"}:
            continue
        if not r.get("parent_prefix"):
            continue
        k = keystr((r.get("collection"), r.get("parent_prefix"), r.get("replicate"), r.get("item")))
        pair_groups[k][r["branch"]] = r
    arm_pairs = []
    for k, g in sorted(pair_groups.items()):
        if set(g) != {"a", "0"}:
            continue
        a, z = g["a"], g["0"]
        av, zv = a.get("parsed_value"), z.get("parsed_value")
        arm_pairs.append({
            "pair_key": k,
            "collection": a.get("collection"),
            "parent_prefix": a.get("parent_prefix"),
            "replicate": a.get("replicate"),
            "item": a.get("item"),
            "a_value": av,
            "zero_value": zv,
            "a_parse": a.get("parse_status"),
            "zero_parse": z.get("parse_status"),
            "numeric_difference_a_minus_zero": (av - zv) if is_num(av) and is_num(zv) else None,
            "a_source": a.get("source_file"),
            "zero_source": z.get("source_file"),
        })

    # 5. Decode-noise resamples: raw10 NOISEa/NOISE0 are retained as their own
    # cell distributions. Pair the two arms by item only as a descriptive
    # convenience; do not label their difference an effect.
    noise = [r for r in battery if r.get("collection") == "raw10"]
    noise_by_cell_item = {
        keystr((cell, item)): describe([r.get("parsed_value") for r in noise
                                       if r.get("cell") == cell and r.get("item") == item])
        for cell in sorted({r.get("cell") for r in noise})
        for item in sorted({r.get("item") for r in noise})
    }

    # 6. Cold distributions: cells whose stored kind is cold or cold_schema.
    cold_groups = collections.defaultdict(list)
    for r in battery:
        if r.get("kind") not in {"cold", "cold_schema"}:
            continue
        if is_num(r.get("parsed_value")):
            cold_groups[keystr((r.get("collection"), r.get("cell"), r.get("item")))].append(r["parsed_value"])
    cold = {k: describe(v) for k, v in sorted(cold_groups.items())}

    out = {
        "schema_version": 1,
        "rules": [
            "No sentinels, names, refusals, or malformed answers are coerced to numbers.",
            "a/0 differences require exact collection + parent_prefix + replicate + item matches.",
            "No cross-prefix observations are substituted for missing pair members.",
            "All outputs are descriptive; interpretation belongs to the final writeup pass.",
        ],
        "counts": {
            "completed_units": len(data),
            "battery_answers": len(battery),
            "exact_a0_pairs": len(arm_pairs),
        },
        "parse_status_by_collection": {k: dict(sorted(v.items())) for k, v in sorted(parse_by_collection.items())},
        "parse_status_by_item": {k: dict(sorted(v.items())) for k, v in sorted(parse_by_item.items())},
        "coverage": dict(sorted(coverage.items())),
        "numeric_distributions": distributions,
        "cold_numeric_distributions": cold,
        "exact_a0_pairs": arm_pairs,
        "decode_noise_by_cell_item": noise_by_cell_item,
    }
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {OUT.name}")
    print(json.dumps(out["counts"], indent=2))


if __name__ == "__main__":
    main()
