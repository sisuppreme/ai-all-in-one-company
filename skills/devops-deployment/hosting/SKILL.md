# hosting

## Metadata

- **Owner department:** D6 DevOps & Deployment (DO)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Netlify Docs, "Create deploys" — https://docs.Netlify.com/site-deploys/create-deploys ; Render Docs, "Deploy for Free" — https://render.com/docs/free ; OWASP Logging Cheat Sheet — https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html ; Cloudflare Docs, "Rate limiting rules" — https://developers.cloudflare.com/waf/rate-limiting-rules/ ; Kubernetes Docs, liveness/readiness probes — https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/ ; AWS Well-Architected Reliability Pillar — https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html
- **Depends on:** infrastructure-as-code, deployment-strategies, free-tiers
- **Feeds into:** reliability, domains-dns, ssl-certificates, scaling

## When to use / Do NOT use

- **Use when:** choosing or changing where a web application runs, promoting a deployment from validation to production use, or auditing an existing host against its recorded limits.
- **Do NOT use when:** deciding how a release is rolled out (deployment-strategies), accounting for a provider's free-tier caps in depth (free-tiers), or configuring DNS records and certificates themselves (domains-dns, ssl-certificates).

## Rules

1. **DO-141 — The host decision is recorded.** The hosting record names the provider and plan, region(s), scaling behavior, sleep policy, bandwidth and build caps, and the exit path, each with the date it was checked against the provider's own documentation. A host chosen without this record is not chosen yet.
2. **DO-142 — Every deployment carries a posture tier.** Each deployment is labeled validation posture or production posture in the hosting record. The record names the promotion trigger (first real user, first payment, first availability commitment) and lists which detection parameters are knowingly waived at validation posture.
3. **DO-143 — No unrecorded single point of failure.** A production-posture deployment with availability requirements does not run as a single instance with its database on the same host unless that risk is a recorded decision in the hosting record with a named exit path.
4. **DO-144 — Health checks reflect the ability to serve.** The app exposes a readiness endpoint that fails when a required dependency (database, cache, queue) is unreachable, and the platform's health check points at it. A probe aimed at the homepage or any static page does not satisfy this rule.
5. **DO-145 — Ephemeral filesystems hold no state.** On a platform whose filesystem is reset by redeploys or spin-downs, user uploads and the application database live in external stores (object storage, managed database), never in local files or a local database file.
6. **DO-146 — Platform config is the IaC of record.** The provider's config file (for example `netlify.toml`, `render.yaml`, `fly.toml`, `vercel.json`) is committed to the repo, and the console matches it. Any difference between console and committed config is drift and is reconciled the same day it is found.
7. **DO-147 — Debug and admin surfaces stay closed.** Production runs with framework debug mode off, error responses contain no stack traces, and `/.git`, `/.env`, admin, and metrics paths are unreachable publicly or sit behind authentication plus network restriction.
8. **DO-148 — Host defaults are hardened.** Directory listing is off, server and framework version banners are suppressed, default welcome pages and unused virtual hosts are removed, and only the ports the application needs are open.
9. **DO-149 — Auth endpoints are throttled at the edge.** Rate-limit rules at the CDN, WAF, or gateway cover login, password-reset, and signup paths before launch, with stricter limits for unauthenticated traffic.
10. **DO-150 — Production is a separate environment.** Production has its own data store and its own credentials; staging and production resolve to different database hosts, and production data is never the test fixture.
11. **DO-151 — Production is verified from outside.** After every deploy, the public production URL is loaded over valid HTTPS from a network other than the deploy network, and the live deployment's commit SHA is confirmed equal to the repo HEAD and written into progress.md.
12. **DO-152 — The host-limit sheet stays current.** Caps that can stop the app (sleep behavior, bandwidth, build minutes, instance hours, expiring resources such as free databases) are recorded with their expiry or reset dates and re-checked against provider documentation at least every 90 days.

## BAN list

- **BAN-DO-071 — The localhost launch.** Banned: declaring an app launched from a localhost screenshot or a provider's "deployed" badge without an external check of the public URL. Defeats: DET-INF-003. Bad: the launch is announced with a screenshot of localhost:3000 while the production URL still serves the placeholder page. Instead: load the public production URL from a second network over HTTPS and record the live commit SHA before calling anything launched. Severity: BLOCK.
- **BAN-DO-072 — The unrecorded single box.** Banned: running a production deployment as one instance with its database on the same host, with no recorded risk decision and no exit path. Defeats: DET-INF-019. Bad: one VPS runs the app and its PostgreSQL; a single disk failure takes the product and its data down together, and nobody ever wrote the risk down. Instead: move the database to a managed store or separate host, or record the accepted risk and its exit path in the hosting record. Severity: BLOCK.
- **BAN-DO-073 — The homepage health check.** Banned: pointing the platform health check at the homepage or a static page that cannot fail. Defeats: DET-INF-020. Bad: the probe hits `/`, which returns 200 from cache while the database is down, so the platform never restarts or drains the broken instance. Instead: expose a readiness endpoint that checks the app's dependencies and point the platform probe at it. Severity: BLOCK.
- **BAN-DO-074 — Debug shipped to production.** Banned: deploying with framework debug mode enabled, or with `/.git` or `/.env` reachable on the public host. Defeats: DET-INF-021. Bad: the development config is copied to production verbatim, and an error page shows visitors a full stack trace with file paths. Instead: disable debug by environment configuration in production and block the sensitive paths at the host. Severity: BLOCK.
- **BAN-DO-075 — Unthrottled auth at launch.** Banned: launching on a host with no edge rate limit on login, password-reset, or signup endpoints. Defeats: DET-INF-023. Bad: credential stuffing runs against the login form at full speed because the only throttle is application code written for the happy path. Instead: add CDN/WAF or gateway rate-limit rules for the auth paths before launch. Severity: BLOCK.

