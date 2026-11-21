# Example 3 — Same-account backups to an off-domain copy with separate keys

## Before

Backups are written to a bucket in the same cloud account as production, and the access key for that bucket is written inside the committed backup script:

```bash
# backup.sh (committed to the repo)
export BACKUP_BUCKET=s3://prod-backups
export AWS_ACCESS_KEY_ID=AKIA-EXAMPLE-KEY-IN-PLAINTEXT
export AWS_SECRET_ACCESS_KEY=example-secret-in-plaintext
pg_dump appdb | aws s3 cp - "$BACKUP_BUCKET/nightly.sql.gz"
# One account compromise — or one repo leak — destroys production
# and every backup, using the key printed above.
```

## After

The nightly sync copies backups to a bucket in a separate account and region, and the script reads short-lived credentials from secret storage at runtime — nothing secret exists in the repo or beside the backups:

```bash
# backup.sh — no credentials in the file; they are fetched at runtime.
eval "$(secretctl export backup-writer)"        # scoped, write-only role
pg_dump appdb | aws s3 cp - "s3://prod-backups/nightly.sql.gz"

# Off-domain copy: a second, separately-keyed role replicates to another
# account + region. Deleting any backup requires the backup-admin role,
# which neither the app role nor the writer role holds.
aws s3 sync "s3://prod-backups" "s3://prod-backups-dr" --source-region eu-west-1
```

**Corrects DB-202, DB-205** — at least one backup copy lives outside the primary failure domain, and backup credentials are stored apart from the backups themselves.
