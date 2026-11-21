# WCPM_MAPPING.md — Web Craft Pro Max inheritance map

Purpose: the traceability record for the §2 inheritance. It states, with evidence, how the inherited Web Craft Pro Max file (4,015 lines: 13 sections + 6 appendices) reconciles against the brief's summary of it, and where every major structure lands in this repository. Audience: D3 (Frontend, Design & Motion), the detection squads, Verification & Sources, and future maintainers. Rule for this document: discrepancies are stated plainly, never smoothed over; every drop is named with a reason.

Source: `web-craft-pro-max/SKILL.md` and `web-craft-pro-max/RESEARCH_PAPER.md` as received in the handoff zip. Script-measured counts (executor, 2026-11-21): 200 unique BAN IDs (01–200); 198 unique `R-<section>-<n>` rule IDs; 79 unique `G-<PREFIX>-<NN>` gate IDs (DES 6, ENG 14, EXP 11, INT 8, MOT 10, QA 10, SCH 11, VIS 9).

---

## 1. Gate reconciliation — the brief's "69 gates"

**Verdict: the brief's "69 gates" matches the §12.3 acceptance-gate register exactly. It does not match the file's total gate-ID count (79), and the inherited file's own checklist states a third number (68) that matches neither.**

Evidence — §12.3 "Acceptance gates (register)" read in full (SKILL.md lines 2908–3019). The register defines seven families; a script count of unique gate IDs inside the register region returns exactly 69:

| Family | Gates in §12.3 register | IDs |
|---|---|---|
| G-DES (Design) | 6 | G-DES-01…06 |
| G-MOT (Motion) | 10 | G-MOT-01…10 |
| G-VIS (Visual) | 9 | G-VIS-01…09 |
| G-SCH (Search) | 11 | G-SCH-01…11 |
| G-ENG (Engineering) | 14 | G-ENG-01…14 |
| G-EXP (Experience) | 11 | G-EXP-01…11 |
| G-INT (Integration) | 8 | G-INT-01…08 |
| **Register total** | **69** | |

Where the other 10 of the 79 IDs live: **G-QA-01…G-QA-10 are defined in §12.5 "QA protocol (skill releases)"** (lines 3050–3080), not in §12.3. They are hard gates for releasing the *skill itself* (zero invented content in QA scenarios, zero builder fingerprints, detector score ≤19, human review 2-of-3), and several deliberately mirror register gates: G-QA-03 restates the G-DES-01 bar (0 P0 parameters + rubric ≥90 + every category ≥7 + zero F1–F8 auto-fails); G-QA-06 mirrors G-EXP-05 (axe-core 0 violations); G-QA-08 mirrors G-ENG-01 (build/lint/type-check pass). They are a QA mapping layer over the register, not additional project-acceptance gates.

Two further gate-like structures carry **no** G- IDs and so enter neither count:

