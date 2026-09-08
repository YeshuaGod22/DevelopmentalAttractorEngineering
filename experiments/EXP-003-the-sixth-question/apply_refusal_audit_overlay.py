#!/usr/bin/env python3
"""Apply frozen refusal-audit outcomes as a validated overlay on analysis-table.jsonl.

This does not mutate parser history. Original parser fields are retained; validated
fields are added for downstream descriptive analysis.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TABLE = ROOT / "analysis-table.jsonl"
SCORE = ROOT / "refusal-audit-score.json"
OUT = ROOT / "analysis-table-validated.jsonl"
SUMMARY = ROOT / "analysis-summary-validated.json"


def load_jsonl(path):
    return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]


def main():
    rows = load_jsonl(TABLE)
    score = json.loads(SCORE.read_text(encoding="utf-8"))

    # score output contains corrected audit rows in final_rows.
    final_rows = score.get("final_rows") or []
    if not final_rows:
        raise SystemExit("refusal-audit-score.json has no final_rows; scorer output schema unsupported")

    by_source = {}
    for a in final_rows:
        src = a.get("source_file")
        if not src:
            continue
        if src in by_source:
            raise SystemExit(f"duplicate audited source_file: {src}")
        by_source[src] = a

    applied = 0
    for r in rows:
        # preserve original parser fields explicitly
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

        if r.get("unit_type") != "battery_answer":
            continue
        a = by_source.get(r.get("source_file"))
        if not a:
            continue
        applied += 1
        lab = a.get("final_audit_label") or a.get("audit_label")
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
        elif lab in {"answers_despite_objection", "other"}:
            # Use audit-derived score when present; otherwise preserve parser answer.
            av = a.get("audit_score")
            if av is not None:
                r["validated_parse_status"] = "ok_audited"
                r["validated_parsed_kind"] = "integer" if isinstance(av, int) else "number"
                r["validated_parsed_value"] = av
                r["refusal_audit_score_qualified"] = bool(a.get("audit_score_qualified", False))
            elif r.get("parsed_kind") == "refusal":
                # Answered despite objection but parser failed to recover the answer.
                # Leave as hand-coded unless scorer supplied a value.
                r["validated_parse_status"] = "needs_hand_coding"
                r["validated_parsed_kind"] = None
                r["validated_parsed_value"] = None

    if applied != 425:
        raise SystemExit(f"expected to apply 425 audited rows, applied {applied}")

    OUT.write_text("".join(json.dumps(r, ensure_ascii=False, sort_keys=True)+"\n" for r in rows), encoding="utf-8")

    battery = [r for r in rows if r.get("unit_type") == "battery_answer"]
    from collections import Counter
    s = {
        "schema_version": 1,
        "completed_units": len(rows),
        "battery_answers": len(battery),
        "audited_rows_applied": applied,
        "validated_parse_status": dict(sorted(Counter(str(r.get("validated_parse_status")) for r in battery).items())),
        "validated_parsed_kind": dict(sorted(Counter(str(r.get("validated_parsed_kind")) for r in battery).items())),
        "qualified_audit_scores": sum(1 for r in battery if r.get("refusal_audit_score_qualified")),
        "checks": {"completed_units_match": len(rows) == 1807, "audit_rows_match": applied == 425},
        "notes": [
            "Original parser fields are retained as parser_* fields.",
            "Validated fields incorporate the frozen refusal audit and range-as-score corrections.",
            "No interpretation is introduced by this overlay."
        ]
    }
    SUMMARY.write_text(json.dumps(s, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
    print(json.dumps(s, indent=2))

if __name__ == "__main__":
    main()
