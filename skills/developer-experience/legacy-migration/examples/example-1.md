# Example 1 — The one-release rewrite plan

## Before

```markdown
## Migration plan: replace monolith checkout

1. Freeze checkout changes from 1 Dec.
2. Rewrite checkout as a service (est. 4 weeks).
3. Switch all checkout traffic to the new service in the 5 Jan release.
4. Delete the old checkout code in the same release.
```

The whole capability moves in one step: no seam, no per-step rollback, and the old code is deleted in the same release that first exposes the new one to production. Any defect in the new service on 5 Jan is an outage with a rewrite as the only way back.

## After

```markdown
## Migration plan: replace monolith checkout (Strangler Fig)

Seam: edge router rule `checkout/*`, deployed first with 100% of traffic
still routed to the monolith (rollback for every step: flip the rule back).

| Slice | Seam route | Rollback | Data point of no return |
|---|---|---|---|
| Cart totals | `checkout/totals` | route flip | none (read-only) |
| Payment capture | `checkout/pay` | route flip | backup of `payments` table before dual-write starts |
| Order confirmation | `checkout/confirm` | route flip | none |

Coexistence ends: 28 Feb release. The monolith checkout code is deleted in
its own change after each slice's soak period, never at cutover.
```

Each slice migrates behind the router independently, each flip reverses with the same rule, and elimination is scheduled separately against a stated end date.

## Note

Corrected under DX-121: a migration plan names its slices, the seam for each, and the rollback for each step — a plan that is one big step is rejected.
