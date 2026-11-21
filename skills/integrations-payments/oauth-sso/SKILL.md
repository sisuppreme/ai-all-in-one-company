# oauth-sso

## Metadata

- **Owner department:** D11 Integrations & Payments (IN)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** RFC 9700, OAuth 2.0 Security Best Current Practice — https://www.rfc-editor.org/rfc/rfc9700.html ; RFC 7636, PKCE — https://www.rfc-editor.org/rfc/rfc7636.html ; OAuth 2.1 draft (work in progress, not an RFC) — https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1/
- **Depends on:** api-keys-management (provider client credentials live in secret storage)
- **Feeds into:** backend-auth (D7), subscriptions (entitlement identity), transactional-email (account notices)

## When to use / Do NOT use

- **Use when:** adding "Sign in with X", enterprise SSO, or any federated login; consuming identity from an OAuth 2.0 / OpenID Connect provider; linking provider identities to local accounts.
- **Do NOT use when:** the app issues its own passwords and sessions with no external provider (backend-auth owns that), or the task is outbound API authorization for a machine integration with no user identity (third-party-apis).

## Rules

1. **IN-161 — Authorization code flow with PKCE, for every client.** All clients — server-side, SPA, and mobile — use the authorization code flow with PKCE, `code_challenge_method=S256` only; the `plain` method is forbidden (RFC 9700; RFC 7636).
2. **IN-162 — Exact-string redirect URIs.** Every redirect URI is registered as an exact string, per environment, at the provider. No wildcards, no pattern matching, no "any localhost port" in production registrations.
3. **IN-163 — `state` and `nonce` on every request.** Each authorization request carries a fresh, unguessable `state` (CSRF) and `nonce` (ID-token binding), stored server-side or in a signed cookie, and both are verified on the callback before any token is accepted.
4. **IN-164 — ID tokens are validated server-side, every time.** Before an identity is trusted, the server verifies the ID token's signature against the issuer's published JWKS and checks `iss`, `aud`, `exp`, and `nonce`. A token the client merely presents from local state proves nothing.
5. **IN-165 — Access tokens are validated on every API request.** Protected endpoints verify the access token (signature and claims, or introspection) per request; a client-side route guard or a stored "logged in" value is never the authorization check.
6. **IN-166 — Identity is keyed on issuer + subject.** A federated identity is stored and matched as the pair (`iss`, `sub`). Email is a mutable attribute, never the join key.
7. **IN-167 — Linking is explicit.** A provider identity links to an existing account only when the provider verified that identity (matching `iss` + `sub` on file) or when a currently signed-in user confirms the link. A matching email alone never links, merges, or creates a privileged account.
8. **IN-168 — The app owns its session.** After the provider authenticates, the app issues its own session (opaque ID, Secure, HttpOnly cookie) and manages its lifetime. A provider outage must not log out or lock out users with live app sessions.
9. **IN-169 — Refresh tokens rotate or are sender-constrained.** For public clients, refresh tokens are rotated on each use with reuse detection (a replayed token revokes the whole family) or sender-constrained; long-lived static refresh tokens in browser storage are forbidden.
10. **IN-170 — No legacy grants, no tokens in URLs.** The implicit flow and the resource-owner-password flow are forbidden in new integrations. Tokens never travel in query strings or URL fragments.
11. **IN-171 — Least-privilege scopes.** Request only the scopes the feature uses, incrementally where the provider supports it. `openid` plus profile basics is the default ask; broad scopes "for later" are a defect.
12. **IN-172 — Cite the standards at their real status.** RFC 9700 is the normative floor. OAuth 2.1 is an IETF Internet-Draft — its consolidated profile is the target shape, but it is never cited as a published standard, and its status is re-checked at every revision of this skill.

## BAN list

- **BAN-IN-081 — Callback trusted, token never validated.** Banned: treating a successful provider redirect (or a client-posted ID token) as proof of identity without server-side signature and claims validation. Defeats: DET-FAKE-001. Bad: the callback route reads `email` from the posted ID token payload and signs the user in — anyone can forge the payload and sign in as anyone. Instead: validate per IN-164 (JWKS signature, `iss`, `aud`, `exp`, `nonce`) on the server before a session exists. Severity: BLOCK.
- **BAN-IN-082 — Session that is only a client flag.** Banned: recording login as a `localStorage` boolean or a provider token sitting in browser storage, with protected data shipped to the client on that basis. Defeats: DET-FAKE-002. Bad: after the OAuth redirect, the SPA sets `isLoggedIn = true` and renders the account page; editing storage grants "access." Instead: issue the app's own server session (IN-168) and enforce authorization server-side on every request (IN-165). Severity: BLOCK.
- **BAN-IN-083 — Fake SSO button.** Banned: a "Continue with Google" (or similar) button that creates or signs into a local account without a real provider round-trip and token exchange. Defeats: DET-FAKE-003. Bad: the button prompts for an email, creates the account locally, and shows the provider's logo on the button. Instead: run the full authorization code + PKCE flow against the real provider; the account is created from the validated identity (IN-166). Severity: BLOCK.
- **BAN-IN-084 — Auto-linking on email match.** Banned: merging a provider identity into an existing account — above all a privileged one — because the provider returned the same email address. Defeats: DET-FAKE-021. Bad: an attacker registers the admin's email at a lax provider, signs in, and is auto-linked into the admin account. Instead: link only on (`iss`, `sub`) already on file or on explicit confirmation by the signed-in user (IN-167). Severity: BLOCK.
- **BAN-IN-085 — Tokens in URLs.** Banned: implicit-flow responses or any design that places access or ID tokens in a query string or fragment, where they leak into logs, history, and referers. Defeats: DET-FAKE-001. Bad: `response_type=token` returns `#access_token=…` and the token is pasted into analytics events. Instead: authorization code flow (IN-161); tokens move only in POST bodies and headers (IN-170). Severity: BLOCK.

