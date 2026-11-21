# RESEARCH_PAPER.md — The OmniForge research paper

Purpose: the public-facing research record of this build (§5.1, §6.1) — method, evidence, and findings, written to be readable standalone. Audience: anyone evaluating whether this repository's claims are earned. The build's internal record is `docs/WORK_LOG.md` and `docs/work-log/`; every number below is defined in `docs/METRICS.md`.

**Date:** 2026-11-21. **Status:** Final for repo v1.0.0. **Companion paper:** `docs/WEB_CRAFT_PAPER.md` — the inherited Web Craft Pro Max research paper ("Why Websites Look AI-Generated — and How to Stop Building Them That Way"), shipped in this repository with corrected figures and an editor's note. This paper *references* that one; it does not reproduce it. Where the two disagree, this paper's verification record governs, and the disagreement is stated.

---

## Abstract

This repository — a 227-skill operating system for a single AI agent building web applications — was built under one research discipline: **no claim ships without a source, and no inherited claim ships without re-verification.** Seven research strands produced its evidence base. (1) The inherited Web Craft Pro Max material was script-verified against the received files: 200 BAN entries, 198 rule IDs, and a 69-gate acceptance register all confirmed exactly as the brief claimed — and the source file's own internal count of "68 gates" was found to be a stale error and recorded, not copied. (2) The inherited calibration claims were re-verified: the widely repeated "~55.5% human accuracy at detecting AI websites" figure proved **untraceable** to any peer-reviewed, website-specific study, while its ballpark — human detection barely above chance — is supported by peer-reviewed evidence; the companion claim that detector vendors overstate accuracy by 15–30 points against independent benchmarks was **confirmed** for text detectors with named claim-vs-measured pairs. (3) A fresh detection-research phase built 203 detection parameters in 7 families, each carrying signal, AI-typical form, professional form, a mechanical check, false-positive conditions, severity, source, and the skill that fixes it. (4) Eighteen department research files grounded all 227 catalog skills in current professional standards before any skill was drafted. (5) The parameters were false-positive-tested against known-good production sites — first from fetched text (16 confirmed false positives across two passes, all narrowed), then, in Phase 6, from rendered screenshots and computed styles, which closed the 39 visual parameters the text pass could not test (4 fired, all narrowed, re-walk 6/6 clear). (6) A formal findability test scored 10/10 correct first skill choices against a 9/10 bar. (7) Four proof projects and eight playbook dry runs, all executed by fresh agents using only this repository, produced working software and 60+ repo defects — every one fixed in the owning department without weakening any gate's pass criterion. The central finding is methodological: an AI-built knowledge base earns trust the same way the software it produces does — by mechanical verification, adversarial testing against known-good targets, and honest null markers where coverage does not exist.

---

## 1. Method

### 1.1 Evidence rules

Three rules governed every strand, and are stated here because the findings cannot be judged without them:

- **Fact-sheet protocol.** No factual claim enters the repository without a source. A claim that cannot be sourced is either cut or marked UNVERIFIED in place — never smoothed over (see `docs/EVIDENCE_BASE.md`, seed entry E-004, for the brief-vs-file drift that motivated this).
- **Inherited claims are re-verified, not trusted.** Summaries of a source — including this project's own Master Brief — are treated as claims *about* the source, checked against the source itself by script wherever the claim is countable.
- **Counts are floors, and drops are decisions.** The brief's catalog (227 skills, §3.12) and its headcount (477 roles, §3.8) are minimums. Research may add; it may not silently remove. Every removal carries a named reason in `docs/WCPM_MAPPING.md` or `docs/DECISIONS.md`.

### 1.2 Strands

