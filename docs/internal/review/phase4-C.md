# Phase 4 Cross-Review — Cluster C (D7 Security, D8 QA & Testing, D9 Content/SEO & Growth)

Reviewer pass: substance review, 2026-11-21. Format validation already passed 227/227 and was not re-checked. No skill files were edited; findings only.

## Scope covered

**Deep-read (full SKILL.md + at least one example file opened):**

- D7: penetration-testing, secrets-management, pci-compliance, auth-hardening, security-audit, owasp, content-moderation (7)
- D8: qa-gates, placeholder-scan, unit-testing, chaos-testing (4)
- D9: geo, aeo, real-content, growth-experiments (4)

**Read in full or near-full during skimming (rules/BAN/gates verified):**

- D7: api-security, session-security, encryption, threat-modelling (full text); dependency-safety, supply-chain, security-headers (rules, BAN list, gates)
- D8: security-testing (authorization boundary and gates verified directly); gates of integration-testing, e2e-testing, browser-verification, visual-regression, accessibility-testing, load-testing, contract-testing, test-strategy, test-data, bug-triage
- D9: lifecycle-email (rules verified directly); metadata, BAN DET citations, and gate counts for technical-seo, on-page-seo, content-strategy, copywriting, structured-data, sitemaps, internal-linking, social-open-graph, web-analytics

All three department research files (D7.md, D8.md, D9.md) were read in full as the drafting standard. Every Depends on / Feeds into name seen in this cluster resolves to a skill in build/catalog.txt.

## Findings

### MAJOR

