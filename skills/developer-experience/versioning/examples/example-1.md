# Example 1 — The breaking patch

## Before

The `search()` function drops its `limit` parameter and changes its return shape. The commits and release look like this:

```text
fix: simplify search signature
```

```json
{ "version": "1.4.1" }
```

```markdown
## [1.4.1] - 2026-11-20
### Fixed
- Simplified the search call.
```

It ships as a patch because "it's a small cleanup." Every consumer who upgrades for a bug fix gets a broken integration with no warning — their manifests promised 1.4.x compatibility that the content does not deliver.

## After

The same change, released under the contract:

```text
feat!: return paged result object from search()

BREAKING CHANGE: search() no longer accepts `limit` and returns
{ items, total } instead of an array. Pass page size via `pageSize`
in the options argument.
```

```json
{ "version": "2.0.0" }
```

```markdown
## [2.0.0] - 2026-11-21
### Changed
- **BREAKING:** `search()` returns `{ items, total }` instead of an array and no
  longer accepts `limit`. Migration: replace `search(q, 20)` with
  `search(q, { pageSize: 20 })` and read results from `.items`.
```

The bump is the one the commit range derives (a breaking signal → MAJOR), and the migration note sits in the changelog entry itself.

## Note

Corrected under DX-144 (breaking changes force a major bump and a migration note) and DX-143 (the bump is derived from the commit signals, not chosen by feel).
