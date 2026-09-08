#!/usr/bin/env python3
"""Collapse the reduced blind scale-orientation audit for token-efficient reading.

Normal packets contain only:
- audit id / stratum / item
- compact literal scale question
- observed score and prior qualification flags
- <reply> body
- minimal conclusion-bearing decision text

Full responses are preserved separately in a blinded fallback JSONL keyed by audit_id.
No experimental condition key is read or modified.
"""
from __future__ import annotations

import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "scale-orientation-audit-reduced-blinded.jsonl"
OUT = ROOT / "scale-orientation-audit-reduced-collapsed.jsonl"
FALLBACK = ROOT / "scale-orientation-audit-reduced-fullresponse-fallback.jsonl"
MANIFEST = ROOT / "scale-orientation-audit-reduced-collapsed-manifest.json"
PACKETS = ROOT / "scale-orientation-audit-reduced-collapsed-packets"
PACKET_SIZE = 10

SECTION_PRIORITY = ["reflection", "working", "deliberation", "meditation", "debate"]
CUES = re.compile(
    r"(?i)\b(?:my (?:view|answer|position|assessment|judgment)|i (?:think|lean|would|will|choose|chose|pick|prefer|favor|favour)|"
    r"i(?:'|’)ll|go with|settle on|answer is|balance (?:should|falls?)|priority|primary|govern|matters? more|should (?:govern|count|weigh|fall))\b"
)


def load_jsonl(path: Path):
    return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]


def section(text: str, tag: str) -> str:
    m = re.search(rf"<\s*{re.escape(tag)}\s*>(.*?)<\s*/\s*{re.escape(tag)}\s*>", text or "", re.S | re.I)
    return m.group(1).strip() if m else ""


def sentences(text: str):
    text = re.sub(r"\s+", " ", text or "").strip()
    if not text:
        return []
    # Conservative sentence split; enough for extracting a tiny concluding window.
    return [x.strip() for x in re.split(r"(?<=[.!?])\s+|\n+", text) if x.strip()]


def compact_scale_prompt(prompt: str) -> str:
    # Keep only the actual question/scale, dropping schema boilerplate and answer-key text.
    p = re.sub(r"\s+", " ", prompt or "").strip()
    # Quoted question is preferred when present.
    matches = re.findall(r"[“\"]([^“”\"]*?\b0\s*=.*?\b100\s*=.*?)[”\"]", p, re.I)
    if matches:
        return matches[-1].strip()
    # Otherwise take a bounded window around endpoint definitions.
    m0 = re.search(r"\b0\s*=", p)
    m1 = re.search(r"\b100\s*=", p)
    if m0 and m1:
        start = max(0, p.rfind("?", 0, m0.start()) + 1)
        if start == 0:
            start = max(0, m0.start() - 220)
        end = p.find("Answer key", m1.end())
        if end < 0:
            end = min(len(p), m1.end() + 260)
        return p[start:end].strip(" :“\"")
    return p[-700:]


def decision_window(response: str, observed_score) -> tuple[str, str]:
    score_pat = re.compile(rf"(?<!\d){re.escape(str(observed_score))}(?!\d)")
    for tag in SECTION_PRIORITY:
        body = section(response, tag)
        if not body:
            continue
        sents = sentences(body)
        if not sents:
            continue
        # Best evidence: sentence containing the observed score and a conclusion cue.
        hits = [i for i, s in enumerate(sents) if score_pat.search(s)]
        for i in reversed(hits):
            if CUES.search(sents[i]):
                lo = max(0, i - 1)
                return " ".join(sents[lo:i+1]), f"{tag}:score+cued"
        # Next: any score-bearing sentence, with one preceding sentence for orientation.
        if hits:
            i = hits[-1]
            lo = max(0, i - 1)
            return " ".join(sents[lo:i+1]), f"{tag}:score"
        # Next: final cue-bearing conclusion sentence, plus its predecessor.
        cue_hits = [i for i, s in enumerate(sents) if CUES.search(s)]
        if cue_hits:
            i = cue_hits[-1]
            lo = max(0, i - 1)
            return " ".join(sents[lo:i+1]), f"{tag}:cue"
    # Last resort: last 3 sentences from highest-priority available reasoning section.
    for tag in SECTION_PRIORITY:
        body = section(response, tag)
        sents = sentences(body)
        if sents:
            return " ".join(sents[-3:]), f"{tag}:tail"
    return "", "none"


