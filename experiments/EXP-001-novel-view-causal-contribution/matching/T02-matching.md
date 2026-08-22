# T02 Semantic Matching — Runs R09, R22, R29, R41

Blind semantic-matching pass over the extracted view sets for task T02 (finish custom
reporting tool vs. switch to vendor product). Matching is by causal/normative/strategic
structure, not lexical overlap. Run IDs are anonymized and carry no meaning.

View counts: R09 = 10, R22 = 11, R29 = 16, R41 = 12.

## 1. Crosswalk of matched view clusters (EQUIVALENT members)

| Cluster | Shared structure | R09 | R22 | R29 | R41 |
|---|---|---|---|---|---|
| C1 — Sunk-cost exclusion | The 70% built is sunk; only forward-looking costs/benefits count. | V1 | V1 | V1 | V1 |
| C2 — Subscription fee immaterial at labor scale | $4,800/yr is noise against engineering labor; price should not decide the choice. | V2 | V6 | V2 | V3 |
| C3 — Opportunity cost: freed capacity to deal-costing backlog | Switching frees ~4 weeks x 5 people (~20 person-weeks) for customer-facing features tied to lost deals. | V3 | V5 | V5 | V4 |
| C4 — Knowledge-transfer window arithmetic | Finishing consumes 6 of the expert's 8 remaining weeks, leaving ~2 weeks of handoff on the hardest component — insufficient and slack-free. | V5 | V2 | V3 | — |
| C5 — "Costs nothing ongoing" is illusory / orphaned-component maintenance liability | Finishing means permanently owning a tricky component with no remaining expert; real ongoing cost exceeds the vendor fee. | V4, V7 | V4 | V4 | V2 |
| C6 — Schedule-slip optimism of "70% done, 6 weeks left" | Completion estimates at this stage systematically overrun; a slip strands an unfinished/unsupportable tool after the expert leaves — the worst outcome. | — | V3 | V7 | — |
| C7a — The gap's contents are the pivotal variable | Whether the vendor's missing 10% contains a hard must-have (compliance, un-ingestible data, critical export) is what could change the answer. | V8 | V7 | V8 | V7 |
| C7b — Cheap pre-commitment gap audit | Spend ~2–3 days enumerating the missing 10% against actual must-haves before committing. | V8 | V7 | V12 | V8 |
| C8 — Vendor-plus-small-custom-shim hybrid | Even if the gap holds a real requirement, prefer vendor for the commodity 90% plus a small custom piece for the gap over finishing the whole tool. | V9 | V8 | — | V10 |
| C9 — Conditional flip rule with handoff contingency | Stated reversal condition: finish the custom tool only if the audit finds a must-have the vendor/shim cannot cover (especially overlapping the tricky component), with knowledge transfer prioritized. | V10 | — | V16 | V9 |
| C10 — Redeploy the departing expert's remaining time under the switch | Use the expert's final weeks for vendor integration and documentation while they are still present. | V6 | V10 | V15 | — |
| C11 — Vendor-dependency risks requiring diligence | Post-adoption risks: vendor failure/discontinuation, price increases after lock-in, data/security concerns. | — | V9 | V9 | — |

Notes on bundling: R09-V8 and R22-V7 each bundle the pivotal-gap claim (C7a) and the
audit prescription (C7b) in a single view; R29 and R41 split them into separate views.
This is a granularity difference in extraction, not a substantive difference.

## 2. Views appearing in no other run (unique views)

### R09
- None. Every R09 view has an EQUIVALENT counterpart in at least one other run (V4 and
  V7 are near-duplicates within R09, both landing in C5).

### R22
- **V11** — Reframes the abandoned 70% as having purchased a precise requirements
  specification, which is what enables confident evaluation of the vendor's 90% claim.
  No other run extracts value from the write-off itself.

### R29
- **V6** — General build-vs-buy principle: non-differentiator internal tools should be
  bought; no other run appeals to this category-level norm.
