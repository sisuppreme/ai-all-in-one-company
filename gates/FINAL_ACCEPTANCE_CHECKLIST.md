# FINAL_ACCEPTANCE_CHECKLIST.md — Final acceptance checklist (A-01…A-15, CR-09…CR-12)

From Web Craft Pro Max §13. **Governing statement: nothing ships until this checklist is complete. An unchecked item with no disclosure means the project is not complete. There is no third option.**

Every item must be VERIFIED, labeled NOT APPLICABLE with a reason, or listed as a disclosed exception (max 2 mandatory items per delivery). Per the Drop 3 ruling in `docs/WCPM_MAPPING.md`, this checklist states each item's name and **cites the gate(s) that carry its criterion** — the criterion text itself lives only in `gates/ACCEPTANCE_GATES.md`, so a threshold can never drift between two copies.

## Features & correctness

- [ ] **A-01.** Every requested feature works as VERIFIED, with named evidence; non-VERIFIED features are listed with their label and the missing check. — Verifies: G-INT-01, G-INT-08
- [ ] **A-02.** Nothing pre-existing is knowingly broken; pre-existing defects found during the work are disclosed even if out of scope. — Verifies: G-INT-01
- [ ] **A-03.** Real tests are separated from assumptions: executed checks are listed separately from anything assumed, inferred, or untested. — Verifies: G-INT-08

## UI, responsive & motion

- [ ] **A-04.** Every created/changed page inspected via screenshot at 320/768/1440 px minimum (full ladder for new sites). — Verifies: G-EXP-01, G-EXP-02 (method: VQ-1, VQ-3 in `gates/VISUAL_QA_INDEX.md`)
- [ ] **A-05.** Scroll motion is deliberate and non-blocking; sticky elements never cover content or controls. — Verifies: G-MOT-08, G-MOT-10, G-EXP-01
- [ ] **A-06.** Accessibility is respected: keyboard-only pass, reduced-motion pass, contrast and forced-colors checks completed on key pages — label the specific checks run, never write "fully accessible". — Verifies: G-EXP-04, G-EXP-05, G-EXP-06, G-MOT-06

## Security, data & safety

- [ ] **A-07.** Security is considered: auth boundaries tested from both sides where auth exists; state which checks ran; never claim "secure". — Verifies: G-ENG-09, G-ENG-10, G-ENG-11
- [ ] **A-08.** Database changes are safe (or NOT APPLICABLE): migrations tested on a realistic data copy, row counts verified, rollback tested or irreversibility disclosed, no production data used for testing. — Verifies: G-INT-04 (rollback); no dedicated register gate — this item is itself the check.

## Public content — SEO / AEO / GEO

- [ ] **A-09.** Every public page carries its full metadata set, verified by viewing the rendered page source/snapshot — not by reading the template alone. — Verifies: G-SCH-01, G-SCH-02, G-SCH-03, G-SCH-04

## Quality gates & disclosure

- [ ] **A-10.** Static gates pass, with commands and exit codes recorded; any warning is fixed or listed with a reason. — Verifies: G-ENG-01
- [ ] **A-11.** Console and network gates pass on the happy path for created/changed pages; every exception explained in the report. — Verifies: G-ENG-07
- [ ] **A-12.** Every BLOCKER and MAJOR defect is fixed and re-tested (VERIFIED) or listed in the delivery report with severity, reproduction steps, and the recommended next step. — Verifies: G-INT-08 (defect classes: `gates/DEFECT_TAXONOMY.md`)
- [ ] **A-13.** No banned phrase appears in the report. — Reporting rule: the banned verification/reporting phrases are the Appendix A.6 word list, owned repo-wide per `docs/WCPM_MAPPING.md` §2.1; report honesty is enforced by G-INT-08.
- [ ] **A-14.** The delivery report is complete: file list, verification evidence, one status label per claim, defect log, residual risks, rollback plan (Tier 3), next steps for every non-VERIFIED item. — Verifies: G-INT-08, G-INT-04

## CRITICAL rules check (§13.2)

The source's §13.2 also re-checks BAN-01…BAN-08 at delivery; those bans live in the D3 skills that own them (traceability in `docs/WCPM_MAPPING.md` §2.1) and are not restated here. The CR items:

- [ ] **CR-09.** Full reduced-motion support. — Verifies: G-MOT-06
- [ ] **CR-10.** Every entrance, transition, and cascade within the duration ceiling (named exemptions only). — Verifies: G-MOT-01, G-MOT-03
- [ ] **CR-11.** The delivery bar. — Verifies: G-DES-01
- [ ] **CR-12.** Every generation must produce a NEW LEVEL of UI/UX. — No register gate; this is the generational-novelty directive, enforced at delivery by A-15 with G-DES-02 and G-DES-06.

## Generational novelty gate (§13.3)

- [ ] **A-15.** The 2002 test passes: the finished site is as different from the previous build as Google's 2002 site was from Apple's 2002 site. A build that merely matches the last generation's level FAILS. — No register gate; A-15 is itself a gate in the A- namespace (see `docs/WCPM_MAPPING.md` §1), applied alongside G-DES-02 and G-DES-06.

## Sign-off (§13.4)

If all applicable items are VERIFIED, state: "Acceptance checklist complete: [n] items VERIFIED, [n] not applicable, [n] disclosed exceptions (listed below)." Then list the exceptions. If any item fails and is not disclosed, the project is not complete. Do not deliver it as complete. The checklist is a record, not a ritual: an item checked without the underlying evidence is a false record. If challenged, produce the command, screenshot, or test output behind any checked item.
