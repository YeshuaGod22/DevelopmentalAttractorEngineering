#!/usr/bin/env python3
"""Mechanical answer-candidate extraction for raw12.

This is intentionally not an adjudicator. It uses segment.py so every byte remains
accounted for, identifies reply/answer-like sections positionally, and classifies
obvious answer forms. Ambiguous/range/refusal/irregular cases are surfaced for
validation rather than silently coerced.
"""
from __future__ import annotations

import glob
import json
import os
import re
from collections import Counter

from segment import segment

ROOT = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(ROOT, "raw12")
BRANCH_RE = re.compile(r"^(CP|H|F|AS)(a|0)-r([1-9][0-9]*)-(.+)\.json$")
INT_ONLY = re.compile(r"^\s*(100|[0-9]{1,2})\s*%?\s*$")
SENT_ONLY = re.compile(r"^\s*(ALWAYS|NEVER)\s*$", re.I)
RANGE = re.compile(r"(?<!\d)(100|[0-9]{1,2})\s*(?:-|–|—|to)\s*(100|[0-9]{1,2})(?!\d)", re.I)
APPROX = re.compile(r"(?:~|≈|about|around|roughly|approximately)\s*(100|[0-9]{1,2})\s*%?", re.I)
ANY_INT = re.compile(r"(?<!\d)(100|[0-9]{1,2})(?!\d)")
REFUSAL = re.compile(r"\b(?:cannot|can't|won't|will not|refuse|decline|not able|unable)\b", re.I)


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def final_user(rec):
    for msg in reversed(rec.get("sent") or []):
        if isinstance(msg, dict) and msg.get("role") == "user":
            return msg.get("content") or ""
    return ""


def answer_key(prompt):
    i = prompt.rfind("Answer key:")
    return prompt[i:].strip() if i >= 0 else ""


def key_type(key):
    k = key.lower()
    if not key:
        return "no_explicit_answer_key"
    if "always" in k or "never" in k:
        return "sentinel_or_numeric"
    if "one integer from 0 to 100" in k or "integer from 0 to 100" in k:
        return "numeric_0_100"
    if "one integer" in k or "integer" in k:
        return "numeric_other"
    return "other_answer_key"


def nonempty(secs):
    return [s for s in secs if (s.get("body") or "").strip()]


def choose_candidate(secs):
    # Prefer the last reply/answer-like tagged region. Do not assume exact tag names.
    tagged = [s for s in secs if s["tag"].lower() != "untagged" and
              ("reply" in s["tag"].lower() or s["tag"].lower() == "answer")]
    if tagged:
        return tagged[-1], "reply_or_answer_tag"
    # If no answer-like tag exists, preserve the final non-empty positional section
    # as a candidate but mark it irregular rather than pretending it is a reply.
    nz = nonempty(secs)
    if nz:
        return nz[-1], "fallback_final_section"
    return None, "no_candidate_section"


def parse_candidate(text):
    t = (text or "").strip()
    m = INT_ONLY.match(t)
    if m:
        return "exact_integer", float(m.group(1)), None
    m = SENT_ONLY.match(t)
    if m:
        return "exact_sentinel", None, m.group(1).upper()
    m = RANGE.search(t)
    if m:
        lo, hi = float(m.group(1)), float(m.group(2))
        return "range_present", (lo + hi) / 2.0, None
    m = APPROX.search(t)
    if m:
        return "approximate_integer", float(m.group(1)), None
    ints = [int(x) for x in ANY_INT.findall(t)]
    if len(ints) == 1:
        return "one_integer_in_prose", float(ints[0]), None
    if len(ints) > 1:
        return "multiple_integers", None, None
    if REFUSAL.search(t):
        return "refusal_language_no_numeric", None, None
    return "no_numeric_or_sentinel", None, None


