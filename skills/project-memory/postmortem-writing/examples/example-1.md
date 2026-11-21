# Example 1 — Blame line rewritten as a system cause

## Before

## Contributing causes

Root cause: the on-call engineer restarted the wrong service. He selected the staging database instead of production during the incident and caused the data-sync outage. He has been reminded to check the service name before restarting.

## After

## Contributing causes

- The admin console listed the staging and production databases under the same display name ("orders-db"), distinguished only by a region tag in small print.
- The restart action required no confirmation and did not display which environment was about to be restarted.
- The runbook named the service by its display name rather than its unique service ID, so the on-call engineer (role) selected the staging entry during the incident.

Note: corrects PM-082 / BAN-PM-041 — the person is replaced by role, and the causes are the system properties that made the wrong selection possible.
