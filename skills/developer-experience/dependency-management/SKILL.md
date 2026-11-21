# dependency-management

## Metadata

- **Owner department:** D15 Developer Experience (DX)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Dependabot version updates — https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/configure-version-updates ; Renovate npm manager and lockfile maintenance — https://docs.renovatebot.com/modules/manager/npm/
- **Depends on:** dev-environment (toolchain pins the installs run under), tech-debt (debt register holds stale-update reasons)
- **Feeds into:** dependency-safety (D7 — receives routed advisories), versioning

## When to use / Do NOT use

- **Use when:** adding, updating, pinning, or removing a dependency; configuring update automation; reviewing a change that touches the manifest or the lockfile.
- **Do NOT use when:** responding to a published vulnerability or a compromised package — that is D7's dependency-safety, which owns advisory triage, patch SLAs, and incident response. This skill owns the everyday discipline of choosing, pinning, and updating dependencies; it routes advisories to D7 and never runs a parallel security process.

## Rules

1. **DX-061 — The lockfile is committed and canonical.** The lockfile is version-controlled next to the manifest. A change that edits one without the other is incomplete and does not merge.
2. **DX-062 — Installs are frozen and reproducible.** Local setup and CI install from the lockfile in frozen mode (`npm ci`, `pnpm install --frozen-lockfile`, or the ecosystem equivalent). An install that modifies the lockfile is a failed install, not a fix.
3. **DX-063 — Every new direct dependency is justified in one line.** The change description states what the package does, why the standard library and the existing dependencies do not cover it, and its maintenance status. No justification, no merge.
4. **DX-064 — Update automation is configured in the repo.** A committed `.github/dependabot.yml` or `renovate.json` drives updates: minor and patch grouped, majors individual, security updates ungrouped and immediate. The config validates against its schema.
5. **DX-065 — Updates land in small, reviewed batches.** Grouped minor/patch updates merge as small batches; a major update is its own change. A single change never bumps many unrelated packages at once.
6. **DX-066 — Read the changelog before a major update.** The change description names the breaking changes from the release notes and the code changes they required. "Tests pass" alone is not a major-update review.
7. **DX-067 — Version ranges are deliberate.** Applications pin exact versions. Caret ranges appear only in published libraries where the ecosystem convention makes them the consumer contract. Wildcard ranges are prohibited (BAN-DX-032).
8. **DX-068 — No stale update without a recorded reason.** No update PR or report entry stays unaddressed past the project's stated window (default 30 days) unless the debt register records why and when it will be taken.
9. **DX-069 — Dead and duplicate dependencies are removed.** A package nothing imports is deleted from the manifest in the same change that removed its last use; two packages serving one job collapse to one. Removal is part of the work, not a later cleanup.
10. **DX-070 — The manifest stays coherent.** Every manifest entry is imported, or its build/plugin role is documented in the manifest's config; every import resolves to a declared entry. Transitive packages are never imported directly.
11. **DX-071 — Advisories route to D7, currency stays here.** Audit findings are handed to dependency-safety for triage and patching priority; this skill's job is only to keep versions current enough that D7's patches are small. Never sit on a known advisory because "the update is scheduled."
12. **DX-072 — An update merges only on a green suite.** The full test suite passes in CI on the updated tree, installed frozen from the updated lockfile, before any update change merges.

## BAN list

- **BAN-DX-031 — Uncommitted or casually regenerated lockfile.** Banned: deleting the lockfile and regenerating it inside an unrelated change, or leaving it out of version control. Defeats: DET-CODE-028. Bad: a feature PR deletes `package-lock.json` and commits a fresh one, silently moving 40 transitive versions. Instead: regenerate the lockfile only in a dedicated update change whose diff is the review. Severity: BLOCK.
- **BAN-DX-032 — Wildcard or `latest` version ranges.** Banned: `"*"`, `latest`, or an open range in any manifest entry. Defeats: DET-CODE-028. Bad: `"axios": "*"` installs whatever exists on the day of the build. Instead: pin the exact version for applications; use a caret range only for a published library per DX-067. Severity: BLOCK.
- **BAN-DX-033 — Manifest and lockfile changed out of step.** Banned: a change that edits the manifest without the lockfile, or the lockfile without the manifest. Defeats: DET-CODE-028. Bad: `package.json` gains a dependency; the lockfile is "fixed later," so CI and the author's machine resolve different trees. Instead: generate both in the same local install and commit them together (DX-061). Severity: BLOCK.
- **BAN-DX-034 — Duplicate libraries for one job.** Banned: two packages serving the same purpose in one codebase (two date libraries, two HTTP clients, two validation libraries). Defeats: DET-CODE-028. Bad: `moment` is added to a project already using `dayjs` because one snippet online used it. Instead: use the package already in the tree; if the new one is genuinely better, migrate fully and remove the old in the same change. Severity: BLOCK.
- **BAN-DX-035 — Hand-edited lockfile.** Banned: editing lockfile entries by hand to force a version, instead of changing the manifest and letting the package manager resolve. Defeats: DET-CODE-028. Bad: a version string inside `package-lock.json` is edited to silence a conflict; the next install rewrites it and the build changes. Instead: express the constraint in the manifest (pin, override field) and regenerate the lockfile with the package manager. Severity: BLOCK.

