# Example 3 — A restore drill on record

## Before

```markdown
## Launch checklist

- [x] Backups: enabled ✓ (nightly snapshots on the same cloud
      account as production)
```

Backups are asserted, not evidenced: snapshots sit in the same failure domain as the primary, and nobody has ever restored one, so the recovery time is unknown.

## After

```markdown
## Restore drill log — orders database

- **Cadence:** monthly (DO-269). **Targets:** RTO 60 min,
  RPO 24 h; DR tier: backup-and-restore (DO-270).
- **Storage:** nightly dumps replicated to a separate cloud
  account and region from the primary (DO-268).

| Date | Backup restored | Duration | Result |
|---|---|---|---|
| 2026-10-03 | dump 2026-10-02 | 38 min | Pass — within RTO |
| 2026-11-04 | dump 2026-11-03 | 41 min | Pass — within RTO |
```

The drill is dated, timed, and compared against the RTO target, and the backup copy lives outside the primary failure domain — so the "protected" claim is evidence, not a checkbox.

Note: Demonstrates DO-268, DO-269, and DO-270 — backups outside the primary failure domain, restores rehearsed on cadence with timings recorded, and written RTO/RPO targets with a chosen DR tier.
