# DET-INF — Infrastructure & Deployment Detection Parameters (X-Infra)

Purpose: Detect whether a project's infrastructure and deployment practice was professionally operated or AI-assembled and abandoned at "it runs on my machine." Each parameter names one observable tell, the professional contrast, an exact check, and the known false positives.
How to run: Work the parameters in ID order against the repo, the hosting/cloud console, and the live production URL. Record pass/fail per parameter with the evidence the Check step produced; a fail at blocker severity stops the release until fixed or formally waived.
Scoring note: Judge the running system and its history (CI runs, deploy logs, restore records), not the presence of config files alone — AI output often contains plausible config that was never executed.

### DET-INF-001 — No CI pipeline exists
- **Signal:** No `.github/workflows/`, `.gitlab-ci.yml`, `Jenkinsfile`, or equivalent in the repo; no build badges or CI settings on the host.
- **AI-typical:** Code is generated, run locally once, and declared done; nothing ever builds or tests it automatically.
- **Professional:** Every push and pull request triggers an automated build, lint, and test run whose result is visible on the change.
- **Check:** List CI config files in the repo root and `.github/workflows/`; open the host's Actions/Pipelines tab and confirm at least one run in the last 30 days.
- **False positives:** CI may live in an external system (Buildkite, TeamCity) not visible from the repo; ask for the pipeline URL before failing it.
- **Severity:** blocker.
- **Source:** https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions
- **Fix:** ci-cd.

### DET-INF-002 — CI exists but never gates
- **Signal:** Workflow files exist, but branch protection does not require them, tests are skipped (`continue-on-error`, `-DskipTests`, commented-out steps), or recent runs are red and merges happened anyway.
- **AI-typical:** A generated workflow that fails or was never wired to merging; the check is decoration.
- **Professional:** Required status checks block merge on failure; a red pipeline is treated as a stop, not background noise.
- **Check:** Inspect branch protection/rulesets for required checks; review the last 10 workflow runs and compare outcomes against merge commits in the same window.
- **False positives:** A deliberately advisory lint job may be non-blocking while build/test jobs gate; fail only if no job gates.
- **Severity:** major.
- **Source:** https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions
- **Fix:** ci-cd.

### DET-INF-003 — No environment separation
- **Signal:** One deployment target only; the same database URL, API keys, and config serve local development, staging (if any), and production.
- **AI-typical:** A single `.env` with production values used everywhere; test traffic and real users share one database.
- **Professional:** At least dev/staging/production are separate targets with separate data stores and credentials; production data is never the test fixture.
- **Check:** Compare environment variable sets per target in the hosting console; confirm staging and production resolve to different database hosts.
- **False positives:** A pre-launch MVP may legitimately have only production plus local; distinguish by whether production credentials are also the local ones.
- **Severity:** blocker.
- **Source:** https://12factor.net/config
- **Fix:** deployment-strategies, hosting.

### DET-INF-004 — Manual, unreproducible deploys
- **Signal:** Deploy means copying files over FTP/SFTP, SSHing in to `git pull` and restart, or running a build on the production server; no deploy log or artifact record.
- **AI-typical:** Instructions say "upload the files and restart"; nobody can say exactly which code is live or rebuild it identically.
- **Professional:** Deploys run from CI off a versioned, immutable artifact (image or bundle) with an auditable record of who/what/when.
- **Check:** Ask for the deploy procedure and the last three deploy records; fail when the procedure is undocumented hand-steps or the live revision cannot be identified — no mapping to a commit SHA, a stored artifact, or a deploy tool's revision record.
- **False positives:** A documented, scripted deploy is automated, not manual — the class is on-host deploy/rebuild tools with a written procedure and a revision record: SSH-based release tools, container rebuild launchers shipped with distributable software, and platform deploy scripts all belong to it. Check for the documented procedure and its records, not for a CI pipeline shape; this covers a distributable product's vendor-supported upgrade path as much as a single operated service.
- **Severity:** blocker.
- **Source:** Derived: PROJECT_ANATOMY.md Part 4/5.
- **Fix:** ci-cd, deployment-strategies.

