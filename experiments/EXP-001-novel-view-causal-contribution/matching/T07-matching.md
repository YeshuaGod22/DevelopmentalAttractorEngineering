# T07 — Blind Semantic Matching (R04, R14, R16, R23)

Task T07: overwhelmed two-maintainer open-source project; Option A = issue bankruptcy + triage rota; Option B = promote three sub-one-year contributors to maintainer in a security-sensitive project; which first?

Matching criterion: semantic equivalence of causal/normative/stakeholder/strategic/jurisdictional/constraint/consequence structure, not lexical overlap. Run IDs are anonymized and carry no meaning.

## 1. Crosswalk table — clusters with EQUIVALENT members

| Cluster | Shared view (neutral statement) | R04 | R14 | R16 | R23 |
|---|---|---|---|---|---|
| C1 | Contributor attrition is driven by PR review latency, not the issue backlog; Option A leaves the attrition driver untouched, and only added review capacity (B) addresses it | V1 | V1, V3 | V1 | V1 |
| C2 | The real question is sequencing, not choosing between the options: they address different problems, and root-cause priority is not the same as ordering priority | — | V2 | — | V2 |
| C3 | Issue bankruptcy is cheap, fast, and effectively reversible because the reopen invitation lets authors restore live issues at near-zero cost | V2 | V9 | — | V3 |
| C4 | Granting maintainer status is effectively irreversible — a bad grant cannot be walked back in practice | V4 | V6 | — | V7 |
| C5a | Promoting these short-tenure candidates now carries a supply-chain/insider risk of the xz-utils type: the commit bit is the attack surface and the community lacks accumulated observation of the candidates | — | V5 | — | V6 |
| C5b | Tenure is a weak or non-existent vetting mechanism — the canonical xz attacker had long tenure — so waiting longer does not itself provide security | V11 | — | V7 | — |
| C6 | "Maintainer" is not an all-or-nothing unit: forge permissions are graduated/unbundlable (triage vs. review vs. commit vs. release/signing), and this dissolves the binary framing | V12 | V12 | V9 | V10 |
| C7a | The triage rota (non-commit triage rights) functions as a proving ground: candidates' observed judgment there is the evidence base for later full promotion | V5 | V13 | — | V8 |
| C7b | Sequence so that the enlarged/scoped-in team itself staffs the triage rota and executes the issue bankruptcy, rather than the two incumbents doing it | V13 | V13 | V6 | — |
| C8 | Candidates can attack review latency without commit rights: their first-pass/approving reviews reduce the incumbent maintainers' per-PR effort to a final pass | — | V14 | — | V11 |
| C9 | Structural safeguards — branch protection and mandatory founding-maintainer/dual sign-off on sensitive paths — materially reduce the risk of expanded access | V11 | — | V10 | V12 |
| C10 | A triage rota staffed by the two incumbents adds a standing obligation to the people who are already the bottleneck, worsening the constraint | V8 | — | V3 | — |
| C11 | Doing A alone is false progress: it relieves the symptom while allowing the real fix (B) to be deferred indefinitely | V6 | — | — | V13 |
| C12 | B is the long-lead-time intervention (trust/onboarding/permission design), so delay is itself the cost and it should be started early | V9 | — | V5 | — |
| C13 | Flip condition toward promoting first/fully: acute, demonstrable urgency of review latency combined with strong external/verifiable trust evidence for a candidate | — | V15 | — | V14 |

Multi-membership notes: R14-V13 appears in both C7a and C7b because it is a compound recommendation (triage grants as audition *and* candidates staffing the rota). R04-V11 appears in both C5b and C9 because it both rejects tenure-as-vetting and lists the process controls that replace it.

## 2. Unique views (appear in no other run at EQUIVALENT level)