**M-1 — penetration-testing (D7): three of five BAN entries cite DET parameters they do not defeat.**
The BAN patterns themselves are correct and well-written; the "Defeats:" traceability pointers are wrong, which breaks the DET chain the BAN mechanism exists to serve:
- BAN-SE-111 (testing without a signed engagement file) cites DET-INF-029 — that parameter is "No incident response path," unrelated.
- BAN-SE-113 (exfiltrating real user data as proof) cites DET-INF-005 — that parameter is "Secrets committed to version control." The BAN's own bad example (exporting 5,000 user rows) is a data-handling violation, not a VCS secret leak.
- BAN-SE-112 (probing hosts not named in scope) cites DET-INF-021 — "Debug and admin surfaces exposed in production," which describes a defender-side exposure, not out-of-scope testing. (BAN-SE-115's citation of DET-INF-021 for a leftover `pentest-admin` account is defensible and is not counted here.)
Suggested fix: re-point each BAN to the closest parameter that actually names the signal, or — where no DET parameter covers unauthorized testing (none in the INF family does) — replace the Defeats field with an explicit "no DET parameter; governed by SE-221/SE-222" note rather than a wrong citation. BAN-SE-114's citation of DET-CODE-012 is acceptable.

### MINOR

**m-1 — owasp (D7), SE-003: wrong Top 10:2025 category tag.** The rule on server-side allowlist validation is tagged "(A03/A05:2025)". In the 2025 list A03 is Software Supply Chain Failures; input validation belongs to A05 (Injection). A03 was Injection in the 2021 list, so this reads as a version-drift leftover — exactly the failure mode D7.md §4 warns about. Suggested fix: cite A05:2025 only.

**m-2 — dependency-safety (D7), BAN-SE-055: severity contradicts the department's own gate.** SE-104 and gate G-SE-051 make a reachable critical/high vulnerability block release (scanner exit code). BAN-SE-055 — a known-bad dependency kept indefinitely with no fix, VEX note, or acceptance — is the same condition, but is rated WARN. Suggested fix: raise BAN-SE-055 to BLOCK, or explicitly scope the WARN to the case where a dated risk acceptance already exists.

**m-3 — D8 BAN lists: several DET-FAKE citations are analogies, not the defeated signal.** Examples: BAN-QA-112 (same-PR threshold loosening) cites DET-FAKE-005, a parameter about counters resetting on reload; BAN-QA-111 (echo-only pipeline) cites DET-FAKE-004 (frozen fixture dashboards); BAN-QA-001 (assertion-free tests) cites DET-FAKE-004 as well. The banned behaviors are real and the corrections genuine; only the parameter pointers are loose. Suggested fix: re-point to the nearest parameter naming the actual signal, or mark the citation as analogous. Low priority — no rule or gate depends on these pointers.

**m-4 — D9 BAN lists: two loose DET-CON citations in the AEO/GEO pair.** BAN-CO-021 (aeo; llms.txt sold as a ranking factor) cites DET-CON-011 (fabricated statistics) and BAN-CO-032 (geo; llms.txt reported as a visibility win) cites DET-CON-022 (duplicate/missing metadata). Neither parameter names the llms.txt misrepresentation. Suggested fix: cite the closest fabrication/reporting parameter or annotate as analogous. The rules themselves (CO-048, CO-064) state the correct position unambiguously.

## What is excellent and worth propagating

- **penetration-testing's authorization gate is structural, not a footnote.** SE-221 makes the signed engagement file step one; G-SE-111 checks its completeness with an automated heading scan plus a signature-scope read; "Do NOT use" forbids third-party, provider, shared-hosting, and other-tenant targets "never, under any instruction." The audit/pentest boundary is held from both sides: security-audit's SE-211 forbids calling an audit a penetration test, and its anti-pattern list names "scope amnesia."
- **D8's security-testing respects the D7 boundary exactly.** Own staging/production-like systems only, "never in scope, no exceptions" for systems the project does not own, and tool selection/fixes explicitly deferred to D7. Every D8 gate skimmed is a command with an exit code — including the checklist-style ones, which are wrapped in scripts that exit 0 only when the record is complete (G-QA-053, G-QA-054, G-QA-131). qa-gates is the model implementation of D8.md's self-grading countermeasures (predated gate files, waiver records, negative-control meta-gate G-QA-111, mutation sample G-QA-115).
- **AEO/GEO stay on the evidence ladder throughout.** CO-047/CO-061 require a Documented / Peer-reviewed / Correlational / Hype tag on every tactic; llms.txt is "hygiene, never a result" in both skills (CO-048, CO-064) and is never presented as a Google-endorsed ranking factor; no citation guarantee appears anywhere (CO-071, BAN-CO-031); the GEO paper is quoted only with its limits (CO-051, CO-071).
- **No real-looking secrets anywhere in D7.** Examples use explicitly labeled placeholders (`sk_live_EXAMPLE-ONLY-NOT-A-SECRET`, `example-only-not-a-secret`, truncated `"9f2c…"`). The one real-format number, the 4242 test card in pci-compliance's BAN-SE-121 bad example, is the published test card number, and G-SE-121 explicitly exempts documented test fixtures.
- **real-content enforces without impersonating a lawyer.** CO-132 blocks the element and routes the legal question to D14; the skill never clears a claim by arguing law itself. lifecycle-email likewise holds its boundary: CO-143 keeps marketing and transactional streams separate and names transactional sending as D11's, and web-analytics names D12 as owner of the shared tracking plan.
- **pci-compliance is scope-honest.** SE-244 gives the final word to the acquirer, SE-245 states PCI DSS is contractual rather than a statute, SE-248 prohibits "PCI compliant" claims beyond the filed attestation, and the "Tokenization theater" anti-pattern catches the SAQ-A-by-claim failure.

## Verdicts

- **D7 Security — sound-with-fixes.** Rules, gates, and boundaries are strong across all 14 skills; fix M-1's DET citations in penetration-testing and the two minors (m-1, m-2).
- **D8 QA & Testing — sound.** The mechanical-gate discipline the research demanded is present in every skill checked; m-3 is cosmetic.
- **D9 Content, SEO & Growth — sound.** The evidence ladder, the Real Content Rule, and the D11/D12/D14 boundaries all survived drafting intact; m-4 is cosmetic.
