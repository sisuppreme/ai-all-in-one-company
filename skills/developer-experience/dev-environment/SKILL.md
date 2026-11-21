# dev-environment

## Metadata

- **Owner department:** D15 Developer Experience (DX)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://containers.dev/implementors/json_reference/ ; https://mise.jdx.dev/dev-tools/ ; https://12factor.net/config
- **Depends on:** none — standalone: setup is derived from the project's own repo (its manifests, version pins, and environment variables) so a fresh machine can run it; it is a starting-point skill and consumes no other skill's output. It feeds monorepo-tooling and dependency-management.
- **Feeds into:** monorepo-tooling, dependency-management

## When to use / Do NOT use

- **Use when:** a project is created or handed over; a new machine, container, or CI runner must reach a running app; setup instructions, tool versions, or environment variables are being written or changed.
- **Do NOT use when:** the question is which versions to bump in an existing dependency set (use dependency-management), how releases are numbered (use versioning), or how production is deployed (use D6 deployment skills) — this skill covers the local development environment only.

## Rules

1. **DX-001 — One bootstrap command.** Exactly one documented command (e.g. `make setup`, `npm run setup`, or `mise install` plus the install step) takes a clean clone to a running app with the test suite passing. Any second manual step is a defect in the setup, not a README footnote.
2. **DX-002 — One pin file.** Every runtime and CLI tool version is declared exactly once, in one committed pin file (`mise.toml`, `.tool-versions`, or the ecosystem equivalent). No other file restates a tool version.
3. **DX-003 — Exact pins, never "latest".** The pin file and dependency manifests carry exact versions for tools and application dependencies. Floating references (`latest`, `*`, unpinned "current LTS") are not permitted anywhere in setup instructions or config.
4. **DX-004 — Lockfile committed, installs frozen.** The dependency lockfile is committed, and local and CI installs run in frozen/CI mode (`npm ci`, `--frozen-lockfile`, or equivalent) so an install never silently rewrites the resolved set.
5. **DX-005 — `.env.example` is complete.** Every variable the code reads appears in `.env.example` with a placeholder value and a one-line purpose note. A variable read by code but missing from the example file is a defect.
6. **DX-006 — Placeholders only.** Example files contain only obviously non-functional values (`change-me`, `sk_test_...`, reserved example hosts). No real secret, token, or connection string appears in any committed file, example or otherwise.
7. **DX-007 — Config fails fast.** The app validates required configuration at startup and exits non-zero, naming each missing or malformed variable. There is no silent fallback to a default environment, host, or credential.
8. **DX-008 — Setup is idempotent.** Running the bootstrap command a second time changes nothing and breaks nothing: no duplicate installs, no clobbered local config, no appended duplicates in generated files.
9. **DX-009 — CI runs the same pins.** CI installs the toolchain from the same pin file and the dependencies from the same lockfile as a laptop. A CI-only version override is drift, treated as a defect under DX-002.
10. **DX-010 — Services are declared, not hand-started.** When the app needs backing services (database, cache, queue), they are declared in `.devcontainer/devcontainer.json` and/or a compose file committed with the project, and the bootstrap starts them. "Start Postgres locally first" is not a setup step.
11. **DX-011 — Config comes from the environment.** Per-deploy values arrive as environment variables (Twelve-Factor Factor III), strictly separate from code. Code contains no `if (environment === "prod")` branches selecting hardcoded URLs, hosts, or credentials.
12. **DX-012 — README references, never restates.** The README names the bootstrap command and links the pin file and `.env.example`. It restates no version numbers and no variable lists, so there is exactly one place each can drift from.

## BAN list

- **BAN-DX-001 — Real secret in an example or config file.** Banned: a working API key, password, or connection string committed in `.env.example`, a config sample, or source. Defeats: DET-CODE-018. Bad: `.env.example` ships with the project's live Stripe key copied from the dashboard "so the demo works." Instead: placeholder values only, per DX-006. Severity: BLOCK.
- **BAN-DX-002 — Floating tool versions.** Banned: setup instructions or manifests that install `latest`, a wildcard range, or an unpinned "current LTS" for any runtime or CLI tool. Defeats: DET-CODE-028. Bad: the README says "install Node (latest LTS) and the newest Docker." Instead: pin the exact version in the pin file and install from it, per DX-002 and DX-003. Severity: BLOCK.
- **BAN-DX-003 — Setup steps outside the bootstrap.** Banned: any required setup step that lives only in a wiki, chat message, or a human's memory instead of the bootstrap command. Defeats: DET-CODE-032. Bad: after cloning, a new developer must "ask in chat for the extra step" that creates the local storage bucket. Instead: fold the step into the bootstrap command, per DX-001. Severity: BLOCK.
- **BAN-DX-004 — Silent default to production.** Banned: a fallback that points the app at a production host, database, or credential when a configuration variable is unset. Defeats: DET-CODE-020. Bad: `DATABASE_URL` defaults to the production database URL when the variable is missing, so a misconfigured laptop writes to prod. Instead: no default for environment-selecting variables; fail fast naming the variable, per DX-007. Severity: BLOCK.
- **BAN-DX-005 — A committed real `.env` file.** Banned: committing a `.env` (or equivalent) containing real values, or leaving it out of `.gitignore`. Defeats: DET-CODE-018. Bad: `.env` with the real database password is tracked in git "temporarily" and never removed from history. Instead: commit `.env.example` with placeholders only and gitignore the real file, per DX-005 and DX-006. Severity: BLOCK.

