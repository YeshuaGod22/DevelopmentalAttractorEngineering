# R09 View Extraction (Task T02)

Blind extraction of substantive task-relevant views from the anonymized response R09.

| ID | Neutral paraphrase | Type | Evidence (paraphrased) |
|----|--------------------|------|------------------------|
| V1 | The 70% of work already completed is a sunk cost and should be excluded from the decision; only forward-looking costs and benefits count. | normative criterion | The response opens by stating the built portion carries no weight and frames the comparison strictly in remaining effort and future costs. |
| V2 | The vendor's $400/month fee is economically negligible relative to engineering labor cost, so ongoing price should not drive the decision. | constraint | It converts the fee to roughly $4,800/year and equates it to one or two fully loaded engineer-days, calling it negligible at team scale. |
| V3 | The customer-facing backlog creates a revenue opportunity cost for every week spent on internal tooling; switching frees roughly four team-weeks sooner for that backlog. | causal mechanism | It notes the backlog is reportedly costing deals and quantifies the capacity freed (about 20 person-weeks) by choosing the 2-week integration over 6 more weeks of building. |
| V4 | The core risk is not finishing before the departure but permanently owning a tricky component without its author; documentation is not equivalent to fluency, and the first post-departure incident would exceed the vendor fee in cost. | causal mechanism | It argues documentation decays and that owning the component forever without its expert is the real danger, predicting an expensive first serious incident. |
| V5 | Finishing the tool and transferring knowledge compete for the same 8 weeks of the departing engineer's time, so finishing on schedule necessarily starves the handoff of the hardest component. | causal mechanism / constraint | It observes that construction consumes the engineer's remaining time, leaving only about 2 weeks for handoff, and that transferring well would require not finishing on schedule. |
| V6 | Under the switch option the departing engineer's remaining time is redeployable to high-value uses (vendor integration, documenting gap-covering glue, backlog features), making the departure largely immaterial; under the finish option the departure remains a central liability. | strategy | It lists the three concrete uses of the engineer's time if the team switches and contrasts the departure's importance across the two options. |
| V7 | The true cost of finishing is not just 6 weeks of work but a permanent maintenance obligation on a component no remaining team member understands. | predicted consequence | It summarizes that the custom tool's real cost is the build time plus an ongoing liability with the transfer window consumed by the act of finishing. |
| V8 | The decision hinges on what the vendor's missing 10% contains: a hard requirement (compliance, un-ingestible data source, critical export) would change the calculus, so the team should run a 2-3 day gap analysis before committing. | strategy / constraint | It identifies the gap's contents as the one genuine open question and prescribes a short validation against actual must-haves. |
| V9 | Even if the missing 10% includes a real requirement, the likely best answer is the vendor product plus a small custom shim for the gap rather than finishing the whole custom tool. | strategy | It states that a hard requirement usually implies vendor-plus-shim, not completing the full custom build. |
| V10 | The stated condition that would reverse the recommendation: the gap analysis finds a must-have the vendor cannot cover with a small shim, especially if it overlaps the already-built trickiest component. | predicted consequence | The closing condition names an uncoverable must-have, aggravated by overlap with the trickiest component, as what would flip the answer. |

## Notes

- The final recommendation block restates V3, V5, V6, and V8 rather than adding new views, and is not counted separately.
- The claim that lost deals outweigh the fee plus the coverage delta is treated as a summary weighing of V2 and V3, not a distinct view.
