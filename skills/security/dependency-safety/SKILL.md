# dependency-safety

## Metadata

- **Owner department:** D7 Security (SE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://osv.dev/ ; https://owasp.org/www-project-top-ten/
- **Depends on:** none — standalone: it works from the project's own manifests, lockfiles, and published vulnerability advisories — primary sources read directly, not another skill's output. Its hygiene rules feed supply-chain.
- **Feeds into:** supply-chain

## When to use / Do NOT use

- **Use when:** adding, updating, or removing a dependency; setting up CI for a project; preparing a release; triaging a vulnerability alert; choosing or pinning a base image.
- **Do NOT use when:** the question is how the release artifact itself was built, signed, or provenance-attested — that is supply-chain. License legality beyond a compatibility flag is D14 licensing.

## Rules

1. **SE-101 — The lockfile is the build input.** A lockfile pinning every direct and transitive version is committed, and CI installs from it with the frozen/locked mode of the stack (`npm ci`, `pip install --require-hashes`, or equivalent). A build that resolves versions at install time fails this rule by definition.
2. **SE-102 — One SBOM per release.** CI generates an SBOM (CycloneDX or SPDX) from the shipped manifest for every release and stores it with the release artifacts.
3. **SE-103 — Scanning runs in CI and on a schedule.** A vulnerability scanner (OSV-Scanner, `npm audit`, `pip-audit`, or the stack equivalent) runs on every change and on a recurring schedule against the last released manifest; a scheduled run that finds a new critical opens an alert, not just a log line.
4. **SE-104 — Reachable criticals and highs block release.** A critical or high vulnerability in a reachable dependency stops the release until fixed. An unreachable or disputed finding is exempted only by a written, dated analysis (for example a VEX note) naming the finding, the reachability reasoning, and a review-by date.
5. **SE-105 — Update automation is on.** Dependabot, Renovate, or the platform equivalent is configured for every manifest and base image in the repo; security fixes are fast-tracked as individual PRs, routine updates are batched on a stated cadence, and opened update PRs are merged or explicitly rejected — never left to rot.
6. **SE-106 — New dependencies pass an adoption check.** Before a dependency is added, the PR records: it is actively maintained, its license is compatible (flag conflicts to D14 licensing), and it is actually needed over the standard library or an existing dependency.
7. **SE-107 — Install scripts are code execution.** The install/postinstall scripts of a new or updated dependency are read before merge, exactly as its library code would be; an unread install script blocks the merge.
8. **SE-108 — Abandoned and lookalike packages are rejected at adoption.** A package with no maintenance activity, or whose name is a lookalike of a popular package, is not adopted; if it is already in the tree, it gets a replacement plan or a dated risk acceptance under SE-104's format.
9. **SE-109 — Scanners run against what ships.** Scanning covers the production manifest and the final built image, not only the development tree; a green dev-tree scan is not evidence about the shipped artifact.
10. **SE-110 — Base images are pinned and rebuilt on a cadence.** Base images are pinned by digest, rebuilt on a stated cadence so OS patches flow in, and the rebuild is verified by a scan of the new image before it replaces the old one.
11. **SE-111 — The manifest stays coherent.** Every manifest entry is imported or used by the build, every import resolves to a manifest entry, and no version range is a wildcard or `latest`; removals prune the entry in the same change.
12. **SE-112 — Suppressions expire.** Every scanner suppression carries the finding ID, the justification, and an expiry date; expired suppressions fail CI until re-justified or fixed. There are no permanent global ignores.

## BAN list

- **BAN-SE-051 — Floating versions or a missing lockfile.** Banned: a manifest with `*`/`latest` ranges, or CI installing without a committed lockfile. Defeats: DET-CODE-028. Bad: `"express": "*"` in package.json and CI running plain `npm install`. Instead: pin exact versions, commit the lockfile, and install in CI with `npm ci`. Severity: BLOCK.
- **BAN-SE-052 — Muting a critical or high finding without analysis.** Banned: adding a CVE to a scanner ignore list with no written reachability analysis. Defeats: DET-INF-025. Bad: `.osv-scanner.toml` gains an ignore entry commented "probably fine". Instead: fix the dependency, or file a dated VEX note with reachability reasoning and a review-by date (SE-104). Severity: BLOCK.
- **BAN-SE-053 — Merging a dependency whose install scripts nobody read.** Banned: adding or updating a package with install/postinstall hooks without reviewing what they execute. Defeats: DET-CODE-028. Bad: a PR adds a package whose postinstall downloads and runs a remote binary; the diff is approved on the version number alone. Instead: read the install scripts, record the review in the adoption check (SE-106, SE-107), then merge. Severity: BLOCK.
- **BAN-SE-054 — Unpinned base images.** Banned: a Dockerfile or deploy config referencing a mutable tag such as `latest` for a production base image. Defeats: DET-INF-026. Bad: `FROM node:latest`. Instead: pin by digest (`FROM node:22-bookworm-slim@sha256:<digest>`) and rebuild on the SE-110 cadence. Severity: BLOCK.
- **BAN-SE-055 — Known-bad dependency kept indefinitely with no decision on record.** Banned: a dependency with an unpatched critical/high CVE stays in the shipped tree release after release with no fix, VEX note, or risk acceptance. Defeats: DET-INF-025. Bad: the same critical finding appears in three consecutive release scans, acknowledged in chat each time, written down nowhere. Instead: fix it, replace it, or record a dated risk acceptance with an owner and a review-by date. Severity: BLOCK.

## Gates

- **G-SE-051 — CI vulnerability gate (automated).** Verifies: SE-103, SE-104. Check: CI runs `osv-scanner --lockfile=<committed lockfile>` (or `npm audit --audit-level=high` / `pip-audit` for the stack) on every PR and on the release branch. Pass: exit code 0 — no critical or high finding without an unexpired SE-104 analysis on file. Fail: merge and release are blocked. Recorded in: progress.md.
- **G-SE-052 — Lockfile presence and sync (automated).** Verifies: SE-101, SE-111. Check: CI fails if no lockfile is committed, and a frozen install (`npm ci` or equivalent) succeeds without modifying it. Pass: lockfile present, in sync with the manifest, and unchanged by install. Fail: block merge; regenerate and commit the lockfile. Recorded in: progress.md.
- **G-SE-053 — SBOM artifact check (automated).** Verifies: SE-102. Check: the release job emits an SBOM file (CycloneDX or SPDX) generated from the shipped manifest and attaches it to the release. Pass: SBOM exists, parses, and its component count matches the lockfile's package count. Fail: release is blocked until the SBOM is produced. Recorded in: progress.md.
- **G-SE-054 — Scheduled rescan of the shipped artifact (automated).** Verifies: SE-103, SE-109. Check: a scheduled workflow (at least weekly) scans the last released manifest and final image and files an alert on any new critical or high. Pass: the schedule exists, its last run is under 8 days old, and its target is the released artifact — not the dev tree. Fail: treat as a missing control; fix the schedule before the next release. Recorded in: progress.md.
- **G-SE-055 — Adoption review (manual).** Verifies: SE-106, SE-107, SE-108. Check: for every PR that adds a dependency, the PR record shows the maintenance check, the license flag, the need justification, and the install-script review. Pass: all four items recorded for every added dependency. Fail: the dependency is removed or the record is completed before merge. Recorded in: progress.md.

## Anti-patterns

- **Scanner-green theater.** The scanner runs in CI but its exit code is ignored or its threshold is set so high nothing can fail; the pipeline is green while findings pile up. Catch it by checking that a deliberately vulnerable test branch actually fails G-SE-051.
- **Automation without follow-through.** Dependabot/Renovate PRs open on schedule and are never merged or rejected, so the inventory looks managed while nothing is ever patched. Catch it by counting update PRs older than the stated cadence.
- **Borrowed suppressions.** An ignore list or VEX note is copied from another project (or an older release) without re-checking reachability in this codebase. Catch it by sampling suppressions and asking for the analysis behind each.
- **Dev-tree confidence.** A "0 vulnerabilities" claim sourced from a scan that included devDependencies but never touched the production image. Catch it by asking which manifest and image the scan ran against (SE-109).

## Examples

- [Example 1 — Floating range, no lockfile](examples/example-1.md) — violates/corrects SE-101, SE-111 (BAN-SE-051).
- [Example 2 — Muted critical vs. VEX note](examples/example-2.md) — violates/corrects SE-104, SE-112 (BAN-SE-052).
- [Example 3 — Unpinned base image](examples/example-3.md) — violates/corrects SE-110 (BAN-SE-054).

## Recall anchors

- The lockfile is the build input; resolution at install time is unreviewed by definition.
- Reachable critical blocks release; unreachable needs a dated VEX note, not a mute.
- Install scripts are code execution — read them before merge.
- Scan what ships: production manifest and final image, not the dev tree.
- Suppressions expire; update PRs get merged or rejected, never left to rot.

## Checklist

- [ ] Lockfile committed, in sync, and CI installs from it in frozen mode (SE-101, G-SE-052).
- [ ] SBOM generated for this release and stored with the artifacts (SE-102, G-SE-053).
- [ ] CI scan passes with no unexempted critical/high findings (SE-103, SE-104, G-SE-051).
- [ ] Every suppression has a finding ID, justification, and unexpired date (SE-112).
- [ ] Scheduled rescan targets the last released manifest and image (SE-109, G-SE-054).
- [ ] Update automation is configured and no update PR is older than the cadence (SE-105).
- [ ] Every newly added dependency has a recorded adoption check, including install-script review (SE-106, SE-107, SE-108, G-SE-055).
- [ ] Base images are digest-pinned and within their rebuild cadence (SE-110).
