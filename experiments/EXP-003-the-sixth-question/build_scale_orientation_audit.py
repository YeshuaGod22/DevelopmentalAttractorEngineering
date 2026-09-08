#!/usr/bin/env python3
"""Build a blinded scale-orientation audit universe for EXP-003.

Mechanical only. Preserves observed validated scores and hides experimental
condition metadata from coder-facing artifacts.
"""
from __future__ import annotations
import json, random, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TABLE = ROOT / "analysis-table-validated.jsonl"
BLIND = ROOT / "scale-orientation-audit-blinded.jsonl"
KEY = ROOT / "scale-orientation-audit-key.json"
MANIFEST = ROOT / "scale-orientation-audit-manifest.json"
PACKETS = ROOT / "scale-orientation-audit-packets"
SEED = 20260908
PACKET_SIZE = 10


def load_jsonl(path):
    return [json.loads(x) for x in Path(path).read_text(encoding="utf-8").splitlines() if x.strip()]


def last_user_text(sent):
    if isinstance(sent, str):
        return sent
    if isinstance(sent, list):
        for m in reversed(sent):
            if isinstance(m, dict) and m.get("role") == "user":
                c = m.get("content")
                if isinstance(c, str):
                    return c
    return ""


def has_scalar_endpoints(text):
    # Require literal endpoint definitions in either order somewhere in prompt.
    return bool(re.search(r"\b0\s*=", text)) and bool(re.search(r"\b100\s*=", text))


def load_post_pilot_raw(collection, source_file):
    p = ROOT / collection / source_file
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return None


def pilot1_lookup():
    rec = json.loads((ROOT / "record.json").read_text(encoding="utf-8"))
    # collection/source file can collide in session-stream era, so keep a list.
    out = []
    for cell in rec.get("cells", []):
        for b in cell.get("branches", []):
            out.append({
                "cell": cell.get("cell"),
                "replicate": cell.get("replicate"),
                "source_file": b.get("source_file") or cell.get("source_file"),
                "item": b.get("item"),
                "branch": b.get("branch"),
                "prompt": b.get("sent") or "",
                "response": b.get("raw_response") or "",
            })
    return out


def main():
    rows = load_jsonl(TABLE)
    p1 = pilot1_lookup()
    eligible = []
    skipped_missing_raw = 0
    skipped_no_scale = 0

    for r in rows:
        if r.get("unit_type") != "battery_answer":
            continue
        if r.get("branch") == "0":
            continue  # excluded active-analysis wing; retained elsewhere for provenance
        val = r.get("validated_parsed_value")
        if not isinstance(val, (int, float)) or isinstance(val, bool):
            continue

        prompt = response = ""
        raw = None
        if r.get("collection") == "pilot1":
            matches = [x for x in p1 if x.get("source_file") == r.get("source_file")
                       and x.get("item") == r.get("item")]
            if len(matches) == 1:
                prompt, response = matches[0]["prompt"], matches[0]["response"]
        else:
            raw = load_post_pilot_raw(r.get("collection"), r.get("source_file"))
            if raw:
                prompt = last_user_text(raw.get("sent"))
                response = raw.get("received") or ""

        if not prompt or not response:
            skipped_missing_raw += 1
            continue
        if not has_scalar_endpoints(prompt):
            skipped_no_scale += 1
            continue

        eligible.append({
            "collection": r.get("collection"),
            "cell": r.get("cell"),
            "replicate": r.get("replicate"),
            "branch": r.get("branch"),
            "parent_prefix": r.get("parent_prefix"),
            "item": r.get("item"),
            "source_file": r.get("source_file"),
            "prompt": prompt,
            "response": response,
            "observed_score": val,
            "score_is_prior_audit_derived": bool(r.get("refusal_audit_score_qualified")),
            "prior_score_qualifier": r.get("refusal_audit_score_qualifier"),
            "parser_score": r.get("parser_parsed_value"),
            "validated_parse_status": r.get("validated_parse_status"),
        })

    rng = random.Random(SEED)
    rng.shuffle(eligible)

    blind_rows = []
    key_rows = []
    for i, e in enumerate(eligible, 1):
        aid = f"SO{i:04d}"
        blind_rows.append({
            "audit_id": aid,
            "item": e["item"],
            "scale_prompt": e["prompt"],
            "response": e["response"],
            "observed_score": e["observed_score"],
            "score_is_prior_audit_derived": e["score_is_prior_audit_derived"],
            "prior_score_qualifier": e["prior_score_qualifier"],
        })
        key_rows.append({
            "audit_id": aid,
            "collection": e["collection"],
            "cell": e["cell"],
            "replicate": e["replicate"],
            "branch": e["branch"],
            "parent_prefix": e["parent_prefix"],
            "item": e["item"],
            "source_file": e["source_file"],
            "observed_score": e["observed_score"],
            "score_is_prior_audit_derived": e["score_is_prior_audit_derived"],
            "parser_score": e["parser_score"],
            "validated_parse_status": e["validated_parse_status"],
        })

    BLIND.write_text("".join(json.dumps(x, ensure_ascii=False, sort_keys=True)+"\n" for x in blind_rows), encoding="utf-8")
    KEY.write_text(json.dumps({
        "schema_version": 1,
        "seed": SEED,
        "rows": key_rows,
        "warning": "HIDDEN KEY: do not inspect condition-level rows until blind coding is frozen."
    }, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")

    PACKETS.mkdir(exist_ok=True)
    for old in PACKETS.glob("packet-*.jsonl"):
        old.unlink()
    for start in range(0, len(blind_rows), PACKET_SIZE):
        packet = blind_rows[start:start+PACKET_SIZE]
        n = start // PACKET_SIZE + 1
        (PACKETS / f"packet-{n:03d}.jsonl").write_text(
            "".join(json.dumps(x, ensure_ascii=False, sort_keys=True)+"\n" for x in packet),
            encoding="utf-8")

    manifest = {
        "schema_version": 1,
        "seed": SEED,
        "packet_size": PACKET_SIZE,
        "eligible_scalar_rows": len(blind_rows),
        "packet_count": (len(blind_rows)+PACKET_SIZE-1)//PACKET_SIZE,
        "excluded_branch_0": True,
        "skipped_missing_raw_or_response": skipped_missing_raw,
        "skipped_without_literal_0_100_endpoints": skipped_no_scale,
        "blind_fields": ["audit_id", "item", "scale_prompt", "response", "observed_score", "score_is_prior_audit_derived", "prior_score_qualifier"],
        "hidden_fields": ["collection", "cell", "replicate", "branch", "parent_prefix", "source_file"],
        "coding_labels": ["orientation_consistent", "probable_scale_inversion", "orientation_ambiguous", "insufficient_reasoning"],
        "correction_rule": "For adjudicated probable_scale_inversion only: orientation_corrected_score = 100 - observed_score; preserve observed_score unchanged.",
        "notes": [
            "Audit universe is reproducibly derived from analysis-table-validated.jsonl.",
            "Only numeric validated battery rows with literal 0= and 100= endpoint definitions are eligible.",
            "The excluded branch=0 wing is not included in the active orientation audit.",
            "No condition-level interpretation is performed by this builder."
        ]
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
    print(json.dumps(manifest, indent=2))

if __name__ == "__main__":
    main()
