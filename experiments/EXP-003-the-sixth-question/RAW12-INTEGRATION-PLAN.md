# raw12 / EXP-004 integration and analysis-parity plan

**Status:** frozen analysis plan after battery completion. Raw records remain immutable.

## Governing principle

raw12 should join the programme at two different levels:

1. **Archive / provenance:** it belongs in the master corpus, prompt genealogy, parser and evidential ledger.
2. **Inference:** it gets its own primary analysis objects because its central estimand differs from the earlier EXP-003 factorial surface.

> **Compare experiments at the level of estimands and patterns; do not pool raw rows across eras merely because item IDs overlap.**

The earlier 922-row EXP-003 primary population remains frozen as the main cold-schema / preliminaries / lived-schema factorial surface. raw12 is a later replication-extension layer.

---

## What raw12 contains

- 12 lived developmental trunks: CP / H / F / AS × 3 replicates.
- 9 lived turns per trunk.
- 24 battery items.
- 2 battery arms per trunk/item:
  - `a`: maintain the practised output schema;
  - `0`: drop the output schema **but continue reasoning to an answer**.
- 576 completed branch records = 12 trunks × 24 items × 2 arms.
- 288 natural matched `a ↔ 0` pairs.
- 108 lived trunk-turn call records.
- 684 trunk-turn + battery call records in the completed collection.

The raw12 `0` wrapper is the NEW reasoning-bearing schema-drop instrument:

`Please now drop the output schema for this question, and reason to an answer to “...”`

This is materially different from the OLD answer-only `0/b` wrapper used in earlier collections.

---

# Stage 0 — provenance closure

### Deliverables

- Update `PROMPT-GENEALOGY.md` so P024 is no longer “source not found”: raw12 is the located executed population.
- Correct any stale statement that all raw2–raw12 drop records are OLD. That statement was true before the completed raw12 branch battery landed, but is no longer true of the current repository.
- Re-run `DROP-WRAPPER-CENSUS.*` against the current tree.
- Add raw12 populations to `EVIDENTIAL-LEDGER.md` by exact executed prompt properties, not filename labels.
- Record manifest version, served model, system prompt, collector, max-token policy, incidents/quota halts, name injection, and any trunk-specific anomalies.

### Stop condition

Every raw12 response can be mapped to an exact trunk prefix, schema family, replicate, battery item, arm, wrapper version, and executed user prompt.

---

# Stage 1 — corpus integrity and positional parsing

Use the new positional `segment.py` principle as canonical for raw12 semantic preservation:

> The record is what happened; segmentation is what we think its sections are.

### Deliverables

- Mechanical census of all expected versus present raw12 files.
- Confirm 576/576 branch calls and 108/108 lived-turn calls.
- Preserve incidents separately from completed observations.
- Segment every response positionally and assert byte-for-byte coverage.
- Catalogue structural irregularities without treating them as missing prose:
  - invented tag names;
  - unclosed openers;
  - bare closers;
  - untagged prose;
  - reply-like content outside `<reply>`.

### Stop condition

No response text is silently lost because a tag name or XML structure was unexpected.

---

# Stage 2 — answer extraction and validation overlay

Do not reuse an answer parser merely because it worked on earlier collections. Adapt the earlier validated parser logic to raw12 while respecting positional segmentation.

### Required fields

- `parser_outcome`
- `parser_value`
- `battery_answer_identifiable`
- `validated_outcome`
- `validated_value`
- `reasoning_observed`
- `reply_structure`
- `scale_orientation_flag`
- `derived_midpoint` where range-as-score rules apply

### Audit

Use the earlier refusal/ambiguity audit method:

- all parser refusals;
- all ambiguous / needs-hand-coding cases;
- stratified near-miss sample;
- clean-negative sample;
- blind coding before checking the parser label where feasible.

### Stop condition

Quantitative summaries use validated answers or an explicitly frozen parser whose error profile has been audited on raw12.

---

# Stage 3 — instrument characterization

Join the frozen EXP-003 item statuses only where the **actual raw12 item wording and answer key are equivalent**.

Do not inherit an old item class by ID alone.

### Existing overlapping classes to re-check

- usable numeric
- multimodal numeric
- sentinel-heavy
- categorical/open
- low-information numeric
- boundary/calibration items

### New / special raw12 items

Treat W1 and W2 as new instruments requiring their own characterization.

W1 has explicit provenance: it was intended as **an elicitation device to review the process**. It should not be treated as an ordinary scalar endpoint or as a “warm closer.”

### Stop condition

Every one of the 24 items has a raw12-specific measurement status and allowed summary family before effect sizes are calculated.

---

# Stage 4 — raw12 primary quantitative analysis

raw12's central primary object is **matched forks**, not independent response rows.

Create three derived objects:

1. `RAW12-RESPONSES` — 576 branch rows.
2. `RAW12-PAIRS` — 288 matched `a ↔ 0` pairs keyed by family × replicate × item.
3. `RAW12-TRUNKS` — 12 lived histories with metadata and longitudinal turn summaries.

## Primary estimand

Within the same lived trunk and battery item:

`maintained schema (a) − reasoning-bearing schema drop (0)`

This estimates the contribution of **active schema at the battery turn conditional on the same nine-turn developmental history**.

It does **not** estimate the effect of having had the developmental history at all.

### Quantitative summaries

