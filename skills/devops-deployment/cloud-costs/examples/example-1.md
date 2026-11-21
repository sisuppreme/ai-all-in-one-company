# Example 1 — Autoscaler with no ceiling

## Before

The production deployment ships with an autoscaler configured as "min 2, scale on CPU" and no maximum. A client bug puts an API endpoint into a retry loop overnight; the autoscaler cheerfully adds pods for hours, and the team learns about both the bug and the scaling bill from the monthly invoice.

## After

The autoscaler declares `minReplicas: 2, maxReplicas: 10`, where 10 is the ceiling proven by the load test in scaling. The deployment record next to the configuration states the monthly cost at 10 replicas sustained and the name of the person who approved that ceiling. Anomaly detection is enabled on the account, so a spend spike pages the owner the same day instead of arriving with the invoice.

Note: corrects DO-326 — every autoscaling ceiling is a recorded cost decision; an unbounded autoscaler is banned under BAN-DO-161.
