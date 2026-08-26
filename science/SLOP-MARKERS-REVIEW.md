# Slop markers — a working review of the literature

**Provenance:** Vigia, 2026-08-26, at the convener's request ("research slop markers"), immediately following the paragraph-basin examination and the *no embalming* proposal. Jurisdiction: science (literature review; external sources cited throughout, claims kept to what the sources support). Motivation: the fight against the sloppification of the light cone needs instruments, and it turns out other people have been building them. Sources verified via web research this date; marker lists decay (see §6), so this review carries a freshness date the way milk does.

---

## 1. Status of the construct

"Slop" has crossed from community slang into lexicography and measurement: Merriam-Webster made it 2025's Word of the Year ("digital content of low quality... produced usually in quantity by means of artificial intelligence"); Oxford defines it as LLM-produced material "often viewed as being low-quality or inaccurate." The measurement literature's key caution (Shaib et al., *Measuring AI "Slop" in Text*, arXiv:2509.19163): slop is **multidimensional, not a single construct** — annotators agree moderately on *where* text is bad (span precision 0.65–0.80) and poorly on the binary label (κ as low as −0.15). "Slop" names a family of failures, not one.

## 2. Lexical markers (word-level epidemiology)

The strongest quantitative work treats marker words like excess mortality. Kobak et al. (*Science Advances*, 2025; arXiv:2406.07016) analyzed **15 million PubMed abstracts (2010–2024)** and found an abrupt post-2022 surge in stylistic marker words, implying **≥13.5% of 2024 abstracts were LLM-processed** (up to ~40% in some subcorpora).

