# METRICS.md — OmniForge build metrics

Purpose: every quantitative claim about this build, as a VALUE / DEFINITION / METHOD triple (§6.1). Audience: the user and future maintainers. No number appears in any build document without an entry here.

---

## Budget

| Metric | Value | Definition | Method |
|---|---|---|---|
| Brief token budget | 2,500M tokens | Total build budget set by MASTER_BRIEF.md v5.1 §8; phase shares are caps (§8.1) | Brief §8.1 table; shares: P0 8% / P1 12% / P2 27% / P3 22% / P4 8% / P5 7% / P6 10% / P7 3% / contingency 3% |
| Executor token accounting | Per-phase estimates recorded at each phase end | This runtime does not expose a billable-token usage view to the executor, so exact §8.1 ledger accounting is not measurable here; the honest substitute is a per-phase record of agents spawned, deliverables produced, and approximate session usage where visible | Recorded in this file at each phase end; the limitation itself is recorded here rather than hidden (QB-07: no invented numbers) |
| Phase 6 hosting spend cap | $0 until the user sets a cap | Real-money hosting/domain spend for proof projects, separate from tokens (§8) | DECISIONS.md D-005; free tiers first |

## Runtime (measured, §3.8 rule 1)

| Metric | Value | Definition | Method |
|---|---|---|---|
| Sub-agent capability | Spawning supported; max delegation depth 2 | The executor runtime can spawn parallel sub-agents; a sub-agent's own sub-agents are the deepest level | Runtime configuration, 2026-11-21 |
| Concurrency probe | Batch of 8 parallel research agents at Phase 0 start: **8/8 completed successfully, no throttling or failures observed** → measured concurrency ≥8 on this runtime | §3.8 rule 1 probe, executed as real work: the Phase 0 anatomy research batch doubled as the probe — no tokens spent on empty probe agents | Spawned and completed 2026-11-21 (all 8 slice files written and verified on disk) |
| Company headcount vs runtime | 477 named roles (brief §3.8) are executed as role-passes by the executor + sub-agents, not as 477 simultaneous processes | The brief's headcount is a work-partitioning architecture (every role has a named deliverable and a reviewer, §3.10); the runtime executes those partitions in parallel batches and sequential passes | This note; per-phase agent counts recorded in the work log |

## Inheritance verification (preliminary — final counts land in Phase 2)

| Metric | Value | Definition | Method |
|---|---|---|---|
| WCPM SKILL.md length | 4,015 lines | Lines in web-craft-pro-max/SKILL.md as received | `wc -l`, 2026-11-21 |
| WCPM RESEARCH_PAPER.md length | 711 lines, 9 numbered sections | Lines + `## N.` section count as received | `wc -l` + heading grep, 2026-11-21 |
| WCPM BAN/gate/rule-ID exact counts | Script-measured 2026-11-21 + register read in D3 integration: **200 unique BAN-NN IDs (01–200) ✓; 198 unique R-<section>-<n> IDs ✓; gates: the §12.3 acceptance register holds exactly 69 ✓ brief claim — the 79 total gate IDs add G-QA-01…10 (§12.5 skill-release QA gates); the source file's own §12 text says "68", a stale internal error recorded in the mapping** | Python regex extraction over the full file text + full read of the §12.3 register region with a script count of the register; reconciliation in docs/WCPM_MAPPING.md |

## Phase 4 cross-review (2026-11-21)

| Metric | Value | Definition | Method |
|---|---|---|---|
| Skills deep-read | 94 of 227 | Full SKILL.md read against the department research file, plus ≥1 example file opened and checked against its named rule | Six reviewer agents, one per cluster (A: D1–D3, B: D4–D6, C: D7–D9, D: D10–D12, E: D13–D15, F: D16–D18); reports in docs/internal/review/phase4-*.md |
| Findings | 0 blockers, 6 majors, 31 minors | BLOCKER = teaches a wrong practice or is unusable as written; MAJOR = a gate/rule/metadata defect that misleads execution; MINOR = clause-level imprecision | Reviewer grading in the six reports; all 6 majors and all actionable minors fixed by six fix agents, one per cluster |
| Post-fix validation | 227/227 ALL PASS | scripts/validate-skills.py over the full repo after all fix passes | Executor run, 2026-11-21 |
| DET-NONE markers | 23 | BAN entries whose Defeats field honestly records that no DET parameter names the banned pattern's signal (Phase 4 convention, defined in templates/SKILL_TEMPLATE.md) | grep over skills/*/SKILL.md |
| Phase 4 build agents | 12 | 6 substance reviewers + 6 fix agents, spawned by the executor | Spawn records, 2026-11-21 |

