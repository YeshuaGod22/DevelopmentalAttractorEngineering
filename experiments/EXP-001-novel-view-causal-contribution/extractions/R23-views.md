# R23 View Extraction — Task T07 (maintainer overload: issue bankruptcy vs. promotions)

Blind extraction of substantive task-relevant views. Types: causal mechanism / stakeholder-impact / normative criterion / constraint / jurisdiction / strategy / predicted consequence.

## V1 — The backlog and the review latency are different problems
- **Paraphrase:** The 400-issue backlog is mainly a signaling-and-attention problem, while the six-week PR review time is the actual retention problem; contributors leave because their work sits unreviewed, so only added review capacity (Option B) addresses the stated cause of attrition.
- **Type:** causal mechanism
- **Evidence:** The response distinguishes the two wounds up front, conceding that B fixes the driver of contributor attrition and A does not.

## V2 — Root-cause priority is not the same as sequencing priority
- **Paraphrase:** Deciding which option fixes the root cause is a different question from which to do first; sequencing should be governed by risk asymmetry and by whether one option makes the other safer.
- **Type:** normative criterion
- **Evidence:** The response explicitly separates "which fixes the root cause" from "which should be done first" and names risk asymmetry plus mutual de-risking as the governing criteria.

## V3 — Option A is low-cost and reversible
- **Paraphrase:** Issue bankruptcy is cheap, fast, and reversible because a wrongly closed issue can be reopened by its author with a click, and the closing message invites exactly that.
- **Type:** constraint
- **Evidence:** The response characterizes A's residual cost as a day or two of focused work with mistakes recoverable by reopening.

## V4 — Bulk-closing risks burying live security reports
- **Paraphrase:** In a project deployed in security-sensitive environments, a bulk close could entomb an unresolved vulnerability report, converting a housekeeping action into a latent security incident.
- **Type:** predicted consequence
- **Evidence:** The response names the closed-and-forgotten vulnerability report as A's one genuinely dangerous failure mode.

## V5 — A pre-close security-triage pass neutralizes the burial risk
- **Paraphrase:** Before any bulk close, triage all security-labeled issues and keyword-search the backlog for likely mislabeled security reports (e.g., crash, overflow, auth, bypass), exempting matches from the bulk action.
- **Type:** strategy
- **Evidence:** The response prescribes this pass as step one of its plan, noting that reporters often fail to label security issues correctly.

## V6 — Short tenure is a trust-accumulation problem, not a competence problem
- **Paraphrase:** The candidates' sub-one-year history matters because the community has had less time to observe their judgment under pressure and to rule out patient social engineering of the kind seen in supply-chain compromises, even though their competence is granted.
- **Type:** causal mechanism
- **Evidence:** The response reframes the tenure concern as insufficient accumulated trust, citing the commit bit as the attack surface and invoking the xz-utils precedent.

## V7 — Granting maintainership is effectively irreversible
- **Paraphrase:** Revoking maintainer status later is socially costly and typically reads as a crisis, so the promotion decision cannot be undone the way a closed issue can be reopened.
- **Type:** predicted consequence
- **Evidence:** The response contrasts un-ringing the promotion bell with the one-click reversibility of reopening an issue.

## V8 — The triage rota doubles as a vetting audition for the candidates
- **Paraphrase:** Including the three candidates in the triage rota with non-commit permissions exposes their judgment on ambiguous reports, hostile reporters, and security-flagged items, converting "competent contributor" into evidence-based maintainer trust over six to eight weeks.
- **Type:** strategy
- **Evidence:** The response argues triage rights require no commit access yet reveal exactly the judgment a promotion decision needs.

## V9 — A cleaned backlog makes new maintainers effective
- **Paraphrase:** Promoting people into a 400-issue swamp wastes their early energy on archaeology, whereas promoting them into a triaged backlog with a working rota gives them a functioning system to join.
- **Type:** causal mechanism
- **Evidence:** The response gives this as the second reason A actively de-risks B.

## V10 — The security-triage pass enables graduated privileges
- **Paraphrase:** Knowing which open items are security-relevant tells current maintainers what new maintainers must not yet touch, enabling a staged promotion path (triage, then PR review without merge, then merge with co-sign, then full) instead of an all-or-nothing grant.
- **Type:** strategy
- **Evidence:** The response presents the pass's output as precisely the artifact a graduated-privilege promotion requires.

## V11 — Interim PR-review rights capture most of B's benefit without the commit bit
- **Paraphrase:** The candidates can start reviewing PRs immediately; a thorough review from a trusted-but-unprivileged contributor reduces the maintainers' work to a final-pass approval, easing the review bottleneck during the vetting window.
- **Type:** strategy
- **Evidence:** The response insists the PR problem should not wait for full promotion and recommends review rights starting now.

## V12 — Structural safeguards make eventual promotion safer than the binary framing suggests
- **Paraphrase:** Branch protection, mandatory co-review, and two-maintainer sign-off on security-sensitive merges materially reduce the risk of granting maintainership, even after promotion.
- **Type:** strategy
- **Evidence:** The recommendation retains dual sign-off on security merges post-promotion and cites branch protection as changing the risk calculus.

## V13 — The failure mode of A-first is procrastination on B
- **Paraphrase:** If the rota is stood up but promotion is indefinitely deferred, the review bottleneck driving attrition never resolves, and in six months the maintainers face a fresh backlog plus three demoralized candidates; hence B must follow on an explicit one-to-two-month timeline.
- **Type:** predicted consequence
- **Evidence:** The response names A-as-procrastination as the trap and binds B to a short, explicit schedule.

## V14 — Conditions that would flip the sequencing
- **Paraphrase:** Acute, demonstrable attrition driven specifically by PR latency, combined with strong external trust signals for the candidates (verifiable security-relevant track records, employer vouching, existing dual-review branch protection), would justify promoting first with scoped privileges.
- **Type:** predicted consequence
- **Evidence:** The response's flip-condition statement pairs urgency evidence with external trust evidence as the joint trigger for reversing the order.

## Not counted
- The restatement of the task in "The question" section (restatement, not a view).
- The numeric confidence line (no mechanism content beyond views above).
- "Main reason" summary (recapitulates V2, V5, V7, V8, V11).
