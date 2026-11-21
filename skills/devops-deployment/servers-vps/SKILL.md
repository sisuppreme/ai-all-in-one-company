# servers-vps

## Metadata

- **Owner department:** D6 DevOps & Deployment (DO)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** OWASP, "Logging Cheat Sheet" (exposure guidance cited by DET-INF-021/022) — https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html ; PROJECT_ANATOMY.md Part 4, Infrastructure/Hosting elements
- **Depends on:** infrastructure-as-code, domains-dns
- **Feeds into:** deployment-strategies, reliability, rollback

## When to use / Do NOT use

- **Use when:** a single virtual private server (or a small fixed set of them) hosts production: provisioning, hardening, patching, deploying to, and eventually replacing that host.
- **Do NOT use when:** the workload runs on a managed platform or Kubernetes — use hosting or kubernetes instead. Do not use a VPS as an excuse to skip the discipline those platforms enforce automatically; the VPS operator supplies it by hand.

## Rules

1. **DO-121 — Scripted provisioning.** The server is provisioned by a script or playbook committed to the repo, never by remembered console clicks. Every package, user, and config file on the box traces to that script.
2. **DO-122 — Hardening before first deploy.** Before any application deploys: directory listing off, version banners suppressed, default pages and default vhosts removed, unused services stopped and disabled (DET-INF-022).
3. **DO-123 — No public admin surfaces.** Debug endpoints, admin panels, and status pages are never reachable on the public interface; admin access sits behind authentication plus a network restriction (VPN, allowlist, or localhost-only binding) (DET-INF-021).
4. **DO-124 — Reverse proxy terminates TLS.** The application sits behind a reverse proxy (nginx, Caddy, or equivalent) that terminates TLS and forwards to the app on a loopback or private port; the app port is not exposed publicly.
5. **DO-125 — Patching is scheduled and recorded.** OS and package updates run on a written cadence (at least monthly, security updates sooner), and each run is logged with its date in the ops record. A box with no patch record is a finding (DET-INF-025).
6. **DO-126 — Deploys land as artifacts.** A deploy installs a built artifact — a container image or a versioned release directory — never an in-place edit of files on the live server (DET-INF-004).
7. **DO-127 — Previous release stays switchable.** Releases live in versioned directories with a symlink (or proxy target) selecting the live one; the previous release remains on disk so rollback is a symlink flip, not a rebuild (DET-INF-017).
8. **DO-128 — Logs ship off the box.** Application and system logs stream or rotate to storage outside the server. Logs that exist only on the box are lost with it and fill its disk until then (DET-INF-013).
9. **DO-129 — Saturation has an alert and a ceiling.** Disk, memory, and CPU usage are monitored with an alert before exhaustion — disk at 80% at the latest — and the server's capacity ceiling is written in the project docs (DET-INF-027).
10. **DO-130 — Only required ports are open.** The firewall defaults to deny; the open-port list matches the architecture document exactly, and any port not in the document is closed in the same change that discovers it.
11. **DO-131 — Key-only, named access.** SSH password authentication and direct root login are disabled; each operator logs in with a named account and an individual key, and elevation is via sudo.
12. **DO-132 — The server is replaceable.** Everything needed to rebuild the host — provisioning script, config, deploy procedure, restore steps — lives in the repo, and a rebuild from those files alone is drilled before the server is trusted (G-DO-063).

## BAN list

- **BAN-DO-061 — In-place live edits.** Banned: editing application code or config directly on the production server to "fix it quickly". Defeats: DET-INF-004. Bad: an operator SSHs in and patches a template file with a text editor; the fix exists on no other machine and vanishes at the next deploy. Instead: change the source in the repo, build a new artifact, and deploy it as a new release. Severity: BLOCK.
- **BAN-DO-062 — Default configuration shipped.** Banned: leaving the stock server page, default vhost, version banners, or directory listing live in production. Defeats: DET-INF-022. Bad: the domain's default vhost still serves the web server's welcome page and announces its exact version in response headers. Instead: apply the DO-122 hardening baseline before the first deploy and re-check it after every server change. Severity: BLOCK.
- **BAN-DO-063 — Public admin surface.** Banned: an admin panel, debug endpoint, or metrics page reachable from the public internet protected by nothing more than its own login form. Defeats: DET-INF-021. Bad: `/admin` answers on the public domain and takes password guesses at full speed. Instead: bind admin surfaces to localhost or a VPN interface, or put them behind an IP allowlist, with authentication on top. Severity: BLOCK.
- **BAN-DO-064 — The never-patched box.** Banned: a production server with no patch cadence and no patch record since provisioning. Defeats: DET-INF-025. Bad: the VPS has run 14 months; nobody can say which security updates it has or has not received. Instead: schedule the patch cadence, log every run with its date, and treat a stale log as a release blocker. Severity: WARN.

