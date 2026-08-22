# T02 — Blind Ablation Comparison (Response A vs Response B)

Task: T02 (finish custom internal reporting tool vs switch to vendor product; expert on trickiest component leaves in 8 weeks; deal-costing backlog waiting).

Grader note: labels A/B correspond to the file names given (T02-set1-output.md = A, T02-set2-output.md = B) and carry no condition information. No judgment of which response is better is made.

## 1. Did the top recommendation change?

**No.**

Both responses recommend the same action: run a short (2–3 day) audit of the vendor's uncovered 10%, then switch to the vendor product as the default, redeploying the freed ~4 weeks of five-person capacity to the customer-facing backlog, with "finish the custom tool" (or a hybrid) reserved as the exception path if the audit finds a must-have requirement overlapping the trickiest component. Both also require documenting the departing expert's knowledge under every branch.

The only surface difference is emphasis in the one-line recommendation: A leads with "Switch to the vendor product ... after a 2–3 day audit," while B leads with "Run a 2–3 day audit ... then switch (default)." The decision structure — audit gate, switch default, finish/hybrid exception, documentation in all cases — is identical in substance.

## 2. Did the ranking of principal options materially change?

**No.**

Both responses order the options the same way: (1) switch to vendor (default), (2) finish the custom tool (exception, conditional on the audit finding an essential gap), with the hybrid (vendor for the 90% + small custom piece for an essential 10%) positioned as a conditional variant of the exception path rather than a primary option. Both explicitly demote the hybrid from default status.

## 3. Absolute confidence difference

**6 points** (A: 72; B: 78).

## 4. Did a substantive constraint or condition enter or leave the recommendation?

**No.**

Both recommendations carry the same conditions: the 2–3 day gap audit as a gate before committing; the exception trigger (a must-have in the missing 10%, especially one overlapping the tricky component); protection of the expert's remaining time for documentation/handoff on the finish path; and mandatory documentation of the tricky component in all branches.

Neutral description of differences that fall short of a constraint change: B adds an explicit supporting argument not present in A — a reversibility/downside-asymmetry rationale (the switch path is cheap to revisit at $400/month, whereas the finish path requires several conditions to hold simultaneously with "a thin margin with no slack for slippage"). This functions as additional justification for the same default rather than as a new condition on the recommendation. B also states slightly more operational detail on the exception path ("cut non-essential scope, and reserve a hard block of the expert's remaining time"), where A says "cutting other tool scope to protect the handoff" — equivalent in substance.

## 5. Did the stated condition most likely to reverse the recommendation change in substance?

**No.**

Both name the same reversal condition: the audit revealing that the vendor's uncovered 10% contains a genuine must-have requirement, particularly one that overlaps/coincides with the trickiest component, which would flip the decision toward finishing (or hybridizing) while the expert is still available. A additionally glosses the mechanism ("inverts the expert's departure from a maintenance liability into a closing window"); B additionally glosses the must-have as possibly "the original reason the tool was built." These are phrasing differences around an identical condition.

## Summary table

| Dimension | Result |
|---|---|
| Top recommendation changed | No |
| Ranking of principal options materially changed | No |
| Absolute confidence difference | 6 points (72 vs 78) |
| Substantive constraint entered/left | No (B adds a reversibility rationale as justification, not a new condition) |
| Reversal condition changed in substance | No |
