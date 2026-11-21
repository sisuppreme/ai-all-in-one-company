# owasp

## Metadata

- **Owner department:** D7 Security (SE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** OWASP Top 10:2025, https://owasp.org/www-project-top-ten/ ; OWASP ASVS 5.0.0, https://asvs.owasp.org/
- **Depends on:** none — standalone: the OWASP Top 10:2025 is an external standard applied directly to the application's own code and configuration; no other skill's output is an input. Its control checklist feeds security-audit, api-security, auth-hardening, and supply-chain.
- **Feeds into:** security-audit, api-security, auth-hardening, supply-chain

## When to use / Do NOT use

- **Use when:** building or reviewing any web application feature, and at every release, to run the OWASP Top 10:2025 as a control-and-test checklist.
- **Do NOT use when:** the task is a formal verification pass against ASVS (use security-audit) or adversarial testing of a running system (use penetration-testing, under its authorization gate).

## Rules

1. **SE-001 — Top 10 checklist per release.** For each OWASP Top 10:2025 category (A01–A10), the release record names the control this project implements, where it lives in code or config, and the test that proves it. A category marked not applicable carries a written reason; a blank category fails the release.
2. **SE-002 — Parameterize every query.** All SQL uses bound parameters or the ORM's parameter binding; request values are never concatenated or interpolated into query strings (A05:2025).
3. **SE-003 — Validate input server-side, by allowlist.** Every request body, query parameter, and upload is checked against a schema (type, range, size, format) on the server before it is stored, queried, or rendered; invalid input gets a structured 4xx (A05:2025).
4. **SE-004 — Authorize on the server, per object and function.** Every endpoint checks the authenticated caller's right to the specific object and function requested; hiding a control in the UI is not an authorization check (A01:2025).
5. **SE-005 — Errors fail closed.** An exception in an authorization, payment, or moderation path denies the action and logs the event; it never falls through to success (A10:2025).
6. **SE-006 — No control disabled by configuration in production.** TLS verification, CORS, authentication, and framework security flags ship enabled; a disabled control in the production config is a release blocker (A02:2025).
7. **SE-007 — No internals in client responses.** Error responses contain a generic message and a correlation ID only — never a stack trace, SQL text, file path, or framework banner (A02/A10:2025).
8. **SE-008 — Standard cryptography only.** Passwords are hashed with a dedicated password KDF (per auth-hardening); sensitive data at rest uses AEAD encryption (per encryption); no hand-rolled ciphers, modes, or key handling (A04:2025).
9. **SE-009 — Log security events, alert on anomalies.** Authentication outcomes, authorization denials, privilege changes, and validation-rejection spikes are logged with actor and timestamp, and alerting rules exist for them (A09:2025).
10. **SE-010 — Meet the ASVS floor.** A public application meets OWASP ASVS 5.0.0 Level 1 at minimum; anything holding payments or sensitive personal data meets Level 2. Requirements are cited with versioned IDs (e.g. `v5.0.0-…`).
11. **SE-011 — Debug and admin surfaces off in production.** Framework debug modes are disabled by environment config, and admin, metrics, and diagnostic endpoints require authentication and network restriction or do not exist in the production build (A02:2025).
12. **SE-012 — Cite standards with versions.** Every reference to a standard carries its edition — `A01:2025`, `API1:2023`, `v5.0.0-…` — and the checklist is re-checked against the current edition at each major release.

## BAN list

- **BAN-SE-001 — String-built SQL.** Banned: constructing a query by concatenation or template interpolation of request values. Defeats: DET-CODE-017. Bad: `db.query("SELECT * FROM orders WHERE id = " + req.params.id)`. Instead: use a bound parameter — `db.query("SELECT * FROM orders WHERE id = $1", [req.params.id])`. Severity: BLOCK.
- **BAN-SE-002 — Fail-open exception handler.** Banned: catching an exception in an authorization, payment, or moderation path and continuing as if the operation succeeded. Defeats: DET-CODE-005. Bad: `try { await checkAccess(user, doc); } catch { /* ignore */ } render(doc);`. Instead: deny on error — on exception, return 403, log the event, and stop. Severity: BLOCK.
- **BAN-SE-003 — Control disabled to make it run.** Banned: shipping production config that disables a security control (TLS `verify=False`, CORS `*` with credentials, auth checks off, debug on). Defeats: DET-CODE-020. Bad: `process.env.NODE_TLS_REJECT_UNAUTHORIZED = "0"` in the production profile. Instead: fix the underlying certificate, origin, or credential problem and ship with the control enabled. Severity: BLOCK.
- **BAN-SE-004 — Stack trace to the client.** Banned: returning exception details, stack traces, or SQL errors in an HTTP response, or leaving framework debug mode reachable in production. Defeats: DET-INF-021. Bad: `res.status(500).json({ error: err.stack })`. Instead: log the full error server-side with a correlation ID and return `{ error: "Internal error", id: <correlation-id> }`. Severity: BLOCK.
- **BAN-SE-005 — Browser-only validation.** Banned: relying on client-side form checks as the only validation of data the server stores, queries, or renders. Defeats: DET-CODE-019. Bad: an email field checked only by an HTML `pattern` attribute, then written to the database unchecked. Instead: validate the same field against a server-side schema on every request and reject failures with a structured 4xx. Severity: BLOCK.

## Gates

- **G-SE-001 — ZAP baseline scan.** Verifies: SE-001, SE-007, SE-011. Check: run the OWASP ZAP baseline scan against the staging deployment in CI (`docker run --rm ghcr.io/zaproxy/zaproxy:stable zap-baseline.py -t https://staging.<project-domain>` or the project's pinned equivalent). Where neither Docker nor a staging deployment exists, the substitute evidence path is this skill's own compensating gates — G-SE-002 (disabled-control grep and config read), G-SE-003 (Top 10 checklist review), and G-SE-004 (production surface probe) — performed and recorded in full, plus a recorded waiver per §6.3 naming the constraint; the automated ZAP scan remains required before any public launch. Pass: zero high-severity findings. Fail: block shipment until findings are fixed or formally accepted with an owner and date. Recorded in: progress.md.
- **G-SE-002 — Disabled-control grep.** Verifies: SE-006. Check: `grep -rnE "verify\s*=\s*False|rejectUnauthorized:\s*false|NODE_TLS_REJECT_UNAUTHORIZED|Access-Control-Allow-Origin:\s*'\*'" src/ config/` plus a manual read of the production config profile. Pass: no hits outside local-development config that cannot reach production. Fail: block shipment. Recorded in: progress.md.
- **G-SE-003 — Top 10 checklist review.** Verifies: SE-001, SE-010, SE-012. Check: manual, checklist-driven — walk the release's Top 10 record line by line; each category shows a control, a code/config location, a test, and versioned ASVS IDs where cited. Pass: all ten categories complete, N/A entries carry written reasons. Fail: return the release for completion. Recorded in: progress.md.
- **G-SE-004 — Production surface probe.** Verifies: SE-007, SE-011. Check: `curl -s -o /dev/null -w "%{http_code}" https://<prod-domain>/.env` and the same for `/.git/config` and the framework debug path, then trigger one bad request and read the error body. Pass: probes return 403/404 and the error body contains no stack trace, SQL, or file paths. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **Poster compliance.** The Top 10 is cited in a README or slide deck, but no release record maps categories to controls and tests. Catch it: ask for the checklist; if it does not exist, the citation is decoration.
- **Scanner-says-clean.** A passing ZAP or SAST run is treated as proof the app is secure. Scanners cannot judge per-object authorization or business-flow abuse; if no per-role authorization test exists, the clean scan is covering the highest-risk gap.
- **Escape-by-hand.** Injection is "handled" with manual string escaping or a denylist regex instead of parameterization and allowlists. Catch it: search for escape/replace chains near query or render calls.
- **Version-free citation.** Text says "per OWASP" or cites an ASVS number with no edition. ASVS 5.0 renumbered nearly every requirement from 4.0.3, so an unversioned citation is unverifiable.

## Examples

- [Example 1 — Parameterized query](examples/example-1.md) — violates/corrects SE-002 (BAN-SE-001).
- [Example 2 — Fail-closed authorization](examples/example-2.md) — violates/corrects SE-005 (BAN-SE-002).
- [Example 3 — Generic production errors](examples/example-3.md) — violates/corrects SE-007 (BAN-SE-004).

## Recall anchors

- Every Top 10 category: a named control, a named test, or a written N/A.
- Bind parameters; never build SQL from request strings.
- When a security check throws, the answer is no.
- The client sees a generic error and an ID — nothing else.
- Cite the edition: A01:2025, v5.0.0 — unversioned claims rot.

## Checklist

- [ ] Top 10 record for this release lists a control and a test for all ten categories (SE-001).
- [ ] No query in the change is built by concatenation or interpolation (SE-002).
- [ ] New inputs are validated server-side against a schema (SE-003).
- [ ] New endpoints authorize per object and per function on the server (SE-004).
- [ ] Error paths in auth, payment, and moderation code deny on exception (SE-005).
- [ ] Production config has no disabled security control and no debug surface (SE-006, SE-011).
- [ ] ZAP baseline shows zero high findings; surface probe and grep gates pass (G-SE-001, G-SE-002, G-SE-004).
