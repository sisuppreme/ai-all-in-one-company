# auth-hardening

## Metadata

- **Owner department:** D7 Security (SE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** NIST SP 800-63B Rev. 4, https://pages.nist.gov/800-63-4/sp800-63b.html ; OWASP Cheat Sheet Series, "Authentication Cheat Sheet", https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html
- **Depends on:** session-security, encryption
- **Feeds into:** api-security, backend-auth, security-audit

## When to use / Do NOT use

- **Use when:** Building or reviewing login, registration, password reset, MFA enrolment, or any privilege-change flow (role grant, email change, MFA reset).
- **Do NOT use when:** The question is token/session mechanics after login (use session-security), object-level authorization on API endpoints (use api-security), or password storage primitives in isolation (use encryption for the KDF parameters).

## Rules

1. **SE-061 — Password length policy.** Require at least 15 characters for single-factor passwords and at least 8 when MFA is also required; accept at least 64 characters; impose no composition rules (no forced symbol/uppercase mixes) per NIST SP 800-63B Rev. 4.
2. **SE-062 — Breached-password screening.** Screen every password at set and reset against a blocklist of known-breached and commonly used passwords; reject matches with a message that names the reason class, not the matched entry.
3. **SE-063 — No scheduled rotation, no hints.** Never force periodic password expiry absent evidence of compromise, never offer password hints, and never use knowledge-based recovery ("security questions").
4. **SE-064 — Paste and managers allowed.** Login and registration fields permit paste, autofill, and password-manager use; no `onpaste` blocking, no `autocomplete` suppression on credential fields.
5. **SE-065 — Strictest rate limits on auth.** Login, reset, and MFA-verification endpoints carry the strictest rate limits in the product, keyed on account identifier plus source IP — never on a client-supplied header alone (defeats DET-INF-023).
6. **SE-066 — Progressive delay, not silent failure.** After repeated failures, apply progressive delays and, at a defined threshold, a temporary lock or step-up challenge; the limit values live in config, not scattered constants.
7. **SE-067 — Generic failure responses.** Login and recovery responses never reveal whether an account exists: identical message, status, and response shape for "no such account" and "wrong password"; flatten obvious timing differences where feasible.
8. **SE-068 — Passwords hashed with a password KDF.** Store passwords only as Argon2id hashes (first choice), or scrypt/bcrypt/PBKDF2 at current OWASP parameters; never plaintext, never reversible encryption, never a fast general-purpose hash.
9. **SE-069 — MFA offered, pushed for privilege.** Offer MFA to every account — TOTP or WebAuthn/passkeys preferred over SMS — and require it (or a recorded exception) for admin and other privileged roles.
10. **SE-070 — Recovery as strong as login.** Reset tokens are single-use, short-lived, and unguessable; a successful reset invalidates existing sessions and notifies the account holder out-of-band; the reset endpoint never confirms whether the email is registered.
11. **SE-071 — Re-authentication for privilege changes.** Role grants, email changes, password changes, and MFA resets require the current password or an active MFA factor, and each notifies the account holder through a channel they already control.
12. **SE-072 — Auth events logged and alerted.** Log every authentication event — success, failure, reset requested/completed, MFA enrolment/change, lockout — with account, IP, and timestamp, and alert on anomaly patterns (failure bursts, impossible travel, stuffing signatures).

## BAN list

- **BAN-SE-031 — Any-password or test-mode login.** Banned: a login path that accepts any password, a fixed test password, or a backdoor bypass flag in shipped code. Defeats: DET-FAKE-001. Bad: `if (password === "test123" || user) { createSession(user) }` left in production. Instead: verify the submitted password against the stored KDF hash on every login, with no alternate success path. Severity: BLOCK.
- **BAN-SE-032 — Reset flow that fakes or leaks.** Banned: a password-reset flow that reports success without issuing a real single-use token, or whose response reveals whether the account exists. Defeats: DET-FAKE-020. Bad: "No account for that email" on the reset form, or a reset link that never expires and can be replayed. Instead: always return the same neutral confirmation, issue a single-use short-lived token, and expire it on first use. Severity: BLOCK.
- **BAN-SE-033 — Client-trusted privilege flags.** Banned: accepting role or privilege state (`isAdmin`, `role`) from the request body, a cookie, or any client-controlled value. Defeats: DET-FAKE-021. Bad: `if (req.body.isAdmin) grantAdmin()`. Instead: read the role from the server-side account record on every privileged request and re-check it at the endpoint. Severity: BLOCK.
- **BAN-SE-034 — Unlimited auth attempts.** Banned: login, reset, or MFA endpoints with no rate limit, lockout, or progressive delay. Defeats: DET-INF-023. Bad: a `/login` route reachable at full request speed from a single IP indefinitely. Instead: enforce per-account and per-IP limits with progressive delays on the auth endpoints, stricter than any other route class. Severity: BLOCK.
- **BAN-SE-035 — Plaintext or fast-hash password storage.** Banned: storing passwords in plaintext, reversibly encrypted, or hashed with MD5/SHA-1/SHA-256 or another fast general-purpose hash. Defeats: DET-CODE-018. Bad: a `users` table column holding `sha256(password)`. Instead: store an Argon2id (or approved KDF) hash with a per-password salt generated by the KDF. Severity: BLOCK.

## Gates

- **G-SE-031 — Auth abuse test pack.** Verifies: SE-065, SE-066, SE-067, SE-070. Check: run the scripted abuse suite against staging — a credential-stuffing burst (100 rapid attempts), a reset-token replay, a reset token used after expiry, and enumeration probes against login and reset. Pass: burst is throttled or locked by the configured threshold, replayed and expired tokens are rejected, and enumeration probes return indistinguishable responses. Fail: block release. Recorded in: progress.md.
- **G-SE-032 — NIST policy conformance assertion.** Verifies: SE-061, SE-062, SE-063, SE-064. Check: automated config assertion against the live auth configuration — minimum length ≥15 (single-factor) / ≥8 (with MFA), maximum length ≥64, composition rules off, forced rotation off, breached-password screening on, paste allowed. Pass: every assertion matches. Fail: block release. Recorded in: progress.md.
- **G-SE-033 — Password storage audit.** Verifies: SE-068. Check: `grep -RInE "md5\(|sha1\(|sha256\(.*password|password.*plaintext" src/` plus a schema inspection confirming the credential column stores KDF output (Argon2id/scrypt/bcrypt/PBKDF2 identifier prefix). Pass: zero fast-hash or plaintext hits and a recognised KDF format in stored credentials. Fail: block release. Recorded in: progress.md.
- **G-SE-034 — Privilege-change drill.** Verifies: SE-069, SE-071, SE-072. Check: manual drill on staging — grant a role, change an account email, and reset MFA, each first without re-authentication, then with it. Pass: every change is refused without re-authentication, succeeds with it, produces a holder notification, and appears in the auth event log. Fail: block release. Recorded in: progress.md. Simulated-channel provision (pre-provisioning): where the operator has no email or SMS channel available, the holder notifications are delivered to a local simulated channel — a captured test inbox or an SMS double — and the drill otherwise runs unchanged; the result is recorded as simulated in progress.md and in the product's own documentation, a drill with notification delivery over a real channel remains required before public launch, and simulated delivery must never be presented as real in any user-facing surface (Real Content Rule).

## Anti-patterns

- **Lockout as a denial-of-service gift.** Hard permanent lockouts let an attacker disable any account by failing logins as them; catch it by checking that throttling pairs per-account limits with per-IP limits and a recovery path that does not depend on the locked factor.
- **Security theatre policy.** Composition rules and 30-day rotation that push users to `Password1!` and sticky notes while the minimum length stays at 8; catch it by reading the policy as an attacker — length and blocklist do the work, rituals do not.
- **MFA bolted onto login only.** MFA enforced at sign-in but absent from recovery and MFA-reset flows, so the weakest path bypasses it; catch it by walking every path that ends in an authenticated session and checking each one demands the same assurance.
- **Helpful error messages.** Distinct "user not found" / "wrong password" / "account locked" responses written for support convenience; catch it by diffing the three responses byte-for-byte in a test account sweep.

## Examples

- [Example 1 — Password policy rewritten to NIST 800-63B](examples/example-1.md) — violates/corrects SE-061, SE-062, SE-063.
- [Example 2 — Login endpoint gains throttling and generic errors](examples/example-2.md) — violates/corrects SE-065, SE-066, SE-067.
- [Example 3 — Reset and privilege-change flow made real](examples/example-3.md) — violates/corrects SE-070, SE-071.

## Recall anchors

- Length and blocklist beat composition rules and rotation rituals.
- The strictest rate limits in the product belong on auth endpoints.
- Never reveal whether the account exists — anywhere, including reset.
- Recovery is part of login's strength, not an exception to it.
- Privilege changes re-authenticate and notify, every time.

## Checklist

- [ ] Password policy matches SE-061/SE-063 and passes the G-SE-032 config assertion.
- [ ] Breached-password screening is active at set and reset (SE-062).
- [ ] Auth endpoints are rate-limited per account + IP with progressive delay (SE-065, SE-066; G-SE-031 passes).
- [ ] Login and reset responses are indistinguishable for existing vs. non-existing accounts (SE-067).
- [ ] Stored credentials are KDF hashes only (SE-068; G-SE-033 passes).
- [ ] MFA is offered to all accounts and required for privileged roles (SE-069).
- [ ] Reset tokens are single-use and short-lived, sessions invalidated on reset (SE-070).
- [ ] Privilege changes re-authenticate, notify the holder, and are logged (SE-071, SE-072; G-SE-034 passes).
