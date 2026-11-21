# Example 2 — The secondary-metric rescue

## Before

A signup-form test (EXP-009) ran its full registered period. The primary metric — form completion rate — finished flat: +0.3%, confidence interval crossing zero on both sides. Rather than record a loss, the team pointed to a secondary metric, average time on page, which was up 22%, declared the experiment a success in the growth review, and shipped the variant. The next quarter's planning cited EXP-009 as evidence that "longer forms engage better", a claim the experiment never tested.

## After

At the horizon, the register entry for EXP-009 is completed exactly as the data dictates: SRM passed; primary metric +0.3% (95% CI −1.8% to +2.4%); decision — kill, the variant does not ship. The time-on-page observation is not deleted; it is written into the hypothesis backlog as a new question ("Does the added explainer step increase informed completions among returning visitors?") and, when prioritized, registered as its own experiment with that measure as its primary metric. The growth review reports EXP-009 as a recorded loss with a usable learning, and no later document cites it as a win.

Note: corrects CO-264 (the primary metric decides; secondary metrics generate hypotheses, they never overturn the result) and CO-269 (every concluded experiment leaves a complete register entry, losers included).
