# Example 2 — The example file with a real key

## Before

```dotenv
# .env.example
DATABASE_URL=postgres://app:<real-password-pasted-here>@db.internal.example.com:5432/app_prod
STRIPE_SECRET_KEY=sk_live_... (a working key, pasted "temporarily")
SESSION_SECRET=hunter2-corp-prod
# PORT is also read by the code but is not listed here.
```

The example file leaks two production credentials, and the app — which reads `PORT` and `SMTP_URL` as well — starts silently on built-in defaults when they are absent, including a default database URL pointing at production.

## After

```dotenv
# .env.example — copy to .env. Every value below is a non-functional
# placeholder; local development works with them unchanged.
DATABASE_URL=postgres://app:change-me@localhost:5432/app_dev   # local dev database (started by make setup)
STRIPE_SECRET_KEY=sk_test_example-placeholder                  # Stripe TEST-mode key; get your own from the test dashboard
SESSION_SECRET=change-me-to-a-long-random-string               # signs session cookies; any random string works locally
PORT=3000                                                      # HTTP port the app listens on
SMTP_URL=smtp://localhost:1025                                 # local mail catcher started by make setup
```

Startup validates the full list: with any required variable unset, the app exits with `Missing required config: SMTP_URL (see .env.example)` instead of falling back to a default.

## Note

Corrected under DX-006 (placeholders only — a real key in an example file is BAN-DX-001) and DX-005 (every variable the code reads is listed); the fail-fast behavior satisfies DX-007 and removes the silent production default banned by BAN-DX-004.
