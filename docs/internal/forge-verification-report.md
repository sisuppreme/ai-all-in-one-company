# Forge Verification Report — Phase 5 (D8 QA verification pass)

Verifier: Phase 5 Forge verification agent (D8 role — independent of the Forge builders).
Date: 2026-11-21. Repo: `ai-all-in-one`, branch `main`.
Method: independent measurement and inspection only; no deliverable was edited. Token measure throughout: **tokens = ceil(characters ÷ 4)**, the repo definition recorded in `docs/METRICS.md`.
Defect classes per `gates/DEFECT_TAXONOMY.md` (QB-01): **P0** = security / data loss / crash; **P1** = broken feature or gate failure; **P2** = cosmetic / copy.

## Verdict summary

| # | Check | Verdict |
|---|---|---|
| 1 | Bundle caps | **PASS** |
| 2 | Bundle ID integrity | **PASS** |
| 3 | Index integrity | **FAIL** — 19 entries lack the brief-required standalone justification (defect F-01) |
| 4 | BAN vs anti-pattern duplication (§5.4) | **FAIL** — 2 confirmed duplicate pairs (defects F-02, F-03) |
| 5 | Playbook completeness (§5.6) | **PASS** |
| 6 | Gates registry | **PASS** |
| 7 | Custom instructions (§5.5) | **PASS** |
| 8 | BOOTSTRAP findability dry-run | **PASS** — 9/10, at the §5.3 bar (one routing ambiguity, defect F-04) |
| 9 | Linkage (mirror check + contracts) | **PASS** |

**Totals: 7/9 checks PASS. Defects: P0 = 0, P1 = 1, P2 = 3.**

---

## Check 1 — Bundle caps: PASS

All 33 files in `bundles/` measured independently:

- `core.md`: **9,554 tokens** vs cap < 10,000 — PASS.
- Every other bundle ≤ 30,000 — PASS. Largest: `devops-deployment.md` 29,861; `security.md` 29,662; `seo-content.md` 29,417; `two-sided-marketplace.md` 29,048. Smallest capped bundle: `online-learning-lms.md` 5,912.
- `ALL_SKILLS.md`: 584,918 tokens, uncapped by design; its header carries the required line **"DO NOT LOAD WHOLE — use bundles/ or SKILLS_INDEX.md."** — confirmed present.

No failures.

## Check 2 — Bundle ID integrity: PASS

For each of the 18 departments, the rule, gate, and BAN ID sets in the department bundle(s) were compared against the sets defined in the source `SKILL.md` files, and the `<!-- generated from skills/<dept>/<skill>/SKILL.md … -->` provenance comments were matched path-for-path against the department's skill folders:

- All 18 departments: **0 missing rule IDs, 0 missing gate IDs, 0 missing BAN IDs**.
- Provenance: exact set equality in all 18 departments (e.g. database 20/20, devops-deployment 17/17, cloning-replication 7/7); total 227 skills, 0 duplicates, 0 extras.

## Check 3 — Index integrity: FAIL (defect F-01)

`SKILLS_INDEX.md` was parsed into its 227 entries:

- Entry count: **227** ✓. Every entry's Path resolves to a file on disk: **227/227** ✓.
- Gates field non-empty (real `G-<CODE>-NNN` IDs) in **227/227** ✓.
- Anatomy element present in **227/227** ✓.
- **Depends on: 19 entries read `Depends on: none` with no standalone justification in the index entry.** The index faithfully reproduces the source skills' own metadata (spot-checked: discovery, ci-cd, project-templates, owasp all declare `Depends on: none` in their SKILL.md), so this is not a generator error. But the brief (§3.10 item 6, applied to the §5.3 index) requires an unlinked skill to either gain links or record a one-line justification ("standalone: no cross-department input or output") in its index entry, and states that an unjustified unlinked skill does not ship. "none" alone is not that justification.

  The 19 entries: discovery, adr-writing, design-tokens, ci-cd, infrastructure-as-code, dependency-safety, owasp, session-security, technical-seo, changelog, documentation-writing, project-templates, logging, monitoring, licensing, dev-environment, refactoring, tech-debt, support-ticketing.

  Note: most of these are genuinely foundational skills with real *Feeds into* lists (e.g. project-templates feeds readme-writing, documentation-writing, progress-tracking, handover), so a truthful one-line standalone justification exists for each — the fix is recording it, in the skills' metadata (so regeneration carries it) or as an index-generation rule for `none` entries.