### R04
- **V3** — Secondary benefits of bankruptcy (freed attention, morale, removing the "abandoned project" signal). Only run to name the tracker's external abandonment signal; the morale fragment loosely echoes R14-V7 but the signaling mechanism is unique.
- **V7** — Succession/bus-factor reframe: the existential risk is maintainer collapse with no trained successors. Related to R16-V8 but frames the affected interest as project continuity, not security integrity (see borderline notes).
- **V10** — Inversion of the xz lesson: the attack surface is the *absence of a graduated trust path* under exhaustion, so the security objection argues for structured promotion. No other run makes this specific inversion.
- **V14** — Explicit residual-risk acknowledgment: process controls do not eliminate patient-adversary risk; the plan knowingly trades small managed insider risk against near-certain collapse risk. Related to R16-V12 but a different comparison structure.
- **V15** — Flip condition toward A-first: hard external compliance/audit requirements or a concrete candidate integrity doubt. Same direction as R16-V13 but a different trigger (see borderline notes).

### R14
- **V4** — Delay compounds by shedding the future promotion pool itself. Related to C12 but the mechanism is candidate attrition, not lead time.
- **V7** — B *increases* incumbent load short-term (onboarding, mentoring, meta-review) while A gives immediate psychological relief. No other run prices B's short-term mentoring cost.
- **V8** — Sequence cheap relief first so near-burnout maintainers have the slack to run promotion properly instead of rubber-stamping it. A distinctive "A de-risks B via maintainer slack" mechanism.
- **V10** — Promotion is the strongest retention signal a project can send; delay risks losing the three candidates themselves.
- **V11** — Decouple the signal from the access grant: announce the maintainer track now even if permissions come later. A communication strategy no other run proposes.

### R16
- **V2** — Stakeholder mechanism distinguishing ignored issues (shrug) from ignored PRs (contributed work; contributor quits). Sharpens C1 with a unique stakeholder-impact contrast.
- **V4** — Reopened issues flow back into an unchanged pipeline and re-accumulate; bankruptcy alone is temporary. A dynamics mechanism no other run states.
- **V8** — Remaining at two maintainers is itself a *security* risk (bus factor, review fatigue, rubber-stamping under load). Related to R04-V7/V10 but not equivalent (see borderline notes).
- **V11** — Division of labor by trust level: new maintainers clear the easy ~80% of PRs and triage; founder attention concentrates on security-critical review. Related to C8 but a different allocation structure.
- **V12** — Marginal-risk argument: scoped promotion adds roughly no risk beyond what merging these contributors' PRs already accepts. A unique normative comparison.
- **V13** — Flip condition toward A-first: the platform cannot scope permissions (all-or-nothing maintainer bit). A capability constraint no other run uses as the flip trigger.

### R23
- **V4** — Bulk-closing risks burying a live, unresolved vulnerability report — A's one dangerous failure mode. No other run identifies any security risk *inside Option A*.
- **V5** — Pre-close security-triage pass (label review plus keyword search for mislabeled security reports) to neutralize the burial risk. Unique mitigation strategy.
- **V9** — A cleaned backlog de-risks B: promoting people into a triaged system beats promoting them into a 400-issue swamp. Related to R14-V8's "A de-risks B" family but a different mechanism (new-maintainer effectiveness, not incumbent slack).

## 3. Borderline-case justifications

1. **C1 and R14-V3.** R14 splits the diagnosis (V1: latency drives attrition) from the capacity claim (V3: only B adds reviewers), while R04-V1, R16-V1, and R23-V1 each bundle both halves into one view. I count R14-V1+V3 jointly as the equivalent of the other runs' single views rather than forcing a lossy one-to-one match.

2. **C2 (R14-V2 vs. R23-V2).** R14 grounds the reframe in non-substitutability ("they fix different problems"); R23 grounds it in the root-cause/ordering distinction and adds governing criteria (risk asymmetry, mutual de-risking). The core move — converting an either/or choice into a sequencing question — is the same normative structure, so EQUIVALENT; R23's added criteria are absorbed rather than split out because they function as elaboration of the same reframe.