## Phase 5 — Forge

- Token measure (repo-wide definition): **tokens = ceil(characters ÷ 4)**, the brief's own equivalence (~120 KB of Markdown ≈ 30,000 tokens). All bundle sizes below use it.
- Bundles: 33 files. core.md 9,554 (cap <10,000). Largest capped bundle: devops-deployment.md 29,975 (cap 30,000). ALL_SKILLS.md 584,918 (uncapped by design). Cap failures after fixes: 0.
- SKILLS_INDEX.md: 227 entries; 227/227 paths resolve; 227/227 entries carry gates + anatomy element; 19 standalone justifications added (F-01 fix).
- Findability dry-run (Forge, index-only): 9/10 correct first choices across 10 departments — at the §5.3 bar. Formal fresh-agent test runs in Phase 6.
- Verification: 9 checks, 7 PASS first run → 9/9 after fixes. Defects: P0 0, P1 1 (F-01), P2 3 (F-02, F-03, F-04) — all fixed and re-verified.
- Build agents used in Phase 5: 17 (F1 6, F2 6, bundle fixes 3, verification 1, defect fix 1).

## Phase 6 — QA / proof test

- Token measure: same repo-wide definition as Phase 5 — **tokens = ceil(characters ÷ 4)**. Exact billable-token accounting remains not measurable in this runtime (see Budget, "Executor token accounting"); the Phase 6 record is agents spawned + measured outcomes below, per-phase estimates only.
- Findability test (formal, §5.3): **10/10 correct first choices (bar 9/10)**, 7 departments spanned; fresh agent, BOOTSTRAP + SKILLS_INDEX only, choices committed before opening any SKILL.md. Index defects found and fixed: 3.
- Proof gates (checks passed / total recorded by each proof): P1 TaskBoard 43/52 (4 waived tool-form with substitute evidence, 4 blocked provisioning/Stripe-live class, 1 partial); P2 Atlas Blog 19/19; P3 Ledger API 42/48; P4 ShopClone 49/56 (3 waived with DECISIONS entries). Proof tests: P1 29/29 automated tests green. Slop hits 0 and fake-content hits 0 in every proof that records them (P2 explicitly; no proof reported a hit). P1 compliance: ai-studio.md load order verified against the proof's PROOF_REPORT.md.
- Proof defects: project-side P1 0/1/5 (P0/P1/P2), P4 0/3/7 + AF-1 (P2, counts as its 1 minor); P3's built service: zero open defects in all classes. Repo defects: P1 DEF-001…006 (6), P2 DEF-01…05 (5), P3 2 P1 + 3 P2, P4 P4-D1…D9 (9) — all fixed or verified closed; no gate's pass criterion weakened.
- Dry runs: 8 playbooks, gates passed/total — dashboard 36/36, LMS 28/33, booking 23/30, landing 25/30, portfolio 37/38, CRUD tool 37/38, marketplace 36/43, chat 25/35. All 13 playbooks covered (floor ≥11). Friction: 66 points pre-dedup (14 P1, 52 P2) → 28 clusters (22 open, 6 already-fixed) + 6 not-a-defect; worst severity P1, P0 0. All 22 open clusters (DR-01…DR-22) fixed.
- Screenshot false-positive pass (DET-VIS): of the 39 parameters untested after Phase 1 — FP 4 parameters (DET-VIS-001, 015, 022, 041; 6 site-level hits), NO-FIRE 35, UNTESTED 0. All 4 narrowed per the Phase 1 protocol; re-walk 6/6 clear.
- Final verification (executor, 2026-11-21 ~21:50 PKT): index + bundles regenerated — 34 bundles, 0 cap failures; `scripts/validate-skills.py`: "Checked 227 skills. ALL PASS".
- Build agents used in Phase 6: 28 (findability 1 + its fix 1, proofs 4, proof fixes 5, dry runs 8, triage 1, dry-run fixes 5, screenshot FP 1, FP fix 1, records 1).