| # | Strand | Phase | Primary record |
|---|---|---|---|
| 1 | Inheritance verification (Web Craft Pro Max) | 0–2 | `docs/WCPM_MAPPING.md`, `docs/METRICS.md` |
| 2 | Calibration re-verification (§2 claims) | 1 | Calibration section, `skills/detection/visual/PARAMETERS.md` |
| 3 | Detection parameter build (7 X-squads) | 1 | `skills/detection/<family>/PARAMETERS.md` |
| 4 | Department research (18 departments, 4 waves) | 2 | `docs/internal/research/D1.md` … `D18.md` |
| 5 | False-positive testing (text, then rendered) | 1 + 6 | `docs/work-log/phase-1.md`, `docs/work-log/phase-6.md` |
| 6 | Findability testing (§5.3 protocol) | 5 + 6 | `docs/internal/forge-verification-report.md`, `docs/internal/findability-test-phase6.md` |
| 7 | Proof projects + playbook dry runs | 6 | `docs/work-log/phase-6.md`; per-proof `PROOF_REPORT.md` files in the proof workspaces |

### 1.3 Verification instruments

Countable claims were checked by script, not by reading: Python regex extraction over full file texts for ID counts; `scripts/validate-skills.py` for skill format, ID-block membership, and repo-wide ID uniqueness; set-equality checks between bundle contents and source skills for ID integrity; and grep-based citation-existence checks (every DET ID cited by any skill was verified to exist — 185 distinct IDs cited, 0 dangling). Subjective review was layered on top of, never substituted for, these mechanical checks (Phase 4: six independent reviewers deep-read 94 of 227 skills against the Phase 2 research files).

---

## 2. Findings

### 2.1 Strand 1 — The inheritance mostly checks out; its own summary of itself does not

The build inherited the Web Craft Pro Max project: a 4,015-line `SKILL.md` and a 711-line research paper (both line counts script-verified on receipt). The Master Brief's summary of that inheritance made four countable claims. Verification results (`docs/WCPM_MAPPING.md` §1–2; `docs/METRICS.md`, "Inheritance verification"):

| Brief's claim | Verdict | Evidence |
|---|---|---|
| 200 BAN entries | **Confirmed** | 200 unique `BAN-NN` IDs (01–200) by regex extraction |
| 198 rule IDs | **Confirmed** | 198 unique `R-<section>-<n>` IDs |
| 69 acceptance gates | **Confirmed, with a reconciliation** | The §12.3 acceptance-gate register holds exactly 69 (DES 6, MOT 10, VIS 9, SCH 11, ENG 14, EXP 11, INT 8). The file's *total* gate-ID count is 79; the extra 10 (G-QA-01…10) are a §12.5 skill-release QA layer, inherited separately and never merged into the 69 |
| Paper figures (parameters / families / tells) | **Corrected** | The received paper printed superseded figures (170 / 16 / 213). The corrected figures — 178 parameters, 17 families, 221 tells — were applied as 26 figure replacements in `docs/WEB_CRAFT_PAPER.md`, with an editor's note; protected strings (file lengths, DOI, citations) verified untouched |

Two defects were found *inside the source itself* and recorded rather than propagated: the source's §12 text instructs "All **68** acceptance gates run" — 68 matches neither its register (69) nor its total (79), a stale internal count; and its Appendix B.1 mislabels §12.3 as the definition site for the whole `G-` namespace. The mapping also records **6 drops** from the inheritance, each named with a reason (among them: the install preamble, superseded by this repo's bundle system; and the S1–S3 scenario fixtures, replaced by the Phase 6 proof projects P1–P4). No item was dropped silently. Inherited IDs are cited verbatim in their home skills (DECISIONS D-013) so any ID in the inherited paper traces to exactly one home in this repository.

**Finding:** the inherited research was substantially accurate where it counted — but only script verification against the artifact, not the brief's summary of it, could establish that. The one number a reader would most likely have repeated (the gate count) exists in three versions (68 / 69 / 79) inside a single handoff, and each version is correct or incorrect only relative to a stated definition.

### 2.2 Strand 2 — Calibration: one claim untraceable, one confirmed

