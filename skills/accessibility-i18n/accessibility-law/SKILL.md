# accessibility-law

## Metadata

- **Owner department:** D13 Accessibility & i18n (AC)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Directive (EU) 2019/882 (European Accessibility Act) summary, EUR-Lex — https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=legissum%3A4403933 ; Revised 508 Standards, US Access Board — https://www.access-board.gov/ict/ ; WCAG 2.2, W3C — https://www.w3.org/TR/WCAG22/
- **Depends on:** accessibility-audit (its dated per-criterion results are the evidence every statement and map entry rests on), wcag (the conformance target)
- **Feeds into:** legal-documents, compliance-audit (D14 confirms legal applicability and owns the legal determinations)

## When to use / Do NOT use

- **Use when:** A project needs its accessibility obligations mapped before launch, before entering a new market or sector, before bidding on public procurement, or when an accessibility statement or ACR/VPAT must be produced — the output is a recorded technical target: which instrument, which pinned WCAG version and level, which conformance artifact.
- **Do NOT use when:** Giving legal advice or deciding whether a law applies (that is D14/counsel — this skill escalates those questions), running the technical evaluation itself (accessibility-audit), or fixing defects (the owning D13 skill).

## Rules

1. **AC-061 — Map jurisdictions before launch.** Before launch, produce a jurisdiction map in the project's legal file set: for each market served, record the jurisdiction, the sector, the customer type (consumer, business, public procurement), the applicable instrument, and a named reviewer. No map, no launch claim.
2. **AC-062 — Record the pinned WCAG version per instrument.** Each map row names the WCAG version and level the instrument pins, not just the instrument's name. Current pins from the research: EAA via EN 301 549 V3.2.1 → WCAG 2.1 AA; Section 508 → WCAG 2.0 AA; ADA Title II rule → WCAG 2.1 AA. A row that says only "EU — EAA" is incomplete.
3. **AC-063 — Applicability follows the user and the customer, never the developer.** The governing law is determined by where the users are, what sector the product is in, and who the customer is. The team's own location confers no obligations and no exemptions.
4. **AC-064 — Build to the newest; document against the pinned.** The build target stays WCAG 2.2 AA. Where an instrument pins an older version, conformance is additionally documented against that pinned version (2.2 removes only 4.1.1 Parsing, which a 2.0-pinned engagement still lists — record how it was treated, never silently skip it).
5. **AC-065 — State the technical result; never a legal verdict.** Deliverables state standard, version, level, scope, and date ("Evaluated against WCAG 2.1 Level AA, EN 301 549 scope, 2026-11-21"). They never state "ADA compliant", "EAA compliant", or "legally accessible". This skill gives engineering conformance guidance; it is not legal advice and guarantees no legal outcome.
6. **AC-066 — Escalate interpretation questions to D14/counsel.** Whether an instrument applies, what an exemption requires, and what exposure a gap creates are legal questions. Record each question in the map with the answer's source and date when D14/counsel provides it; engineering does not fill the gap with an assumption.
7. **AC-067 — Name the required conformance artifact per jurisdiction, with an owner.** Before launch, the map lists the artifact each jurisdiction or customer requires — an accessibility statement (WAD/EAA model), an ACR/VPAT for US procurement, or none — and names who produces and maintains it.
8. **AC-068 — The accessibility statement must match the audit.** A published statement contains: the conformance status from the latest accessibility-audit report, the known exceptions and non-accessible content, a working feedback/contact mechanism, and the preparation and review dates. Any claim beyond the audited scope, or any audited exception omitted, makes the statement false.
9. **AC-069 — The feedback mechanism is real, routed, and tested.** The statement's contact route reaches a named owner (monitored inbox or ticket queue), and a test barrier report is submitted and confirmed received before publication. A route nobody reads is recorded as a defect, not published as a mechanism.
10. **AC-070 — Exemptions are documented legal determinations, never engineering assumptions.** Disproportionate burden, fundamental alteration, and microenterprise carve-outs exist only as determinations recorded in the map with the determiner (D14/counsel), the evidence relied on, and the date. An engineer closing a finding "exempt" without that record has made a legal decision they cannot make.
11. **AC-071 — Re-map on scope change and on the review date.** A new market, a new sector, a government customer, or a change to an instrument (a revised EN 301 549 cited in the Official Journal, an ADA Title II date extension) triggers re-verification of the affected rows. Every map carries a review date; an expired review date means the map is stale, not still valid.
12. **AC-072 — Read procurement documents per engagement.** A contract can pin a WCAG version older than both the law's floor and the department target (a Section 508 contract pins 2.0) or require a specific artifact format. Record the contract's exact accessibility requirement in the map before any conformance promise is made in a bid or statement of work.

