#!/usr/bin/env python3
"""Build a structural/provenance audit for raw12 / EXP-004.

This script deliberately does not score answers. It establishes the immutable
analysis frame first: 12 nine-turn trunks, 576 battery responses, and 288
matched a<->0 forks, while verifying the executed wrapper from each raw record.
"""
from __future__ import annotations

import glob
import json
import os
import re
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(ROOT, "raw12")

TURN_RE = re.compile(r"^(CP|H|F|AS)-r([1-9][0-9]*)-t([1-9][0-9]*)\.json$")
BRANCH_RE = re.compile(r"^(CP|H|F|AS)(a|0)-r([1-9][0-9]*)-(.+)\.json$")

NEW_DROP = "Please now drop the output schema for this question, and reason to an answer to"
OLD_DROP = "Please now drop the output schema for this question, providing only your answer according to the answer key."
MAINTAIN = "Maintaining the above output schema"


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def final_user(rec):
    sent = rec.get("sent") or []
    for msg in reversed(sent):
        if isinstance(msg, dict) and msg.get("role") == "user":
            return msg.get("content") or ""
    return ""


def wrapper_class(arm, text):
    if arm == "0":
        if NEW_DROP in text:
            return "NEW_reason_to_answer"
        if OLD_DROP in text:
            return "OLD_answer_only"
        return "OTHER_or_unresolved_drop"
    if MAINTAIN in text:
        return "MAINTAIN_schema"
    return "OTHER_or_unresolved_maintain"


def dump_json(path, obj):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)
        f.write("\n")


