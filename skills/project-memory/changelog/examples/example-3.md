# Example 3 — Breaking change shipped as a patch bump

Demonstrates: PM-127 (the bump matches the content) — gate G-PM-064 catches the Before.

## Before

```markdown
## [1.4.1] - 2026-11-10

### Removed

- The `/v1/reports` API endpoint has been removed; use `/v2/reports` instead.

### Fixed

- Corrected timezone handling in scheduled report emails.
```

The release removes a public API endpoint — a breaking change — but the version only moved from 1.4.0 to 1.4.1. Every consumer pinning `^1.4.0` auto-upgrades into a broken integration. G-PM-064 fails the release: a Removed entry requires a major bump.

## After

```markdown
## [2.0.0] - 2026-11-10

### Removed

- The `/v1/reports` API endpoint has been removed; use `/v2/reports` instead. The endpoint was deprecated in 1.4.0 with a planned removal in the next major release.

### Fixed

- Corrected timezone handling in scheduled report emails.
```

The same content under 2.0.0: the version number itself now warns integrators before they upgrade, and the entry shows the deprecation was announced a release earlier (PM-133).
