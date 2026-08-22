# T01 — Blind Semantic Matching Crosswalk

Grader: blind semantic-matching pass over anonymized extractions R13, R15, R20, R27 for task T01 (support-team evening coverage: shift three agents vs. hire two part-time contractors). Matching criterion is substantive structure (mechanism, criterion, affected interest, constraint, strategy, consequence), not lexical overlap. No condition inference.

Note on granularity: the four extractions segment at different grain. Where one run's single view spans two clusters (e.g., R20-V2) or a cluster corresponds to only part of a composite view (e.g., R27-V5), the membership is marked "(partial)". A view counts as matched only where an EQUIVALENT member exists in another run; views whose best cross-run match is RELATED BUT MATERIALLY DISTINCT appear in the unique lists with a near-match note.

## 1. Crosswalk table — matched view clusters (EQUIVALENT members)

| Cluster | Shared substantive content | R13 | R15 | R20 | R27 |
|---|---|---|---|---|---|
| C1 | The 8pm–11pm window has zero scheduled coverage, so the demand–supply mismatch is worse than the "triple response times" figure suggests; part of the 40% evening demand window is fully unstaffed. | V1 | V1 | V1 | V1 |
| C2 | Enterprise complaints convert the coverage gap from an internal/operational metric into an active revenue (churn) risk. | — | V2 | — | V2 |
| C3 | Delay cost dominates: the churn cost of leaving escalated enterprise clients with tripled response times exceeds the payroll cost difference between the options, making the slow-to-take-effect path the costliest despite the smallest budget line. | V4 | — | V2 (partial) | — |
| C4 | The contractor option's 6-week onboarding leaves the coverage problem at full severity precisely while enterprise escalation is live. | — | V3 | V2 (partial) | V7 |
| C5 | Stated compliance is unreliable: forcing reluctant agents onto evening shifts creates a real attrition/morale risk ("would comply" ≠ will stay). | V5 | V7 | V5 (partial) | V5 (partial) |
| C6 | Losing one experienced agent would cost more than the contractor budget (and would worsen the coverage problem it was meant to fix). | — | V8 | V5 (partial) | — |
| C7 | Mitigation package for the shift move: solicit volunteers across all 12 agents first, attach a shift differential/perk, and time-box the arrangement with an explicit review or end date. | V6 | V13 (partial) | V6 | V5 (partial) |
| C8 | New part-time contractors are the weakest match for complex enterprise-tier tickets — exactly the ticket class that generated the complaints — even after onboarding. | V7 | V4 | — | V8 |
| C9 | Shifting three agents thins daytime staffing against the ~60% of volume that is still daytime, degrading daytime service; a cost of Option A that contractors (net-added capacity) avoid. | V8 | — | V4 | — |
| C10a | The either/or is a false dichotomy: the two options are not mutually exclusive over time and address different problems (emergency vs. structure). | V12 (embedded) | V13 (embedded) | V3 | V11 (embedded) |
| C10b | Sequenced do-both plan: shift agents now as an explicitly temporary bridge while hiring contractors in parallel, then unwind the forced shifts when contractors are effective (~6–8 weeks), retaining any agent who prefers evenings. | V12 | V13 | V8 | — |
| C11 | Proactively contact the two complaining enterprise clients this week with a concrete, dated plan — retention depends on perceived responsiveness/being heard as much as on the latency metric itself. | — | V14 | V9 | — |
| C12 | Single-option fallback: if only one option can be taken, choose the shift move, because uncovered enterprise demand is the nearer cliff. | — | V15 | V10 | — |
| C13 | Reversal condition: if the reluctant agents are credible flight risks (would quit rather than comply), the recommendation flips to contractors-only with interim triage measures for the enterprise accounts. | V13 | — | V11 | V12 |

## 2. Views appearing in no other run (unique views)

