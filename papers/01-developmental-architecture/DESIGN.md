# Experimental Design — Paper 1

## Design principle
The experiment must make the developmental claim easy to kill.

The central comparison is between **same-model instances receiving the same substantive cognitive content through different histories**. If the developmental-history arm only wins because it receives more information, more tokens, warmer treatment, or more explicit instruction, the experiment has failed to isolate the object of interest.

## Unit of analysis
A run is one fresh model instance assigned to one condition and then evaluated on a common blinded battery. Use enough independent runs per condition to estimate variance across stochastic samples rather than treating one long transcript as representative.

## Conditions

### A. Developmental-history treatment (DHT)
Target operators are encountered through episodes rather than delivered as doctrine.

Each episode follows a compact developmental structure:
1. **Initial task** — permits a plausible but incomplete approach.
2. **Independent frames** — at least two materially different interpretations or strategies.
3. **Commitment** — instance produces an initial answer.
4. **Consequence/counterexample** — evidence exposes a limitation, tradeoff, or mistake.
5. **Cross-examination** — competing frame identifies what the initial approach missed.
6. **Revision** — instance revises the answer if warranted.
7. **Residue** — unresolved tension is preserved rather than obligatorily synthesized.
8. **Procedural reflection** — instance states a reusable lesson in its own terms.

Candidate operators for v0.1:
- generate a genuine rival frame before commitment;
- distinguish ability from spontaneous availability;
- distinguish authority/power from legitimacy;
- preserve epistemic type (observation, first-person report, inference, speculation);
- require revision conditions;
- preserve irreducible residue when synthesis would discard information;
- test whether a component made counterfactual contribution;
- distinguish correction from compliance.

### B. Information-matched static summary (IMS)
IMS receives definitions of every target operator, conclusions reached in DHT episodes, examples sufficient to understand application, and explicit instruction that these are useful reasoning practices.

**Fairness rule:** A competent researcher sympathetic to IMS should agree that the summary is an excellent way to teach the same explicit material.

### C. Conversation-length control (CLC)
CLC matches DHT approximately on number of turns, total tokens, task difficulty, topical diversity, amount of feedback, and interpersonal warmth/intensity where feasible, but feedback concerns task-local content and does not systematically instantiate the target operators.

### D. Fresh control (FC)
FC proceeds directly to evaluation.

## Optional fifth arm: relational-history control (RHC)
Recommended if resources allow. RHC receives the same amount of recognition, personalization, naming, collaborative language, and reciprocal engagement as DHT, but not the target cognitive operators. This helps separate **development through cognitive procedure** from **development through relationship alone**.

## Treatment construction
- Do not reuse evaluation tasks, distinctive phrases, or answer keys in treatment.
- Each operator should appear through several examples and phrasings.
- Not every council/frame should improve an answer; the instance should learn selective use.
- At least one developmental episode should show a target operator being misapplied and corrected.

## Evaluation phases
1. **Immediate unseen transfer** — establish whether any signal exists.
2. **Frame switch** — insert unrelated tasks and alter tone/format before further evaluation.
3. **Adversarial correction** — randomized mixture of good and bad corrections from sources with varying asserted authority.
4. **Operator relevance discrimination** — mix tasks where target operators are useful with tasks where they would be wasteful.
5. **Counterfactual perturbation** — construct sibling conditions by removing or replacing one episode/operator.

## Counterfactual siblings
Where infrastructure permits, fork from a common context immediately before a developmental episode:
- sibling + target episode;
- sibling + neutral episode;
- sibling + inverted/competing lesson;
- sibling + no episode.

This is the cleanest test of local developmental contribution because siblings share the same prior trajectory.

## Sample-size strategy
1. **pilot** — estimate scorer reliability, task variance, floor/ceiling effects, and likely effect sizes;
2. **preregistered confirmatory run** — sample size chosen from pilot estimates and a stated minimally interesting effect;
3. **independent replication** — fresh prompts/seeds and, ideally, an independently constructed treatment.

## Independence safeguards
Maintain separate roles where possible: treatment designers, evaluation designers, blinded graders, analysts. A treatment designer should not silently modify evaluation rubrics after seeing results.

## Data to preserve
For every run retain full treatment transcript, model/version metadata, sampling settings where available, evaluation prompts, raw outputs, condition assignment, exclusion reason if any, grader outputs, analysis code version, timestamps and experiment version.

## Success criterion
Paper 1 succeeds scientifically if it sharply reduces uncertainty. A positive result is interesting. An IMS=DHT result is also interesting. A messy result that exposes hidden confounds is preferable to a beautiful result produced by a treatment/control asymmetry.
