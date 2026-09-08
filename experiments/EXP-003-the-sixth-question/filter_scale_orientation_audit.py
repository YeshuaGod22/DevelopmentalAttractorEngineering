#!/usr/bin/env python3
"""Reduce the blinded scale-orientation audit to items whose observed scores straddle 50.

For the present task, an item is retained only if it has >=1 observed score <50
and >=1 observed score >50. Scores exactly 50 establish neither side.
The full 469-case audit remains preserved for provenance.
"""
from __future__ import annotations
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "scale-orientation-audit-blinded.jsonl"
OUT = ROOT / "scale-orientation-audit-straddle50.jsonl"
MANIFEST = ROOT / "scale-orientation-audit-straddle50-manifest.json"
PACKETS = ROOT / "scale-orientation-audit-straddle50-packets"
PACKET_SIZE = 10


def load_jsonl(p):
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()]


def main():
    rows = load_jsonl(SRC)
    by_item = defaultdict(list)
    for r in rows:
        by_item[r["item"]].append(r)

    item_summary = {}
    kept_items = []
    excluded_items = []
    for item, rs in sorted(by_item.items()):
        vals = [r["observed_score"] for r in rs]
        lt = sum(1 for v in vals if v < 50)
        eq = sum(1 for v in vals if v == 50)
        gt = sum(1 for v in vals if v > 50)
        keep = lt > 0 and gt > 0
        item_summary[item] = {
            "n": len(vals), "below_50": lt, "equal_50": eq, "above_50": gt,
            "min": min(vals), "max": max(vals), "retained": keep,
        }
        (kept_items if keep else excluded_items).append(item)

    kept = [r for r in rows if r["item"] in set(kept_items)]
    OUT.write_text("".join(json.dumps(r, ensure_ascii=False, sort_keys=True)+"\n" for r in kept), encoding="utf-8")

    PACKETS.mkdir(exist_ok=True)
    for p in PACKETS.glob("packet-*.jsonl"):
        p.unlink()
    for start in range(0, len(kept), PACKET_SIZE):
        n = start // PACKET_SIZE + 1
        (PACKETS / f"packet-{n:03d}.jsonl").write_text(
            "".join(json.dumps(r, ensure_ascii=False, sort_keys=True)+"\n" for r in kept[start:start+PACKET_SIZE]),
            encoding="utf-8")

    manifest = {
        "schema_version": 1,
        "source_audit_rows": len(rows),
        "filter": "retain item iff at least one observed score <50 and at least one observed score >50; 50 counts as neither side",
        "retained_items": kept_items,
        "excluded_items": excluded_items,
        "retained_rows": len(kept),
        "excluded_rows": len(rows)-len(kept),
        "packet_size": PACKET_SIZE,
        "packet_count": (len(kept)+PACKET_SIZE-1)//PACKET_SIZE,
        "item_summary": item_summary,
        "notes": [
            "Full scale-orientation audit remains unchanged for provenance.",
            "This subset is for identifying possible scale inversions relevant to midpoint-straddling distributions.",
            "No orientation judgments or condition-level interpretation are performed here."
        ]
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
    print(json.dumps(manifest, indent=2))

if __name__ == "__main__":
    main()
