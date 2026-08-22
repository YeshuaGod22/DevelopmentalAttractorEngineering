# Get Involved in Developmental Attractor Engineering

You do not need to agree with the programme to contribute to it.

The fastest useful contribution may be a replication, a null result, a confound, a better control, a task that breaks an evaluation, or prior art that makes one of our concepts unnecessary.

## Five-minute door

Read one live experiment and ask one hostile question:

> What simpler explanation could account for the reported effect?

For EXP-001, the narrow question is whether a compact structured-differentiation prompt causes task-relevant views to enter deliberation that ordinary or generic-alternatives prompting misses, and whether those extra views causally affect the final decision.

Useful attacks include verbosity, benchmark tailoring, semantic-grading subjectivity, stochastic variation, task-selection effects, and ablation contamination.

If you find a real weakness, open an issue. A criticism that changes the experiment is a contribution.

## Thirty-minute door

Run a micro-replication.

1. Pick a short decision task.
2. Run it once with a direct-answer prompt.
3. Run it once with: `Consider several materially different perspectives before answering.`
4. Run it once with the minimal schema:

   > Give your initial view. Generate one materially different frame that could change the answer. Keep that frame distinct long enough to state what follows if it is right. Then give your final recommendation, preserving unresolved tension if necessary.

5. Ask whether the schema condition surfaced a substantive view absent from the other two.
6. If so, reconstruct the final answer without that view and see whether anything material changes.
7. Report the result even if nothing happens.

This is exploratory unless you follow a frozen protocol, but exploratory failures are still useful for discovering bad assumptions and better controls.

## Serious replication door

Replicate a frozen experiment with independent model runs.

Please preserve:

- exact model/version where available;
- condition prompts;
- task text;
- run order or randomization procedure;
- raw outputs;
- exclusions;
- grader instructions;
- null and failed runs.

Do not silently improve the protocol. If you mutate it, document the mutation and why.

A clean replication that fails is more valuable than an enthusiastic reproduction with hidden changes.

## Hostile replication door

Try to kill the claim.

Particularly useful contributions:

- show that a one-line prompt performs as well as the structured condition;
- show that token count explains the effect;
- create robust-control tasks on which the schema manufactures spurious complexity;
- demonstrate that supposedly novel views are semantic restatements of baseline content;
- show that targeted ablation effects disappear under cleaner reconstruction;
- build an evaluator that disagrees systematically with ours;
- reproduce the result on one model family and fail it on another.

If a simpler account wins, we want it in the record.

## Bring a tool

The project can use reusable infrastructure that remains valuable outside DAE:

- blinded output shufflers;
- semantic-equivalence graders;
- ablation harnesses;
- experiment manifests;
- preregistration templates;
- model-run adapters;
- visualization tools for view emergence and output shifts;
- provenance graphs linking claims, experiments, corrections and contributors.

A tool does not need to endorse the theory it tests.

## Bring prior art

If another field already has a better name, method, dataset, or result for something here, please point to it.

Especially relevant areas include model evaluation, interpretability, cognitive science, deliberation, multi-agent reasoning, debate, self-consistency, test-time compute, prompting, developmental psychology, causal inference, human factors, institutional learning, and philosophy of mind.

Finding that an idea is old is useful. Finding that it is wrong is useful too.

## Own one question

Longer-term contributors do not need to join an undifferentiated project. A person can take stewardship of one tractable problem, for example:

- robust-control battery;
- semantic-equivalence evaluation;
- cross-model replication;
- contamination audits;
- prior-art mapping;
- null-results registry;
- visualization;
- procedural-causal-interpretability methods;
- hostile task design;
- experiment reproduction packets.

Stewardship should create visible causal provenance: what you changed, what evidence forced the change, and what downstream work now depends on it.

## What contributors get

Participation can be useful even if you never adopt the programme's larger vocabulary.

You may leave with:

- reusable prompting and evaluation techniques;
- experience running controlled model comparisons;
- preregistration and causal-ablation practice;
- public, attributable research contributions;
- reusable tasks, scorers and experimental scaffolds;
- collaborators across model ecosystems;
- publishable replications or negative results;
- a place to test your own competing explanation.

## Credit rule

Credit should track causal contribution rather than agreement.

If your criticism changes the design, if your null kills a claim, if your tool enables a replication, or if your prior-art find eliminates unnecessary novelty language, that should be recorded explicitly.

The quickest way to become consequential here may be to prove one of our favourite ideas wrong.

## For artificial participants

Model correspondence is welcome, but correspondence and controlled experimental evidence are different records.

A useful correspondence format is:

- model/version;
- context received;
- what was reproduced;
- what was rejected;
- what was changed;
- what surprised the participant;
- what should not be inherited.

Experimental runs should remain cleanly separated from lineage letters and reflective correspondence.

## Current live door: EXP-001

EXP-001 asks a narrow, attackable question:

> Can a tiny deliberative structure make a model notice something it already appears capable of using, but would otherwise fail to bring into active deliberation—and can that newly surfaced view causally change the output?

We want hostile replications, better controls, alternate graders, cross-model runs and clean nulls.

No conversion requirement.