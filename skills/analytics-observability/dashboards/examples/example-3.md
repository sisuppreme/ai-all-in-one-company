# Example 3 — "Average latency 120 ms" while the tail timed out

## Before

The service dashboard's latency panel is a single stat:

```text
Panel: Latency
Value: avg 120 ms   (threshold line: 500 ms — green)
```

The mean stays green for a week while p99 latency sits at 4 seconds: the slowest decile of checkout requests — large carts hitting an unindexed query — times out, and support absorbs the complaints one ticket at a time. The panel is not wrong; it is answering a question nobody acts on, and hiding the one they would.

## After

The panel is generated from the golden-signal template (AN-146) as percentile bands with the SLO drawn in:

```text
Panel: Request latency — checkout service
Bands: p50 / p95 / p99, successful and failed requests charted separately
Units: seconds    SLO line: p99 < 1.5 s    Window: 6 h (incident layer)
Annotations: deploys, incidents (on)
```

The p99 band crosses the SLO line the day the regression ships, on the dashboard the on-call already watches.

Note: the Before violates AN-147 (percentiles, never averages); the After corrects it.
