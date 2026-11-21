# Example 2 — The alert that posted to a dead channel

## Before

```yaml
receivers:
  - name: team-alerts
    slack_configs:
      - channel: "#eng-alerts"   # archived last quarter; nobody is a member
```

The error-rate alert fires correctly and is read by no one. The outage is discovered from user complaints two hours later. There is no named owner and no escalation if the channel stays silent.

## After

```yaml
route:
  receiver: pagerduty-oncall        # current rotation, owned by D6 mechanics
  group_by: [service]
  repeat_interval: 4h
receivers:
  - name: pagerduty-oncall
    pagerduty_configs:
      - service_key: <routing-key>  # deduplicates and escalates per policy

# Alert payload (excerpt)
annotations:
  summary: "API error budget burning at >6x over 6h"
  impact: "Elevated 5xx on all API reads and writes"
  runbook: "https://repo.example/runbooks/api-errors.md"
  dashboard: "https://grafana.example/d/api-golden-signals"
labels: { severity: page, owner: "api-team" }
```

Receipt is proven, not assumed: the G-AN-062 fire drill fires this alert in staging and times its arrival at the on-call channel.

Note: corrects AN-128 — pages route through the alert manager to the current on-call with deduplication and a complete payload, instead of a channel nobody watches.
