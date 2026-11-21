# Example 2 — Three versions of the version

## Before

Release day, three places are edited by hand — and one is missed:

```json
// package.json
{ "version": "3.0.0" }
```

```ts
// src/config.ts
export const APP_VERSION = '2.9.4'; // powers the in-app banner and support dialog
```

```markdown
<!-- CHANGELOG.md -->
## [3.0.0] - 2026-11-21
```

The app reports itself as 2.9.4, the registry serves 3.0.0, and a bug report saying "I'm on 2.9.4" cannot be tied to any release. Each copy was correct the day it was typed; nothing keeps them correct.

## After

The manifest is the single source of truth; everything else reads from it:

```json
// package.json — the one hand-maintained copy
{ "version": "3.0.0" }
```

```ts
// src/config.ts — generated at build time from package.json, never edited
import pkg from '../package.json';
export const APP_VERSION = pkg.version;
```

The release commit sets the manifest, creates tag `v3.0.0`, and moves the `[Unreleased]` changelog entries into a `## [3.0.0]` section — one commit, three identical strings, verified by the triple-equality gate before the release is called done.

## Note

Corrected under DX-142 (one source of truth for the version; other displays are read or generated from it) and DX-149 (tag, manifest, and changelog heading form one consistent release triple).
