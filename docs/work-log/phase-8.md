# Phase 8 — Hybrid expansion (work log)

Date: 2026-11-21. Status: IN PROGRESS. Wave 1 (builders) and integration are complete and verified on disk (file existence, line counts, and example counts checked 2026-11-21; bundle total re-verified at the board stage). The debater stage is complete and recorded below. The board stage is in progress; the committee stage has not run yet and is recorded below as planned structure only — no committee findings exist yet, and none are stated here.

## Commission

- **Commissioned by MUHIUM, 2026-11-21 ~23:48 PKT:** build the full hybrid set, in detail — 8 hybrid missions that combine existing departments into end-to-end capabilities (clone & redesign completely, clone & rebrand, rescue & relaunch, replatform/migration, prototype → production, AI-ify an existing product, localize & launch a new market, single app → SaaS conversion), delivered as new skills + new playbooks on top of the shipped v1.0.0 repository.
- **Staffing as commissioned:** 30 builders + 10 debaters + 5 board + 4 committee (49 agents). Builders work first; debaters review adversarially and get flaws fixed; a 5-agent board sits over the debaters; a 4-agent committee finalises.
- **Mid-flight protocol upgrade (same evening, on MUHIUM's quality order — "quality must be high"):** structured handoffs between agents, coordinator-level verification of builder output before it is accepted, debaters cross-assigned (no debater reviews their own slice's work), and wave gates between stages (a wave does not start until the previous wave's gate passes).

## Wave 1 — builders (30, via 3 coordinators)

Builders ran under three coordinators (A: skills batch 1, B: skills batch 2, C: playbooks). Each new skill was written to the repo's skill format with a registered ID block and 3 worked examples; each coordinator spot-read its deliverables before reporting them up.

### Coordinator A — 4 skills, each with 3 examples

| Skill | Lines | ID block | Gates / BANs |
|---|---|---|---|
| clone-redesign (D16, `skills/cloning-replication/clone-redesign/`) | 78 | CL-141–152 | 5 gates / 5 BANs |
| rebrand-execution (D16, `skills/cloning-replication/rebrand-execution/`) | 89 | CL-701–716 | 5 gates / 7 BANs |
| project-takeover (D15, `skills/developer-experience/project-takeover/`) | 82 | DX-161–172 as originally written — see the collision under Integration | (per coordinator report) |
| seo-migration (D9, `skills/seo-content/seo-migration/`) | 84 | CO-281–292 | 5 gates / 6 BANs |

### Coordinator B — 4 skills, each with 3 examples

| Skill | Lines | ID block | Gates / BANs |
|---|---|---|---|
| prototype-hardening (D15, `skills/developer-experience/prototype-hardening/`) | 92 | DX-161–176 | 6 gates / 8 BANs |
| ai-retrofit (D17, `skills/ai-features/ai-retrofit/`) | 81 | AI-201–212 | 5 gates / 5 BANs |
| market-expansion (D1, `skills/product-requirements/market-expansion/`) | 95 | PR-261–280 | 5 gates / 6 BANs |
| saas-conversion (D2, `skills/architecture/saas-conversion/`) | 88 | AR-261–278 | 6 gates / 6 BANs |

- **Coordinator-layer defect catch (B):** saas-conversion's SKILL.md carried a phantom index entry pointing at a fourth example that does not exist; caught at the coordinator layer and fixed before handoff. The skill ships with exactly 3 examples, verified on disk.

### Coordinator C — 8 playbooks, all spot-read at the coordinator layer

| Playbook | Lines |
|---|---|
| `playbooks/clone-and-redesign.md` | 120 |
| `playbooks/clone-and-rebrand.md` | 158 |
| `playbooks/rescue-and-relaunch.md` | 148 |
| `playbooks/replatform-migration.md` | 140 |
| `playbooks/prototype-to-production.md` | 145 |
| `playbooks/ai-ify-existing-product.md` | 142 |
| `playbooks/localize-new-market.md` | 151 |
| `playbooks/single-app-to-saas.md` | 148 |

### Remaining builders (integration + records, 6 of the 30)

The balance of the 30 builders is the integration and records staff (registry/index/bundles, README/CHANGELOG/VERSION updates, this log + METRICS.md, and the dry run). Their work is recorded under Integration below, as it lands.

## Integration

- **DX ID collision — caught by the executor from the coordinator reports, before integration ran.** project-takeover (Coordinator A) and prototype-hardening (Coordinator B) were written independently and both claimed ID blocks starting at DX-161 (project-takeover DX-161–172; prototype-hardening DX-161–176) — a duplicate-ID defect that repo validation would reject. Resolution assigned to integration agent I1: prototype-hardening keeps its block; project-takeover is renumbered to a free DX block, with its registry row written to match. **State: FIX LANDED and verified in the files (I1, 2026-11-21).** `project-takeover` now carries rules DX-181–DX-192, gates G-DX-091–G-DX-095, and BANs BAN-DX-091–BAN-DX-095 across its SKILL.md and its 3 example files; I1's repo-wide grep confirms the new block appears only in `project-takeover/` and the old DX-161–172 / G-DX-081–085 / BAN-DX-081–085 block only in `prototype-hardening/`. This item is closed.
- **Registry rows for the 8 new skills** — assigned to integration (I1). **State: LANDED (I1, 2026-11-21)** — rows for all 8 new skills are present in `docs/RULE_ID_REGISTRY.md`, each matching the ID ranges the skill actually defines, including project-takeover's renumbered block.
- **Index regeneration** — assigned to integration (`scripts/build-index.py`). **State: LANDED (I2, 2026-11-21)** — `SKILLS_INDEX.md` was regenerated at 235 skills · 18 departments, with all 8 new skills indexed. One follow-on defect from that run — build-index warned "no anatomy element serves it" for all 8 new skills, leaving their Anatomy element fields empty — was fixed in the debater stage (Debater 10): anatomy assignments were added to `docs/PROJECT_ANATOMY.md` and the index regenerated with zero warnings, still 235 skills.
- **Bundle regeneration** — assigned to integration (`scripts/build-bundles.py`). **State: regeneration ran (I2, 2026-11-21) — 35 bundle files written, 0 cap failures — but none of the 8 new playbook bundles was generated:** `build-bundles.py` builds playbook bundles only for slugs registered in its hardcoded `KEY_SKILLS` dict, which still lists only the original 13 playbooks. **State: CLOSED in the debater stage (Debater 9)** — the 8 slugs were registered in `KEY_SKILLS` (with 2 parser micro-fixes) and the bundles regenerated; `bundles/` now holds the final **43 files**, filesystem-verified at the board stage.
- **Validation** — assigned to integration (`scripts/validate-skills.py`) after the registry rows, renumber, and regeneration land. **State: LANDED (I2, 2026-11-21) — "Checked 235 skills. ALL PASS", exit code 0, no failure lines.**
- **Dry run** — a fresh-agent exercise of a new hybrid playbook, run as an integration-stage step. **State: COMPLETED** — the playbook was exercised end-to-end and **12 friction points were recorded, each dispositioned** (fixed, or waived with a recorded reason) before the board stage.
- **Repo totals as now verified in the files:** skills 235 (index header); playbooks 21 (files on disk); examples 706 (files on disk — 682 pre-Phase-8 + 24 new; the v1.0.0 documents' "681" figure was off by one, because the pre-existing `vector-db` skill carries a fourth example file). Bundles: **43 files, final** (after Debater 9's KEY_SKILLS fix and regeneration; filesystem-verified at the board stage).

## Debaters — COMPLETE

10 debaters, cross-assigned under the upgraded protocol (no debater reviewed the slice they or their coordinator built). Each argued against the assigned skills/playbooks — format compliance, ID integrity, overlap with existing skills, factual claims — and every upheld flaw was fixed in place and re-verified; validation re-runs after the fixes still report "Checked 235 skills. ALL PASS". Upheld flaws fixed, per slice:

| Slice | Flaws fixed |
|---|---|
| clone-redesign | 6 |
| rebrand-execution | 5 |
| project-takeover | 6 |
| seo-migration | 6 |
| prototype-hardening | 8 |
| ai-retrofit | 5 |
| market-expansion | 5 |
| saas-conversion | 3 |
| Integration (Debater 9) | `KEY_SKILLS` registration for the 8 hybrid playbooks + 2 parser micro-fixes; playbook bundles regenerated to the final 43 files |
| Anatomy / docs (Debater 10) | Anatomy assignments for all 8 new skills (incl. the new "Market expansion" element — catalog now 128 elements), index regenerated with zero warnings; docs/counts corrections (incl. the 682 → 706 examples reconciliation) |

**P1 highlights (the flaws that would have hurt a real user):**

- **clone-redesign** shipped without a brand-clearance rule and with ungated imagery — a clone could have carried protected brand assets into a "redesign". Both closed with rules/gates.
- **single-app-to-saas** — the playbook itself taught the banned default-tenant sweep (assigning orphaned rows to a default tenant), the exact pattern the saas-conversion skill bans. Playbook corrected to the orphan-report route.
- **prototype-hardening** — a worked example performed a payment charge inside a database transaction (the classic double-charge/locked-funds shape). Example rewritten to the safe ordering.
- **replatform-migration** — wrong-bundle routing: steps pointed at bundles that do not carry the skills they load. Routing table corrected against the regenerated bundles.

## Board — IN PROGRESS

The 5-agent board is sitting over the debaters' record, one member per dimension: (1) format/validation integrity, (2) cross-skill overlap and duplication, (3) playbook↔skill routing correctness, (4) documentation and counts truthfulness, (5) legal/safety guardrails (including the clone missions' protected-expression line). Per-dimension verdicts will be recorded here as each member signs off; the stage gate passes only when all five dimensions are signed.

## Committee — TO BE COMPLETED

_This section is a placeholder for a stage that has not run. No findings exist yet._

Planned structure: a 4-agent final committee confirms the closing state — final validation result, repo totals as regenerated, version bump and changelog, README/USER_GUIDE consistency, and the GitHub push of the Phase 8 state. Its sign-off will be recorded here when the stage completes.

## Decisions recorded this phase

D-020 — "Phase 8 hybrid expansion: scope, staffing, and upgraded quality protocol" — recorded in `docs/DECISIONS.md` during integration (I4, 2026-11-21). It covers the commission and the staffing/protocol terms above (MUHIUM's direct instructions of 2026-11-21 ~23:48–23:55 PKT) and records the DX ID collision with its renumber fix.

## Staffing

As commissioned: 30 builders (Wave 1: 24 content builders under 3 coordinators — 16 skill/example builders + 8 playbook builders — plus 6 integration/records builders), 10 debaters, 5 board, 4 committee. Coordinators are counted within the executor's coordination layer, as in earlier phases' records practice.