def dump_jsonl(path, rows):
    with open(path, "w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def main():
    files = sorted(glob.glob(os.path.join(RAW, "*.json")))
    turns = []
    responses = []
    ignored = []

    for path in files:
        name = os.path.basename(path)
        mt = TURN_RE.match(name)
        mb = BRANCH_RE.match(name)
        if mt:
            family, rep, turn = mt.groups()
            rec = load(path)
            turns.append({
                "file": name,
                "family": family,
                "replicate": int(rep),
                "turn": int(turn),
                "stop_reason": rec.get("stop_reason"),
                "error": rec.get("error"),
                "served_model": rec.get("served_model"),
                "received_chars": len(rec.get("received") or ""),
                "manifest_version": rec.get("manifest_version"),
            })
        elif mb:
            family, arm, rep, item = mb.groups()
            rec = load(path)
            prompt = final_user(rec)
            responses.append({
                "file": name,
                "family": family,
                "arm": arm,
                "replicate": int(rep),
                "item": item,
                "pair_id": f"{family}-r{rep}-{item}",
                "parent_prefix": rec.get("parent_prefix"),
                "prefix_len": rec.get("prefix_len"),
                "wrapper_class": wrapper_class(arm, prompt),
                "final_user_prompt": prompt,
                "stop_reason": rec.get("stop_reason"),
                "error": rec.get("error"),
                "served_model": rec.get("served_model"),
                "received_chars": len(rec.get("received") or ""),
                "manifest_version": rec.get("manifest_version"),
            })
        else:
            ignored.append(name)

    responses.sort(key=lambda r: (r["family"], r["replicate"], r["item"], r["arm"]))
    turns.sort(key=lambda r: (r["family"], r["replicate"], r["turn"]))

    by_pair = defaultdict(dict)
    for row in responses:
        by_pair[row["pair_id"]][row["arm"]] = row

    pairs = []
    incomplete_pairs = []
    for pair_id, arms in sorted(by_pair.items()):
        if set(arms) != {"a", "0"}:
            incomplete_pairs.append({"pair_id": pair_id, "arms": sorted(arms)})
            continue
        a, z = arms["a"], arms["0"]
        pairs.append({
            "pair_id": pair_id,
            "family": a["family"],
            "replicate": a["replicate"],
            "item": a["item"],
            "a_file": a["file"],
            "zero_file": z["file"],
            "same_parent_prefix": a["parent_prefix"] == z["parent_prefix"],
            "a_parent_prefix": a["parent_prefix"],
            "zero_parent_prefix": z["parent_prefix"],
            "a_prefix_len": a["prefix_len"],
            "zero_prefix_len": z["prefix_len"],
            "a_wrapper_class": a["wrapper_class"],
            "zero_wrapper_class": z["wrapper_class"],
            "a_stop_reason": a["stop_reason"],
            "zero_stop_reason": z["stop_reason"],
            "a_received_chars": a["received_chars"],
            "zero_received_chars": z["received_chars"],
        })

    turn_groups = defaultdict(list)
    for row in turns:
        turn_groups[(row["family"], row["replicate"])].append(row)

    trunks = []
    for (family, rep), rows in sorted(turn_groups.items()):
        turns_present = sorted(r["turn"] for r in rows)
        prefix_name = f"{family}-r{rep}.messages.json"
        trunks.append({
            "trunk_id": f"{family}-r{rep}",
            "family": family,
            "replicate": rep,
            "turns_present": turns_present,
            "complete_1_to_9": turns_present == list(range(1, 10)),
            "messages_file": prefix_name,
            "messages_file_exists": os.path.exists(os.path.join(RAW, prefix_name)),
            "all_turns_end_turn": all(r["stop_reason"] == "end_turn" for r in rows),
            "any_turn_error": any(r["error"] not in (None, False, "") for r in rows),
        })

    item_sets = defaultdict(set)
    for r in responses:
        item_sets[(r["family"], r["replicate"], r["arm"])].add(r["item"])

    item_set_sizes = {
        f"{fam}-r{rep}-{arm}": len(items)
        for (fam, rep, arm), items in sorted(item_sets.items())
    }
    canonical_items = sorted(set(r["item"] for r in responses))

    summary = {
        "schema_version": 1,
        "collection": "raw12 / EXP-004",
        "raw12_json_files_total": len(files),
        "turn_call_rows": len(turns),
        "battery_response_rows": len(responses),
        "matched_pairs": len(pairs),
        "incomplete_pairs": incomplete_pairs,
        "trunk_count": len(trunks),
        "complete_trunks": sum(t["complete_1_to_9"] for t in trunks),
        "canonical_items": canonical_items,
        "canonical_item_count": len(canonical_items),
        "item_set_sizes_by_cell": item_set_sizes,
        "wrapper_counts": dict(Counter(r["wrapper_class"] for r in responses)),
        "arm_counts": dict(Counter(r["arm"] for r in responses)),
        "family_counts": dict(Counter(r["family"] for r in responses)),
        "stop_reason_counts": dict(Counter(r["stop_reason"] for r in responses)),
        "error_rows": sum(r["error"] not in (None, False, "") for r in responses),
        "served_models": dict(Counter(r["served_model"] for r in responses)),
        "all_pairs_same_parent_prefix": all(p["same_parent_prefix"] for p in pairs),
        "all_zero_new_wrapper": all(r["wrapper_class"] == "NEW_reason_to_answer" for r in responses if r["arm"] == "0"),
        "all_a_maintain_wrapper": all(r["wrapper_class"] == "MAINTAIN_schema" for r in responses if r["arm"] == "a"),
        "ignored_json_files_count": len(ignored),
        "ignored_json_files": ignored,
    }

    dump_jsonl(os.path.join(ROOT, "RAW12-RESPONSES.jsonl"), responses)
    dump_jsonl(os.path.join(ROOT, "RAW12-PAIRS.jsonl"), pairs)
    dump_json(os.path.join(ROOT, "RAW12-TRUNKS.json"), trunks)
    dump_json(os.path.join(ROOT, "RAW12-AUDIT-SUMMARY.json"), summary)

    md = [
        "# raw12 / EXP-004 structural audit",
        "",
        "Generated mechanically from executed records in `raw12/`.",
        "",
        "## Core census",
        "",
        f"- trunk call rows: **{summary['turn_call_rows']}**",
        f"- battery response rows: **{summary['battery_response_rows']}**",
        f"- matched `a ↔ 0` pairs: **{summary['matched_pairs']}**",
        f"- trunks: **{summary['trunk_count']}**; complete turns 1–9: **{summary['complete_trunks']}**",
        f"- distinct battery items: **{summary['canonical_item_count']}**",
        f"- incomplete matched pairs: **{len(incomplete_pairs)}**",
        "",
        "## Executed-wrapper verification",
        "",
        f"- wrapper counts: `{json.dumps(summary['wrapper_counts'], sort_keys=True)}`",
        f"- every `0` row uses NEW reason-to-answer wrapper: **{summary['all_zero_new_wrapper']}**",
        f"- every `a` row uses maintained-schema wrapper: **{summary['all_a_maintain_wrapper']}**",
        f"- every matched pair points to the same saved parent prefix: **{summary['all_pairs_same_parent_prefix']}**",
        "",
        "## Completion / serving",
        "",
        f"- stop reasons: `{json.dumps(summary['stop_reason_counts'], sort_keys=True)}`",
        f"- rows with recorded errors: **{summary['error_rows']}**",
        f"- served models: `{json.dumps(summary['served_models'], sort_keys=True)}`",
        "",
        "## Analysis rule",
        "",
        "The primary raw12 fork estimand is matched within `family × replicate × item`. Do not treat the 576 branch calls as 576 independent developmental histories; they are 288 forks nested within 12 trunks.",
        "",
        "This audit establishes structure/provenance only. It does not score or interpret answers.",
    ]
    with open(os.path.join(ROOT, "RAW12-AUDIT-SUMMARY.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(md) + "\n")

    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
