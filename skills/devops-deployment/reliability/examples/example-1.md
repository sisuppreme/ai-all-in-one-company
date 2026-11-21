# Example 1 — An SLO that can gate a release

## Before

```markdown
## Reliability goals

We aim for high availability and fast responses. Uptime should be
as close to 100% as possible; if users complain a lot, we will
slow down releases for a while.
```

There is no SLI, no target, and no window, so nothing can be measured and the release "slowdown" depends on whoever complains loudest.

## After

```markdown
## checkout-api — SLO

- **SLI:** successful requests / total requests over a rolling
  30-day window, measured by the `checkout_requests_total` and
  `checkout_requests_failed_total` counters (5xx and timeouts
  count as failures; 4xx client errors do not).
- **Target:** 99.9% — error budget 0.1% ≈ 43 minutes of full
  outage equivalent per 30 days.
- **Budget policy:** remaining budget is shown on the team board.
  Budget exhausted → feature releases pause, reliability work
  takes priority, until the window recovers (DO-262).
```

The SLI is a query, the budget is a number, and the consequence of spending it is decided in advance.

Note: Demonstrates DO-261 and DO-262 — a written SLO with a measurable SLI, and an error budget that gates release pace.
