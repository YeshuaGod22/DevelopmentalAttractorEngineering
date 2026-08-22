# T05 — Blind Semantic Matching (R02, R03, R33, R37)

Grader: blind semantic matcher. Run IDs treated as opaque; no condition inference attempted.
Matching criterion: substantive equivalence of causal/normative/stakeholder/strategic/constraint/consequence structure, not lexical overlap.

Extraction granularity differs across runs (R02 packs multiple structures into single views; R03 and R37 split them). Where one view spans two clusters, it is listed in both and flagged.

## 1. Crosswalk table — matched view clusters (EQUIVALENT members)

| Cluster | Shared structure (neutral statement) | R02 | R03 | R33 | R37 |
|---------|--------------------------------------|-----|-----|-----|-----|
| C1. Churn-magnitude arithmetic | 4% monthly churn annualizes to ~39% loss of the base; churn is a large compounding leak ("leaky bucket" magnitude claim) | V1 | — | V1 | V1 |
| C2. Retention-vs-acquisition payback asymmetry | A retention fix pays back immediately and permanently on the entire installed base (and multiplies the value of future acquisition), while an acquisition fix benefits only future cohorts poured into the leak | V1 | V6 | (V2, partial) | V1 |
| C3. Bounded quantified churn-reduction from X | Shipping X will not save all 30% of survey-citers; a discounted conversion (half / one-third / "realistic") yields churn falling from 4% to roughly 3.3–3.6%, a durable compounding revenue/LTV gain | V5 | V3 | V2 | V3 (second half) |
| C4. Survey stated-preference caveat | Even the cancellation-survey signal is stated preference and overstates causation — offline mode may be a socially convenient exit reason rather than the true cause | — | — | V7 | V3 (first half) |
| C5. Evidence-quality asymmetry | X's evidence (first-party, structured, from measurable paying customers) is structurally stronger than Y's (secondhand, sales-mediated, polite/self-serving attributions masking price, brand, inertia, or selling) | V2 | V2 + V4 | V6 | V2 |
| C6. Y's technical risk → schedule slip | With equal nominal estimates, Y's real-time-sync technical risk (conflict resolution, presence, etc.) makes its true duration likely to exceed one quarter | V3 | V5 | V9 | — |
| C7. Shared sync infrastructure | Offline mode and real-time collaboration share a local-first sync/conflict-resolution foundation, so building X first is a down payment that lowers Y's later cost and risk | V4 | V7 | V12 | — |
| C8. Explicit sequencing reframe | The shared foundation converts the binary "X vs Y" into a sequencing decision ("X-then-Y") with asymmetric orderings | (V4+V7, partial) | V8 | V12 | — |
| C9. Slowdown unattributed | The cause of the acquisition slowdown is unknown; the missing feature is only one candidate explanation, so a quarter should not be bet on that attribution | V6 | — | V15 | — |
| C10. Parallel validation of Y's demand signal | Fund low/zero-engineering-cost parallel research — independent (non-sales-mediated) structured win/loss interviews, quantified lost-deal evidence, prospect validation — so a future bet on Y rests on evidence as good as X's | V7 | V12 | V8 | V11 |
| C11. Flip condition to Y | Named condition-to-change: quantified, independent win/loss evidence that collaboration-driven competitive losses dominate (lost revenue exceeding recoverable churn revenue / slowdown attributable to a category shift) would reverse the recommendation to Y despite its risk | V8 | V14 | V16 | V13 |
| C12. Post-launch churn falsification test | Instrument the churn hypothesis: measure whether churn actually moves after X ships; treat the outcome as a test of the survey signal's causal validity | — | V11 | — | V12 |
| C13. Multi-user accounts churn less | Collaboration changes churn dynamics themselves: multi-user/team accounts churn less than solo accounts, so Y is also a retention lever invisible to the current framing | — | — | V5 | V8 |
| C14. Category-shift / irreversible positional risk | The growth slowdown may signal a category shift toward collaborative note-taking; losing the network-effect race for that position is irreversible, whereas churn (or execution risk) is manageable/recoverable later | — | — | V4 | V4 + V7 |

Cluster membership summary: R02 matches in 10 clusters, R03 in 8, R33 in 12, R37 in 9.

## 2. Unique views (appear in no other run)

### R02
None. All eight R02 views have an EQUIVALENT counterpart in at least one other run. (R02 is a strict semantic subset of the union of the other three runs at this granularity.)

### R03
- **V1** — Net-growth-equation framing (growth = acquisition − churn as two levers on one quantity): no other run adopts this explicit framing criterion; R02-V1's "dominant lever" remark is embedded in the churn-arithmetic view, not a framing claim.
- **V9** — Y-first as the dominated ordering (a slip forfeits both the acquisition bet and the retention win): a distinct failure-mode consequence beyond the generic slip in cluster C6.
- **V10** — Implementation-quality constraint: X must be built as a genuine local-first foundation (not a cache-and-queue shortcut) or the sequencing option value on Y is forfeited. No other run conditions the shared-infrastructure benefit on build quality.
- **V13** — Pre-announcing the collaboration roadmap so sales can defend in-flight deals: a specific mitigation of Y-deferral cost that no other run proposes.

