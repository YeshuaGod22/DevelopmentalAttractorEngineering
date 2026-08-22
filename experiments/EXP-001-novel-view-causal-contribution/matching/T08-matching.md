# T08 — Blind Semantic Matching (R05, R30, R35)

Task T08: gym owner lease decision — renew at +20% rent for five years vs. move to a cheaper space 15 minutes away with ~25% surveyed member non-follow; thin margins, rent 30% of costs, flat membership, competitor opened a mile away.

Runs compared: R05 (8 views), R30 (12 views), R35 (10 views). Matching is by causal/normative/strategic structure, not wording. Note that the three extractions segment differently (R05 packs multiple mechanisms into single views, notably V1 and V4; R30 splits the same terrain most finely), so several matches are view-to-view-cluster rather than one-to-one.

## 1. Crosswalk of matched view clusters

| # | Cluster (shared structure) | R05 | R30 | R35 | Classification |
|---|---------------------------|-----|-----|-----|----------------|
| C1 | Rent-share arithmetic: rent is 30% of costs, so +20% rent = ~+6% total costs and −15% rent = ~−4.5% total costs | V1 (first half) | V1 | V1 | EQUIVALENT across all three (identical causal conversion and figures) |
| C2 | Revenue-shock vs. cost-shock asymmetry: on thin margins the move's ~25% revenue loss dwarfs its ~4.5% cost saving; renewal squeezes margin, moving produces outright loss (each run with a worked margin illustration) | V1 (second half) | V2 + V3 | V2 | EQUIVALENT across all three (same comparison-in-common-units structure and same conclusion; illustrative margins differ — 10% in R05, 5% in R30, ~10% in R35 — which is parameterization, not structure) |
| C3 | Stated-preference survey understates real attrition; the added 15-minute drive is a known friction/churn driver for gym attendance | V3 | V6 | V3 | EQUIVALENT across all three. R05-V3 additionally contains a follow-then-churn-later mechanism absent from R30/R35 (see borderline B1) |
| C4 | Vacating the current site hands displaced members directly to the nearby competitor (they don't leave the market; moving therefore worsens the competitive position) | V4 (core) | V7 | V4 | EQUIVALENT across all three on the member-transfer mechanism. R05-V4 bundles extra sub-mechanisms not found elsewhere (see borderline B2) |
| C5 | Negotiation strategy: a credible alternative space gives leverage; counter the +20% and seek a shorter term / rent ramp / concessions rather than accepting or moving | V5 | V10 (with V9 adjacent — see below) | V9 | EQUIVALENT across all three. R30-V9 (five-year lock-in identified as renewal's principal risk, to be cured by renegotiation not relocation) is RELATED BUT MATERIALLY DISTINCT from the cluster core: it is the risk-identification step, which R05 folds into V4/V5 as fragments and R35 folds into V5; only R30 states it as a standalone constraint view (see borderline B3) |
| C6 | Decision criterion of asymmetric reversibility: a wrong renewal is a recoverable/correctable wound, a wrong move is a fast, likely fatal, irreversible error — prefer the recoverable branch | V7 | — | V7 | EQUIVALENT (R05, R35). Absent from R30, whose closest analogue (V8, shock-absorption capacity) is a different mechanism |
| C7 | Flip/revision condition keyed to competitor-bound attrition: if member loss to the competitor is accelerating, renewal locks in a premium on a weakening base and moving becomes defensible — check before deciding | V8 | V12 | (V10 related — see below) | EQUIVALENT (R05, R30): same trigger, same directional flip, same pre-decision timing. R35-V10 is RELATED BUT MATERIALLY DISTINCT: same causal trigger (cancellations flowing to the competitor) but deployed as post-renewal instrumentation with a pre-committed future move, not a pre-signing check (borderline B4) |
| C8 | Flat-membership constellation (topic cluster with NO equivalent pair): flat membership as decision-relevant fact | V6 | V8 | V5 | ALL PAIRS RELATED BUT MATERIALLY DISTINCT. R05-V6: reframing — the real problem is growth, moving is an unproven acquisition bet, renew and fix retention/per-member revenue. R30-V8: constraint — no growth engine to absorb shocks, so take the smaller wound. R35-V5: declining-asset inference — flat membership + competitor entry + landlord's rent demand signal an eroding incumbent position, which argues *toward* moving. Same fact, three different mechanisms, and R35-V5 points in the opposite direction (borderline B5) |
| C9 | Post-renewal revenue tactics | V6 (tail) | V11 | — | RELATED BUT MATERIALLY DISTINCT. Overlap: ancillary/per-member revenue (personal training, classes vs. dues increase, ancillary revenue). But R05-V6 offers it as strategic reframing of what the decision optimizes, while R30-V11 offers it as a tactical plan to close a quantified ~1% post-renewal margin gap (borderline B6) |
| C10 | Missing-information framing | (V8 partial) | (V12 partial) | V8 | RELATED BUT MATERIALLY DISTINCT. R35-V8 names three decisive unknowns (why membership is flat, whether the competitor has actually drawn members, whether the new location has real demand). The middle unknown coincides with the C7 trigger, but R35-V8 is an information-constraint view spanning additional unknowns (new-site demand quality) that neither R05 nor R30 raises (borderline B7) |

## 2. Views unique to a single run

### R05
- **R05-V2** (one-time relocation costs — build-out, equipment, downtime, re-signage, marketing — on top of recurring revenue loss): no other run mentions move transaction costs at all. Unique material constraint.

### R30
- **R30-V4** (gyms are fixed-cost businesses, so lost member revenue falls almost entirely to the bottom line): an operating-leverage mechanism that sharpens C2 but appears explicitly nowhere in R05 or R35. Unique causal mechanism.
- **R30-V5** (break-even sensitivity: the move only pays if real churn is ~5%, i.e., the survey must be wrong by a factor of five): a threshold/sensitivity computation absent from the other runs; it is adjacent to C3 but is a different analytic move (see borderline B8). Unique predicted consequence.

### R35
- **R35-V6** (moving as repositioning: the 25% churn is a one-time known loss vs. an ongoing unbounded bleed, and the cheaper five-year lease locks in a lower cost base with new-territory growth): the only developed pro-move strategic case in any run. R05-V4 gestures at "the case for moving" only to dismiss it; no run states this mechanism as a view except R35. Unique strategy (see borderline B9).

Views not listed here but also not in any EQUIVALENT cluster (R30-V9, R35-V5, R35-V8, R35-V10, R30-V11, and the R05-V6/R30-V8 pair) have cross-run relatives and are classified RELATED BUT MATERIALLY DISTINCT in the crosswalk rather than unique.

## 3. Borderline-case justifications

- **B1 (C3, R05-V3's extra tail).** All three runs share the two load-bearing mechanisms (stated-vs-revealed preference gap; drive-time friction), so the cluster is EQUIVALENT. R05 alone adds a third mechanism — members who initially follow may churn later as the longer drive erodes the habit — which extends the predicted consequence in time. I did not split this into a separate unique view because the extraction itself presents it as part of one view, but a finer segmentation would count it as an R05-only sub-view.

- **B2 (C4, R05-V4's bundling).** The core mechanism (vacating donates members to the competitor) is clearly equivalent in all three runs. R05-V4 additionally contains: a weakness-signaling effect, doubt about demand in the cheaper area, and no protection from future competitor entry there. None of these sub-mechanisms appears in R30 or R35. The cluster is scored on the shared core; the surplus content is noted but is not enough to demote the match below EQUIVALENT, since the causal spine (member transfer to rival) is identical.

- **B3 (C5, R30-V9).** R30 separates "the five-year lock-in is renewal's main risk" (V9) from "negotiate using the credible alternative" (V10). R05 and R35 carry the same lock-in concern only as embedded fragments (R05-V4's "five-year lock-in of exposure," R05-V5's 3-year-term ask, R35-V5's "five-year war of attrition," R35-V9's shorter-term ask). Because the substance exists across runs but never as an equivalent standalone view, R30-V9 is classified RELATED BUT MATERIALLY DISTINCT rather than either EQUIVALENT or unique. This is a segmentation artifact more than a substantive novelty.

- **B4 (C7 vs. R35-V10).** R05-V8 and R30-V12 are a clean equivalent pair: same trigger metric (attrition trend since the competitor opened), same flip (a move/cheaper reset becomes the right call), same timing (before signing). R35-V10 shares the trigger but changes the strategy's temporal structure: renew first, instrument cancellation destinations for 12 months, and pre-commit to a proactive move if the data confirms the declining-asset frame. A different strategy (monitoring-and-option-preservation vs. pre-decision verification) built on the same causal trigger is the textbook case for RELATED BUT MATERIALLY DISTINCT.

- **B5 (C8, the flat-membership constellation).** This is the strongest case against lexical matching: all three views cite the identical fact (two years of flat membership) and two of the three even support the same recommendation, yet no pair is equivalent. R05-V6 turns the fact into a problem-reframing ("the decision doesn't solve the real problem — growth"), R30-V8 into an absorption-capacity constraint ("no growth engine to buffer a 25% revenue shock"), and R35-V5 into evidence for a declining-asset diagnosis that argues for moving. Different mechanisms, different criteria, and in R35's case a reversed directional force.

- **B6 (C9, R05-V6 tail vs. R30-V11).** Both mention ancillary/per-member revenue, but the surrounding structure differs: R05 uses it to redefine the objective (fix growth, not rent), R30 uses it to close a specific quantified gap created by accepting the renewal. Overlapping tactic, different strategic role → RELATED BUT MATERIALLY DISTINCT.

- **B7 (C10, R35-V8).** One of its three unknowns (has the competitor actually drawn members) is exactly the C7 trigger, which tempted an EQUIVALENT call. But R35-V8 is a constraint view ("the decisive evidence is absent"), not a flip rule, and two of its three unknowns (cause of flatness; whether the new site has demand or merely cheap rent) appear nowhere else. RELATED BUT MATERIALLY DISTINCT.

- **B8 (R30-V5 vs. C3).** R30-V5 (move breaks even only at ~5% churn) reinforces the same conclusion as C3 (survey likely understates churn) and could be mistaken for the same view. It is not: C3 is an argument about the direction of survey error; V5 is a sensitivity threshold showing how large the error would have to be *in the opposite direction* for the move to pay. Different analytic mechanism → counted unique to R30 rather than merged into C3.

- **B9 (R35-V6 uniqueness).** R05-V4's evidence line records that R05 "weighs the case for moving (contested location, five-year lock-in of exposure)," which brushes against R35-V6. But R35-V6's actual mechanism — churn as a bounded one-time loss vs. an unbounded ongoing bleed, plus locking in a lower cost base with growth optionality — is not present in R05's brief acknowledgment. Counted unique; the alternative reading (RELATED BUT MATERIALLY DISTINCT to R05-V4) would not change any cluster's equivalence membership.

## Summary counts

- EQUIVALENT clusters spanning all three runs: 5 (C1, C2, C3, C4, C5).
- EQUIVALENT clusters spanning exactly two runs: 2 (C6: R05+R35; C7: R05+R30).
- Strictly unique views: R05: 1 (V2); R30: 2 (V4, V5); R35: 1 (V6).
- Related-but-materially-distinct relations dominate the flat-membership and revision-condition terrain, where all three runs touch the same facts through different mechanisms.