## Check 4 — BAN vs anti-pattern duplication (§5.4): FAIL (defects F-02, F-03)

Method: automated screen of all 227 skills comparing normalized BAN pattern names against anti-pattern names (token-overlap ≥ 0.6), then manual adjudication of every candidate against the §5.4 rule ("an item appears in exactly one of BAN list / Anti-patterns, never both"). 4 candidates; 2 confirmed, 2 rejected:

- **CONFIRMED — `skills/frontend/motion`:** BAN-FE-042 "Reduced motion ignored" (shipping animation with no `prefers-reduced-motion` handling) and the anti-pattern "The reduced-motion retrofit" (reduced-motion handling planned for later, i.e. not shipped with the animation) are the same failure mode in both lists; the anti-pattern's own catch test is the BAN's requirement (reduce block in the same commit, FE-085).
- **CONFIRMED — `skills/frontend/webgl-3d`:** BAN-FE-152 "The engine-default scene" (one white ambient light, one stock material, default centered camera) and the anti-pattern "Library by default, scene by tutorial" (a stock Three.js example with the demo object swapped) describe the same defect; the anti-pattern text itself says the G-FE-152 gate "exists to catch exactly this."
- **Rejected — `skills/developer-experience/code-generation`:** BAN-DX-021 "The hand-edited generated file" (editing generated output in place) and BAN-DX-022 "The unmarked generated file" (no generated-file header) vs anti-pattern "The almost-generated file" (a generated file copied elsewhere and hand-maintained as a fork). Related family, three distinct failure modes — no duplication.

In both confirmed cases the two entries give *consistent* guidance (no contradiction); the defect is the §5.4 list-exclusivity violation. Fix: merge each pair into the BAN entry (the anti-pattern's "catch it" line can survive as the BAN's detection note) or re-scope the anti-pattern to a genuinely different failure mode.

## Check 5 — Playbook completeness (§5.6): PASS

All 13 playbooks in `playbooks/` contain every required element: goal; departments + order; skills to load with bundle names; docs to write first; a step-by-step sequence with explicit decision points (◆ DECISION markers and §6.3 "stop and ask" points in every playbook); gates cited by real IDs (29–55 distinct gate IDs per playbook, every one verified to exist in a skill); failure handling; definition of done; and a worked mini-example.

Cross-cutting rules verified:

- **D13 step:** present in the build step of every UI playbook (all except api-database-service, which is non-UI and still references accessibility where relevant).
- **D12 + D14 steps:** explicit numbered steps in all 12 playbooks where the brief requires them — and also present in landing-page.md, which the brief exempts (inclusion is not a violation).
- **D17 / D18 conditional steps:** present where relevant (e.g. online-learning-lms step 7 = D18 learner experience; realtime-chat-app step 6 = D18; content-blog-site step 4b = D17 conditional).
- **D6 last build step:** the Deploy (D6) step is the final build step in all 13 playbooks; the only later step, where present, is the brief-mandated D9 launch/finish step. Clone-rebuild additionally enforces the authorization record (D14 clone-ethics gates G-LG-091/G-LG-092) before any crawl, at step 1.

## Check 6 — Gates registry: PASS

