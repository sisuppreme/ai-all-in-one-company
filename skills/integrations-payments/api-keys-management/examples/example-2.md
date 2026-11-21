# Example 2 — Replacing a committed .env with secret-store references

## Before

The real configuration file is committed to the repository:

```text
# .env — committed in the initial scaffold commit
PROVIDER_SECRET_KEY=sk_live_EXAMPLE
WEBHOOK_SIGNING_SECRET=whsec_EXAMPLE
DATABASE_URL=postgres://app:EXAMPLE_PASSWORD@db.internal:5432/app
```

Every clone, fork, backup, and CI cache now carries working credentials.
Removing the file in a later commit changes nothing: the values remain in
git history, readable by anyone who ever had the repo.

## After

The repo carries placeholders only; real values resolve from the secret
store at deploy time, and the leaked values have been rotated:

```text
# .env.example — the only env file in the repository
PROVIDER_SECRET_KEY=sk_live_EXAMPLE
WEBHOOK_SIGNING_SECRET=whsec_EXAMPLE
DATABASE_URL=postgres://app:EXAMPLE_PASSWORD@db.internal:5432/app
```

```text
# deployment configuration
env:
  PROVIDER_SECRET_KEY:  secret-store://prod/provider-secret-key
  WEBHOOK_SIGNING_SECRET: secret-store://prod/webhook-signing-secret
  DATABASE_URL:         secret-store://prod/database-url
```

`.env` is in `.gitignore`, the secret scan covers the full history
(G-IN-101), and because the original values were treated as leaked
(IN-208), the rotated keys — not the committed ones — are what authenticate.

Note: corrects IN-201 — keys live in secret storage, never in the repo; the repository carries only `.env.example` with dummy placeholders.
