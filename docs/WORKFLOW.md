# WORKFLOW.md — How this repository was built

Purpose: the build workflow as actually executed (§5.1, §6.1), written as a reusable method — an operator should be able to re-run this workflow from this document alone. Audience: future maintainers and anyone repeating the build. The diary is elsewhere: `docs/WORK_LOG.md` indexes the per-phase logs (`docs/work-log/phase-0.md` … `phase-6.md`), `docs/DECISIONS.md` records every deviation, and `docs/METRICS.md` defines every number. This file is the method those records evidence.

**Executed:** 2026-11-21, from Master Brief v5.1 (1,194 lines), under repo version 1.0.0.

---

## 1. The workflow at a glance

Eight phases, strictly ordered where the brief orders them, each with a named deliverable set and a mechanical exit gate. No phase starts on the previous phase's *drafts* — it starts on its *validated outputs*.

| Phase | Name | Produces | Exit gate (all mechanical or independently verified) |
|---|---|---|---|
| 0 | Discovery | Project anatomy (127 elements), project-file set, playbook set | Traceability gate, script-checked both directions |
| 1 | Detection research | 203 detection parameters in 7 families + calibration record | Consistency audit + false-positive passes |
| 2 | Department research | 18 research files; 227/227 skills grounded; inheritance mapped | Coverage count 227/227; WCPM counts script-verified |
| 3 | Skill drafting | 227 SKILL.md files + 681 example files | `scripts/validate-skills.py` — ALL PASS, per wave and full-repo |
| 4 | Cross-review | Substance review of all departments; fixes | 0 blockers unresolved; full-repo validation ALL PASS after fixes |
| 5 | Forge | Index, bootstrap, bundles, playbooks, gates registry, custom instructions | Independent verification (9 checks); bundle caps; ID set-equality |
| 6 | QA / proof test | 4 proof projects, 8 dry runs, findability test, rendered FP pass | Per-project thresholds; all repo defects fixed + re-verified |
| 7 | Finalise | README, USER_GUIDE, RESEARCH_PAPER, WORKFLOW, QA_REPORT | §9.1 ship checklist; final ship only on the user's approval |

Two ordering rules are load-bearing and were never violated:

- **Detection first.** Phase 1's parameters exist before Phase 2's department research and Phase 3's drafting, because every skill's BAN list must cite the parameter it defeats. Drafting before detection would have made traceability retrofitted fiction.
- **Template and registry before drafting.** Phase 3 opened by shipping `templates/SKILL_TEMPLATE.md` and `docs/RULE_ID_REGISTRY.md` (D-012: pre-assigned ID blocks — rules 20, gates 10, BAN entries 10 per skill, in catalog order). Parallel drafters can then never collide on an ID, and format validation is a script, not an opinion.

## 2. Standing rules that governed the build

These rules were in force from kickoff; each is recorded in `docs/DECISIONS.md`.

