# Example 2 — Phantom heading and version-source mismatch

Demonstrates: PM-129 (no heading without a release) and PM-130 (declared version source of truth) — the Before violates BAN-PM-064.

## Before

```markdown
## [Unreleased]

## [2.0.0] - 2026-10-15

### Added

- Redesigned dashboard with customizable widgets.

## [1.4.0] - 2026-09-20
```

The project has no `v2.0.0` tag and no published 2.0.0 artifact — the dashboard redesign is still in progress on a branch. The 2.0.0 heading claims a release that never happened, and gate G-PM-063 fails: the declared source of truth (latest git tag, `v1.4.0`) does not equal the top version heading.

## After

```markdown
## [Unreleased]

### Added

- Redesigned dashboard with customizable widgets (in progress, not yet released).

## [1.4.0] - 2026-09-20
```

Unshipped work lives under Unreleased, honestly marked as in progress. The 2.0.0 section is created only on the day 2.0.0 is actually tagged and published, and G-PM-063 then passes because the top heading equals the new tag.
