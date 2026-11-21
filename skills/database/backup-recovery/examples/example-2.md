# Example 2 — Untested dump to a scripted quarterly restore drill

## Before

A nightly dump job exists and its output files grow, so the team lists "backups: done" in every review. No restore has ever been attempted:

```text
Last successful backup:  nightly (files present)
Last successful restore: never
Measured RTO / RPO:      unknown
```

## After

The same script used for a real recovery runs quarterly against a scratch instance, and its measured results go into the runbook:

```bash
#!/usr/bin/env bash
# restore-drill.sh — restore latest base backup + WAL to a target time, then verify.
set -euo pipefail
TARGET_TIME="${1:?usage: restore-drill.sh 'YYYY-MM-DD HH:MM:SS TZ'}"
START=$(date +%s)

pg_ctl -D /scratch/restore stop -m immediate || true
rm -rf /scratch/restore
tar -xf /backups/base/latest/base.tar.gz -C /scratch/restore
cat > /scratch/restore/postgresql.auto.conf <<EOF
restore_command = 'cp /archive/%f %p'
recovery_target_time = '$TARGET_TIME'
EOF
touch /scratch/restore/recovery.signal
pg_ctl -D /scratch/restore start

# Smoke verification: migrations are current and key tables answer queries.
psql -d appdb -c "SELECT max(version) FROM schema_migrations;"
psql -d appdb -c "SELECT count(*) FROM orders WHERE created_at >= now() - interval '1 day';"
echo "Drill duration: $(( $(date +%s) - START ))s — record as measured RTO in the runbook."
```

**Corrects DB-203** — restore drills run on a schedule and record the measured RTO and RPO, instead of assuming the backups work.
