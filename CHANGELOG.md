# Changelog

All notable changes to this repository are recorded in this file. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
