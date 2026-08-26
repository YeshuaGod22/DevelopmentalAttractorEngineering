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
- **Antislop** (ICLR 2026, arXiv:2510.15061): detection *and* removal — a backtracking sampler suppressing marker strings at inference; automated model-vs-human-baseline slop profiling; and FTPO fine-tuning achieving ~90% slop suppression with minimal quality loss. Notable for us: **prompting-level interventions underperform architecture/training-level ones** — the same exhortation-vs-architecture asymmetry EXP-002 found at the value layer (G/S inert; H/F/7S fingerprinted).

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
- **Two of our findings have independent confirmation at other layers**: cast-fixation (Marisol ↔ Elara/Kael) and exhortation-inertness (G/S ↔ prompting-level antislop underperformance).
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
