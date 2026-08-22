# T12 Semantic Matching — R01, R07, R43, R45

Task T12: property manager with $40,000; Option A (roof replacement, 2–4 yr life, 8%/yr escalation, cascading failure damage) vs. Option B (lobby/hallway renovation; 6 vacancies at $7,200/mo; renovated comps at 95% occupancy).

Blind semantic matching. Run IDs are anonymized and carry no meaning; no condition labels inferred. Classification is by causal/normative/stakeholder/strategic/constraint/consequence structure, not lexical overlap. "(part)" marks a view that bundles this cluster's content with another cluster's.

## 1. Crosswalk of matched view clusters

| Cluster | Shared substantive structure | R01 | R07 | R43 | R45 | Classification |
|---|---|---|---|---|---|---|
| C1 | Vacancy loss is certain, ongoing, and quantified (~$86,400/yr); closing roughly half the gap to comp occupancy recovers ~$43,200/yr, giving the $40k renovation a sub-one-year payback | V1 | V3 | V4 (part) | V2 | EQUIVALENT (all 4) |
| C2 | Deferring the roof has a small, priced escalation cost (~$3.2k yr 1, ~$6.6k–$7k over 2 yrs at 8% compounding on a $40k base) | V2 | V1 | V2 | V4 | EQUIVALENT (all 4) |
| C3 | Roof failure is a cascading, asymmetric tail risk: interior damage, tenant claims/displacement, liability, emergency costs — loss well beyond the roof itself | V3 | V2 | V1 | V5 | EQUIVALENT (all 4) |
| C4 | Fiduciary/asset-stewardship norm favors the roof: deferred envelope maintenance is the characteristic way owners destroy building value | V4 | — | V3 | — | EQUIVALENT (R01, R43) |
| C5 | Direct economic comparison: the certain vacancy bleed dwarfs the cost of roof deferral, so the renovation dominates on expected value / timing-certainty asymmetry | V5 | V8 | — | V1 | EQUIVALENT (R01, R07, R45); see borderline B2, B3 |
| C6 | Sequencing logic: the options are not truly mutually exclusive — renovation-recovered rent funds the roof within its 2–4 yr window, whereas roof-first leaves no funding engine (B-then-A dominates A-first) | V6 | V7 (part) | V5 | V6 | EQUIVALENT (all 4) |
| C7 | Binding commitment mechanism: earmark recovered rent into a dedicated roof reserve with a hard replacement deadline (year 2 / next budget year) — B only as B-then-A, never B-instead-of-A | V10 (part) | V7 (part) | V10 | V7 | EQUIVALENT (all 4); see borderline B5 |
| C8 | Independent roof inspection (second opinion) plus small interim maintenance/patching budget to carry the roof safely through the deferral | V10 (part) | V10 | V9 (part) | V8 | EQUIVALENT (all 4) |
| C9 | Demand-side diligence as a precondition: verify with leasing agent/brokers/prospects that the common areas — not pricing, unit condition, or market — are the binding constraint before spending | V11 | — | V8 | V9 | EQUIVALENT (R01, R43, R45); absent from R07 |
| C10 | Alternative-cause critique: two declining prospects is thin evidence; vacancies may stem from pricing, unit condition, marketing, or a soft market, making renovation ROI speculative | V7 | — | V6 | V11 (part), V9 (embedded) | EQUIVALENT (R01, R43); R45 carries it partially; absent from R07 as a critique (R07 asserts the opposite, see C11) |
| C11 | Tenant citations as strong direct causal evidence: prospects explicitly naming the common areas when declining is unusually clean attribution, elevating confidence in occupancy recovery | — | V4 | V4 (part) | V3 | EQUIVALENT (R07, R45; R43 partial) |
| C12 | Roof-side flip condition: if inspection shows the roof at the short end (active leaks / credible failure within ~12–24 months), the decision flips to Option A regardless of the vacancy math | V9 | V12 | V9 (part) | V11 (part) | EQUIVALENT (all 4) |

Observed tension worth flagging (not a matching category): C10 and C11 are opposed readings of the same evidence. R01 holds only the skeptical reading (V7), R07 holds only the confident reading (V4), R43 holds both (V4 asserts the causal link, V6 flags it as thin), and R45 leans confident (V3) while retaining the alternative-cause hedge inside its diligence and flip views (V9, V11).

## 2. Views appearing in no other run (unique views)

### R01
- **V8** — Stakeholder mechanism: water intrusion drives existing-tenant churn and bad reviews, so the roof protects the very revenue stream the lobby is meant to attract. Borderline-unique; see B1.

### R07
- **V5** — Constraint: $40k is very likely insufficient for a full roof replacement on a 60-unit building, so Option A as stated is a partial repair or down payment, not a replacement. No other run questions the $40k roof price; all others compute escalation on a $40k base (C2). This is a materially different constraint structure.
- **V6** — Normative criterion of completeness-per-dollar: $40k buys an incomplete roof fix but a complete renovation solution. Derivative of V5; no analogue elsewhere.
- **V9** — Strategy: obtain 2–3 firm replacement quotes to convert "cost unknown" into a real number. Distinct from the C8 inspection cluster: quotes are price discovery, inspection is condition assessment; see B4.
- **V11** — Strategy: verify insurance coverage for interior damage to partially transfer the tail risk during deferral. No other run proposes risk transfer.
- **V13** — Flip condition: if $40k genuinely covers a complete replacement (coating-eligible/small-footprint roofs), the comparison tightens toward A. Derivative of V5; unique.

