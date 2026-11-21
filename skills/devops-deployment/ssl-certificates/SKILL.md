# ssl-certificates

## Metadata

- **Owner department:** D6 DevOps & Deployment (DO)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Mozilla, "Server Side TLS" — https://wiki.mozilla.org/Security/Server_Side_TLS ; OWASP, "Transport Layer Protection Cheat Sheet" — https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html
- **Depends on:** domains-dns, hosting
- **Feeds into:** cdn-strategy, reliability

## When to use / Do NOT use

- **Use when:** any service becomes reachable over a network — first HTTPS setup, a new domain or subdomain goes live, a certificate is issued or replaced, TLS settings change, or a scan flags the TLS configuration.
- **Do NOT use when:** the service is local-only or reachable solely inside a private network with no public route (record that fact in the project notes instead). Do not hand-edit cipher suites outside a maintained profile — that is this skill's configuration step, not improvisation.

## Rules

1. **DO-221 — HTTPS everywhere, automated.** Every public hostname serves a valid certificate obtained through provider-managed issuance or an ACME client (Let's Encrypt via Certbot/acme.sh). A certificate installed by hand-upload with no renewal path does not satisfy this rule.
2. **DO-222 — Redirect all HTTP.** Every route, including API routes, answers plain HTTP with a 301 redirect to the same path over HTTPS. No route serves content or accepts credentials over HTTP.
3. **DO-223 — HSTS after stability.** HSTS is enabled only after HTTPS has been verified working on every route; the header is present on HTTPS responses once enabled and is never enabled as part of the first, untested TLS change.
4. **DO-224 — Mozilla Intermediate profile.** The server TLS configuration follows the Mozilla Intermediate profile: TLS 1.2 and 1.3 only, with the profile's cipher list. Deviations are listed in the project notes with a reason.
5. **DO-225 — Legacy protocols need an expiry.** TLS 1.0/1.1 or a legacy cipher may be enabled only for a named legacy client need, with a documented exception and an expiry date in the project notes. An exception without a date is removed.
6. **DO-226 — Renewal runs unattended.** Renewal is scheduled (ACME client timer or provider auto-renew) and a post-renewal hook reloads or restarts the server so the renewed certificate is actually served, not just stored on disk.
7. **DO-227 — Renewal is proven by dry-run.** `certbot renew --dry-run` (or the provider equivalent) passes at initial setup and after any server, DNS, or web-server change. An untested renewal is treated as no renewal.
8. **DO-228 — Expiry alert is the backstop.** An expiry monitor alerts at least 30 days before the served certificate's not-after date. The alert exists to catch automation failure; it is never the renewal mechanism itself.
9. **DO-229 — Zero mixed content.** No page served over HTTPS references an `http://` asset, script, stylesheet, or API endpoint. Asset URLs are HTTPS or scheme-relative behind the TLS terminator.
10. **DO-230 — Challenge type is chosen deliberately.** Wildcard certificates use DNS-01; per-host certificates use HTTP-01 or the web-server plugin. The chosen challenge and its credential (DNS API token scope) are recorded in the project notes.
11. **DO-231 — Full chain served.** The server presents the complete certificate chain (leaf plus intermediates); a scan or `openssl s_client -showcerts` shows no missing-intermediate error on any client.
12. **DO-232 — Scan after every TLS change.** An external scan (SSL Labs or `testssl.sh`) runs at launch and after any TLS configuration change; the grade and enabled protocol list are recorded in progress.md.

## BAN list

- **BAN-DO-111 — Manual certificate with calendar renewal.** Banned: a certificate installed once by hand (one-off Certbot run or uploaded commercial cert) with renewal left to memory or a calendar reminder. Defeats: DET-INF-016. Bad: the launch checklist says "renew cert in March" and no ACME timer or managed renewal exists. Instead: issue through an ACME client or provider-managed certificate with unattended renewal, a reload hook, and a dry-run proof. Severity: BLOCK.
- **BAN-DO-112 — HTTP left serving.** Banned: the site answers on plain HTTP without a redirect, or login/API routes accept HTTP. Defeats: DET-INF-014. Bad: `curl -sI http://example.com/login` returns 200 and the login form posts over HTTP. Instead: 301-redirect every HTTP route to its HTTPS equivalent and verify no route serves over HTTP. Severity: BLOCK.
- **BAN-DO-113 — Legacy TLS shipped unexamined.** Banned: default server TLS settings from an old base image or tutorial shipped as-is, leaving TLS 1.0/1.1 or obsolete ciphers enabled with no documented exception. Defeats: DET-INF-015. Bad: `testssl.sh` lists TLS 1.0 and 3DES as enabled and nobody can say why. Instead: apply the Mozilla Intermediate profile; keep any legacy protocol only as a dated, documented exception. Severity: BLOCK.
- **BAN-DO-114 — Hardcoded http:// references.** Banned: `http://` asset, script, or API URLs hardcoded in pages or configuration served over HTTPS. Defeats: DET-INF-015. Bad: the HTTPS homepage loads `http://cdn.example.com/app.js`, triggering mixed-content warnings. Instead: use the HTTPS URL (or scheme-relative URL behind the terminator) for every referenced resource. Severity: WARN.

## Gates

- **G-DO-111 — External TLS scan.** Verifies: DO-224, DO-225, DO-231, DO-232. Check: run `testssl.sh <domain>` (or the SSL Labs scan) at launch and after any TLS change. Pass: TLS 1.2/1.3 only (any legacy protocol matches a dated exception in the project notes), full chain presented, grade and protocol list recorded. Fail: block shipment until the configuration matches the Mozilla Intermediate profile. Before a production environment is provisioned, this gate's disposition is a recorded provisioning waiver per the §6.3 protocol; it unblocks when a production domain is provisioned and the deployed service is reachable over public TLS. Recorded in: progress.md.
- **G-DO-112 — Redirect and HSTS probe (automated).** Verifies: DO-222, DO-223. Check: `curl -sI http://<domain>` and `curl -sI http://<domain>/login` return 301 to the `https://` URL; `curl -sI https://<domain>` shows the `Strict-Transport-Security` header once HTTPS is stable. Pass: every probed route redirects and the header is present. Fail: block shipment. Recorded in: progress.md.
- **G-DO-113 — Renewal proof.** Verifies: DO-221, DO-226, DO-227. Check: `certbot renew --dry-run` (or provider equivalent) exits 0, and the renewal timer/managed setting plus reload hook are shown in the server configuration. Pass: dry-run succeeds and the unattended renewal path is visible. Fail: block shipment — an unproven renewal is an unscheduled outage. Recorded in: progress.md.
- **G-DO-114 — Expiry and mixed-content check (automated).** Verifies: DO-228, DO-229. Check: `echo | openssl s_client -connect <domain>:443 -servername <domain> 2>/dev/null | openssl x509 -noout -enddate` shows more than 30 days remaining, an expiry alert rule exists at the 30-day threshold, and a crawl of key pages (browser console or `grep -r "http://" templates/`) finds zero `http://` resource references. Pass: all three conditions hold. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **Expiry-alert complacency.** The 30-day alert exists, so nobody checks whether auto-renewal actually works — until the alert fires during a holiday. Catch it: the dry-run gate (G-DO-113) is the mechanism check; the alert is only the backstop.
- **Cert renewed, server stale.** Renewal succeeds on disk but the web server keeps serving the old certificate because no reload hook runs. Catch it: after any renewal change, compare the served certificate's dates against the on-disk certificate.
- **HSTS on day one.** HSTS is enabled in the same change that first turns on HTTPS, locking in a misconfiguration before a single route is verified. Catch it: HSTS ships only in a later change, after the redirect probe passes.
- **Wildcard by default.** A wildcard certificate is issued because it was convenient, widening the blast radius of one private key across every subdomain. Catch it: per-host certificates are the default; a wildcard needs the DNS-01 decision recorded under DO-230.

## Examples

- [Example 1 — Manual cert and calendar renewal](examples/example-1.md) — violates/corrects DO-221, DO-226, DO-227.
- [Example 2 — HTTP left serving beside HTTPS](examples/example-2.md) — violates/corrects DO-222, DO-223.
- [Example 3 — Tutorial TLS defaults and an http:// script](examples/example-3.md) — violates/corrects DO-224, DO-229.

## Recall anchors

- Automate issuance and renewal; the expiry alert is the backstop, not the mechanism.
- Redirect every HTTP route — APIs and logins included.
- Mozilla Intermediate: TLS 1.2+ only; legacy needs a dated exception.
- Renewal is proven by dry-run, or it does not exist.
- Zero `http://` references on an HTTPS page.

## Checklist

- [ ] Certificate is provider-managed or ACME-issued, with unattended renewal and a reload hook (DO-221, DO-226).
- [ ] `certbot renew --dry-run` (or provider equivalent) passes and is re-run after server changes (DO-227).
- [ ] Every HTTP route 301-redirects to HTTPS; HSTS enabled only after HTTPS verified stable (DO-222, DO-223).
- [ ] Configuration matches the Mozilla Intermediate profile; any legacy protocol has a dated exception (DO-224, DO-225).
- [ ] Expiry alert set at 30 days and served certificate shows more than 30 days remaining (DO-228).
- [ ] No `http://` asset or API references on HTTPS pages (DO-229).
- [ ] Challenge type (DNS-01 for wildcards, HTTP-01/plugin per host) recorded in the project notes (DO-230).
- [ ] External scan grade and protocol list recorded in progress.md after the latest TLS change (DO-232).
