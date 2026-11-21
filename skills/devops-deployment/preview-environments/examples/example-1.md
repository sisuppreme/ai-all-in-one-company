# Example 1 — Preview database isolation

## Before

The hosting platform's preview deploy inherits the project's production environment group, so every PR preview starts with the production configuration:

```text
DATABASE_URL=postgres://app:****@db.prod.internal:5432/app_prod
PAYMENT_PROVIDER_KEY=sk_live_... (production secret)
```

A reviewer testing the new checkout flow on the preview URL creates real orders in the live database and charges a real card in test clicking.

## After

Preview deploys get their own environment group. The pipeline provisions a per-PR database, runs migrations, loads the synthetic seed set, and injects sandbox credentials:

```text
DATABASE_URL=postgres://preview:****@db.preview.internal:5432/app_pr_482
PAYMENT_PROVIDER_KEY=sk_test_... (sandbox key, previews group only)
```

The same checkout test now writes only to `app_pr_482`, which is destroyed when the PR closes.

Note: corrects DO-022 — previews never touch production data (and DO-023, separate credentials).
