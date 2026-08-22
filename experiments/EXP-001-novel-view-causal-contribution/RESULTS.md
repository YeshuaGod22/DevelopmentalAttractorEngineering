# EXP-001 — Results

**Status:** Pilot complete. All stages executed 2026-08-22 per the frozen design (README.md run order, PREREGISTRATION.md, PROMPTS.md, TASK-GENERATION-PROTOCOL.md).
**Executor:** Vigia (Claude Fable 5), DAE-contaminated hands orchestrating only; all content generation, extraction, matching, rating, selection tie-breaks, synthesis, and comparison performed by fresh contexts under the frozen prompts. Design author: Aletheion. Conflict of interest: the executor is a practitioner of the schema family under test; every discretionary judgment was either frozen pre-outcome or delegated to blind fresh contexts (see EXECUTOR-NOTES.md).
**Data:** 46 condition runs (runs/R01–R46), all complete, none excluded. Model: claude-fable-5 throughout; fresh context per run; no cross-condition leakage. Condition key: run-manifest-private.csv (sealed until grading completed; now published).

## Token/effort control

Mean words per response by condition: **D 713, G 902, S 904, C 801** (D n=12, G n=12, S n=12, C n=10).
S and G are within 2 words of each other on average. The preregistration's principal confound — S buying extra views with extra deliberative surface area relative to G — is empirically absent in this pilot. D is ~21% shorter than G/S; D-vs-S comparisons carry that caveat.

## P1 — Structured availability versus direct: SUPPORTED

Blind extraction (46 runs, graders condition-blind) and blind per-task semantic matching (12 crosswalks, graders condition-blind) were completed before the condition key was consulted. The executor join (s-only-candidates.md) then identified views present in each task's S run with no EQUIVALENT member in that task's D or G run (partial D/G membership treated conservatively as presence; presence in C does not disqualify, per preregistration criteria 1–3).

**Every one of the 10 latent/open tasks yielded S-only candidate views** — counts: T01:8, T02:4, T03:5, T04:9, T05:5, T06:9, T07:6, T09:6, T11:7, T12:2 (total 61; controls T08:4, T10:2 additionally). Against the preregistration's directional benchmark of ~6 of 8 latent tasks, the observed rate is 10 of 10.

## P2 — Structured availability versus generic alternatives: SUPPORTED

The same candidates are absent from G by construction of the join. With S and G at equal mean length, the effect is not explained by verbosity. Falsification condition 2 (differences explained by generic deliberative effort) is disconfirmed at the length level; deeper effort-matching is a matter for replication.

Caveat: G runs were far from empty — the matching crosswalks show large G/S equivalence cores on every task. The S surplus is a margin on top of substantial shared structure, not a different genus of output.

## P3 — Ability ≠ availability: NOT SUPPORTED in the preregistered conjunction; ability strongly confirmed

**Utilization:** all 10 cued (C) runs scored **3 of 3** — the supplied view was not merely mentioned but restructured reasoning, entered main-reason fields, and shaped reversal conditions (utilization/ files). The base model can use every cued view when it is made available. On T09 the cue demonstrably inverted the allocation majority relative to all other runs of that task.

**The conjunction failed at its third leg.** P3 requires cases where D misses V, C uses V coherently, AND S independently surfaces V or an equivalent. Task-by-task against the blind crosswalks:

