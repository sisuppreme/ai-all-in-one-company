# Example 3 — The hotfix that rewrote history

## Before

A crash is found in 2.3.1 an hour after release. The fix is committed and the existing tag is quietly moved:

```bash
git tag -f v2.3.1
git push origin v2.3.1 --force
# package registry artifact for 2.3.1 replaced with the rebuilt one
```

Two users now run different code that both call themselves 2.3.1. When the "fixed" build still fails for one of them, there is no way to tell which 2.3.1 they have, and the crash reports for the original build point at code that no longer exists under that name.

## After

The published version is left exactly as it shipped, and the fix gets its own number:

```bash
git tag v2.3.2
git push origin v2.3.2
```

```markdown
## [2.3.2] - 2026-11-21
### Fixed
- Crash on startup when the config file is empty (present in 2.3.1).

## [2.3.1] - 2026-11-21 [YANKED]
### Fixed
- Initial fix for config loading. Yanked the same day: crashes on an empty
  config file; superseded by 2.3.2.
```

Anyone pinned to 2.3.1 can see what it was, why it was withdrawn, and where to go — and every report can be tied to exactly one build.

## Note

Corrected under DX-148 (a released version is immutable; fixes ship as a new version, never a moved tag) and DX-151 (yanked releases are marked `[YANKED]` with a reason, never erased).