1. **Best-approach delegation (D-001).** The user delegated all technical questions to the executor in advance ("use the best technical approach, in advance, without asking"). Questions were therefore answered by evidence and recorded as decisions, not escalated. The two brief checkpoints became report-only deliveries. One decision was *not* delegated and never treated as delegated: the §9.1 criterion 16 final ship approval, which remains the user's, with no timeout.
2. **Auto agent mode (D-009).** From 2026-11-21 18:07 PKT the executor proceeded through all phases autonomously — no questions, reports at phase ends. The only remaining user actions were ones the executor technically cannot perform (setting account passwords through secure entry; creating the GitHub repository after the connector returned 403 on `create_repository` — D-011).
3. **Real content only.** No fake placeholders, data, people, social proof, or functionality anywhere — including in examples (a realistic-looking credential string in one example was replaced with an obviously fake token in Phase 4) and in reporting (an executor arithmetic error in a Phase 2 progress figure — 107 stated, 123 true — was corrected openly in the log and to the user). A claim without a source is cut or marked UNVERIFIED in place; the fact-sheet protocol governs research, drafting, and proof content alike.
4. **Single-agent compatibility is a hard constraint.** The repository is built *by* many agents but must work *for one*: a lone agent with no sub-agents, possibly modest context, no team, no provisioned infrastructure. Every artifact was tested against that consumer (Phase 6's proof team rule, §5 below), and every place the material silently assumed a team, a tool, or a provisioned environment was treated as a defect.
5. **Counts are floors (QB-14).** 227 skills, 203 parameters (floor 180), 13 playbooks (floor 11), 477 roles — research may raise a floor, never lower one. The two playbook additions (D-007) came from Phase 0 evidence, not preference.
6. **No silent drops.** Removing anything the brief or the inheritance names requires a recorded decision with a reason (WCPM mapping: 6 drops, each named; D-013: inherited IDs frozen as citations rather than renumbered).
7. **$0 spend (D-005).** Phase 6 hosting on free tiers first; provisioning gaps become recorded waivers with unblocking conditions, never silent payments or hidden skips.

## 3. Staffing model

### 3.1 The plan

The brief's §3.8 headcount — **477 roles** (306 workers, 36 minor leads, 18 major leads, 64 detection-squad members, 15 Forge, 12 Proof, 8 Paper & Records, 6 Verification & Sources, 5 Orchestrators, 7 Technical Board) — is a work-partitioning architecture, not a process count: every role has a named deliverable and a reviewer. The runtime executes those partitions in parallel batches and sequential passes; METRICS.md records spawned build agents by phase and role as the measurable proxy.

### 3.2 The correction (D-014) — read this before re-running

Through Phase 3 wave R2 the executor consolidated roles for speed (one researcher per department; one drafter per 6–7 skills; ~35 spawns). The deliverables were identical in form and passed the same gates, but the staffing did not follow the brief's structure, and §3.8 forbids reducing total headcount to fit a concurrency cap — waves and sub-waves are the sanctioned mechanism. When the user challenged the build on exactly this point, the executor disclosed the deviation plainly and corrected the model **from R3 onward**:

- **One agent per named deliverable** — one drafter per skill, one researcher per research file, one reviewer per cluster.
- **Named cross-cutting roles instantiated alongside**, per §3.8: department reviewer, detection re-check (rule 3), D8 gate liaison (rule 4).
- **Sub-waves of ~6 concurrent agents**, sequential between sub-waves, inside the measured concurrency (probe: a batch of 8 parallel agents, 8/8 completed, no throttling → measured concurrency ≥8; the probe was real Phase 0 work, not empty test agents).
- **No completed work redone** — the correction changed staffing, not artifacts, because the artifacts had passed the same gates either way.

Consequence, disclosed to the user at the time: longer wall-clock, within the 2.5B token budget. Total spawned build agents across the project exceed 400, matching the plan's headcount model (per-phase counts: Phase 4 — 12; Phase 5 — 17; Phase 6 — 28; earlier phases recorded in their work logs).

### 3.3 Wave structure

Phases 2 and 3 ran in the brief's department waves (W1: D1, D2, D10, D15 → W2: D3, D4, D5, D13, D16, D17 → W3: D6, D7, D11, D14 → W4: D8, D9, D12, D18), each wave re-run in dependency order per phase. Phase 3 drafting rolled out as R1–R7.4 by department after a single-department pilot (D1) whose format validation and substance spot-check set the standard the rollout waves were held to. Phase 5's Forge worked in two waves (F1: index, bootstrap, playbooks, gates, instructions; F2: structure, docs, examples, bundles, links) plus a separate verification agent. Phase 6's proof team was staffed entirely by fresh agents (§5).

## 4. Phase by phase — what each produced and how it was gated

### Phase 0 — Discovery

Eight parallel research slices (A–H) mapped the anatomy of a complete web project; a scripted traceability pre-check found 74 of 227 catalog skills traced to no element — clustering exactly where the brief's own project-file list is silent (all of D3, D17, D18, plus depth skills). A second batch (slices I–M, 59 elements) was commissioned *because the gate failed*, and the assembled anatomy (`docs/PROJECT_ANATOMY.md`: 127 elements, 12 parts + appendices) passed the gate in both directions: 227/227 skills trace to ≥1 element; 127/127 elements name ≥1 serving skill; 0 orphans. The same phase validated the 22 mandated project files (brief-internal names honestly marked UNVERIFIED where no public standard exists), added 9 research-supported files (→ D-006), and surveyed 20 web-app types against the playbook set (11 exact fits, 7 partial, 2 real gaps → 13 playbooks, D-007). **Lesson baked into the method: a failing gate at Phase 0 is the cheapest defect the build ever produced.**

### Phase 1 — Detection research

Seven squad agents drafted the 7 parameter files in parallel (203 parameters, all families above floor). Then validation, in three parts: a cross-family **consistency audit** (ID/format/Fix integrity PASS; 1 duplicate + 13 overlap clusters resolved by ownership division + 70 `See also` lines; 2 severity inconsistencies resolved by the tell-vs-verdict rule); **calibration re-verification** of the two inherited §2 claims (55.5% figure: untraceable, demoted to a sourced ballpark; vendor-gap claim: confirmed for text detectors — full record in `docs/RESEARCH_PAPER.md` §2.2); and **false-positive tests** against known-good sites (9 FP in the visual/content pass, 7 confirmed + 2 borderline in code/infra; all 14 flagged parameters narrowed in 37 field edits; every case re-walked clean). The 39 visual parameters not testable from text were recorded UNTESTED and explicitly carried into Phase 6 — the carry-forward was written into the phase log, not left to memory.

### Phase 2 — Department research

Four waves produced `docs/internal/research/D1.md` … `D18.md` (227/227 skills with research notes). In parallel, the D3 integration agent produced the inheritance deliverables: `docs/WCPM_MAPPING.md` (every inherited structure mapped to its home; the 69-vs-79 gate question reconciled against the §12.3 register; 6 drops named) and `docs/WEB_CRAFT_PAPER.md` (the inherited paper with 26 figure corrections + editor's note). Boundary agreements between departments (D6↔D12 monitoring split, D14 clone-ethics ownership, and others) were recorded in the research files themselves so Phase 3 drafters cross-referenced instead of duplicating.

### Phase 3 — Skill drafting

Template + registry first (§1), then a D1 pilot (13 skills, 2 drafters): format validation ALL PASS, and one validator bug found and fixed in the process (the validator counted checklist mentions as ID definitions — 51 false "duplicate ID" failures; fixed to count definitions only). Rollout waves R1–R7.4 drafted the remaining departments; after D-014, one drafter per skill. Every wave was validated per department before commit. One executor error is recorded in the log as a standing lesson: the R4.1 dispatch briefed three skill names invented from memory instead of read from the catalog; all three drafters correctly refused (no registry block, no research notes, no catalog entry), no files were written, and the real skills were drafted in their place. **Dispatch names are now always read from the catalog file, never recalled.** Exit: 227/227 skills, 681 example files, full-repo validation ALL PASS.

### Phase 4 — Cross-review

Six independent reviewers (one per department cluster) deep-read 94 skills against the Phase 2 research and skimmed the rest; reviewers edited nothing — six separate fix agents applied findings. Mechanical checks ran first (DET-citation existence: 185 distinct DET IDs cited, 0 dangling). Result: **0 blockers, 6 majors, 31 minors; no department needed a redraft.** All six majors were fixed (recorded in full in `docs/work-log/phase-4.md`), including the pattern that produced this phase's one new convention: BAN entries citing semantically nearest rather than matching DET parameters. The remedy — re-point where a match exists, otherwise mark **DET-NONE**, an explicit greppable null (D-016; 23 occurrences) — was written into `templates/SKILL_TEMPLATE.md` so future skills inherit it. Extending the DET families instead was rejected: new parameters would need Phase 1-style FP testing first. Checkpoint B was delivered as a report (D-009).

### Phase 5 — Forge

Assembly of the consumable product: `SKILLS_INDEX.md` (script-generated from metadata, never hand-maintained), `BOOTSTRAP.md` (61 lines, cap <100), 13 playbooks, the `gates/` registry (the 69 acceptance gates extracted faithfully from the inherited §12.3 register; the 10 QA-protocol gates kept separate), 4 custom-instruction sets, and 33 bundles generated only by `scripts/build-bundles.py`. The bundle cap (30,000 tokens; core <10,000) forced the phase's main decision: full-text department bundles exceeded the cap for 12 of 18 departments, so **D-015** put department bundles into "bundle form" (rules, gates, checklists, anchors in full; BAN entries complete except the "Bad:" narrative; examples/anti-patterns omitted with pointers), with a two-rung condensation ladder (anchors/gate-check condensation, then checklist omission) for the departments still over — all caps PASS, no file split, ID integrity verified by set equality against source skills for all 18 departments. An independent D8 verification agent then ran 9 checks: 7 PASS at first run, findability dry-run 9/10 (at the §5.3 bar), and 4 defects (1 P1, 3 P2) — all fixed and re-verified.

### Phase 6 — QA / proof test

Detailed in §5 below; exit state: final regeneration (34 bundles, 0 cap failures) and full-repo validation ALL PASS, run by the executor after the last fix batch.

### Phase 7 — Finalise

The record documents (this file, `docs/RESEARCH_PAPER.md`, README, USER_GUIDE, QA_REPORT) are assembled from the phase records — written from the logs, never reconstructed from memory — and `docs/BAR_TRACEABILITY.md` is completed with Phase 6/7 evidence. Ship follows the §9.1 checklist; criterion 16 (user sign-off) closes the build.

## 5. The defect loops

The build ran four distinct defect loops. Their shared shape is the method's core: **defects route to the owning department, fixes are verified by re-running the mechanical gates, and no defect is ever closed by weakening the criterion that caught it** (fix iterations capped at 3 per the brief; none needed a third).

### 5.1 Proof-team loop (Phase 6)

Fresh agents — never the authors of what they used, briefed only through the repo (BOOTSTRAP entry) — built four real projects (P1 TaskBoard as the single-agent proof under the mandatory AI Studio instructions, with load-order compliance measured; P2 Atlas Blog; P3 Ledger API; P4 ShopClone) and ran 8 playbook dry runs with small real builds. Thresholds per project: 0 critical defects, ≤3 minor, 0 P0 slop hits, 0 fake-content hits, gates green or formally dispositioned. Every repo defect a proof surfaced (DEF-001…006, DEF-01…05, D-P3-01…05, P4-D1…D9) was fixed by a separate fix agent in the owning department and re-verified. Recurring root causes, in order of frequency: cited-but-unshipped artifacts (manifests, scripts — fixed by shipping real ones); gates naming a single tool/environment as their only form (fixed by adding manual/local/substitute forms); team-assuming requirements (fixed with explicit single-operator modes). Provisioning-only failures (no hosting, no live Stripe, GitHub push blocked) were dispositioned as recorded waivers with unblocking conditions — visible in every proof report, never hidden.

### 5.2 Dry-run friction triage (Phase 6)

The 8 dry runs filed 66 friction points. A dedicated triage agent deduplicated them into **28 root-cause clusters** (DR-01…DR-22 open; AF-01…AF-06 already fixed by the proof batches; 6 not-a-defect — environment-only or deliberate design), checking current repo state before declaring any cluster open. Five fix agents then closed all 22 open clusters in parallel batches, including the structural ones: a named "pre-provisioning complete" state added to all 13 playbooks' Definitions of Done (DR-01), and bundle assembly fixed so playbook bundles carry gate criteria (DR-04).

### 5.3 False-positive narrowing loop (Phases 1 + 6)

Detection parameters were treated as code under test: run against known-good targets; on a fire, classify (breadth vs core); narrow breadth only; re-walk every firing case; keep fabrication/secret cores at blocker. Phase 1 narrowed 14 parameters (37 field edits); the Phase 6 rendered pass closed the 39 text-untestable visual parameters (4 fired, narrowed, re-walk 6/6 clear, UNTESTED now 0). The DET-NONE convention (§4, Phase 4) is this loop's sibling: where the honest answer is "no parameter covers this," the record says so in a form a script can find.

### 5.4 Review loop (Phase 4) and verification loop (Phase 5)

Substance review and assembly verification were both done by agents other than the producers, with findings written to files (`docs/internal/review/phase4-A.md` … `phase4-F.md`; `docs/internal/forge-verification-report.md`) and fixes applied by separate agents. The executor's own role in every loop: run the mechanical checks (validation, caps, ID integrity, citation existence) after each fix batch and record the result — verification is a command output, not an impression.

## 6. Records discipline

- **One work log per phase**, written as the phase runs (`docs/work-log/phase-<n>.md`), indexed by `docs/WORK_LOG.md`. Retroactive reconstruction is banned by the brief (§3.10) and was not needed: each phase log was closed at its phase end.
- **Every deviation is a DECISIONS entry** (D-001…D-017 by Phase 6 close), with context, decider, and consequences — including the executor's own errors (the D-014 staffing deviation; the R4.1 invented skill names; the Phase 2 arithmetic correction).
- **Every number is a METRICS triple** (value / definition / method). Where a number could not be honestly measured — billable tokens in this runtime — METRICS records the limitation and the proxy used, instead of an invented figure.
- **Git history mirrors the phases**: one commit per validated wave or phase, on branch `main`, from the local-first repo (D-002/D-011); push to GitHub happens at finalization, losing no history.

## 7. Re-running this workflow — operator checklist

1. **Intake in one pass.** Collect the brief, any inherited material (files, not summaries of files), naming/licence/hosting constraints, and the delegation rule (who answers technical questions mid-build). Record standing instructions as decisions before Phase 0.
2. **Verify the inheritance by script on day one.** Line counts, ID counts, register counts — before any of it is cited. Expect the source's self-summary to be wrong somewhere; find where while it is still cheap.
3. **Probe concurrency with real work.** Spawn the first research batch at increasing parallelism; record the measured cap in METRICS; plan sub-waves inside it. Never consolidate roles to fit the cap — split waves instead (D-014).
4. **Detection before departments; template and registry before drafting.** The two ordering rules in §1 are the difference between traceability that is real and traceability that is theater.
5. **Gate every phase mechanically, and let gates fail.** Budget the second research batch, the validator fix, the re-narrowing pass *before* they happen: each phase of this build produced exactly one such loop, and each loop made the final artifact measurably better.
6. **Staff review and proof with strangers.** Reviewers must not be authors; proof agents must be briefed only through the artifact under test. Compliance (load order, sources actually consulted) is measured and recorded, not assumed.
7. **Route defects to owners; never weaken the catching criterion.** Cap fix iterations at 3; disposition environment-only failures as waivers with unblocking conditions, in the open.
8. **Write the record as you go.** Work log per phase, decision per deviation, metric per number. The Phase 7 documents then assemble themselves from records — if they cannot, the records were the defect.
