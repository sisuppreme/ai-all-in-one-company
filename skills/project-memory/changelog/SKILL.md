# changelog

## Metadata

- **Owner department:** D10 Project & Memory (PM)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Keep a Changelog 1.1.0 — https://keepachangelog.com/en/1.1.0/ ; Semantic Versioning 2.0.0 — https://semver.org/spec/v2.0.0.html
- **Depends on:** none — standalone: entries are written from the project's own commit history and release diff, read directly from the repo; no other skill's output is an input. It feeds readme-writing and handover.
- **Feeds into:** readme-writing (README links the changelog), handover

## When to use / Do NOT use

- **Use when:** a project ships anything a user can notice — a release, a deprecation, a fix — and its CHANGELOG.md must be created, updated, or cut for release.
- **Do NOT use when:** recording internal work with no user effect (that belongs in the work log or commit history), or announcing a release socially (release notes and posts are written from the changelog, not instead of it). Do not keep a second change history in GitHub Releases that can drift from CHANGELOG.md (PM-124).

## Rules

1. **PM-121 — One file, newest first.** Exactly one CHANGELOG.md at the project root. `## [Unreleased]` sits on top; released sections follow in strictly descending version order. No per-year, per-component, or per-team changelog files.
2. **PM-122 — Entries land with the change.** Every user-visible change adds its entry to Unreleased in the same change (same PR/commit) as the behavior it describes. A release is never assembled by reconstructing entries from memory at release time.
3. **PM-123 — Six categories only.** Category headings are exactly: Added, Changed, Deprecated, Removed, Fixed, Security. No invented categories ("Misc", "Improvements", "Updates"), and an empty category is omitted, not left as a bare heading.
4. **PM-124 — One canonical history.** CHANGELOG.md is the single source of truth for change history. Release-page or store notes are generated or copied from it at release time, never maintained as a separate, editable copy.
5. **PM-125 — Written for users.** Each entry describes the effect on the user in one plain sentence: what they can now do, what behaves differently, what they must act on. Implementation details, internal codenames, and ticket IDs never appear.
6. **PM-126 — Curated, never generated.** Entries are selected and written by a human judgment pass. Merge commits and internal refactors with no user effect are omitted; one user-visible change is one entry, however many commits it took.
7. **PM-127 — The bump matches the content.** SemVer: breaking change → major, new feature → minor, fix only → patch. A release containing Removed entries or breaking Changed entries cannot ship as minor or patch; a release with Added entries is at least minor.
8. **PM-128 — Exact heading and date format.** Release headings are `## [X.Y.Z] - YYYY-MM-DD` with a real SemVer version and the actual release date in ISO 8601. Version labels are written the same way everywhere: no mixing of `v1.2`, `1.2`, and `Version 1.2.0`.
9. **PM-129 — No heading without a release.** A version section is created only when that version actually ships — a tag or published artifact exists for it. Planned versions live in Unreleased or the roadmap, never as empty or speculative version headings.
10. **PM-130 — The version source of truth is declared, never assumed.** The project states its version source — git tag, `package.json`, a `VERSION` file, or another stack-specific file — in the changelog header or project config. Gates read the version from that declared source only; no gate hardcodes a source.
11. **PM-131 — Every entry traces to a real change.** Each entry corresponds to a change actually merged in the release it sits under. An entry for work that was planned, reverted, or shipped in a different release is removed or moved, never left in place.
12. **PM-132 — Published sections are frozen.** After a version ships, its section is not silently edited. A factual error is corrected with a dated erratum note appended to that section, so the record shows both what was claimed and what was corrected.
13. **PM-133 — Deprecation precedes removal.** A feature appears under Deprecated at least one release before it appears under Removed, and the deprecation entry names the release in which removal is planned when that is known.

## BAN list

- **BAN-PM-061 — The dumped git log.** Banned: pasting raw commit output, merge commits, or commit hashes into CHANGELOG.md as entries. Defeats: DET-CON-004. Bad: "## [1.4.0] - 2026-11-02 — Merge pull request #812 from fix/typo; a3f9c1e wip; revert 'revert add export'". Instead: curate the release into user-effect entries under the six categories (PM-125, PM-126) — the export fix becomes one Fixed entry, the merge and revert noise is omitted. Severity: BLOCK.
- **BAN-PM-062 — Entries for changes that never shipped.** Banned: changelog entries describing features, fixes, or behavior that are not in the release — planned, reverted, or imagined. Defeats: DET-CON-014. Bad: the 1.4.0 section announces "Added: CSV export" but the export PR was reverted before release and no export exists in 1.4.0. Instead: the entry is deleted before release; if the feature ships later, its entry lands with that release (PM-131). Severity: BLOCK.
- **BAN-PM-063 — The content-free entry.** Banned: entries that carry no information about what changed — "bug fixes and improvements", "various enhancements", "performance improvements" with no behavior named. Defeats: DET-CON-006. Bad: "Fixed: Bug fixes and performance improvements." Instead: name the user-visible effect: "Fixed: invoice PDFs no longer render a blank second page for multi-currency accounts." Severity: WARN.
- **BAN-PM-064 — The phantom version heading.** Banned: a `## [X.Y.Z]` section for a version that was never tagged or published. Defeats: DET-CON-015. Bad: CHANGELOG.md carries a polished `## [2.0.0] - 2026-10-15` section, but the project's latest tag is v1.4.0 and no 2.0.0 artifact exists anywhere. Instead: unreleased work stays under `## [Unreleased]` until the version actually ships (PM-129). Severity: BLOCK.
- **BAN-PM-065 — Mixed version labels.** Banned: referring to versions inconsistently across the changelog and release surfaces — `v1.2`, `1.2`, `Version 1.2.0`, `Release 12` for the same versioning scheme. Defeats: DET-CON-017. Bad: the changelog heads a section `## [1.2] - 2026-09-01` while the tag is `v1.2.0` and the README announces "Version 1.2". Instead: one label form everywhere — the SemVer number in brackets in the changelog, matching the declared source of truth (PM-128, PM-130). Severity: WARN.

