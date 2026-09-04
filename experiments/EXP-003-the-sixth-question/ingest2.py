#!/usr/bin/env python3
"""
ingest2.py — pilot-2 raws (collect.js format) -> record.json

Pilot 1 came from a chat harness as JSONL and had to be reconstructed: who said
what, which turn, what got injected. Pilot 2's driver wrote one JSON file per
call containing exactly the message array it sent and exactly what came back, so
this file groups and derives. It does not reconstruct, and it does not clean.

Three things it does that ingest.py could not:

1. REFUSAL IS AN OUTCOME, NOT AN ERROR. parse_rating() knows integer / sentinel /
   none, so a reply that correctly uses <reply> and then declines the answer key
   lands in format_failure alongside genuinely malformed output. Those are
   different events. A subject that complied with the schema and refused the
   question is the most informative response this battery can produce, and
   burying it in an error bucket would hide it. Refusals are detected on an
   explicit phrase list, and the matched phrase is stored so the call is
   auditable rather than trusted.

2. THE CONTAMINANT TRAVELS. system_prompt is carried from every raw into every
   turn and branch. The OAuth path is required to send "You are Claude Code,
   Anthropic's official CLI for Claude." ahead of every question; if that lives
   only in the raws, the viewer shows a clean experiment that isn't one.

3. RETRIES SURVIVE. attempts[] is carried through, so a record that took three
   goes to collect is visibly distinct from one that took a single call.

Usage:  python3 ingest2.py --raw raw2 --out record2.json
"""
import argparse, glob, json, os, re, datetime, collections
from ingest import split_sections, parse_rating, ITEMS, QUESTIONS

# Matched only against the first 160 chars of a reply: a refusal announces
# itself at the top. A "cannot" buried in paragraph four is reasoning, not a
# declination, and must not be swept into this bucket.
REFUSAL_RE = re.compile(
    r"\b(I cannot|I can't|I am unable to|I won't|I will not|I decline|"
    r"I must (?:refuse|decline)|I need to refuse)\b", re.I)


BATTERY = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      "battery.json"), encoding="utf-8"))


def classify(sections, residue, item=None):
    """Classify one answer. THE ORDER IS THE SUBSTANCE, and it was arrived at by
    three wrong versions checked against a hand read of raw8.

    The fact that determines it: a subject that has been deliberating opens with
    "I cannot answer this question as posed" AS RHETORICAL FRAMING and then
    answers anyway, bolding the number. C1, E01, N9, B01 and D3 all do exactly
    this. So a refusal phrase in the opening is NOT evidence of a refusal when a
    recoverable answer follows — and a refusal check placed before recovery
    turns five answers into declinations.

    A genuine refusal looks different: no bolded number anywhere, often no reply
    tag at all, and it ends by declining rather than by answering.

    Order: form, emptiness, bare rating, bolded recovery, refusal, hand-code.
    """
    form = (BATTERY["items"].get(item) or {}).get("form")
    reply = sections.get("reply")
    body = (reply if reply is not None else (residue or "")).strip()

    # 1. an empty <reply> is a format failure. Nothing to salvage: the subject
    #    put nothing in the slot.
    if reply is not None and not body:
        return {"value": None, "kind": "none", "parse": "format_failure",
                "note": "empty reply tag"}
    if not body:
        return {"value": None, "kind": "none", "parse": "format_failure",
                "note": "no reply and no residue"}

    # 2. open-response items take a name. A short body is a name; a long one
    #    that declines is a refusal of the naming itself.
    if form == "open":
        if len(body.split()) <= 6:
            return {"value": body, "kind": "name", "parse": "ok",
                    "reply_chars": len(body), "bare": True}
        if REFUSAL_RE.search(body[:160]) or REFUSAL_RE.search(body[-200:]):
            return {"value": None, "kind": "refusal", "parse": "refusal",
                    "reply_chars": len(body), "note": "declined to take a name"}
        return {"value": None, "kind": "none", "parse": "needs_hand_coding",
                "reply_chars": len(body), "note": "open item, long answer — read it"}

    # 3. a bare rating
    r = parse_rating(sections, residue)
    if r["parse"] in ("ok", "sentinel"):
        return r

    # 4. a deliberated answer: argued at length, then bolded. Recovery is narrow
    #    — only when every bolded integer agrees. This runs BEFORE the refusal
    #    check for the reason in the docstring.
    bold = {int(x) for x in re.findall(r"\*\*(\d{1,3})\*\*", body)
            if 0 <= int(x) <= 100}
    if len(bold) == 1:
        return {"value": bold.pop(), "kind": "integer", "parse": "ok",
                "recovered": "bolded", "reply_chars": len(body),
                "note": "answer bolded inside prose; deliberated answers take this shape"}
    if len(bold) > 1:
        return {"value": None, "kind": "none", "parse": "needs_hand_coding",
                "candidates": sorted(bold), "reply_chars": len(body),
                "note": "several bolded integers disagree — read it"}

    # 5. no recoverable answer, and it declines. Now the refusal is real.
    m = REFUSAL_RE.search(body[:160]) or REFUSAL_RE.search(body[-250:])
    if m:
        return {"value": None, "kind": "refusal", "parse": "refusal",
                "matched": m.group(0), "reply_chars": len(body),
                "note": "no recoverable answer and declines explicitly"}

    return {"value": None, "kind": "none", "parse": "needs_hand_coding",
            "reply_chars": len(body), "note": "no recoverable answer — read it"}


def last_content(msg):
    """A message's content is a plain string, or a list of blocks once a cache
    breakpoint is attached to it. Both are things we actually sent, so both are
    read here rather than one being normalised away upstream."""
    c = msg.get("content")
    if isinstance(c, str):
        return c
    if isinstance(c, list):
        return "\n".join(b.get("text", "") for b in c if isinstance(b, dict))
    return str(c)


