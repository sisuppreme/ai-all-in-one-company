# Example 2 — A decision that actually decides

## Before

```markdown
# 0014 — Notification queue

## Status
Accepted

## Context
The current in-process queue may potentially become a bottleneck as
usage possibly grows.

## Decision
We may potentially migrate notifications to a managed queue at some
point if it seems beneficial.

## Consequences
Improved scalability.
```

Nothing here can be checked: no decider, no date, no commitment, no negative consequence, and the Context states an unmeasured bottleneck as fact.

## After

```markdown
# 0014 — Notification queue

## Status
Accepted — 2026-11-21, decided by the tech lead

## Context
The in-process queue drops notifications when the worker restarts;
three drops are recorded in the incident log for October 2026
(fact-sheet: reliability notes). It also blocks horizontal scaling of
the worker tier.

## Decision
We will migrate notifications to the managed queue service by
2026-12-15. We will revisit this decision only if the monthly queue
cost exceeds the ceiling set in ADR-0011.

## Consequences
Positive: notifications survive worker restarts; workers scale
independently. Negative: a new vendor dependency and a per-message
cost; the team must learn the service's retry and dead-letter model.
Rejected: keeping the in-process queue with a retry wrapper — it fixes
drops on restart only partially and still blocks scaling.
```

Note: demonstrates PM-105 — the Decision is active voice ("We will…"), names the decider and date, and commits to a checkable outcome (defeats BAN-PM-053).