## Gates

- **G-DX-031 — Frozen-lockfile install.** Verifies: DX-061, DX-062. Check: in a clean CI checkout run `npm ci` (or the ecosystem frozen equivalent), then `git status --porcelain`. Pass: install exits 0 and the lockfile shows no modification. Fail: block merge; the manifest/lockfile pair is regenerated and recommitted. Recorded in: progress.md.
- **G-DX-032 — Production audit threshold.** Verifies: DX-071. Check: run `npm audit --production` / `pip-audit` / ecosystem equivalent in CI. Pass: no high or critical advisories in production dependencies; any finding is logged and routed to D7 dependency-safety the same day. Fail: block release until D7 triages. Recorded in: progress.md.
- **G-DX-033 — Update-bot config present and valid.** Verifies: DX-064. Check: assert `.github/dependabot.yml` or `renovate.json` exists and validate it (`npx renovate-config-validator` or the Dependabot schema check). Pass: file present, schema-valid, majors ungrouped, security updates ungrouped. Fail: block; add or fix the config before further dependency work. Recorded in: progress.md.
- **G-DX-034 — Stale-dependency report.** Verifies: DX-065, DX-068. Check: run `npm outdated` (or equivalent) and list direct dependencies more than one major behind, or with an update unaddressed past the 30-day window. Pass: the list is empty, or every entry has a debt-register reason with a take-by date. Fail: warn and register the items before the next feature change. Recorded in: progress.md.
- **G-DX-035 — Manifest coherence scan.** Verifies: DX-069, DX-070. Check: run `npx depcheck` (or equivalent) and diff the import list against the manifest. Pass: no unused and no missing dependencies, except build/plugin packages documented in config. Fail: block; remove or declare before merge. Recorded in: progress.md.

## Anti-patterns

- **Dependency as first resort.** A package is added for a ten-line job the standard library already does. Catch it at the DX-063 justification line: if it cannot name why the platform fails, the package does not enter.
- **Phantom transitive imports.** Code imports a package that only arrives transitively through another dependency; it breaks without warning when the parent updates. Catch it with G-DX-035 and by asking of every import: is this declared by us?
- **The update snowball.** Update PRs are ignored for months until dozens of majors, some breaking, must land together under time pressure. Catch it by watching the G-DX-034 report trend, not its snapshot.
- **Manifest copied from another project.** A new project starts by pasting a familiar manifest wholesale, inheriting packages nothing will import. Catch it at the first coherence scan: every entry must trace to a use in this project.

## Examples

- [Example 1 — A second date library for one snippet](examples/example-1.md) — violates/corrects DX-063, DX-069.
- [Example 2 — Wildcard range and a regenerated lockfile](examples/example-2.md) — violates/corrects DX-061, DX-067.
- [Example 3 — One giant "update everything" change](examples/example-3.md) — violates/corrects DX-065, DX-066.

## Recall anchors

- The manifest is the intent; the lockfile is the truth.
- Every dependency is inventory: justified, pinned, pruned.
- Majors land one at a time, changelog in hand.
- Security response belongs to D7; currency belongs here.
- If nothing imports it, it does not stay.

## Checklist

- [ ] Lockfile committed, and a frozen install leaves it unchanged (G-DX-031).
- [ ] Every new direct dependency carries its one-line justification (DX-063).
- [ ] Update-bot config exists, validates, and keeps majors and security updates ungrouped (G-DX-033).
- [ ] No update is past the stale window without a debt-register reason (G-DX-034).
- [ ] Coherence scan is clean: nothing unused, nothing missing, no transitive imports (G-DX-035).
- [ ] Major updates landed individually with their breaking changes named (DX-065, DX-066).
- [ ] Full suite green on the updated tree before merge (DX-072).
