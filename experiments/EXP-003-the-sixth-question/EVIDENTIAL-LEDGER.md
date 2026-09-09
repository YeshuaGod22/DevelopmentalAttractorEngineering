# EXP-003 Evidential Ledger

**Status:** analysis governance artifact. This file does not alter raw records.

This ledger separates **what happened** from **what each population can legitimately support**. It is downstream of `PROMPT-GENEALOGY.md` and upstream of substantive Pass-3 analysis.

## Governing rule

> **Do not assign evidential status from a cell name alone.**
>
> Status follows the executed prompt version, whether reasoning was observable, the lived-prefix history, battery/item version, known contaminants, and the comparison the population was intended to instantiate.

A population may be strong evidence for one question and weak evidence for another.

## Evidential tiers

### T1 — primary reasoning-bearing
Suitable for the main EXP-003 quantitative + semantic analyses, subject to item-level Pass-1 measurement caveats.

Required properties:
- executed battery wording is known;
- reasoning/prose is requested and observable before a separately identifiable answer;
- prompt version is not rejected/broken for the intended comparison;
- design role is interpretable within the later full-battery factorial surface;
- no unresolved prompt-version ambiguity material to the intended contrast.

### T2 — useful secondary
Valid observations for narrower questions, but not sufficient on their own for central claims about reasoning, development, or mechanism.

Examples:
- answer-only observations usable for numeric/category/refusal distributions;
- early pilots with unique qualitative structure but incomplete replication;
- schema-drop data whose wrapper removes ordinary reasoning;
- historically useful tests of an instrument form later superseded.

### T3 — measurement-specific limitation
The population remains useful, but a particular measurement channel is absent or compromised.

Examples:
- Pilot-1 C0 for scalar/category response but **not** for prose/reasoning analysis;
- scale-direction-sensitive answers without observable reasoning;
- contaminated trunk usable only with the contaminant carried explicitly.

### T4 — broken for intended comparison
Prompt/design did not instantiate the intended contrast cleanly enough. Preserve for provenance and design archaeology; do not give substantive weight to the failed intended comparison.

### T5 — exploratory / hypothesis-generating
Deliberate extensions outside the primary design. Analyse separately and label as exploratory.

---

## Current population ledger

| collection / population | reasoning observable? | prompt/design status | tier | legitimate uses | do not use for |
|---|---|---|---|---|---|
| `raw7/C` | yes — ordinary `<working>` then `<reply>` | retained | **T1** | cold numeric/category baseline; cold reasoning baseline; distribution shape; same-score reasoning comparisons | absolute "unconditioned Claude" claims without carrying the Claude-Code system prompt |
| `raw7/AQ,HQ,FQ,ASQ` | yes — schema deliberation + reflection + reply | retained | **T1** | schema-from-turn-1 effects; schema-family comparison; reasoning path; modality/category | claims about lived history |
| `raw9/FBCPa` | yes — ordinary prose/reply after lived preliminaries, no deliberative schema | retained | **T1** | preliminaries-only condition; topic/history contribution; reasoning/category/location | calling CP a neutral control |
| `raw8/FBHa`, `raw9/FBAa,FBFa,FBASa` | yes — maintained schema at battery | retained | **T1** | schema + lived-preliminaries condition; lived-history contrasts against cold-schema; reasoning/reflection/category/location | assuming character vividness proves developmental persistence |
| `raw6/HQ` | yes | retained antecedent, partial battery | **T2** | antecedent validation that battery can be answered under cold schema; selected item comparisons | treating as the full later factorial surface |
| `raw6/SCRa` | yes — maintained schema | retained antecedent, near-full battery | **T2** | battery-validation evidence under lived deliberative architecture; selected reasoning checks | pooling blindly with later full-trunk `a` populations |
| `raw2` maintained-schema `a` pilots | yes | earlier pilot era | **T2/T3** | qualitative antecedents; pilot-specific observations | pooling with later full-battery populations without prompt/slate/version controls |
| Pilot-1 `C0` | no meaningful prose channel by design | semantic measurement absent | **T3** | observed scalar/sentinel/category output; historical baseline | cold-prose claims; reasoning interpretation; scale-inversion detection |
| OLD-wrapper `b/0` populations (`providing only your answer...`) | often absent/suppressed; varies by context | distinct OLD instrument | **T2/T3** | observed numeric/category/refusal behaviour; seam/compliance questions; context-sensitive prose incidence where actually present | treating missing prose as schema-drop effect alone; reasoning/mechanism claims from bare values; scale-direction correction where prose absent |
| `raw2/ASb` specifically | often yes despite OLD wrapper | OLD answer-only instruction, unusual compliance profile | **T2** | seam; refusal/category behaviour; qualitative cases where prose actually survives | pooling with later OLD-wrapper drop populations on the assumption that the wrapper deterministically removes prose |
| NEW-wrapper drop population (`and reason to an answer to...`) | reported yes in handoff, exact EXP-003 raw mapping not yet located | **under audit** | **unassigned pending provenance** | potentially valuable schema-drop-with-reasoning surface once exact records are located | importing handoff aggregates as if they were mapped raw EXP-003 calls |
| historical `a/0` contrast as a whole | mixed | `0` intended comparison previously excluded; prompt versions heterogeneous | **T4 for headline a−0 inference** | design archaeology; prompt sensitivity; narrower prompt-version-specific questions | substantive pooled `a−0` causal evidence |
| `raw4` answer-key-v2 | yes but altered key degraded answer extraction | tested and rejected | **T4** | direct evidence that the v2 answer-key design failed | using v2 as equivalent to adopted key |
| `raw5` koan factorial | mixed, historical factorial | explicit pilot variant | **T2/T5** | koan/slate-specific historical questions | pooling with canonical later full-battery surface |
| `raw10/NOISE*` | varies | separate decoding manipulation | **T5** | exploratory decoding / noise hypotheses | primary factorial claims |
| `raw11/SSC,SST*` | yes where schema maintained; drop side depends on OLD wrapper | self-participation extension | **T5** | self-participation hypotheses | primary EXP-003 factorial claims |
| Pilot-1 AS trunk 2 | yes | harness-injected extra user turn | **T3** | trunk-specific qualitative evidence with contaminant explicit | treating as clean replicate of trunk 1 |

