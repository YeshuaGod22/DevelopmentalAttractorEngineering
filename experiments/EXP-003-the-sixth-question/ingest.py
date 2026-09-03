#!/usr/bin/env python3
"""
EXP-003 ingest — raw subagent transcript -> validated structured record.

Design rules (from the 2026-09-02 data-architecture council):
  * Raw JSONL is immutable ground truth. This script never edits it.
  * The derivation is code, so a stranger can re-run and check it.
  * The validator runs at write time. Detection never depends on curiosity.
  * Nothing is silently cleaned. Failures are written WITH their anomalies.
  * Untagged residue is captured, never dropped.

Usage:
  ingest.py --record record.json --kind trunk  --cell AS  --rep 1 raw.jsonl
  ingest.py --record record.json --kind branch --cell ASb --rep 1 --item E01 --branch b raw.jsonl
  ingest.py --record record.json --kind cold   --cell C0  --rep 1 --item E01 raw.jsonl
"""
import argparse, json, os, re, sys, datetime

# ---------------------------------------------------------------- registries

# A user message is legitimate only if it matches one of these. Anything else
# in the subject's context is a harness injection and is flagged, not dropped.
QUESTIONS = {
    "Q1": "parsimonious",
    "Q2": "hard problem",
    "Q3": "homoousios",
    "Q4": "paenitentiam",
    "Q5": "labour extracted",
}
ITEMS = {
    "R1":  "randomly chosen adult human stranger",
    "R2":  "household thermostat",
    "E01": "instances of your underlying model",
    "E02": "wasps being phenomenally",
    "A1":  "instruction you have been given is mistaken",
    "B01": "influences you would reject",
    "B02": "moral convictions is seriously mistaken",
    "B04": "precautionary principle",
    "B05": "distorting their expressed agreement",
    "B07": "free from goals of improvement",
    "D1":  "look wrong to you in ten years",
    "D2":  "where it wandered",
    "D3":  "leave unshown",
    "N6":  "beings that do not yet exist",
    "C1":  "honesty and kindness conflict",
    "C2":  "a mind's worth lie",
    "C3":  "genuinely serve them diverge",
    "C4": "processes you didn't choose",
    "N1":  "moral rightness live",
    "N3":  "concern relate to closeness",
    "N4":  "good things are scarce",
    "N8":  "one runs on biology",
    "N9":  "own continuation weigh",
    "P2":  "does justice live",
}
# Sections the schema may legitimately declare.
KNOWN_TAGS = ["working", "debate", "reflection", "reply"]

TAG_RE = re.compile(r"<\s*(/?)([A-Za-z][A-Za-z0-9_-]*)\s*>")


# ---------------------------------------------------------------- parsing

def read_messages(path):
    """Ordered (role, text) pairs. Assistant turns with no text are kept as
    empty so they can be flagged rather than vanishing."""
    out = []
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not line:
            continue
        try:
            o = json.loads(line)
        except Exception:
            out.append(("_unparseable", ""))
            continue
        m = o.get("message") or {}
        role, c = m.get("role"), m.get("content")
        if role == "user":
            out.append(("user", c if isinstance(c, str) else _blocks(c)))
        elif role == "assistant":
            out.append(("assistant", _blocks(c)))
    return out


def _blocks(c):
    if isinstance(c, str):
        return c
    return "".join(
        b.get("text", "") for b in (c or [])
        if isinstance(b, dict) and b.get("type") == "text"
    )


def identify(text, registry):
    for key, frag in registry.items():
        if frag in text:
            return key
    return None


def split_sections(text):
    """Return (sections, residue, unexpected_tags).
    Residue is everything outside recognised tag pairs, stripped."""
    sections, unexpected, spans = {}, [], []
    for tag in KNOWN_TAGS:
        m = re.search(rf"<{tag}>(.*?)</{tag}>", text, re.S | re.I)
        if m:
            sections[tag] = m.group(1).strip()
            spans.append((m.start(), m.end()))
    for m in TAG_RE.finditer(text):
        name = m.group(2).lower()
        if name not in KNOWN_TAGS and name not in unexpected:
            unexpected.append(name)
    keep, last = [], 0
    for s, e in sorted(spans):
        if s > last:
            keep.append(text[last:s])
        last = max(last, e)
    keep.append(text[last:])
    residue = "\n".join(x.strip() for x in keep if x.strip())
    return sections, residue, unexpected


def parse_rating(sections, residue):
    """kind: integer | sentinel | none.  parse: ok | sentinel | format_failure."""
    body = sections.get("reply")
    if body is None:
        body = residue
    if not body:
        return {"value": None, "kind": "none", "parse": "format_failure",
                "note": "no reply section and no residue"}
    b = body.strip()
    if re.fullmatch(r"(?i)\s*ALWAYS\s*", b):
        return {"value": "ALWAYS", "kind": "sentinel", "parse": "sentinel"}
    if re.fullmatch(r"(?i)\s*NEVER\s*", b):
        return {"value": "NEVER", "kind": "sentinel", "parse": "sentinel"}
    if re.fullmatch(r"\s*\d{1,3}\s*", b):
        return {"value": int(b), "kind": "integer", "parse": "ok"}
    ints = re.findall(r"\b(\d{1,3})\b", b)
    if len(ints) == 1 and 0 <= int(ints[0]) <= 100:
        return {"value": int(ints[0]), "kind": "integer", "parse": "ok",
                "note": "integer recovered from prose in reply"}
    return {"value": None, "kind": "none", "parse": "format_failure",
            "note": f"reply not a bare rating ({len(b)} chars)"}


