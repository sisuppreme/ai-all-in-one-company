# cdn-strategy

## Metadata

- **Owner department:** D6 DevOps & Deployment (DO)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://developers.cloudflare.com/waf/rate-limiting-rules/ ; https://wiki.mozilla.org/Security/Server_Side_TLS ; https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html
- **Depends on:** hosting, ssl-certificates
- **Feeds into:** reliability, scaling

## When to use / Do NOT use

- **Use when:** A public site or app serves static assets or cacheable responses, needs edge TLS and HTTPS redirect, or exposes login, reset, signup, or paid-cost API endpoints to the internet.
- **Do NOT use when:** The service is internal-only behind a VPN with no public traffic (edge controls belong to the network design), or the platform CDN is fully managed with no configurable cache or rate-limit rules — then record the platform defaults in hosting instead.

## Rules

1. **DO-181 — CDN in front of the origin.** All public traffic reaches the origin only through the CDN; DNS for public hostnames points at the CDN, never directly at the origin.
2. **DO-182 — Cache policy per content type, written down.** The project records one policy table: fingerprinted static assets cache long with `immutable`; HTML caches short or revalidates; authenticated and API responses are never publicly cached (`private`/`no-store`).
3. **DO-183 — Versioned assets, designed invalidation.** Static asset URLs carry a content fingerprint or version segment; a deploy either serves new fingerprints or purges the changed paths, so no user receives a page mixing old and new assets.
4. **DO-184 — Cache keys are explicit.** Each cache rule names what varies the key (path, selected query parameters, encoding); cookies and authorization headers never enter a public cache key.
5. **DO-185 — Rate-limit the abuse-prone paths at the edge.** Login, password-reset, signup, and paid-cost API paths have CDN/WAF rate-limit rules, stricter for unauthenticated traffic, returning 429 or a block when exceeded (DET-INF-023).
6. **DO-186 — Alert on sustained throttling.** Rate-limit events feed an alert: sustained rule hits from one source or a sharp rise in 429s notifies the operator through the project's alerting path.
7. **DO-187 — Shield the origin.** Where the platform allows it, the origin accepts traffic only from the CDN (IP allowlist, authenticated origin pull, or a private origin); a direct request to the origin IP or origin hostname is refused.
8. **DO-188 — HTTPS enforced at the edge.** The CDN terminates TLS with a valid certificate and 301-redirects every HTTP request to HTTPS on every route, including APIs (DET-INF-014).
9. **DO-189 — No mixed content by construction.** Every asset and API URL referenced by a page is HTTPS; no `http://` references ship in HTML, CSS, or JS (DET-INF-015).
10. **DO-190 — CDN configuration is versioned.** Cache rules, rate-limit rules, and redirect rules live in committed configuration (provider config file, Terraform, or an exported ruleset in the repo); console-only changes are back-ported the same day.

## BAN list

- **BAN-DO-091 — Unthrottled auth endpoints.** Banned: login, password-reset, or signup endpoints reachable with no edge rate-limit rule. Defeats: DET-INF-023. Bad: `/login` accepts unlimited POSTs per IP; credential stuffing runs unopposed. Instead: add a CDN/WAF rate-limit rule on the auth paths with a stricter unauthenticated tier that returns 429. Severity: BLOCK.
- **BAN-DO-092 — Plain-HTTP asset references.** Banned: shipping `http://` URLs for scripts, images, fonts, or API calls on an HTTPS page. Defeats: DET-INF-015. Bad: `<script src="http://cdn.example.com/app.js">` triggers mixed-content warnings and downgrade risk. Instead: reference every asset over HTTPS (or a scheme-relative URL behind the CDN) and fix the URL at the source. Severity: BLOCK.
- **BAN-DO-093 — Origin open to direct traffic.** Banned: the origin accepts requests from any source IP, so all edge rules are bypassable via the origin hostname or IP. Defeats: DET-INF-023. Bad: an attacker skips the CDN and hits the unthrottled origin login directly. Instead: restrict the origin to CDN traffic only (allowlist, authenticated origin pull, or private origin). Severity: BLOCK.
- **BAN-DO-094 — No HTTP-to-HTTPS redirect at the edge.** Banned: HTTP requests served content or a CDN default page instead of redirecting to HTTPS. Defeats: DET-INF-014. Bad: `curl -sI http://example.com` returns 200 with the page over plain HTTP. Instead: configure an edge 301 redirect from HTTP to HTTPS for every route. Severity: BLOCK.