### DET-INF-005 — Secrets committed to version control
- **Signal:** Live API keys, database passwords, private keys, or tokens in tracked files, config, or git history; `.env` not in `.gitignore`.
- **AI-typical:** Generated config files ship with real credentials filled in, and they get committed with everything else.
- **Professional:** Secrets live in a secrets manager or platform env store, are injected at runtime, and secret scanning runs on push.
- **Check:** Run a scanner (`gitleaks` or `trufflehog`) over the repo including history; grep tracked files for `API_KEY`, `PASSWORD`, `BEGIN.*PRIVATE KEY`. Classify each hit by file role and value (see False positives) before recording a finding.
- **False positives:** Example, sample, and template files generally (`.env.example`, `samples/`, `templates/`, `*.sample.*`, files headed "copy and edit") with placeholder values are fine. Value test: a credential that is dictionary-fake (`pa$$word`, `changeme`, `password123`) and paired with reserved example hosts (`example.com`) is a placeholder; escalate only values that are high-entropy, real-looking, or verifiably live — verify against the provider if unsure.
- **Severity:** blocker.
- **Source:** https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html
- **Fix:** secrets-management.
- **See also:** DET-CODE-018 (secret literals written into source code are CODE-018's scope; INF-005 owns secrets tracked in version control and history)
- **See also:** DET-INF-006 (the same secret shipped to the browser is INF-006's scope; INF-005 owns exposure at rest in the repo)

### DET-INF-006 — Secrets exposed in client bundles
- **Signal:** Server-side credentials reachable from the browser: private API keys in `NEXT_PUBLIC_*`/`VITE_*` variables, keys visible in shipped JS, or admin tokens in mobile/web bundles.
- **AI-typical:** The generator puts the working key wherever the code first runs, including public env prefixes, because it works in the demo.
- **Professional:** Only publishable/public keys ship to clients; privileged calls go through a server route that holds the real secret.
- **Check:** Download the production JS bundles and grep for key patterns and provider secret prefixes (`sk_live`, `sk-`, service-role keys); check the env variable names used client-side.
- **False positives:** Publishable keys (Stripe `pk_live`, Firebase web config, public analytics IDs) are designed to be public; fail only privileged credentials.
- **Severity:** blocker.
- **Source:** https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html
- **Fix:** secrets-management.
- **See also:** DET-CODE-018 (secret literals in source are CODE-018's scope; INF-006 owns exposure in the delivered client bundle)
- **See also:** DET-INF-005 (secrets committed to version control are INF-005's scope; INF-006 owns what reaches the browser)

### DET-INF-007 — Config hardcoded or per-machine
- **Signal:** Environment-specific values (URLs, hostnames, feature toggles, credentials) are constants in source code, or each server has a hand-edited config file that exists nowhere else.
- **AI-typical:** `const API_URL = "http://localhost:3000"` or a production IP baked into code that "worked" in the generated environment.
- **Professional:** All deploy-varying config comes from environment variables or a config service; the same artifact runs unchanged in every environment.
- **Check:** Grep built/deployed artifacts and runtime source for `localhost`, raw IPs, and `http://` literals — exclude tests, `docs/`, `samples/`, `templates/`, `examples/`, README files, and locale files, and ignore values on reserved example domains. A hit counts only if the literal survives into the artifact that actually runs. Diff config between two environments and confirm differences come only from env values.
- **False positives:** Internal constants that never vary between deploys (route definitions, enum values) are code, not config; the test is whether the value changes per deploy. Literals in documentation and fill-in templates are the documented place where per-deploy values go — a placeholder host in a sample config the operator is instructed to replace is the config mechanism working, not hardcoding.
- **Severity:** major.
- **Source:** https://12factor.net/config
- **Fix:** secrets-management, deployment-strategies.
- **See also:** DET-CODE-032 (CODE-032 owns config duplicated and drifted across services in code; INF-007 owns the hardcoded/per-machine deploy surface)

### DET-INF-008 — No backups configured
- **Signal:** No automated backup job, snapshot schedule, or managed backup policy for the production database and user-uploaded files.
- **AI-typical:** Data durability is never mentioned; the database is a container volume or a single unmanaged instance.
- **Professional:** Scheduled, automated backups with defined retention exist for every stateful store, owned by the platform or a backup tool.
- **Check:** In the database/hosting console, open the backup or snapshot policy and confirm it is enabled with a recent successful run.
- **False positives:** Stateless services with data held in a managed store elsewhere need no backup of their own; verify where the state actually lives before failing.
- **Severity:** blocker.
- **Source:** https://sre.google/sre-book/data-integrity/
- **Fix:** backup-recovery.

### DET-INF-009 — Backups never restore-tested
- **Signal:** Backups exist on a schedule, but there is no restore drill, runbook entry, or restored environment anywhere in the project's history.
- **AI-typical:** A cron line or console checkbox is declared "backups done"; the first restore attempt would happen during a real incident.
- **Professional:** Restores are rehearsed on a cadence into an isolated environment and timed, so recovery time is a measured fact.
- **Check:** Ask for the date and evidence of the last successful restore test (ticket, log, drill record); absence of any record is the fail.
- **False positives:** Managed services with point-in-time recovery still need a drill, but a documented provider-level recovery test may substitute for an early-stage project.
- **Severity:** major.
- **Source:** https://sre.google/sre-book/data-integrity/
- **Fix:** backup-recovery.

### DET-INF-010 — Backups share the primary failure domain
- **Signal:** Backups stored on the same server, same cloud account, or same region as the primary data, with no off-site or cross-account copy and no immutability.
- **AI-typical:** A nightly dump written to a folder on the same VPS that runs the database.
- **Professional:** At least one backup copy survives loss of the host, the region, and the account (separate storage, ideally versioned or immutable against ransomware and deletion).
- **Check:** Identify backup storage location(s) and compare against the primary's host, region, and account; confirm object lock/versioning or an equivalent safeguard.
- **False positives:** Small projects may accept same-account, cross-region copies as their tier of protection; fail only same-host or same-region-only setups.
- **Severity:** major.
- **Source:** https://sre.google/sre-book/data-integrity/
- **Fix:** backup-recovery.

### DET-INF-011 — No monitoring of the golden signals
- **Signal:** No metrics dashboard, APM, or host monitoring for production; nobody can answer current latency, error rate, traffic, or saturation without SSHing in.
- **AI-typical:** Observability is skipped because the demo did not need it; the first symptom of failure is a user complaint.
- **Professional:** Latency, traffic, errors, and saturation are collected continuously and viewable on a dashboard tied to the service's SLOs.
- **Check:** Open the monitoring tool linked from the runbook and confirm live data for all four golden signals over the last 7 days.
- **False positives:** A tiny static site needs only uptime and error-log checks; apply the full four-signal bar to anything serving dynamic requests or holding user data.
- **Severity:** blocker.
- **Source:** https://sre.google/sre-book/monitoring-distributed-systems/
- **Fix:** monitoring.

### DET-INF-012 — Alerts reach nobody
- **Signal:** No alert rules, or alerts fire into an unmonitored channel (an unused Slack channel, an ex-employee's email, a dashboard nobody opens); no on-call owner named.
- **AI-typical:** "Monitoring" is a dashboard link; nothing pages a human when error rate or downtime crosses a threshold.
- **Professional:** Symptom-based alerts on SLO burn or downtime route to a paging tool (PagerDuty, Opsgenie, platform equivalent) with a named rotation and escalation.
- **Check:** List active alert rules and their notification targets; trigger or inspect the last test alert and confirm a current team member received it.
- **False positives:** Business-hours products may route to a monitored team inbox instead of a pager; the test is a named human who demonstrably receives and acts.
- **Severity:** blocker.
- **Source:** https://sre.google/workbook/alerting-on-slos/
- **Fix:** alerting, incident-response.

### DET-INF-013 — Logs are ephemeral console output
- **Signal:** Application logs go to stdout on the host or container and vanish on restart/redeploy; no central log store, retention, or search; errors are debugged by "checking the server."
- **AI-typical:** `console.log` debugging left in place, with logs treated as a local dev convenience rather than an operational record.
- **Professional:** Structured logs are shipped to a central, searchable store with defined retention, and errors are captured by an error tracker with stack traces and release tags.
- **Check:** Restart or redeploy a non-production instance and confirm prior logs remain queryable; verify retention settings and that production errors appear in the tracker.
- **False positives:** Platforms like Vercel or Cloud Run retain platform logs by default; confirm the retention window and searchability before passing.
- **Severity:** major.
- **Source:** https://12factor.net/logs
- **Fix:** logging, monitoring.

### DET-INF-014 — No HTTPS, or HTTP not redirected
- **Signal:** The site answers on plain HTTP without a redirect to HTTPS, or login/API routes accept HTTP.
- **AI-typical:** The generated deploy serves the platform default; TLS was "a later step" that never happened.
- **Professional:** All traffic is HTTPS; HTTP requests 301 to HTTPS and HSTS is set once HTTPS is confirmed stable.
- **Check:** `curl -sI http://<domain>` and confirm a redirect to `https://`; load the site and confirm no page or API call is served over HTTP.
- **False positives:** A local-only or internal-network tool behind a VPN may acceptably skip public TLS; anything reachable from the public internet may not.
- **Severity:** blocker.
- **Source:** https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html
- **Fix:** ssl-certificates, domains-dns.

### DET-INF-015 — Weak TLS configuration or mixed content
- **Signal:** TLS 1.0/1.1 still enabled, obsolete cipher suites accepted, or HTTPS pages loading scripts, images, or API calls over HTTP (mixed content warnings in the console).
- **AI-typical:** Default server TLS settings from an old base image or tutorial are shipped unexamined; asset URLs are hardcoded `http://`.
- **Professional:** Configuration follows a maintained profile (Mozilla Intermediate or stricter): TLS 1.2+ only, current ciphers, and zero mixed-content references.
- **Check:** Run an external scan (SSL Labs) or `testssl.sh` against the domain; crawl key pages with the browser console open and count mixed-content warnings.
- **False positives:** A legacy client base (embedded devices, old enterprise browsers) may justify TLS 1.0/1.1 temporarily; require a documented exception and expiry date, not silent acceptance.
- **Severity:** major.
- **Source:** https://wiki.mozilla.org/Security/Server_Side_TLS
- **Fix:** ssl-certificates.

### DET-INF-016 — Certificate expiry is unmanaged
- **Signal:** Certificates are manually installed with no auto-renewal (no ACME client, no managed certificate), and no expiry alert; the cert's remaining validity is short or unknown.
- **AI-typical:** A one-off Certbot run or an uploaded commercial cert gets the demo live; renewal is a future outage nobody scheduled.
- **Professional:** Certificates auto-renew (ACME or provider-managed) and an alert fires weeks before expiry as a backstop.
- **Check:** Inspect the served certificate's dates (`openssl s_client` or browser padlock); find the renewal mechanism (certbot timer, platform setting) and any expiry alert rule.
- **False positives:** Provider-managed certs (Cloudflare, ALB, Vercel) renew invisibly — verify in the provider console rather than on the host before passing.
- **Severity:** major.
- **Source:** https://wiki.mozilla.org/Security/Server_Side_TLS
- **Fix:** ssl-certificates, alerting.

### DET-INF-017 — No rollback path for a bad deploy
- **Signal:** Deploying overwrites the live release in place; there is no previous artifact, release history, blue/green or canary setup, or documented way to return to the last good version.
- **AI-typical:** The deploy script copies new files over old ones, so a bad release can only be fixed by another forward fix under pressure.
- **Professional:** Each deploy keeps the previous version immediately redeployable (immutable artifacts, release slots, or platform rollback), and rollback is a rehearsed, timed operation.
- **Check:** Ask the operator to name the exact command or console action that restores the previous release, and find evidence it was used or drilled at least once.
- **False positives:** A static site behind a CDN with versioned assets can roll back by repointing; confirm the repoint target actually exists before passing.
- **Severity:** blocker.
- **Source:** Derived: PROJECT_ANATOMY.md Part 4/5.
- **Fix:** rollback, deployment-strategies.

### DET-INF-018 — Irreversible or manual database migrations
- **Signal:** Schema changes are applied by hand in a SQL console, or migration files exist with no down/rollback path and no record of what ran against production.
- **AI-typical:** The generated schema is created once from the ORM; later changes are ad-hoc `ALTER` statements nobody versioned.
- **Professional:** Migrations are versioned, run by the deploy pipeline in order, tracked in a schema-history table, and each ships with a reversal or a documented forward-fix plan.
- **Check:** Inspect the migrations folder and the production schema-history table; confirm the latest deploy's migration appears in both and has a down path or documented exception.
- **False positives:** Some changes (dropping a column) are legitimately irreversible; the professional pattern is a documented expand/contract sequence, not a missing down file.
- **Severity:** major.
- **Source:** Derived: PROJECT_ANATOMY.md Part 4/5.
- **Fix:** rollback, deployment-strategies.

### DET-INF-019 — Single point of failure in serving
- **Signal:** In a named production deployment with stated availability requirements: one app instance, one server, one availability zone, and a stateful database on the same box; any single failure takes the whole product down. This parameter judges a deployment, not distributable software or its shipped default templates.
- **AI-typical:** The architecture diagram is one box; scaling and redundancy were never part of the generated plan.
- **Professional:** Stateless tiers run at least two instances behind a load balancer (or on a platform that provides this), and data stores use managed replication or a documented failover.
- **Check:** For the named deployment under review: count running instances and their placement in the hosting console; kill or stop one non-production instance and confirm the service stays up. Do not apply this check to a vendor's sample or default topology files — evaluate the actual deployment or, for distributable software, the documentation test in False positives.
- **False positives:** An early MVP may consciously accept a single instance; the fail is the absence of a recorded decision and a path to redundancy, not the topology alone. For distributable/self-hosted software, vendor documentation that presents the single-node topology as an explicit option alongside a documented multi-node path satisfies the recorded-decision test — the decision and the exit path are recorded in the project's own docs.
- **Severity:** major.
- **Source:** https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html
- **Fix:** hosting, deployment-strategies.

### DET-INF-020 — No health check endpoint or probes
- **Signal:** The app exposes no `/health` or readiness endpoint; orchestrator/platform probes are absent or point at a static page that cannot fail.
- **AI-typical:** "Up" is judged by the homepage loading, so dead dependencies and hung processes look healthy to automation.
- **Professional:** Liveness and readiness checks reflect real ability to serve (process up; dependencies reachable for readiness), and the platform restarts or drains failing instances automatically.
- **Check:** Request the health endpoint directly; in Kubernetes inspect `livenessProbe`/`readinessProbe` in the deployment spec; stop a dependency in staging and confirm readiness fails.
- **False positives:** A health endpoint that returns 200 without dependency checks is correct for liveness; fail only when readiness also ignores dependencies or no endpoint exists at all.
- **Severity:** major.
- **Source:** https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/
- **Fix:** monitoring, hosting.

### DET-INF-021 — Debug and admin surfaces exposed in production
- **Signal:** Framework debug mode on (Werkzeug/Django `DEBUG=True`, Laravel Debugbar, stack traces to users), or reachable `/.git`, `/.env`, `/phpinfo`, `/server-status`, unauthenticated admin/metrics endpoints.
- **AI-typical:** Development settings are copied to production verbatim because they made errors easier to see during generation.
- **Professional:** Debug tooling is disabled by environment config in production, errors return generic responses, and admin/metrics surfaces sit behind authentication and network restrictions.
- **Check:** Probe the listed paths against the production URL and record status codes; trigger an error and confirm the response contains no stack trace, SQL, or file paths.
- **False positives:** An intentionally public `/metrics` with no sensitive labels exists on some internal-only services; on a public host it must be authenticated or network-restricted.
- **Severity:** blocker.
- **Source:** https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html
- **Fix:** hosting, deployment-strategies.
- **See also:** DET-CODE-020 (CODE-020 owns the unsafe default in code and config; INF-021 owns what is actually exposed on the production host)

### DET-INF-022 — Default server configuration shipped unchanged
- **Signal:** Directory listing enabled, server/version banners exposed (`Server: Apache/2.4.x`, `X-Powered-By`), default welcome pages on unused vhosts, default database ports reachable from the internet.
- **AI-typical:** The base image or one-click install defaults go live untouched; hardening was never in the generated scope.
- **Professional:** Server config follows a maintained baseline: banners suppressed, listing off, only required ports open, unused services and vhosts removed.
- **Check:** `curl -sI` the site for banner headers; request a directory path expecting a listing; run an external port scan and reconcile every open port against the architecture.
- **False positives:** Version banners alone are low-risk noise on an otherwise hardened host; escalate when banners combine with open default ports or listing.
- **Severity:** minor.
- **Source:** Derived: PROJECT_ANATOMY.md Part 4/5.
- **Fix:** hosting, domains-dns.

### DET-INF-023 — No rate limiting at the edge
- **Signal:** Login, password-reset, signup, and public API endpoints accept unlimited request rates from a single IP; no WAF, CDN rule, or gateway throttle in front of them.
- **AI-typical:** Rate limiting lives, if anywhere, in application code written for the happy path; credential stuffing and scraping are unopposed.
- **Professional:** Edge limits (CDN/WAF or API gateway) throttle auth and expensive endpoints, with stricter tiers for unauthenticated traffic and alerting on sustained abuse.
- **Check:** From a test IP, script repeated login attempts and confirm throttling (429/block) engages; inspect CDN/WAF rate-limit rules for the auth and API paths.
- **False positives:** Low-risk read-only public content needs no strict limit; the fail is unthrottled auth, reset, or paid-cost endpoints specifically.
- **Severity:** major.
- **Source:** https://developers.cloudflare.com/waf/rate-limiting-rules/
- **Fix:** hosting, monitoring.

### DET-INF-024 — No infrastructure as code, or IaC drifted
- **Signal:** Servers, networks, and DNS were created by clicking in consoles with no infrastructure-as-code record — IaC defined functionally: infrastructure declared in version-controlled files that a tool applies convergently — or IaC exists but `plan` shows drift because changes bypass it.
- **AI-typical:** A generated `main.tf` describes the demo environment while the real one was hand-built and has since diverged silently.
- **Professional:** All durable infrastructure is declared in code, reviewed like code, and applied from CI; console changes are emergencies that get back-ported the same day.
- **Check:** Run the IaC tool's plan/diff against the real environment in read-only mode; unexplained resources or attribute drift is the fail. Before recording "no IaC", check companion deployment repositories and non-listed declarative systems (see False positives); no IaC anywhere — in this repo or its deployment companions — is the stronger fail.
- **False positives:** Fully managed platforms encode infrastructure in their own config files; treat those files as the IaC and check they match the console. The same class covers any declarative, version-controlled infrastructure system, whatever the tool: companion deployment repositories (a separate repo holding the deploy tooling), container-template/launcher systems, orchestration manifests, and provisioning playbooks all count as IaC when a tool applies them convergently — the test is declaration plus convergent application, not the brand of tool.
- **Severity:** major.
- **Source:** https://developer.hashicorp.com/terraform/language/state
- **Fix:** infrastructure-as-code.

### DET-INF-025 — Dependencies and base images never patched
- **Signal:** No Dependabot/Renovate config, base images pinned to old tags, OS packages unpatched since provisioning, and no record of a dependency update ever being merged.
- **AI-typical:** The generated lockfile and Dockerfile are a time capsule from generation day; vulnerability scanning is absent from CI.
- **Professional:** Automated update PRs flow continuously, CI scans dependencies and images for known vulnerabilities, and critical findings have a patch SLA.
- **Check:** Open the dependency-update tool's history and the last merged update PR; check the production base image's age and run a vulnerability scan (`trivy`, `npm audit`, provider scanner).
- **False positives:** A deliberately frozen stack under a change freeze or certification window is legitimate with a documented end date; indefinite freeze is the fail.
- **Severity:** major.
- **Source:** https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/about-dependabot-version-updates
- **Fix:** ci-cd, infrastructure-as-code.

### DET-INF-026 — Mutable or unpinned production artifacts
- **Signal:** Production runs `latest` image tags with no pinning mechanism available, installs dependencies at container start, or deploys whatever is on an ungated development branch HEAD at deploy time rather than a built, tagged artifact.
- **AI-typical:** `docker pull app:latest` and `npm install` in the start script make every restart a silent, untested upgrade.
- **Professional:** Deploys reference immutable artifacts by digest or version tag, built once in CI and promoted unchanged between environments.
- **Check:** Inspect the deployment spec/compose file for the image reference. Fail when (a) no pinning mechanism exists (no digest, version, or revision option), or (b) the floating target is an ungated development branch. Where staging and production both exist, confirm they ran the identical artifact.
- **False positives:** Auto-updating is acceptable for disposable preview environments; production and staging-for-approval must be pinned. A rolling default that tracks a vendor's tested release channel — where the same config documents a pin option (a version/revision field accepting any fixed release) — is a noted risk, not a fail: distinguish "pinning impossible or never done" from "vendor-supported rolling default with pinning available".
- **Severity:** major (minor — noted risk only — for a rolling vendor-release default with a documented pin option).
- **Source:** Derived: PROJECT_ANATOMY.md Part 4/5.
- **Fix:** deployment-strategies, ci-cd.

### DET-INF-027 — No resource limits or saturation headroom
- **Signal:** Containers run without CPU/memory limits or requests, no autoscaling policy exists, and disk/connection saturation has no alert; one traffic spike or memory leak takes down co-located services.
- **AI-typical:** Generated manifests and compose files omit resources entirely, because the demo ran fine on an empty machine.
- **Professional:** Every workload declares requests and limits sized from observed usage, saturation metrics (CPU, memory, disk, connections) alert before exhaustion, and scaling behavior is defined.
- **Check:** Inspect deployment specs for `resources:` blocks and the autoscaler configuration; confirm saturation alerts exist for disk and memory in the alerting tool.
- **False positives:** A single small VPS without containers expresses this as monitoring plus a documented capacity ceiling; fail when neither limits nor saturation alerting exist in any form.
- **Severity:** minor.
- **Source:** https://sre.google/sre-book/monitoring-distributed-systems/
- **Fix:** monitoring, alerting, hosting.

### DET-INF-028 — No external uptime check or status communication
- **Signal:** The only "monitoring" is internal; no independent external probe checks the public URL, and there is no status page or defined channel for telling users about an outage.
- **AI-typical:** If the whole host or network path dies, every internal check dies with it and the team learns about it from social media.
- **Professional:** An external synthetic check (separate provider) probes the public endpoints on a short interval and feeds the same paging path; a status page or equivalent comms channel is ready before it is needed.
- **Check:** Identify the external uptime service and its check interval and targets; confirm its alerts route to the same on-call path as DET-INF-012.
- **False positives:** The external probe built into a hosting platform counts if it runs outside the failing unit and pages independently; an in-dashboard chart does not.
- **Severity:** major.
- **Source:** https://sre.google/sre-book/managing-incidents/
- **Fix:** monitoring, alerting.

### DET-INF-029 — No incident response path
- **Signal:** No runbook, no named incident owner or on-call rotation, no post-incident review practice; past outages were handled ad hoc in chat with no record.
- **AI-typical:** Operations knowledge exists only as the generator's optimistic README line "contact the developer if something breaks."
- **Professional:** A short runbook covers the top failure modes with exact commands, an incident commander role is defined, and every significant incident produces a blameless postmortem with tracked follow-ups.
- **Check:** Ask for the runbook and the last incident record or postmortem; if neither exists for a system older than a few months, that absence is the finding.
- **False positives:** A pre-revenue side project may reasonably have a one-page runbook and business-hours response; fail when even that minimum is missing.
- **Severity:** major.
- **Source:** https://sre.google/sre-book/managing-incidents/
- **Fix:** incident-response, logging.

### DET-INF-030 — Domain and DNS under unmanaged control
- **Signal:** The domain sits in a personal registrar account with no auto-renew, no MFA, DNS records edited by hand with no export or IaC record, and no expiry alerting.
- **AI-typical:** Whoever set up the demo registered the domain on a personal card and account; the business cannot recover or renew it independently.
- **Professional:** The domain is held by the organization with auto-renew and MFA on, DNS changes are versioned or at least exported, and expiry/transfer-lock status is monitored.
- **Check:** Verify registrar account ownership, auto-renew and MFA status, and transfer lock; confirm a current DNS zone export or IaC record exists.
- **False positives:** A founder-held domain is common at seed stage; pass it only when auto-renew, MFA, and a recovery path to the organization are all demonstrably in place.
- **Severity:** minor.
- **Source:** Derived: PROJECT_ANATOMY.md Part 4/5.
- **Fix:** domains-dns.