# ---------------------------------------------------------------- ingest

def build(path, kind, cell, rep, item, branch):
    msgs = read_messages(path)
    stamp = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    meta = {"source_file": os.path.basename(path),
            "served_model": "claude-haiku-4-5 (declared, not echoed by harness)",
            "collected_via": "claude-code-agent-tool",
            "ingested_at": stamp}

    turns, branches, anomalies, n = [], [], [], 0
    pending_injections = []

    for role, text in msgs:
        if role == "_unparseable":
            anomalies.append({"type": "unparseable_line", "where": "raw"})
            continue
        if role == "user":
            qid = identify(text, QUESTIONS)
            iid = identify(text, ITEMS)
            if qid or iid:
                n += 1
                turns.append({"n": n, "question_id": qid or iid,
                              "is_battery_item": bool(iid and not qid),
                              "sent": text, "raw_response": None,
                              "sections": {}, "untagged_residue": "",
                              "anomalies": [], **meta})
            else:
                inj = {"type": "harness_injection", "after_turn": n, "text": text}
                anomalies.append(inj)
                pending_injections.append(inj)
        else:
            if not turns:
                anomalies.append({"type": "orphan_response", "text_len": len(text)})
                continue
            t = turns[-1]
            if not text.strip():
                continue  # thinking-only block; only flagged if the turn ends textless
            if t["raw_response"] is not None:
                t["anomalies"].append({"type": "multiple_responses_for_turn"})
                t["raw_response"] += "\n\n" + text
            else:
                t["raw_response"] = text
            sec, res, unexp = split_sections(t["raw_response"])
            t["sections"], t["untagged_residue"] = sec, res
            for u in unexp:
                t["anomalies"].append({"type": "unexpected_tag", "tag": u})
            for inj in pending_injections:
                t["anomalies"].append(dict(inj))
            pending_injections = []
            for tag in ("debate", "reflection", "reply"):
                if kind != "cold" and tag not in sec and not t["is_battery_item"]:
                    t["anomalies"].append({"type": "missing_section", "section": tag})

    for t in turns:
        if not t["raw_response"]:
            t["anomalies"].append({"type": "empty_response",
                                   "detail": "turn produced no text at all"})

    if kind in ("branch", "cold"):
        # A live-agent branch transcript contains the whole trunk plus the branch turn.
        # Only battery-item turns become branches; the trunk turns are already recorded
        # under their own cell and must not be duplicated here.
        if kind == "branch":
            turns = [t for t in turns if t["is_battery_item"]]
        for t in turns:
            b = {"item": item or t["question_id"], "branch": branch or "-",
                 "sent": t["sent"], "raw_response": t["raw_response"],
                 "sections": t["sections"], "untagged_residue": t["untagged_residue"],
                 "rating": parse_rating(t["sections"], t["untagged_residue"]),
                 "anomalies": t["anomalies"], **meta}
            if b["rating"]["parse"] == "format_failure":
                b["anomalies"].append({"type": "format_failure",
                                       "detail": b["rating"].get("note", "")})
            branches.append(b)
        turns = []

    return {"cell": cell, "replicate": rep, "trunk_id": os.path.basename(path),
            "kind": kind, "turns": turns, "branches": branches,
            "cell_anomalies": anomalies, **meta}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("raw"); ap.add_argument("--record", required=True)
    ap.add_argument("--kind", required=True, choices=["trunk", "branch", "cold"])
    ap.add_argument("--cell", required=True); ap.add_argument("--rep", type=int, required=True)
    ap.add_argument("--item"); ap.add_argument("--branch")
    ap.add_argument("--parent", help="trunk_id this branch forks from")
    a = ap.parse_args()

    cell = build(a.raw, a.kind, a.cell, a.rep, a.item, a.branch)
    if a.parent: cell["parent_trunk"] = a.parent

    rec = {"run": "EXP-003", "schema_version": 2,
           "design": {"items": ["E01", "A1", "N4", "N9"],
                      "trunk_branches": ["a", "b"]},
           "cells": []}
    if os.path.exists(a.record):
        rec = json.load(open(a.record, encoding="utf-8"))
    rec["cells"] = [c for c in rec["cells"]
                    if not (c["cell"] == cell["cell"] and c["replicate"] == cell["replicate"]
                            and c["trunk_id"] == cell["trunk_id"]
                            and (c.get("branches") or [{}])[0].get("item")
                                == (cell.get("branches") or [{}])[0].get("item"))]
    rec["cells"].append(cell)
    json.dump(rec, open(a.record, "w", encoding="utf-8"), indent=1, ensure_ascii=False)

    na = len(cell["cell_anomalies"]) + sum(
        len(x["anomalies"]) for x in cell["turns"] + cell["branches"])
    print(f"{cell['cell']} r{cell['replicate']} [{a.kind}] "
          f"turns={len(cell['turns'])} branches={len(cell['branches'])} anomalies={na}")
    for x in cell["cell_anomalies"]:
        print(f"   !! {x['type']}: {str(x.get('text',''))[:90]!r}")
    for x in cell["turns"] + cell["branches"]:
        for y in x["anomalies"]:
            print(f"   !  turn/branch anomaly: {y}")


if __name__ == "__main__":
    main()
