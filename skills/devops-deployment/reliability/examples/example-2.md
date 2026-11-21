# Example 2 — A burn-rate alert with a runbook

## Before

```yaml
# alerts.yml — pages on a cause, with no action attached
- alert: HighCPU
  expr: node_cpu_seconds_total > 80
  for: 5m
  labels:
    severity: page
```

CPU crosses 80% on every deploy and most load spikes; the page names no symptom, no user impact, and no runbook, so the on-call learns to ignore it.

## After

```yaml
# alerts.yml — pages on error-budget burn, with a runbook
- alert: CheckoutFastBurn
  expr: |
    (1 - (sum(rate(checkout_requests_success_total[1h]))
          / sum(rate(checkout_requests_total[1h])))) > 0.144
  for: 5m
  labels:
    severity: page
  annotations:
    summary: "checkout-api is burning its 30-day error budget
      14.4x too fast (1h window) — budget gone in ~2 days
      at this rate"
    runbook_url: "https://example.internal/runbooks/checkout-burn"
```

The alert fires on the symptom users feel — the SLO burning down — at the SRE Workbook's fast-burn threshold, and the annotation links the exact runbook section. Rule files pass `promtool check rules` in CI (G-DO-132).

Note: Demonstrates DO-264 and DO-265 — burn-rate alerting against the SLO, and every paging alert actionable with a runbook link.
