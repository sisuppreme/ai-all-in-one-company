# Example 1 — The revenue panel that read the same number for a quarter

## Before

The product overview carries a text panel added during the launch sprint:

```text
Panel: Revenue today
Value: $4,820
```

The number was the first day's real total, typed in so the dashboard "looked complete" for a demo. Nothing recomputes it. In week ten the founder quotes "$4,820 a day" from the overview while actual daily revenue has fallen to a third of that; the panel never disagreed.

## After

The panel is a query over live order records, with its definition and cadence on the panel:

```text
Panel: Revenue today
Query: sum(orders.total) where orders.status = 'paid'
       and orders.created_at >= start_of_day(local)
Definition: revenue-analytics "recognized revenue, daily" (metrics doc)
Refresh: aggregated every 15 minutes; panel labeled "15-min aggregate"
```

Before the dashboard ships, the data-change test (G-AN-071) completes one test order, waits one 15-minute cycle, and confirms the figure rises by exactly that order's total, then falls back when the order is removed.

Note: the Before violates AN-144 (computed from live records only); the After corrects it.
