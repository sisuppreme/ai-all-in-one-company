# backend-auth

## Metadata

- **Owner department:** D4 Backend & APIs (BE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** OWASP Session Management Cheat Sheet — https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html ; PROJECT_ANATOMY.md, "Authentication and authorization implementation"
- **Depends on:** secrets-management, rate-limiting
- **Feeds into:** rbac, oauth-sso, session-security

## When to use / Do NOT use

- **Use when:** implementing or reviewing signup, login (by password, passkey/WebAuthn, or a delegated flow), logout, session handling, or password reset for any client — anywhere the system must prove who a caller is before trusting a request. Whatever the proof method, the session it produces obeys this skill's rules.
- **Do NOT use when:** deciding what an authenticated user may do (rbac), hardening auth against advanced attacks in depth (auth-hardening), or running OAuth/OIDC provider flows (oauth-sso — though the session those flows produce obeys this skill's rules). This skill owns identity proof and the session lifecycle.

## Rules

1. **BE-101 — Server-side proof on every request.** Authentication is verified by the server on each protected request. Client state — a storage flag, a hidden route, a client-sent role — is never evidence of authentication.
2. **BE-102 — Passwords are hashed, memory-hard, salted.** Passwords are stored only as hashes from a vetted memory-hard algorithm (Argon2id/bcrypt class) with a per-user salt. Plaintext storage, reversible encryption, and fast hashes (MD5/SHA-1/plain SHA-2) are defects.
3. **BE-103 — Sessions are server-issued and cookie-carried.** A session is a high-entropy opaque ID (or a signed token with server-side revocation), issued at login and carried in a `Secure` + `HttpOnly` + `SameSite` cookie for browser clients.
4. **BE-104 — Rotation on authentication and privilege change.** The session ID is rotated at login and whenever privilege changes; the previous ID stops working immediately.
5. **BE-105 — Expiry is enforced server-side.** Logout, idle timeout, and absolute timeout all invalidate the session on the server. A client deleting its cookie is not a logout.
6. **BE-106 — Signup is not done until login works.** Signup completes only when the account record exists, the password is hashed per BE-102, and a login with the new credentials from a clean session succeeds.
7. **BE-107 — Reset is a credential change.** A reset uses a single-use, expiring token; completing it changes the stored credential and revokes all existing sessions. The old password must stop working.
8. **BE-108 — No account enumeration.** Failed-login responses are identical in body and status for an unknown account and a wrong password, and signup/reset messaging never confirms whether an account exists.
9. **BE-109 — Auth endpoints are rate-limited.** Login, signup, and reset endpoints carry per-account and per-IP limits (mechanics in rate-limiting), independent of the API's general budget.
10. **BE-110 — Credentials never leak into artifacts.** Passwords, session IDs, and reset tokens never appear in URLs, logs, error responses, or analytics events.
11. **BE-111 — Delegated login changes nothing.** A session produced by an OAuth/OIDC flow (oauth-sso) obeys BE-103 through BE-105 identically — same cookie attributes, rotation, and server-side expiry.

## BAN list

- **BAN-BE-051 — Any-password login.** Banned: a login that accepts any password, one hardcoded credential, or a credential check performed only in client code. Defeats: DET-FAKE-001. Bad: the demo login "signs in" with whatever is typed, and the shipped build keeps the behavior behind the real-looking form. Instead: verify credentials server-side against the stored hash (BE-101, BE-102) and reject wrong passwords with the generic error (BE-108). Severity: BLOCK.
- **BAN-BE-052 — Session that is only a flag.** Banned: post-login state stored as a `localStorage` boolean or in-memory variable, with protected data served on the client's say-so. Defeats: DET-FAKE-002. Bad: `localStorage.setItem("isLoggedIn", "true")` after login; editing storage by hand "authenticates," and the API answers protected routes without any session. Instead: issue a server-side session in a `Secure` + `HttpOnly` cookie and enforce it on every request (BE-101, BE-103). Severity: BLOCK.
- **BAN-BE-053 — Signup that registers nothing.** Banned: a signup flow that shows success while creating no account record — data discarded, or kept only in the browser. Defeats: DET-FAKE-003. Bad: "Account created!" renders, the user signs out, and no credentials will ever sign them back in because nothing was stored. Instead: write the account with its hashed password, then prove it — a clean-session login with the new credentials succeeds before signup is called done (BE-106). Severity: BLOCK.
- **BAN-BE-054 — Reset that resets nothing.** Banned: a forgot-password flow whose token is unchecked, reusable, or disconnected from the credential store, so the "reset" succeeds and the old password keeps working. Defeats: DET-FAKE-020. Bad: the form accepts any code, shows "Password updated," and the original password still logs in — the flow is theater over an unchanged credential. Instead: single-use expiring token; on use, replace the hash and revoke all sessions (BE-107). Severity: BLOCK.
- **BAN-BE-055 — Plaintext or fast-hash password storage.** Banned: storing passwords in plaintext, reversibly encrypted, or hashed with a fast unsalted algorithm. Defeats: DET-CODE-020 (nearest match — no DET parameter names this exact signal). Bad: the user table holds `sha256(password)` values, so one database leak becomes a credential list that falls to a commodity GPU in hours. Instead: hash with a memory-hard algorithm and a per-user salt (BE-102), and verify storage with G-BE-052. Severity: BLOCK.

## Gates

- **G-BE-051 — Auth test pack.** Verifies: BE-101, BE-103, BE-105. Check: automated — in CI, run the pack against a running instance: wrong password is rejected; a real session survives a reload; after logout the same session ID is refused server-side; a direct API call with no credentials returns `401`. Pass: all four behaviors hold. Fail: block shipment. Recorded in: progress.md.
- **G-BE-052 — Credential-store inspection.** Verifies: BE-102. Check: automated query plus manual review — select the password column for all users; assert every value matches the approved hash format, salts are unique per user, and no value equals or contains its plaintext. Pass: 100% conforming hashes, zero plaintext. Fail: block shipment and treat any plaintext find as an incident. Recorded in: progress.md.
- **G-BE-053 — Reset drill.** Verifies: BE-107. Check: automated — on a test account, request a reset, complete it, then assert: the old password fails, the new password works from a clean session, the token cannot be reused, and sessions opened before the reset are rejected. Pass: all four assertions hold. Fail: block shipment. Recorded in: progress.md.
- **G-BE-054 — Enumeration probe.** Verifies: BE-108. Check: automated — submit failed logins for an existing account with a wrong password and for a nonexistent account; compare status, body, and response shape. Pass: responses are indistinguishable. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **The demo credential that shipped.** A test account with a published or guessable password, created for a demo, is still active in production. Catch it: list accounts that have never been seen in real use and try the credentials from the seed data and the README.
- **Security by route hiding.** Protected pages are "protected" because the navigation never links to them and the route name is unguessable. Catch it: request the route directly, unauthenticated — hiding is presentation, not a control (BE-101).
- **The forever reset link.** Reset tokens that never expire and work repeatedly, so an old email in a shared inbox is a permanent back door. Catch it: complete a reset, then use the same link again tomorrow — BE-107 says it must already be dead.
- **Log-the-login.** During debugging, auth code logs passwords, full session IDs, or reset tokens, and the logging ships. Catch it: grep the log configuration and one day's logs for credential-shaped values (BE-110).

## Examples

- [Example 1 — localStorage flag replaced by a server session](examples/example-1.md) — corrects BE-101, BE-103.
- [Example 2 — Theatrical reset replaced by a real credential change](examples/example-2.md) — corrects BE-107.
- [Example 3 — Enumerating login errors replaced by one generic failure](examples/example-3.md) — corrects BE-108.

## Recall anchors

- Client state is never evidence; the server proves identity on every request.
- Hash memory-hard and salted — plaintext and fast hashes are defects.
- Logout, idle, and absolute expiry all kill the session server-side.
- Reset changes the credential and revokes every session.
- Unknown user and wrong password get the same answer.

## Checklist

- [ ] Wrong password is rejected and a real session survives reload (G-BE-051).
- [ ] Every stored password is a salted memory-hard hash; zero plaintext (G-BE-052).
- [ ] Sessions ride in Secure + HttpOnly + SameSite cookies and rotate on login and privilege change (BE-103, BE-104).
- [ ] Logout invalidates the session server-side, not just the cookie (BE-105).
- [ ] Signup is proven by a clean-session login with the new credentials (BE-106).
- [ ] The reset drill passes: old password dead, token single-use, prior sessions revoked (G-BE-053).
- [ ] Login failures are indistinguishable for unknown vs. existing accounts (G-BE-054).
- [ ] No password, session ID, or reset token appears in any URL or log (BE-110).