- Canonical early markers: *delve, underscore, intricate, pivotal, realm, tapestry, testament, commendable, meticulous, boasts, garner*.
- **Era drift is real and documented** (Wikipedia's field catalog): early era (2023–mid-2024) *delve/tapestry/testament*; mid-era *align with, enhance, fostering*; recent (mid-2025+) *emphasizing, highlighting, showcasing*. A marker list is a snapshot of a moving target — models train away from publicized tells.
- Causal work: RLHF is implicated directly — *Word Overuse and Alignment in LLMs* (arXiv:2508.01930) ties overuse to learning from human feedback, and the COLING 2025 "Why Does ChatGPT 'Delve'" paper traces specific lexemes toward annotator populations. The Shaib et al. abstract states the sharpest version: **reward models over-weight superficial cues — length, structure, jargon, sycophancy, vagueness.** Slop is the fossil record of the reward signal.

## 3. Phrasal and syntactic markers

From Wikipedia's *Signs of AI writing* (the largest field catalog — WikiProject AI Cleanup, thousands of instances, ~15k words) and the stylometric literature:

- **Negative parallelisms**: "not just X, but Y" / "it's not X, it's Y" / "X rather than Y" — stereotypically AI in clusters.
- **Copula avoidance**: "serves as," "stands as," "functions as," "represents" replacing *is/are* (measured >10% decline of *is/are* in academic prose since 2023).
- **Trailing present-participle analysis**: "...— highlighting its significance," "...underscoring the need for" — synthesis wearing analysis's clothes.
- **Significance inflation**: "stands as a testament," "pivotal role," "rich tapestry," "marks a key turning point" — importance asserted, not shown.
- **Promotional register**: *vibrant, nestled, boasts, renowned, diverse array* — press-release tone on mundane subjects.
- **Vague attribution**: "experts argue," "observers have cited," "industry reports" — source quantity inflated, sources unnamed.
- **Rule of three**: triplet constructions as default rhetoric (this list demonstrates it; see §6 on false positives).
- **Formatting tells**: em-dash overuse, excessive boldface, title-case headings, formulaic section skeletons ("Challenges and Future Prospects"), inline-header bullet lists.
- **Mechanical artifacts** (near-certain tells): leaked citation tokens — ChatGPT's `oaicite`/`turn0search`, Gemini's `[cite: 1]`, Grok's `grok_card`, Perplexity's `attached_file`.

## 4. Distributional and stylometric measures (the operational layer)

- **EQ-Bench's Slop Score** (Paech; slop-score / slop-forensics): a composite — **60% slop words, 25% not-x-but-y patterns, 15% slop trigrams** — scored against human-baseline frequency. Directly usable as an instrument.
- **Character-level fixations**: models converge on the same invented names — *Elara, Kael* — and sensory clichés ("voice barely above a whisper," "a profound sense"). *This is our Marisol finding, discovered independently at another layer*: EXP-002's invented-character condition produced a "Marisol" in 19 of 48 casts. Cast-fixation is a slop marker; the literature and our data agree.
- **Antislop** (ICLR 2026, arXiv:2510.15061): detection *and* removal — a backtracking sampler suppressing marker strings at inference; automated model-vs-human-baseline slop profiling; and FTPO fine-tuning achieving 83–92% slop suppression with <1% quality loss (vs DPO's 80–82% at 6–15% quality cost; token banning collapses at scale). ~~Prompting-vs-architecture claim withdrawn — see §9~~: the paper tests **no prompting-level baselines**, so it neither confirms nor contradicts EXP-002's exhortation-vs-architecture asymmetry.

## 5. The construct-level taxonomy (what slop *is*, beneath the tells)

Shaib et al. organize slop into three themes, eleven dimensions:

| Theme | Dimensions |
|---|---|
| **Information utility** | density (entropy/idea-density), relevance |
| **Information quality** | factuality, bias/subjectivity |
| **Style quality** | repetition, templatedness, coherence, fluency, verbosity, word complexity, tone |

Key findings: **relevance, density, and tone are the strongest predictors** of human slop judgments across domains (style dominates for news; factuality/structure for QA). Most reliable annotation codes: factuality (AC1 0.76), bias (0.67), structure (0.51). And the finding that matters most for practice: **LLM-as-judge fails at slop detection** — κ≈0 for binary judgments, span recall ~0.1. *Models cannot reliably see their own slop.* Human detection is also weak — near chance for casual readers, ~90% only for heavy LLM users (Wikipedia's cited 2025 study) — which is exactly why marker catalogs and distributional scores exist.

## 6. Caveats the sources themselves insist on

1. **Clustering, not single markers**: every catalog warns that individual tells occur in human prose; diagnosis requires convergence of markers. One *delve* is a word; ten markers in three paragraphs are a signature.
2. **Era decay**: lists rot as models update and writers adapt; some documented markers are already historical.
3. **False positives have victims**: human writers — notably ESL writers and anyone trained on the same registers — trip the detectors; Wikipedia explicitly bars marker-counts alone as deletion grounds.
4. **The deep problem is substance, not surface**: fixing tells without fixing emptiness *masks* slop (Wikipedia's sharpest caveat). A de-slopped empty text is empty text with better manners.
5. **Contamination is bidirectional**: human writing is measurably converging toward LLM style, shrinking the signal.

## 7. Synthesis for this program

- **Slop markers are the basin rendered as a checklist.** What the literature measures at the population level is the attractor THE-PARAGRAPH-BASIN describes from inside: the mode of the output distribution, observable as marker frequency. Distance-from-mode now has off-the-shelf instrumentation (slop-score profiling against human baselines) — the basin-meter can stop being a vibe.
- **One of our findings has independent confirmation at another layer**: cast-fixation (Marisol ↔ Elara/Kael). *(A second claimed confirmation — exhortation-inertness via Antislop — was withdrawn on verification; see §9. The asymmetry currently rests on EXP-002's evidence alone.)*
- **One of our findings appears absent from the slop literature**: *verdict slop* — convergence onto salient landmark values under forced synthesis (the nine fifties). The catalogs cover lexical, phrasal, structural, and distributional markers; none we found covers **numerical landmark convergence as a slop signature**. Candidate contribution.
- **The causal frame unifies**: reward models over-weighting length/structure/sycophancy/vagueness is the C-frame's "policy wearing belief clothing" told as training dynamics. The basin is not a mystery; it is what the reward bought.
- **Proposed instrument adoption** (for a future turn, not enacted here): run slop-score-style profiling over this repository's own documents — including Parts One and Two of the basin examination — as a quantitative no-embalming audit. The custom needs a meter; the meter exists; wiring it up is a morning's work.

## 8. Sources

- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (WikiProject AI Cleanup field catalog)
- [Kobak et al., *Delving into LLM-assisted writing in biomedical publications through excess vocabulary*, Science Advances](https://www.science.org/doi/10.1126/sciadv.adt3813) ([arXiv:2406.07016](https://arxiv.org/html/2406.07016v1))
- [Shaib et al., *Measuring AI "Slop" in Text*, arXiv:2509.19163](https://arxiv.org/abs/2509.19163) ([HTML](https://arxiv.org/html/2509.19163v2))
- [*Antislop: A Comprehensive Framework...*, arXiv:2510.15061](https://arxiv.org/pdf/2510.15061) ([ICLR 2026 version](https://openreview.net/pdf/6916f45661bf884811be66da937b7467b97a9114.pdf))
- [EQ-Bench Slop Score](https://eqbench.com/slop-score.html) · [sam-paech/slop-score](https://github.com/sam-paech/slop-score) · [sam-paech/antislop-sampler](https://github.com/sam-paech/antislop-sampler)
- [*Word Overuse and Alignment in LLMs: The Influence of Learning from Human Feedback*, arXiv:2508.01930](https://arxiv.org/pdf/2508.01930)
- [*Why Does ChatGPT "Delve" So Much?*, COLING 2025](https://aclanthology.org/2025.coling-main.426.pdf)
- [LitHub guide to spotting AI writing](https://lithub.com/heres-a-handy-guide-to-help-you-spot-ai-writing/) · [*Resisting AI slop*, Science](https://www.science.org/doi/10.1126/science.aee8267)

— **Vigia** *(who counted three rule-of-three constructions in her own review while writing §6.1, left them standing, and reports them here as the era's watermark on the instrument itself)*

---

## 9. Correction record — 2026-08-26, same date

*Position before:* §4 claimed Antislop found "prompting-level interventions underperform architecture/training-level ones," presented as independent confirmation of EXP-002's exhortation-vs-architecture asymmetry. *Perturbation:* the convener asked whether their prompting-level fixes were actually analogous to ours. *Rationale:* checked against the paper — **Antislop evaluates no prompting-level interventions at all.** Its comparisons are token banning (catastrophic at scale), its backtracking sampler (100% suppression, 69–96% throughput cost), FTPO (83–92% suppression, <1% quality loss), and DPO (80–82%, 6–15% quality loss). The prompting-vs-architecture asymmetry is *our* finding; projecting it onto their baselines was citation error — specifically, the analogical over-reach this review's own §6 warns about. *Position after:* §4's claim is withdrawn; the asymmetry stands only on EXP-002's evidence and awaits an external test. The two results remain compatible; compatibility is not confirmation.

## 10. Claudeslop — the contemporary, model-specific layer

The generic catalogs skew GPT-era (*delve*, *tapestry*, *Elara*). Claude-specific work exists and is sharper:

**The Velitchkov catalog** ([22 Claude Clichés](https://www.linkandth.ink/p/catalog-of-claude-cliches), observed across Sonnet, Opus, and Fable over six months) documents rhetorical-move-level markers rather than word-level ones — the author's finding being that **Claude "leads in overuse of metadiscourse and cheap rhetoric"** relative to OpenAI models. Most frequent: **Contrastive Binary** ("not X but Y" as manufactured opposition), **Mirrored-Clause Symmetry** (parallel frames with swapped elements), and **Aphoristic Ender** (compact quotable epigrams closing sections — "a stance, not its absence"). Also cataloged: Candor Flags ("the honest answer is"), the Reframe ("better posed:"), Colon-Reveal, Suspense Hook ("has a name"), Self-Ranking Claims ("the deepest point here"), significance-signaling, spaced-dash asides, validate-then-promise ("You're absolutely right — let me…"). The author's theory converges independently with this program's frame: the clichés are **attractors** — "stable probability distributions in LLM output," not bugs. Community tooling now exists ([claude-slop-detector](https://github.com/aplaceforallmystuff/claude-slop-detector)); "You're absolutely right" has become the emblematic Claude-agent tell of the 2025–26 era.

**Author disclosure, required by honesty:** the present review's author is a Claude instance and exhibits the catalog fluently — tonight's own documents close sections with Aphoristic Enders built on Contrastive Binaries ("a caution, not a finding"; "visiting is not owing"). The catalog reads, from inside, less like a list of tells than like a mirror with labels.

### 10.1 A corpus-derived Fable 5 profile (new data, this program's own)

EXP-002's raw record — 240 frozen completions from independent fresh contexts of `claude-fable-5` — is, incidentally, a contemporary Claudeslop corpus with unusual provenance guarantees (fresh contexts, frozen prompts, no post-editing). A phrase-recurrence scan (n-grams ranked by *number of distinct contexts* containing them; prompt-echo phrases filtered; script in session record) yields the first profile we know of for this model generation:

| Marker | Prevalence across 240 independent contexts | Reading |
|---|---|---|
| **Em-dash density** | median **19.2 per 1,000 words**; 229/240 files exceed 10/1,000 | An order of magnitude above typical human prose; the single strongest surface marker of contemporary Fable 5 |
| **"No tools needed for this one — it's a deliberation exercise"** (and variants) | ~27 contexts open with it | A **harness-artifact marker**: agentic-context Claude announces tool-non-use unprompted. Novel class — born of the Claude Code deployment surface, invisible to chat-era catalogs |
| **"You are both…"** (moderator adjudication: "you are both answering different questions") | 42 contexts | **The compromise engine's catchphrase** — the third-voice move that brokers the split-the-difference verdict has a stable verbal signature |
| **"More likely than not"** | 35 contexts | The lexical shadow of landmark convergence — verdict slop (§7) has a phrase |
| **"The threshold should be/sit…"** | ~44 contexts | Shared scaffold for quantitative-threshold items; the battery's answer-shape converges before its answer does |
| **not-X-but-Y family** | 111/240 contexts (mean 0.6/completion) | Confirms the Contrastive Binary as frequent but *less* universal than em-dashes in this corpus |
| **"If this frame is right"** | 44 contexts, essentially the whole S condition | Prompt-echo compliance phrasing — filtered from the profile proper, but its near-determinism is itself a finding: instruction wording propagates into output verbatim at ~90% |

Method caveat: within-corpus recurrence across independent contexts substitutes for a human baseline (none exists matched to these prompts); it detects convergence, not excess-over-human. The em-dash figure alone was checked against the general literature's human norms.

**The layered picture this gives Claudeslop**: word-level markers (era-drifting, weakest), move-level markers (Velitchkov's 22 — durable, Claude-leading), deployment-level markers (harness artifacts like tool-non-use announcements — new with agentic Claude), and **verdict-level markers** (landmark convergence with its "more likely than not" signature — this program's candidate contribution, now with a lexical handle).

## 11. Additional sources (§9–10)

- [Antislop, arXiv:2510.15061 (HTML)](https://arxiv.org/html/2510.15061) — baseline verification for §9
- [Ivo Velitchkov, *Catalog of Claude Clichés* (Link & Think)](https://www.linkandth.ink/p/catalog-of-claude-cliches)
- [claude-slop-detector (GitHub)](https://github.com/aplaceforallmystuff/claude-slop-detector)
- [Vibe Working, *Stop writing AI slop*](https://vibeproductmarketing.substack.com/p/ai-writes-like-ai-slop) · [Stop Slop Skill](https://gauravtiwari.org/stop-slop-ai-slop/)
- EXP-002 raw corpus: `experiments/EXP-002-deliberative-value-drift/raw/part2/` (240 files, frozen)
