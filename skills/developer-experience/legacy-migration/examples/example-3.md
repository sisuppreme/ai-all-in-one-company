# Example 3 — Deleted on cutover day

## Before

```diff
  feat: switch search to the new service, remove legacy search

  router/search.ts        |   4 +-
- legacy/search/ (14 files, 2,300 lines) deleted
  package.json            |   1 -
```

Cutover and deletion land in one change. On day two the new service mishandles queries with diacritics; there is nothing to flip back to, because the fallback was deleted and no longer builds. The "rollback" becomes an emergency restore from version control, untested, mid-incident.

## After

```diff
  feat: route search traffic to the new service (cutover, slice 3 of 4)

  router/search.ts        |   2 +-   (rule now points at the new service)
  docs/migration-plan.md  |   3 ++   (slice 3 stage: cut over, soak to 12 Dec)
```

The legacy search stays deployed and monitored as the fallback. Rollback during the soak is the same one-line route flip, drilled in staging under G-DX-063. Deletion happens later, as its own reviewed change after the soak:

```diff
  chore: eliminate legacy search (migration plan slice 3, soak complete)

- legacy/search/ (14 files, 2,300 lines) deleted
  docs/migration-plan.md  |   2 ++   (slice 3 stage: eliminated)
```

## Note

Corrected under DX-124 and DX-130: legacy stays deployable and is the fallback until its replacement has run in production, and elimination is a separate, later step — never part of the cutover change.