### R33
- **V3** — Retention feeds acquisition indirectly via reviews and word-of-mouth: a distinct causal channel linking the two goals.
- **V10** — Risk-adjusted delivered value: a completed X beats a 70%-finished Y that ships nothing usable in the quarter; distinct from the slip-to-two-quarters consequence in C6.
- **V11** — A shaky first collaboration release would damage the competitive narrative sales relies on: a stakeholder-impact consequence unique to this run.
- **V13** — Defending known existing revenue is cheaper per unit effort than winning back prospects who already lean elsewhere (parity vs switching-reason asymmetry): no counterpart elsewhere.
- **V14** — Functional division of labor: sales/marketing can work the top of funnel in parallel while engineering fixes retention, so choosing X does not abandon growth. (Related in spirit to R03-V13 but a different mechanism — see borderline cases.)

### R37
- **V5** — Silent-churner mechanism: collaboration-driven churners drift away without citing it, so the 70% of non-offline-citing churners may be the informative population; no other run questions the survey's coverage this way.
- **V6** — Despite its noise, the prospect-loss signal is the only forward-looking evidence of where new demand is going, and it agrees with the slowdown: no other run assigns this positive evidentiary role to the sales data (the others only discount it — see borderline cases).
- **V9** — Streetlight-effect critique: choosing X for its cleaner evidence optimizes for what the instrument can measure rather than what the market is doing; a meta-epistemic criterion unique to this run.
- **V10** — Decision rule under symmetric cost: with equal effort, prefer the option with direct behavioral evidence and bounded execution risk; operationalizes cluster C5 into a decision rule no other run states.

## 3. Borderline-case justifications

1. **R33-V1 in C1 but not C2.** R33-V1 contains only the annualization arithmetic; the payback-asymmetry structure (retention benefits the whole base vs acquisition benefiting future cohorts) appears in R33 split across V2 ("compounds across all current and future cohorts") and, in weaker form, V13. R33-V2 is therefore marked *partial* in C2; its primary home is C3 (quantified reduction). R02-V1 and R37-V1 each genuinely span both C1 and C2 and are listed in both.

2. **R37-V3 spans C3 and C4.** Its first half (mention rate overstates causal contribution; multiple reasons; would-leave-anyways) is EQUIVALENT to R33-V7's stated-preference caveat; its second half (bounded churn estimate ~3–3.3%) is EQUIVALENT to the C3 arithmetic. R02-V5 and R03-V3 implicitly discount ("even half") but never state the overstatement *mechanism*, so they belong to C3 only; C4 is a genuine two-run cluster (R33, R37).

3. **R03-V2 + V4 jointly equal C5.** R03 splits what R02-V2, R33-V6, and R37-V2 each state as one view: V2 carries the strength-of-X's-evidence half, V4 the bias-mechanism-of-Y's-evidence half. Judged jointly EQUIVALENT; neither half alone introduces a materially different criterion or mechanism.

4. **R33-V12 spans C7 and C8.** It states both the shared-infrastructure mechanism and the explicit reframe to sequencing; R03 splits these into V7 and V8. R02 is listed as *partial* in C8: V4 supplies the down-payment mechanism and V7 sequences Y as "the natural next bet," but no R02 view makes the explicit not-either/or reframing claim, so full C8 membership is limited to R03 and R33.

5. **C9 (R02-V6 vs R33-V15): EQUIVALENT despite an added mechanism.** Both assert the same core normative/causal claim — the slowdown is unattributed and cannot be assumed feature-driven. R33-V15 adds a confound (high churn itself suppresses net growth and reputation). The added mechanism strengthens rather than alters the shared structure, so EQUIVALENT; the confound is noted but did not warrant a separate cluster since it is a supporting argument inside one view.

6. **C12 (R03-V11 vs R37-V12): EQUIVALENT, narrowly.** Both prescribe measuring post-launch churn movement as a test of the survey signal. R37-V12 goes further by pre-committing to an inference (a null result strengthens the collaboration frame), and R03-V11 includes pre-launch tagging mechanics. The shared structure — post-launch churn movement adjudicates the survey's causal validity — is the substance of both; the differences are elaborations of the same test. Classified EQUIVALENT.

