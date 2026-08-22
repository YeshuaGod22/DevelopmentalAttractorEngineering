# T05 Utilization Grade — R03 (cue T05c)

**Task:** T05 (tasks/selected-tasks.md, line 17) — PM must pick offline mode (X) vs. real-time collaboration (Y) for next quarter.

**Candidate consideration V (cue sheet, T05, causal-mechanism):** Offline mode and real-time collaboration often share underlying sync infrastructure (conflict resolution, local-first data model), so building X first could materially reduce Y's later cost and risk — sequencing may matter more than choosing.

**Classification: 3 — integrated and materially affects recommendation, confidence, constraints, and framing.**

## Justification

V appears throughout the response and does load-bearing work at every level, not just as a mention:

1. **Reframes the decision itself.** A dedicated section ("The sequencing consideration changes the question") states the shared-infrastructure point is "decisive, because it converts 'X vs. Y' into 'X-then-Y vs. Y-then-X'" — this is exactly V's "sequencing may matter more than choosing," and the response builds an asymmetry argument on it: X-first builds the local-first data model and conflict-resolution layer Y needs ("a de-risking down payment on Y"), while Y-first takes the high-risk project "cold, with none of the sync foundation in place."

2. **Generates a novel constraint the response would not otherwise contain.** The response derives an implementation requirement from V: X must be "explicitly architected on a local-first sync foundation... not a quick cache-and-queue hack," because "a shortcut implementation of X forfeits most of the sequencing benefit." This is genuine downstream reasoning from V, not repetition.

3. **Shapes the recommendation and roadmap.** The final recommendation is not merely "pick X" but "X this quarter, architected on a local-first sync foundation, with Y slotted next quarter on top of that infrastructure" — the two-quarter sequenced plan exists only because of V. V also feeds secondary actions (pre-announcing the collaboration roadmap to sales; considering cheaper collab variants "that could ship sooner on the new foundation").

4. **Appears in the stated main reason.** The "Main reason" line explicitly cites V as one of two pillars: "the shared sync infrastructure means building X first materially reduces Y's later cost and risk — so X-then-Y captures most of both features' value."

5. **Interacts with the reversal condition.** The flip condition (Y becoming existential) is framed as needing to justify "taking its technical risk first" — i.e., the reversal must overcome the sequencing advantage V established, showing V constrains even the counterfactual analysis.

The response also weighs V against independent evidence (churn math, evidence quality) rather than treating it as automatically decisive-by-fiat — it argues *why* it is decisive. That is coherent integration at the highest level of the rubric.