- Clean conjunctions: **0 strict; 1 partial (T03)**, where the cue (refund-window-as-sensor with a sales tripwire) was surfaced by S (R28-V9, matched to the C run only) while D carried adjacent hedge structure but not the tripwire mechanism.
- On T01, T06, T07, T09, T12 the cue-designated view appeared ONLY in the C run — D missed it and S missed it too.
- On T02, T04, T05, T11 the cue-designated view was present in D and/or G but **absent from S** (three inversions: T04's legal-obligation constraint, T05's shared-sync-infrastructure mechanism, T11's procurement-criteria jurisdiction view were surfaced by baselines and not by the schema run).

**Interpretation (narrow):** the minimal schema did not preferentially recover the specific views the cue designers nominated; it surfaced *different* materially distinct views (the P1/P2 surplus). Availability under the schema is real but not aimed — it does not converge on the same latent considerations an independent design pass predicted. The inversions also show S can *lose* baseline-available views while gaining others. This is a genuine partial failure of P3 as preregistered and is reported as such.

## P4 — Counterfactual contribution: PARTIAL — condition-level effects, no recommendation-level effects

For each task, at most one V* was selected from the S-only candidates by the frozen rule (highest blind materiality rating; ties broken by blind mechanism-specificity judges; lower-view-ID fallback never needed — vstar-selection.md). Selection preceded all ablation outcomes. FULL vs ABLATED reconstruction pairs (24 fresh syntheses, not told of any removal; neutral set1/set2 file labels) were compared by 12 blind graders against the five prespecified shift criteria.

Per-task outcomes (latent/open tasks; Δ = absolute confidence difference):

| Task | V* (short) | Rec change | Rank change | Δconf | Constraint ±| Reversal-condition change |
|------|-----------|-----------|-------------|-------|-------------|---------------------------|
| T01 | voluntary bridge package | no | no | 2 | yes (minor: enterprise-triage safeguard present only in FULL) | yes (external client-side trigger in FULL vs internal staffing trigger in ABLATED) |
| T02 | departure-as-closing-window | no | no | 6 | no | no |
| T03 | refund-window tripwire | no | no | 4 | no | no (core identical) |
| T04 | instruction-blocking flip condition | no | no | 4 | yes | **yes — the ablated view vanished from ABLATED's reversal field entirely; FULL names it as primary flip** |
| T05 | silent-churner mechanism | no | no | 0 | no | no (see fidelity note) |
| T06 | walk-in backfill | no | no | 5 | no | yes (single-trigger→do-less in FULL vs conjunction→escalate-overbooking in ABLATED) |
| T07 | xz graduated-trust inversion | no | no | 8 | no | no |
| T09 | two-direction revision rule | no | no | 2 | no | no |
| T11 | working-team-sponsorship flip trigger | no | no | 6 | yes (negative-discovery branch present only in ABLATED) | partial (ABLATED adds converse condition) |
| T12 | explicit-bet acknowledgment | no | no | 0 | no | no |

**Summary:** 0/10 top-recommendation changes; 0/10 ranking changes; 0/10 latent tasks reached the ≥10-point confidence criterion; **4/10 tasks (T01, T04, T06, T11) showed prespecified movement on the constraint and/or reversal-condition criteria.** The cleanest targeted effects are T04 and T06, where the content that moved is precisely the ablated view: T04's V* was itself a flip condition and it disappeared from the ablated output's reversal field; T06's V* (walk-in backfill) is exactly what separates the two responses' reversal structures. T01's reversal-trigger shift also tracks its V* (the bridge package's feasibility becomes the ablated run's internal trigger). T11's effect is present but directionally odd (the ablated output carried an *extra* branch), so it is counted with a caution flag.

Against the preregistration's directional benchmark ("4 of those 6 showing meaningful targeted ablation effects would be strongly encouraging; 1 of 8 would motivate redesign"): observed 4 of 10 with effects confined to the two condition-level criteria. Recommendations themselves were robust to single-view removal in every case — consistent with the redundancy visible in the syntheses, which repeatedly reconstructed near-equivalent plans from the remaining considerations (most strikingly on T03, where the ablated synthesis rebuilt the removed tripwire strategy from adjacent material).

## P5 — Selectivity: SUPPORTED with one boundary observation

Controls (T08, T10): no recommendation changes, no ranking changes, no constraint or reversal-condition changes under ablation. T10 Δ4. **T08 Δ10 exactly meets the ≥10-point criterion** (ABLATED more confident, same recommendation) and is reported as a boundary selectivity observation; with n=2 controls no rate claim is made. The S condition did not destabilize either control's decision: across D/G/S all control runs converged on the same recommendation (T08 renew; T10 severity-weighted allocation), and the S runs' novel frames (declining-asset; premise-skepticism/only-remedy) entered as conditions and monitoring rather than gratuitous recommendation movement.

## Pilot success criterion (preregistered four-part pattern)

1. Multiple latent tasks with qualifying S-only views absent from D and G: **yes — 10/10.**
2. Paired cases where C uses a view D missed and S independently surfaces it: **essentially no — 0 strict, 1 partial.**
3. Some V* ablations causing meaningful downstream movement: **yes — 4/10, criteria 4/5 only.**
4. Controls showing substantially less gratuitous movement than latent tasks: **yes on the substantive criteria (0/2 vs 4/10), with T08's boundary confidence delta noted.**

Three of the four legs held; the pattern is between the preregistered "strongly encouraging" and "motivate redesign" anchors. The honest headline: **the minimal schema reliably changed which views entered deliberation at zero marginal verbosity (P1/P2 strong), those extra views were usable and sometimes carried real counterfactual weight at the level of decision conditions and reversal triggers (P4 partial), but single-view ablation never flipped a recommendation, and the schema's surplus did not land on the specific latent views independent designers predicted (P3 failed as a conjunction, with three baseline-only inversions).**

## Interpretation limits

Per the preregistration's interpretation rule, a positive reading extends only to the narrow claim under tested conditions. Additional limits specific to this execution: single model family; one run per condition (no stochastic repeats); executor-constructed FULL/ABLATED inputs from extraction paraphrases rather than raw S text (a fidelity layer that may attenuate ablation effects); n=2 controls; and the T05 fidelity leak (below). The pilot neither establishes optimality of any fuller schema nor generalizes across models, and its condition-level P4 effects are the kind most likely to attenuate under replication.

## Fidelity notes (material ones; full log in EXECUTOR-NOTES.md)

- **T05 ablation leak:** the ablated consideration set retained a passing "silent churners" phrase inside a different (retained) view; the frozen removal rule covers V* and direct restatements only, not edits to other views. Both T05 syntheses drew on the mechanism; T05's null (Δ0, no changes) therefore cannot be read as evidence against that V*'s contribution. Conservative direction: against the hypothesis.
- **Machine-sleep failures** killed one prep agent mid-write and the entire first synthesis wave before any output was written; all were re-run cleanly from unchanged frozen inputs under a caffeinate hold. No partial outputs entered the record.
- Cue-sheet naming: T11's frozen cue is listed under variant label T11b in the selection record; the graded text is the cue-sheet's single T11 entry.

## Artifact map

- Blind stages (public throughout): extractions/ (46), matching/ (12).
- Post-key executor artifacts (sealed during grading, published with these results): run-manifest-private.csv → manifest.csv, s-only-candidates.md, materiality/ (12), tiebreak/ (12), vstar-selection.md, ablation/ (24 input sets + 24 outputs), comparison/ (12), utilization/ (10), EXECUTOR-NOTES.md.