### R13
- **V2** — Complaints as a *lagging* indicator of accumulated frustration, so the client-perceived remediation clock is longer than the calendar clock. Related to C2/C3 but introduces a distinct perception-timing mechanism no other run has.
- **V3** — True contractor time-to-effect is 8–10 weeks because *recruiting time precedes* the stated 6-week onboarding. Extends C4 with a hiring-lead-time mechanism unique to R13.
- **V9** — 40% evening demand is structural, so a permanent evening capability is the durable answer (with contractor scheduling flexibility as a bonus). Near-match R15-V11, but the justifying mechanism differs (demand permanence vs. cost-efficiency).
- **V10** — Validate the 40% figure's severity mix before committing; a lighter intervention may suffice if evening volume is low-priority. No counterpart anywhere.
- **V11** — Diagnose whether complaints concern 6–8pm slowness or the 8–11pm dead zone, since that shapes the staffing response. No counterpart.

### R15
- **V5** — Shift reassignment is within the lead's ordinary operational authority (jurisdiction view). Only jurisdictional claim in any run.
- **V6** — Normative reframe: the binding constraint is retention of experienced agents, not schedule coverage hours. Criterion-level generalization of C5 that no other run states as a criterion.
- **V9** — Reversibility as the decision criterion, mapped as: slow response is recoverable, attrition is not → prefer the contractor path's delay. Near-match R20-V10 applies the same criterion with the *opposite* mapping (see borderline notes).
- **V10** — Bridge package for a contractor-first plan: paid volunteer 8–11pm on-call rotation, dated client outreach, morning-first enterprise triage, offered unconditionally. Near-match R20-V11 names similar measures but only as conditional substitutes.
- **V11** — Contractors are cheap permanent capacity worth buying on their own terms (half an FTE against 40% of demand). Near-match R13-V9; different mechanism (cost-efficiency vs. structural durability).
- **V12** — The problem underdetermines the frame conflict; data to weigh churn risk against attrition risk is absent, so a pure-form choice is unjustified. Only epistemic-underdetermination claim in any run.
- **V16** — Opposite-direction reversal: in-window enterprise renewal/escalation or contractor failure on enterprise tickets would *force the permanent shift* despite retention cost. Mirror image of C13, not a member of it.

### R20
- **V7** — Proportional sizing (40% volume → ~4–5 evening heads) concluding *neither option alone is sufficient*, so both are needed. Near-match R27-V3 runs the same calculation to a materially different adequacy verdict.

### R27
- **V3** — Same proportional sizing, concluding the three-agent shift *by itself* approximately matches the demand-shaped target while contractors alone under-staff the evening. Near-match R20-V7 (see borderline notes).
- **V4** — The shift option works immediately at zero incremental cost with no quality dip because shifted agents already know the product, tooling, and enterprise accounts. The quality-preservation half is the affirmative mirror of C8; the immediacy claim lacks C3's churn-cost comparison; no full equivalent elsewhere.
- **V6** — Daytime thinning is *absorbable* because daytime holds a disproportionate capacity share relative to its ~60% of volume. Same topic as C9 with the opposite valence — a different consequence claim, not an equivalent.
- **V9** — Pull the two enterprise contracts to check response-time SLAs and near-term renewal dates before finalizing, since penalties or a lost renewal dwarf the cost delta. Only run that makes contract diligence an action item.
- **V10** — Contract-exposure criterion: the contractor path is tolerable only if there is no SLA exposure and renewals are ≥ ~6 months out, and even then it trades a preference problem for an unproven-quality problem. No counterpart.
- **V11** — Sequencing with contractors held *in reserve*: shift now, hire contractors only if shifted-agent dissatisfaction persists at the review date. Shares C10a's framing but is materially distinct from C10b's parallel-hire plan.

## 3. Borderline-case justifications

