# VISUAL_QA_INDEX.md — Visual QA checks → gates (VQ-0…VQ-12)

The 13 visual-QA checks from Web Craft Pro Max Appendix B.4, each mapped to the gate(s) that enforce it. The source marks this mapping **VERIFIED at assembly**: all 13 checks are enumerated and mapped; none is unmapped, and none is dropped in this repo.

**Where things live.** The *method* — the §6.8 inspection walk, the viewport ladder, the capture protocol — lives in the D3 skills (`design-system` and `layout-responsive` cite it). The *criteria* stay single-sourced in `gates/ACCEPTANCE_GATES.md`. This file is only the index between them: it names which gate enforces which check, and restates no criterion.

| Visual QA check | Maps to (skill) | Gate(s) |
|---|---|---|
| VQ-0 What the gate is | §6.8 (inspect the render, not the code) | G-VIS-01–09 |
| VQ-1 Viewport ladder | §11.1 (canonical ladder) | G-EXP-01, G-EXP-02 |
| VQ-2 Capture protocol | §6.8 + §12.2 (screenshots as evidence) | G-INT-08 |
| VQ-3 Inspection walk | §6.8 (ordered procedure per page per width) | G-VIS-01–08 |
| VQ-4 Sticky-collision protocol | §13.1 A-05 (sticky never covers content/controls) | G-EXP-01 |
| VQ-5 Defect catalog | §12.1 (defect log) + §13.1 A-12 | G-INT-08 |
| VQ-6 Programmatic checks | §9.2 (budgets) + §11.3 (contrast/scan) | G-ENG-02/03/08, G-EXP-05/06 |
| VQ-7 Screenshot review method | §6.8 + §12.2 | G-VIS-01–08 |
| VQ-8 Motion/themes/engines/keyboard passes | §7.7, §6.2, §11.3 | G-MOT-06, G-EXP-04, G-EXP-07 |
| VQ-9 Fix-and-re-inspect loop | §12.1 (fix-and-retest, max 3 attempts) | All gates |
| VQ-10 Honest reporting | §12.2 (status labels) | G-INT-08 |
| VQ-11 Banned list (visual QA) | Appendix A | BAN-01–200 |
| VQ-12 Acceptance checklist | §13.1 (final acceptance checklist) | A-01–A-15 |

Notes:

- VQ-11 maps to the BAN list, not to a G- gate: the 200 banned patterns live in the D3 skills that own them (traceability in `docs/WCPM_MAPPING.md` §2.1).
- VQ-12 maps to the acceptance checklist items A-01–A-15, which live in `gates/FINAL_ACCEPTANCE_CHECKLIST.md`.
