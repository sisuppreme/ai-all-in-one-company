# Example 2 — Seed script that refuses production

## Before

The seed script connects to whatever database the environment points at and inserts 200 demo users, 40 products, and a page of testimonials. The only protection is a comment at the top: "DO NOT RUN IN PRODUCTION." During a deploy rehearsal it is run against the production database, and the fabricated customers and praise quotes go live as if they were real.

## After

The seed entry point checks the environment before writing anything:

```bash
if [ "$APP_ENV" = "production" ] && [ "$ALLOW_DEMO_SEED" != "1" ]; then
  echo "Refusing to seed production without ALLOW_DEMO_SEED=1" >&2
  exit 1
fi
```

Every record it writes carries the synthetic marker (`is_seed = true`, seed-domain emails), and CI runs the refusal check (G-QA-122) on every change to the seed path. The rehearsal run now exits non-zero and writes zero rows.

Note: corrects QA-247 (the seed path refuses production).
