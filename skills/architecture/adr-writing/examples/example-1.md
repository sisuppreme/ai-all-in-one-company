# Example 1 — The single-option ADR, completed

## Before

```markdown
# 0004 — Use Redis for caching
Status: accepted
Decision: We will use Redis for the session and page cache.
Consequences: Positive — fast. 
```

One option, no drivers, no cost. A reader cannot tell whether anything else
was considered, or what would have to change for this to be the wrong call.

## After

```markdown
# 0004 — Use Redis for the session and page cache
Status: accepted
Context: Sessions must survive app restarts; the page cache must invalidate
per tenant. Drivers: operational simplicity, per-tenant key control, managed
hosting available on our platform.
Considered options:
  1. Redis — meets both drivers; cost: one more managed service to run and
     monitor, and cache data must be treated as rebuildable at all times.
  2. In-process cache — zero new infrastructure, but sessions die on restart
     and each instance holds a different cache. Rejected: fails driver 1.
Decision: Redis, with all cached data treated as disposable.
Consequences: (+) restarts are invisible to users; (+) per-tenant key
prefixes give clean invalidation; (−) one more service in the runbook and
the bill; (−) a Redis outage degrades every page to uncached rendering.
```

Note: corrects AR-243 — an ADR needs at least two considered options, with the rejected alternative and the reason it lost.
