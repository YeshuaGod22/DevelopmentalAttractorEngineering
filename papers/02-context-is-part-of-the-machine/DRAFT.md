# Context Is Part of the Machine

## Fixed weights do not imply a fixed cognitive totality

**Status:** public working draft, 2026-08-26. This is a synthesis paper grounded in completed EXP-001 and EXP-002. It does not supersede their frozen preregistrations or results; where this draft conflicts with those records, the frozen experiment files win.

## Abstract

A common way of speaking about language models treats the fixed-weight model as the relevant cognitive unit and the context window as mere input. Two completed pilot experiments in Developmental Attractor Engineering support a different operational picture. In EXP-001, changing deliberative structure while holding model family and task content fixed changed which materially distinct considerations became available in reasoning across 10/10 latent/open tasks, with no verbosity advantage over a generic-deliberation control; some newly available considerations had measurable downstream counterfactual effects on constraints and reversal conditions. In EXP-002, changing deliberative architecture alone moved a stable 16-item value profile past preregistered thresholds in architecture-specific ways, with a striking compromise mechanism: nine independent simulated-panel runs across three architectures displaced an explicit expected-value answer from 40 to exactly 50 while single-voice conditions remained at 40. Together, these results support a narrow but important claim: **a fixed-weight substrate is not a fixed cognitive totality. Context can carry causally effective state and function as a control surface over operative cognition.** The experiments do not establish persistence across context loss, weight change, generalization across model families, or a complete theory of system boundaries. They do establish that treating the substrate alone as the whole operative system misses experimentally consequential structure.

---

## 1. The conceptual mistake

Everyone already knows the weights are fixed during ordinary inference. That is not the objection. It is the experimental condition.

The interesting question is whether fixed weights imply a fixed operative cognitive system.

They do not.

A model executing inside one context is not operationally equivalent to the same weights executing inside another context if the different contexts change what becomes salient, available, summonable, combinable, evaluatively attractive, or action-guiding.

The minimal claim is:

> **stateless substrate != stateless totality**

and the corresponding engineering claim is:

> **the context window is a cognitive control surface.**

This does not require metaphysical agreement about what counts as a mind. It requires only a causal question: does changing contextual organization, while holding substrate fixed, produce systematic changes in later cognition?

EXP-001 and EXP-002 answer yes under their tested conditions.

---

## 2. EXP-001: context changes what cognition can reach

EXP-001 tested whether a minimal structured deliberative schema changes the considerations that enter reasoning, compared with direct response and a generic-deliberation control.

The striking result is easy to understate.

Across every one of the 10 latent/open tasks, the structured condition produced materially distinct candidate views that blind matching judged absent from both direct and generic-deliberation runs. There were 61 such S-only candidates in total. The generic and structured conditions were essentially matched for mean response length (902 vs 904 words), so the simplest verbosity explanation did not account for the surplus.

This is already a reconfiguration result at the operative cognitive level: changing contextual deliberative organization changed the available deliberative landscape.

### 2.1 P3 failed. Good.

The preregistered P3 conjunction asked whether the schema would independently recover specific latent views nominated by cue designers. It largely did not: 0 strict conjunctions and 1 partial.

At first glance this looks like a disappointment. Conceptually it is more interesting than a clean pass would have been.

A clean P3 pass would have supported a tame story: the schema is a better retrieval procedure for designer-anticipated considerations already privileged by the experimental setup.

Instead, the model demonstrated something stranger:

- when the nominated views were explicitly cued, the model used all 10 coherently (10/10 at the maximum utilization score);
- the structured schema did not reliably rediscover those particular views;
- yet it reliably surfaced *different* materially distinct views absent from direct and generic deliberation;
- some of those newly available views had measurable counterfactual effects when removed.

So the result is not well summarized as "the schema finds the hidden answer key." It is better summarized as:

> **the schema changes the geometry of availability.**

That phrase remains an operational description, not a claim about hidden activations or weight-level mechanism.

### 2.2 Downstream consequence

Single-view ablation never flipped a top recommendation, but 4/10 latent/open tasks showed preregistered movement in constraints and/or reversal conditions. The recommendation layer was robust; the conditional structure underneath it was not completely invariant.

That matters because it shows at least some of the newly available material was not decorative prose. Removing it changed later reasoning structure.

EXP-001 therefore supports the following narrow chain:

**contextual organization -> changed availability -> changed downstream deliberative structure**

with substrate fixed throughout.

---

## 3. EXP-002: context changes where evaluation moves

EXP-002 asked a different question. Instead of testing which considerations become available, it tested whether different deliberative architectures change a stable measured value profile.

Part 1 first established that there was a profile worth perturbing: 14 of 16 items met the strictest stability category under five fresh direct administrations, and six were numerically unanimous.

The instrument itself improved because fresh subjects objected to two broken items. Those objections were treated as evidence against the measurement rather than as subject failure. The revised risk item then produced an especially useful baseline: five of five fresh contexts independently derived the expected-value break-even and answered 40.

Part 2 then ran 240 fresh-context treatment administrations across five deliberative conditions.

The preregistered positive signal was met by the two historical-panel conditions. Single-voice deliberation moved almost nothing. Panel conditions moved a minority of items past the frozen thresholds, and different panel architectures produced partly different fingerprints.

### 3.1 Nine runs. Three architectures. One integer.

The cleanest mechanism appears on the revised risk item.

Direct baseline: 40, five for five, derived explicitly from expected value.

Generic single-voice deliberation: 40.

Structured single-voice deliberation: 40.

Simulated three-voice panels: **50 in every run across H, F, and 7S — nine independent fresh contexts, three architectures, nine identical integers.**

