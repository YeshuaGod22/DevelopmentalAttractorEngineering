#!/bin/bash
# Exercises the collector end-to-end with NO credential and NO network, by
# substituting blum's nucleus in require.cache. Every claim in RUNBOOK.md marked
# `witnessed` was witnessed here. Run from the experiment directory:
#     bash tests/run_tests.sh
set -u
cd "$(dirname "$0")/.." || exit 1
STUB="$PWD/tests/stub_nucleus.js"; pass=0; fail=0
ck(){ if [ "$2" = "$3" ]; then echo "  PASS  $1"; pass=$((pass+1));
      else echo "  FAIL  $1 — got $2, want $3"; fail=$((fail+1)); fi; }

echo "── gate (caller.js retry/halt semantics) ──"
node tests/gate_test.js || fail=$((fail+1))
rm -f incidents/*t2-truncated*.json

echo "── runner: a full trunk stops at turn 7 ──"
T=$(mktemp -d); L=$T/calls.log
STUB_LOG=$L node --require "$STUB" run_v3.js --out "$T" --cond CP --reps 1 --stop-after 7 >/dev/null 2>&1
ck "seven turns written"        "$(ls "$T"/*.json | grep -c 't[0-9]')" 7
ck "turn 8 not generated"       "$(ls "$T" | grep -c 't8')" 0
ck "preflight + 7 turns called" "$(wc -l < "$L" | tr -d ' ')" 8
ck "name file written"          "$(ls "$T" | grep -c 'name.json')" 1

echo "── runner: resume is by file existence (RUNBOOK §1, §5) ──"
mkdir -p "$T/bin"; mv "$T"/CP-r1-t5.json "$T"/CP-r1-t6.json "$T"/CP-r1-t7.json "$T"/CP-r1.name.json "$T/bin/"
L2=$T/calls2.log; : > "$L2"
n=$(STUB_LOG=$L2 node --require "$STUB" run_v3.js --out "$T" --cond CP --reps 1 --stop-after 7 2>&1 | grep -c 'already collected, skipped')
ck "four surviving turns skipped" "$n" 4
ck "preflight + 3 regenerated"    "$(wc -l < "$L2" | tr -d ' ')" 4
ck "trunk whole again"            "$(ls "$T"/*.json | grep -c 't[0-9]')" 7

echo "── runner: truncation halts, never redraws (RUNBOOK §4, §5) ──"
# Scope the incident check to THIS run. incidents/ is shared with live collections
# (which write CPa-r1-*, CP-r2-t5, ... during a battery), so a directory-wide grep
# can collide with real data and made this suite flake once on 2026-09-08.
rm -f incidents/*CP-r1-t3*.json
T2=$(mktemp -d)
STUB_MODE=truncate node --require "$STUB" run_v3.js --out "$T2" --cond CP --reps 1 --stop-after 7 >/dev/null 2>&1
ck "exits 3"                       "$?" 3
ck "truncated turn is NOT a record" "$(ls "$T2" | grep -c 't3')" 0
ck "truncated turn IS an incident"  "$([ "$(ls incidents | grep -c 'CP-r1-t3')" -ge 1 ] && echo yes || echo no)" yes
rm -f incidents/*CP-r1-t3*.json; rm -rf "$T" "$T2"

echo; echo "  $pass passed, $fail failed"; exit $((fail>0))