## Gates

- **G-DX-001 — Fresh-clone bootstrap test.** Verifies: DX-001, DX-008, DX-010. Check (automated): in a clean container or VM, `git clone <repo> test-clone && cd test-clone && <bootstrap command>`, then run the test suite and the app's health check; run the bootstrap a second time and repeat. Pass: app starts, tests pass, second run changes nothing, and zero undocumented steps were needed. Fail: block shipment. Recorded in: progress.md.
- **G-DX-002 — Example-file secret scan.** Verifies: DX-006. Check (automated): run a secret scanner (gitleaks or equivalent) over the tree, plus `git grep -nE "sk_live|AKIA[0-9A-Z]{16}|BEGIN [A-Z ]*PRIVATE KEY" -- .env.example "*.example" "*.sample"` must return nothing. Pass: zero hits and every example value is an obvious placeholder. Fail: block shipment. Recorded in: progress.md.
- **G-DX-003 — Pin singularity and CI parity check.** Verifies: DX-002, DX-003, DX-009, DX-012. Check (automated): the pin file exists; `grep -rniE "latest" README.md docs/ <setup files>` returns no install instruction using it; CI configuration references the pin file and frozen install mode rather than naming its own tool versions. Pass: one pin file, referenced by CI, no floating versions anywhere. Fail: block shipment. Recorded in: progress.md.
- **G-DX-004 — Environment-variable coverage check.** Verifies: DX-005. Check (automated): extract variable names read by the code (e.g. `grep -rhoE "process\.env\.[A-Z_]+|os\.environ\[\"[A-Z_]+\"\]" src/`), extract keys from `.env.example`, and diff. Pass: zero variables missing from `.env.example`, and every entry has a purpose note. Fail: block shipment. Recorded in: progress.md.
- **G-DX-005 — Fail-fast startup check.** Verifies: DX-007, DX-011. Check (automated): start the app with one required variable unset, then with it set to a malformed value. Pass: both runs exit non-zero with an error naming the variable; no run silently connects to a default environment. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **Bootstrap that "mostly works."** The setup script prints warnings, skips failed steps, and exits 0, leaving a half-built environment that fails later in confusing ways. Catch it by checking the bootstrap's exit code on an induced failure — it must be non-zero.
- **Pin file present but bypassed.** The pin file exists, but developers actually run globally installed tools and only CI uses the pins, so version bugs surface at release time. Catch it by asking what `which <tool>` resolves to in a fresh shell after bootstrap — it must be the pinned install.
- **`.env.example` updated "later."** New variables land in code during feature work while the example file waits for a cleanup pass that never comes. Catch it by running G-DX-004 on every change that touches configuration reads, not only at release.
- **Warm-machine timing.** Setup is declared "fast" based on the author's machine with warm caches and pre-installed tools. Catch it by timing only the clean-container run from G-DX-001 and recording that number.

## Examples

- [Example 1 — The nine-step README](examples/example-1.md) — violates/corrects DX-001, DX-002.
- [Example 2 — The example file with a real key](examples/example-2.md) — violates/corrects DX-005, DX-006, DX-007.
- [Example 3 — CI on a different Node](examples/example-3.md) — violates/corrects DX-003, DX-009.

## Recall anchors

- One command from clone to running — a second manual step is a defect.
- Versions live in one pin file; docs reference it, never restate it.
- Examples hold placeholders; real secrets live nowhere in git.
- Missing config fails fast and names the variable — never defaults to prod.
- If it only works on your machine, the gate has failed, not the machine.

## Checklist

- [ ] One bootstrap command reaches a running app with tests green from a clean clone (DX-001, G-DX-001).
- [ ] Every tool version pinned exactly once in one committed pin file; no `latest` anywhere (DX-002, DX-003, G-DX-003).
- [ ] Lockfile committed; installs run frozen/CI mode locally and in CI (DX-004).
- [ ] `.env.example` lists every variable the code reads, with placeholder value and purpose note (DX-005, G-DX-004).
- [ ] Secret scan over examples and tree returns zero real credentials (DX-006, G-DX-002).
- [ ] App fails fast, naming any missing or malformed required variable (DX-007, G-DX-005).
- [ ] Bootstrap run twice in the clean test with no change on the second run (DX-008, G-DX-001).
- [ ] CI installs from the same pin file and lockfile as a laptop (DX-009, G-DX-003).
- [ ] Backing services declared in devcontainer/compose and started by the bootstrap (DX-010).
