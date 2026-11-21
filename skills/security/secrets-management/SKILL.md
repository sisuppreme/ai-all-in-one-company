# secrets-management

## Metadata

- **Owner department:** D7 Security (SE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Gitleaks — https://github.com/gitleaks/gitleaks ; OWASP Secrets Management Cheat Sheet — https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html ; The Twelve-Factor App, "Config" — https://12factor.net/config
- **Depends on:** encryption
- **Feeds into:** security-audit, ci-cd

## When to use / Do NOT use

- **Use when:** a project is created, a new credential of any kind is introduced (API key, database password, signing key, service token), a deploy pipeline is set up, or a leak is suspected. This skill owns where secrets live, how they are scoped, rotated, and revoked.
- **Do NOT use when:** the question is how a secret is used once delivered — session handling belongs to session-security, request-level credential checks to api-security, and the cryptography itself to encryption. Public values (publishable keys, public analytics IDs) are not secrets and are out of scope.

## Rules

1. **SE-081 — Secrets live outside code.** Every secret is read from an environment variable or a dedicated secret manager, injected at deploy time. No secret value is written into source, tests, or committed config at any point, including "temporarily."
2. **SE-082 — `.env.example` carries names only.** The committed example file lists every required variable name with an obviously fake placeholder (`example-only-not-a-secret`) and, where a URL is needed, a reserved example host (`example.com`). A placeholder that could authenticate anywhere is a leak, not a placeholder.
3. **SE-083 — `.env` is ignored from commit one.** Every project template git-ignores `.env` before the first real value exists; `git check-ignore .env` must succeed, and no `.env` file appears in `git ls-files`.
4. **SE-084 — One credential per service per environment.** Development, staging, and production each hold distinct credentials, and no service shares another service's key. A master key reused across environments is a finding, not a shortcut.
5. **SE-085 — Nothing secret ships to the client.** Client code and client-visible environment prefixes (e.g. `NEXT_PUBLIC_*`, `VITE_*`) contain only values designed to be public. Any privileged call is proxied through a server route that holds the real secret.
6. **SE-086 — Secrets are never logged.** No secret value appears in application logs, error messages, CI output, or debug dumps; startup diagnostics print variable names and presence, never values, and CI masks secret values in job logs.
7. **SE-087 — Every secret has an owner and a rotation date.** The project secret inventory records, per secret: owner, scope, creation date, next rotation date, and the revocation procedure. Rotation happens on schedule and immediately on suspicion.
8. **SE-088 — Revocation is tested, not just documented.** Each secret's revocation path (provider console or API) is exercised at least once before launch and after any provider change, and the test date is recorded in the inventory.
9. **SE-089 — Least-privilege scope.** Each credential grants only the permissions its service needs. A broadly scoped or admin-level key standing in for a narrow one is a defect to fix, not a convenience.
10. **SE-090 — Scanning runs before commit and in CI.** A secret scanner (gitleaks or equivalent) runs as a pre-commit hook and as a CI gate over the full git history, not only the working tree. A finding blocks the merge until resolved under SE-091.
11. **SE-091 — A committed secret is public.** On any confirmed exposure the order is fixed: revoke the credential first, issue a replacement, purge the value from history, then investigate how it got there. Deleting the line without revoking is not a fix.
12. **SE-092 — One config source per environment.** Deploy-varying values come from the environment, never from per-machine hand-edited files or constants copied between services. The same artifact runs unchanged in every environment; differences are env values only.

## BAN list

- **BAN-SE-041 — Secret literal in source or tests.** Banned: an API key, password, token, or connection string written as a literal in code, tests, or fixtures. Defeats: DET-CODE-018. Bad: `const key = "sk_live_EXAMPLE-ONLY-NOT-A-SECRET"` committed in `billing.ts` (shape shown with a placeholder; a real value here is the violation). Instead: read `process.env.BILLING_SECRET_KEY` and keep the name, with a fake placeholder, in `.env.example`. Severity: BLOCK.
- **BAN-SE-042 — Live secret committed to version control.** Banned: committing a `.env` file or any tracked file containing a live credential, in any commit, including one later "removed." Defeats: DET-INF-005. Bad: `.env` with the production database password lands in the initial commit because `.gitignore` was added a week later. Instead: git-ignore `.env` from commit one (SE-083) and store the value in the platform secret store. Severity: BLOCK.
- **BAN-SE-043 — Privileged key in a client bundle.** Banned: exposing a server-side credential through a client-visible env prefix or shipped JavaScript. Defeats: DET-INF-006. Bad: the provider secret key is set as `VITE_PAYMENTS_SECRET` so the checkout page can call the API directly. Instead: the browser calls a server route; the route holds the secret and makes the privileged call. Severity: BLOCK.
- **BAN-SE-044 — Delete-without-revoke "fix."** Banned: responding to a committed secret by deleting the line or file and continuing to use the same credential. Defeats: DET-INF-005. Bad: the leaked key is removed in a follow-up commit, the team moves on, and the key stays valid — while remaining readable in git history. Instead: revoke first, replace, purge history, then investigate (SE-091). Severity: BLOCK.
- **BAN-SE-045 — Real value pasted as the "example."** Banned: putting a working credential into `.env.example`, docs, or a template as the sample value. Defeats: DET-CODE-018. Bad: `.env.example` ships with the team's real staging key filled in "so setup is faster." Instead: use an obviously fake placeholder (`example-only-not-a-secret`) and document where the real value is issued. Severity: BLOCK.

## Gates

- **G-SE-041 — Full-history secret scan.** Verifies: SE-081, SE-090. Check: run `gitleaks git .` in CI over the complete git history on every pull request and before release. Where gitleaks is unavailable in the environment, the acceptable equivalent is a documented pattern scan over the full git history (the complete history walked with the project's secret patterns — credential formats, key prefixes, high-entropy strings — e.g. via `git log -p` or `git grep` across all revisions), with the substitution and the patterns used recorded in progress.md. Pass: zero findings; placeholder hits in `.env.example` are confirmed fake per SE-082 and allowlisted individually. Fail: block merge; any confirmed live value triggers SE-091. Recorded in: progress.md.
- **G-SE-042 — Ignore and tracking check.** Verifies: SE-083. Check: `git check-ignore .env` exits 0 and `git ls-files | grep -E '(^|/)\.env$'` returns nothing. Pass: both conditions hold. Fail: block release until the file is untracked and its values rotated. Recorded in: progress.md.
- **G-SE-043 — Client bundle scan.** Verifies: SE-085. Check: download the production client bundles and grep for provider secret prefixes and key patterns (e.g. `sk_live`, service-role keys, `PRIVATE KEY`). Pass: only publishable/public keys are present. Fail: block deployment; move the call behind a server route. Recorded in: progress.md.
- **G-SE-044 — Example-file audit.** Verifies: SE-082. Check: diff the variable names in `.env.example` against the names the code reads, and inspect every example value. Pass: names match exactly and every value is an obvious placeholder on a reserved example host where a URL appears. Fail: block merge until names and placeholders are corrected. Recorded in: progress.md.
- **G-SE-045 — Inventory and revocation review.** Verifies: SE-087, SE-088, SE-089. Check: walk the secret inventory before launch and quarterly: every secret has an owner, a scope no broader than its service needs, a rotation date in the future, and a dated revocation test. Pass: no entry is missing a field. Fail: block launch for missing owners or untested revocation. Recorded in: progress.md.

## Anti-patterns

- **Rotate-later promise.** A known weak or shared credential stays in place behind a ticket that says "rotate soon." Catch it: if the inventory shows a rotation date that has already slipped once, treat it as a defect now, not a plan.
- **Secrets shared through chat and tickets.** A credential is pasted into a chat message, issue, or doc "so the team has it," creating uncontrolled copies no scan will find. Catch it: any secret that has traveled by chat is rotated and re-issued through the secret store.
- **Startup env dump.** The app prints its full environment or resolved config at boot for debugging, and the dump survives into production logs. Catch it: grep boot code for env/config printing; diagnostics name variables, never values (SE-086).
- **One vault, no scopes.** All secrets sit in a single store entry or file that every service and environment reads wholesale, so any one compromise exposes everything. Catch it: access is granted per service per environment (SE-084); a service that can read another service's secrets is the tell.

## Examples

- [Example 1 — Hardcoded key in source](examples/example-1.md) — violates/corrects SE-081, SE-082 (BAN-SE-041).
- [Example 2 — Secret shipped to the browser](examples/example-2.md) — violates/corrects SE-085 (BAN-SE-043).
- [Example 3 — Leak deleted but not revoked](examples/example-3.md) — violates/corrects SE-091 (BAN-SE-044).

## Recall anchors

- If it is in the repo, the bundle, or the log, it is public — treat it that way.
- Names in `.env.example`, values in the secret store, never the reverse.
- One key per service per environment; a shared master key is a finding.
- Leaked means revoked first, investigated second — deletion is not a fix.
- Every secret: an owner, a scope, a rotation date, a tested way to kill it.

## Checklist

- [ ] `git check-ignore .env` succeeds and no `.env` is tracked (G-SE-042).
- [ ] `gitleaks git .` over full history reports zero findings — or, where gitleaks is unavailable, the documented pattern-scan equivalent over the full history reports zero findings, with the substitution recorded in progress.md (G-SE-041).
- [ ] `.env.example` names match the code exactly and hold only obvious placeholders (G-SE-044).
- [ ] Production client bundles contain no privileged key patterns (G-SE-043).
- [ ] Each credential is unique per service and per environment, scoped least-privilege (SE-084, SE-089).
- [ ] Secret inventory lists owner, rotation date, and a dated revocation test for every secret (G-SE-045).
- [ ] Logs and CI output print variable names only, with secret masking enabled (SE-086).