## Gates

- **G-PM-061 — Heading and category parser.** Verifies: PM-121, PM-123, PM-128. Check: automated — a script asserts every `## ` heading in CHANGELOG.md matches `^## \[Unreleased\]$` or `^## \[(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)\] - \d{4}-\d{2}-\d{2}$`, the captured date parses as a real calendar date, and every `### ` heading is one of Added, Changed, Deprecated, Removed, Fixed, Security. Pass: zero non-matching headings. Fail: block the release; fix the heading or category. Recorded in: progress.md.
- **G-PM-062 — Order and date sequence.** Verifies: PM-121, PM-127. Check: automated — the parser from G-PM-061 additionally asserts version headings are in strictly descending SemVer order and their dates are non-increasing down the file. Pass: no inversions. Fail: block; reorder the sections — never edit a date to make the order pass. Recorded in: progress.md.
- **G-PM-063 — Version source-of-truth match.** Verifies: PM-129, PM-130. Check: automated — read the project's declared version source (per PM-130: e.g. `git describe --tags --abbrev=0` stripped of a leading `v`, or the `version` field of `package.json`, or the contents of `VERSION`) and compare it with the topmost version heading in CHANGELOG.md. Pass: the two are exactly equal. Fail: block the release; either the release was not tagged or the heading is wrong — fix whichever is false. Recorded in: progress.md.
- **G-PM-064 — Bump consistency.** Verifies: PM-127. Check: automated — diff the newest section's categories against the previous version: if Removed is present or any Changed entry is marked breaking, the major number must have increased; if Added is present, at least the minor number must have increased; a patch bump may contain only Fixed and Security entries. Pass: the actual bump is at least the required level. Fail: block; renumber the release before anything ships under the wrong version. Recorded in: progress.md.
- **G-PM-065 — Entry-to-change cross-check.** Verifies: PM-122, PM-131. Check: manual, sampled — pick three entries from the newest release and trace each to a merged change (PR or commit) inside that release's range; separately, if the diff since the previous tag contains user-visible changes, Unreleased must not have been empty at release time. Pass: 3 of 3 entries trace to real changes. Fail: block; remove or move every untraceable entry and re-run. Recorded in: progress.md.

## Anti-patterns

- **The release-day reconstruction.** Unreleased stays empty for weeks, then one person writes the whole section the night before release from memory and merged-PR titles. Catch it: check whether entries arrived in the same commits as their changes (PM-122); a single giant changelog commit at release time is the tell.
- **The marketing changelog.** Entries written as launch copy — "our most powerful release ever", superlatives, exclamation marks — instead of statements of what changed. Catch it: read an entry aloud and ask what the user can now do; if the answer is an adjective, rewrite it (PM-125).
- **The security-fix whisper.** A fix for an exploitable vulnerability is buried as an ordinary Fixed entry, so users cannot tell they must upgrade urgently. Catch it: any fix that closes a vulnerability, leak, or permission hole belongs under Security (PM-123), worded to convey urgency without disclosing exploit detail.
- **The orphaned changelog.** CHANGELOG.md exists but nothing links to it — not the README, not the release page — so it silently rots while users read stale release notes elsewhere. Catch it: the README links the changelog (readme-writing), and G-PM-063 failing after a release means the file was left behind.

## Examples

- [Example 1 — Git log dump vs curated release section](examples/example-1.md) — corrects PM-126 / BAN-PM-061.
- [Example 2 — Phantom heading and version-source mismatch](examples/example-2.md) — corrects PM-129, PM-130 / BAN-PM-064.
- [Example 3 — Breaking change shipped as a patch bump](examples/example-3.md) — corrects PM-127 / G-PM-064.

## Recall anchors

- Entries land with the change, not at release time.
- Written for users: effect, not implementation.
- Six categories, no inventions.
- No heading without a real release behind it.
- The bump must match the content — breaking means major.

## Checklist

- [ ] Every user-visible change in this release has an entry, added in the same change as the behavior (PM-122).
- [ ] All entries sit under the six categories only, one user effect per entry (PM-123, PM-125).
- [ ] No entry describes anything that is not actually in the release (PM-131, BAN-PM-062).
- [ ] Heading format, descending order, and ISO dates verified by G-PM-061 and G-PM-062.
- [ ] Top version heading equals the declared version source of truth (PM-130, G-PM-063).
- [ ] The version bump is consistent with the categories present (PM-127, G-PM-064).
- [ ] Deprecations were announced at least one release before any removal in this release (PM-133).
- [ ] Gates G-PM-061 to G-PM-065 pass; results recorded in progress.md.
