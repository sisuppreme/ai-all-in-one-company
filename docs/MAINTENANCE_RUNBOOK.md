# MAINTENANCE_RUNBOOK.md — Keeping this repository current

Operational runbook for maintaining the repo after v1.0 ships (brief §11). Maintenance is done by the user **with any agent** — the quarterly re-verification of the full catalog is not one person's manual job. At handover the user names a maintainer; the name is recorded in the handover note.

A repo that never updates goes stale: tools change, best practices move, and detection parameters lose accuracy as AI output improves. This runbook is the countermeasure.

## Versioning (semantic versioning over the versioned interface)

The versioned interface is: skill folder paths, rule IDs, gate IDs, `SKILLS_INDEX.md` fields, and bundle filenames. The repo version lives in `VERSION` at the repo root.

| Bump | What counts |
|---|---|
| **MAJOR** | A renamed or removed skill; a changed rule or gate ID; a changed index field; a Phase 2 scope addition (new platform scope) |
| **MINOR** | A new skill; a new detection parameter; a new playbook |
| **PATCH** | Wording fixes; claim corrections; example updates |

Rules that never bend:

- Rule and gate IDs are never reused or renumbered (see `docs/RULE_ID_REGISTRY.md`).
- A skill is never silently deleted. It is marked deprecated in `SKILLS_INDEX.md` with a pointer to its replacement, and removed only in a MAJOR release.
- Every release updates the repo-root `CHANGELOG.md` and regenerates the index and all bundles (below).

## Release procedure

Run in order; do not publish a release with any step skipped.

1. **Apply the changes** to the skills, parameters, playbooks, or docs that the release covers.
2. **Validate the skills:** `python3 scripts/validate-skills.py` — must exit 0 (all skills pass the §5.4 format checks). Fix failures in the skills, never in the validator, to make a release pass.
3. **Regenerate the index:** `python3 scripts/build-index.py` — `SKILLS_INDEX.md` is generated from skill metadata, never hand-edited. Commit the regenerated file with the release.
4. **Regenerate all bundles** with the bundle builder in `scripts/` (§5.8 generation rule), and confirm every bundle is within its cap: `bundles/core.md` under 10,000 tokens, every other bundle at or under 30,000 tokens. A bundle whose source skills changed without regeneration is a ship-blocking defect.
5. **Update `CHANGELOG.md`** (repo root, Keep a Changelog format) with the release's Added / Changed / Deprecated / Removed entries, and set `VERSION` to the new version.
6. **Handle deprecations:** any skill deprecated by this release is marked deprecated with a replacement pointer in the index; removals happen only in a MAJOR release and are listed under Removed.
7. **Record the release** in `docs/METRICS.md` (version, date, what changed, counts after the change) and in `docs/work-log/`.

## Quarterly checklist

Cadence from §11: tool/dependency claims re-verified **quarterly**; detection parameters reviewed **every 6 months**; the full skill catalog reviewed **yearly**. The quarterly pass below is the one that runs four times a year; the 6-month and yearly items join it when due.

- [ ] **Re-verify dated facts in skills against their sources.** Every skill fact that carries a date or a "Last verified" stamp gets re-checked, in particular:
  - Free-tier limits and provider caps (D6 `free-tiers` and `hosting` skills — entries go stale 90 days after their check date).
  - Provider specifics annexes (D17 `llm-integration`'s dated provider annex — endpoints, key formats, model behaviour claims).
  - Legal and standards version pins (D13 `accessibility-law` — WCAG versions pinned by EAA/EN 301 549, Section 508, ADA Title II; D14 regime tables and age thresholds).
  - Any tool, API, or platform claim whose source has moved or changed (QB-07: an unverified claim does not stay in the repo).
- [ ] **Re-run the DET false-positive spot checks.** Walk a sample of detection parameters from each family in `skills/detection/` against known-professional sites and a known open-source codebase (the Phase 1 method: record fires, borderline cases, and not-testable parameters honestly). Any parameter that fires on professional work gets narrowed — check, false-positive clause, or scoping — and the fix is recorded in `docs/DECISIONS.md`.
- [ ] **Review the gap-report backlog.** Triage open GitHub issues filed from the templates in `.github/ISSUE_TEMPLATE/` (gap reports from consuming agents, §11 feedback loop): route each to the owning department, fix what this cycle covers, and record dispositions. A gap that recurs is a defect in the repo, not in the agents reporting it.
- [ ] **Check bundle and index drift.** Re-run steps 2–4 of the release procedure on the current tree; any drift between skills and generated files is fixed by regeneration, and the drift itself is noted in `docs/METRICS.md`.
- [ ] **(Every 6 months) Detection review.** Re-check the parameter set against current AI output: parameters that no longer discriminate are revised or retired (IDs retired, never reused), new tells are added as new parameters (a MINOR release), and the §6.2 fake-class table is kept 1:1 with the DET-FAKE family.
- [ ] **(Yearly) Full catalog review.** Every skill read once against its sources and its department research: claims, gates, and examples confirmed or corrected; stale skills deprecated with pointers rather than left to rot.

## Automated checks

The checks that exist in `scripts/` today. Run them from the repo root.

| Command | What it does | When |
|---|---|---|
| `python3 scripts/validate-skills.py` | Validates every skill against the §5.4 format: sections present and in order, ≤400 lines, rule/gate/BAN IDs inside the skill's registry block and unique repo-wide, ≥3 gates, every BAN entry citing a DET parameter (or DET-NONE) and a replacement, ≥3 example files with Before/After, ≤5 recall anchors. Exit 0 = all pass. Accepts department folders as arguments to check a subset. | Every release; every quarterly pass; after any skill edit |
| `python3 scripts/build-index.py` | Regenerates `SKILLS_INDEX.md` from the skills' own metadata and `docs/PROJECT_ANATOMY.md`. Run it, then check the diff: an unexpected diff means a skill's metadata changed without the index being regenerated. | Every release; every quarterly pass |

Bundle regeneration and bundle-cap measurement run through the bundle builder in `scripts/` as part of the release procedure (step 4 above), per the §5.8 generation rule.
