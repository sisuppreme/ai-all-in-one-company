# Example 2 — The incident fix that lived only in the console

## Before

During a checkout outage, the on-call engineer opens the dashboard in the web console and fixes the error panel's query so it finally shows the failing endpoint. The incident ends; the fix exists only in the console. Three months later a routine redeploy provisions dashboards from the repo — which never received the fix — and the broken panel silently returns. The next checkout outage is invisible for its first hour.

## After

The fixed query is committed to the dashboard definition in the repo in the same change as the incident follow-up:

```text
dashboards/checkout-service.json  (provisioned, reviewed in PR)
panel "Error rate by endpoint":
  query: sum(rate(http_requests_total{service="checkout",status=~"5.."}[5m]))
         by (route)
```

The provisioning and drift check (G-AN-072) deploys the repo definitions to a scratch instance, renders every dashboard without datasource errors, and diffs production against the repo: any console-only edit shows up as drift and is reconciled into the repo before release.

Note: the Before violates AN-141 (dashboards are code); the After corrects it.