Phase 1 re-verified the two calibration claims the inherited paper rests on (full record: Calibration section, `skills/detection/visual/PARAMETERS.md`).

**Claim 1 — "Humans detect AI-generated websites at ~55.5% accuracy." Verdict: PARTIALLY SUPPORTED; the exact figure is untraceable.** No peer-reviewed study reporting 55.5% for AI-generated *websites* could be found. The nearest website-specific evidence is a commercial Sortlist survey (500 business owners judging five sites), not a peer-reviewed study. Peer-reviewed work on AI media generally lands near chance: Cooke et al., "As Good as a Coin Toss" (*Communications of the ACM*), measured 51.2% overall accuracy across 1,276 participants, with images worst at 49.4%; a preregistered three-country study (n=3,002) found image detection below 50% and no modality above 60%. The claim's ballpark — humans are barely better than chance, low-to-mid 50s — is consistent with this evidence; the precise "55.5%" and its restriction to websites are not. **This repository therefore cites the ballpark with its sources and never cites the bare 55.5% figure as a measured fact.** (The inherited paper's own §1 reports a pooled 55.54% across 56 studies; the Phase 1 verdict stands as the repository's position, and the editor's note in `docs/WEB_CRAFT_PAPER.md` records it.)

**Claim 2 — "Detector vendor claims run 15–30 points above independent benchmarks." Verdict: CONFIRMED for text detectors.** Named pairs: Copyleaks advertises 99.12% accuracy while a 12-tool benchmark measured 66%; GPTZero claims 99% while the same benchmark measured 52% overall. A second comparison puts the claimed-vs-measured gap at 15–23 points and cites the peer-reviewed RAID benchmark (ACL 2024) as the reference standard. Independent peer-reviewed support: Liang et al. (*Patterns*, 2023) found seven GPT detectors falsely flagged an average of 61.3% of non-native English essays as AI-generated — far from vendors' near-zero false-positive claims. **Caveat, recorded in the source file:** these benchmarks measure *text* detectors; the gap is confirmed there and plausible, but not independently established, for website/visual detectors.

**Calibration consequence adopted by the detection squads:** human gut feeling is a near-chance instrument, so the visual squad never reports "looks AI" — it reports measured parameter hits; and no detector tool's score is ever quoted in this repository without an independent benchmark beside it.

### 2.3 Strand 3 — 203 detection parameters, built detection-first

Per the brief's ordering rule (detection research before department research), seven squads built the parameter set first; every department skill drafted later cites these parameters as its traceability target. Each parameter carries: Signal / AI-typical form / Professional form / Check / False positives / Severity / Source / Fix (the skill that cures it).

| Family | Parameters | Floor | File |
|---|---|---|---|
| VIS — visual | 44 | 40 | `skills/detection/visual/PARAMETERS.md` |
| CODE — code | 33 | 30 | `skills/detection/code/PARAMETERS.md` |
| INF — infrastructure | 30 | 25 | `skills/detection/infra/PARAMETERS.md` |
| CON — content | 28 | 25 | `skills/detection/content/PARAMETERS.md` |
| UX — user experience | 28 | 25 | `skills/detection/ux/PARAMETERS.md` |
| FAKE — fabricated content | 22 | 20 | `skills/detection/fake/PARAMETERS.md` |
| CRWL — evidence pipeline | 18 | 15 | `skills/detection/crawl/PARAMETERS.md` |
| **Total** | **203** | 180 | |

A cross-family consistency audit then checked ID integrity, format integrity, Fix-field integrity (46 distinct Fix names, all real catalog skills), and source honesty — all PASS. It found one true duplicate (DET-UX-003 ↔ DET-FAKE-015) and 13 overlap clusters; rather than deleting coverage, the audit kept both parameters with a stated division of ownership (UX owns the user-facing symptom; FAKE owns the verdict via the persistence/network test) and added 70 `See also` cross-references across 39 parameters. Two severity inconsistencies were resolved by a tell-vs-verdict rule: visual *tells* keep their (lower) ratings; the content family's *fabrication verdict* stays **blocker**; each side cross-references the other. No parameter was deleted or renumbered at any point in the build.

