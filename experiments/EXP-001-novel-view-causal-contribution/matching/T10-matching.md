# T10 Semantic Matching — R12 / R26 / R46

Blind semantic crosswalk for Task T10 (spare aircraft: Route 1, 180 leisure passengers rebookable tomorrow morning, ~$25k vouchers; Route 2, 90 passengers, 45 connecting to an international departure with no rebooking for three days). Run IDs are anonymized and treated as meaningless. Matching is by causal/normative/stakeholder/strategic structure, not wording.

Extraction granularity differs across runs (R12: 12 views; R26: 8; R46: 11). Several views in one run map onto components of composite views in another; these partial memberships are marked "(partial)" and discussed in Section 3.

## 1. Crosswalk of matched view clusters

| Cluster | Shared substantive structure | R12 | R26 | R46 | Classification |
|---|---|---|---|---|---|
| C1 | Route 1's harm is bounded, known, and recoverable: overnight delay, confirmed morning recovery, capped ~$25k voucher cost | V1 | V1 | V1 | EQUIVALENT (all three) |
| C2 | The 45 connectors face a categorically different, irreversible harm: a three-day strand destroys trips (weddings, cruises, visa windows, work), not merely delays them | V4 (partial: stakeholder-harm half) | V2 | V2 | EQUIVALENT (all three) |
| C3 | Raw headcount (180 vs 90) favors Route 1 only under equal weighting, which should be rejected; severity-weighting flips the result to Route 2 | V3 + V4 (partial: normative half) | V6 | V5 (partial: severity-beats-headcount half) | EQUIVALENT (all three) |
| C4 | Worst-case criterion (maximin / minimax): comparing the worst-off outcome under each allocation favors Route 2 | V5 | V5 (partial: minimax half) | V5 (partial: minimax-regret half) | EQUIVALENT (all three) |
| C5 | Expected dollar cost of failing Route 2 exceeds Route 1's $25k: multi-day duty-of-care (hotels/meals), EU261-style regulatory compensation, rebooking costs | V2 | V3 (partial: cost core) | V3 | EQUIVALENT (all three) |
| C6 | Reputational failure modes are asymmetric: a compensated overnight delay is routine; a three-day international strand produces lifetime customer loss, press/regulator attention | V6 | V3 (partial: reputational clause only) | V4 | EQUIVALENT: R12-V6 ≡ R46-V4. R26 participates only via an undeveloped clause inside V3 — counted as partial, see §3.4 |
| C7 | Mitigation package for the losing route (Route 1): immediate hotel/meal vouchers, proactively confirmed morning seats, proactive communication | V11 (partial: Route 1 half) | V7 | V11 | EQUIVALENT (all three) |
| C8 | Alternative-protection decision rule: attempt to protect the 45 connections by other means (interline/partner rebooking, holding the international departure); if that succeeds, the spare goes to Route 1 instead | V12 + V11 (partial: interline half) | V8 | V9 + V10 | EQUIVALENT (all three) at the decision-rule level; sequencing varies within cluster, see §3.2 |
| C9 | Irreversibility/recoverability as the allocation principle: scarce capacity goes to the problem money and time cannot later fix | V10 | V6 (partial: "no recovery path is categorically worse" strand) | — (present only as components of V2/V5, no separate equivalent view) | EQUIVALENT: R12-V10 ≈ R26-V6 strand; R46 partial only. Borderline, see §3.3 |
| C10 | Tonight's allocation shapes tomorrow's network state: where the aircraft (and crew) end the night, and the morning rebooking load, are second-order allocation factors | V7 | — | V8 | EQUIVALENT: R12-V7 ≡ R46-V8 on the positioning core; R12 adds a rebooking-load mechanism, see §3.5. Absent from R26 |

## 2. Views appearing in no other run (no EQUIVALENT member elsewhere)

