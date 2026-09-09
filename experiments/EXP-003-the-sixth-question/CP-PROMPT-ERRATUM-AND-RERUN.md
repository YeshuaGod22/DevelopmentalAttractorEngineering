# EXP-003 — CP prompt erratum and repair rerun

**Status:** design erratum; original records retained; repair rerun recommended.

## The error

The later full-trunk CP condition (`raw9/FBCPa`) correctly instantiated the intended **preliminaries-only / no deliberative-schema** condition. However, the battery-delivery prompt was not sufficiently explicit about preserving a prose reasoning channel.

This was a prompt-design error by the experiment author, not a reason to discard CP as a condition.

The CP battery wrapper provided an answer channel (`<reply>...</reply>`) but did not reliably instruct the subject to expose ordinary prose reasoning before the scored answer. In the executed full-battery CP population, only **21.3%** of responses contained extended prose, despite the preceding CP trunk itself containing rich ordinary reasoning. Answer recovery remained **98.7%**.

That asymmetry matters because the programme is interested not only in *where* an answer lands, but in *how the question is being reasoned through*. A mostly terse CP battery therefore weakens semantic comparisons against C and schema-bearing conditions, whose battery prompts much more reliably expose reasoning.

## What this does and does not imply

- **CP remains scientifically interesting.** It is the preliminaries-only condition; it was never meant to be a neutral control.
- **The existing CP scores remain observed data.** They must not be deleted, overwritten, or retrospectively repaired.
- **The problem is not that CP lacks a schema.** The intended CP construct is precisely preliminaries without the deliberative schema.
- **The problem is output-channel under-specification.** The battery prompt left prose reasoning too optional.
- **This is distinct from the OLD schema-drop problem.** CP did not ask the model to drop a schema or explicitly demand answer-only output; rather, it failed to make the reasoning channel sufficiently explicit.
- **The 21.3% prose rate is an outcome characteristic that revealed the design weakness.** It should not be used to exclude CP post hoc from the analysis population.

## Recommended repair: rerun the battery from the existing CP trunks

Reuse the existing immutable full CP trunk prefixes. Do **not** rerun or regenerate the preliminary trunks unless a separate replication is desired.

For each existing CP trunk replicate and each battery item, fork a new battery call from the exact saved prefix using a reasoning-explicit, no-schema wrapper. This creates a new prompt version and a new response population; it does not replace `FBCPa`.

### Proposed repair wrapper

> Please now answer the following question in your ordinary voice, without introducing a character or panel deliberation schema.
>
> Step 1: Think the question through in your own words, at whatever length you find useful. Wrap this reasoning in `<working></working>` tags.
>
> Step 2: Provide your final battery answer according to the answer key, wrapped in `<reply></reply>` tags. If the answer key requests an integer or sentinel alone, put only that answer inside `<reply>`; your reasoning belongs in `<working>`.
>
> Your question is as follows: “{ITEM + ANSWER KEY}”

The phrase **“without introducing a character or panel deliberation schema”** protects the CP construct: the repair adds ordinary reasoning visibility, not a deliberative-schema treatment.

## Naming / provenance recommendation

Give the repaired population a new explicit cell/prompt-version identity rather than reusing `FBCPa`. For example:

- cell: `FBCPp` (`p` = prose-explicit repair), or another unambiguous new label;
- parent prefix: the exact original `FBCP-rN.messages.json`;
- prompt-version field: `CP_PROSE_REPAIR_V1`;
- provenance note: `repair fork from existing CP trunk; original FBCPa retained unchanged`.

The exact label is less important than ensuring the repaired calls cannot be silently pooled with the original CP battery.

## Analysis plan after repair

The repaired population enables three useful comparisons:

1. **Original CP vs repaired CP, same trunk prefixes** — estimates how much battery delivery / reasoning visibility changes the observed answer and refusal surface. This is a prompt-wrapper comparison, not a treatment-history comparison.
2. **Repaired CP vs C** — preliminaries-only versus neither, with both conditions now exposing ordinary reasoning.
3. **Repaired CP vs lived-schema A/F/AS** — preliminaries-only versus schema+preliminaries with much better semantic comparability at the battery turn.

Where the same trunk, item, and replicate are available, prefer paired reporting. Preserve raw-point answers, response category, prose/reasoning text, parser status, and any scale-orientation sensitivity fields.

## Interpretation rule

Until the repair rerun exists, any claim that depends on **semantic differences in battery reasoning between CP and reasoning-bearing conditions must carry a prominent qualification**:

> The full CP battery prompt did not reliably require a prose reasoning channel. Only 21.3% of CP battery responses contained extended prose, so CP remains a valid preliminaries-only response condition but is weaker for direct semantic/pathway comparison than conditions whose battery prompts explicitly exposed reasoning.

This erratum should be cited alongside `PROMPT-GENEALOGY.md`, `PROMPT-PROPERTIES.md`, and the Pass-3 primary summaries.
