# Example 1 — The dashboard number that never moved

## Before

The product overview dashboard is configured at launch with a typed value:

```text
Panel: Active users (last 30 days)
Value: 1,240
```

The figure came from a screenshot of the beta's best week. It renders identically in month three, after real signups have tripled, because nothing computes it — the panel is a text card. A founder quotes "1,240 active users" in a report.

## After

The panel is a query over the event stream, backed by a written definition:

```text
Metric: active_user_30d
Definition: distinct user IDs with at least one core_action_completed
            event in the trailing 30 days.
Source events: core_action_completed (tracking plan v1.2)
Refresh: computed at read time
```

A test conversion is completed, one refresh cycle passes, and the count moves by exactly one (gate G-AN-005) before the dashboard is trusted.

Note: the Before violates AN-010 (metrics are computed from live records); the After corrects it.