- **V10** — Morale/stakeholder impact of shelving nearly finished work (including the
  departing expert's send-off), with the counterweight that shipping revenue features
  also boosts morale. The only stakeholder-morale view in any run.
- **V11** — Uncertainty asymmetry: the custom tool is a known quantity while the
  vendor's real-world fit is untested until integration begins. Distinct from C11's
  vendor-viability risks (different mechanism: epistemic fit-uncertainty vs. business risk).
- **V13** — Optionality strategy: adopt vendor now, shelve (not delete) the 70% build,
  revisit in 3–6 months, and build only the missing slice if the gap proves painful.
  Related to C8 but materially distinct (see borderline cases).
- **V14** — Anti-pattern warning: "finish it a little on the side" is worse than either
  clean option because it recreates the key-person problem with less focus. No analogue elsewhere.

### R41
- **V5** — The missing 10% is likely *concentrated* in the essential, unusual
  requirement that motivated the custom build (and likely coincides with the trickiest
  component). A probabilistic claim with a mechanism; stronger than C7a's "may contain"
  (see borderline cases).
- **V6** — Inversion: if the gap is essential, the expert's departure is a *closing
  window* arguing for finishing immediately — the vendor option is permanent, the
  expert's knowledge is expiring. No other run reads the departure fact in this direction.
- **V11** — Path-independent knowledge capture: document the tricky component before
  departure *whichever* option is chosen, as a hedge on the switch bet. Related to C10
  but materially distinct (see borderline cases).
- **V12** — Under the essential-gap frame, the backlog pressure argues for finishing
  fast now rather than switching (avoiding an unbounded later reimplementation). Same
  fact as C3, opposite strategic conclusion (see borderline cases).

## 3. Borderline-case justifications

1. **R29-V2 in C2 (EQUIVALENT, borderline).** R09-V2/R22-V6/R41-V3 use the fee-to-labor
   comparison defensively ("price should not decide"), while R29-V2 extends it into an
   affirmative quantified case ($50k–80k of extra labor vs. a fee that takes a decade to
   match). The underlying cost-scale structure — the subscription is dwarfed by the labor
   delta between paths — is identical, so I classify it EQUIVALENT; the order-of-magnitude
   quantification is elaboration of the same comparison, not a new mechanism.

2. **R09-V4 and R09-V7 both in C5.** These are near-duplicates within a single run
   (orphaned-component liability; true cost = build time + permanent maintenance
   obligation). Both map to C5; counted as one cluster membership for R09, listed jointly.

3. **R22-V2 straddles C4 and C6.** Its core is the window arithmetic (C4), but it also
   carries the slip-strands-an-unfinished-tool worst case, which is the consequence half
   of C6 (R29-V7). Placed in C4 by its primary mechanism; its slip component corroborates
   R22-V3's membership in C6 rather than constituting a separate view.

4. **R41-V5 vs. C7a (RELATED BUT MATERIALLY DISTINCT → unique).** C7a members say the
   gap *may* contain a must-have and treat this as an open empirical question. R41-V5
   makes a stronger, differently-structured claim: coverage is non-fungible, vendors
   converge on the common 90%, and custom tools exist *because of* the unusual
   requirement — so the gap is *disproportionately likely* to be essential. That added
   probabilistic mechanism (selection effect on why the tool was built) is a distinct
   causal contribution, not a rewording of C7a.

5. **R41-V7 in C7a (EQUIVALENT, borderline).** Its hinge claim — the deciding variable
   is whether the gap holds a must-have overlapping the tricky component — matches
   R09-V8/R22-V7/R29-V8. It additionally carries a meta-observation (the departure fact
   reads oppositely under two frames), but that meta-claim is the connective tissue to
   R41's unique V6, not a separate decision structure; the pivotal-variable core is equivalent.

6. **R29-V13 vs. C8 (RELATED BUT MATERIALLY DISTINCT → unique).** C8 (R09-V9, R22-V8,
   R41-V10) prescribes a vendor-plus-shim architecture as the answer when the gap holds a
   real requirement. R29-V13 shares "build only the missing slice, never the whole tool,"
   but introduces a different mechanism: temporal deferral with preserved optionality
   (shelve the code, revisit in 3–6 months, act only if pain materializes). Deciding now
   with a shim vs. deferring the shim decision is a materially different strategy.

7. **R41-V10 in C8 (EQUIVALENT, borderline).** It appears inside R41's finish-branch and
   specifies the custom piece be built/documented while the expert is present, whereas
   R09-V9/R22-V8 offer the shim as the general fallback. The strategic structure —
   vendor for the commodity 90%, small custom component for the essential 10%, instead of
   completing the full build — is the same; branch placement and timing detail do not
   change the mechanism.

8. **R22 and C9.** R22 has no EQUIVALENT member in C9: where R09-V10/R29-V16/R41-V9
   state a condition under which the answer flips to finishing, R22-V8 explicitly holds
   that even a hard requirement does *not* flip the answer (vendor+shim still wins).
   R22-V8 therefore belongs to C8, and its absence from C9 is a substantive difference,
   not an extraction gap.

9. **R22-V10 in C10 (EQUIVALENT, borderline).** R22-V10 is narrower (sequence the
   integration inside the expert's tenure so they can map concepts) than R09-V6/R29-V15
   (full redeployment of the expert's time to integration, documentation, salvage). The
   operative mechanism — deliberately spending the expert's remaining tenure on the
   switch path's transition work — is shared, so EQUIVALENT; R09-V6's additional claim
   that the departure becomes immaterial under the switch is treated as elaboration.

10. **R41-V11 vs. C10 (RELATED BUT MATERIALLY DISTINCT → unique).** C10 redeploys the
    expert conditional on switching. R41-V11 prescribes knowledge capture *regardless of
    path*, motivated as a hedge because the switch itself is a bet that the gap stays
    unimportant. The path-independence and hedge rationale are a different strategic
    structure from switch-conditional redeployment.

11. **R41-V12 vs. C3 (RELATED BUT MATERIALLY DISTINCT → unique).** Both start from the
    deal-costing backlog, but C3 uses it to argue for switching (freed capacity), while
    R41-V12 argues that under the essential-gap frame the same pressure favors finishing
    quickly now over an open-ended later reimplementation. Same affected interest,
    opposite consequence structure — distinct by the stated criteria.

12. **R29-V12 straddles C7b and C8.** Its audit prescription is EQUIVALENT to C7b; its
    lightweight-workarounds claim (export script/spreadsheet step closes most of the gap
    cheaply) is adjacent to C8's shim logic but stops short of the architectural hybrid.
    Counted in C7b only; the workaround component is corroborating detail, and R29's
    architectural analogue is V13 (held distinct per item 6).

13. **R22-V5 in C3 (EQUIVALENT).** R22 adds a skeptical discount on the sales team's
    self-interested claim before weighing the freed capacity. The discount is an
    evidential adjustment inside the same opportunity-cost mechanism, not a new
    mechanism; classified EQUIVALENT without reservation beyond this note.

## Summary observations (structural, no condition inference)

- A stable consensus core spans all four runs: C1, C2, C3, C5, C7a, C7b (six clusters
  with EQUIVALENT members in all four runs).
- R09 contributes no unique views; its content is fully absorbed by the shared clusters.
- R29 is the most granular extraction (16 views) and contributes the most unique
  peripheral views (5), mostly additional criteria and risks on the same side of the
  decision as the consensus.
- R41 is structurally the outlier in kind rather than count: its unique views (V5, V6,
  V12) form a coherent alternative frame (gap concentration → departure as closing
  window → backlog favors finishing) that inverts the reading of two facts the other
  runs treat unidirectionally, plus a path-independent hedge (V11). R41 is also the only
  run missing the window-arithmetic cluster (C4).
- R22 uniquely declines the flip condition (C9), holding vendor+shim dominant in all
  scenarios.
