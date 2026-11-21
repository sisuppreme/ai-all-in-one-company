# Example 3 — Fake badges and a copied manual

## Before

```markdown
# Ledgerline

![build](https://img.shields.io/badge/build-passing-brightgreen)
![coverage](https://img.shields.io/badge/coverage-98%25-brightgreen)
![version](https://img.shields.io/badge/version-2.0-blue)

## User guide

### Creating an invoice

Click **New Invoice**, pick a client from the dropdown, add line items...
(14 more sections of user-guide prose copied from the manual)
```

Both shields are hand-written images: the repo has no CI and no coverage run, and the tagged version is 1.2, not 2.0. Below them, the README duplicates the user guide, so the two copies will drift apart.

## After

```markdown
# Ledgerline

![build](https://github.com/example/ledgerline/actions/workflows/ci.yml/badge.svg)
![version](https://img.shields.io/github/package-json/v/example/ledgerline)

## Documentation

- [User guide](docs/user-guide.md) — creating invoices, payments, reports
- [Architecture](docs/ARCHITECTURE.md)
- [Changelog](CHANGELOG.md)
```

The build badge is served by the actual CI workflow; the version badge reads the package version, the source of truth; the coverage badge is gone until a coverage run exists to report. The guide lives in one file and the README links to it.

Demonstrates PM-044 (badges report real systems only) and PM-045 (link, never duplicate).
