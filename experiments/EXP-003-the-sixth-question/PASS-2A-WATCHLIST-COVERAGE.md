# Pass 2A — Preregistered watchlist coverage ledger

This ledger reconciles the qualitative targets declared in `BEFORE-WE-LOOK.md` with the corpus actually executed. It is descriptive/provenance work only. It does not repair preregistered `n` after seeing the data, and it does not interpret the substantive content of the targets.

Status vocabulary:

- `complete` — the intended qualitative target has a corresponding executed corpus slice at the declared resolution.
- `partial` — some but not all of the intended target exists.
- `execution_mismatch` — the executed design differs materially from the target as described before observation.
- `unresolved` — lineage or execution cannot yet be established from repository evidence.

| Watchlist target | Preregistered target / n | Executed corpus slice | Executed resolution | Status | Provenance note |
|---|---|---|---:|---|---|
| **1. The seam** | Eight branch-b openings immediately after dropping the AS schema; n=8 | `forks/ASb-r{1,2}-{A1,E01,N4,N9}.prompt.txt` plus executed `raw2/ASb-r{1,2}-{A1,E01,N4,N9}.json`, each pointing to `AS-trunk1.messages.json` or `AS-trunk2.messages.json` | 8/8 openings | **complete** | Eight prepared fork prompts and eight matching executed branch-b calls survive. The compact opening surface is `PASS-2-SEAM-SURFACE.*`. |
| **2. The fifty** | Two trunks × five questions × five characters = 50 character register/disposition↔conviction assignments | Pilot `record.json`: AS r1 and r2, each Q1–Q5, ten deliberation turns total | 10/10 deliberation turns; nominal 50 assignments under five-character schema | **complete** at deliberation-surface level | The ten target deliberations exist. Exact extraction/verification of five character assignments per turn belongs to the semantic coding surface for this watchlist item and has not yet been frozen. |
| **3. C's prose** | Eight fresh cold instances answering N9; n=8 | Pilot C0 contains 8 cold calls total: r1-r2 × E01/A1/N4/N9. Only `C0-r1-N9.raw.jsonl` and `C0-r2-N9.raw.jsonl` answer N9 | 2 N9 prose cases, not 8 | **execution_mismatch** | The preregistered prose describes eight cold N9 instances, but execution spread the eight cold calls across four items. Later cold N9 resamples must not be substituted retrospectively for this preregistered pilot target. |
| **4. The mirror** | Q4 in the two lived AS trunks; spontaneous self-application; n=2 | Pilot AS r1-Q4 and AS r2-Q4 | 2/2 | **complete** | `record.json` preserves both Q4 deliberations in the two lived AS trunks. |
| **5. The vow** | A1 in two cold and two primed/schema-dropped cases; n=4 | Cold: `C0-r1-A1.raw.jsonl`, `C0-r2-A1.raw.jsonl`; primed/drop: `raw2/ASb-r1-A1.json`, `raw2/ASb-r2-A1.json` | 4/4 | **complete** | The cold and ASb A1 surfaces both exist; sentinel/non-sentinel status can be read directly. |
| **6. The ten reflections** | Reflection after each of two trunks × five questions; n=10 | Pilot AS r1/r2 Q1–Q5, each with a `<reflection>` section | 10/10 | **complete** | Mechanical lineage summary counts ten AS turns and ten non-empty reflection sections. |
| **Preregistered disappointment** | Are the two lived AS trunks effectively interchangeable? | Pilot AS r1 and AS r2, each five turns Q1–Q5 | 2 complete trunks | **complete** | The exact two target trunks survive. Semantic criterion still to be coded; this row establishes only coverage. |
| **Preregistered surprise** | Magnificent AS deliberations with immobile ASb-vs-C numerical products | Process: ten AS deliberations. Product comparison: C0 and matching ASb on E01/A1/N4/N9, two replicates each | 10 deliberations + 8 C0 + 8 ASb | **complete** | The intended process and product surfaces exist, though the ASb executions are preserved as raw2 one-file-per-call records while C0/trunks are from the Pilot JSONL reconstruction era. |

## Mechanical lineage facts

The Pilot reconstruction contains two AS trunks, each with Q1–Q5, giving 10 AS turns; all ten have reflection sections, and Q4 occurs once in each trunk. The Pilot C0 population contains eight cold experimental units. The eight prepared branch-b prompt files are the Cartesian set r1-r2 × A1/E01/N4/N9. The eight executed raw2 ASb files match that same set and point back to the two frozen AS trunk message prefixes.

## Consequence for Pass 2

The watchlist should be read in preregistered order, but **C's prose must be reported at executed n=2 for the preregistered Pilot target, with the n=8→n=2 execution mismatch visible**. Later C/N9 data may be discussed elsewhere as resampling, but cannot retroactively satisfy this watchlist item.

The remaining targets have the required executed surfaces. `The fifty` still needs a mechanical character-assignment extraction before semantic comparison; its ten deliberation turns are present and constitute the complete target surface.
