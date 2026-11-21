# Phase 4 — Cross-Review & Checkpoint B (2026-11-21)

Phase 4 cross-reviewed all 227 Phase 3 skills for substance (format validation had already passed 227/227 and was not re-run). Six independent reviewer agents, one per department cluster, each deep-read a sample of skills against the Phase 2 research files (rules verifiable, BAN replacements genuine, gates exact and automatable, examples demonstrating the named rule, metadata references resolving to the catalog) and skimmed the rest of their cluster. Reviewers edited nothing; six separate fix agents applied the findings.

## Mechanical checks (executor, before review)

- DET citation existence: 203 real DET IDs in `skills/detection/*/PARAMETERS.md`; skills cite 185 distinct DET IDs; **0 citations to non-existent DET IDs**.
- Depends on / Feeds into resolution (checked independently by reviewers A, B, D, E, F): every named skill resolves to the 227-name catalog, with one exception found and fixed (changelog's "release notes", an artifact, not a skill — removed from Feeds into).

## Review results

| Cluster | Departments | Deep-read | Blockers | Majors | Minors | Verdict |
|---|---|---|---|---|---|---|
| A | D1, D2, D3 | 15 | 0 | 1 | 9 | sound-with-fixes (all three) |
| B | D4, D5, D6 | 19 | 0 | 1 | 3 | D4 sound, D5 sound, D6 sound-with-fixes |
| C | D7, D8, D9 | 15 | 0 | 1 | 4 | D7 sound-with-fixes, D8 sound, D9 sound |
| D | D10, D11, D12 | 12 | 0 | 0 | 4 | D10/D11 sound-with-fixes, D12 sound |
| E | D13, D14, D15 | 18 | 0 | 1 | 4 | D13/D14 sound-with-fixes, D15 sound |
| F | D16, D17, D18 | 15 | 0 | 2 | 7 | sound-with-fixes (all three) |
| **Total** | **18** | **94** | **0** | **6** | **31** | **no department needs a redraft** |

Full reports: `docs/internal/review/phase4-A.md` … `phase4-F.md`.

## The six majors (all fixed)

1. **A/M-1 — fact-sheet:** the price-mirror gate G-PR-063 assumed a billing provider exists. Added the no-billing-provider fallback (diff against the fact sheet's own price entries, per pricing-monetization PR-210).
2. **B/M-1 — incident-response (D6):** the skill required multi-human incident roles (rotation, separate IC and scribe) that the repo's single operator can never satisfy — G-DO-141 was unpassable in the exact context the repo is built for. Added the explicit single-operator mode mirroring reliability DO-266 / deployment-strategies DO-045 (escalation = project owner; IC and fixer in sequence; contemporaneous incident-record timeline replaces the scribe). The gate is adapted, never silently deleted.
3. **C/M-1 — penetration-testing:** three BAN entries cited DET parameters they do not defeat. Re-pointed or marked DET-NONE (see convention below).
4. **E/M-1 — D13 BAN citations:** a substantial minority of accessibility BAN entries cited DET parameters naming a different failure than the banned pattern. Full remapping pass; identical patterns in different skills now carry identical treatment.
5. **F-1 — page-reconstruction:** Metadata "Feeds into" direction contradicted behavior-cloning (the flow runs behavior-cloning → page-reconstruction). Removed the reversed edge.
6. **F-2 — activation-metrics:** gate G-CX-043's pass criterion ("retains measurably better") was not decidable. The activation definition must now record a minimum retention delta and horizon in advance; the gate passes only against that pre-recorded threshold.

## Convention established: DET-NONE

The dominant cross-cluster theme was BAN "Defeats:" citations that were nearest-match rather than semantically exact (clusters B, C, E; ~23 entries). Remedy applied uniformly: re-point where a semantically matching DET parameter exists; otherwise the entry now reads **"Defeats: DET-NONE — no DET parameter names this signal; governed by \<rule IDs\>"**. DET-NONE is an explicit, greppable null marker — no fake traceability. The rule is recorded in `templates/SKILL_TEMPLATE.md` so future skills inherit it. Cluster B's alternative (extending the DET families with new parameters for free-tier misstatement and seed-data leakage) is noted as a possible future detection amendment; it was not done in Phase 4 because the DET set was calibrated and false-positive-tested in Phase 1 and new parameters would need the same FP testing.

## Other fixes of note

- Template now defines Depends on / Feeds into semantics (consumes inputs from / outputs consumed by; cycles permitted between co-evolving skills, no execution-order meaning) — cluster A m-7.
- Duplicate gates across D2 skills given canonical owners (multitenancy-saas for tenant-key, adr-writing for manifest-to-ADR); the duplicates became citations — cluster A m-5.
- vector-db gained example-4.md: a placeholder-free synthetic fixture procedure for the recall-vs-exact gate — cluster B m-2.
- dev-environment example-2's realistic-looking credential string replaced with an obviously fake token — cluster E m-3.
- owasp SE-003 category tag corrected to A05:2025; dependency-safety BAN-SE-055 raised WARN → BLOCK — cluster C m-1/m-2.

## Verification after fixes

- Per-cluster validation after each fix pass: PASS (all six).
- Full-repo run by the executor: `python3 scripts/validate-skills.py` → **"Checked 227 skills. ALL PASS"**.
- DET-NONE occurrences in skills: 23.

## Checkpoint B

Report-only per DECISIONS D-009 (auto agent mode). Result: **0 blockers, 6 majors fixed, 31 minors fixed or dispositioned, no redrafts.** Phase 4 complete; Phase 5 (Forge) begins.