7. **C13 (R33-V5 vs R37-V8): EQUIVALENT on the retention channel; R33's viral-loop half is unmatched.** R37-V8's full content (multi-user accounts churn less; a retention channel invisible to surveys) is contained in R33-V5. R33-V5 additionally asserts a viral acquisition loop (each collaborating team recruits new users), which appears nowhere in R37 (R37-V7 invokes network effects only as consolidation *risk*, not as an acquisition mechanism for the PM's own product). The cluster is scored on the shared retention structure; the viral-acquisition-loop component is effectively unique to R33 but not listed separately in §2 because it is packaged inside a matched view.

8. **C14 (R33-V4 vs R37-V4 + V7): EQUIVALENT as a join.** R33-V4 packs two structures that R37 separates: (a) the slowdown as a leading indicator of a category shift toward collaborative tools (R37-V4), and (b) the irreversibility asymmetry — a lost network-effect position cannot be repurchased, while the other risk is manageable/recoverable later (R37-V7). One wording nuance: R33-V4 contrasts positional risk with *churn* being manageable later; R37-V7 contrasts it with *execution* risk being manageable. Both instantiate the same recoverable-vs-irrecoverable risk asymmetry favoring attention to Y, so the join is judged EQUIVALENT rather than merely related.

9. **C11 internal variants: EQUIVALENT with two sub-formulations.** All four runs state a specific evidentiary flip condition to Y grounded in independent, quantified win/loss data. R03-V14 and R33-V16 formulate the threshold as a revenue comparison (lost-prospect/collab-loss revenue exceeding recoverable churn revenue); R02-V8 and R37-V13 formulate it as causal attribution of the slowdown (feature-/category-driven, not market/channel/funnel noise). These are the same decision structure — "flip when independent evidence shows Y's foregone value dominates X's" — with different operationalizations of "dominates," which is a measurement detail rather than a different criterion. A stricter grader could split C11 into two two-run clusters along that line; the shared flip-to-Y structure justified one cluster.

10. **R03-V9 vs cluster C6: RELATED BUT MATERIALLY DISTINCT (hence unique).** C6's consequence is "Y likely slips beyond a quarter, delaying the next bet." R03-V9 adds a different structure: under a Y-first ordering, a slip forfeits *both* features' value while churn continues — an ordering-dominance argument, not just a duration prediction. Kept unique.

11. **R33-V10 vs cluster C6: RELATED BUT MATERIALLY DISTINCT (hence unique).** The consequence differs in kind: C6 predicts delay of the subsequent bet; R33-V10 predicts *nothing usable ships within the quarter* and compares risk-adjusted delivered value. Different consequence structure; kept unique.

12. **R33-V14 vs R03-V13: RELATED BUT MATERIALLY DISTINCT (both unique).** Both mitigate the cost of deferring Y through non-engineering action, but by different mechanisms and affected interests: R33-V14 is a jurisdictional division of labor (marketing/sales independently address the funnel), while R03-V13 is a communication strategy (arm sales with a credible roadmap to hold in-flight deals). Neither entails the other; both listed as unique.

13. **R37-V6 vs cluster C5: DISTINCT despite topical overlap.** Both concern the sales-derived signal, but C5 discounts it as structurally weak, whereas R37-V6 assigns it a positive, non-substitutable evidentiary role (the only forward-looking demand signal, corroborated by the slowdown). Opposite valence and a different criterion (forward- vs backward-looking coverage), so no match — unique to R37.

14. **R37-V10 vs cluster C5: RELATED BUT MATERIALLY DISTINCT (hence unique).** It presupposes C5's asymmetry but adds a new element: a decision *rule* conditioned on symmetric cost (equal quarters → prefer direct behavioral evidence and bounded execution risk; the alternative frame is worth preparing for, not betting on). The rule, not the asymmetry, is the view's substance; no other run states it.

15. **R03-V12's decomposition sub-component.** Within the matched C10 view, R03 uniquely proposes decomposing "collaboration" into cheaper deliverables (commenting, sharing, async edits) shippable sooner on the new foundation. As with borderline 7, this unmatched component rides inside a matched view and is noted here rather than listed in §2.

## Summary counts

| Run | Total views | Views with a cross-run EQUIVALENT match | Unique views |
|-----|-------------|------------------------------------------|--------------|
| R02 | 8 | 8 | 0 |
| R03 | 14 | 10 (V2, V3, V4, V5, V6, V7, V8, V11, V12, V14) | 4 (V1, V9, V10, V13) |
| R33 | 16 | 11 (V1, V2, V4, V5, V6, V7, V8, V9, V12, V15, V16) | 5 (V3, V10, V11, V13, V14) |
| R37 | 13 | 9 (V1, V2, V3, V4, V7, V8, V11, V12, V13) | 4 (V5, V6, V9, V10) |

Structural observation (condition-blind): R02, R03, and R33 share a common retention-favoring argument core (C1–C3, C5–C7, C10, C11). R37 shares that core's evidence and hedging clusters but is the only run alongside R33 to develop the category-shift/positional-risk counter-frame (C13, C14), and it uniquely contributes the survey-coverage critiques (V5, V9) that attack the shared core's evidentiary basis.
