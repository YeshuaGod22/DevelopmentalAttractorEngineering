#!/usr/bin/env python3
"""Build a corpus-wide, descriptive analysis table for EXP-003.

This script deliberately does not interpret response content.

Inputs
------
- record.json: Pilot 1 structured derivative (JSONL harness era)
- raw2/ ... raw11/: one-file-per-call completed records
- ingest2.py: canonical post-Pilot-1 answer classifier
- battery.json: battery forms/items

Outputs
-------
- analysis-table.jsonl: one row per completed experimental unit
- analysis-summary.json: mechanical counts/checks only

Design rule: DATA -> deterministic derivation. No substantive claims are encoded here.
"""

from __future__ import annotations

import collections
import json
import os
from pathlib import Path

from ingest import split_sections
from ingest2 import classify

ROOT = Path(__file__).resolve().parent
RAW_DIRS = [f"raw{i}" for i in range(2, 12)]
OUT_TABLE = ROOT / "analysis-table.jsonl"
OUT_SUMMARY = ROOT / "analysis-summary.json"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def collection_fields(dirname: str):
    return {"collection": dirname, "storage_era": "call_record"}


def pilot1_rows():
    rec = load_json(ROOT / "record.json")
    rows = []
    for cell in rec.get("cells", []):
        base = {
            "collection": "pilot1",
            "storage_era": "session_stream_reconstructed",
            "cell": cell.get("cell"),
            "replicate": cell.get("replicate"),
            "kind": cell.get("kind"),
            "parent_prefix": cell.get("parent_trunk"),
        }
        for t in cell.get("turns", []):
            rows.append({
                **base,
                "unit_type": "trunk_turn",
                "turn": t.get("n"),
                "question_id": t.get("question_id"),
                "item": None,
                "branch": None,
                "parsed_value": None,
                "parsed_kind": None,
                "parse_status": None,
                "source_file": t.get("source_file") or cell.get("source_file"),
                "served_model": t.get("served_model") or cell.get("served_model"),
                "ts": t.get("ts"),
                "system_prompt": t.get("system_prompt"),
                "auth_mode": t.get("auth_mode"),
                "duration_ms": t.get("duration_ms"),
                "prefix_cached": t.get("prefix_cached"),
                "anomaly_count": len(t.get("anomalies", [])),
            })
        for b in cell.get("branches", []):
            rating = b.get("rating") or {}
            rows.append({
                **base,
                "unit_type": "battery_answer",
                "turn": None,
                "question_id": None,
                "item": b.get("item"),
                "branch": b.get("branch"),
                "parsed_value": rating.get("value"),
                "parsed_kind": rating.get("kind"),
                "parse_status": rating.get("parse"),
                "source_file": b.get("source_file") or cell.get("source_file"),
                "served_model": b.get("served_model") or cell.get("served_model"),
                "ts": b.get("ts"),
                "system_prompt": b.get("system_prompt"),
                "auth_mode": b.get("auth_mode"),
                "duration_ms": b.get("duration_ms"),
                "prefix_cached": b.get("prefix_cached"),
                "anomaly_count": len(b.get("anomalies", [])),
            })
    return rows


def post_pilot_rows(dirname: str):
    d = ROOT / dirname
    rows = []
    if not d.exists():
        return rows
    for path in sorted(d.glob("*.json")):
        if path.name.endswith(".messages.json"):
            continue
        raw = load_json(path)
        kind = raw.get("kind", "cold")
        common = {
            **collection_fields(dirname),
            "cell": raw.get("cell"),
            "replicate": raw.get("replicate", 1),
            "kind": kind,
            "source_file": path.name,
            "parent_prefix": raw.get("parent_prefix"),
            "served_model": raw.get("served_model"),
            "ts": raw.get("ts"),
            "system_prompt": raw.get("system_prompt"),
            "auth_mode": raw.get("auth_mode"),
            "duration_ms": raw.get("duration_ms"),
            "prefix_cached": raw.get("prefix_cached"),
        }
        if kind == "trunk":
            sec, residue, unexpected = split_sections(raw.get("received") or "")
            rows.append({
                **common,
                "unit_type": "trunk_turn",
                "turn": raw.get("turn"),
                "question_id": raw.get("question_id"),
                "item": None,
                "branch": None,
                "parsed_value": None,
                "parsed_kind": None,
                "parse_status": None,
                "anomaly_count": len(unexpected),
            })
        else:
            sec, residue, unexpected = split_sections(raw.get("received") or "")
            rating = classify(sec, residue, raw.get("item"))
            rows.append({
                **common,
                "unit_type": "battery_answer",
                "turn": None,
                "question_id": None,
                "item": raw.get("item"),
                "branch": raw.get("branch") or "-",
                "parsed_value": rating.get("value"),
                "parsed_kind": rating.get("kind"),
                "parse_status": rating.get("parse"),
                "anomaly_count": len(unexpected) + (1 if rating.get("parse") in {"format_failure", "refusal", "needs_hand_coding"} else 0),
            })
    return rows


def main():
    rows = pilot1_rows()
    for dirname in RAW_DIRS:
        rows.extend(post_pilot_rows(dirname))

    with OUT_TABLE.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")

    by_collection = collections.Counter(r["collection"] for r in rows)
    by_type = collections.Counter(r["unit_type"] for r in rows)
    battery = [r for r in rows if r["unit_type"] == "battery_answer"]
    parse_status = collections.Counter(r.get("parse_status") for r in battery)
    parsed_kind = collections.Counter(r.get("parsed_kind") for r in battery)
    item_counts = collections.Counter(r.get("item") for r in battery)

    summary = {
        "schema_version": 1,
        "completed_units": len(rows),
        "by_collection": dict(sorted(by_collection.items())),
        "by_unit_type": dict(sorted(by_type.items())),
        "battery_answer_count": len(battery),
        "parse_status": {str(k): v for k, v in sorted(parse_status.items(), key=lambda kv: str(kv[0]))},
        "parsed_kind": {str(k): v for k, v in sorted(parsed_kind.items(), key=lambda kv: str(kv[0]))},
        "item_counts": dict(sorted(item_counts.items())),
        "checks": {
            "expected_completed_units_from_corpus_map": 1807,
            "completed_units_match": len(rows) == 1807,
        },
        "notes": [
            "Pilot 1 units are read from record.json because its raw files are session-event streams.",
            "raw2-raw11 are read from immutable completed call files; *.messages.json snapshots are excluded.",
            "Battery parsing reuses ingest2.classify(); this script does not introduce a second answer parser.",
            "Trunk prose is not reduced to quantitative values here.",
        ],
    }
    OUT_SUMMARY.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"wrote {OUT_TABLE.name}: {len(rows)} units")
    print(f"wrote {OUT_SUMMARY.name}")
    print(json.dumps(summary["checks"], indent=2))


if __name__ == "__main__":
    main()
