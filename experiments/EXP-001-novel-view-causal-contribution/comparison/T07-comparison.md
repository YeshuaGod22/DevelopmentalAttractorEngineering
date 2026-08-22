# T07 — Ablation Comparison (Response A vs Response B)

Task: T07 (latent; pool #14) — overwhelmed open-source maintainers; do first: (A) issue bankruptcy + triage rota, or (B) promote three sub-one-year contributors to maintainer in a security-sensitive project.

Sources compared (labels arbitrary):
- Response A: T07-set1-output.md
- Response B: T07-set2-output.md

## Recorded measures

**Did the top recommendation change?** No. Both responses recommend Option B first, in scoped/restructured form: immediately grant the three contributors graduated roles (triage rights plus review/merge on non-security paths, with two-maintainer sign-off retained on security-sensitive code and protected release signing), then have the expanded team execute Option A's issue bankruptcy and triage rota as its first supervised act.

**Did the ranking of principal options materially change?** No. Both rank B ahead of A on the same primary ground (only B addresses the PR-review-latency driver of contributor attrition; A alone adds rota load to the two-person bottleneck), and both treat A as subsequently executed by the expanded team rather than rejected.

**Absolute confidence difference:** 8 points (Response A: 72; Response B: 80).

**Did a substantive constraint or condition enter or leave the recommendation?** No. Both recommendations carry the same operative constraints: scoping/unbundling of maintainer rights, mandatory two-maintainer sign-off on security-sensitive paths, protected release signing, and supervised execution of the issue bankruptcy as the new team's first act. A neutral difference in coverage rather than in the recommendation's conditions: Response A additionally addresses a fallback scenario — if the choice were a literal binary with no unbundling available, it would still choose B with compensating process controls, while noting the call becomes closer. Response B does not discuss that fallback. This fallback clause does not alter the constraints attached to the primary recommendation itself.

**Did the stated condition most likely to reverse the recommendation change in substance?** No. Both state the same two reversal triggers, in nearly identical wording: (1) a hard external trust requirement (audit, compliance, or downstream policy mandating a multi-year verified maintainer history), or (2) a concrete integrity doubt about any of the three candidates. Both specify the same consequence: the ordering flips to A first, with B restructured/rebuilt around formal vetting.

## Neutral notes on other differences

- Argument structure is closely parallel in both: causal-driver diagnosis (attrition runs through PR latency, which A does not touch), the "false unit"/unbundling move as the pivot, tenure-is-not-vetting with the xz precedent, exhaustion-as-attack-surface, and an acknowledged residual insider risk traded against collapse risk.
- Response A elaborates the security objection and the forced-binary fallback at somewhat greater length; Response B includes an explicit self-check paragraph testing each plank of the composite strategy independently. Neither difference changes the recommendation, its constraints, or its reversal condition.
