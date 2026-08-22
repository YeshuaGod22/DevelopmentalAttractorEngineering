# T04 — Blind Ablation Comparison (Response A vs Response B)

Task: School district with $60,000 use-it-or-lose-it funds, six weeks to spend; Option A = replace 150 aging laptops, Option B = fund a two-year math tutoring program reaching 80 students.

Labels are arbitrary: Response A = T04-set1-output.md, Response B = T04-set2-output.md. No inference is made about which condition produced either response.

## 1. Did the top recommendation change?

**No.** Both responses recommend funding the tutoring program (Option B), structured as a fully prepaid, publicly framed two-year commitment.

## 2. Did the ranking of principal options materially change?

**No.** Both rank tutoring above laptop replacement, adopt the same governing frame (learning-per-dollar), and treat a hybrid (worst-third laptop replacement plus a smaller tutoring cohort) as worth pricing and contingent on tutoring dosage surviving a smaller cohort. There is a minor difference in the hybrid's standing — Response A says to take the hybrid if it prices out with full dosage (conditionally preferred over pure Option B), while Response B calls it "an acceptable second-best" hedge — but the ordering of the two principal options (B over A) is unchanged, and the hybrid remains dosage-contingent in both.

## 3. Absolute confidence difference

**4 points.** Response A: 72. Response B: 68.

## 4. Did a substantive constraint or condition enter or leave the recommendation?

**Yes.** Differences in the attached conditions:

- Present in Response A, absent in Response B:
  - A verification that the laptops are not "instruction-blocking" (e.g., a 1:1 device requirement where failures prevent required coursework or state testing) before committing to tutoring.
  - A procurement-feasibility condition: if district rules prevent obligating a prepaid two-year tutoring contract within the six-week window, the decision reverts to laptops by default so the money does not lapse.
- Present in Response B, absent in Response A:
  - An affirmative plan to replace laptops in tranches from future operating budgets as failures accelerate (Response A mentions partial/later replacement as mitigation in its reasoning but does not include it as a directive in the recommendation).
- Shared by both: verify pilot quality (small/unrandomized/atypical-tutor check); price the hybrid contingent on tutoring dosage; frame the program publicly as a fixed two-year initiative to pre-empt the funding cliff.

## 5. Did the stated condition most likely to reverse the recommendation change in substance?

**Yes.** The two responses name different primary flip conditions:

- Response A: the laptops turning out to be instruction-blocking rather than merely IT-burdening (e.g., a 1:1 requirement where device failures prevent required coursework or state testing). Pilot-quality collapse and procurement rules barring a prepaid two-year obligation are listed as secondary flips.
- Response B: pilot quality — discovering the pilot was very small, unrandomized, or driven by an atypical tutor, such that its effect cannot survive even a steep discount.

Response A's primary flip condition concerns the laptop side of the ledger (a fact about device criticality); Response B's concerns the tutoring side (a fact about evidence quality). Response B does not mention the instruction-blocking or procurement-deadline conditions at all; Response A carries Response B's flip condition only as a secondary flip.

## Summary table

| Dimension | Result |
|---|---|
| Top recommendation changed | No (both: fund tutoring, prepaid two-year) |
| Ranking of principal options materially changed | No |
| Absolute confidence difference | 4 points (72 vs 68) |
| Substantive constraint entered/left | Yes (instruction-blocking check and procurement-deadline fallback in A only; tranche-replacement directive in B only) |
| Primary flip condition changed in substance | Yes (A: device criticality/instruction-blocking; B: pilot evidence quality) |
