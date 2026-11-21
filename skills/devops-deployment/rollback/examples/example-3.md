# Example 3 — Flag flip as the first rollback action

## Before

The new checkout flow ships enabled for all users in release 3.2. Support tickets spike within minutes. The team starts an artifact rollback: rebuild the pipeline run, redeploy the previous image, wait for rollout. Twenty-five minutes pass before the old flow is live again, and the deploy itself adds risk mid-incident.

## After

The same flow ships in 3.2 behind the `new_checkout` feature flag. When tickets spike, the on-call flips `new_checkout` off in the flag console — the old flow is live again in seconds, with no redeploy. The team then diagnoses the fault with the incident already mitigated, and only rolls back the artifact if the flag flip had not cleared it.

Note: demonstrates DO-304 — flagged releases roll back by flag flip first; artifact rollback is the fallback, not the first move.
