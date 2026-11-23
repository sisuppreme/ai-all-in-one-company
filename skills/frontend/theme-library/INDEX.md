# OmniForge Theme Library — Index

The library holds **100 themes**, each specified exactly once, in full, in [`expanded/`](expanded/).

## Canonical source rule

- The canonical full specification for theme *N* is **`expanded/theme-NNN.md`** (zero-padded: theme 7 → `expanded/theme-007.md`). Build from that file.
- The four range files are **indexes only** — they list their themes and point to the canonical expanded files. They contain no specifications.
  - [themes-001-025.md](themes-001-025.md) — Themes 1–25
  - [themes-026-050.md](themes-026-050.md) — Themes 26–50
  - [themes-051-075.md](themes-051-075.md) — Themes 51–75
  - [themes-076-100.md](themes-076-100.md) — Themes 76–100
- [EXPANSION-STANDARD.md](EXPANSION-STANDARD.md) is the depth standard every expanded spec was written and verified against (per-element build specs, choreography timelines, state matrices, breakpoint behaviour, edge cases, accessibility, tokens, worked examples, scroll choreography map, performance budget, build order).

## History

Each theme began as a short entry (~950–1,400 words) inside the range files. Once a theme's 50x expansion in `expanded/` was verified, its short entry was removed, per the standing rule that the final library holds only the deep versions.
