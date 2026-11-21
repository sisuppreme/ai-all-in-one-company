# Work log — Phase 2 (Department research)

Phase dates: started 2026-11-21. Owners: all 18 departments in four waves (§7); D3 carries the Web Craft Pro Max inheritance integration (§2).

## 2026-11-21 — Launch + WCPM inheritance counts (executor)

- Waves: W1 = D1, D2, D10, D15 (launched); W2 = D3, D4, D5, D13, D16, D17; W3 = D6, D7, D11, D14; W4 = D8, D9, D12, D18. Each department writes `docs/internal/research/<code>.md` — standards, failure modes, per-skill research notes, gates, sources — the direct input to Phase 3 drafting.- **§2 inheritance verification, script-measured on the received SKILL.md (4,015 lines):**
  - BAN entries: **200 unique IDs (BAN-01…BAN-200)** — brief claim 200 ✓ confirmed.
  - Rule IDs: **198 unique `R-<section>-<n>` IDs** — brief claim 198 ✓ confirmed.
  - Gates: **79 unique `G-<PREFIX>-<NN>` IDs** (DES 6, ENG 14, EXP 11, INT 8, MOT 10, QA 10, SCH 11, VIS 9) vs the brief's claim of 69. The file has a §12.3 "Acceptance gates (register)" — reconciliation (register count vs total IDs) is D3's integration task; the outcome is recorded in `docs/WCPM_MAPPING.md`. Until then the honest statement is: 79 gate IDs exist; the brief's 69 is unconfirmed, not yet contradicted (the register may hold exactly 69 acceptance gates).
  - ID-scheme note: the file's own schemes (BAN-NN, R-x.y-z, G-PREFIX-NN) are what the repo inherits; the brief summary's `DET-`/`BAN-<CODE>-<NNN>` descriptions apply to this repo's own new artifacts, and the mapping doc records both.

## 2026-11-21 — Wave 1 complete (executor)

- D1 (28.9 KB), D2, D10, D15 (21.9 KB) research files written to `docs/internal/research/` — 44 skills with core methods, encodable rules, automatable gates, verified sources.
- Notable open risks carried to Phase 3: D2's three API skills need one pre-decided house style (Zalando vs Google conventions conflict); D10's DECISIONS.md vs docs/adr/ duality must be resolved inside the skills; D15 flags generated-stub vs Real Content Rule tension and single-agent translation of team practices. These get DECISIONS entries or drafting rules in Phase 3, not silence.
- Wave 2 launched: D3 research + D3 WCPM integration (mapping + corrected paper), D4, D5, D13, D16, D17.

## 2026-11-21 — Wave 2 complete + WCPM integration (executor)

- Research files: D3 (40 KB), D4 (~39 KB), D5 (39 KB), D13, D16 (22 KB), D17 (23.9 KB) — 79 more skills researched (123 cumulative of 227). [Correction: this entry originally said 63/107 — executor arithmetic error, fixed 2026-11-21.]
- **WCPM integration delivered:** `docs/WCPM_MAPPING.md` + `docs/WEB_CRAFT_PAPER.md`.
  - **Gate reconciliation (the 69 vs 79 question): RESOLVED in the brief's favor.** The §12.3 acceptance-gate register holds exactly **69** gates (DES 6 + MOT 10 + VIS 9 + SCH 11 + ENG 14 + EXP 11 + INT 8). The 79 total adds G-QA-01…10, §12.5 skill-release QA hard gates. The inherited file's own §12 text says "68 gates" — a stale internal error in the source, recorded in the mapping, not copied into the repo.
  - Mapping covers: 200 BAN entries + 3 word lists, 198 R- rule IDs (split per the source's Appendix B.2 owner registry), all 79 gate IDs, 178 parameters / 17 families + tells, 67 cure rules, 13 VQ QA mappings. **6 drops, each named with a reason** (install preamble superseded by the bundle system, duplicate quick-reference tables, verbatim criterion restatements, §3.4 restatements, one restated gate criterion → citation, S1–S3 scenario fixtures replaced by proof projects P1–P4). No silent drops.
  - Paper shipped with **26 figure replacements** (170→178, 213→221, 16→17 families/dimensions) + an editor's note recording the corrections and the Phase 1 calibration verdict; protected strings (file-length figures, DOI, CFR citation) verified untouched.
- Wave 3 launched: D6, D7, D11, D14.

## 2026-11-21 — Wave 3 complete (executor)

- Research files: D6 (~40 KB), D7 (~41 KB), D11 (40 KB), D14 (42 KB) — 53 more skills (176 cumulative of 227).
- Notable Phase 3 inputs: D6 recommends explicit posture tiers (free-tier launch vs production-grade) with named promotion triggers, resolving the D-005 tension structurally; D7 draws the audit-vs-penetration-test authorization line (owner-controlled systems, written engagement); D14 requires structural forcing functions for clone-ethics (pre-committed authorization artifacts checked by tooling) instead of single-agent self-approval; D11 keeps invoicing-tax to patterns only, no jurisdiction rates.
- Wave 4 launched: D8, D9, D12, D18 — the final research wave.

## 2026-11-21 — Wave 4 complete — PHASE 2 COMPLETE (executor)

- Research files: D8 (45 KB), D9 (44 KB), D12 (46.5 KB), D18 (27 KB) — 51 more skills. **Phase 2 exit state: 18/18 department research files in `docs/internal/research/`, 227/227 catalog skills with research notes, plus the WCPM integration (`docs/WCPM_MAPPING.md`, `docs/WEB_CRAFT_PAPER.md`).**
- Cross-department boundary agreements recorded in the research files themselves (D6↔D12 monitoring split, D11↔D4/D7 overlaps, D14 clone-ethics ownership, D18↔D1/D11/D12 metric co-ownership) — Phase 3 drafters cross-reference rather than duplicate.
- Phase 3 setup followed immediately: skill template + rule ID registry shipped (see work-log/phase-3.md).
