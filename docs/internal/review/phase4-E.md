# Phase 4 Cross-Review — Cluster E (D13, D14, D15)

Reviewer: Phase 4 cross-review, cluster E. Date: 2026-11-21.
Scope: substance review only (format validation already passed 227/227). No skill files were edited.

## Scope covered

**Deep-read (full SKILL.md + at least one example file opened) — 18 skills**

- D13: accessibility-audit, wcag, accessibility-law, keyboard-accessibility, rtl-layouts, screen-readers, reduced-motion, internationalization
- D14: privacy-laws, cookie-consent, licensing, dsar-handling, clone-ethics
- D15: dev-environment, dependency-management, refactoring, versioning, tech-debt

**Skimmed (Rules / BAN / Gates sections read in full) — 10 skills**

- D13: localization-workflow, inclusive-copy
- D14: data-residency, legal-documents, compliance-audit, age-requirements, audit-trails
- D15: monorepo-tooling, code-generation, legacy-migration

All 28 skills in the three departments were covered. Metadata `Depends on` / `Feeds into` references in every deep-read skill were checked against `build/catalog.txt`: every named skill exists.

## Findings

### BLOCKER

None.

### MAJOR

**M-1 — `Defeats:` DET citations are semantically wrong in a substantial minority of D13 BAN entries (cross-skill, D13; milder echoes in D14/D15).**
The cited DET IDs all *exist* (the parent's existence check passes), but the parameter they name frequently describes a different failure than the pattern being banned. A detection pass keyed to these fields would test for the wrong defect. Worst instances, verified against `skills/detection/ux/PARAMETERS.md` and `skills/detection/visual/PARAMETERS.md`:

- accessibility-audit **BAN-AC-001** (scan-only audit reported as conformance) cites DET-UX-018 — "Focus indicator removed or invisible."
- accessibility-audit **BAN-AC-003** (accessibility overlay offered as the fix) cites DET-UX-022 — "Placeholder text used as the only label." The same overlay pattern in wcag **BAN-AC-015** cites DET-UX-020 — "Interactive text and controls unreadable at real sizes." No DET parameter covers overlays, so two skills improvised two different wrong citations for one identical pattern.
- accessibility-audit **BAN-AC-005** (legal verdict in a technical report) cites DET-UX-020; the same pattern in accessibility-law **BAN-AC-031** cites DET-UX-006 — "Generic, coded, or blaming error messages." Again one pattern, two wrong citations.
- internationalization **BAN-AC-061** (hard-coded string) cites DET-UX-015 ("Same action, different behavior across screens"); **BAN-AC-062** (sentence by concatenation) cites DET-UX-006; **BAN-AC-063** (`count == 1` plural branching) cites DET-UX-020. None of the three parameters describes the banned i18n defect.
- screen-readers **BAN-AC-021** (clickable divs as controls) cites DET-UX-016 ("Keyboard trap") — a div control is unreachable, not a trap; rtl-layouts **BAN-AC-083** (un-isolated LTR run) cites DET-UX-020; reduced-motion **BAN-AC-053** (flashing above threshold) cites DET-VIS-041 ("Reduced motion ignored").
- By contrast, many citations are exact (wcag BAN-AC-011→UX-018, BAN-AC-012→UX-021, BAN-AC-013→UX-022, BAN-AC-014→UX-019; keyboard-accessibility BAN-AC-041/042/044/045; inclusive-copy's set), so the file set is inconsistent rather than uniformly loose.

*Suggested fix:* re-map each flagged BAN's `Defeats:` field to the semantically matching DET parameter where one exists; where none exists (overlays, bare legal verdicts, i18n mechanics), state "no DET parameter — pattern owned by this skill" instead of citing an unrelated ID. Apply the same pass to the D14/D15 instances in m-1/m-2 below while doing it.

### MINOR

**m-1 — D14: DET-FAKE-022 ("Progress and sync states that lie") is used as a catch-all for three unrelated patterns.**
cookie-consent BAN-LG-041 (pre-ticked toggles), dsar-handling BAN-LG-025 (silent deadline slip), and age-requirements BAN-LG-073 (`age_verified` set without verification) all cite DET-FAKE-022. Only the third is arguably a "state that lies." Also privacy-laws BAN-LG-004 (rights promised with no process behind them) cites DET-FAKE-015 ("Forms that submit nowhere") where DET-CON-028 ("Promises with no backing process") is the exact parameter, and dsar-handling BAN-LG-024 cites DET-FAKE-001 with a self-flagged "(inverted: …)" note — honest, but still a non-matching citation. Most other D14 citations are exact or adjacent-family (FAKE-011/015/019 in dsar-handling are exact; CON-017/CON-028 in licensing/legal-documents are apt).
*Fix:* remap BAN-LG-041 and BAN-LG-025 (or mark "no DET parameter"), point BAN-LG-004 at DET-CON-028.

**m-2 — D15: citation monotony and one cross-skill BAN duplication.**
All five dependency-management BANs cite the single parameter DET-CODE-028 ("Dependency manifest incoherence") — legitimate, since that parameter genuinely covers the cluster, but the mapping gives detection tooling no discrimination between five distinct patterns. Separately, the commented-out-code pattern is banned twice with near-identical text: refactoring BAN-DX-054 and tech-debt BAN-DX-042 (both → DET-CODE-010); and tech-debt BAN-DX-042's "Instead" cites DX-081 (the register rule) for a deletion rationale that belongs to DX-090/refactoring DX-112.
*Fix:* leave the rules as they are; in Phase 5 indexing, note the shared DET-CODE-028 mapping, and cross-reference the two commented-out-code BANs so a reader finds both from either skill. Correct the DX-081 citation in BAN-DX-042 to DX-090.

**m-3 — dev-environment example-2 embeds a realistic-looking credential string.**
`skills/developer-experience/dev-environment/examples/example-2.md` shows a "Before" `.env.example` containing a full `postgres://appuser:<password>@db.internal.example.com` URL. The host is a reserved example domain and the credential is plainly synthetic, but the string is realistic enough to trip secret scanners (including this repo's own G-DX-002-style greps if extended to URLs) and it models the exact artifact BAN-DX-001 bans.
*Fix:* replace the password segment with an obviously fake token (e.g. `<real-password-pasted-here>`) while keeping the example's teaching point.

**m-4 — clone-ethics metadata omits one consumer it names in prose.**
clone-ethics' "When to use" lists behavior-cloning among the D16 skills executing inside its gate, but its `Feeds into` lists only site-discovery, asset-harvesting, page-reconstruction, fidelity-verification.
*Fix:* add behavior-cloning to `Feeds into`.

## Department-specific checks required by the brief

- **D13 — WCAG version discipline: EXACT everywhere checked.** Build target is stated as WCAG 2.2 AA in wcag (AC-021), accessibility-audit (AC-001), and accessibility-law (AC-064). Law pins match D13.md §1.2 precisely: EAA via EN 301 549 V3.2.1 → WCAG 2.1 AA; Section 508 → WCAG 2.0 AA; ADA Title II rule → WCAG 2.1 AA (accessibility-law AC-062). The 4.1.1 Parsing nuance for 2.0-pinned engagements is handled correctly (AC-064: record how it was treated, never silently skip). No version errors found.
- **D14 — clone-ethics forcing function: INTACT and structural.** LG-181 requires the authorization record as a pre-committed, dated repo artifact that crawl tooling checks and fails closed without; LG-185 makes `licensed` impossible to self-approve (the manifest tooling itself rejects a `licensed` row whose approver is the harvesting actor, and requires attached license evidence); gates G-LG-091/092/093 automate the pre-flight check, the authorization-vs-first-crawl timestamp comparison, and manifest approval completeness. This is exactly the structural (non-self-attestation) design D14.md §4 demanded.
- **D14 — no jurisdiction overreach.** Age thresholds appear only as per-market configuration sourced from the research table (age-requirements LG-141/152 restate Article 8 / UK 13 / COPPA under-13 exactly as D14.md §1.5 gives them); DSAR clocks are computed from a regime table in the project file, never hardcoded (dsar-handling LG-043); privacy-laws LG-010 limits deep profiles to GDPR + CCPA/CPRA with everything else "register before serving"; escalation stops are hard stops (LG-011, compliance-audit LG-131, legal-documents LG-061 fails loudly on missing register inputs instead of drafting around them).
- **D15 — dependency-management ↔ D7 dependency-safety boundary: RESPECTED.** The skill's "Do NOT use" routes vulnerability response to D7 explicitly, DX-071 routes advisories to dependency-safety for triage while currency stays in D15, G-DX-032 blocks release "until D7 triages," and Metadata records "Feeds into: dependency-safety (D7 — receives routed advisories)." No parallel security process is created.
- **D15 — research open risks all addressed:** monorepo trigger condition (monorepo-tooling DX-021 + BAN-DX-015), generated-stub honesty (code-generation DX-049 + BAN-DX-023 + G-DX-025 stub honesty check), canonical debt-register location fixed at `docs/tech-debt.md` (tech-debt DX-081), versioning app-mode (versioning DX-152).

## Excellence worth propagating

- **clone-ethics (D14)** — the reference implementation for single-agent-safe approval: pre-committed artifacts + fail-closed tooling + timestamp comparison, rather than a second "approver" persona. Other departments with approval gates should copy this shape.
- **accessibility-law G-AC-033 (statement-vs-audit diff)** — mechanically diffs a published claim against the audit evidence, including a link-presence crawl. The same "public claim vs. evidence artifact" diff pattern is reused well in compliance-audit (LG-125) and data-residency (LG-027).
- **tech-debt's gates are genuinely single-agent runnable** — the marker-reference lint (G-DX-041) even carries the DET-CODE-011 exclusion for template fill-ins, the register-completeness awk check (G-DX-042), and the `comm`-based cross-reference/expiry check (G-DX-043) are exact commands with exact pass criteria.
- **versioning G-DX-072** (bump derived from Conventional Commits over the tag range and compared to the bump actually taken) turns "the number is a contract" into a mechanical check; DX-152's app-mode keeps it honest for deployed web apps.
- **dsar-handling G-LG-021** — the drill asserts both export completeness against known test records and zero post-erasure residue across DB, index, analytics, and admin views; "erasure is proven by absence" is the right standard, stated and gated.
- **rtl-layouts G-AC-084/G-AC-085** — per-script visual QA (Arabic passing does not certify Nastaliq) plus an icon flip-list conformance diff against the design-system list; both directly encode D13.md §1.4/§4 risks.

## Verdicts

- **D13 Accessibility & i18n — sound-with-fixes.** Substance, WCAG discipline, gates, and examples are strong throughout; the one systematic defect is the `Defeats:` citation layer (M-1), which needs a remapping pass before Phase 5 indexing consumes it.
- **D14 Legal & Privacy — sound-with-fixes.** The strongest department in the cluster: clone-ethics, dsar-handling, audit-trails (including the LG-170 trail-as-personal-data recursion), and legal-documents all match or exceed the research standard. Only minor citation cleanups (m-1, m-4).
- **D15 Developer Experience — sound.** Every research rule and every §4 open risk is addressed; gates are mechanical and single-agent runnable; the D7 boundary is explicit. The m-2/m-3 items are polish, not corrections.
