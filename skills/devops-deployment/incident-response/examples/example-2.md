# Example 2 — Mitigate first at 3 a.m.

## Before

An alert fires at 03:12. The responder opens a laptop and starts reading production logs to find the root cause, working from memory of a similar issue and commands half-remembered from a chat thread months ago. Seventy minutes later the cause is still unproven and the site is still down.

## After

The responder opens the runbook entry for the alert's symptom and runs its exact mitigation steps: `kubectl rollout undo deployment/api` restores the previous release in four minutes, and service is healthy by 03:20. Diagnosis moves to the morning, against the restored system's logs and the scribe's timeline.

Note: Demonstrates DO-285 and DO-286 — a runbook with exact commands reachable at 3 a.m., and mitigation (rollback) executed before any root-cause diagnosis.
