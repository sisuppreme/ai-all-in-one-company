# Example 3 — Unbounded staleness replaced by a tolerance and a fallback

## Before

The price list reads from the replica with no tolerance and no lag monitoring. During a traffic spike, lag reaches four minutes and customers are quoted prices that changed minutes ago:

```text
price_list -> replica   tolerance: (none stated)
lag metric: (none)      alert threshold: (none)
Observed staleness during spike: ~4 minutes, discovered via complaints
```

## After

The read declares its tolerance, lag is a monitored metric, and crossing the threshold reroutes the read to the primary automatically:

```text
price_list -> replica   tolerance: 30 s
lag metric: pg_stat_replication replay_lag, scraped every 10 s
alert threshold: 20 s (warn), 30 s (fallback engages)

Fallback rule (in the data-access layer):
  if replay_lag > 30 s: route price_list to primary
  until lag < 10 s for 5 consecutive checks.
Verified by the fallback drill (G-DB-113) with replay paused in staging.
```

**Corrects DB-224, DB-226** — every replica read states its staleness tolerance, and excess lag triggers a declared fallback instead of silent staleness.