- `gates/ACCEPTANCE_GATES.md`: exactly **69** register gate IDs, by family — DES 6 (01–06), MOT 10 (01–10), VIS 9 (01–09), SCH 11 (01–11), ENG 14 (01–14), EXP 11 (01–11), INT 8 (01–08). No extras, no gaps.
- `gates/QA_PROTOCOL_GATES.md`: contains **G-QA-01…G-QA-10**, complete. The three register IDs appearing in the file (G-DES-01, G-ENG-01, G-EXP-05) are *citations*, not merges: the header states G-QA-06 mirrors G-EXP-05 and G-QA-08 mirrors G-ENG-01, and G-QA-03 "cites G-DES-01, so the bar exists in exactly one place" per the mapping's Drop 5 ruling. The QA protocol keeps its own 10 gates.
- `gates/VISUAL_QA_INDEX.md`: covers **VQ-0 through VQ-12**, complete.
- `gates/FINAL_ACCEPTANCE_CHECKLIST.md`: items A-01…A-15 and CR-09…CR-12, each citing its gate(s) ("Verifies: G-…") instead of restating criteria, per the Drop 3 ruling. Spot-check of 5 items (A-01, A-04, A-07, A-10, CR-09): all cite gate IDs; the three items with no register gate (A-08, CR-12, A-15) say so explicitly and name the enforcing mechanism rather than inventing a gate.

## Check 7 — Custom instructions (§5.5): PASS

All four instruction files in `custom-instructions/` (`ai-studio.md`, `claude-code.md`, `claude.md`, `generic.md`) contain all six required contents: (1) the repo URL placeholder `https://github.com/sisuppreme/ai-all-in-one-company`; (2) the repo-first sequence (BOOTSTRAP.md → SKILLS_INDEX.md scan → load skills → docs before code); (3) the fallback (ask the user to paste `bundles/core.md`, proceed with core only, flag the gap in `progress.md`); (4) the single-agent rule; (5) the Real Content Rule in one line; (6) the version pin **v1.0.0 / 2026-11-21**. Gate results recorded in `progress.md` are also instructed in all four. No file promises the agent "behaves correctly from then on."

## Check 8 — BOOTSTRAP findability dry-run: PASS (9/10)

Method: using only `BOOTSTRAP.md`'s routing rule and `SKILLS_INDEX.md` (department sections + Keywords + Use-when lines) — no SKILL.md files opened for the choice — one first-choice skill was committed per task, then scored against the skills' own Use-when lines as reproduced in the index. (The formal fresh-agent test is Phase 6; this is the Forge dry-run.)

| # | Task | Dept | First choice | Verdict |
|---|---|---|---|---|
| T1 | Add Stripe subscriptions with a free trial to a SaaS | D11 | `subscriptions` — Use-when opens "a product sells recurring access — trials, renewals, plan changes…" | ✓ |
| T2 | Make a blog pass WCAG 2.2 AA | D13 | `accessibility-audit` — "an evidence-producing evaluation against WCAG 2.2 AA — before launch… or after remediation" | ✓ |
| T3 | Rebuild a competitor's public pricing page legally | D14/D16 | `clone-ethics` — "any work would crawl, inventory, harvest from, or replicate an existing site — before the first request is made" (authorization precedes discovery in the clone playbook) | ✓ |
| T4 | Stop secrets leaking into the git repo | D7 | `secrets-management` — "…or a leak is suspected. This skill owns where secrets live…" | ✓ |
| T5 | Add full-text search to a Postgres product catalog | D5 | `search-engines` — "choosing between PostgreSQL full-text search and a dedicated engine…" | ✓ |
| T6 | Set up CI/CD with preview environments | D6 | `ci-cd` — "the automated pipeline that builds, tests, publishes, and deploys" (preview-environments loads with it) | ✓ |
| T7 | Add scroll-triggered animations to a landing page | D3 | `scroll-experiences` — "anything tied to scroll position — reveal choreography, parallax…" | ✓ |
| T8 | Track why users drop off in onboarding | D12/D18 | `product-analytics` — routed via the analytics department; defensible ("instrumenting flows", tracking plan) **but** the most precise Use-when match is D18 `activation-metrics` ("auditing an activation dashboard or funnel report") | ✗ |
| T9 | Get product pages cited by AI search engines | D9 | `geo` — "inclusion and citation inside synthesized answers (ChatGPT, Perplexity, Copilot…)" | ✓ |
| T10 | Add a support chatbot grounded in our help-center docs | D17 | `rag-retrieval` — "a feature answers questions… from a document corpus the project owns — help-center assistants, document Q&A…" | ✓ |

