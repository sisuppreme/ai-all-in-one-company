# security-testing

## Metadata

- **Owner department:** D8 QA & Testing (QA)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** OWASP Web Security Testing Guide (WSTG), https://owasp.github.io/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/01-Information_Gathering/05-Review_Webpage_Content_for_Information_Leakage ; OWASP Session Management Cheat Sheet, https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html
- **Depends on:** integration-testing, e2e-testing
- **Feeds into:** qa-gates, bug-triage

## When to use / Do NOT use

- **Use when:** A release needs security evidence: WSTG checklist execution, CI scanner triage, authorization/IDOR testing, session and authentication abuse cases — always against the project's own staging or production-like environments, or inside its own CI pipeline.
- **Do NOT use when:** The target is any system the project does not own or operate — never in scope, no exceptions. Tool selection, hardening, and fixes belong to D7 (security); penetration testing under a written engagement belongs to D7's penetration-testing skill.

## Rules

1. **QA-181 — Written scope before any test runs.** The test plan names the target environments (own staging/production-like only), the accounts and roles used, and the techniques allowed; testing outside that written scope does not start.
2. **QA-182 — WSTG checklist per release.** Each release executes the app-relevant OWASP WSTG categories (information gathering, authentication, authorization, session management, input validation, business logic) under their stable test IDs (e.g., WSTG-INFO-05), with pass/fail and evidence recorded per case.
3. **QA-183 — Skipped categories are named, with reasons.** The release record lists every WSTG category executed and every category skipped with its reason; an unlisted category is treated as not executed.
4. **QA-184 — Scanner suite in CI on every change.** Dependency, SAST, secrets, and container/config scanners run on every change; a new confirmed critical or high finding fails the pipeline with a non-zero exit.
5. **QA-185 — Every scanner result is triaged.** Each result is marked confirmed-exploitable, accepted-risk with a written note, or false-positive with the reason; raw scanner output is never the finding record.
6. **QA-186 — Authorization matrix by replay.** For every privileged endpoint, an automated test replays the request with a lower-privilege session and requires rejection (401/403); UI hiding is never accepted as evidence of enforcement.
7. **QA-187 — IDOR sweep on object access.** For every endpoint that takes an object ID, a test requests another account's object ID under a different session and requires rejection, run against own staging data only.
8. **QA-188 — Session cases per the OWASP Session Management Cheat Sheet.** Tests verify cookie flags (HttpOnly, Secure, SameSite), session rotation on login and privilege change, and server-side invalidation on logout.
9. **QA-189 — Authentication abuse cases pass end to end.** A wrong password is rejected (no any-password login), and a password reset is proven by logging in with the new password while the old one fails — receiving the reset email alone is not a pass.
10. **QA-190 — Findings close only by retest.** Every finding is recorded with evidence, severity, and remediation, and is retested after the fix; an unretested fix leaves the finding open.
11. **QA-191 — Business-logic abuse cases per release.** The app's core flows get manual abuse cases scanners cannot see: price/quantity tampering, step skipping, replayed submissions, and concurrent-request races, each with a recorded verdict.
12. **QA-192 — DAST only against own staging, authenticated.** Dynamic scans run against the project's staging environment with test accounts for each role; results enter the same triage queue as every other scanner (QA-185).

## BAN list

- **BAN-QA-091 — Cosmetic authorization accepted as tested.** Banned: signing off authorization because a privileged button is hidden in the UI while the endpoint was never replay-tested. Defeats: DET-FAKE-021. Bad: "Admin page is safe — the delete button only renders for admins." Instead: replay the delete request with a standard-user session and require 403 before sign-off (QA-186). Severity: BLOCK.
- **BAN-QA-092 — Reset test that stops at the email.** Banned: marking password reset tested because a reset email arrived, without proving the credential changed. Defeats: DET-FAKE-020. Bad: test asserts the inbox received a reset link and closes the case. Instead: complete the reset, then assert login with the old password fails and login with the new password succeeds (QA-189). Severity: BLOCK.
- **BAN-QA-093 — Security control disabled to get CI green.** Banned: suppressing a scanner rule, skipping the secrets scan, or loosening an auth check in shipped configuration so the pipeline passes. Defeats: DET-CODE-020. Bad: `// nosec` added to a flagged query with no ticket or risk note. Instead: fix the finding, or record an accepted-risk note with owner and expiry and keep the control on (QA-185). Severity: BLOCK.
- **BAN-QA-094 — Session "verified" by a client-side flag.** Banned: treating a `loggedIn=true` value in browser storage as proof a session exists or is enforced. Defeats: DET-FAKE-002. Bad: test sets the flag, reloads, sees the dashboard, and passes session management. Instead: verify the server-issued session cookie's flags and that a protected API call without it is rejected (QA-188). Severity: BLOCK.
- **BAN-QA-095 — Real credentials hardcoded in test assets.** Banned: real passwords, tokens, or API keys committed in security-test fixtures, scripts, or CI configuration. Defeats: DET-CODE-018. Bad: the DAST script contains the production admin password "so it can log in." Instead: use dedicated staging test accounts whose credentials live in the CI secret store and are injected at runtime. Severity: BLOCK.

