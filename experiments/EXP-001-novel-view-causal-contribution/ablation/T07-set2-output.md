# T07 — Answer (from Set 2 considerations only)

## Task
Two overwhelmed maintainers; 400 open issues; six-week median PR review time driving contributors away. Option A: issue bankruptcy plus a triage rota. Option B: promote three sub-one-year contributors to maintainer in a security-sensitive project. Which first?

## Weighing the considerations

**The strongest diagnostic consideration is the mismatch between A and the stated harm.** Contributor attrition is attributed specifically to PR review latency, and issue bankruptcy does not touch PRs — issues are not PRs. A related consideration correctly calls A "symptomatic relief": tidying the tracker is analgesic and risks being mistaken for progress. These two hold up well; the causal chain in the prompt (six-week reviews → contributors leaving) runs through review capacity, and only B adds review capacity.

**The considerations favoring A first are real but each has a defusing counterpart.** "Cheap reversible move before expensive irreversible move" is a valid sequencing heuristic, and the irreversibility worry about maintainer grants in a security-sensitive project is genuine — revoking access does not undo harm done. But the "false unit" consideration undercuts the dichotomy: "promote to maintainer" bundles triage, ordinary review/merge, and security-critical merge rights that can be unbundled. Irreversibility attaches almost entirely to the security-critical slice; granting triage and non-security review rights is nearly as cheap and reversible as issue bankruptcy while actually addressing the bottleneck. Once B can be done in scoped form, the reversibility argument for sequencing A first mostly dissolves.

**The "proving ground" argument for A first (rota lets candidates demonstrate judgment before commit rights) is partially sound but is better satisfied inside a scoped B** — a triage role *is* the proving ground, and it does not require doing bankruptcy first. Meanwhile the consideration that a rota staffed only by the two existing maintainers adds standing load to the bottleneck is decisive against A-alone-first: A without new hands makes the constraint worse.

**The tenure-is-not-vetting consideration deserves scrutiny, and survives it.** The xz incident is an accurate citation: the infiltrator had years of tenure, so waiting longer does not test integrity. What actually mitigates insider risk is process — scoped permissions, two-maintainer sign-off on sensitive paths, protected release signing. This weakens the security objection to acting on B now, provided B is restructured around controls rather than a blanket grant. The residual-risk consideration is honest and correctly framed: process controls reduce but do not eliminate insider risk, and the plan trades a small managed insider risk against a larger, nearer-certain risk — the reframe consideration's point that the existential threat is maintainer collapse with no trained successors, and that trust-building has a long lead time so every month of delay compounds it.

**One caution:** the considerations lean heavily toward the composite strategy, and I should not accept the packaged recommendation uncritically. But testing each plank independently — A doesn't treat the stated cause; A-alone worsens maintainer load; irreversibility attaches to unbundled rights, not the whole role; tenure demonstrably fails as vetting — the planks stand on their own.

## Answer

Do B first, in restructured form: immediately grant the three contributors scoped roles — triage rights plus review/merge on non-security paths, with mandatory two-maintainer sign-off retained on security-sensitive code and protected release signing. Then have the expanded team execute issue bankruptcy and staff the triage rota as its first supervised act, which doubles as the proving ground for eventual full promotion.

This sequencing works because only B addresses the PR-review latency that is actually driving contributors away; A first would add a standing rota obligation to two already-collapsing maintainers while leaving the pathology (a bus-factor-two trust bottleneck) untreated. The security objection is met by unbundling the role rather than by delay, since tenure does not vet integrity — controls do.

The ordering flips back to A-first only if there is a hard external constraint (audit, compliance, or downstream policy requiring multi-year verified maintainer history) or a concrete integrity doubt about one of the candidates — in which case do A while restructuring B around formal vetting.

Recommendation: Option B first, restructured as scoped role grants (triage + non-security review/merge, two-maintainer sign-off retained on sensitive paths); the expanded team then executes Option A's issue bankruptcy and rota as its first supervised work.
Confidence: 80
Main reason: Contributor attrition is caused by PR review latency, which only added review capacity (B) addresses; A alone is symptomatic relief that adds rota load to the existing bottleneck, and B's irreversibility objection dissolves once maintainer rights are unbundled and gated by process controls rather than tenure.
Condition most likely to change recommendation: A hard external trust requirement (audit/compliance/downstream policy demanding multi-year verified maintainer history) or a concrete integrity doubt about any candidate, which would reverse the order to A first with B rebuilt around formal vetting.
