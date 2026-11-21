# security-headers

## Metadata

- **Owner department:** D7 Security (SE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** OWASP Secure Headers Project, https://owasp.org/www-project-secure-headers/
- **Depends on:** encryption
- **Feeds into:** security-audit

## When to use / Do NOT use

- **Use when:** defining, setting, or reviewing the HTTP response header policy of a web application — CSP, HSTS, clickjacking, MIME-sniffing, referrer, and permissions headers — at the edge, in middleware, or in framework configuration.
- **Do NOT use when:** the work is TLS protocol and certificate configuration (use encryption and ssl-certificates), cookie attributes on session cookies (use session-security), or a formal ASVS verification pass over all controls (use security-audit).

## Rules

1. **SE-161 — One written header sheet per project.** Every expected header and its exact value are recorded once in the project's header sheet before deployment; the runtime configuration is generated or checked from it, and the assertion gate diffs the deployed site against it.
2. **SE-162 — Headers are set once, centrally.** The policy is applied at one point — edge configuration or a single middleware — so every route inherits it; no route, controller, or template sets or overrides a security header locally.
3. **SE-163 — CSP is an allowlist of the app's real origins.** Each CSP directive names only origins the app actually loads from, inventoried from the built pages; `script-src` carries no `unsafe-inline` and no wildcard on any app serving authenticated pages.
4. **SE-164 — CSP ships report-only first, then enforced.** A new or changed CSP runs in report-only mode with a monitored report endpoint until violation reports are clean, then switches to enforcing; report-only has a recorded end date and is never the final state.
5. **SE-165 — HSTS only after HTTPS is universal.** Strict-Transport-Security is enabled only once every host it will cover serves valid HTTPS; `includeSubDomains` and preload submission are separate, deliberate decisions recorded in the header sheet with their date.
6. **SE-166 — `nosniff` on every response.** X-Content-Type-Options is set to `nosniff` for pages, APIs, and static assets alike, so browsers never MIME-sniff a response away from its declared type.
7. **SE-167 — Clickjacking defense is CSP `frame-ancestors`.** Framing is controlled by the `frame-ancestors` directive set to the origins allowed to embed the app (`'none'` when none are); X-Frame-Options is sent only as a legacy fallback and never as the sole control.
8. **SE-168 — Referrer-Policy and Permissions-Policy are set deliberately.** Referrer-Policy is chosen and recorded (default `strict-origin-when-cross-origin` unless the sheet says otherwise), and Permissions-Policy disables every device API the app does not use (camera, microphone, geolocation, payment handlers).
9. **SE-169 — Error and API responses carry the same policy.** 4xx/5xx responses, redirects, and JSON API responses carry the identical header set as HTML pages; a policy present only on successful page renders is incomplete.
10. **SE-170 — Framework and server banners are suppressed.** `X-Powered-By` and server version banners are removed or reduced to the bare product name on production responses; the deployed response set is checked, not the framework's documentation.
11. **SE-171 — Weakening a header is a control change.** Removing a header, widening a CSP source, or shortening an HSTS max-age goes through the same review as removing any other security control, and the header sheet and gate expectations are updated in the same change.

## BAN list

- **BAN-SE-081 — Tutorial-copied CSP.** Banned: shipping a CSP copied from a tutorial or another project that permits CDNs, script hosts, or `unsafe-inline` the app does not use. Defeats: DET-CODE-020. Bad: `script-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net https://unpkg.com` on an app that loads no script from either CDN. Instead: inventory the origins the built app actually loads from and allowlist exactly those (SE-163). Severity: BLOCK.
- **BAN-SE-082 — CSP parked in report-only forever.** Banned: leaving Content-Security-Policy-Report-Only in place with no enforcement date, so violations are observed but never blocked. Defeats: DET-CODE-020. Bad: report-only mode still active six months after launch, with the report endpoint unmonitored. Instead: monitor reports until clean, then enforce by the recorded date (SE-164). Severity: BLOCK.
- **BAN-SE-083 — Headers set only by the HTML layer.** Banned: applying the header policy in page rendering or a web-framework after-request hook that API routes and error handlers bypass. Defeats: DET-INF-022. Bad: pages carry CSP and HSTS, but `/api/*` JSON responses and the 500 error page carry none. Instead: set the policy once at the edge or in middleware that wraps every response, errors included (SE-162, SE-169). Severity: BLOCK.
- **BAN-SE-084 — HSTS switched on before HTTPS is universal.** Banned: sending Strict-Transport-Security with `includeSubDomains` or submitting the domain for preload while any covered subdomain still serves plain HTTP or an invalid certificate. Defeats: DET-INF-014. Bad: preload submitted while `legacy.example.com` is still HTTP-only, locking its users out for the preload duration. Instead: confirm every covered host serves valid HTTPS first, then enable HSTS and record the subdomain/preload decision (SE-165). Severity: BLOCK.
- **BAN-SE-085 — Production headers assumed from local defaults.** Banned: treating the header set as done because the framework "sets secure defaults," verified only against a local dev server. Defeats: DET-INF-022. Bad: the dev server sends a starter CSP from a plugin, but the production edge strips it and nobody checks the deployed site. Instead: assert the deployed production responses against the header sheet with the release gate (SE-161, G-SE-081). Severity: BLOCK.

## Gates

- **G-SE-081 — Deployed header assertion (automated).** Verifies: SE-161, SE-162, SE-166, SE-169. Check: release script runs `curl -sI` against the production URL for a page route, an API route, and a forced-error route, and diffs the returned security headers against the header sheet. Pass: all three responses carry every sheet header with the exact expected value. Fail: block shipment. Recorded in: progress.md.
- **G-SE-082 — CSP quality lint (automated, CI).** Verifies: SE-163, SE-164. Check: CI script parses the configured CSP and fails on `unsafe-inline` or `*` in `script-src`/`default-src`, on any source origin absent from the sheet's origin inventory, and on report-only mode whose recorded end date has passed. Pass: none of the three conditions present. Fail: block merge. Recorded in: progress.md.
- **G-SE-083 — HSTS precondition check (automated).** Verifies: SE-165. Check: before any change enabling `includeSubDomains` or preload, a script requests `https://` for the apex and every subdomain in the sheet and requires a valid certificate and a 2xx/3xx response from each. Pass: every covered host passes. Fail: block the HSTS change. Recorded in: progress.md.
- **G-SE-084 — CSP violation report review.** Verifies: SE-164. Check: after each deploy, the CSP report endpoint's violations for the release window are reviewed; each new blocked-uri source is triaged as legitimate (sheet updated) or hostile/erroneous (left blocked). Pass: zero unreviewed violation sources from the current release. Fail: warn and hold CSP changes until reviewed. Recorded in: progress.md.

## Anti-patterns

- **Grade-chasing.** Tuning headers to raise an automated scanner score while the CSP still allows origins the app never uses — the score improves, the policy does not; catch it by diffing the CSP against the origin inventory, not the grade.
- **Per-route header drift.** Individual routes add or relax headers locally until responses differ across the app; the tell is two routes returning different CSPs with no sheet entry explaining why.
- **Decorative CSP.** A policy so broad (`default-src *`, `unsafe-inline` everywhere) that it blocks nothing real but is cited in reviews as "we have a CSP"; catch it by asking which concrete script injection it would stop.
- **Staging-prod mismatch shrugged off.** Headers verified on staging, where a plugin or platform default supplies them, while production is served by a different layer that does not — visible when the gate's curl output is from any host other than production.

## Examples

- [Example 1 — CSP rebuilt as a real-origin allowlist](examples/example-1.md) — violates/corrects SE-163.
- [Example 2 — Headers moved from the page layer to one central middleware](examples/example-2.md) — violates/corrects SE-162, SE-169.
- [Example 3 — HSTS enabled in safe stages](examples/example-3.md) — violates/corrects SE-165.

## Recall anchors

- One sheet, one place: headers are written down once and set centrally.
- CSP allowlists real origins — a copied policy is a finding.
- Report-only is a phase with an end date, never the destination.
- HSTS after HTTPS is universal, never before.
- Errors and APIs carry the same headers as pages.

## Checklist

- [ ] The project header sheet lists every expected header and exact value, and production config matches it (SE-161).
- [ ] Headers are set at one central point; no route overrides them locally (SE-162).
- [ ] CSP names only inventoried real origins, with no `unsafe-inline` or wildcard in `script-src` (SE-163).
- [ ] CSP is enforcing, or report-only with a monitored endpoint and a recorded enforcement date (SE-164).
- [ ] HSTS was enabled only after every covered host served valid HTTPS; the `includeSubDomains`/preload decision is recorded (SE-165).
- [ ] `nosniff`, `frame-ancestors`, Referrer-Policy, and Permissions-Policy are set as the sheet specifies (SE-166, SE-167, SE-168).
- [ ] Page, API, and error responses all carry the policy, and `curl -sI` output shows no framework or version banners (SE-169, SE-170).
- [ ] G-SE-081 and G-SE-082 pass on the deployed production host (SE-171).