## Gates

- **G-QA-091 — Scanner gate.** Verifies: QA-184, QA-185. Check: `scripts/security-scan.sh` runs the dependency, SAST, secrets, and container/config scanners and exits non-zero on any new confirmed critical/high finding. Pass: exit code 0 and a triage record exists for every result. Fail: block merge/release. Recorded in: progress.md.
- **G-QA-092 — Authorization matrix gate.** Verifies: QA-186, QA-187. Check: `npm run test:authz` runs the privilege-replay and IDOR suites; the run exits non-zero if any privileged endpoint lacks a replay test or any replay is not rejected. Pass: exit code 0 with one replay test per privileged endpoint. Fail: block release. Recorded in: progress.md.
- **G-QA-093 — Seeded-fault negative control.** Verifies: QA-184. Check: on a scratch branch, seed one known-vulnerable dependency and remove one authorization check, then run the pipeline; both G-QA-091 and G-QA-092 must exit non-zero. Pass: both gates report red on the seeded branch. Fail: the gates are broken — fix the gates before any release relies on them. Recorded in: progress.md.
- **G-QA-094 — WSTG release record gate.** Verifies: QA-182, QA-183. Check: `test -s docs/security/wstg-record.md && grep -q "Skipped:" docs/security/wstg-record.md` — the record exists, names executed categories by WSTG ID with evidence, and lists skipped categories with reasons. Pass: command exits 0. Fail: block release sign-off. Recorded in: progress.md.

## Anti-patterns

- **Scanner theater.** Dashboards are green and dashboards are shown, but the findings queue has not been triaged in weeks; catch it by sampling five scanner results and asking for each one's triage verdict.
- **Happy-path-only auth tests.** Every security test logs in as an admin and asserts success; no test ever asserts a rejection. Catch it by counting tests whose expected result is 401/403 — zero means the suite proves nothing.
- **Checklist photocopy.** The WSTG record is last release's file with the date changed and identical evidence links. Catch it by spot-checking one evidence artifact per category against this release's build.
- **Staging drift.** DAST and replay suites run against a staging build whose auth configuration differs from production, so green results describe a system that does not ship. Catch it by diffing the security-relevant configuration of staging and production before sign-off.

## Examples

- [Example 1 — Authorization proven by replay, not by a hidden button](examples/example-1.md) — violates/corrects QA-186.
- [Example 2 — Scanner output triaged into a finding record](examples/example-2.md) — violates/corrects QA-185.
- [Example 3 — Password reset proven end to end](examples/example-3.md) — violates/corrects QA-189.

## Recall anchors

- Test from the attacker's seat: replay it as the low-privilege user.
- A scanner report is raw material, not a verdict — triage every line.
- Skipped is a recorded decision; silent is a gap.
- An unretested fix is an open finding.
- Own systems only — if the project does not own it, it is out of scope.

## Checklist

- [ ] Written scope names own environments, accounts, and allowed techniques (QA-181).
- [ ] WSTG record lists executed categories by ID with evidence, and skipped categories with reasons (QA-182, QA-183).
- [ ] Scanner suite ran in CI on this change and exited 0 (QA-184, G-QA-091).
- [ ] Every scanner result carries a triage verdict (QA-185).
- [ ] Privilege-replay and IDOR suites pass, one replay per privileged endpoint (QA-186, QA-187, G-QA-092).
- [ ] Session cases cover cookie flags, rotation, and logout invalidation (QA-188).
- [ ] Reset proven by login with the new password; wrong-password login rejected (QA-189).
- [ ] All fixed findings retested; seeded-fault control still turns the gates red (QA-190, G-QA-093).