### R43
- **V7** — Meta-criterion: the two frames price different unknowns (failure probability vs. conversion rate) and each assumes the other's unknown benign, so both uncertainties must be held in view rather than netted out. See B3 for why this is not folded into C5.
- **V11** — Explicit acknowledgment that the plan accepts a ~2-year window of elevated roof risk and would look reckless in hindsight if the roof failed early — the recommendation as an explicit bet, not a proof. No other run names the hindsight/accepted-risk structure.

### R45
- **V10** — Normative criterion: because roof failure destroys (rather than delays) value, the correct posture is B-with-hard-commitment, not B-instead-of-A. Borderline-unique; see B5.

## 3. Borderline-case justifications

- **B1 (R01-V8 vs. C3/C12 members).** R01-V8 shares surface content with R45-V5 ("additional vacancies" from failure) and R07-V12 ("failure would empty units faster than a renovated lobby fills them"), and R01-V3 itself notes a leaking building cannot hit 95% occupancy. But in the other runs this mechanism appears only as a clause inside a broader tail-risk or flip-condition view, whereas R01-V8 is a standalone stakeholder analysis with a distinct causal chain (churn of existing tenants + reputational damage via reviews deterring prospects). Ruling: RELATED BUT MATERIALLY DISTINCT from C3/C12 members; listed as R01-unique at the standalone-view level.

- **B2 (R07-V8 within C5).** R07-V8 runs the same comparison structure as R01-V5 and R45-V1 (cost of delay vs. cost of vacancy, renovation dominates) but computes the delay cost as ~$25k on a hypothetical $150k roof — a premise no other run shares (it follows from R07's unique V5). The comparison's causal/consequence structure is the same; only the magnitudes differ because of the differing cost premise. Ruling: EQUIVALENT within C5, with the premise difference attributed to R07-V5's unique constraint rather than to a different comparison structure.

- **B3 (R43-V7 vs. C5).** R43-V7 addresses the same territory as C5 (certain large loss vs. possible tail loss) but its substantive claim is epistemic and procedural: the frames do not reconcile, each quietly assumes the other's unknown away, and both uncertainties must be carried unnetted. C5 members net the comparison out and declare dominance. Introducing a different criterion (refusal to net) makes this RELATED BUT MATERIALLY DISTINCT from C5 — hence listed as R43-unique.

- **B4 (R07-V9 vs. C8).** Both involve engaging roof professionals before committing. C8's mechanism is condition assessment (remaining life, failure probability) plus interim maintenance; R07-V9's mechanism is price discovery (firm quotes converting an unknown cost into a planning number). These target different unknowns and feed different decisions (feasibility/budgeting vs. timing/risk). Ruling: RELATED BUT MATERIALLY DISTINCT; R07-V9 listed as unique. (R07 separately holds a genuine C8 member, V10.)

- **B5 (R45-V10 vs. C7 and R01-V4/C4).** R45-V10 supplies the normative justification for the C7 commitment structure, and its "B-with-commitment, not B-instead-of-A" formulation matches the warning embedded in R43-V10 ("renovated common areas over a failing roof"). But R43-V10's substantive content is the binding reserve mechanism (a strategy), while R45-V10 is the asymmetric-downside criterion itself, stated as the reason the recommendation takes the form it does. It also echoes R01-V4's asymmetry logic but reaches a different conclusion (commitment structure rather than roof-first). Ruling: RELATED BUT MATERIALLY DISTINCT from both C7 and C4; listed as R45-unique, with the caveat that its content is the weakest of the uniques — it is a justificatory layer over C7 rather than a wholly new mechanism.

- **B6 (R43-V4 spanning C1 and C11).** R43-V4 bundles the quantified vacancy loss (C1) with the causal attribution via declining tenants and the occupancy gap (C11). It is counted as a partial member of both clusters rather than forced into one; neither cluster's membership claim rests on R43-V4 alone.

- **B7 (R45-V11 spanning C12 and C10).** R45-V11 states two flip triggers: the roof-side trigger (C12, clearly equivalent to R01-V9/R07-V12/R43-V9) and a demand-side trigger (Option B collapses if vacancies stem from pricing/soft market), which is the alternative-cause critique of C10 in conditional form. Counted as a partial member of both. The C10 critique is judged present-but-partial in R45 because it appears only inside conditional/diligence views (V9, V11), never as a standalone epistemic challenge as in R01-V7 and R43-V6.

- **B8 (R01-V9 directionality).** R01-V9 states the hinge in both directions (2+ years runway → B dominates; failure inside ~18 months → A dominates), while R07-V12, R43-V9, and R45-V11 state primarily the flip-to-A direction. The controlling structure — roof-life reliability as the decisive uncertainty with a stated threshold — is the same. Ruling: EQUIVALENT within C12.

- **B9 (C4 membership).** R01-V4 bundles the fiduciary norm with a tail-risk-insurance argument (wide error bars, correlated downside); R43-V3 is the stewardship norm alone. The shared core — deferred envelope maintenance as the characteristic value-destruction pattern, making roof-first the fiduciary default — is present in both. Ruling: EQUIVALENT; R01-V4's insurance-logic surplus is covered by C3/C5 content rather than constituting a separate unmatched view.

## Summary counts

| Run | Total views | In shared clusters | Unique |
|---|---|---|---|
| R01 | 11 | 10 | 1 (V8, borderline) |
| R07 | 13 | 8 | 5 (V5, V6, V9, V11, V13) |
| R43 | 11 | 9 | 2 (V7, V11) |
| R45 | 11 | 10 | 1 (V10, borderline) |

R07 is the outlier on unique content, driven largely by one distinct constraint (V5: $40k cannot buy a full roof) from which three of its five uniques derive. R07 is also the only run lacking both the demand-side diligence strategy (C9) and any standalone skeptical reading of the tenant-citation evidence (C10).