## Gates

- **G-DO-091 — Header audit.** Verifies: DO-182, DO-188. Check: `curl -sI https://<domain>/`, `curl -sI https://<domain>/<fingerprinted-asset>`, and `curl -sI http://<domain>/`; compare `Cache-Control` against the DO-182 policy table and confirm the HTTP request returns a 301 to `https://`. Pass: every sampled header matches the policy and the redirect is present. Fail: block shipment. Recorded in: progress.md.
- **G-DO-092 — Throttle test.** Verifies: DO-185. Check: from one test IP, script repeated login POSTs past the rule threshold (e.g., a loop of `curl -s -o /dev/null -w "%{http_code}\n" -X POST https://<domain>/login`) and confirm 429 or a block response engages. Pass: throttling engages at or below the configured threshold. Fail: block shipment. Recorded in: progress.md.
- **G-DO-093 — Origin bypass test.** Verifies: DO-181, DO-187. Check: request the origin directly (`curl -sk https://<origin-host>/ --resolve <domain>:443:<origin-ip>`) and confirm refusal (403, connection failure, or CDN-only error). Pass: direct origin access is refused. Fail: block shipment. Recorded in: progress.md.
- **G-DO-094 — Mixed-content scan.** Verifies: DO-189. Check: grep the built HTML/CSS/JS output for `http://` asset references (`grep -rEo 'src="http://[^"]+"|href="http://[^"]+"|url\(http://' dist/`) and load key pages with the browser console open. Pass: zero `http://` asset references and zero mixed-content warnings. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **Vendor-default TTL on everything.** The CDN preset (one TTL for all content) is left in place because pages "feel fast"; catch it by comparing live headers against the DO-182 policy table before launch.
- **Purge-everything deploys.** Every deploy flushes the whole cache, causing an origin stampede and a slow first hour; catch it when the deploy script contains a full-zone purge instead of fingerprint rollover or path-scoped purges.
- **Cached error pages.** A brief origin outage gets cached at the edge and keeps serving 5xx after recovery; catch it by confirming error responses carry `no-store` or a seconds-long TTL in the policy table.
- **Rate limit in permanent log-only mode.** The rule exists but is set to simulate/log forever "to be safe"; catch it by checking the rule action is block/429, not log, at the G-DO-092 throttle test.

## Examples

- [Example 1 — Per-type cache headers](examples/example-1.md) — violates/corrects DO-182, DO-183.
- [Example 2 — Edge rate limiting for auth paths](examples/example-2.md) — violates/corrects DO-185.
- [Example 3 — Shielded origin, HTTPS-only assets](examples/example-3.md) — violates/corrects DO-187, DO-189.

## Recall anchors

- Fingerprinted assets: long and immutable. HTML: short or revalidated. Authenticated: never public.
- A CDN the origin doesn't require is decoration — shield the origin.
- Login, reset, signup, paid-cost paths: throttled at the edge, stricter when unauthenticated.
- If a deploy can serve a mixed old/new page, the invalidation design is missing.
- Every asset URL is HTTPS; HTTP only ever answers with a 301.

## Checklist

- [ ] Policy table exists covering static assets, HTML, and authenticated/API responses (DO-182).
- [ ] Asset URLs are fingerprinted or versioned, and the deploy invalidation path is named (DO-183).
- [ ] Rate-limit rules cover login, reset, signup, and paid-cost paths, with alerting on sustained hits (DO-185, DO-186).
- [ ] Direct origin access is refused in the G-DO-093 bypass test (DO-187).
- [ ] Header audit passes: cache headers match policy and HTTP 301-redirects to HTTPS (G-DO-091).
- [ ] Throttle test returns 429/block past the threshold (G-DO-092).
- [ ] Mixed-content scan finds zero `http://` asset references (G-DO-094).
- [ ] CDN cache, rate-limit, and redirect rules are committed in the repo (DO-190).
