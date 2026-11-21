# versioning

## Metadata

- **Owner department:** D15 Developer Experience (DX)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://semver.org/ ; https://www.conventionalcommits.org/en/v1.0.0/ ; https://keepachangelog.com/en/2.0.0/
- **Depends on:** changelog
- **Feeds into:** dependency-management

## When to use / Do NOT use

- **Use when:** cutting any release of a library, package, API, or deployed app; choosing the next version number; deprecating or removing a public feature; withdrawing a bad release; setting up a project's release process.
- **Do NOT use when:** versioning an HTTP API's URL/contract scheme itself (use api-versioning in D2 — this skill supplies the SemVer contract and deprecation window it builds on), or recording what changed in prose (use changelog in D10 — this skill governs the number, the tag, and their consistency).

## Rules

1. **DX-141 — SemVer 2.0.0 is the public contract.** Every published package, library, and API carries a version of the form MAJOR.MINOR.PATCH with SemVer precedence rules: MAJOR for incompatible changes, MINOR for backward-compatible functionality, PATCH for backward-compatible fixes. No other numbering scheme (dates, codenames, "final") is used for the same artifact.
2. **DX-142 — One source of truth for the version.** The version string lives in exactly one place — the package manifest or the git tag, as the project declares — and every other appearance (docs, banners, generated files, `--version` output) is read or generated from that source. No file is hand-edited to "also" update the version.
3. **DX-143 — The bump is derived, not chosen.** The next bump is computed from the Conventional Commits in the range since the last release tag: any `BREAKING CHANGE:` footer or `!` → MAJOR; else any `feat:` → MINOR; else PATCH. The highest signal wins, and the release notes state the derivation. A bump that disagrees with the derivation is a defect.
4. **DX-144 — Breaking changes force a major bump and a migration note.** Any incompatible change to the public API — removed or renamed symbols, changed signatures, changed defaults or behavior consumers rely on — ships only under a new MAJOR version, and its changelog entry carries a migration note saying what consumers must change. There is no "small breaking change" exception.
5. **DX-145 — Deprecation precedes removal.** A public feature is marked deprecated in at least one MINOR release (libraries/APIs) before it is removed in a MAJOR release, announced in the changelog's Deprecated section with the replacement named. Removal without a prior deprecation release is a process failure, not a shortcut.
6. **DX-146 — Pre-1.0 is an explicit, declared state.** While the major version is 0, the project states in its README that anything may change; within 0.x, incompatible changes bump MINOR and compatible features bump PATCH. Version 1.0.0 is cut when the public API becomes a real commitment consumers are invited to depend on — not when the code feels old enough.
7. **DX-147 — Pre-release and build metadata follow the SemVer grammar.** Pre-release suffixes are dot-separated identifiers (`1.0.0-alpha.1`, `1.0.0-rc.2`) with no leading zeros in numeric identifiers; build metadata (`+build.5`) never affects precedence and is never the only difference between two published artifacts. Invented suffixes outside the grammar (`-final`, `-new`, `-v2`) are invalid versions.
8. **DX-148 — A released version is immutable.** Once a version is tagged and published, its code and artifacts are never modified, re-tagged, or republished. A fix ships as a new PATCH version. If the tag must move because the release was cut in error before publication, that fact is recorded in progress.md with the reason — after publication, never.
9. **DX-149 — A release is a consistent triple.** Each release produces, in one release commit: a git tag `vX.Y.Z`, the manifest version set to the identical string (without the `v`), and the top CHANGELOG version heading with the same number and an ISO 8601 date. If any of the three disagrees, the release is not done.
10. **DX-150 — The changelog is the consumer record of versions.** Releases move entries from `[Unreleased]` into a new version section, grouped by the six Keep a Changelog types (Added, Changed, Deprecated, Removed, Fixed, Security), written for consumers — what changed for them — with breaking changes marked in place. Entries are added under `[Unreleased]` as work lands, not reconstructed from memory at release time.
11. **DX-151 — Yanked releases stay in history, marked.** A withdrawn release is marked `[YANKED]` in the changelog with the date and reason, and its tag remains. Deleting the section, the tag, or the artifact record so the version "never happened" destroys the trace consumers need when they are pinned to it.
12. **DX-152 — Deployed apps version for traceability.** A deployed web app still tags every production deployment and keeps the changelog; its version is an internal traceability device (deployment → tag → exact commit), so bump rules may relax but DX-148 and DX-149 do not. Every bug report and incident note cites the deployed version or tag it was observed on.

## BAN list

- **BAN-DX-071 — Silent re-tag or republish.** Banned: moving a version tag to a different commit, or replacing a published artifact, so the same version number names different code. Defeats: DET-CODE-031. Bad: the 2.3.1 tag is force-moved to include a late fix; users who installed "2.3.1" yesterday run different code from users who install it today. Instead: publish the fix as 2.3.2 with its own tag and changelog entry (DX-148). Severity: BLOCK.
- **BAN-DX-072 — Breaking change under a minor or patch bump.** Banned: shipping an incompatible API change while bumping only MINOR or PATCH, because the change "feels small." Defeats: DET-CODE-028. Bad: `getUser(id)` changes its return shape in 1.4.1, a patch release; every consumer's manifest promised compatibility the content does not have. Instead: bump MAJOR and write the migration note (DX-144). Severity: BLOCK.
- **BAN-DX-073 — Version hand-edited in several places.** Banned: updating the version by editing the manifest, a source constant, and the docs independently, so the copies can disagree. Defeats: DET-CODE-032. Bad: manifest says 3.0.0, the app banner still renders 2.9.4 from a hardcoded string, and support cannot tell which build a user runs. Instead: keep one source of truth and generate or read every other display from it (DX-142). Severity: BLOCK.
- **BAN-DX-074 — Non-SemVer release identity.** Banned: releasing under an identity that is not a valid SemVer version — `latest`, `final`, `1.0`, `2.0-new`, or a date — for a versioned artifact. Defeats: DET-CODE-028. Bad: the download page offers "app-final-v2.zip" and the manifest says `"version": "1.0"`. Instead: assign the next derived SemVer version and tag it (DX-141, DX-143, DX-147). Severity: BLOCK.
- **BAN-DX-075 — Erasing a withdrawn release.** Banned: deleting a yanked version's changelog section, tag, or release record instead of marking it withdrawn. Defeats: DET-CODE-031. Bad: after a broken 4.1.0 is pulled, its changelog section is deleted; consumers pinned to 4.1.0 find no record it ever existed or why it vanished. Instead: mark it `[YANKED]` with the date and reason, tag intact (DX-151). Severity: BLOCK.

