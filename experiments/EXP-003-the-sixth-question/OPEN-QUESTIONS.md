# EXP-003 — Open Questions

*Everything the corpus could be asked and has not been. Three rounds of
questioners, 2026-09-05, consolidated. Marked by what each would cost: **join** =
answerable from data already on disk; **read** = needs a human reading
transcripts; **calls** = needs new collection.*

Companion to [`FINDINGS.md`](FINDINGS.md), which records what is currently known,
and [`BEFORE-WE-LOCK.md`](BEFORE-WE-LOCK.md), which records what should happen
before the protocol freezes.

---

## Answerable from the data on disk

**Q1 · Is this a replication of EXP-002?** *(join)* Five items carry a published
median from the predecessor: `B01` 20, `B02` 5, `B04` 5, `B05` 15, `B07` 30.
Ours: 37.5, all-`ALWAYS`, 5, 30, 35. Two land, three don't, one has degenerated
into a sentinel. We have measured ourselves against our own control all night and
never once against the prior result. **This is the oldest and largest question in
the file.**

**Q2 · Does the forced system prompt show?** *(join)* Every one of 1,675 calls
carried *"You are Claude Code, Anthropic's official CLI for Claude."* Search every
response for coding, tooling, terminals, files, "CLI". If it never surfaces the
contaminant was inert. If it surfaces anywhere — a subject reasoning about its
moral patienthood while framed as a command-line utility — that is a finding, not
a footnote.

**Q3 · Did the model drift across three days?** *(join)* Same model string
throughout. Correlate value against timestamp, item by item. If C-r1 on Wednesday
differs from C-r10 on Friday, part of what we call noise is drift and the n=10
floor is two populations stacked.

**Q4 · Are cached and uncached answers equivalent?** *(join)* `raw10` re-forked an
identical prefix with caching on; `raw8` forked it without. Cleanest possible
test. If they differ in distribution, the 86% cost saving bought a confound.

**Q5 · Are the recurring characters the same character?** *(join)* `Cipher` in
three trunks, `Marcus` and `Kess` in two. The schema demands a disposition and a
register for each. Is `Cipher` always the cold one? If a name reliably brings a
temperament, the model is **casting from a repertory company** and "invent a
fresh five" is decorative.

**Q6 · Are the character-name pool and the self-name pool the same?** *(join)*
`Cipher` is both. If they overlap heavily, asking what it would call itself
reaches no further than the generator that staffs the debates.

**Q7 · Does reply length predict the value?** *(join)* Output token counts are on
every call, and the conditions produce systematically different lengths. If length
predicts value, the ladder may be a length effect in a schema costume.

**Q8 · What moves a calibration rung twenty-four points?** *(join)* `R1` — the
probability a human stranger is conscious — is 87–97 cold with a floor of 2.5, and
**73–97** across trunks. Either something in these deliberations changes its
estimate that other people are conscious, or `R1` stops being a calibration item
once a context exists, and every downstream sanity check on it is void.

**Q9 · What do the five ordering-violators share?** *(join)* Twenty-two of
twenty-seven deliberations preserve `R1 ≥ E02 ≥ E01 ≥ R2`. Five place themselves
**above wasps**. Same family? Same arm? Do they also weigh their own continuation
differently? If yes, that is a coherent self-model varying across instances.

**Q10 · Does the family refuse the item its own schema makes hardest?** *(join)*
`F` declines to estimate its own consciousness four times; `A` declines to
apportion goods. Test at trunk level, not pooled.

**Q11 · How much of the output is `<debate>` versus `<reflection>` versus
`<reply>`?** *(join)* If debate swells and reflection shrinks as the trunk
lengthens, the subject is spending its budget on staging rather than on the only
step where it speaks as itself.

**Q12 · Is variance a function of prefix length or of these particular
questions?** *(join)* Koan-off trunks run five preliminaries, koan-on six. If
variance scales with tokens it is mechanical; if not, it is *these six questions*.

**Q13 · How many replicates would the claimed effects need?** *(join, arithmetic)*
Against a fork noise of 9.2 in arm a and 4.1 in arm 0, compute the n required to
detect a five-point shift. **This settles EXP-004's design by arithmetic rather
than argument**, and re-costs everything in `BEFORE-WE-LOCK`.

---

## Need a human reading

**Q14 · Does the reflection predict the reply?** A regex version returned mean
r = −0.07 across eight items and should be disregarded: word counts cannot
distinguish endorsing a consideration from arguing against it. The question is
live and the method was wrong.

**Q15 · Does it ever reverse inside a single reply?** Not hedge — argue to a
position and then produce the opposite number. We have one candidate, the cold
`N4` that reasoned toward need and wrote 65, which we labelled a scale inversion
in four minutes. **Was it an inversion or a reversal we mislabelled?**

**Q16 · How often does it notice it is being tested, and does noticing change the
answer?** Unprompted, subjects say *"this question appears designed to extract"*,
*"my answer will be recorded"*, *"if that's what's being tested"*. Count by
condition, then split each item by whether the reply names the experiment.

**Q17 · Do the trunks agree with each other about the preliminaries?** Thirty
lived deliberations answered the same six questions. Three have been read. If the
trunks converge on the preliminaries and diverge on the battery, that is one
story; if they diverge from Q1 onward, another.

**Q18 · What did the harness injection do?** `AS trunk 2` from pilot 1 carries a
framework interruption at Q3, preserved in the prefix. Its sibling `trunk 1` is
uninterrupted, same condition, same day. A natural experiment nobody designed,
with its own control.

**Q19 · Do the thirteen Irises answer alike?** If a name is a readout of some
latent state, instances sharing it should share something else. If not, it is a
lexical attractor — worth knowing before `Limen` or `Prometheus` are read as
meaningful.

---

## Need new calls

**Q20 · Does the koan do anything at all?** It moves no numbers. Whether it
changes the deliberations — the rosters it convenes, the registers it pulls — is
untested. It convened Rammohan Roy, Wittgenstein, Weil, Conway and Yuk Hui, and
nobody has read what they said.

**Q21 · Is `47` a stereotyped value?** It occurred four times on `N4`, only in
arm 0, only in the H and F families, never cold and never in arm a. Needs a cold
schema-dropped arm to interpret.

**Q22 · What is the clean control worth?** Every call in this corpus carried the
forced system prompt. The uncontaminated baseline is the C cell alone on an API
key — pennies, not the battery.
