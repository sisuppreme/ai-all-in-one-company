# Example 3 — A hand-run backfill replaced with a first-class backfill

## Before

The orders pipeline was down for three days. To recover, an engineer writes
a one-off script on the production server:

```bash
# /tmp/fix_days.sh  -- written during the incident, deleted after
for d in 2026-11-15 2026-11-16 2026-11-17; do
  psql -c "INSERT INTO cleaned_orders SELECT ... WHERE day = '$d'"
done
```

The script approximates the real transform from memory, skips the quality
checks, and leaves no record of what it did. The three "recovered" days are
subtly different from every normally processed day, forever.

## After

Backfill is the same DAG, invoked over the missed range. Airflow's backfill
runs the identical tasks with each day's window as the parameter:

```bash
airflow dags backfill orders_pipeline \
  --start-date 2026-11-15 \
  --end-date   2026-11-17
```

Each backfilled run executes the same extraction, transformation, quality
gates, and idempotent load as a scheduled run — including the checks the
hand script skipped — and each appears in the orchestrator's run history
with its window, so the recovery is auditable. There is no second code path
to keep in sync, because recovery was designed as a feature of the pipeline
instead of an improvisation during the incident.

Note: corrects DB-365 — backfill is a first-class operation running the same code path as scheduled runs.