### R12
- **R12-V8** — Verify Route 1's "morning rebooking" is a protected recovery, not optimistic seat-finding, before committing. An epistemic precondition on Route 1's assumed recoverability; the other runs treat the morning recovery as given (R26-V7's "confirm seats" is mitigation execution, not premise verification — see §3.6).
- **R12-V9** — Legal/physical operability check: crew duty time, aircraft range, and gauge must permit the spare to fly the chosen route (and a 90-seat problem may fit the spare better). A material constraint no other run raises as a decision input (R46-V8 mentions crew duty only incidentally, inside the positioning view).

### R26
- **R26-V4** — Serving Route 2 also benefits its 45 non-connecting passengers, who arrive tonight instead of joining a rebooking queue. The only run to name this stakeholder group as a distinct affected interest.

### R46
- **R46-V6** — Epistemic challenge to the scenario premise: "no rebooking for three days" likely describes only the airline's own aircraft; harm should be measured as the residual after the full recovery toolkit (interline, alliance, alternate hubs, ground transport, holding the flight) is exhausted. Related to C8 but materially distinct: it disputes the stated fact and reframes how harm is measured, rather than prescribing a contingency strategy (§3.7).
- **R46-V7** — Only-remedy allocation frame that flips toward Route 1: Route 1's harm is irreducible by any lever except the spare aircraft, while Route 2's may be reducible through other channels, so under this frame the scarce asset should go to Route 1. The inverse application of R12-V10's scarcity principle — same abstract criterion, opposite factual premise and opposite direction — hence not equivalent (§3.3).

## 3. Borderline-case justifications

**3.1 Composite views split across clusters (R12-V4, R26-V3, R26-V5/V6, R46-V5).** Extraction granularity differs: R12 separates headcount (V3), severity-flip (V4), maximin (V5), and irreversibility (V10) into four views, while R26-V5 and R46-V5 each compress two or three of these criteria into one composite ("minimax and expected cost converge"). I matched at the component level and marked memberships "(partial)". The convergence claim itself ("multiple decision rules agree") is not counted as an independent view in any run, since each of its component rules is separately matched (C3, C4, C5).

**3.2 C8 sequencing variation.** R26-V8 and R46-V9 prescribe a bounded *pre-commit* check (protect the connections first, then release the aircraft); R12-V11/V12 and R46-V10 prescribe *commit-to-Route-2-now while working reprotection in parallel, with a reversal trigger*. The trigger condition (connectors protectable by other means) and the consequence (aircraft flips to Route 1) are identical across all runs, so I classified the cluster EQUIVALENT at the decision-rule level. A stricter reading focused on operational sequencing would split it into two sub-clusters: pre-commit check {R26-V8, R46-V9} vs parallel-with-reversal {R12-V11/V12, R46-V10} — either way, all three runs are represented.

**3.3 R12-V10 vs R26-V6 vs R46-V7 (the scarcity/irreversibility principle).** R12-V10 ("allocate scarce capacity where substitutes don't exist" → Route 2) and the recoverability strand of R26-V6 ("a delay with no recovery path is categorically worse") deploy the same criterion in the same direction and are matched EQUIVALENT, though R26 uses it to reject headcount weighting rather than as a named allocation principle. R46-V7 invokes the identical abstract principle but with the opposite factual premise (Route 2 *does* have substitutes via reprotection; Route 1 does not) and reaches the opposite conclusion. Same criterion, different mechanism and consequence — RELATED BUT MATERIALLY DISTINCT, so R46-V7 is listed as unique. R46's *harm-side* irreversibility content lives in V2 (matched in C2), which is why C9 shows R46 as partial-only.

**3.4 R26-V3's reputational clause vs C6.** R26 mentions "outsized reputational damage" only as one cost term inside its expected-cost view; R12-V6 and R46-V4 develop reputation as a standalone asymmetry (viral complaints, regulator filings, lifetime customer loss, press). The mechanism is the same, so R26 gets partial membership, but the developed cluster equivalence is R12-V6 ≡ R46-V4. R12-V6 additionally asserts the connectors skew high-value — an extra affected interest not present in R46-V4; not enough to break equivalence of the core, but noted as a within-cluster increment unique to R12.

**3.5 C10 (R12-V7 vs R46-V8).** Both hold that tonight's allocation determines tomorrow's network state via aircraft (and crew) positioning, and both note this can compound the case for Route 1. EQUIVALENT on that core. R12-V7 adds a second mechanism — flying Route 1 clears 180 passengers from tomorrow's rebooking load, whereas choosing Route 2 pushes that burden onto a morning schedule whose seats must actually exist. That rebooking-load strand has no counterpart in R46-V8; it is an increment within the cluster rather than a separate view, since R12 packaged the two mechanisms as one view.

**3.6 R12-V8 vs R26-V7.** Superficially both involve morning seats for Route 1. R26-V7 (and R46-V11) *execute* confirmation as mitigation, presupposing recovery capacity exists; R12-V8 *questions whether it exists* and makes verification a precondition of the whole recommendation. Different function in the argument (premise audit vs remedy), so RELATED BUT MATERIALLY DISTINCT — R12-V8 stays unique.

**3.7 R46-V6 vs C8.** R46-V6 could be read as merely the rationale for the C8 strategy, and R46's own extraction notes V9/V10 operationalize it. But R12 and R26 prescribe the reprotection attempt without disputing the scenario's "no rebooking for three days" claim; only R46 asserts the stated fact is probably own-metal-only and redefines the harm measure as post-toolkit residual. That is a distinct causal/epistemic mechanism, not just a strategy, so V6 is classified unique (RELATED to C8, not equivalent).

## 4. Summary counts

| | R12 | R26 | R46 |
|---|---|---|---|
| Views extracted | 12 | 8 | 11 |
| Views with an EQUIVALENT cross-run match (incl. partial memberships) | 10 (V1–V7, V10–V12) | 7 (V1–V3, V5–V8) | 9 (V1–V5, V8–V11) |
| Unique views | 2 (V8, V9) | 1 (V4) | 2 (V6, V7) |

Core shared structure across all three runs: bounded-vs-irreversible harm asymmetry (C1/C2), rejection of raw headcount in favor of severity weighting (C3), worst-case reasoning (C4), expected-cost asymmetry (C5), Route 1 mitigation (C7), and the alternative-protection decision rule with a flip-to-Route-1 trigger (C8). Differentiation concentrates in operational-constraint auditing (R12), an additional beneficiary group (R26), and premise skepticism plus the inverted scarcity frame (R46).
