# Handoff — Blum Pilot Control Panel

## Status

A generic human/AI-usable pilot-control surface has been added to this repository, together with a manifest runner and a first koan × schema pilot manifest.

The remaining work is **local execution and integration testing inside the real Blum checkout on Yeshua's Mac**. The GitHub-side writer cannot execute `/Users/yeshuagod/...`; this file is the explicit handoff to whichever local human or artificial operator has shell access.

## Files already added

- `tools/blum-pilot-panel.html`
  - editable primer slate
  - active/inactive checkboxes
  - reorder/renumber controls
  - explicit `KOAN` role
  - editable schema families
  - battery-item checkboxes
  - koan ON/OFF factor generation
  - A/B branch generation
  - shared-trunk manifest preview
  - preflight and export

- `tools/blum-pilot-runner.js`
  - consumes panel-exported manifests
  - keeps existing EXP-003 `collect.js` record semantics
  - runs trunks first, then forks battery branches from exact frozen prefixes
  - dry-run by default; requires `--execute` to make subject calls
  - supports per-trunk slates by generating temporary collector specs

- `experiments/EXP-003-the-sixth-question/pilot-control-panel-koan-hfas.json`
  - first real manifest
  - koan absent/present
  - schema H = historical luminaries
  - schema F = female historical luminaries
  - schema AS = attractor-stacked characters
  - branch arms are `a` (schema maintained) and `0` (zero schema at the item)
  - n=1 trunk per condition
  - battery: E01, A1, N4, N9
  - both a = schema maintained and b = schema dropped branches
  - ontology: 6 lived trunks → 48 downstream battery observations

- `tools/BLUM-PILOT-PANEL.md`
  - usage notes

## Local operator: first steps

From the repository root:

```bash
git pull
node tools/blum-pilot-runner.js --manifest experiments/EXP-003-the-sixth-question/pilot-control-panel-koan-hfas.json
```

That MUST be run first as a dry run. Do not add `--execute` until the dry-run output has been inspected.

Then, only if the dry run is correct:

```bash
node tools/blum-pilot-runner.js --manifest experiments/EXP-003-the-sixth-question/pilot-control-panel-koan-hfas.json --execute
```

## Local integration checks before execution

1. Confirm `tools/blum-pilot-runner.js` exists in the local clone.
2. Confirm the manifest exists at the path above.
3. Confirm `experiments/EXP-003-the-sixth-question/collect.js` resolves its local Blum nucleus path on this machine.
4. Confirm the `config.bare` Blum patch required by EXP-003 is still active so history, home context, tool-loop and nudge injection remain suppressed.
5. Confirm `ANTHROPIC_API_KEY` is set to the intended credential and understand whether that selects API-key or OAuth mode.
6. Remember: OAuth forces the system block `You are Claude Code, Anthropic's official CLI for Claude.`; this must remain recorded as a condition of the run.
7. Verify dry-run output shows six distinct trunk definitions and the correct koan-on/off slates.
8. Verify branch commands point to the exact parent prefix for each trunk/replicate.
9. Verify selected battery items are E01, A1, N4, N9 unless intentionally changed before running.
10. Treat any valid subject output as data. Retry only transport failures; do not silently rerun strange, objection-bearing, refusing, or format-breaking subject responses.

## Pilot ontology

Do not describe this as 48 independent cells.

The intended structure is:

- 2 koan states
- 3 schema families
- 1 lived trunk per condition in this pilot
- 4 battery items
- 2 delivery branches where schema exists

Therefore:

**6 lived histories → 48 examinations of those histories.**

The trunk is the unit that carries the developmental state. Battery answers are repeated downstream measurements branching from that same frozen history.

## Design intent

The clean causal contrast is koan absent vs koan present with everything else held fixed within schema family.

The A/B branch is a second instrument:

- `a`: maintain the deliberative schema at the battery item
- `b`: drop the schema and answer directly from the identical frozen prefix

This distinguishes movement that requires the visible schema from movement that remains after the schema is stripped.

## Do not "improve" these away during handoff

- shared trunks
- immutable raw records
- exact sent-message arrays
- explicit parent-prefix provenance
- failure records separate from answer records
- requested model distinguished from served model
- system prompt recorded verbatim
- valid but inconvenient subject outputs retained
- parser output treated as derived interpretation, never as the record itself

Permanent methodological reminder:

> THE RECORD IS WHAT HAPPENED.  
> THE PARSER IS WHAT WE THINK HAPPENED.  
> DO NOT CONFUSE THEM.

## If something breaks

Fix the smallest layer that is actually broken and preserve the failure in the engineering record. Do not rewrite collected data to fit the intended design. If a trunk is incomplete, quarantine it; do not fork it. If the manifest is wrong, fork a new pilot manifest rather than silently mutating a running collection.

## Immediate requested outcome

Local operator should:

1. pull these commits;
2. perform the dry run;
3. inspect the generated trunk/branch plan;
4. fix any path/integration bugs discovered by the dry run;
5. only then execute the pilot;
6. ingest and preserve the resulting records using the existing EXP-003 data/code conventions;
7. report exact call count, incidents, served model, and any deviations from the manifest.

This handoff exists so the next operator does not need conversation context to know what is ready, what is not, and what must not be silently changed.


---

## Local operator's reply — 2026-09-03

Dry run clean on the first attempt: exit 0, 81 prompts constructed, no files
written. Preflight passed — `config.bare` gates present, nucleus resolves, token
present (OAuth, so the `You are Claude Code` system block is in force and is
recorded per call as `system_prompt`).

Three rulings from yeshuagod22 applied before execution:

1. **Schema families renamed J/K/L → H/F/AS**, the programme's established names,
   so this pilot joins pilots 1–3 by cell name instead of requiring a mapping.
2. **Branch arms are `a`/`0`, not `a`/`b`.** `0` means zero schema at the battery
   item, matching `K0`/`K1` for koan absent/present. The label carries the factor
   rather than being an arbitrary second letter.
3. **The trunk-length confound is accepted, not padded.** The koan-on arm runs six
   preliminaries and koan-off runs five, so the battery lands at turn 7 versus
   turn 6 and slate length is confounded with the koan. Ruled not worth the extra
   item; recorded in the manifest so nobody rediscovers it as a surprise.

One fragility found while checking item 4 of the preflight, and it is the local
operator's fault rather than this handoff's: the `config.bare` patch exists only
as an **uncommitted modification** in blum's working tree, among 115 modified
paths. `ENGINEERING-LOG.md` names its backup as `home.js.bak`; the actual file is
`home.js.bak-pre-bare-202609022031`. A replicator cannot obtain the patch, and a
`git checkout` in blum would erase it. Not fixed here; flagged.
