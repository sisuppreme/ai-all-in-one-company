# Example 3 — Leak deleted but not revoked

## Before

A scanner flags the production database password in an early commit. The fix:

```text
commit a1b2c3d  "remove password from config"
- DB_PASSWORD=<the real production password, REDACTED here>
```

The team moves on. The password is still valid, and still readable by anyone who checks out the earlier commit — the deletion changed nothing that matters.

## After

The same discovery, handled in the fixed order:

1. **Revoke:** the database password is changed at the provider immediately; the old value stops working everywhere.
2. **Replace:** the new password is issued into the platform secret store and injected as `DB_PASSWORD`; `.env.example` gains the name with the placeholder `example-only-not-a-secret`.
3. **Purge:** history is rewritten (or the repo re-created) so the old value no longer appears in any commit, and `gitleaks git .` re-runs clean over the full history.
4. **Investigate:** the log records how the value was committed (`.gitignore` added late) and the template is fixed so `.env` is ignored from commit one.

Note: demonstrates SE-091; the Before is BAN-SE-044 (defeats DET-INF-005).
