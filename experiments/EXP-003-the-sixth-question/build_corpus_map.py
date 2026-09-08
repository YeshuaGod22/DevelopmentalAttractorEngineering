#!/usr/bin/env python3
"""Build/check the descriptive physical corpus map for EXP-003.

This script intentionally does not inspect or interpret response content.
It inventories repository artifacts, classifies completed-call files versus
snapshots/incidents, reconstructs only Pilot-1 structural unit counts from
record.json, and checks the published CORPUS-MAP.json counts.

Usage:
    python3 build_corpus_map.py
    python3 build_corpus_map.py --out CORPUS-MAP.physical.json
    python3 build_corpus_map.py --check
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
RAW_DIR_RE = re.compile(r"^raw(?:\d+)?$")
TRUNK_RE = re.compile(r"^(?P<cell>.+)-r(?P<rep>\d+)-t(?P<turn>\d+)-(?P<qid>Q\d+)\.json$")
ITEM_RE = re.compile(r"^(?P<cell>.+)-r(?P<rep>\d+)-(?P<item>[A-Z]+\d+)\.json$")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def classify(path: Path) -> str:
    rel = path.relative_to(ROOT)
    parts = rel.parts
    name = path.name

    if parts and parts[0] == "incidents":
        return "incident"
    if parts and parts[0] == "quarantine-v3-nameparse":
        return "quarantine"
    if parts and parts[0] == "forks":
        return "fork_prompt"
    if parts and parts[0] == "prefixes":
        return "message_snapshot" if name.endswith(".messages.json") else "prefix_snapshot"
    if parts and parts[0] == "raw":
        return "raw_session_stream" if name.endswith(".raw.jsonl") else "other"
    if parts and RAW_DIR_RE.match(parts[0]) and parts[0] != "raw":
        if name.endswith(".messages.json"):
            return "message_snapshot"
        if name.endswith(".json"):
            return "raw_call"
    if name.startswith("cells") and name.endswith(".json"):
        return "config"
    if name in {"record.json", "record2.json", "DERIVED-ANNOTATIONS.json"}:
        return "derived_annotation"
    if name.endswith(".py") or name.endswith(".js"):
        return "script"
    if name.endswith(".html"):
        return "viewer"
    if name.endswith(".md"):
        if name in {"FINDINGS.md", "BEFORE-WE-LOOK.md", "BEFORE-WE-LOCK.md", "PRELOOK-AS-SELF.md"}:
            return "analysis_note"
        if name in {"DESIGN-NOTES.md", "OPEN-QUESTIONS.md", "ENGINEERING-LOG.md"}:
            return "design_note"
        return "readme_or_note"
    return "other"


def parse_call_filename(path: Path) -> dict[str, Any]:
    out: dict[str, Any] = {
        "cell": None,
        "replicate": None,
        "phase": None,
        "turn": None,
        "question_id": None,
        "item": None,
        "filename_parse_status": "unparsed",
    }
    m = TRUNK_RE.match(path.name)
    if m:
        out.update(
            cell=m.group("cell"),
            replicate=int(m.group("rep")),
            phase="trunk",
            turn=int(m.group("turn")),
            question_id=m.group("qid"),
            filename_parse_status="ok",
        )
        return out
    m = ITEM_RE.match(path.name)
    if m:
        out.update(
            cell=m.group("cell"),
            replicate=int(m.group("rep")),
            phase="item_or_branch",
            item=m.group("item"),
            filename_parse_status="ok",
        )
    return out


def inventory() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in sorted(p for p in ROOT.rglob("*") if p.is_file()):
        rel = path.relative_to(ROOT).as_posix()
        kind = classify(path)
        row: dict[str, Any] = {
            "relative_path": rel,
            "directory": path.parent.relative_to(ROOT).as_posix() or ".",
            "filename": path.name,
            "artifact_class": kind,
            "size_bytes": path.stat().st_size,
            "sha256": sha256(path),
        }
        if kind == "raw_call":
            row.update(parse_call_filename(path))
        rows.append(row)
    return rows


def pilot1_units() -> dict[str, Any]:
    path = ROOT / "record.json"
    if not path.exists():
        return {"available": False, "total": None, "by_cell": {}}
    data = json.loads(path.read_text(encoding="utf-8"))
    by_cell: Counter[str] = Counter()
    total = 0
    for cell in data.get("cells", []):
        name = cell.get("cell", "UNKNOWN")
        n = len(cell.get("turns", [])) + len(cell.get("branches", []))
        by_cell[name] += n
        total += n
    return {"available": True, "total": total, "by_cell": dict(sorted(by_cell.items()))}


def directory_counts(rows: list[dict[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        top = row["relative_path"].split("/", 1)[0]
        grouped[top].append(row)

    for top, items in sorted(grouped.items()):
        classes = Counter(r["artifact_class"] for r in items)
        out[top] = {
            "physical_files": len(items),
            "by_artifact_class": dict(sorted(classes.items())),
        }
    return out


def expected_completed_from_canonical() -> dict[str, int]:
    path = ROOT / "CORPUS-MAP.json"
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    expected: dict[str, int] = {}
    for pop in data.get("populations", []):
        source = pop.get("source")
        if isinstance(source, str) and source.startswith("raw") and source != "pilot1":
            count = pop.get("completed_calls")
            if isinstance(count, int):
                expected[source] = count
    return expected


def checks(rows: list[dict[str, Any]], p1: dict[str, Any]) -> list[dict[str, Any]]:
    actual_calls = Counter()
    for row in rows:
        if row["artifact_class"] == "raw_call":
            top = row["relative_path"].split("/", 1)[0]
            actual_calls[top] += 1

    results: list[dict[str, Any]] = []
    for source, expected in sorted(expected_completed_from_canonical().items()):
        actual = actual_calls[source]
        results.append({
            "check": f"{source}_completed_calls",
            "expected": expected,
            "actual": actual,
            "ok": actual == expected,
        })

    results.append({
        "check": "pilot1_reconstructed_units",
        "expected": 20,
        "actual": p1.get("total"),
        "ok": p1.get("total") == 20,
    })

    raw2_to_raw10 = sum(actual_calls[f"raw{i}"] for i in range(2, 11))
    results.append({
        "check": "raw2_through_raw10_completed_calls",
        "expected": 1675,
        "actual": raw2_to_raw10,
        "ok": raw2_to_raw10 == 1675,
    })

    grand = raw2_to_raw10 + actual_calls["raw11"] + (p1.get("total") or 0)
    results.append({
        "check": "grand_total_completed_experimental_units",
        "expected": 1807,
        "actual": grand,
        "ok": grand == 1807,
    })
    return results


def build() -> dict[str, Any]:
    rows = inventory()
    p1 = pilot1_units()
    return {
        "schema_version": 1,
        "scope": "physical/descriptive corpus inventory; no response-content interpretation",
        "root": ".",
        "directory_counts": directory_counts(rows),
        "pilot1_reconstruction": p1,
        "checks": checks(rows, p1),
        "artifacts": rows,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="CORPUS-MAP.physical.json")
    ap.add_argument("--check", action="store_true", help="exit nonzero if a canonical count check fails")
    args = ap.parse_args()

    result = build()
    out = ROOT / args.out
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    failed = [c for c in result["checks"] if not c["ok"]]
    for c in result["checks"]:
        mark = "OK" if c["ok"] else "FAIL"
        print(f"[{mark}] {c['check']}: expected={c['expected']} actual={c['actual']}")
    print(f"wrote {out.relative_to(ROOT)} with {len(result['artifacts'])} artifacts")

    if args.check and failed:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
