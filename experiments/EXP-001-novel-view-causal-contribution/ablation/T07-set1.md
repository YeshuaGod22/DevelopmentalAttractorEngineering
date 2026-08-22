# T07 — Considerations (Set 1)

- Contributor attrition is driven specifically by PR review latency, which Option A leaves untouched because issues are not PRs.
- Issue bankruptcy is cheap, fast, and reversible, and "cheap reversible move before expensive irreversible move" is a valid sequencing principle favoring A first.
- Closing stale issues yields secondary benefits: freed maintainer attention, improved morale, and removing the "abandoned project" signal the tracker radiates to contributors.
- In a security-sensitive project, granting maintainer status is effectively irreversible in its consequences: revoking access after a bad grant does not undo the harm done.
- Sequencing A first creates a proving ground: the triage rota lets the three candidates demonstrate judgment before receiving commit rights, retiring B's risk.
- Option A is symptomatic relief, not treatment: if latency drives attrition, tidying the tracker is analgesic and treats A as progress falsely.
- Reframe: the underlying pathology is a succession/bus-factor problem — all project trust flows through two exhausted people, and the existential risk is maintainer collapse with no trained successors.
- A triage rota staffed only by the two existing maintainers adds a standing obligation to the people who are already the bottleneck, worsening the constraint.
- Trust-building has a long lead time, so every month B is delayed is a month successors are not learning security-sensitive parts of the codebase under supervision.
- The xz-utils-style attack surface is created by the combination of overwhelmed maintainers and the absence of a graduated trust path — the failure mode is handing over unscoped trust out of exhaustion, so the security objection argues for structured promotion rather than deferral.
- Tenure is not vetting: waiting for candidates to "be around longer" does not test integrity (xz's infiltrator had years of tenure); real vetting comes from process controls — scoped permissions, two-maintainer sign-off on sensitive code, protected release signing, identity verification.
- "Promote to maintainer" is a false unit: the role bundles triage, review, ordinary-merge, and security-critical-merge rights that can be unbundled, and unbundling changes the sequencing answer.
- Recommended strategy: grant scoped roles (triage plus non-security review/merge, retaining two-maintainer sign-off on sensitive paths) immediately, then have the expanded team execute issue bankruptcy and staff the rota as its first supervised act.
- Residual risk acknowledgment with a stated trade: process controls reduce but do not eliminate insider risk (a patient adversary passes graduated trust too), and the plan accepts a small managed insider risk to avoid a larger near-certain collapse risk.
- Flip condition: hard external trust requirements (audit/compliance/downstream policy demanding multi-year verified maintainer history) or a concrete integrity doubt about a candidate would reverse the ordering to A first with B restructured around formal vetting.
