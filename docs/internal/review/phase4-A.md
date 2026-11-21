# Phase 4 Cross-Review — Cluster A (D1, D2, D3)

Reviewer: Phase 4 cross-review agent, cluster A. Date: 2026-11-21.
Scope of method: substance review against `docs/internal/research/D1.md`, `D2.md`, `D3.md`. Format validation was already passed (227/227) and was not re-run. No skill files were edited.

## Scope covered

**Deep-read** (full SKILL.md plus at least one example file opened and checked against its named rule):

- D1: fact-sheet (ex. 1), discovery (ex. 3), requirements-writing, acceptance-criteria, scope-control
- D2: system-design, api-architecture (ex. 1), api-versioning, multitenancy-saas, event-driven
- D3: design-tokens (ex. 2), frontend-core, ui-states, forms (ex. 2), typography

**Skimmed** (full SKILL.md text read; rules, BAN entries, gates, and metadata assessed; example files not opened):

- D1: user-research, personas-jtbd, user-stories, competitive-analysis, product-metrics, pricing-monetization, unit-economics, roadmapping
- D2: c4-diagrams, stack-selection, api-documentation, api-paradigms, data-architecture, architecture-patterns, domain-driven-design, adr-writing
- D3: design-system, component-library, motion, scroll-experiences, layout-responsive, frontend-state, data-fetching, client-routing, data-visualisation, pwa-offline, webgl-3d

**Mechanical check (all 42 skills):** every `Depends on` / `Feeds into` name in D1–D3 was extracted by script and resolved against the 227-name catalog. Result: **0 unresolved references.** All cited skill names exist.

## Findings

### MAJOR

**M-1 — fact-sheet: the price-mirror gate has no no-billing-provider fallback.**
PR-130 and gate G-PR-063 require diffing the sheet's prices against "the billing configuration export." On a project with no billing provider (brochure site, quoted pricing), that export does not exist and the gate cannot run at all — it fails silently or is skipped, which is precisely the failure D1.md §4 (open risk 6) warned about and asked drafters to pre-empt. The fallback does exist elsewhere in the department — pricing-monetization PR-210 makes the fact sheet itself the price source of truth and runs its gate G-PR-101 against the sheet — but fact-sheet never references it, and fact-sheet is the skill a builder reaches for first.
*Suggested fix:* add one sentence to G-PR-063 (and a note on PR-130): "Where no billing provider exists, the diff runs against the fact sheet's own price entries as the source of truth, per pricing-monetization PR-210."

### MINOR

**m-1 — scope-control: the ~60% Must cap has no recorded-override path.**
PR-144/PR-145 make exceeding ~60% Must effort a defect that forces re-triage. D1.md §4 (open risk 5) asked for heuristics to be encoded as defaults with a recorded override, as unit-economics PR-224 correctly does for LTV:CAC ("recorded as defaults with an explicit override note"). Scope-control offers no equivalent: a legitimately small, fixed-scope release that is honestly 70% Must has no compliant path except re-triage theater.
*Suggested fix:* add an override clause to PR-145 mirroring PR-224 — over-cap is permitted when the release records the override, its reason, and the accepted contingency risk.

**m-2 — competitive-analysis: G-PR-083's automated check does not verify what its Pass criterion claims.**
The check is `grep -ciE "decision|build:|skip:|position" analysis.md` returning ≥1, but the Pass text requires "decisions section present **with cell citations**." The grep cannot detect a citation. A document with the word "decision" once and no cell references passes the command while failing the stated criterion.
*Suggested fix:* either extend the check (e.g., require each decision line to match a cell-reference pattern) or narrow the Pass text to presence-only and move the citation requirement into the manual G-PR-084 audit.

**m-3 — user-stories: G-PR-041 overclaims what its lint can check.**
The gate is described as a regex over story text, but one of its checks — "the benefit clause must not repeat the capability text" — is a semantic-similarity judgment, not a regex (only an exact-string containment is). As written, an implementer will either skip the clause or build an unreviewable heuristic.
*Suggested fix:* split the check: regex verifies template shape and role; the benefit-repetition clause moves to the manual split review (G-PR-043) or is reworded to exact-duplicate detection.

