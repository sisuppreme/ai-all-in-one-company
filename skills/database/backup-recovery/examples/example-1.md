# Example 1 — No backups to a scheduled, tiered backup policy

## Before

The production database has no backup job of its own. The launch checklist says "the provider handles backups", nobody has verified what that means, and there is no retention policy:

```text
Backup schedule:    (none configured)
Retention:          (unstated)
Restore procedure:  (none)
```

## After

An automated policy runs without human initiation, with retention tiers in writing and point-in-time recovery via WAL archiving:

```bash
# Nightly base backup (cron on the database host, credentials from secret storage)
pg_basebackup -D /backups/base/$(date +%F) -Ft -z -P

# Continuous WAL archiving (postgresql.conf):
#   archive_mode = on
#   archive_command = 'test ! -f /archive/%f && cp %p /archive/%f'

# Retention, stated in the runbook:
#   daily backups kept 7 days, weekly kept 4 weeks, monthly kept 12 months
#   one copy synced nightly to object storage in a second region/account
```

**Corrects DB-201, DB-202** — backups are automated on a schedule, and retention tiers are written down with an off-domain copy.
