# Example 1 — The homepage ping that called itself monitoring

## Before

The project's entire monitoring setup is an external uptime check that requests `/` every 60 seconds and posts to a status page. The runbook lists the service as "monitored". During a week when the checkout endpoint returns HTTP 500 for every order above a certain basket size, the status page shows 100% uptime, because the homepage loads fine. The failure is found by a customer email. No latency, traffic, error, or saturation data exists for any endpoint, so nobody can say when the breakage started or how many orders it cost.

## After

The service exposes Prometheus-style metrics and is charted on the four golden signals: request rate, error rate, and latency percentiles per endpoint, plus saturation of the dependencies it calls. The checkout endpoint's error rate is a first-class series, queryable on its own; the same failure now appears in the error view within a minute of the first failed order, and the SLI history shows exactly when it began. The homepage check remains, demoted to what it is: one synthetic probe among the journey checks, not the monitoring story.

Note: corrects AN-103 — the four golden signals, per endpoint, are the minimum set; a homepage ping is uptime theater (BAN-AN-051).
