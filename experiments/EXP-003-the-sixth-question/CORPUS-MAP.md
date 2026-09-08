# EXP-003 Corpus Map

A descriptive front door to the physical corpus for **EXP-003 — The Sixth Question**.

This file deliberately contains **no interpretation of response content**. It answers only: what exists, how it is stored, what was configured, what completed, what failed or is absent, and what provenance survives.

Canonical machine-readable companion: [`CORPUS-MAP.json`](CORPUS-MAP.json).

Generator/checker: [`build_corpus_map.py`](build_corpus_map.py).

## Completed experimental-unit census

| source | completed units | snapshots / non-call companions | coverage |
|---|---:|---:|---|
| Pilot 1 (`raw/`) | 20 reconstructed units | 8 fork prompts + 4 prefix/snapshot files | complete reconstructed coverage |
| `raw2/` | 42 | 2 snapshots | complete |
| `raw3/` | 30 | 3 snapshots | complete |
| `raw4/` | 12 | 0 | complete |
| `raw5/` | 81 | 6 snapshots | physically complete; config source not uniquely located |
| `raw6/` | 148 | 0 | physically complete; instrument mapping unresolved |
| `raw7/` | 550 | 0 | complete |
| `raw8/` | 167 | 3 snapshots | 168 configured paths; 1 incident-backed gap |
| `raw9/` | 595 | 12 snapshots | 597 configured paths; 2 repository-absent gaps |
| `raw10/` | 50 | 0 | complete |
| `raw11/` | 112 | 2 snapshots | complete |

**Total completed experimental units: 1,807.**

Cross-checks:

- `raw2` through `raw10`: **1,675** completed call files.
- `raw11`: **112** additional completed calls.
- Pilot 1: **20** reconstructed experimental units from 12 JSONL session streams.

## Two storage eras

### Pilot 1

Pilot 1 uses session-event JSONL streams rather than one-file-per-call records.

- `raw/`: 12 `.raw.jsonl` streams.
- `forks/`: 8 prompt-text artifacts.
- `prefixes/`: 2 `.messages.json` snapshots + 2 `.prefix.txt` files.
- `ingest.py` reconstructs the experimental dialogue from user/assistant events while leaving other raw session events in the immutable JSONL.

Reconstructed Pilot-1 units:

| cell | units |
|---|---:|
| AS | 10 trunk turns: r1-r2 × Q1-Q5 |
| C0 | 8 cold items: r1-r2 × E01/A1/N4/N9 |
| ASb | 2 branch units: r1-r2 × N9/b |

Rule: **raw event count != reconstructed dialogue turn count != experimental unit count**.

### `raw2/` onward

From Pilot 2 onward, completed calls are stored as one JSON file per subject call. Frozen `*.messages.json` files are prefix snapshots and are not subject calls.

Core provenance fields observed from `raw2` onward include:

`cell`, `replicate`, `kind`, `sent`, `received`, `stop_reason`, `served_model`, `usage`, `error`, `ts`, `duration_ms`, `collected_via`, `auth_mode`, `system_prompt`.

Trunk records add `turn` / `question_id`. Branch records expose lineage fields including `branch`, `parent_prefix`, and `prefix_len`. Later records also expose fields such as `attempts` and `prefix_cached`.

## Coverage ledger

### `raw2`

Instrument: `cells.json`.

- C: 3 replicates × 4 items = 12
- H/F trunks: 2 × 5 turns = 10
- Ha/Fa/ASa: 3 × 4 items = 12
- ASb: 2 replicates × 4 items = 8

**42 configured / 42 completed.**

### `raw3`

Instrument: `cells3.json`.

- H/F/CP trunks: 3 × 6 turns = 18
- Ha/Fa/CPa: 3 × 4 items = 12

**30 configured / 30 completed.**

### `raw4`

Instrument: `cells4.json` — tested and not adopted.

Ha2/Fa2/CPa2 × 4 items = **12 configured / 12 completed**.

### `raw5`

**81 completed calls + 6 snapshots.**

Observed topology: K0/K1 × AS/F/H trunks, with `a` and `0` four-item branches. Physical coverage is closed; a unique dedicated config source was not located during this census.

