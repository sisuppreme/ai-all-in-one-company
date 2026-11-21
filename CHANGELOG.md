# Changelog

All notable changes to this repository are recorded in this file. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] — 2026-11-21

### Added

- Phase 8 hybrid expansion: 8 new skills for cross-department "hybrid" missions, bringing the total from 227 to 235 — `clone-redesign` and `rebrand-execution` (D16), `project-takeover` and `prototype-hardening` (D15), `seo-migration` (D9), `ai-retrofit` (D17), `market-expansion` (D1), and `saas-conversion` (D2), each in the mandatory memory-proof format with 3 worked examples (24 new example files; 682 → 706 total — the pre-Phase-8 count was 682, not 681 as v1.0.0 documents stated, because the pre-existing `vector-db` skill carries a fourth example file).
- 8 new hybrid playbooks under `playbooks/`, bringing the total from 13 to 21 — one per hybrid mission (clone & redesign, clone & rebrand, rescue & relaunch, replatform/migration, prototype → production, AI-ify an existing product, localize for a new market, single-app → SaaS), each routing to its anchor skill plus the existing department skills the mission combines.
- Release scope includes regeneration of `SKILLS_INDEX.md` and of the bundles under `bundles/` for the new skills and playbooks (34 → 43 bundle files), performed as a separate integration step of this release.

### Fixed

- One rule-ID collision between the two new D15 skills (`project-takeover` and `prototype-hardening`), found during integration and fixed by renumbering `project-takeover` into its own free ID block.

### Process

- Phase 8 was executed under the owner's specified staffing and upgraded quality protocol (D-020): 30 builders, 10 cross-assigned debaters, a 5-member review board, and a 4-member final committee, with structured handoffs and a coordinator verification layer between tiers.

## [1.0.0] — 2026-11-21

### Added

- 18 departments (D1–D18) covering the full web-application lifecycle, from product requirements through architecture, build, security, QA, deployment, and customer experience.
- 227 skills in the mandatory memory-proof format — each with numbered rules, a BAN list, gates, anti-patterns, examples, recall anchors, and a checklist.
- 203 detection parameters across 7 families (visual, code, infra, content, UX, fake, crawl) under `skills/detection/`, each with signal, AI-typical vs. professional form, check, false positives, severity, source, and fix.
- Generated bundles under `bundles/`: `core.md` (under 10,000 tokens), one bundle per department, one per playbook, and `ALL_SKILLS.md` as a reference-only single file that must never be loaded whole.
- 13 project playbooks under `playbooks/`, one per common web-app type, each stating goal, department order, skills to load, gates by ID, failure handling, definition of done, and a worked mini-example.
- Gate registry under `gates/`: the 69 inherited acceptance gates, the G-QA-01…10 skill-release QA protocol, and `DEFECT_TAXONOMY.md`.
- Ready-to-paste custom instructions under `custom-instructions/` for Muse, Claude, Google AI Studio, and generic agents.
- `BOOTSTRAP.md` repo-first protocol (including the 19-rank skill precedence order) and the script-generated `SKILLS_INDEX.md` catalog of every skill.
