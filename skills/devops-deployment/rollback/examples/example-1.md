# Example 1 — Runbook rollback step written before release

## Before

Release 2.7 ships on a Friday. The runbook's rollback section reads: "Rollback plan: redeploy the previous version if something goes wrong." No command, no version identifier, no named target. When error rates spike, the operator spends 20 minutes figuring out which build was live before 2.7 and how the platform restores it — during the outage.

## After

Before 2.7 merges, the runbook entry for the release reads: "Rollback for 2.7: run `kubectl rollout undo deployment/web` (restores revision of build `ghcr.io/app/web@sha256:9f2c…`, commit `a1b2c3d`). Abort if error rate exceeds baseline +1 point for 5 minutes; on-call lead may call it." When the fault appears, the undo runs in under a minute and the drill target of 5 minutes to healthy traffic is met.

Note: demonstrates DO-301 — the exact rollback action is written in the runbook before the release ships.