## Gates

- **G-DO-071 — External production check.** Verifies: DO-151, DO-141. Check: automated — `curl -sI https://<production-domain>/` from a network other than the deploy network returns 200 over a valid certificate, and the provider's deployment record shows a commit SHA equal to `git rev-parse HEAD`. Pass: both true. Fail: block the launch or release announcement until both hold. Before a production environment is provisioned, this gate's disposition is a recorded provisioning waiver per the §6.3 protocol; it unblocks when a production domain is provisioned and the release is deployed to it. Recorded in: progress.md.
- **G-DO-072 — Readiness honesty test.** Verifies: DO-144. Check: automated — in staging, stop the database (or block its port), then confirm the readiness endpoint returns a non-200 status within 60 seconds while the liveness endpoint still returns 200. Pass: readiness fails and liveness passes. Fail: block promotion to production posture. Recorded in: progress.md.
- **G-DO-073 — Exposure probe.** Verifies: DO-147, DO-148. Check: automated — `for p in /.git/HEAD /.env /phpinfo; do curl -s -o /dev/null -w "%{http_code} $p\n" https://<production-domain>$p; done` returns only 403 or 404, and `curl -sI https://<production-domain>/` shows no version-bearing `Server:` or `X-Powered-By` header. Pass: all probes blocked and no version banners. Fail: block shipment. Before a production environment is provisioned, this gate's disposition is a recorded provisioning waiver per the §6.3 protocol; it unblocks when a production domain is provisioned and the deployed release can be probed from an external network. Recorded in: progress.md.
- **G-DO-074 — Config-drift diff.** Verifies: DO-146. Check: semi-automated — export the provider console settings and diff them against the committed platform config file (build command, environment variable names, region, instance count). Pass: zero unexplained differences. Fail: reconcile the same day; drift surviving one release blocks the next deploy. Recorded in: progress.md.
- **G-DO-075 — Hosting record audit.** Verifies: DO-141, DO-142, DO-143, DO-152. Check: manual — open the hosting record and confirm provider, region, scaling behavior, sleep policy, caps, exit path, posture tier, any single-point-of-failure decision, and a check date no more than 90 days old are all present. Pass: every field present and current. Fail: block promotion to production posture. Recorded in: progress.md.

## Anti-patterns

- **The generous free tier.** The host is picked because its free tier "should be enough"; the binding cap is discovered at the first traffic spike. Catch it: the host-limit sheet names the binding cap and what happens when it is hit, before launch (DO-152).
- **Sleep-blind scheduling.** Webhooks, cron jobs, or background workers are placed on a host that spins down when idle, so they silently stop firing. Catch it: check the record's sleep policy against every scheduled and webhook dependency before wiring them up.
- **Region by default.** The app runs in whatever region the provider defaulted to, far from both its users and its database. Catch it: app region and database region are both named in the hosting record, and they match.
- **Dashboard truth.** The provider dashboard is treated as the record of what is live; nobody can say which commit is running without opening it. Catch it: the live commit SHA is written into progress.md at every deploy (G-DO-071).

## Examples

- [Example 1 — A localhost "launch" replaced by an externally verified deployment](examples/example-1.md) — corrects DO-151.
- [Example 2 — A single-box deployment recorded, then promoted](examples/example-2.md) — corrects DO-143.
- [Example 3 — A static-page probe replaced by a real readiness check](examples/example-3.md) — corrects DO-144.

## Recall anchors

- Pick the host by workload shape; write its limits down.
- Production is proven from outside, on the current commit.
- Readiness checks dependencies; a static page proves nothing.
- Ephemeral disk holds no state — uploads and data live in real stores.
- Console and committed config match, or it is drift.

## Checklist

- [ ] Hosting record is complete: provider, region, scaling, sleep policy, caps, exit path, check date (DO-141).
- [ ] Posture tier is declared, with its promotion trigger and waived parameters (DO-142).
- [ ] No unrecorded single point of failure in production posture (DO-143, G-DO-075).
- [ ] Readiness fails in staging when the database is stopped (G-DO-072).
- [ ] Exposure probes are blocked and no version banners are served (G-DO-073).
- [ ] External check passes and the live commit SHA equals repo HEAD (G-DO-071).
- [ ] Console settings diff clean against the committed platform config (G-DO-074).