**Score: 9/10** — at the §5.3 findability bar (9/10 correct first choices, 10 tasks spanning 10 departments). The single miss is a routing ambiguity, not a wrong-skill error: for the "drop-off in onboarding" phrasing, the index offers no tie-breaker between D12 product-analytics and D18 activation-metrics, and in practice both load together via the Load-with graph. Recorded as defect F-04 for an index keyword/cross-reference improvement.

## Check 9 — Linkage: PASS

- `docs/DEPARTMENT_LINKS.md` states its mirror-check result verbatim: **"mirror check: PASS, 0 unmatched links"** (final run: 262 (pair, type) keys, 280 directed claims, all mirrored; no CONSTRAINS or VERIFIES link bidirectional). The file also documents the check's first run, which found 4 unmatched links (brief omissions, recorded as correction C8) that were fixed in the partner rows and re-run clean.
- Contracts vs backbone: the matrix names **13 backbone links**; `docs/contracts/` holds **14 files**. The difference is explained in the file itself (Section 4): backbone link 2 (D2 → D4/D5) is realized as two contracts, one per consuming department (`d2-d4.md`, `d2-d5.md`). Counts therefore match: **13 links ↔ 14 contract files, reason recorded**.

---

## Defect list

| ID | Class | Location | Defect | Evidence |
|---|---|---|---|---|
| F-01 | **P1** | `SKILLS_INDEX.md` (+ source SKILL.md metadata) | 19 entries carry `Depends on: none` without the one-line standalone justification the brief (§3.10 item 6 / §5.3) makes a ship condition for unlinked skills. The index is otherwise complete (227/227 paths, gates, anatomy). Graded P1 because the brief's rule is an explicit ship condition on a primary deliverable ("an unjustified unlinked skill does not ship"); it does not impair findability (check 8 passed at the bar). | Check 3: discovery, adr-writing, design-tokens, ci-cd, infrastructure-as-code, dependency-safety, owasp, session-security, technical-seo, changelog, documentation-writing, project-templates, logging, monitoring, licensing, dev-environment, refactoring, tech-debt, support-ticketing. Fix in the skills' metadata so regeneration carries it. |
| F-02 | **P2** | `skills/frontend/motion/SKILL.md` | Same failure mode in both lists, violating §5.4 exclusivity: BAN-FE-042 "Reduced motion ignored" ↔ anti-pattern "The reduced-motion retrofit". Guidance is consistent; no gate fails. | Check 4 (manual adjudication of the automated screen's candidates). |
| F-03 | **P2** | `skills/frontend/webgl-3d/SKILL.md` | Same failure mode in both lists: BAN-FE-152 "The engine-default scene" ↔ anti-pattern "Library by default, scene by tutorial" (the anti-pattern text itself names the BAN's gate as the catch). Guidance is consistent. | Check 4. |
| F-04 | **P2** | `SKILLS_INDEX.md` (Keywords / cross-references) | Findability ambiguity: the task phrasing "track why users drop off in onboarding" routes by department to D12 `product-analytics`, while the most precise Use-when owner is D18 `activation-metrics`. No keyword or Load-with signal in the index breaks the tie. | Check 8, task T8 (the dry-run's only miss; score still at the 9/10 bar). Suggested fix: add drop-off / onboarding-funnel keywords to activation-metrics' index entry or a cross-reference from product-analytics. |

**Class totals: P0 = 0, P1 = 1, P2 = 3.** No defect blocks the Phase 5 assembly itself; F-01 must be fixed (or formally dispositioned) before the §9.1 ship gate, and F-02/F-03/F-04 are log-and-fix items.

## Notes on method (for the record)

- Check 4's automated screen produced 4 candidates; 2 were rejected on manual reading (code-generation's three generated-file items are distinct failure modes). A purely mechanical pass would have over-reported.
- Check 1 sizes were measured from the files on disk, not from `scripts/build-bundles.py` output; check 2's ID sets were extracted independently from both bundles and source skills.
- The verifier did not re-run Phase 4's substance review; skills' content quality was verified in Phase 4 and is out of scope here except where a Phase 5 rule (§5.4 list exclusivity) applies.