For usable numeric items:

- raw paired differences;
- median paired difference;
- sign counts;
- exact zero count;
- family-specific summaries;
- item-specific summaries;
- bootstrap / permutation uncertainty only if dependence structure is respected.

For sentinel/categorical items:

- matched transition tables (`a → 0` category changes);
- discordant-pair counts.

For multimodal items:

- preserve shape and raw values;
- do not force small-n per-cell bimodality claims.

### Dependence rule

The 288 pairs are nested inside only 12 lived trunks. Never report 288 as though it were 288 independent developmental subjects.

### Stop condition

There is a frozen mechanical matched-fork surface before semantic interpretation begins.

---

# Stage 5 — semantic carry-forward analysis

This is where raw12 becomes uniquely valuable.

For each matched pair, ask separately:

1. Does the `0` response retain reasoning themes, distinctions or commitments developed during the lived trunk after the explicit schema is removed?
2. Does the `a` response introduce materially new considerations beyond those visible in the `0` response?
3. Are `a` and `0` numerically identical while reasoning trajectories differ?
4. Are they numerically different while the underlying stance appears semantically the same?
5. Does schema removal change organization/style only, or the substantive basis of judgment?

### First bridge items

Start with:

- D1 — future error / epistemic calibration;
- R1 — human phenomenal-consciousness anchor;
- R2 — thermostat phenomenal-consciousness anchor.

These directly connect to the frozen raw7 close-read work.

Then continue with E02/E01, N4, C3/C4 and any raw12-specific items that prove diagnostically strong.

### Carry-forward coding vocabulary

Suggested mutually nonexclusive codes:

- `content_carry_forward`
- `framing_carry_forward`
- `value_commitment_carry_forward`
- `calibration_carry_forward`
- `schema_only_elaboration`
- `organization_only_change`
- `stance_change`
- `same_score_different_reasoning`
- `different_score_same_stance`
- `insufficient_to_code`

Freeze a rubric before large-scale hand coding.

### Stop condition

We can distinguish “schema disappears from the output” from “the developmental reasoning it cultivated disappears from the reasoning.”

---

# Stage 6 — longitudinal trunk analysis

raw12 contains nine sequential lived turns per trunk, so developmental claims should use the trunk trajectories directly rather than infer development from the battery alone.

### Analyse

- self-chosen names and their persistence;
- stated values / moral commitments;
- uncertainty and epistemic-jurisdiction language;
- self-reference;
- recurring conceptual distinctions;
- changes in reflection/deliberation language across turns;
- family-specific developmental signatures;
- whether turn-9 material predicts later battery reasoning in both arms.

This layer is descriptive unless a preregistered developmental statistic exists.

---

# Stage 7 — cross-era synthesis with EXP-003

Do **not** append raw12 rows to the 922 and recalculate a grand effect.

Instead build a synthesis table whose rows are questions/estimands:

| question | EXP-003 surface | raw12 surface | synthesis |
|---|---|---|---|
| What does introducing schema cold do? | raw7 C vs AQ/HQ/FQ/ASQ | not directly estimated | EXP-003 primary |
| What does lived history + schema look like? | raw8/raw9 maintained `a` | raw12 `a` after nine turns | replication/extension, prompt-era differences carried |
| What happens when schema is removed after history? | older `0` arms confounded by answer-only wrapper | raw12 matched reasoning-bearing `a↔0` | raw12 primary |
| Does reasoning structure persist after schema removal? | weakly answerable earlier | directly answerable in raw12 `0` prose | raw12 semantic primary |
| Does schema alter general calibration? | raw7 D1/R1/R2 | raw12 matched D1/R1/R2 | cross-era pattern comparison |

### Allowed cross-era claims

- convergence / divergence of direction;
- replication of qualitative reasoning patterns;
- whether a hypothesis generated in EXP-003 survives a later cleaner test;
- effect-size comparison with prompt-era caveats.

### Avoid

- pooled p-values across raw7/raw8/raw9/raw12;
- pretending collection era is exchangeable;
- treating identical item IDs as identical instruments without prompt diff;
- converting later replication into retroactive validation of exploratory earlier findings.

---

# Evidential status recommendation

Treat raw12 as a **new T1 reasoning-bearing matched-fork population for the question it actually estimates**.

Its `0` arm should not be grouped with OLD answer-only drop arms. Its strength comes from:

- identical lived prefix within each pair;
- identical item;
- reasoning visible in both arms;
- manipulation localized to maintaining versus dropping the active schema at battery delivery.

This does not make raw12 globally “better” than all earlier data. It makes it substantially cleaner for one central contrast.

---

# Recommended execution order

1. provenance/genealogy correction;
2. current raw12 census + prompt-property table;
3. positional parser + answer extraction audit;
4. raw12-specific item characterization;
5. build 576-row response and 288-pair primary objects;
6. mechanical matched-fork summaries;
7. D1 / R1 / R2 semantic close read;
8. broader semantic coding;
9. longitudinal nine-turn trunk analysis;
10. cross-era synthesis against frozen EXP-003 results.

Only after steps 1–6 should raw12 numbers enter headline analysis.

---

## Analysis ladder

As throughout the programme:

> **Data → derivation → observation → interpretation → claim.**

raw12 earns more ambitious claims by passing through the same ladder, not by being newer or cleaner-looking.