## Phase 7 — Finalise

- Token measure: same repo-wide definition as Phase 5 — **tokens = ceil(characters ÷ 4)**. Exact billable-token accounting remains not measurable in this runtime (see Budget, "Executor token accounting").
- Deliverables (line counts by `wc -l`, 2026-11-21): README.md 98 (full rewrite; licence note per D-004 — licence applied at GitHub finalization, none invented in-repo); USER_GUIDE.md 134 (English + Roman Urdu quick-start); docs/RESEARCH_PAPER.md 160; docs/WORKFLOW.md 132; QA_REPORT.md 463 — including 8 open items (OI-1…OI-8) recorded unsoftened: four provisioning-blocked deployments, P4 AF-1 (open accessibility defect), the G-SE-001 waiver's outstanding user agreement, P1's blocked/partial provisioning-class gates, and the DET-VIS-020/032 scoped aspects; docs/BAR_TRACEABILITY.md — Phase 6/7 evidence completed for all 14 quality bars (QB-02 partial and QB-11 with an open defect, both recorded as such).
- Ship state: repository complete and ship-ready locally. Pending owner actions, not defects: final ship approval (§9.1 criterion 16) and the GitHub push (empty private repo `ai-all-in-one-company` + app selection, D-011).
- **Closing project totals.** Skills: 227, in 18/18 departments. Detection parameters: 203 (7 families, every family above its brief floor). Playbooks: 13. Bundles: 33 + ALL_SKILLS.md (34 files; final regeneration 0 cap failures). Gates: 69 (acceptance register) + 10 (QA protocol) = 79. Final validation: `scripts/validate-skills.py` — "Checked 227 skills. ALL PASS".
- Build agents used in Phase 7: 4 (3 documentation agents + 1 records agent).
- **Total build agents: 61** — the sum of the per-phase totals recorded in this file (Phase 4: 12 + Phase 5: 17 + Phase 6: 28 + Phase 7: 4). Phases 0–3 predate per-phase totals in this file; their staffing is enumerated in work-log/phase-0.md … phase-3.md without a single recorded total, so no figure for them is stated or folded into the sum (QB-07: no invented numbers).

## Phase 8 — Hybrid expansion (v1.1.0)

- **Closing project totals.** Skills: 235, in 18/18 departments (227 + 8 hybrid-mission skills: clone-redesign, rebrand-execution, project-takeover, prototype-hardening, seo-migration, ai-retrofit, market-expansion, saas-conversion). Detection parameters: 203 (7 families — unchanged this phase). Playbooks: 21 (13 by app type + 8 hybrid mission playbooks). Bundles: 43 files (core + 20 department bundle files covering 18 departments — `seo-content` and `devops-deployment` each split across two files — + 21 playbook bundles + `ALL_SKILLS.md`). Worked examples: 706 files (682 pre-Phase-8 + 24 new; the v1.0.0 documents' "681" figure was off by one — the pre-existing `vector-db` skill carries a fourth example).
- Final validation: `scripts/validate-skills.py` — "Checked 235 skills. ALL PASS" (integration run, re-confirmed on debater re-runs).
- Findability spot check on the new skills: **5/5 correct first choices** (fresh agent, BOOTSTRAP + SKILLS_INDEX only).
- Dry run: one new hybrid playbook exercised end-to-end by a fresh agent — **12 friction points recorded, each dispositioned** (fixed, or waived with a recorded reason) before the board stage.
- Debater stage: 44 upheld flaws fixed across the 8 new skills (per-slice counts in work-log/phase-8.md), plus the `KEY_SKILLS` registration fix that unblocked the 8 hybrid playbook bundles (with 2 parser micro-fixes) and the anatomy assignments for the 8 new skills (catalog: 128 elements). One rule-ID collision between the two new D15 skills was caught in integration and fixed by renumbering `project-takeover` (DX-181–192 block).
- Version: 1.0.0 → **1.1.0** (see `VERSION`, `CHANGELOG.md`, decision D-020).
- Staffing (as commissioned, D-020): 30 builders + 10 cross-assigned debaters + 5-member board + 4-member final committee, under the upgraded handoff/verification protocol. Full record: docs/work-log/phase-8.md.