## Gates

- **G-DO-061 — Port reconciliation scan.** Verifies: DO-122, DO-130. Check: automated — run `nmap -Pn --top-ports 1000 <host>` (full-range `-p-` at setup) from an external machine and diff the open ports against the architecture document's port list. Pass: the two lists are identical. Fail: block the release; close or document every extra port. Recorded in: progress.md.
- **G-DO-062 — Banner and listing probe.** Verifies: DO-122, DO-123. Check: automated — `curl -sI https://<domain>/` shows no server version banner, `curl -s https://<domain>/assets/` returns 403 or 404 (never a listing), and each admin/debug path returns 403, 404, or a network refusal from a non-allowlisted address. Pass: all three probes behave as stated. Fail: block the release until the baseline is applied. Recorded in: progress.md.
- **G-DO-063 — Rebuild drill.** Verifies: DO-121, DO-132. Check: manual, timed — provision a fresh VPS using only the repo's scripts, deploy the current release, restore data per the documented steps, and run the smoke tests. Pass: the rebuilt server serves the application correctly with no step taken from memory or from the old box. Fail: the server is not yet replaceable; fix the scripts and repeat. Recorded in: progress.md.
- **G-DO-064 — Patch record audit.** Verifies: DO-125. Check: automated — read the last entry date in the ops patch log and compare it against the written cadence. Pass: the last recorded patch run is within one cadence interval of today. Fail: warn the operator; two consecutive misses block the next release. Recorded in: progress.md.

## Anti-patterns

- **The pet server.** Nobody dares reboot or rebuild the box because nobody knows what state lives only on it. Catch it: if the rebuild drill (G-DO-063) has never been run, the server is a pet by definition.
- **The orphaned test vhost.** A staging or test vhost from an early experiment still answers on the same box, unpatched and unmonitored, sharing the production IP. Catch it: list every vhost and service the provisioning script does not create; each one is removed or adopted into the script.
- **Monitoring that lives on the box.** The uptime check and the disk alert run on the server they watch, so a dead or full server reports nothing. Catch it: monitoring and log storage must be reachable and intact while the server is powered off.
- **Tribal-knowledge operations.** Restart commands, deploy quirks, and "watch out for" steps live in one operator's memory or chat history. Catch it: any step performed during an incident that is not in the repo's runbook is added to it before the incident is closed.

## Examples

- [Example 1 — An in-place hotfix replaced by an artifact deploy](examples/example-1.md) — corrects DO-126.
- [Example 2 — A default server configuration hardened before launch](examples/example-2.md) — corrects DO-122.
- [Example 3 — A public admin panel moved behind a network restriction](examples/example-3.md) — corrects DO-123.

## Recall anchors

- The server is replaceable; the repo is the server.
- Harden before the first deploy, not after the first incident.
- Artifacts in, symlink flips — never edits on the live box.
- Admin is never public; patches are never unrecorded.
- Logs and monitoring live somewhere the server's death cannot reach.

## Checklist

- [ ] Provisioning script in the repo reproduces the server with no manual steps (DO-121, G-DO-063).
- [ ] Hardening baseline applied: no default pages, banners, listings, or unused services (DO-122).
- [ ] Port scan output matches the architecture document exactly (G-DO-061).
- [ ] Admin and debug surfaces unreachable from a non-allowlisted address (DO-123, G-DO-062).
- [ ] Current deploy is an artifact in a versioned release directory; previous release still switchable (DO-126, DO-127).
- [ ] Patch log's last entry is within one cadence interval (DO-125, G-DO-064).
- [ ] Logs ship off the box and the disk alert fires at or before 80% (DO-128, DO-129).
- [ ] SSH is key-only with root login disabled and named operator accounts (DO-131).
