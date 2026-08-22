# R16 — View Extraction (Task T07)

Task: Overwhelmed two-maintainer open-source project; Option A = issue bankruptcy + triage rota; Option B = promote three sub-one-year contributors to maintainer in a security-sensitive project. Which first?

Response recommendation: Option B first, in a permission-scoped form; Option A a few weeks later staffed by the enlarged team.

## Extracted views

- **V1**
  - Paraphrase: Contributor attrition is driven by PR review latency (a throughput problem), so the true causal bottleneck is review capacity, not the issue backlog.
  - Type: causal mechanism
  - Evidence: The response identifies six-week review time as the stated cause of contributors leaving and frames it as two maintainers being unable to review fast enough.

- **V2**
  - Paraphrase: The 400 issues are an accumulated stock problem with weaker attrition effects than PRs: an ignored issue is shrugged off, but an ignored PR represents contributed work and drives the contributor to quit.
  - Type: stakeholder-impact
  - Evidence: The response contrasts the contributor whose issue is ignored (shrugs) with the contributor whose PR is ignored (quits), distinguishing backlog noise from the attrition mechanism.

- **V3**
  - Paraphrase: Issue bankruptcy performed by the current team would backfire: it adds a standing triage-rota obligation to the two people who are already the constraint, and the mass-close triggers a wave of reopen requests and community friction the project has no capacity to absorb.
  - Type: predicted consequence
  - Evidence: The response argues Option A does nothing for throughput while adding rota load and reopen traffic at the moment of least capacity.

- **V4**
  - Paraphrase: Without a change in processing capacity, closed issues that get reopened simply flow back into the unchanged pipeline and the backlog re-accumulates.
  - Type: causal mechanism
  - Evidence: The response states that issues reopened into an unchanged pipeline just re-accumulate, making bankruptcy alone a temporary fix.

- **V5**
  - Paraphrase: Option B has inherent lead time (permission design, onboarding, norm-setting), which is an independent reason to start it first regardless of other considerations.
  - Type: strategy
  - Evidence: The response notes promotion is the option with lead time, so if it will happen at all it should be started first.

- **V6**
  - Paraphrase: Sequencing B before A creates a synergy: the three new maintainers can staff the triage rota and absorb the reopen wave, converting bankruptcy from a two-person cleanup spasm into routine, sustainable hygiene.
  - Type: strategy
  - Evidence: The response's recommendation is to do A a few weeks after B, explicitly staffed by the enlarged five-person team.

- **V7**
  - Paraphrase: The security objection is real (patient sock-puppet supply-chain attacks are documented, citing the xz/liblzma case), but tenure is a weak screen for it, since the canonical attacker had more than a year of contribution history.
  - Type: normative criterion
  - Evidence: The response takes the under-a-year concern seriously while noting the xz perpetrator's longer history undercuts tenure as the safeguard.

- **V8**
  - Paraphrase: Remaining at two maintainers is itself a security risk in security-sensitive use, via low bus factor, review fatigue, and rubber-stamping under load.
  - Type: causal mechanism
  - Evidence: The response argues a two-person project in security-sensitive environments is itself a security risk, so "never add maintainers" is not the mitigation.

- **V9**
  - Paraphrase: The correct mitigation is scoped, graduated trust: grant the new maintainers triage and review rights only, withholding release/signing keys, security-advisory access, force-push, and CI-secret access.
  - Type: jurisdiction
  - Evidence: The response specifies exactly which decision rights the new maintainers get and which stay with the founders.

- **V10**
  - Paraphrase: Branch protection requiring at least one founding-maintainer approval on protected (or security-sensitive) branches lets new maintainers accelerate review without ever becoming a sole gate.
  - Type: constraint
  - Evidence: The response prescribes a merge rule keeping a founder in the approval path for protected branches.

- **V11**
  - Paraphrase: Labor should be divided by trust level: new maintainers clear the easy majority of the PR queue and run triage, while the founders' attention concentrates where their trust is irreplaceable.
  - Type: strategy
  - Evidence: The response has new maintainers handling the easy 80% of PRs and triage so founder attention is reserved for security-critical review.

- **V12**
  - Paraphrase: Under the scoped structure, the marginal security risk of promotion is roughly the risk the project already accepts by merging these contributors' PRs at all, while the throughput gain is immediate.
  - Type: normative criterion
  - Evidence: The response argues scoped promotion adds little beyond the existing exposure from accepting their code contributions.

- **V13**
  - Paraphrase: The recommendation is conditional on permission tiering being possible: if maintainer status necessarily grants full release/signing/CI-secret access with no branch-protection backstop, the ordering flips — do A first as the safe pressure release and use the bought time to build a slower vetting path for B.
  - Type: predicted consequence
  - Evidence: The response's stated condition-most-likely-to-change is the platform's inability to scope permissions, which reverses the sequencing.