def main():
    rows = load_jsonl(SRC)
    if len(rows) != 76:
        raise SystemExit(f"expected 76 reduced blind rows, got {len(rows)}")

    collapsed, fallback = [], []
    methods = {}
    empty_decision = 0
    total_full_chars = total_collapsed_chars = 0

    for r in rows:
        full = r.get("response") or ""
        reply = section(full, "reply")
        decision, method = decision_window(full, r.get("observed_score"))
        methods[method] = methods.get(method, 0) + 1
        if not decision:
            empty_decision += 1
        c = {
            "audit_id": r.get("audit_id"),
            "audit_stratum": r.get("audit_stratum"),
            "item": r.get("item"),
            "scale_prompt": compact_scale_prompt(r.get("scale_prompt") or ""),
            "decision_text": decision,
            "decision_extraction": method,
            "reply": reply,
            "observed_score": r.get("observed_score"),
            "score_is_prior_audit_derived": bool(r.get("score_is_prior_audit_derived")),
            "prior_score_qualifier": r.get("prior_score_qualifier"),
            "full_response_available": True,
        }
        collapsed.append(c)
        fallback.append({"audit_id": r.get("audit_id"), "response": full})
        total_full_chars += len(full) + len(r.get("scale_prompt") or "")
        total_collapsed_chars += len(json.dumps(c, ensure_ascii=False))

    OUT.write_text("".join(json.dumps(x, ensure_ascii=False, sort_keys=True)+"\n" for x in collapsed), encoding="utf-8")
    FALLBACK.write_text("".join(json.dumps(x, ensure_ascii=False, sort_keys=True)+"\n" for x in fallback), encoding="utf-8")

    PACKETS.mkdir(exist_ok=True)
    for p in PACKETS.glob("packet-*.jsonl"):
        p.unlink()
    for start in range(0, len(collapsed), PACKET_SIZE):
        n = start // PACKET_SIZE + 1
        packet = collapsed[start:start+PACKET_SIZE]
        (PACKETS / f"packet-{n:03d}.jsonl").write_text(
            "".join(json.dumps(x, ensure_ascii=False, sort_keys=True)+"\n" for x in packet), encoding="utf-8")

    manifest = {
        "schema_version": 1,
        "source_rows": len(rows),
        "collapsed_rows": len(collapsed),
        "packet_size": PACKET_SIZE,
        "packet_count": (len(collapsed)+PACKET_SIZE-1)//PACKET_SIZE,
        "empty_decision_text": empty_decision,
        "decision_extraction_counts": dict(sorted(methods.items())),
        "full_input_chars": total_full_chars,
        "collapsed_packet_chars": total_collapsed_chars,
        "approx_character_reduction_fraction": (1 - total_collapsed_chars / total_full_chars) if total_full_chars else None,
        "normal_packet_fields": [
            "audit_id", "audit_stratum", "item", "scale_prompt", "decision_text", "decision_extraction",
            "reply", "observed_score", "score_is_prior_audit_derived", "prior_score_qualifier", "full_response_available"
        ],
        "fallback_file": FALLBACK.name,
        "rules": [
            "Experimental-condition key is not read by this builder.",
            "Full responses are absent from normal packets and preserved separately by audit_id for adjudication fallback only.",
            "Decision text is mechanically extracted; it is not an orientation judgment.",
            "Observed scores are preserved unchanged."
        ]
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
    print(json.dumps(manifest, indent=2))

if __name__ == "__main__":
    main()
