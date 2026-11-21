# Work log — Phase 1 (Detection research)

Phase dates: started 2026-11-21. Owners: the seven X squads (§3.3), coordinated by the executor. Rule: detection research comes before department research (§7) — parameters are evidence, not opinion; every parameter carries a source or an EVIDENCE_BASE reference.

## 2026-11-21 — Launch (executor)

- Phase 0 closed same day (see phase-0.md). Per D-009 (auto agent mode) Phase 1 starts without waiting.
- Batch 1: 7 parallel agents, one per family, each drafting its family's parameter file at `skills/detection/<family>/PARAMETERS.md` with `DET-<FAMILY>-<NNN>` IDs:
  - X-Visual → visual/PARAMETERS.md (DET-VIS, floor 40) + calibration re-verification (§2: the 55.5% human-detection figure and detector-claims-vs-benchmarks — trace to real studies or report untraceable)
  - X-Code → code/PARAMETERS.md (DET-CODE, floor 30)
  - X-Infra → infra/PARAMETERS.md (DET-INF, floor 25)
  - X-Content → content/PARAMETERS.md (DET-CON, floor 25)
  - X-UX → ux/PARAMETERS.md (DET-UX, floor 25)
  - X-Fake → fake/PARAMETERS.md (DET-FAKE, floor 20)
  - X-Crawl → crawl/PARAMETERS.md (DET-CRWL, floor 15 — evidence-pipeline checks)
- Validation (inter-rater pass, false-positive tests on known-good projects, severity calibration) follows drafting; results recorded here and in METRICS.md.

## 2026-11-21 — Drafting complete: 203 parameters (executor)

| Family | File | Parameters | Floor | Result |
|---|---|---|---|---|
| X-Visual | skills/detection/visual/PARAMETERS.md | 44 (DET-VIS-001–044) | 40 | ✅ |
| X-Code | skills/detection/code/PARAMETERS.md | 33 (DET-CODE-001–033) | 30 | ✅ |
| X-Infra | skills/detection/infra/PARAMETERS.md | 30 (DET-INF-001–030) | 25 | ✅ |
| X-Content | skills/detection/content/PARAMETERS.md | 28 (DET-CON-001–028) | 25 | ✅ |
| X-UX | skills/detection/ux/PARAMETERS.md | 28 (DET-UX-001–028) | 25 | ✅ |
| X-Fake | skills/detection/fake/PARAMETERS.md | 22 (DET-FAKE-001–022) | 20 | ✅ |
| X-Crawl | skills/detection/crawl/PARAMETERS.md | 18 (DET-CRWL-001–018) | 15 | ✅ |
| **Total** | | **203** | 180 | ✅ |

- **Calibration (§2 re-verification, in the VIS file):** Claim 1 (humans detect AI websites at ~55.5%) — **partially supported**: the exact figure is untraceable; peer-reviewed evidence (Cooke et al., CACM: 51.2% overall) supports only the near-chance ballpark. The repo therefore cites the ballpark with sources, never the bare 55.5%. Claim 2 (detector vendor claims 15–30 points above independent benchmarks) — **confirmed** with named pairs (Copyleaks 99.12% claimed vs 66% measured; GPTZero 99% vs 52%), caveat: benchmarks cover text detectors.
- Local commit 849ccfc (16 files, 452 KB) ready to push; GitHub repo creation moved to the user after the connector returned 403 on create (DECISIONS.md D-011).
- Validation batch launched: false-positive tests + cross-family consistency audit (below).

## 2026-11-21 — Phase 1 complete: validation results (executor)

- **Consistency audit (script-checked):** 203 parameters; ID integrity, format integrity, Fix-field integrity (46 distinct fix names, all real catalog skills), source honesty — PASS. Two FAILs, both fixed: (1) one true duplicate (DET-UX-003 ↔ DET-FAKE-015) + 13 overlap clusters with no cross-references → **70 `See also` lines across 39 parameters**, duplicate kept with a stated division of ownership (UX owns the symptom, FAKE owns the verdict); (2) two severity inconsistencies → resolved by the audit's tell-vs-verdict rule (VIS tells keep their rating; the CON fabrication verdict stays **blocker**, cross-referenced both ways). No parameter deleted or renumbered.
- **False-positive test 1 (VIS/CON vs stripe.com, linear.app, basecamp.com):** 9 false positives in 5 parameters — all breadth problems (first-party stats and ordinary puffery flagged at blocker/major). Fabrication core (DET-CON-010/012/013/019) fired nowhere. 39/44 VIS parameters are not testable from fetched text (need screenshots/computed styles) — recorded as UNTESTED, scheduled for the Phase 6 browser proof, not silently passed.
- **False-positive test 2 (CODE/INF vs Discourse):** 7 confirmed + 2 borderline false positives — grep checks not excluding samples/templates/docs/locales, FP clauses naming products instead of classes, deployment-scoped parameters hitting distributable software.
- **FP fix pass:** all 14 flagged parameters narrowed (37 field edits): path exclusions in checks, class-based FP clauses, deployment scoping, first-party-vs-third-party claim split (CON-011), measurable-claims-only superlatives (CON-026), page-level genericness test (CON-006). Every FP case re-walked: none fires now; fabrication and real-secret cases remain blocker. `See also` lines untouched; counts intact (44/33/30/28/28/22/18 = 203).
- **Phase 1 exit state:** 203 validated parameters + calibration record (VIS file). The one open validation item — screenshot-based FP testing of 39 VIS parameters — is carried into Phase 6 explicitly.