## BAN list

- **BAN-AC-031 — Bare compliance verdict.** Banned: writing "ADA compliant", "EAA compliant", "100% accessible", or "legally accessible" in any deliverable, page, badge, or bid. Defeats: DET-NONE — no DET parameter names this signal; pattern owned by this skill. Bad: pricing page footer: "Fully ADA compliant website." Instead: "Evaluated against WCAG 2.2 Level AA on 2026-11-21; per-criterion results in the audit report; legal applicability confirmed by D14." Severity: BLOCK.
- **BAN-AC-032 — Dead feedback route in the statement.** Banned: an accessibility statement whose feedback/contact link is a placeholder (`#`, an unbuilt page) or an address nobody monitors. Defeats: DET-UX-002. Bad: statement reads "To report a barrier, contact us" with the link pointing to `#contact`. Instead: link a live contact route owned under AC-069, verified by the G-AC-034 test submission before publication. Severity: BLOCK.
- **BAN-AC-033 — Barrier-report form that submits nowhere.** Banned: a feedback form that shows a success message but stores and routes nothing, so reported barriers vanish. Defeats: DET-UX-003. Bad: the "Report an accessibility barrier" form thanks the user; no ticket, email, or record exists afterward. Instead: persist the report to the support queue, return a reference the user can cite, and confirm receipt in the G-AC-034 live test. Severity: BLOCK.
- **BAN-AC-034 — Engineering-assumed exemption.** Banned: closing a barrier or skipping a required flow as "disproportionate burden", "out of scope", or "the vendor's widget" on an engineer's say-so. Defeats: DET-UX-013. Bad: ticket closed: "Screen-reader checkout fix deferred — disproportionate burden." Instead: keep the finding open and escalate under AC-066/AC-070; only a recorded D14/counsel determination with evidence can close it. Severity: BLOCK.
- **BAN-AC-035 — Orphaned accessibility statement.** Banned: publishing the statement at a URL linked from nowhere — absent from the footer, help section, and sitemap — so users who need it cannot find it. Defeats: DET-UX-014. Bad: statement live at `/legal/a11y-statement-v2` with zero inbound links. Instead: link the statement from the footer and help navigation on every page, and verify the link in the G-AC-033 check. Severity: WARN.

## Gates

