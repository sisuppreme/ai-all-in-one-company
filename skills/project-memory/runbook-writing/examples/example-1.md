# Example 1 — Narrative steps rewritten as actions with expected results

## Before

Runbook: "API latency high" — procedure section:

> First, look into whether the database is the bottleneck. Check the
> connection pool and resolve any exhaustion you find. You may also want to
> look at slow queries. Once things look healthier, the latency should come
> back down.

No commands, no thresholds, no expected outputs. The on-call engineer must
already know how to check the pool, what "exhaustion" looks like, and what
"healthier" means — knowledge the runbook was supposed to supply.

## After

> 1. Check pool saturation:
>    `psql -h db-primary -c "SELECT count(*) FROM pg_stat_activity;"`
>    Expected: a count below 80 (pool limit 100). If the count is 100, go to
>    step 2. If it is below 80, the database is not the bottleneck — go to
>    step 4.
> 2. Identify the blocking sessions:
>    `psql -h db-primary -c "SELECT pid, state, wait_event FROM pg_stat_activity WHERE state <> 'idle';"`
>    Expected: a short list of active sessions. Note the pid holding the
>    oldest transaction.
> 3. Terminate the blocking session from step 2:
>    `psql -h db-primary -c "SELECT pg_terminate_backend(<pid>);"`
>    Expected: returns `t`, and re-running step 1 shows the count falling
>    below 80 within 30 seconds. If it does not fall, escalate (see
>    Escalation) instead of terminating further sessions.

Every step is one action, names the exact command, states the expected
result, and branches where the output can differ.

Note: corrects PM-063 — steps are actions with expected results, not explanations.
