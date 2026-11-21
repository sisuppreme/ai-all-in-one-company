# Example 3 — The 200 ms claim with no trace behind it

## Before

A review comment states: "The product endpoint averages about 200 ms; the slowness users report must be the network." No trace, percentile, or window is cited — the figure is a memory of one fast local run. Acting on it, the team spends a week on CDN configuration. Field complaints continue, because the endpoint's production p95 is several seconds, and almost all of it is one unindexed database query that a single staging trace would have shown in the span breakdown.

## After

The claim is restated from evidence or withdrawn: the endpoint's per-service view shows duration at p50/p95/p99 over the last 7 days, and the slow traces behind the p95 — reachable through the chart's exemplars — decompose the duration into application time and a database child span that dominates it. The optimization work goes to the query, and its effect is verified against the same percentile view. The rule for the next review is the skill's anchor: a latency claim without a trace behind it is an opinion.

Note: corrects AN-188 — latency claims name their trace evidence and percentile window; database time is its own span (AN-190).
