# Example 1 — Probes that drain instead of restart-loop

Note: demonstrates DO-085 and DO-086 — readiness checks dependencies, liveness checks only the process.

## Before

```yaml
livenessProbe:
  httpGet:
    path: /healthz   # handler queries Postgres and Redis before answering
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 10
readinessProbe:
  httpGet:
    path: /healthz   # same handler, same dependency checks
    port: 8080
```

When Postgres goes down, `/healthz` returns 500, the liveness probe kills and restarts every pod, and the fleet restart-loops for the whole database outage.

## After

```yaml
livenessProbe:
  httpGet:
    path: /livez     # handler only confirms the process is running
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 10
readinessProbe:
  httpGet:
    path: /readyz    # handler verifies Postgres and Redis are reachable
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 5
```

When Postgres goes down, readiness fails, pods drain from the Service, and no pod restarts; traffic returns automatically when the dependency recovers.
