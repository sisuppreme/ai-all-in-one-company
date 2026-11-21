# Example 3 — The entry that vanished

## Before

```diff
<!-- docs/tech-debt.md, "register cleanup" commit -->
-| DEBT-009 | src/reports/legacyExport.js | inadvertent + reckless |
-| Interest: exporter loads the whole table into memory; exports over
-| ~50k rows crash the worker | Owner: DX | Trigger: 2026-09-01 |
```

The entry is deleted as "old, probably fine." Nothing was fixed: the exporter still loads the whole table, and the next 80k-row export crashes the worker in production — now with no record that the risk was ever known.

## After

```markdown
<!-- docs/tech-debt.md -->
| ID | Location | Quadrant | Interest | Owner | Trigger | Incurred | Status |
|---|---|---|---|---|---|---|---|
| DEBT-009 | src/reports/legacyExport.js | inadvertent + reckless | Exporter loads the whole table into memory; exports over ~50k rows crash the worker | DX | 2026-09-01 | 2026-08-14 | Closed 2026-11-21 — streaming export merged in PR #214; verified by the 100k-row export test |
```

The entry stays in the register as a closed record: what the debt was, who owned it, and the merged change that removed it. If the project had instead decided to cap exports at 50k rows permanently, the entry would be reclassified as an accepted-risk decision with the decider named — still not deleted.

## Note

Corrected under DX-090: entries close only by a merged change recorded against the entry (or a named accepted-risk reclassification); deleting a line from the register is not closure and is caught by G-DX-045.