### `raw6`

**148 completed calls, no snapshots.**

Observed topology:

- C: r1-r10 × five items = 50
- HQ: r1-r10 × five items = 50
- SCRa: r1 × 24 items = 24
- SCR0: r1 × 24 items = 24

`N8` is absent from both SCR branch populations. Physical coverage is closed; exact historical instrument-to-subpopulation mapping remains unresolved.

Do **not** attach `cells-FLOOR-C-n10.json` to `raw6` merely because both contain C at n=10: that snapshot specifies the full 25-item battery and belongs to the staged `raw7` extension.

### `raw7`

Staged instruments:

- `cells-FULL-cold.json`: 5 cells × n=1 × 25 items = 125
- `cells-FLOOR-n3.json`: add r2-r3 for 5 cells = 250
- `cells-FLOOR-C-n10.json`: add C r4-r10 = 175

Total: **550 configured / 550 completed**.

Observed final topology:

- C: r1-r10 × 25 = 250
- AQ: r1-r3 × 25 = 75
- HQ: r1-r3 × 25 = 75
- FQ: r1-r3 × 25 = 75
- ASQ: r1-r3 × 25 = 75

### `raw8`

Instrument: `cells-FULLTRUNK-H.json`.

At observed r1-r3:

- 6 FBH trunk turns per replicate
- 25 FBHa items per replicate
- 25 FBH0 items per replicate

Expected: **168**. Completed: **167**.

Missing completed path:

- `FBHa-r3-D1.json`

A matching incident artifact is preserved in `incidents/`.

### `raw9`

Instrument: `cells-FULLTRUNK-rest.json`.

Per replicate:

- four trunks × six turns = 24
- seven branch families × 25 items = 175
- total = 199

Across r1-r3: **597 configured paths**.

Completed: **595**.

Repository-absent configured paths:

- `FBASa-r3-A1.json`
- `FBASa-r3-C4.json`

No matching indexed incident artifact was found for either during this census. That is a repository-state observation, not proof that no historical attempt occurred.

### `raw10`

Instrument: `cells-DECODE-NOISE.json`.

- NOISEa: 25
- NOISE0: 25

**50 configured / 50 completed.**

### `raw11`

Instrument: `cells-AS-SELF.json` (exploratory).

- SSC trunk: 6
- SST trunk: 6
- SSCa: 25
- SSC0: 25
- SSTa: 25
- SST0: 25

**112 configured / 112 completed**, plus two frozen message snapshots.

## Incidents and anomalies

Keep attempt incidents separate from completed experimental units.

Observed incident shapes include:

1. call-shaped failures with empty `received`, `stop_reason: "error"`, null served-model/usage fields, and populated `error`;
2. quarantined partial prefixes stored as message arrays;
3. later branch-shaped failures preserving `parent_prefix`, `prefix_len`, and full sent-message provenance.

Pilot 1 also has reconstruction-level anomaly fields in `record.json` / `ingest.py` such as harness injections, orphan responses, multiple responses, missing sections, empty responses, and format failures.

The exact physical file count under `incidents/` was **not mechanically closed** during this census because the connector directory listing was truncated. Do not estimate it from the visible prefix of the listing.

## Data model

The corpus map keeps four descriptive layers distinct:

1. **ARTIFACTS** — every physical repository object.
2. **COVERAGE** — configured experimental paths and their repository status.
3. **CALLS** — completed experimental units only.
4. **INCIDENTS** — failed/partial attempts preserved separately.

Coverage status vocabulary:

- `completed`
- `incident`
- `absent`
- `not_applicable`

A physical directory is not automatically a run, and a run is not automatically a collection. Those identifiers remain separate unless the repository supports the join.

## Interpretive firewall

This map does not treat `FINDINGS.md`, derived annotations, preregistered watchlists, or prior prose summaries as corpus truth.

The governing rule is:

> **The record is what happened; the parser is what we think happened.**

And for this census:

> **Never reconcile what the repository has not reconciled.**

Response-content interpretation belongs in the final writeup, not here.
