# Example 3 — Fixtures, a leaked key, and a fresh account that finally starts empty

Scenario: "LedgerLite" (a hypothetical invoicing prototype) is about to take
its first real customers. The DX-161 inventory finds two findings that block
the verdict on sight: the production seed script loads the demo's invented
customers and invoices, and a live payment-provider secret key is committed
in the repo — and, worse, inlined into the built client bundle, where any
visitor can read it.

## Before

```js
// src/config.js — committed to the repo, and imported by client code,
// so the secret is inlined into the production JavaScript bundle.
export const PAYMENTS_SECRET_KEY = 'sk_live_' + 'EXAMPLE0000000000000000DEMO';
// (The key above is a fake placeholder, printed here as two joined literals
// so this document does not itself trip secret scanners. In the repo it was
// one continuous live key string — that is the violation.)
export const API_BASE = 'http://localhost:3000'; // hardcoded per-machine URL
```

```js
// server/seed.production.js — run on every production deploy
await db.insert('customers', [
  { name: 'Acme Demo Co',      email: 'acme@example.test' },
  { name: 'Globex (sample)',   email: 'globex@example.test' },
  { name: 'Jane Demo',         email: 'jane@example.test' },
]);
await db.insert('invoices', demoInvoices); // 14 invented invoices,
                                           // staged "recent activity"
await db.insert('users', [
  { email: 'demo@ledgerlite.example', password: 'demo1234', role: 'admin' },
]);
```

```text
# What a fresh production account saw before hardening
Dashboard → 3 customers, 14 invoices, activity feed already populated —
none of it theirs. The demo admin account above also signed in, because
the seeder created it in production with a guessable password.
```

This is BAN-DX-084 (seed and fixture data shipped as real data) and
BAN-DX-082 (a secret in source, history, and the client bundle) at the same
time. Relabeling the invoices "sample" would not fix either one: DX-169
requires removal, not relabeling, and DX-165 treats a key found in the
bundle as compromised even after it leaves the source file.

## After

Step 1 — rotate first, then move (DX-165). The exposed key is revoked in
the provider dashboard and a replacement is issued *before* any code
change, because the old value has been public since it shipped:

```bash
# Old key: revoked at the provider (not merely deleted from the repo).
# New key: exists only in the environment / secrets store.
grep -rn "sk_live" src/ server/ dist/   # tree AND built bundle re-scanned
# → no matches
```

Rotation closes the provider side; the repository side is closed by
purging the value from committed history (a history rewrite per
`secrets-management`, agreed with everyone holding a clone). Deleting
`src/config.js` alone would leave the live value one `git log -p` away —
only after the purge does the history scan in Step 4 mean anything.

```js
// server/config.js — server-only module; never imported by client code
const key = process.env.PAYMENTS_SECRET_KEY;
if (!key) throw new Error('PAYMENTS_SECRET_KEY is not configured');
export const payments = createPaymentsClient({ secretKey: key });
export const API_BASE = requiredEnv('API_BASE'); // per-environment (DX-171)
```

Step 2 — delete the fixtures from production paths (DX-169). The
production seeder is removed entirely; the demo dataset survives only in a
demo configuration that production cannot enable:

```js
// server/seed.js — the only seeder left
if (process.env.APP_ENV === 'production') {
  throw new Error('Seeding is disabled in production.');
}
if (process.env.DEMO_MODE !== 'true') {
  throw new Error('Demo seed requires DEMO_MODE=true (non-production only).');
}
// …demo customers/invoices inserted here, into a non-production store…
```

Step 3 — ship honest empty states instead of staged content (DX-169):

```jsx
// src/pages/Dashboard.jsx
{invoices.length === 0 ? (
  <EmptyState
    title="No invoices yet"
    body="Invoices you create will appear here."
    action={<Link to="/invoices/new">Create your first invoice</Link>}
  />
) : (
  <InvoiceList invoices={invoices} />
)}
```

Step 4 — prove it with gate G-DX-083 against the production-configured
build, and record the outcome in the hardening ledger:

```text
G-DX-083 — Secret and placeholder sweep of the shipped artifact
- Secret scanner over working tree ............ 0 findings
- Secret scanner over committed history ....... 0 findings (the exposed
  value survives only in the provider's revocation log, nowhere in the repo)
- Secret scanner over built client bundle ..... 0 findings
- placeholder-scan sweep (QA-284) of rendered
  production output ........................... 0 findings
- Fresh production account created ............ dashboard shows the
  "No invoices yet" empty state; 0 customers, 0 staged activity
- Demo admin account .......................... login rejected (removed)
Result: PASS — data area closed HARDENED (DX-174)
```

One shortcut is deliberately kept and disclosed rather than hidden: the
demo dataset still lives in the repo for sales demos. Under DX-173 it is
entered in the tech-debt register with its interest (fixture data must
never gain a production import path) and its repayment trigger (delete the
dataset when the demo environment is retired), and it is named in the
hardening ledger — it is not left as an undocumented risk.

## Note

Corrected under DX-165 (every secret rotated, revoked, moved to the
environment or a secrets store, and the tree, history, and built bundle
re-scanned), DX-169 (fake and placeholder content removed, not relabeled;
honest empty states; surviving demo mode isolated behind a labeled
non-production configuration), and DX-171 (environment-specific values from
configuration, environments separated). Removes the violations in
BAN-DX-082 (secrets in source, history, or the client bundle) and
BAN-DX-084 (seed and fixture data shipped as real data). Verified by
G-DX-083; the kept demo dataset is registered under DX-173.