**m-4 — system-design: G-AR-002's "automated" label-grep is format-dependent and unspecified.**
The gate's automated check includes "a companion grep fails if any relationship line in the diagram source lacks a protocol label." Whether a relationship line "lacks a label" is parseable depends entirely on the diagram syntax (Structurizr DSL vs. Mermaid vs. PlantUML), which the gate never names. This is the exact failure D2.md §4 (open risk 3) predicted: a gate that sounds automated but is not, as specified. The gate's other half (container section present; referenced ADRs exist) is genuinely automatable, and c4-diagrams G-AR-012 shows the defensible version of a label lint (exact generic names, empty labels).
*Suggested fix:* scope the grep to the project's chosen diagram syntax by name, or demote the label clause to the manual walk (G-AR-001) and keep G-AR-002 purely structural.

**m-5 — D2: two gates are duplicated across skills under different IDs, with no canonical owner.**
(a) The tenant-key schema check exists as both multitenancy-saas G-AR-092 and data-architecture G-AR-074 (rules AR-186 and AR-149 likewise duplicate the requirement). (b) The manifest-to-ADR coverage check exists as both stack-selection G-AR-021 and adr-writing G-AR-122. The duplicates currently agree, but nothing keeps them agreeing; a project can run both, get divergent results after a future edit, and not know which verdict governs. (Contrast: design-system G-FE-014 explicitly delegates to design-tokens' gates as its "enforcement arm" — the correct pattern.)
*Suggested fix:* designate one canonical gate per check (multitenancy-saas for tenant-key, adr-writing for manifest cross-check) and replace the other instance with a citation of it.

**m-6 — multitenancy-saas: gates do not state their cross-department execution dependency.**
D2.md §4 (open risk 4) recommended marking gates whose fixtures/execution belong to other departments ("specifies, executed by D8 with D5 fixtures"). G-AR-091 (cross-tenant suite) and G-AR-092 are written as if the skill's user runs them unaided; the suite in particular needs auth fixtures (D4/D5/D7 territory) and a test harness (D8). The gates are honestly specified — this is a missing ownership note, not an overclaim.
*Suggested fix:* add an execution note to G-AR-091/G-AR-092 naming the executing department and fixture owners.

**m-7 — All three departments: circular `Depends on` / `Feeds into` pairs, with the semantics never defined.**
Instances: fact-sheet ⇄ competitive-analysis (mutual `Depends on`); fact-sheet ⇄ pricing-monetization (pricing both depends on and feeds into fact-sheet); api-versioning ⇄ api-documentation; stack-selection ⇄ system-design; frontend-core ⇄ ui-states; plus a 3-cycle frontend-state → client-routing → data-fetching → frontend-state. All names resolve (see mechanical check), and the relationships are substantively real — these skills genuinely co-evolve. The defect is that neither the template nor any skill defines whether `Depends on` means "reads inputs from" (cycles fine) or "must be executed/read first" (cycles break any topological bootstrap order a single agent might derive from the metadata).
*Suggested fix:* one template-level definition — `Depends on` = consumes inputs from; `Feeds into` = outputs consumed by; cycles permitted for co-evolving pairs — or prune the redundant back-edges. Do not fix per-skill; fix the convention once.

**m-8 — client-routing: BAN-FE-114 cites the wrong DET parameter for its failure.**
BAN-FE-114 (router guard as the authorization boundary) cites DET-VIS-032 (missing/fake UI states). frontend-state's BAN-FE-093 covers the same underlying failure — a client-side flag standing in for server authorization — and cites DET-FAKE-002. The two D3 skills should point at the same parameter for the same failure class; DET-FAKE-002 is the precise one.
*Suggested fix:* change BAN-FE-114's citation to DET-FAKE-002 (keeping DET-VIS-032 as a "see also" if desired).

**m-9 — frontend-core: FE-005 restates the thresholds it says are not restated.**
FE-005 gives the Core Web Vitals numbers inline (LCP ≤ 2.5s, INP ≤ 200ms, CLS ≤ 0.1) and in the same breath says thresholds are "cited from the numbers registry in `gates/`, per WCPM Appendix F — not restated per project." If the registry value ever changes, this rule text becomes a second, contradictory source — the drift the single-sourcing rule exists to prevent.
*Suggested fix:* drop the inline numbers from FE-005 (keep them in the gate G-FE-001 only if the registry is cited there too), or mark the inline figures "as of last verified" so the registry visibly wins.

## What is excellent — propagate these patterns

1. **Degradation paths for missing humans are encoded, consistently, across departments.** D1.md and D2.md both flagged "the method assumes real customers / domain experts the single agent may not have" as their top structural risk. The drafters answered it: discovery PR-010 (user-supplied material only; anything inferred is UNVERIFIED with no downstream citation rights), user-research PR-030, personas-jtbd PR-048 (HYPOTHETICAL label, no citation rights), domain-driven-design AR-229 (inferred glossary terms marked UNVERIFIED). This four-skill chain is the strongest substance decision in the cluster and should be the template for any future evidence-dependent skill.
2. **Every fragile automated gate carries a named manual fallback.** acceptance-criteria PR-109/G-PR-054 (signed checklist where no BDD runner exists), pricing-monetization PR-210 (fact sheet as truth where no billing provider exists), api-architecture G-AR-031, api-versioning G-AR-041, c4-diagrams G-AR-011 (documented manual walk where the sandbox cannot run the tool). This is exactly the mitigation D2.md §4 risk 2 demanded — and it is what makes finding M-1 stand out: fact-sheet is the one gate that missed the pattern.
3. **The D2 house-style conflict was resolved by pre-decision, not by luck.** D2.md §4 risk 1 warned that api-architecture / api-versioning / api-documentation drafted independently would contradict each other (Zalando snake_case vs. Google camelCase). All three skills instead carry the same explicit house-profile block (Zalando-based: snake_case, sub-resource actions, Problem Details, cursor pagination, path-segment version, Deprecation/Sunset headers), and api-versioning cleanly separates style (Zalando) from the compatibility classification (Google's enumerated list). No contradiction found anywhere in the trio.
4. **Examples do real work.** design-tokens example-2 computes actual contrast ratios (≈2.2:1 fail → ≈5.4:1 pass) rather than asserting "improved contrast"; forms example-2 is complete, runnable code whose Before version names the exact BAN entries it commits; fact-sheet example-1 lets the verified numbers shrink ("The published numbers are smaller. They are also true") — the department's whole thesis in one example.
5. **D3 single-sources its inherited law.** The "inherited law" rules (typography FE-151, ui-states FE-171, frontend-state FE-190, data-fetching FE-211, layout-responsive FE-132) cite WCPM families through `docs/WCPM_MAPPING.md` instead of restating them, per DECISIONS D-013 — so a future WCPM correction lands in one place.

## Verdicts

- **D1 Product & Requirements — sound-with-fixes.** One MAJOR (M-1, a one-sentence fix) and three MINORs (m-1, m-2, m-3). The department's research risks were otherwise answered inside the skills themselves.
- **D2 Architecture & System Design — sound-with-fixes.** No MAJORs. Four MINORs (m-4, m-5, m-6, plus its share of m-7). The house-profile pre-decision eliminated the department's biggest predicted failure before drafting began.
- **D3 Frontend, Design & Motion — sound-with-fixes.** No MAJORs. Two MINORs of its own (m-8, m-9) plus its share of m-7. Boundaries between overlapping skills (component-library vs. ui-states state matrices; frontend-state vs. data-fetching server-state split) are stated explicitly on both sides and do not contradict.

Cluster totals: **0 blockers, 1 major, 9 minors** (m-7 counted once as a cross-department finding). Nothing in cluster A needs a redraft; every finding is a clause-level fix.