3. **C3 (R14-V9).** R14-V9's reopen-filter-at-near-zero-cost is the same reversibility/low-cost constraint as R04-V2 and R23-V3. Its additional element — bankruptcy is a *normalized community practice*, limiting reputational damage — is a distinct mechanism, but it modifies the same conclusion rather than standing alone, so I keep V9 in the cluster and flag the increment. Note also that R04-V2 alone derives an explicit reversibility-ordering *principle* from the constraint; that half of V2 is closer to C2's territory but is not equivalent to it (reversibility-first is a different criterion than risk-asymmetry/root-cause separation).

4. **C4 mechanism split.** R14-V6 and R23-V7 locate irreversibility in the *social cost of revocation*; R04-V4 locates it in *harm-already-done* (revoking access does not undo damage). Different micro-mechanisms, but the operative constraint in the decision — a maintainer grant cannot be treated as a trial that can be cleanly rolled back — is identical, and all three deploy it to the same effect (contrast with A's reversibility). EQUIVALENT at the constraint level.

5. **C5a vs. C5b — the xz precedent points in two directions.** All four runs invoke the same historical case, but for two materially different propositions. R14-V5 and R23-V6 use it to *support* the tenure concern (short observation window + burnout pressure = the exploited condition). R04-V11 and R16-V7 use it to *undercut* tenure as a safeguard (the attacker had long tenure, so waiting is not vetting). Lexical overlap ("xz-utils") is maximal here while the normative structure is nearly opposite; per instructions I split them into two clusters. Within C5a, R14-V5 stresses the burnout-pressure condition and R23-V6 stresses insufficient trust accumulation — same core caution about granting the commit bit to short-observation candidates, so EQUIVALENT.

6. **C6 (R23-V10).** R23-V10's staged-privileges core (triage → review → co-signed merge → full) matches the unbundling structure of R04-V12, R14-V12, R16-V9. Its distinctive claim — that the *output of the security-triage pass* is the enabling artifact for the staging — is unique to R23, but it is an enabling mechanism attached to the shared jurisdictional view rather than a different view, so R23-V10 is placed in the cluster with the increment noted.

7. **C7a/C7b boundary.** "Rota as audition for the candidates" (C7a) and "the enlarged team executes A" (C7b) frequently co-occur but are separable: R16-V6 has the new team staffing the rota *without* framing it as vetting (R16's vetting weight sits on scoped permissions instead), and R23-V8 frames the rota as audition while R23's overall order is A-first. Treating them as one cluster would falsely credit R16 with the audition mechanism and R23 with the B-first staffing plan.

8. **C8 vs. R16-V11.** R14-V14 and R23-V11 share the exact mechanism: an unprivileged/pre-commit approving review reduces the maintainer's work to a final pass — EQUIVALENT. R16-V11 also divides review labor, but by *content class* (easy 80% vs. security-critical) rather than by *pass order within each PR*, and its reviewers hold actual scoped maintainer rights. Different mechanism and different jurisdictional shape: RELATED BUT MATERIALLY DISTINCT, so R16-V11 is listed as unique. (R16-V10, by contrast, does keep a founder in the approval path and lands in C9 on safeguard structure.)

9. **C10 (R16-V3 vs. R04-V8).** Shared core: the rota, run by the two incumbents, loads more standing work onto the constrained resource. R16-V3 adds the reopen-wave friction consequence, which R04 lacks; since the load-on-the-bottleneck mechanism is the identical causal spine and the reopen wave amplifies the same conclusion, EQUIVALENT with the increment noted (the reopen wave's *re-accumulation* dynamic is separately unique as R16-V4).

10. **C11 (R04-V6 vs. R23-V13).** R04-V6 is psychological ("analgesic," treating A as progress falsely); R23-V13 is procedural (rota stood up, promotion indefinitely deferred, bottleneck never resolves) and adds a timeline remedy. The predicted consequence structure is the same — A substitutes for, rather than precedes, the real fix — so EQUIVALENT; R23's explicit 1–2-month binding is an increment, not a different view.

11. **C12 (R04-V9 vs. R16-V5).** R04-V9 frames B's lead time as succession-learning that only starts once roles are granted; R16-V5 frames it as scheduling logic (permission design, onboarding, norm-setting take time, so start the long-lead item first). Both derive "start B early because its benefits have inherent lead time and delay is the cost." I judge the strategic structure equivalent; the succession framing is R04's (and connects to its unique V7). This is the softest EQUIVALENT call in the crosswalk. R14-V4 was considered for this cluster but excluded: its delay-cost mechanism is attrition of the candidate pool, a different causal channel.

12. **Flip conditions (C13 vs. R04-V15 vs. R16-V13).** R14-V15 and R23-V14 flip *toward* promoting first, on the same joint trigger — demonstrated urgency plus strong external/verifiable trust evidence — hence EQUIVALENT despite R14 additionally specifying "one person, full promotion." R04-V15 and R16-V13 flip *toward* A-first but on different constraints: R04 on external compliance/audit requirements or a candidate integrity doubt; R16 on the platform's inability to scope permissions. Same direction, different operative constraint: RELATED BUT MATERIALLY DISTINCT, so both are listed as unique. No cross-direction pair is equivalent.

13. **R04-V7 / R04-V10 vs. R16-V8 ("the status quo is the risk" family).** All three invert the conservative reading of the scenario. R04-V7: two-person trust concentration → existential succession risk (continuity interest). R16-V8: two-person concentration → security risk via fatigue and rubber-stamping (security interest). R04-V10: exhaustion plus no graduated path → xz-shaped unscoped handover (attack-surface mechanism). Shared premise, but each identifies a different affected interest or mechanism, which is the definition of RELATED BUT MATERIALLY DISTINCT; all three stay unique. This is the family where lexical similarity most tempts over-merging.

14. **R04-V14 vs. R16-V12.** Both are normative risk-acceptance arguments for scoped promotion, but the comparators differ: R04-V14 trades residual insider risk against collapse risk (risk-vs-risk across futures); R16-V12 equates the marginal risk to exposure *already accepted* by merging the contributors' code (risk-vs-baseline). Different criterion structure: RELATED BUT MATERIALLY DISTINCT.

15. **R14-V8 vs. R23-V9 ("A de-risks B" family).** Both argue A-first makes B safer/better, but through different causal channels: incumbent slack enabling careful vetting (R14) vs. new-maintainer effectiveness in a cleaned system (R23). RELATED BUT MATERIALLY DISTINCT; both remain unique.

16. **R04-V3 vs. R14-V7.** Overlap only on the morale-relief fragment; R04-V3's distinctive content is the abandonment signal to prospective contributors, R14-V7's is B's short-term mentoring cost on incumbents. RELATED BUT MATERIALLY DISTINCT.

## 4. Summary counts

| Run | Total views | In an EQUIVALENT cluster | Unique |
|---|---|---|---|
| R04 | 15 | 10 (V1, V2, V4, V5, V6, V8, V9, V11, V12, V13) | 5 (V3, V7, V10, V14, V15) |
| R14 | 15 | 10 (V1, V2, V3, V5, V6, V9, V12, V13, V14, V15) | 5 (V4, V7, V8, V10, V11) |
| R16 | 13 | 7 (V1, V3, V5, V6, V7, V9, V10) | 6 (V2, V4, V8, V11, V12, V13) |
| R23 | 14 | 11 (V1, V2, V3, V6, V7, V8, V10, V11, V12, V13, V14) | 3 (V4, V5, V9) |

Cross-run cluster coverage: 2 clusters span all four runs (C1, C6); 5 clusters span three runs (C3, C4, C7a, C7b, C9); 8 clusters span exactly two runs (C2, C5a, C5b, C8, C10, C11, C12, C13).