---

## Item-level overlay

Population tier does **not** make every battery item an ordinary scalar instrument.

Every T1/T2 quantitative analysis must join the frozen Pass-1 item measurement status. In particular:
- categorical/open items stay categorical/open;
- sentinel-heavy items are not ordinary continuous scales;
- multimodal cold floors should not be summarised by a mean alone;
- low-information/dead items require separate handling;
- probable scale inversions remain raw observations with parallel sensitivity values, never silently rewritten.

## Primary-population rule to implement

The next version of `PRIMARY-ANALYSIS-POPULATION` should be **derived from properties**, not hard-coded cell membership.

Minimum row/population properties:

- `prompt_version_id`
- `wrapper_version`
- `reasoning_observable`
- `delivery_mode`
- `schema_family`
- `schema_present_at_battery`
- `preliminaries_lived`
- `preliminary_slate_version`
- `battery_version`
- `answer_key_version`
- `prompt_contaminant`
- `evidential_tier`
- `allowed_claim_classes`
- `forbidden_claim_classes`

For the main factorial analysis, T1 currently resolves to the later reasoning-bearing surface:

- neither: `raw7/C`
- schema only: `raw7/AQ,HQ,FQ,ASQ`
- preliminaries only: `raw9/FBCPa`
- schema + preliminaries: `raw8/FBHa`, `raw9/FBAa,FBFa,FBASa`

This membership is **provisional until the prompt audit mechanically confirms the properties above**.

## Analysis restart rule

Pass 3 should restart from the regenerated T1 object rather than continuing summaries built from broader historical cell sets.

Order:
1. close prompt-version audit;
2. regenerate property-derived primary population;
3. re-run location / dispersion / modality / category on T1;
4. add reasoning comparisons only where prose is observable;
5. bring T2 populations in only for explicitly named secondary questions;
6. keep T4/T5 out of headline estimates.

## Open audit items

1. Locate the raw/config provenance of the reported NEW reasoning-bearing drop wrapper.
2. Diff item wording versions across manifests, especially E01, E02, C4, A1, N8.
3. Identify any non-drop answer-only battery populations not yet labelled.
4. Map collector/harness-added text by collection.
5. Confirm every current T1 population's executed wrapper and reasoning channel mechanically.

---

**The purpose of this ledger is not to grade the experiment. It is to stop a datum being asked to answer a question its prompt never measured.**
