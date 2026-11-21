# api-security

## Metadata

- **Owner department:** D7 Security (SE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** OWASP API Security Top 10 (2023), https://orca.security/resources/blog/owasp-api-security-top-10/
- **Depends on:** owasp, session-security, auth-hardening
- **Feeds into:** security-audit, penetration-testing

## When to use / Do NOT use

- **Use when:** designing, building, or reviewing any HTTP API endpoint — authentication, authorization, serialization, quotas, outbound fetching, or third-party API consumption.
- **Do NOT use when:** the work is the login/session lifecycle itself (use auth-hardening and session-security) or a general web vulnerability pass with no API surface (use owasp).

## Rules

1. **SE-041 — Authenticate every request on the server.** Every endpoint not on an explicit, documented public allowlist rejects requests without a valid credential, verified server-side; a check that exists only in the UI is not authentication.
2. **SE-042 — Authorize every object access against ownership (API1/BOLA).** An object ID in a request is a claim, not a permission: the server resolves the object's owner from the authenticated principal and returns 403/404 when they do not match.
3. **SE-043 — Authorize every function by role (API5/BFLA).** Privileged endpoints (admin, billing, moderation, export) check the caller's role server-side on every request, independent of what the client chose to render.
4. **SE-044 — Filter properties in both directions (API3/BOPLA).** Responses pass through an explicit field-allowlist serializer; writes bind only to a request DTO of writable fields, so extra submitted properties are ignored or rejected — never mass-assigned.
5. **SE-045 — Cap resource consumption per endpoint (API4).** Every list endpoint enforces a maximum page size, every endpoint a request-body size limit and a timeout, and every API key a quota; no endpoint runs unbounded.
6. **SE-046 — Protect sensitive business flows from automation (API6).** Signup, login-adjacent, checkout, coupon, OTP, and password-reset flows carry per-account and per-IP rate limits or equivalent anti-automation controls at the edge.
7. **SE-047 — Constrain server-side fetching of user-supplied URLs (API7/SSRF).** Outbound fetches go to allowlisted hosts only, deny private, loopback, and link-local ranges, re-validate the target after every redirect, and never attach internal credentials.
8. **SE-048 — Keep a complete, owned API inventory (API9).** Every deployed version and endpoint appears in the inventory with an owner and a retirement date; an undocumented live endpoint is treated as an incident, not a backlog item.
9. **SE-049 — Validate third-party API data as untrusted input (API10).** Responses consumed from external APIs are schema-validated and range-checked before use or storage, exactly like user input.
10. **SE-050 — Scope, expire, and rotate API keys and tokens.** Each key carries the least privilege it needs, an expiry, and a tested rotation path; keys are issued per consumer, never shared across services.
11. **SE-051 — Ship an authorization test matrix.** Automated tests cover each role × each protected endpoint with own, foreign, and missing credentials, including cross-tenant ID swaps, and run in CI on every change.
12. **SE-052 — Return safe errors and log authorization failures.** Error responses expose no stack traces, internal IDs, or existence oracles beyond the status code; every denied object or function access is logged with principal, endpoint, and object ID.

## BAN list

- **BAN-SE-021 — Trusting client-supplied identity or ownership.** Banned: authorizing from a request-supplied `userId`, `ownerId`, or `isAdmin` field. Defeats: DET-CODE-027. Bad: `if (req.body.isAdmin) { deleteUser(...) }`. Instead: derive the principal and object ownership from the verified server-side session or token. Severity: BLOCK.
- **BAN-SE-022 — Returning the stored record as the response.** Banned: serializing the ORM/database object directly to the client. Defeats: DET-CODE-019. Bad: `res.json(user)` exposing `passwordHash` and `internalNotes`. Instead: pass every response through an explicit field-allowlist serializer. Severity: BLOCK.
- **BAN-SE-023 — Shipping an API secret in a client bundle.** Banned: embedding private, service-role, or signing keys in browser or mobile code, including "public" environment variables. Defeats: DET-INF-006. Bad: a service-role key in a `NEXT_PUBLIC_` variable. Instead: keep the secret server-side and let the client call a scoped backend endpoint. Severity: BLOCK.
- **BAN-SE-024 — Unbounded collection endpoints.** Banned: list, search, or export endpoints with no maximum result size, timeout, or quota. Defeats: DET-CODE-033. Bad: `GET /orders` returns every row to any authenticated key. Instead: enforce a maximum page size, a timeout, and a per-key quota on every collection endpoint. Severity: BLOCK.
- **BAN-SE-025 — Unrestricted fetching of user-supplied URLs.** Banned: server-side fetch of a caller-provided URL with no allowlist or network restriction. Defeats: DET-CODE-019. Bad: `await fetch(req.body.webhookUrl)` reaching `http://169.254.169.254/`. Instead: allowlist hosts, deny private/loopback/link-local ranges, and re-validate after redirects. Severity: BLOCK.

## Gates

- **G-SE-021 — Authorization matrix suite.** Verifies: SE-041, SE-042, SE-043, SE-051. Check: run the API authorization test suite in CI (`pytest tests/api/test_authz_matrix.py` or the project's equivalent), covering each role × endpoint with own, foreign, and missing credentials. Pass: every foreign or unauthenticated case returns 401/403 and leaks no record data. Fail: block shipment. Recorded in: progress.md.
- **G-SE-022 — API inventory diff.** Verifies: SE-048. Check: export the live route listing from the framework and diff it against the documented inventory in CI (`diff <(list-routes) docs/api-inventory.md`). Pass: zero undocumented or unowned routes. Fail: block shipment until the inventory or the deployment is corrected. Recorded in: progress.md.
- **G-SE-023 — Client bundle secret scan.** Verifies: SE-050. Check: scan the built client assets in CI (`gitleaks detect --source dist/client` or a grep for key/secret patterns over the bundle). Pass: no private key, token, or secret pattern found. Fail: block shipment and rotate any exposed credential. Recorded in: progress.md.
- **G-SE-024 — API scan plus SSRF probe.** Verifies: SE-044, SE-047, SE-052. Check: run a ZAP API scan against the OpenAPI definition in CI (`zap-api-scan.py -t openapi.yaml -f openapi`), then manually submit a link-local URL (`http://169.254.169.254/`) to every user-URL fetch feature. Pass: no high-severity scan alerts and every SSRF probe is rejected. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **Scanner-clean complacency.** The automated scan passes, so the API is declared secure — while BOLA stays untested because no scanner can judge ownership. Catch it: if the authorization matrix (G-SE-021) does not exist, the scan result proves nothing about authorization.
- **Happy-path-only security tests.** Tests cover the owner using their own data and stop there; no foreign-ID, lower-role, or missing-credential case exists. Catch it: count the negative cases in the suite — zero negative cases means zero authorization testing.
- **Shadow API versions.** `/v1` stays deployed and reachable after `/v2` launches, unpatched and absent from the inventory. Catch it: probe old version prefixes at every release and reconcile against the inventory.
- **Allowlist drift.** The SSRF or CORS allowlist grows by one-off exceptions until it includes internal or wildcard hosts. Catch it: review allowlist diffs like code, with an owner and an expiry on every exception.

## Examples

- [Example 1 — Object access scoped to the owner](examples/example-1.md) — violates/corrects SE-042.
- [Example 2 — Allowlist serializer instead of the raw record](examples/example-2.md) — violates/corrects SE-044.
- [Example 3 — SSRF-safe server-side fetch](examples/example-3.md) — violates/corrects SE-047.

## Recall anchors

- An ID in the request is a claim, not a permission.
- Scanners cannot judge authorization — the role × endpoint matrix can.
- Serialize by allowlist, in both directions.
- Every deployed endpoint is inventoried and owned, or it is an incident.
- Cap every endpoint: page size, body size, timeout, quota.

## Checklist

- [ ] Every non-public endpoint authenticates server-side (SE-041).
- [ ] Object access resolves ownership from the principal, never the request body (SE-042).
- [ ] Response serializers and request DTOs are explicit allowlists (SE-044).
- [ ] Page-size, body-size, timeout, and quota caps exist on all endpoints (SE-045).
- [ ] User-supplied URL fetches are allowlisted and private-range-denied (SE-047).
- [ ] Live routes diff clean against the API inventory (G-SE-022).
- [ ] Authorization matrix suite passes in CI, including cross-tenant swaps (G-SE-021).
- [ ] Built client bundles scan clean for secrets (G-SE-023).
