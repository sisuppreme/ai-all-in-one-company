# Example 1 — Hardcoded key in source

## Before

```ts
// billing.ts — the working key pasted in "just to get checkout running"
const payments = new PaymentsClient("sk_live_EXAMPLE-ONLY-NOT-A-SECRET");
```

The key sits in source, lands in git history on the first commit, and ships to everyone with repo access. (Placeholder shown; a real value in this position is the violation.)

## After

```ts
// billing.ts — value injected at deploy time, never written in the repo
const key = process.env.PAYMENTS_SECRET_KEY;
if (!key) throw new Error("PAYMENTS_SECRET_KEY is not set");
const payments = new PaymentsClient(key);
```

```dotenv
# .env.example — names and obvious placeholders only
PAYMENTS_SECRET_KEY=example-only-not-a-secret
```

Note: demonstrates SE-081 and SE-082; the Before is BAN-SE-041 (defeats DET-CODE-018).
