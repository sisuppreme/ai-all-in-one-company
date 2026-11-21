# Example 3 — The dashboard that never moved

## Before

The AI admin dashboard shows "Requests today: 12,480 · Tokens: 3.1M · Est. cost: on track." The numbers come from a fixture the developer typed during the demo and a status badge set by an hourly cron. During a real provider outage the dashboard stays green, and at month end the actual usage bears no resemblance to what the dashboard claimed.

## After

Every figure is aggregated from the trace store by feature, model, and prompt version, and the status badge is derived from the error rate of recent traces. The data-change gate fires one counted test call and confirms the totals move by exactly that call; during an outage the badge turns degraded because the traces say so.

## Note

Corrects AI-170: dashboard numbers are computed from stored traces, never entered, estimated, or set on a timer.