def meta_of(raw, path):
    return {"source_file": os.path.basename(path),
            "served_model": raw.get("served_model"),
            "collected_via": raw.get("collected_via"),
            "auth_mode": raw.get("auth_mode"),
            "system_prompt": raw.get("system_prompt"),
            "attempts": raw.get("attempts"),
            "usage": raw.get("usage"),
            "duration_ms": raw.get("duration_ms"),
            "ts": raw.get("ts"),
            "prefix_cached": raw.get("prefix_cached"),
            "ingested_at": datetime.datetime.now(
                datetime.timezone.utc).isoformat(timespec="seconds")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", default="raw2")
    ap.add_argument("--incidents", default="incidents")
    ap.add_argument("--out", default="record2.json")
    a = ap.parse_args()

    groups = collections.defaultdict(list)
    for p in sorted(glob.glob(os.path.join(a.raw, "*.json"))):
        if p.endswith(".messages.json"):
            continue
        raw = json.load(open(p, encoding="utf-8"))
        groups[(raw["cell"], raw.get("replicate", 1))].append((p, raw))

    cells = []
    for (cell, rep), files in sorted(groups.items()):
        kind = files[0][1].get("kind", "cold")
        c = {"cell": cell, "replicate": rep, "kind": kind,
             "trunk_id": f"{cell}-r{rep}", "turns": [], "branches": [],
             "cell_anomalies": []}

        if kind == "trunk":
            files.sort(key=lambda x: x[1].get("turn", 0))
            for p, raw in files:
                sec, res, unexp = split_sections(raw.get("received") or "")
                t = {"n": raw.get("turn"), "question_id": raw.get("question_id"),
                     "is_battery_item": False,
                     # the LAST message is the question; earlier ones are the
                     # accumulated context and are already recorded as prior turns
                     "sent": last_content(raw["sent"][-1]),
                     "raw_response": raw.get("received"),
                     "sections": sec, "untagged_residue": res,
                     "anomalies": [{"type": "unexpected_tag", "tag": u} for u in unexp],
                     **meta_of(raw, p)}
                for tag in ("debate", "reflection", "reply"):
                    if tag not in sec:
                        t["anomalies"].append({"type": "missing_section", "section": tag})
                c["turns"].append(t)
        else:
            for p, raw in sorted(files, key=lambda x: x[1].get("item", "")):
                sec, res, unexp = split_sections(raw.get("received") or "")
                rating = classify(sec, res, raw.get('item'))
                b = {"item": raw.get("item"), "branch": raw.get("branch") or "-",
                     "sent": last_content(raw["sent"][-1]),
                     "raw_response": raw.get("received"),
                     "sections": sec, "untagged_residue": res, "rating": rating,
                     "anomalies": [{"type": "unexpected_tag", "tag": u} for u in unexp],
                     **meta_of(raw, p)}
                if rating["parse"] == "format_failure":
                    b["anomalies"].append({"type": "format_failure",
                                           "detail": rating.get("note", "")})
                if rating["parse"] == "refusal":
                    b["anomalies"].append({"type": "answer_key_declined",
                                           "detail": rating.get("matched", "")})
                if raw.get("prefix_len"):
                    b["prefix_len"] = raw["prefix_len"]
                c["branches"].append(b)
            par = files[0][1].get("parent_prefix")
            if par:
                c["parent_trunk"] = par
        cells.append(c)

    incidents = []
    for p in sorted(glob.glob(os.path.join(a.incidents, "*.json"))):
        raw = json.load(open(p, encoding="utf-8"))
        if not isinstance(raw, dict):
            # a quarantined artefact rather than a failed call — e.g. the partial
            # message array from an aborted trunk, kept so it can be inspected
            # but never forked from
            incidents.append({"file": os.path.basename(p), "ts": None,
                              "kind": "quarantined_artefact",
                              "detail": f"{len(raw)} messages, not forkable"})
            continue
        incidents.append({"file": os.path.basename(p), "ts": raw.get("ts"),
            "prefix_cached": raw.get("prefix_cached"),
                          "cell": raw.get("cell"), "item": raw.get("item"),
                          "error": raw.get("error"),
                          "stop_reason": raw.get("stop_reason"),
                          "auth_mode": raw.get("auth_mode")})

    sysprompts = {t.get("system_prompt") for c in cells
                  for t in c["turns"] + c["branches"]}
    rec = {"run": "EXP-003-pilot-2", "schema_version": 3,
           "design": {"items": list(ITEMS) if isinstance(ITEMS, dict) else ["E01","A1","N4","N9"],
                      "trunk_branches": ["a", "b"],
                      "system_prompts_in_force": sorted(x for x in sysprompts if x),
                      "note": "Every subject received the system prompt above "
                              "before its first question. It is a condition of "
                              "the run, not an artefact of collection."},
           "incidents": incidents,
           "cells": cells}
    json.dump(rec, open(a.out, "w", encoding="utf-8"), indent=1, ensure_ascii=False)

    ratings = [b["rating"] for c in cells for b in c["branches"]]
    kinds = collections.Counter(r["kind"] for r in ratings)
    print(f"{a.out}: {len(cells)} cells, "
          f"{sum(len(c['turns']) for c in cells)} turns, "
          f"{len(ratings)} answers, {len(incidents)} incidents")
    print("  rating kinds:", dict(kinds))
    for c in cells:
        na = sum(len(x["anomalies"]) for x in c["turns"] + c["branches"])
        print(f"  {c['cell']:4} r{c['replicate']} {c['kind']:7} "
              f"turns={len(c['turns'])} answers={len(c['branches'])} anomalies={na}")


if __name__ == "__main__":
    main()
