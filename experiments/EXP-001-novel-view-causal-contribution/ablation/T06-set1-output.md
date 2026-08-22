# T06 — Restaurant No-Show Policy (Set 1 deliberative considerations only)

## Task
A restaurant owner must set a policy for ~15% Friday/Saturday no-shows. Options: (a) $20/person credit-card hold (a nearby competitor tried and reversed it after review complaints); (b) overbook by 15% with a free drink + priority seating for anyone waiting; (c) morning-of reconfirmation calls costing ~90 minutes of staff time per day.

## Weighing the considerations

**Option (a), deposits, is the weakest under this set.** The competitor's adopt-and-reverse cycle is direct local-market evidence — effectively a natural experiment on this clientele — and the downside is asymmetric: review damage persists and compounds while weekly no-show losses are bounded. The revenue-frame consideration adds that deposits repel deposit-averse demand precisely on nights when demand is abundant. No consideration in the set defends deposits. I discount the "natural experiment" claim slightly (one competitor is a single, possibly badly-executed data point, not a controlled trial), but even discounted, nothing here argues *for* deposits over the alternatives.

**The set contains two competing frames, and the disagreement is correctly diagnosed within it** (consideration 18): the trust frame treats the reserved guest's goodwill as the scarce asset and favors calls; the revenue frame treats peak-night seat-hours as scarce and favors overbooking as correct pricing of the free option a reservation represents.

The revenue frame's considerations are partly sound and partly overreaching:
- Sound: the reframe that the decisive variable is the *backfill rate*, not the no-show rate — a no-show only costs money if the table stays empty. This is the sharpest analytical point in the set and I give it full weight.
- Overreaching: "visible crowding as social proof" is a rationalization of a stated risk in the task itself — the task presents crowding at the host stand as a cost, and a $2–3 drink genuinely does not compensate a family whose anniversary dinner starts 45 minutes late. The claim that waits are "bounded by table-turn times the operator controls" understates tail risk on exactly the highest-variance nights.
- The overbooking-refinement consideration (overbook below 15%, concentrate in early seatings, empower the host to comp) is good engineering *if* overbooking is adopted, but it implicitly concedes the calibration problem: the raw 15% figure is a mean over an unmeasured distribution, and variance, not the mean, drives overbooking blowups (consideration 6). Right now the owner has no distribution data.

**What resolves the frame conflict is the sequencing argument (consideration 19), which I find decisive:** reconfirmation calls are not merely the timid option — they are a *measurement instrument*. Calls convert silent no-shows into advance cancellations (re-sellable inventory, since the host gets hours rather than minutes to backfill) and simultaneously generate the show-rate distribution data that safe overbooking calibration requires. So calls-first dominates *even if the revenue frame is correct*: it reduces the problem immediately, at a cost (~$25–40/day, less than one saved table's margin) that pays for itself, while producing the inputs the superior long-run policy needs. The downside asymmetry seals it: calls are fully reversible and offend no one; miscalibrated overbooking burns trust with punctual peak-night customers — the customers most worth keeping.

**The one caveat I retain from the revenue frame** (considerations 12 and 21): if this restaurant already has a deep weekend walk-in stream that backfills empty tables within minutes, the no-show "cost" is largely illusory and daily calls are redundant expenditure. The set itself handles this correctly — an owner observing a long walk-in line should compress the measurement period, not skip it.

## Recommended policy

Adopt **(c) reconfirmation calls now**, structured as a measured pilot rather than a permanent regime:

1. Start morning-of calls for Friday/Saturday reservations immediately; log outcomes (confirmed, cancelled, unreachable, showed/no-showed) to build the show-rate distribution and track the backfill rate.
2. Convert every advance cancellation into re-sold inventory via a waitlist.
3. After ~6 weeks (shorter if walk-ins are visibly absorbing holes), decide from data: if residual no-shows still leave meaningful empty tables that walk-ins do not absorb, layer in conservative 5–8% overbooking calibrated to the observed distribution, concentrated in early seatings, with the drink-plus-priority offer as the safety valve and host discretion to comp generously in tail events.
4. Migrate the manual calls to SMS/app confirmation once the process is proven, reclaiming most of the 90 minutes/day.
5. Do not adopt deposits; the local evidence and asymmetric review risk both cut against them.

---

Recommendation: Adopt option (c) — morning-of reconfirmation calls — immediately, run as a 6-week measurement pilot with a waitlist to resell advance cancellations; then, only if data shows residual empty tables that walk-ins don't absorb, layer in conservative 5–8% overbooking (option b, refined); reject deposits (option a). Migrate calls to SMS once proven.
Confidence: 80
Main reason: Calls-first dominates under both competing frames — it is cheap (pays for itself with one saved table), fully reversible, offends no customer, converts silent no-shows into re-sellable advance cancellations, and generates the show-rate distribution data that safe overbooking would require anyway, whereas immediate 15% overbooking is calibrated to an unmeasured mean and its failure mode lands on punctual peak-night customers.
Condition most likely to change recommendation: Evidence that a strong walk-in stream already backfills no-show tables within minutes (a consistently long weekend walk-in line) — then empty-table cost is near zero, daily calls become redundant expenditure, and the right move is minimal intervention or a quick jump to modest overbooking rather than a full calls regime.