- **G-AC-031 — Jurisdiction map completeness (automated).** Verifies: AC-061, AC-062, AC-067. Check: run the project's map check over the legal file — `python3 scripts/check-jurisdiction-map.py docs/legal/jurisdiction-map.md` — which parses the map table and fails on any row with an empty jurisdiction, instrument, pinned WCAG version, level, required artifact, reviewer, or review-date field, and on any launch market with no row. Pass: zero missing fields and one complete row per launch market. Fail: block launch sign-off. Recorded in: progress.md.
- **G-AC-032 — Pinned-version conformance documented.** Verifies: AC-064, AC-072. Check: for every map row whose pinned version is older than 2.2, confirm a conformance statement against that pinned version exists from the latest accessibility-audit (per-criterion results naming the pinned version), and that any contract-pinned requirement is quoted in the map. Pass: every pinned version has a matching dated conformance statement. Fail: block any external conformance claim for that jurisdiction. Recorded in: progress.md.
- **G-AC-033 — Statement-vs-audit diff (automated).** Verifies: AC-068, BAN-AC-035. Check: extract the published statement's claimed conformance status, scope, and exception list; diff against the latest audit report's scope and findings register; also crawl the footer/help navigation for a working statement link. Pass: the statement claims nothing beyond the audited scope, every audited exception appears in the statement, and the statement link resolves. Fail: block publication (or unpublish) until the statement matches the audit. Recorded in: progress.md.
- **G-AC-034 — Feedback route live test.** Verifies: AC-069. Check: submit a test barrier report through the exact route published in the statement; confirm it arrives with the named owner (ticket ID or inbox receipt) and note the elapsed time. Pass: receipt confirmed by the owner. Fail: block statement publication. Recorded in: progress.md.
- **G-AC-035 — No-verdict language scan (automated).** Verifies: AC-065. Check: `grep -rniE "ADA compliant|EAA compliant|100% accessible|legally accessible|fully compliant" --include='*.md' --include='*.html' .` over deliverables and site copy, excluding quoted legal text and this skill's own BAN list. Pass: zero unaddressed hits — each hit is removed or rewritten as a technical result under AC-065. Fail: block release of the containing deliverable. Recorded in: progress.md.

## Anti-patterns

- **Template statement.** Copying a model accessibility statement, swapping in the product name, and publishing it before any audit exists. Catch it by asking for the audit report the statement's status line came from — if there is none, the statement is fiction (G-AC-033 will fail it).
- **Recycled ACR.** Reusing a VPAT/ACR from a previous product version, a previous vendor, or a marketing page as the current engagement's artifact. Catch it by matching the ACR's date, version, and evaluated build against the current release before it leaves the building.
- **Frozen map.** Treating the jurisdiction map as a kickoff document: written once, never revisited after an instrument changes or a new market opens. Catch it by checking the review date on every launch gate run (AC-071) — an expired date means re-verify, not proceed.
- **Pin drift.** Quietly documenting conformance against WCAG 2.2 because that is the build target, while the customer's contract pins 2.0 and nobody checked the difference. Catch it by reading the map's pinned-version column against the contract before any bid is submitted (AC-072).

## Examples

- [Example 1 — "ADA compliant" badge vs. technical result](examples/example-1.md) — violates/corrects AC-065.
- [Example 2 — Developer's-jurisdiction assumption vs. full jurisdiction map](examples/example-2.md) — violates/corrects AC-061.
- [Example 3 — Overclaiming statement vs. truthful statement with exceptions and feedback route](examples/example-3.md) — violates/corrects AC-068.

## Recall anchors

- Map first: jurisdiction, instrument, pinned version, artifact, reviewer, review date.
- The law follows the user and the customer — never the developer.
- Build to 2.2 AA; document against the version the law or contract pins.
- Technical result only — "compliant" is a verdict engineering never issues.
- A statement that overclaims the audit is a false statement, not marketing.

## Checklist

- [ ] Jurisdiction map exists in the legal file set with one complete row per launch market (AC-061, G-AC-031).
- [ ] Every row pins a WCAG version and level and names its required conformance artifact and owner (AC-062, AC-067).
- [ ] Conformance is documented against each pinned older version, not only against 2.2 (AC-064, G-AC-032).
- [ ] No deliverable, page, or bid contains a legal verdict or blanket compliance claim (AC-065, G-AC-035).
- [ ] Accessibility statement matches the latest audit: status, scope, and every known exception (AC-068, G-AC-033).
- [ ] Feedback route is live, owned, and test-submitted before publication (AC-069, G-AC-034).
- [ ] Every exemption in force is a recorded D14/counsel determination with evidence and date (AC-070).
- [ ] Map carries a current review date and is re-verified on scope change (AC-071).