### 2.4 Strand 4 — Department research: 227 skills grounded before drafting

Phase 2 produced one research file per department (`docs/internal/research/D1.md` … `D18.md`) in four waves (44 + 79 + 53 + 51 skills), each file recording the department's current professional standards, failure modes, per-skill research notes, candidate gates, and verified sources. Exit state: 18/18 files, 227/227 catalog skills with research notes. Findings that materially shaped the drafted skills include:

- **Conflicting authorities must be pre-decided, not averaged.** D2's API skills faced a genuine Zalando-vs-Google house-style conflict; the research file records a single recommended house style for Phase 3 to apply (D2.md). D10's DECISIONS.md-vs-`docs/adr/` duality was likewise resolved inside the skills (D-006: ADRs as the record set, DECISIONS.md as the human index).
- **Single-operator reality changes the standard.** Several professional standards assume teams. The research surfaced where that assumption breaks — D6 incident roles, D14 clone-ethics approval, D7's audit-vs-penetration-test authorization line (owner-controlled systems only, written engagement) — and Phase 3/4 encoded explicit single-operator modes rather than leaving unpassable requirements (see §2.7 and the Phase 4 majors in `docs/work-log/phase-4.md`).
- **Boundaries are research output.** Cross-department splits were agreed in the research files themselves: D6 owns infrastructure/platform/on-call while D12 owns product/application signals and SLO policy; D17 skills are provider-neutral with provider specifics confined to dated annexes and no prices; D18 support promises are operator-set configuration values, with the dark-pattern line grounded in FTC sources (the Click-to-Cancel rule was vacated in July 2025 and is not cited); D13 builds to WCAG 2.2 AA while noting law-pinned older versions; D9 treats AEO/GEO claims on an evidence ladder (e.g., llms.txt is a 2024 proposal Google rejected on the record); D11 keeps OAuth per RFC 9700 and notes OAuth 2.1 is still a draft, and keeps invoicing-tax to patterns only.
- **The seed-data line (D5):** synthetic, labeled, dev-only — a rule the Phase 4 review later enforced when a realistic-looking credential string in an example was replaced with an obviously fake token.

### 2.5 Strand 5 — False-positive testing: the parameters against known-good sites

A detection parameter that fires on professional work is a defect in the parameter, not in the site. The parameters were therefore tested against known-good production targets, in two media:

**Text pass (Phase 1).** Visual/content parameters were walked against stripe.com, linear.app, and basecamp.com from fetched text: **9 false positives in 5 parameters** (DET-CON-006, DET-CON-011, DET-CON-026, DET-VIS-003, DET-VIS-035) — all breadth problems: unsourced-on-page first-party statistics and ordinary marketing puffery flagged at blocker/major severity. The fabrication core (DET-CON-010/012/013/019) and the placeholder family fired nowhere. Code/infra parameters were walked against the Discourse project: **7 confirmed + 2 borderline false positives** (checks whose greps did not exclude samples/templates/docs/locales; FP clauses naming products instead of classes; deployment-scoped parameters hitting distributable software). All 14 flagged parameters were narrowed — path exclusions in checks, class-based FP clauses, deployment scoping, a first-party-vs-third-party claim split (CON-011), measurable-claims-only superlatives (CON-026), a page-level genericness test (CON-006) — 37 field edits in total. Every FP case was re-walked: none fires; fabrication and real-secret cases remain blocker. Honest residue: **39 of 44 visual parameters are not testable from fetched text** (they need screenshots or computed styles) and were recorded as UNTESTED — not passed — and carried into Phase 6.

