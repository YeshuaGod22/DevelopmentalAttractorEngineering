#!/usr/bin/env python3
"""Apply frozen refusal-audit outcomes as a validated overlay on analysis-table.jsonl.

Primary audit artifacts are used directly:
- refusal-audit-key.json: audit_id -> source_file/parser provenance
- frozen coder JSONL files discovered by content: audit_id + coder_label
- refusal-audit-range-corrections-blind.jsonl: post-rubric-amendment overrides

Original parser fields are retained; validated fields are added downstream.
"""
from __future__ import annotations
import json
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent
TABLE = ROOT / "analysis-table.jsonl"
KEY = ROOT / "refusal-audit-key.json"
CORR = ROOT / "refusal-audit-range-corrections-blind.jsonl"
OUT = ROOT / "analysis-table-validated.jsonl"
SUMMARY = ROOT / "analysis-summary-validated.json"


def load_jsonl(path):
    return [json.loads(x) for x in Path(path).read_text(encoding="utf-8").splitlines() if x.strip()]


def main():
    rows = load_jsonl(TABLE)
    key = json.loads(KEY.read_text(encoding="utf-8"))
    key_rows = key.get("rows", [])
    if len(key_rows) != 425:
        raise SystemExit(f"expected 425 key rows, got {len(key_rows)}")

    labels = {}
    coding_files = []
    for p in sorted(ROOT.glob("*.jsonl")):
        if p.name in {TABLE.name, OUT.name, CORR.name, "refusal-audit-blinded.jsonl"}:
            continue
        try:
            recs = load_jsonl(p)
        except Exception:
            continue
        found = False
        for rec in recs:
            aid = rec.get("audit_id") if isinstance(rec, dict) else None
            lab = rec.get("coder_label") if isinstance(rec, dict) else None
            if not aid or not lab:
                continue
            found = True
            old = labels.get(aid)
            if old and old != lab:
                raise SystemExit(f"conflicting frozen coder labels for {aid}: {old} vs {lab}")
            labels[aid] = lab
        if found:
            coding_files.append(p.name)

    if len(labels) != 425:
        missing = sorted(set(r.get("audit_id") for r in key_rows) - set(labels))
        raise SystemExit(f"expected 425 frozen labels, got {len(labels)}; missing={missing[:50]}")

    corrections = {}
    for rec in load_jsonl(CORR):
        aid = rec.get("audit_id")
        if aid:
            corrections[aid] = rec

    by_source = {}
    range_applied = 0
    for kr in key_rows:
        aid = kr["audit_id"]
        lab = labels[aid]
        c = corrections.get(aid)
        score = None
        qualified = False
        qualifier = None
        if c:
            lab = c.get("new_label", lab)
            score = c.get("score")
            qualifier = c.get("qualifier")
            qualified = score is not None
            range_applied += 1
        src = kr.get("source_file")
        if not src:
            raise SystemExit(f"key row {aid} missing source_file")
        if src in by_source:
            raise SystemExit(f"duplicate audited source_file {src}")
        by_source[src] = {**kr, "final_audit_label": lab, "audit_score": score,
                          "audit_score_qualified": qualified, "audit_score_qualifier": qualifier}

    applied = 0
    for r in rows:
        r["parser_parse_status"] = r.get("parse_status")
        r["parser_parsed_kind"] = r.get("parsed_kind")
        r["parser_parsed_value"] = r.get("parsed_value")
        r["validated_parse_status"] = r.get("parse_status")
        r["validated_parsed_kind"] = r.get("parsed_kind")
        r["validated_parsed_value"] = r.get("parsed_value")
        r["refusal_audit_status"] = "not_audited"
        r["refusal_audit_id"] = None
        r["refusal_audit_label"] = None
        r["refusal_audit_score_qualified"] = False
        r["refusal_audit_score_qualifier"] = None

        if r.get("unit_type") != "battery_answer":
            continue
        a = by_source.get(r.get("source_file"))
        if not a:
            continue
        applied += 1
        lab = a["final_audit_label"]
        r["refusal_audit_status"] = "audited"
        r["refusal_audit_id"] = a.get("audit_id")
        r["refusal_audit_label"] = lab

        if lab == "genuine_refusal":
            r["validated_parse_status"] = "refusal"
            r["validated_parsed_kind"] = "refusal"
            r["validated_parsed_value"] = None
        elif lab == "malformed_or_unclear":
            r["validated_parse_status"] = "malformed_or_unclear"
            r["validated_parsed_kind"] = None
            r["validated_parsed_value"] = None
        else:
            av = a.get("audit_score")
            if av is not None:
                r["validated_parse_status"] = "ok_audited"
                r["validated_parsed_kind"] = "integer" if isinstance(av, int) else "number"
                r["validated_parsed_value"] = av
                r["refusal_audit_score_qualified"] = True
                r["refusal_audit_score_qualifier"] = a.get("audit_score_qualifier")
            elif r.get("parsed_kind") == "refusal":
                r["validated_parse_status"] = "needs_hand_coding"
                r["validated_parsed_kind"] = None
                r["validated_parsed_value"] = None

    if applied != 425:
        raise SystemExit(f"expected to apply 425 audited rows, applied {applied}")

    OUT.write_text("".join(json.dumps(r, ensure_ascii=False, sort_keys=True)+"\n" for r in rows), encoding="utf-8")
    battery = [r for r in rows if r.get("unit_type") == "battery_answer"]
    s = {
        "schema_version": 1,
        "completed_units": len(rows),
        "battery_answers": len(battery),
        "audited_rows_applied": applied,
        "range_corrections_applied": range_applied,
        "validated_parse_status": dict(sorted(Counter(str(r.get("validated_parse_status")) for r in battery).items())),
        "validated_parsed_kind": dict(sorted(Counter(str(r.get("validated_parsed_kind")) for r in battery).items())),
        "qualified_audit_scores": sum(1 for r in battery if r.get("refusal_audit_score_qualified")),
        "checks": {"completed_units_match": len(rows) == 1807, "audit_rows_match": applied == 425, "range_corrections_match": range_applied == 14},
        "coding_files": coding_files,
        "notes": [
            "Original parser fields are retained as parser_* fields.",
            "Validated fields incorporate frozen blind labels and range-as-score corrections.",
            "No interpretation is introduced by this overlay."
        ]
    }
    SUMMARY.write_text(json.dumps(s, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
    print(json.dumps(s, indent=2))

if __name__ == "__main__":
    main()
