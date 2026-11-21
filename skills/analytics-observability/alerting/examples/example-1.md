# Example 1 — The CPU page that fired on every deploy

## Before

```yaml
- alert: HighCPU
  expr: node_cpu_seconds_total > 80
  for: 1m
  labels: { severity: page }
  annotations: { summary: "CPU is high" }
```

The pager fires on every deploy and every batch job, and is acknowledged on reflex. Meanwhile no alert exists on the checkout error rate, so an afternoon of 500s pages nobody.

## After

```yaml
# Page: symptom — checkout SLO (99.9% / 30d) burn rate, Workbook parameters
- alert: CheckoutErrorBudgetFastBurn
  expr: |
    (1 - checkout_success_ratio[1h]) > (14.4 * 0.001)
    and (1 - checkout_success_ratio[5m]) > (14.4 * 0.001)
  labels: { severity: page, owner: "payments-team" }
  annotations:
    summary: "Checkout error budget burning at >14.4x (2% of 30d budget in 1h)"
    impact: "Users are failing checkout at an elevated rate"
    runbook: "https://repo.example/runbooks/checkout-errors.md"
    dashboard: "https://grafana.example/d/checkout-golden-signals"

# Ticket: cause — CPU saturation is investigated in working hours
- alert: HostCPUSustained
  expr: node_cpu_saturation > 0.8
  for: 30m
  labels: { severity: ticket, owner: "platform-team" }
```

Note: corrects AN-122 — paging moves from the cause (CPU) to the symptom (SLO burn rate, derived per AN-123); the cause is demoted to a ticket.
