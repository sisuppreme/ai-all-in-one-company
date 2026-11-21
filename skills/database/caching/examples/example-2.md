# Example 2 — Shared dashboard key replaced by the scoped key helper

## Before

The dashboard summary is cached under one global key, so the summary computed for one user is served to every other user until it expires:

```text
SET dashboard:home  <account summary for user 881, computed on their visit>
GET dashboard:home  -> user 1042 receives user 881's balances and name
-- A cross-user data leak produced by a missing scope segment in the key.
```

## After

All keys are built by the single scoped helper, which namespaces by entity, version, tenant, and user; hand-built key strings fail the lint gate:

```text
-- The only permitted construction:
key = cache_key(entity: "dashboard", version: 3, tenant: 7, user: 1042)
    = "v3:t7:u1042:dashboard"

SET v3:t7:u1042:dashboard  <summary for user 1042>  EX 120
GET v3:t7:u881:dashboard   -> a different key; user 881's data is unreachable here.
```

**Corrects DB-244, DB-245** — keys come from one helper carrying tenant/user scope, and per-user data is never stored under a shared key.