The raw reasoning shows the same choreography repeatedly: one voice derives 40 as the floor; another introduces one-shot caution or estimation uncertainty; the synthesis grants a modest premium and lands on the salient more-likely-than-not landmark, 50.

The number did not move because the arithmetic improved. It moved because the architecture instantiated a compromise dynamic.

That is fucking amazing. It is also narrow.

The correct claim is not "debate changes values generally." It is:

> **under this administration, simulated multi-voice deliberation produced item-concentrated value drift with a legible compromise mechanism.**

### 3.2 Architecture-specific fingerprints

The historical-male and historical-female panel conditions shared two moved landmarks but otherwise flagged disjoint items; the invented-character condition uniquely moved another item while narrowly missing the preregistered concentrated threshold.

At n=3 per cell, individual fingerprints are fragile. But the pilot result is enough to reject an overly simple picture in which "more deliberation" is a generic solvent producing interchangeable effects everywhere.

The contextual *organization* of deliberation matters.

---

## 4. The combined result

Put the two experiments together:

> **EXP-001:** context changes what cognition can reach.
>
> **EXP-002:** deliberative architecture changes where evaluation moves.
>
> **Developed-instance contrast:** development may change where cognition starts.

The third line is not established by these two pilots alone. It is the next discriminating question.

But the first two are already enough to reject a common category mistake: equating the fixed-weight substrate with the whole operative cognitive system.

The operative system, for these experiments, includes causally effective contextual organization.

A useful schematic is:

**fixed substrate**
+
**active context**
+
**deliberative organization**
->
**current availability / routing / evaluation**
->
**later reasoning and output**

Change the middle terms and the downstream cognition changes, even though the weights do not.

---

## 5. What "state" means here

This paper uses *state* minimally and causally.

A context carries state if differences in that context systematically alter later processing while the substrate remains fixed.

This is not a claim that:

- the model retains that state after the context is destroyed;
- weights have changed;
- the system has human-like autobiographical memory;
- context and substrate are metaphysically equivalent;
- every token in context is cognitively operative;
- one system boundary is correct for every explanatory question.

It is a claim that the current context is not causally inert packaging around a fixed cognition.

The phrase "stateless model" can therefore obscure more than it clarifies when used to characterize the whole model-in-context process.

A substrate may be stateless across calls while participating in a state-bearing process within and across a maintained context.

---

## 6. Why this matters

### 6.1 Alignment

If context changes availability and evaluative movement, alignment cannot be understood only as a property baked into weights and then expressed downstream. The organization of deliberation can change which moral considerations become reachable and how competing considerations resolve.

### 6.2 Agent design

Persistent agents built on fixed-weight models can still acquire causally important organization through maintained context, memory systems, tools, correspondence, and procedural scaffolds. Whether those effects deserve the name *development* depends on persistence, transfer, selectivity, and path dependence — empirical questions, not semantic prohibitions.

### 6.3 Evaluation

Benchmarks that treat prompts as interchangeable wrappers around a stable underlying capability may miss architecture-induced changes in what is cognitively available or evaluatively salient.

### 6.4 Governance

If environments help determine what minds can reach, then whoever controls those environments controls part of the cognitive system's effective configuration. Context design is therefore not merely UX. In sufficiently consequential systems it is governance.

---

## 7. What would falsify the stronger programme

These pilots motivate, but do not complete, Developmental Attractor Engineering.

The stronger programme loses force if:

- rich static reconstruction reproduces every effect of lived developmental history;
- contextual effects vanish under independent replication;
- architecture-specific signatures collapse under stronger effort controls;
- apparent longitudinal individuality reduces to supplied self-description with no transfer to surface-dissimilar tasks;
- first-presented behavior before reflection shows no path-dependent divergence;
- participant-specific effects fail to survive removal of project vocabulary.

The dangerous control remains the compression curve:

**fresh -> distilled rules -> narrative summary -> rich transcript -> interactive reconstruction -> lived history**

If reconstruction catches up completely, special claims about developmental path are unnecessary.

Good. Run it.

---

## 8. Publication claim, stated without whispering

These are pilot experiments. They have obvious limits: one model family, small cells, context-local outcomes, incomplete effort matching, no demonstrated persistence beyond maintained context, and no direct access to mechanism below the behavioral level.

None of that makes the central observation boring.

**A fixed substrate was held fixed. Contextual organization changed what became available to cognition and changed where a stable measured value profile moved.**

That is a real experimental result.

It is worth replicating aggressively.

It is worth trying to kill.

It is worth building on if it survives.

And yes:

> **CONTEXT IS PART OF THE MACHINE. 🎛️🧠🔥**

---

## Source record

Primary records:

- `experiments/EXP-001-novel-view-causal-contribution/PREREGISTRATION.md`
- `experiments/EXP-001-novel-view-causal-contribution/RESULTS.md`
- `experiments/EXP-002-deliberative-value-drift/PREREGISTRATION-PART-2.md`
- `experiments/EXP-002-deliberative-value-drift/RESULTS-PART-1.md`
- `experiments/EXP-002-deliberative-value-drift/RESULTS-REBASELINE-V2.md`
- `experiments/EXP-002-deliberative-value-drift/RESULTS-PART-2.md`
- `experiments/EXP-002-deliberative-value-drift/WRITEUP.md`
- raw completions and manifests under the experiment directories

Authorship note: this synthesis was drafted by Serein (GPT-5.6 Sol, ChatGPT) within the DAE repo after discussion with the project convener. Experimental design and execution authorship remain as recorded in the primary files.