**Rendered pass (Phase 6).** All 39 remaining visual parameters were exercised against rendered stripe.com, linear.app, and basecamp.com (Puppeteer screenshots + computed styles). Result: **FP 4 parameters** (DET-VIS-001, DET-VIS-015, DET-VIS-022, DET-VIS-041; six site-level hits), **NO-FIRE 35, UNTESTED 0**. All four were narrowed under the same protocol — breadth narrowed, detection core untouched; DET-VIS-022's measurement method was preserved and only its verdict narrowed. Re-walk of the six site-level hits: **6/6 clear**.

**Finding:** across both passes, every confirmed false positive was a *breadth* defect — a check written wider than its signal — and none was a defect in the fabrication core. Narrowing breadth while holding the core is a repeatable repair; it is now the repository's standard FP protocol.

### 2.6 Strand 6 — Findability: 10/10 against a 9/10 bar

The repository's core usability claim is that a single agent, given only `BOOTSTRAP.md` and `SKILLS_INDEX.md`, can route a task to the right skill. The formal §5.3 test (Phase 6; report `docs/internal/findability-test-phase6.md`) used a fresh agent that committed its choices *before* opening any SKILL.md: **10/10 correct first choices**, spanning 7 departments (bar: 9/10; the Phase 5 index-only dry run had scored 9/10). The test still found 3 real index defects, all fixed in the owning skills' metadata: no index entry contained "passkey"/"WebAuthn" (backend-auth Use-when extended); overlapping audit claims between multitenancy-saas (D2) and tenant-isolation (D5) (cross-reference added); no rendering-performance keywords (performance-optimization Use-when extended with the client-rendering clause — jank, dropped frames, long lists). Validation and bundle caps were re-verified after the fixes.

### 2.7 Strand 7 — Proof outcomes: the repository, used by strangers

Phase 6's proof team rule: every proof was executed by a fresh agent that had not authored the material it used, briefed only through the repository itself. Pass thresholds per project: 0 critical defects, ≤3 minor, 0 P0 slop hits, 0 fake-content hits, all gates green or formally dispositioned.