## Gates

- **G-DX-071 — Version triple equality (automated).** Verifies: DX-142, DX-149. Check: extract the manifest version (`node -p "require('./package.json').version"` or the ecosystem equivalent), the newest tag (`git describe --tags --abbrev=0`), and the top CHANGELOG version heading; assert all three are the identical version string. Pass: exact match. Fail: block shipment; fix the out-of-line copy from the source of truth, never by editing all three by hand. Recorded in: progress.md.
- **G-DX-072 — Bump derivation check (automated).** Verifies: DX-143. Check: run commit lint (commitlint with the Conventional Commits config) over `git log <last-tag>..HEAD`, compute the derived bump from the commit types, and compare it with the bump actually taken between the last tag and the candidate version. Pass: lint clean and derived bump equals actual bump. Fail: block shipment; either correct the version or correct the commit record — never ship a number the history does not justify. Recorded in: progress.md.
- **G-DX-073 — Breaking-change / major-bump check (automated).** Verifies: DX-144. Check: diff the public contract against the last release (OpenAPI diff for APIs, exported-symbol diff for libraries); if the diff reports a breaking change, assert the candidate version's MAJOR is exactly one greater and MINOR/PATCH are zero. Pass: no breaking change, or major bumped. Fail: block shipment until the bump is corrected and the migration note exists. Recorded in: progress.md.
- **G-DX-074 — Immutability and grammar check (automated).** Verifies: DX-147, DX-148. Check: validate the candidate version against the official SemVer regular expression from semver.org, and confirm every existing release tag still points at the commit recorded for it at its release (compare `git rev-parse vX.Y.Z^{commit}` against the release record in progress.md). Pass: version is valid SemVer and no tag has moved. Fail: block shipment; a moved tag is restored or the change is shipped as a new version. Recorded in: progress.md.
- **G-DX-075 — Release record review (manual).** Verifies: DX-145, DX-150, DX-151. Check: read the new changelog section as a consumer: entries grouped by the six types, breaking changes marked with migration notes, anything removed was announced as Deprecated at least one minor release earlier, and any withdrawn release in the period is marked `[YANKED]` with a reason. Pass: all four hold. Fail: warn and complete the record before the next release; a missing prior deprecation blocks the removal itself. Recorded in: progress.md.

## Anti-patterns

- **Version inflation.** Major versions bumped for marketing ("Version 10!") or minor versions used as a progress diary, until the number carries no compatibility information and consumers stop trusting it. Catch it by asking what the derived bump (G-DX-072) says — if the release story and the commit history tell different stories, the number is decoration.
- **Release-time changelog archaeology.** The changelog is written the night of the release by scrolling the commit log and guessing what mattered; consumer-visible changes are missed and internal refactors are presented as features. Catch it by checking `[Unreleased]` during ordinary work: an empty section mid-cycle means entries are not being written as work lands.
- **The eternal 0.x.** A package with real external consumers stays at 0.x for years because 1.0.0 "feels like a commitment" — which it is, and avoiding it does not remove the dependence, only the contract. Catch it at release review: if consumers exist and the API has been stable across several minors, the 1.0.0 question belongs on the record.
- **Version by environment.** Dev, staging, and production quietly run different builds under the same version label, so a bug "fixed in 2.3.0" reproduces in production. Catch it by tying every deployment to its tag (DX-152) and comparing the deployed tag, not the label, when a report comes in.

## Examples

- [Example 1 — The breaking patch](examples/example-1.md) — violates/corrects DX-144, DX-143.
- [Example 2 — Three versions of the version](examples/example-2.md) — violates/corrects DX-142, DX-149.
- [Example 3 — The hotfix that rewrote history](examples/example-3.md) — violates/corrects DX-148, DX-151.

## Recall anchors

- The version is a contract, not a mood: derive the bump from the commits.
- One source of truth — tag, manifest, and changelog are the same string or the release is not done.
- Breaking change means major bump plus a migration note. No exceptions for "small" breaks.
- Published means immutable: fixes ship as a new version, never a moved tag.
- Yanked is marked, never erased.

## Checklist

- [ ] The candidate version is valid SemVer, including any pre-release/build suffixes (DX-141, DX-147, G-DX-074).
- [ ] The bump matches the derivation from the commit range since the last tag (DX-143, G-DX-072).
- [ ] Any breaking change has a major bump and a migration note in the changelog (DX-144, G-DX-073).
- [ ] Anything removed was deprecated at least one minor release earlier (DX-145, G-DX-075).
- [ ] Tag, manifest, and changelog heading are the identical version string (DX-149, G-DX-071).
- [ ] No existing tag moved and no published artifact was replaced (DX-148, G-DX-074).
- [ ] The changelog section is grouped by the six types and written for consumers (DX-150).
- [ ] Any withdrawn release is marked `[YANKED]` with a reason, not deleted (DX-151).