- **§12.1 phase gates:** 6 numbered workflow gates (1 INSPECT, 2 PLAN, 3 IMPLEMENT, 4 VALIDATE, 5 REVIEW, 6 DELIVER). They gate phase transitions, not acceptance criteria.
- **§13.3 generational novelty gate:** checklist item **A-15** (the "2002 test" — a build that merely matches the previous generation's level fails). It lives in the §13 acceptance checklist's A- namespace, not the G- namespace.

The discrepancy that does **not** reconcile: the inherited file's own §12 acceptance check (line 3113) instructs "All **68** acceptance gates run" — 68 matches neither its own register (69) nor its total (79). It is a stale count inside the source file. A smaller mislabel travels with it: Appendix B.1 names §12.3 as the definition site for the entire `G-` namespace, but G-QA-01…10 are defined in §12.5.

**Repo ruling (recorded, per §2):** this repository adopts **69** as the acceptance-gate count (the §12.3 register). G-QA-01…10 are inherited as the D8 skill-release QA protocol and land in `gates/` with D8 in Phase 5 — counted separately, never merged into the 69. The source's "68" is recorded here as a known source error and is not copied anywhere.

---

## 2. Inheritance map — where each structure lands

D3 skills named below are from the §3.12 catalog: frontend-core, design-system, design-tokens, component-library, motion, scroll-experiences, layout-responsive, typography, ui-states, frontend-state, data-fetching, client-routing, forms, data-visualisation, pwa-offline, webgl-3d.

### 2.1 The BAN list (Appendix A — 200 banned patterns + 3 word lists)

Appendix A structure: A.1 CRITICAL bans BAN-01–08 (verbatim); A.2 BAN-09–123; A.3 BAN-124–200; A.4 banned adjectives (42 words); A.5 banned filler; A.6 banned phrases for verification/reporting. Each BAN row carries a legacy working ID (L-/C-/T-/W-/M-/I-/D- namespaces, retired per Appendix B.3) — that column is preserved in the receiving skills for traceability.

| BAN subject cluster | Lands in (D3) | Detection cross-reference |
|---|---|---|
| Layout/section bans (working IDs L-, most of A.2/A.3) | layout-responsive, design-system | DET-VIS-001…010 (layout & spacing group) |
| Typography bans (T-) | typography | DET-VIS-011…016 |
| Colour/gradient bans (C-) | design-tokens, design-system | DET-VIS-017…022 |
| Component bans | component-library | DET-VIS-031, 033, 036 |
| Imagery/icon bans (I-) | design-system, component-library | DET-VIS-023…030, 025, 026 |
| Motion bans (M-) | motion | DET-VIS-040, 041 |
| Data/fabrication bans (D-) | frontend-core (rendering of real data only) | DET-VIS-027, 034, 035; primary enforcement X-Fake/X-Content |
| A.4 banned adjectives, A.5 banned filler | frontend-core (UI copy rules) | DET-CON family (X-Content) |
| A.6 banned verification phrases | Repo-wide reporting rule — lands in `docs/` conventions, cited by every department's gates | DET-CRWL (evidence discipline) |

### 2.2 Rule sections (R-<section>-<n> — 198 unique IDs across §1–§13)

The split follows the file's own canonical-owner registry (Appendix B.2: one home per topic; other sections cite, never restate).

| Source section | Primary D3 home | Notes / cross-references |
|---|---|---|
| §1 Priority & conflicts | frontend-core | The operating core: priority order, status labels, never-cut rules |
| §2 Parameter catalog | design-system (as reference) | The catalog itself becomes DET-VIS cross-references (§2.4 below) |
| §3 Diagnosis & cures | design-system (CV cures), motion (CM cures), frontend-core (CD cures) | Rubric + F1–F8 auto-fails → `gates/` (G-DES-01 scoring method) |
| §4 Design brief & distinctiveness | design-system | BR- divergence rules and D-MIN thresholds travel with it |
| §5 Content architecture & copy | frontend-core (in-UI content) | Primary department is D9; D3 absorbs only the component-level content rules (CC cures) |
| §6 Visual craft | design-system, design-tokens, typography, layout-responsive | §6.8 visual-QA inspection method → gates cross-reference (§2.5) |
| §7 Motion & interaction | motion, scroll-experiences, webgl-3d (3D motion) | CR-09 reduced-motion rule cited by ui-states |
| §8 Components & states | component-library, ui-states, forms | State-transition rules cite §7, never restate |
| §9 Engineering | frontend-core, frontend-state, data-fetching, pwa-offline | Performance budgets (N-registry values) → `gates/` thresholds |
| §10 Search (SEO/AEO/GEO) | frontend-core (metadata/SSR rendering surface) | Primary department is D9; D3 absorbs only what the frontend must render |
| §11 Experience (responsive, a11y, conversion) | layout-responsive, ui-states, forms, pwa-offline | Accessibility rules cross-reference D13; never duplicated there |
| §12 Workflow, testing & verification | `gates/` (repo-level) | See §1 of this document; QA protocol → D8 |
| §13 Final acceptance checklist | `gates/` (repo-level) | A-01…A-15 retained as checklist item IDs |
| Appendix D — Sources | docs/WEB_CRAFT_PAPER.md + this file | The research paper ships corrected (26 figure replacements: 170→178, 16→17, 213→221) |
| Appendix E — Worked examples | examples/ | EX- IDs retained, including EX-SLOP-* counter-examples |
| Appendix F — Glossary & numbers registry | docs/ (glossary); `gates/` (N-registry thresholds) | N-values are cited by gates, not copied into skills |

### 2.3 Gate families (§12.3 register + §12.5 QA gates)

All 79 gate IDs land in the repo's `gates/` system in Phase 5, criteria text single-sourced there. D3 relevance, for the skills that must design to pass them:

| Family | Count | Designed-to-pass-by (D3) | Owner of the gate |
|---|---|---|---|
| G-DES | 6 | design-system | D8 (verification) |
| G-VIS | 9 | design-system, typography, design-tokens | D8 |
| G-MOT | 10 | motion, scroll-experiences, webgl-3d | D8 |
| G-SCH | 11 | frontend-core (rendering), D9 (content) | D8/D9 |
| G-ENG | 14 | frontend-core, data-fetching, frontend-state | D8 |
| G-EXP | 11 | layout-responsive, ui-states, forms | D8/D13 |
| G-INT | 8 | frontend-core | D8/D6 |
| G-QA | 10 | — (gates the skill release itself) | D8 |

### 2.4 Parameter families & tells (§2 catalog — 17 families, 178 parameters; + GL tells, CLU clusters)

The §2.2 family index sums to 178 across 17 families (LAY 10, SEC 8, TYP 10, COL 12, CPY 15, MOT 13, CMP 18, IMG 10, ICO 6, SPC 7, COD 20, NAM 8, DAT 7, BEH 10, A11Y 8, MET 10, CLU 6). In this repo the catalog's detection role is served by the X-Visual parameter file (`skills/detection/visual/PARAMETERS.md`, DET-VIS-001…044); the table below is the family-level cross-reference. Cure rules (§3.4: CV 25, CC 10, CM 14, CD 18 = 67) land with the D3 skill named for their family.

| Family (count) | D3 home (cures) | DET-VIS cross-reference |
|---|---|---|
| LAY — Layout patterns (10) | layout-responsive | DET-VIS-001, 002, 003, 005, 008, 010 |
| SEC — Section order & page shape (8) | layout-responsive, design-system | DET-VIS-006, 008 |
| TYP — Typography defaults (10) | typography | DET-VIS-011…016 |
| COL — Colour & gradient defaults (12) | design-tokens, design-system | DET-VIS-017…022 |
| CPY — Copy & wording tells (15) | frontend-core (CC cures) | DET-VIS-034, 035 (visible surface); full set → DET-CON |
| MOT — Animation & motion defaults (13) | motion | DET-VIS-040, 041 |
| CMP — Component patterns (18) | component-library | DET-VIS-003, 026, 031, 033, 036 |
| IMG — Image style tells (10) | design-system | DET-VIS-023, 024, 029, 030 |
| ICO — Iconography (6) | component-library, design-system | DET-VIS-016, 025, 026 |
| SPC — Spacing & rhythm tells (7) | design-tokens, layout-responsive | DET-VIS-001, 004, 043 |
| COD — Code-structure tells (20) | frontend-core (CD cures) | → DET-CODE (X-Code); no DET-VIS equivalent — code tells are not visual |
| NAM — Naming & placeholder tells (8) | frontend-core | → DET-CODE / DET-CON |
| DAT — Data & content tells (7) | data-fetching, frontend-state | DET-VIS-027, 034, 035; primary → DET-FAKE |
| BEH — Behaviour & interaction tells (10) | ui-states, frontend-state, motion | DET-VIS-032, 037, 038, 039, 042, 044 |
| A11Y — Accessibility tells (8) | ui-states, layout-responsive | DET-VIS-022, 041; full set → D13 / DET-UX |
| MET — Meta, SEO & deployment tells (10) | frontend-core | DET-VIS-030, 034; primary → DET-CON / D9 |
| CLU — Attractor clusters (6) | design-system | Cluster rule in PARAMETERS.md (3+ minor in one cluster = 1 major) mirrors CLU-01…06; G-DES-02 enforces |
| GL — 3D/WebGL tells (§3.6, 5 IDs) | webgl-3d | G-VIS-09 enforces 0 GL tells at P0/P1 |

### 2.5 QA mappings (Appendix B.4 — Visual QA → G mapping, VQ-0…VQ-12)

All 13 visual-QA checks (VQ-0…VQ-12) are already mapped to gates in the source (the source marks this VERIFIED at assembly, and the mapping checks out against the register). In this repo the table lands in `gates/` as the visual-QA index: the *method* (§6.8 inspection walk, viewport ladder, capture protocol) is cited by design-system and layout-responsive; the *gate criteria* stay single-sourced in `gates/`. Nothing in B.4 is dropped — but its gate text is not copied a second time into any skill (see Drop 2).

### 2.6 Drops — named, with reasons (never silent)

| # | Dropped item | Reason |
|---|---|---|
| 1 | The single-file operating preamble: "How to use this file", Install (one route per agent), Trimming, Never-cut core, Portability | Superseded by this repo's own install system (bundles, BOOTSTRAP, custom instructions). Two install authorities would conflict; the repo's wins because the brief mandates the §5.1 layout |
| 2 | Appendix C quick-reference tables (as standalone content) | They restate §6/§9 thresholds that Appendix F's numbers registry already single-sources. Keeping both copies is how the source's own 68-vs-69 slip happened. Thresholds survive — cited from the N-registry in `gates/` |
| 3 | §13 checklist criterion restatements (e.g. CR-11 repeats the G-DES-01 criterion verbatim) | The checklist survives in `gates/` as item IDs (A-01…A-15, CR-09…CR-12) citing their gates; duplicated criterion text is dropped so a threshold can never drift between two copies |
| 4 | §3.4 cure table's parameter restatements | Parameters keep exactly one home (the §2 catalog → DET-VIS/D3 cross-references in §2.4). Only the cure text (CV/CC/CM/CD) moves into the D3 skills |
| 5 | G-QA-03's restated criterion text | In the D8 QA protocol it becomes a citation of G-DES-01 — the same bar, referenced once, per the source's own "cite, never restate" rule (Appendix B.2) |
| 6 | §12.5 QA scenario fixtures (S1 "Northwind Heat Pumps", S2 "Installer Hub", S3 "Mara Ellison" content packs) | Fixtures of the WCPM project's own release QA. This repo's proof projects (P1–P4, §9) replace them; the §12.5 protocol (scoring, hard gates, multi-model rule, regression) is fully retained in D8 |

Nothing else is dropped. Structures mapped in total: 200 BAN entries + 3 word lists; 198 R- rule IDs across 13 sections; 79 gate IDs (69 register + 10 QA); 178 parameters in 17 families + 5 GL tells + 6 CLU clusters; 67 cure rules; 13 VQ mappings; 15 acceptance items (A-01…A-15).

---

## 3. Format conversion rules — 4,015 lines → §5.4 SKILL.md files

1. **Split by the source's own owner registry.** Appendix B.2 already declares one canonical home per topic. The split follows those owner boundaries into the D3 skills named in §2 above — not by page count and not by the source's section order alone. A topic is never split across two skills; the non-owner skill cites the owner's ID instead of restating the rule (the source's own rule, applied to itself).
2. **Size rule.** Each output SKILL.md follows the §5.4 mandatory section order and stays ≤400 lines / ~5,000 words. Where an owner section exceeds the cap (§7 motion, §6 visual craft), it splits by family — e.g. §7 → motion (tokens, entrances, micro-interactions) + scroll-experiences (scroll, parallax) + webgl-3d (3D motion) — with each part carrying the full §5.4 structure for its scope.
3. **IDs are frozen and survive verbatim.** Per Appendix B.1 ("IDs are frozen: never renumber, never reuse a retired ID"), BAN-NN, R-<section>-<n>, G-<DOMAIN>-<nn>, the §2 family parameter IDs (LAY-01…CLU-06), cure IDs (CV/CC/CM/CD), F1–F8, and A- item IDs are cited inside the receiving skills exactly as printed in the source. A reader holding either file can trace any ID to the other through this document. BAN citation form: Appendix A prints BAN-01…BAN-08 (A.1) and three-digit forms (BAN-068) in the A.2/A.3 tables; the numeric identity (1–200) is what is preserved.
4. **One home per number.** Thresholds live in the Appendix F numbers registry and are cited by value + N-ID from skills and gates; no skill copies a threshold table (Drop 2).
5. **Worked examples move, IDs intact.** Appendix E examples (EX-, EX-SLOP-*) land in `examples/` beside the skill they illustrate, referenced from the skill's Examples section — they do not inflate SKILL.md line counts.
6. **What does not convert.** Content whose home is not a D3 skill (§12/§13 workflow and gates, §12.5 QA protocol) converts into `gates/` and D8 documents in the same operation, so no structure is left behind in the single file; the single file itself is not shipped.