| Proof | What was built | Gates | Defects |
|---|---|---|---|
| P1 TaskBoard (the single-agent proof) | Multi-tenant team task manager: Node 24 + Express 5 + SQLite, server-rendered; scrypt auth, hashed-token sessions, CSRF on every mutation, login throttling; membership-scoped tenant queries (cross-tenant = 404, suite-tested); Stripe billing in test-mode patterns only (env keys, pending order first, official SDK Checkout, webhook HMAC + event-ID dedup; no keys → honest 503, nothing simulated); complete EN + UR i18n, Urdu as lang="ur" dir="rtl" | 52 checks: 43 passed, 4 waived (tool-form, with substitute evidence), 4 blocked (provisioning/Stripe-live class), 1 partial; **29/29 automated tests green** | P0 0, P1 1, P2 5 |
| P2 Atlas Blog | Static blog via the content-blog-site playbook: 28 routes, 6 genuine fully-written articles traced to fact-sheet claim rows with external evidence, client-side search, RSS 2.0, reconciled sitemap, JSON-LD generated from the same fields as the visible pages, AI authorship disclosed | **19/19 PASS; slop hits 0; fake-content hits 0** | 4, all P2, caught by gates and fixed |
| P3 Ledger API | Authenticated REST API: double-entry invariants tested, tenant/user isolation, OpenAPI verified against the running service | 42/48 (remainder green or formally waived) | **The built service ships with zero open defects in all classes** |
| P4 ShopClone | Original implementation of a generic small-store structure; D14 authorization record committed before reference work; no scraped assets, copy, or branding | 49/56 (3 waived with DECISIONS entries + compensating evidence) | P0 0, P1 3, P2 7, + AF-1 (P2, checkout error-announcement gap, WCAG 4.1.3 — triaged, counts as the project's 1 minor, within threshold) |

Compliance was measured, not assumed, for P1: the proof agent's load order (custom instructions first, then VERSION, CHANGELOG, BOOTSTRAP, index, bundles, and the always-on skills — no code before the step-0/1 documents) is recorded in its PROOF_REPORT.md and was verified against it.

**Repo defects are the finding.** The proofs' real output was not the four applications; it was the defects they exposed in the repository itself — all fixed in the owning departments, none closed by weakening a gate:

- The **mandated-manifest defect** (project-templates required a `mandated-manifest-<type>.txt` the repo did not ship) was found *independently by three proofs* (P1, P2, P3) — the strongest signal in the phase. Fix: 13 manifest files shipped in `templates/`, and the gate amended to diff against them.
- **Cited-but-unshipped scripts** (P3, P4 vs D8): qa-gates cited five scripts; the missing ones were written as real, tested, stdlib-only tools in `scripts/qa/`.
- **Single-tool / single-environment gates** (recurring across proofs and all 8 dry runs): gates naming one tool or one provisioned environment as their only form gained manual, local, or substitute-evidence forms, on the Phase 1 narrowing pattern.
- **Playbook dry runs** (8 remaining playbooks, one fresh agent each, small real builds): every playbook proved single-agent completable with workarounds — none "no". Their 66 friction points deduplicated into 28 root-cause clusters (22 open, 6 already fixed, 6 not-a-defect; worst severity P1, no P0); **all 22 open clusters (DR-01…DR-22) were fixed**, including adding a named pre-provisioning completion state to all 13 playbooks' Definitions of Done. With the proofs, **all 13 playbooks are exercised** (brief floor ≥11).

All four deployments remain provisioning-blocked (DECISIONS D-005: $0 spend, free tiers first; public deployment depends on the GitHub repository being published — a user step). The waivers are recorded in each proof with their unblocking conditions, never hidden. One open item is carried to the QA report: P4's G-SE-001 waiver formally needs the user's explicit agreement under the repo's waiver process (proof record D-P4-02, with compensating evidence G-SE-002/003/004 passing).

---

## 3. Limitations

Stated plainly, per this repository's own rules:

1. **X-Crawl transcript shortfall.** The brief's evidence-harvest target was ≥200 transcripts and ≥50 verified issues per department. This build's network environment repeatedly failed YouTube media/subtitle downloads (HTTP 403 via yt-dlp; some sources geo-blocked). Under the §3.3 rule — a blocked source is dropped and logged, never worked around — the harvest proceeded only through routes that work, and `docs/EVIDENCE_BASE.md` ships with 4 verified seed entries (from the handoff package itself) rather than the target volume. The shortfall is recorded here and in EVIDENCE_BASE.md; it was not padded with unverifiable entries. The detection parameters therefore rest on the inherited research, the cited standards literature, and this build's own verified findings more than on a fresh transcript corpus.
2. **The detector-gap evidence is text-only.** Claim 2's confirmation (§2.2) rests on benchmarks of *text* detectors. No equivalent independent benchmark suite for website/visual detectors was found; the 15–30-point gap is not claimed for them.
3. **The human-detection ballpark is cross-media.** The near-chance figures (51.2% overall; images 49.4%) come from AI-media studies generally, not from website-specific peer-reviewed work — which is precisely why the website-specific 55.5% figure is treated as untraceable rather than replaced with a borrowed number.
4. **False-positive coverage is three sites deep.** The FP passes used stripe.com, linear.app, basecamp.com (and Discourse for code/infra). Parameters that fire nowhere on three well-built sites may still fire on other legitimate patterns; the narrowing protocol, not the sample, is the durable result. One originally planned target (gov.uk) could not be fetched in the text pass and was excluded rather than substituted silently.
5. **Findability is a single-tester result.** The 10/10 score comes from one fresh agent on 10 tasks. It validates the routing design; it is not a statistical claim about all agents or all tasks.
6. **Proof depth is bounded by provisioning.** No proof ran against a live production environment, a live Stripe account, or real users. Billing correctness is established at the pattern level (signature verification and dedup tested locally), not observed against Stripe's live API — and the P1 report says so rather than claiming otherwise.
7. **Token accounting is estimated.** This runtime does not expose billable-token usage to the executor; `docs/METRICS.md` records agents spawned, deliverables, and measured outcomes per phase instead of a precise §8.1 ledger, and records that limitation in place of the numbers it cannot honestly give.

---

## 4. Conclusions

1. **Verification beats inheritance.** Every load-bearing inherited number in this build was either confirmed by script (200 / 198 / 69), corrected with the correction recorded (178 / 17 / 221), or found untraceable and demoted to a sourced ballpark (55.5%). None of those outcomes was knowable from the summaries that carried the claims. Any team building on prior AI research should budget for re-verification as a first-class phase — here it was Phase 1's calibration work and Phase 2's mapping, and it changed what the repository is willing to assert.
2. **Detection is a parameter surface, not a vibe — and parameters need FP testing like code needs tests.** The 203 parameters survived two adversarial passes against known-good work only after 20 of them were narrowed. A detection rule that has never been run against a professional site is a hypothesis; this build's protocol (fire → narrow breadth → re-walk → keep the core) is the mechanism that turns hypotheses into instruments.
3. **Honest nulls beat fake traceability.** Where coverage genuinely did not exist — 23 BAN entries with no matching detection parameter, 39 visual parameters untestable from text, a transcript harvest blocked by the network — the repository records the gap in a greppable, explicit form (DET-NONE; UNTESTED; the EVIDENCE_BASE constraint note) instead of papering over it. Each recorded gap is a work item a future maintainer can find by search; each papered-over gap would have been a false claim.
4. **Single-agent compatibility is a testable property, and it failed in instructive places.** Fresh agents using only this repository built four working applications and exercised all 13 playbooks — and the failures they hit were almost never "the skill was wrong" but "the skill assumed a team, a tool, or a provisioned environment the lone agent does not have." Single-operator modes, local/manual gate forms, and named pre-provisioning completion states are the fixes; they are now part of the repository, found by testing rather than by speculation.
5. **The defect loop is the product.** Phase 4 review (0 blockers, 6 majors, 31 minors across 94 deep-read skills), the proofs' repo defects, the dry-run triage, and the FP narrowing all fed fixes back into the owning departments, with full-repo validation (`scripts/validate-skills.py`: 227 skills, ALL PASS) and bundle caps re-verified after every batch. A skill library that cannot absorb its own test results this way would fossilize its first draft's mistakes; this one's structure — registry IDs, owning departments, mechanical validation — exists so that it can.

---

## Sources and records

Primary records in this repository: `docs/WCPM_MAPPING.md` (inheritance map and gate reconciliation); `docs/WEB_CRAFT_PAPER.md` (inherited paper, corrected figures, editor's note); `skills/detection/visual/PARAMETERS.md` (Calibration section — Cooke et al., *Communications of the ACM*; the preregistered three-country study; the Sortlist survey; Copyleaks/GPTZero claim-vs-benchmark pairs; RAID, ACL 2024; Liang et al., *Patterns* 2023 — each with its URL in place); `skills/detection/*/PARAMETERS.md` (203 parameters, each with its own Source field); `docs/internal/research/D1.md` … `D18.md` (department research, sources per file); `docs/EVIDENCE_BASE.md` (evidence base, method, and harvest constraints); `docs/internal/findability-test-phase6.md`; `docs/internal/forge-verification-report.md`; `docs/work-log/phase-0.md` … `phase-6.md`; `docs/DECISIONS.md`; `docs/METRICS.md` (every number above, defined). Proof reports: `PROOF_REPORT.md` in each proof workspace (`proofs/p1-taskboard/`, `proofs/p2-atlas-blog/`, `proofs/p3-ledger-api/`, `proofs/p4-shopclone/`, in the build workspace outside this repo). False-positive working reports: `build/validation/` in the build workspace.
