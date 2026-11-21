# D7 Example — An Auth Flow That Leaked Everything It Protected

## Scenario

D7 reviews the SaaS's authentication end to end before launch: signup,
login, session handling, password reset, and where the secrets live. The
flow "works" — users can log in — which is precisely why its failures
are invisible without the review.

## Before

```ts
// signup + login
user.password = md5(password);                       // fast hash, no salt
const token = Buffer.from(user.email).toString("base64");  // session "token"
localStorage.setItem("session", token);              // readable by any script

// POST /login — no attempt limits
if (!user) return res.json({ error: "No account for that email" });
if (user.password !== md5(pw)) return res.json({ error: "Wrong password" });

// POST /reset — accepts any token value, never expires
// config.ts, committed to the repo:
export const JWT_SECRET = "dev-secret-do-not-ship";
```

```bash
# .env.example, also committed
DATABASE_URL=postgres://app:Tr7!realpassword@db.internal.example.com/app
```

## What the skills caught

- **BAN-SE-035 — Plaintext or fast-hash password storage**: MD5 falls to
  commodity hardware in minutes. **SE-068 — Passwords hashed with a
  password KDF** (Argon2id or bcrypt); the storage audit **G-SE-033**.
- **BAN-SE-015 — Predictable IDs or a hardcoded token secret**: a base64
  email is not a session, it is an invitation — anyone can mint one for
  any account. **SE-021 — Server-issued, high-entropy session IDs only**.
- Token in `localStorage` with no cookie attributes at all: **SE-024 —
  Cookie attributes set explicitly, per cookie**; the cookie-attribute
  assertion **G-SE-011** and the fixation/rotation test **G-SE-012**
  (the pre-login session ID also survives login — **BAN-SE-012**).
- **BAN-SE-034 — Unlimited auth attempts**: **SE-065 — Strictest rate
  limits on auth**, with **SE-066 — Progressive delay** rather than
  lockout silence.
- The two different login errors enumerate accounts, violating **SE-067
  — Generic failure responses**; the auth abuse test pack **G-SE-031**
  includes exactly this probe.
- Reset accepts anything and never expires — the pattern behind
  **DET-FAKE-020 — Password reset that resets nothing** (here: resets
  everything, for anyone). **SE-070 — Recovery as strong as login**.
- **BAN-SE-041 — Secret literal in source or tests** and **BAN-SE-045 —
  Real value pasted as the "example"**: **SE-081 — Secrets live outside
  code**, **SE-082 — `.env.example` carries names only** (**DET-CODE-018
  — Hardcoded secrets and credentials**, **DET-INF-005**). Both committed
  values must be rotated, not just deleted (**SE-091 — A committed
  secret is public**).

## After

Passwords are hashed with Argon2id with per-user salts, and breached-
password screening runs at signup (**SE-062**). Login returns one
generic message — "Email or password is incorrect" — for every failure
mode, is rate-limited per account and per IP with progressive delay,
and every attempt is logged (**SE-072**).

Sessions are server-issued 128-bit random IDs, rotated at login and at
every privilege change (**SE-023**), carried in a cookie set explicitly:
`HttpOnly; Secure; SameSite=Lax; Path=/`, with idle and absolute
timeouts enforced server-side (**SE-025**, **SE-026**). Logout deletes
the server-side session, not just the cookie (**SE-027**).

Reset links carry a single-use token, stored hashed, expiring in 30
minutes; requesting a reset always returns the same response whether or
not the account exists, and a successful reset invalidates the account's
other sessions (**SE-028**).

Secrets now live in the platform secret store, one credential per
service per environment (**SE-084**). `.env.example` lists names only.
The two leaked values were revoked and replaced before the fix shipped —
deleting them from HEAD would have changed nothing.

## Skills used

- [auth-hardening](../skills/security/auth-hardening/SKILL.md)
- [session-security](../skills/security/session-security/SKILL.md)
- [secrets-management](../skills/security/secrets-management/SKILL.md)
- [owasp](../skills/security/owasp/SKILL.md)