## Gates

- **G-IN-081 — Flow and token-validation test.** Verifies: IN-161, IN-164. Check: automated — scripted authorization-code + PKCE login against the provider's test tenant; then present (a) an ID token with a tampered payload and (b) a validly signed token with a wrong `aud`. Pass: the real login succeeds; both forged tokens are rejected and no session is created. Fail: block shipment. Recorded in: progress.md.
- **G-IN-082 — Redirect URI rejection test.** Verifies: IN-162. Check: automated — attempt the flow with an unregistered redirect URI variant (added path segment, look-alike host, unregistered port). Pass: the provider rejects every variant before any code is issued. Fail: block shipment; fix the provider registration. Recorded in: progress.md.
- **G-IN-083 — State and nonce mismatch test.** Verifies: IN-163. Check: automated — complete a real authorization, then replay the callback with an altered `state` and again with a mismatched `nonce`. Pass: both callbacks are rejected and no session or token exchange results. Fail: block shipment. Recorded in: progress.md.
- **G-IN-084 — Account-linking test.** Verifies: IN-166, IN-167. Check: automated — two providers return the same email for different `sub` values; sign in with each. Pass: two distinct identities result, and one account exists only after the explicit signed-in linking path is used. Fail: block shipment. Recorded in: progress.md.
- **G-IN-085 — Session-independence and grant audit.** Verifies: IN-168, IN-170. Check: automated + manual — end the provider-side session and confirm the live app session still authorizes; then grep the provider client configuration and codebase for `implicit`, `password` grant types and token-in-URL patterns. Pass: app session unaffected; zero legacy-grant or token-in-URL hits. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **The dev-mode validation skip that ships.** Signature checking disabled "while debugging" behind a flag or a commented-out verify call that survives into production. Catch it: grep for the validation call — it must be unconditional on the callback path.
- **Email as the users-table primary key.** Federated sign-ins bolted onto a schema keyed by email, so every provider quirk becomes an account-takeover or duplicate-account bug. Catch it: if a schema change proposes matching users by email at sign-in, the design is wrong (IN-166).
- **Scope hoarding.** Requesting every scope the provider offers at first login "to avoid re-prompting later," training users to rubber-stamp consent. Catch it: diff requested scopes against the features actually shipped.
- **Tokens in the logs.** Access or ID tokens pasted into error reports, analytics, or debug logs during integration work. Catch it: log-scrub for token-shaped strings before any log leaves the machine; a logged token is treated as compromised.

## Examples

- [Example 1 — The callback that trusted the redirect](examples/example-1.md) — corrects IN-164.
- [Example 2 — Auto-linked by email](examples/example-2.md) — corrects IN-166, IN-167.
- [Example 3 — Implicit flow in a single-page app](examples/example-3.md) — corrects IN-161, IN-170.

## Recall anchors

- Code flow + PKCE (S256) for every client — no exceptions.
- Validate the token on the server: signature, `iss`, `aud`, `exp`, `nonce`.
- Identity is (`iss`, `sub`) — never an email address.
- The provider authenticates; your app owns the session.
- RFC 9700 is the floor; OAuth 2.1 is still a draft.

## Checklist

- [ ] Authorization code flow with PKCE S256 is the only flow in use (IN-161, IN-170).
- [ ] Redirect URIs are exact strings, registered per environment (IN-162).
- [ ] `state` and `nonce` are generated per request and verified on callback (G-IN-083).
- [ ] ID-token validation (JWKS, `iss`, `aud`, `exp`, `nonce`) passes the forged-token tests (G-IN-081).
- [ ] Accounts key on (`iss`, `sub`); linking follows the explicit path only (G-IN-084).
- [ ] App sessions survive a provider outage; refresh tokens rotate with reuse detection (IN-168, IN-169).
- [ ] Requested scopes match shipped features — nothing hoarded (IN-171).