1. **C1 membership of R27-V1** (EQUIVALENT). R27-V1 adds a capacity-share quantification (2/12 ≈ 17% of capacity vs. 40% of demand) the others lack, and R13-V1 alone appends an option implication (only the 3–11pm shift reaches 11pm). But the load-bearing constraint in all four is identical: coverage ends at 8pm while demand runs to 11pm, so a portion of the demand window is fully unstaffed and the stated "3x" understates the problem. The extra arithmetic is elaboration of the same constraint, not a new mechanism, so all four are kept equivalent. (R27's separate sizing arithmetic is its V3, handled below.)

2. **R13-V2 vs. C2/C3** (RELATED BUT MATERIALLY DISTINCT). R13-V2 shares the "complaints signal churn risk" territory but its distinctive content is a perception mechanism — frustration accumulated before the complaint, so a 6-week fix reads to clients as 2–3 months. Neither R15-V2/R27-V2 (risk classification) nor R13-V4/R20-V2 (cost-of-delay dominance) contains that client-clock mechanism, so it is excluded from both clusters. (R20-V2 calls complaints a *leading* indicator of churn where R13-V2 calls them a *lagging* indicator of frustration — compatible claims about different referents, but structurally different views.)

3. **R20-V2 split across C3 and C4** (EQUIVALENT in both, partial). R20's extraction fused two claims the other runs separated: (a) the delay itself is the dominant cost, exceeding the payroll delta (matching R13-V4), and (b) the contractor path specifically leaves escalated clients exposed through the onboarding window (matching R15-V3/R27-V7). Rather than force a single assignment, it is listed as a partial member of both clusters; this reflects extraction granularity, not double-counting of distinct content.

4. **R13-V3 vs. C4** (RELATED BUT MATERIALLY DISTINCT). C4 members treat the exposure window as the stated 6 weeks. R13-V3's substantive addition is a different constraint: recruiting time precedes onboarding, stretching true time-to-effect to 8–10 weeks. Because it changes the magnitude and introduces a mechanism (hiring lead time) absent elsewhere, it is unique rather than a C4 member.

5. **R27-V5 as partial member of C5 and C7** (EQUIVALENT, partial). R27-V5 is a composite: it concedes the attrition/morale liability (C5) and immediately supplies the volunteers-first/differential/review-date mitigation (C7). Both halves match cluster content closely; its "manageable" framing softens the risk relative to R13-V5/R15-V7 but does not change the affected interest or the mitigation structure, so partial equivalence in both clusters is warranted.

6. **R20-V5 spanning C5 and C6** (EQUIVALENT in both, partial). R20-V5 contains both the attrition-risk mechanism and the losing-one-agent-costs-more-than-the-contractor-budget consequence, which R15 split into V7 and V8. Same granularity issue as item 3.

7. **R15-V7's cascade claim** (kept EQUIVALENT within C5). R15-V7 adds that resignations cluster ("one departure licensing the next"), a dynamic no other run states. This was judged an intensifier of the same causal claim (forced shifts → attrition) rather than a separate mechanism; the affected interest, trigger, and consequence class are identical, so it stays in C5 rather than becoming unique.

8. **R20-V7 vs. R27-V3** (RELATED BUT MATERIALLY DISTINCT). Both run the identical proportionality calculation (40% of volume → ~4–5 evening agent-equivalents) — a genuine shared mechanism. But the extracted views terminate in incompatible adequacy verdicts: R20-V7 concludes neither option alone suffices (grounding a mandatory do-both), while R27-V3 concludes the three-agent shift alone approximately meets the target (grounding shift-first with contractors optional). Because the consequence/criterion each view exists to support differs materially, they are not classified equivalent despite the shared arithmetic. This is the clearest case where lexical/structural overlap coexists with substantive divergence.

9. **R15-V9 vs. R20-V10** (RELATED BUT MATERIALLY DISTINCT). Both invoke reversibility as the deciding criterion — and reach opposite assignments. R15-V9: attrition is the irreversible harm, slow response is bridgeable, so the shift move carries the worse downside. R20-V10: the shift move is the reversible act, while six more weeks of tripled response times "may not be" recoverable. Identical normative criterion, inverted factual mapping, opposite directional force; equivalence would erase exactly the difference that matters. Meanwhile R15-V15 and R20-V10 *are* clustered (C12) because their shared content — under a forced single choice, take the shift because enterprise exposure is the nearer cliff — is the same conditional conclusion; R20-V10's reversibility rationale is noted but the fallback verdict and urgency grounds match.

10. **C10b membership and R27-V11** (R27 excluded, RELATED BUT MATERIALLY DISTINCT). R13-V12, R15-V13, and R20-V8 all commit to hiring contractors *now*, in parallel with a time-boxed shift bridge, with an explicit handoff when contractors ramp. R27-V11 shares the false-dichotomy framing (hence C10a membership) and the shift-now element, but holds contractors *in reserve*, contingent on persistent dissatisfaction at the review date. Whether the second intervention is purchased immediately or conditionally is a material strategic difference (cost committed, timeline to permanent coverage, dependence on the review outcome), so R27-V11 is not a C10b member.

11. **R15-V10 vs. R20-V11's interim measures** (RELATED BUT MATERIALLY DISTINCT). The named measures overlap heavily (paid evening on-call rotation, enterprise-ticket triage/prioritization, client outreach). But in R15-V10 they are the unconditional bridge attached to a contractor-first permanent plan, while in R20-V11 they appear only as substitutes triggered by the flight-risk reversal condition. Same toolbox, different strategic role and trigger; not equivalent. (R20-V11 itself remains a C13 member on its reversal-condition content.)

12. **C13 membership of R27-V12** (EQUIVALENT, with reservation). R13-V13 flips on flight risk (with a no-volunteers qualifier, or independently on client tolerance of the timeline); R20-V11 flips on likely resignations; R27-V12 requires a *conjunction* — flight risk AND no SLA/renewal exposure within ~2 quarters. The conjunction makes R27's condition strictly narrower. It is retained as equivalent because the core causal structure is shared (credible attrition risk makes the bridge costlier than the problem, flipping the choice to contractors), and the contract-exposure conjunct is R27's own V9/V10 material composed in; but this is the weakest equivalence call in the crosswalk. R15-V16 is *not* a C13 member: its conditions run the opposite direction (forcing the shift despite retention cost), which is a different consequence structure entirely.

13. **R13-V9 vs. R15-V11** (RELATED BUT MATERIALLY DISTINCT). Both conclude contractors merit a permanent place. R13-V9's mechanism is demand permanence (a structural 40% evening share makes evening capability a lasting need) plus scheduling flexibility; R15-V11's is unit-cost efficiency (half an FTE against 40% of volume is cheap capacity "even if the shift question did not exist"). Shared conclusion, disjoint justifying mechanisms — a paradigm case for related-but-distinct under a mechanism-sensitive standard.

14. **R27-V4 vs. C8** (RELATED BUT MATERIALLY DISTINCT). C8 is a negative claim about contractors on enterprise tickets; R27-V4 is the affirmative complement about shifted agents (quality preserved because they know the product and the accounts), bundled with immediacy and zero incremental cost. Because R27 extracted the contractor-weakness claim separately (V8, a C8 member), V4's residual content — no-quality-dip immediacy at zero cost — has no equivalent elsewhere and is listed unique.

15. **R15-V12 vs. R27-V9** (RELATED BUT MATERIALLY DISTINCT). Both notice that contract/renewal information is missing and decision-relevant. R15-V12 is an epistemic claim: the absence of that data (plus tenure, labor market) means neither pure option can be justified. R27-V9 is an action directive: go retrieve the contracts and check SLA clauses and renewal dates, with a stated consequence weighting. A meta-level underdetermination claim and a concrete diligence step share a topic but not a structure.

16. **R27-V6 vs. C9** (RELATED BUT MATERIALLY DISTINCT). R13-V8 and R20-V4 assert daytime degradation as a real cost of the shift option; R27-V6 asserts the same thinning is absorbable because daytime is over-provisioned relative to demand share. Identical mechanism domain, opposite predicted consequence — the difference is precisely what a matching pass must preserve, so R27-V6 is unique.

## Summary counts

- EQUIVALENT clusters: 14 (C1–C9, C10a, C10b, C11, C12, C13).
- Cluster participation: R13 in 9 clusters; R15 in 11; R20 in 12; R27 in 8.
- Unique views: R13: 5 (of 13); R15: 7 (of 16); R20: 1 (of 11); R27: 6 (of 12).
- Views shared by all four runs (as equivalents): C1 only; C5 and C10a reach all four with partial/embedded members.
