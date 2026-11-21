# Example 1 — Git log dump vs curated release section

Demonstrates: PM-126 (curated, never generated) — the Before violates BAN-PM-061.

## Before

```markdown
## [1.4.0] - 2026-11-02

- Merge pull request #812 from fix/typo
- a3f9c1e wip
- revert "revert add export"
- refactor billing module
- fix bug
- bump deps
- Merge branch 'main' into release/1.4.0
```

Raw commit output pasted as the release notes: merge noise, a hash, an internal refactor, and a "fix bug" that tells the user nothing.

## After

```markdown
## [1.4.0] - 2026-11-02

### Added

- Invoices can now be exported as CSV from the billing page, filtered by date range.

### Fixed

- Invoice PDFs no longer render a blank second page for multi-currency accounts.
```

The same release, curated: the revert chain and the export work collapse into the one Added entry the user can act on, the refactor and dependency bump with no user effect are omitted, and "fix bug" becomes the specific behavior that changed.