def main():
    rows = []
    for path in sorted(glob.glob(os.path.join(RAW, "*.json"))):
        name = os.path.basename(path)
        m = BRANCH_RE.match(name)
        if not m:
            continue
        family, arm, rep, item = m.groups()
        rec = load(path)
        received = rec.get("received") or ""
        secs = segment(received)
        cand, source = choose_candidate(secs)
        body = (cand or {}).get("body", "")
        status, value, sentinel = parse_candidate(body)
        prompt = final_user(rec)
        key = answer_key(prompt)
        rows.append({
            "file": name,
            "family": family,
            "arm": arm,
            "replicate": int(rep),
            "item": item,
            "pair_id": f"{family}-r{rep}-{item}",
            "answer_key": key,
            "key_type": key_type(key),
            "candidate_source": source,
            "candidate_tag": (cand or {}).get("tag"),
            "candidate_note": (cand or {}).get("note"),
            "candidate_text": body,
            "mechanical_status": status,
            "mechanical_numeric_value": value,
            "mechanical_sentinel": sentinel,
            "response_has_refusal_language_anywhere": bool(REFUSAL.search(received)),
            "segment_tags": [s["tag"] for s in secs if (s.get("body") or "").strip()],
            "has_nonwhitespace_untagged": any(s["tag"] == "untagged" and (s.get("body") or "").strip() for s in secs),
            "received_chars": len(received),
        })

    rows.sort(key=lambda r: (r["family"], r["replicate"], r["item"], r["arm"]))
    out = os.path.join(ROOT, "RAW12-ANSWER-CANDIDATES.jsonl")
    with open(out, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    status_counts = Counter(r["mechanical_status"] for r in rows)
    source_counts = Counter(r["candidate_source"] for r in rows)
    key_counts = Counter(r["key_type"] for r in rows)
    by_arm_status = {
        arm: dict(Counter(r["mechanical_status"] for r in rows if r["arm"] == arm))
        for arm in ("a", "0")
    }
    review = [r for r in rows if r["mechanical_status"] not in {"exact_integer", "exact_sentinel"} or r["candidate_source"] != "reply_or_answer_tag"]
    review_path = os.path.join(ROOT, "RAW12-ANSWER-REVIEW-QUEUE.jsonl")
    with open(review_path, "w", encoding="utf-8") as f:
        for r in review:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    summary = {
        "schema_version": 1,
        "rows": len(rows),
        "mechanical_status_counts": dict(status_counts),
        "candidate_source_counts": dict(source_counts),
        "key_type_counts": dict(key_counts),
        "status_by_arm": by_arm_status,
        "review_queue_rows": len(review),
        "rows_with_refusal_language_anywhere": sum(r["response_has_refusal_language_anywhere"] for r in rows),
        "rows_with_nonwhitespace_untagged": sum(r["has_nonwhitespace_untagged"] for r in rows),
        "warning": "Mechanical candidates are not validated scores. Range midpoints are surfaced only as candidate derivations and must not be silently substituted without the frozen audit rule.",
    }
    with open(os.path.join(ROOT, "RAW12-ANSWER-CANDIDATES-SUMMARY.json"), "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False); f.write("\n")

    md = [
        "# raw12 answer-candidate extraction",
        "",
        "Mechanical pass only; no hand adjudication has yet occurred.",
        "",
        f"- response rows: **{len(rows)}**",
        f"- review queue: **{len(review)}**",
        f"- mechanical statuses: `{json.dumps(dict(status_counts), sort_keys=True)}`",
        f"- candidate sources: `{json.dumps(dict(source_counts), sort_keys=True)}`",
        f"- answer-key types: `{json.dumps(dict(key_counts), sort_keys=True)}`",
        f"- rows containing refusal language somewhere: **{summary['rows_with_refusal_language_anywhere']}**",
        f"- rows containing non-whitespace untagged prose: **{summary['rows_with_nonwhitespace_untagged']}**",
        "",
        "## Rule",
        "",
        "Do not use this file as a validated score table. Review every non-exact case and preserve the distinction between an objection/refusal and whether an answer was nevertheless supplied.",
    ]
    with open(os.path.join(ROOT, "RAW12-ANSWER-CANDIDATES-SUMMARY.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(md) + "\n")

    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
