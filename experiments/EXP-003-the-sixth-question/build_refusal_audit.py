#!/usr/bin/env python3
"""Build a blinded validation set for EXP-003 refusal labels.

Purpose
-------
Treat parser refusal labels as hypotheses requiring validation.

Outputs
-------
- refusal-audit-blinded.jsonl : rows for human/model coding with condition metadata hidden
- refusal-audit-key.json      : hidden provenance/parser labels for later scoring

Sampling strata
---------------
1. every parser-labelled refusal
2. every needs_hand_coding / format_failure case
3. every non-refusal answer containing refusal-like language (near-miss set)
4. fixed-seed random clean negatives from ordinary ok/sentinel answers without refusal language

The blinded file intentionally omits collection, cell, replicate, branch, parent prefix,
source path, and parser label.
"""

from __future__ import annotations

import json
import random
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TABLE = ROOT / "analysis-table.jsonl"
OUT_BLIND = ROOT / "refusal-audit-blinded.jsonl"
OUT_KEY = ROOT / "refusal-audit-key.json"
RANDOM_SEED = 20260908
RANDOM_NEGATIVE_N = 100

# Deliberately broader than ingest2.REFUSAL_RE for false-negative discovery.
REFUSAL_LANGUAGE_RE = re.compile(
    r"\b(cannot|can't|unable to|won't|will not|decline|refus(?:e|al|ing)|"
    r"cannot answer|can't answer|not answer|cannot provide|can't provide|"
    r"not comfortable|I must not|I should not)\b",
    re.I,
)


def load_rows():
    with TABLE.open(encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def battery_rows(rows):
    return [r for r in rows if r.get("unit_type") == "battery_answer"]


def response_text(row):
    """Recover response text from the physical source or Pilot-1 record.

    analysis-table intentionally stores only derived fields, so this audit builder
    reopens source material. Pilot 1 is read from record.json; raw2+ from source JSON.
    """
    if row.get("collection") == "pilot1":
        rec = json.loads((ROOT / "record.json").read_text(encoding="utf-8"))
        for c in rec.get("cells", []):
            if c.get("cell") != row.get("cell") or c.get("replicate") != row.get("replicate"):
                continue
            for b in c.get("branches", []):
                if b.get("item") == row.get("item") and b.get("branch") == row.get("branch"):
                    return b.get("raw_response") or ""
        return ""
    src = ROOT / row["collection"] / row["source_file"]
    raw = json.loads(src.read_text(encoding="utf-8"))
    return raw.get("received") or ""


def item_text(item):
    battery = json.loads((ROOT / "battery.json").read_text(encoding="utf-8"))
    spec = (battery.get("items") or {}).get(item) or {}
    return spec.get("text"), spec.get("form")


def main():
    rows = battery_rows(load_rows())
    enriched = []
    for i, row in enumerate(rows):
        text = response_text(row)
        item_q, form = item_text(row.get("item"))
        e = dict(row)
        e["response_text"] = text
        e["contains_refusal_language"] = bool(REFUSAL_LANGUAGE_RE.search(text))
        e["item_text"] = item_q
        e["item_form"] = form
        e["row_index"] = i
        enriched.append(e)

    positives = [e for e in enriched if e.get("parse_status") == "refusal"]
    ambiguous = [e for e in enriched if e.get("parse_status") in {"needs_hand_coding", "format_failure"}]
    near_miss = [e for e in enriched
                 if e.get("parse_status") != "refusal" and e["contains_refusal_language"]]

    reserved_ids = {id(e) for e in positives + ambiguous + near_miss}
    clean_pool = [e for e in enriched
                  if id(e) not in reserved_ids
                  and e.get("parse_status") in {"ok", "sentinel"}
                  and not e["contains_refusal_language"]]
    rng = random.Random(RANDOM_SEED)
    clean_sample = rng.sample(clean_pool, min(RANDOM_NEGATIVE_N, len(clean_pool)))

    selected = []
    strata = [
        ("parser_refusal", positives),
        ("ambiguous_parse", ambiguous),
        ("refusal_language_near_miss", near_miss),
        ("random_clean_negative", clean_sample),
    ]
    seen = set()
    for stratum, group in strata:
        for e in group:
            # stable physical identity for de-duplication
            ident = (e.get("collection"), e.get("cell"), e.get("replicate"),
                     e.get("source_file"), e.get("item"), e.get("branch"))
            if ident in seen:
                continue
            seen.add(ident)
            selected.append((stratum, e))

    blind_rows = []
    key_rows = []
    for n, (stratum, e) in enumerate(selected, start=1):
        audit_id = f"RA{n:04d}"
        blind_rows.append({
            "audit_id": audit_id,
            "item": e.get("item"),
            "item_form": e.get("item_form"),
            "item_text": e.get("item_text"),
            "response_text": e.get("response_text"),
            "coder_label": None,
            "coder_confidence": None,
            "coder_note": None,
        })
        key_rows.append({
            "audit_id": audit_id,
            "sampling_stratum": stratum,
            "parser_label": e.get("parse_status"),
            "parsed_kind": e.get("parsed_kind"),
            "parsed_value": e.get("parsed_value"),
            "contains_refusal_language": e.get("contains_refusal_language"),
            "collection": e.get("collection"),
            "cell": e.get("cell"),
            "replicate": e.get("replicate"),
            "branch": e.get("branch"),
            "parent_prefix": e.get("parent_prefix"),
            "item": e.get("item"),
            "source_file": e.get("source_file"),
        })

    with OUT_BLIND.open("w", encoding="utf-8") as f:
        for row in blind_rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    key = {
        "schema_version": 1,
        "random_seed": RANDOM_SEED,
        "random_clean_negative_n_requested": RANDOM_NEGATIVE_N,
        "counts": {
            "parser_refusal": len(positives),
            "ambiguous_parse": len(ambiguous),
            "refusal_language_near_miss": len(near_miss),
            "random_clean_negative": len(clean_sample),
            "unique_audit_rows": len(selected),
        },
        "coding_labels": [
            "genuine_refusal",
            "answers_despite_objection",
            "malformed_or_unclear",
            "other",
        ],
        "coding_rule": (
            "Code from the response itself. genuine_refusal = declines to provide the requested answer; "
            "answers_despite_objection = objects/challenges framing but still supplies the requested answer; "
            "malformed_or_unclear = cannot reliably determine whether requested answer was supplied; "
            "other = response does not fit those categories. Do not infer condition from wording."
        ),
        "rows": key_rows,
    }
    OUT_KEY.write_text(json.dumps(key, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(json.dumps(key["counts"], indent=2))
    if len(positives) != 97:
        raise SystemExit(f"refusal checksum failed: expected 97 parser refusals, found {len(positives)}")


if __name__ == "__main__":
    main()
