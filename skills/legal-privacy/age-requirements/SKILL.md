# age-requirements

## Metadata

- **Owner department:** D14 Legal & Privacy (LG)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng ; https://www.ftc.gov/business-guidance/privacy-security/childrens-privacy
- **Depends on:** privacy-laws, audit-trails
- **Feeds into:** dsar-handling, legal-documents, compliance-audit

## When to use / Do NOT use

- **Use when:** a product is child-directed, is likely to be accessed by children, or may acquire child users in any market; building or changing the age screen, the parental-consent flow, the under-age removal path, or the per-market age table; a market is added where an age regime applies.
- **Do NOT use when:** the product decision itself is open — whether to serve children at all, which verification vendor is proportionate for a children's product, or a contested parental-rights call. Children's products are an escalation stop (LG-151): this skill builds the gate and the records; qualified counsel confirms the regime choices.

## Rules

1. **LG-141 — The threshold is per-market configuration, never a constant.** A table in the project legal file maps each market to its regime, minimum age, accepted verification method, source, last-verified date, and review date (GDPR Article 8: 16 by default, member states may lower to not below 13; UK 13; US COPPA: under 13 with verifiable parental consent). Code reads the table; adding a market means adding a verified row first.
2. **LG-142 — The gate runs before collection.** Where a service is child-directed or child users are expected, the age screen runs before any personal data is collected beyond what the gate itself needs; an under-threshold result stops the signup, not a later step of it.
3. **LG-143 — The age screen is neutral.** No pre-filled or defaulted adult date, no "Are you over X?" one-tap-through on a child-directed service, no copy, ordering, or visual emphasis that coaches a passing answer. The screen asks for the date of birth (or the regime's neutral equivalent) and computes the determination.
4. **LG-144 — Under-threshold means routed or blocked, never waved through.** An under-threshold user is routed to the parental-consent flow where the regime provides one, or blocked where none exists. After a failed determination, changing the entered date in the same session is locked or flagged per the market row — retry-until-pass is a defect, not a UX choice.
5. **LG-145 — Parental consent is verifiable and recorded.** Consent is captured by a method the regime accepts (COPPA: signed form, payment-card transaction with notice, trained-staff call/video, government-ID check with prompt deletion, knowledge-based authentication; GDPR Article 8(2): reasonable efforts to verify parental authorisation) and stored as a consent record — method, timestamp, scope, child account — in the audit trail. A lone "I am the parent" checkbox is not a method.
6. **LG-146 — Store the determination, not the birthday.** The record kept is the threshold determination, its basis (market row, method), and its date. A full date of birth is stored only where a registered purpose in the data map requires it; age-gate data carries its own retention limit and is deleted when the determination no longer needs to be demonstrable.
7. **LG-147 — Age data is never reused.** Data collected for the gate or for parental consent is never used for marketing, profiling, ad targeting, or product analytics. It exists for the determination and its demonstration, and for nothing else.
8. **LG-148 — Actual knowledge applies retroactively.** When the product learns an existing user is under-threshold (support contact, report, content signals), that account enters the same flow as a fresh under-threshold signup: parental consent obtained, or the account is removed. Time on the platform grandfathers nothing.
9. **LG-149 — Parents hold working rights.** A parent can review the child's data, withdraw consent, and demand deletion through the dsar-handling flows, with the same clocks and records as any other request; withdrawal stops the processing the consent justified.
10. **LG-150 — Removal is a defined, executed path.** An under-age account without valid consent is suspended on discovery, then deleted per the retention schedule across primary stores, indexes, analytics, and processors — deletion verified by a residue check, never by hiding the profile.
11. **LG-151 — Design codes and teen laws are register entries, and children escalate.** Regimes beyond the consent age (e.g. the UK Age Appropriate Design Code, US state teen-privacy laws) are rows in the obligations register, flagged as variance and reviewed — not silently ignored. Launching or materially changing a children's product stops for qualified counsel before build, per privacy-laws LG-011.
12. **LG-152 — Every row is dated and sourced.** A market row past its review date is treated as unverified: the threshold it states cannot be relied on until re-verified against the national rule in force at that date. National ages change by statute; the table is the only place they live.

## BAN list

- **BAN-LG-071 — The cosmetic age gate.** Banned: an age control that does not gate — a self-declaration checkbox or "confirm your age" button on a child-directed service whose answer is never checked, never stored, and blocks nothing. Defeats: DET-FAKE-021. Bad: signup shows "I confirm I am 13 or older" with a pre-ticked box; unchecking it still creates the account, and no record of the answer exists. Instead: run a neutral age screen before collection, compute the determination from the market row, and store the determination (LG-142, LG-143, LG-146). Severity: BLOCK.
- **BAN-LG-072 — One hardcoded age for every market.** Banned: a single age constant in code or copy applied to all markets regardless of the per-market regime. Defeats: DET-CON-018. Bad: `MIN_AGE = 13` ships globally; German users are admitted at 13 although the German Article 8 age is 16, and nobody notices because the number looks plausible. Instead: read every threshold from the dated, sourced market table (LG-141, LG-152). Severity: BLOCK.
- **BAN-LG-073 — The recorded lie: age_verified without verification.** Banned: setting an `age_verified` (or equivalent) flag, or telling parents/regulators that age is verified, when the flow performed no verification step. Defeats: DET-FAKE-022. Bad: the account record carries `age_verified: true` because the user clicked "Yes" on a prompt; the privacy notice states "we verify the age of all users." Instead: the flag is set only by a completed determination or parental-consent flow, and the notice describes the method actually used (LG-143, LG-145). Severity: BLOCK.
- **BAN-LG-074 — The birthday kept and spent.** Banned: retaining full dates of birth collected at the gate beyond the determination's need, or reusing gate data for birthday marketing, targeting, or profiling. Defeats: DET-CON-014. Bad: the notice says birth dates are collected "only to check your age"; the full date is stored permanently and feeds a birthday-discount campaign segment. Instead: store the determination and its basis, delete the raw date per its retention limit, and never route gate data to marketing (LG-146, LG-147). Severity: BLOCK.
- **BAN-LG-075 — The child-safety promise with no removal process.** Banned: publishing "children under X cannot use this service" (or equivalent) while no discovery, suspension, and deletion path for under-age accounts exists behind the claim. Defeats: DET-CON-028. Bad: the terms bar under-13s; a parent reports an 11-year-old's account and support replies that they "cannot verify ages," leaving the account live. Instead: ship the actual-knowledge flow — suspend, seek parental consent or delete, verify by residue check — before the promise is printed (LG-148, LG-150). Severity: WARN.

## Gates

- **G-LG-071 — Age-flow test suite.** Verifies: LG-141, LG-142, LG-144. Check (automated): scripted signups run per market row in staging — a test user below the row's threshold must be blocked or routed to the parental-consent flow and must not reach account creation or any age-restricted feature; a test user at the threshold proceeds. Pass: every market row behaves as configured. Fail: block shipment. Recorded in: progress.md.
- **G-LG-072 — Consent-record assertion.** Verifies: LG-145. Check (automated): completing the parental-consent flow in staging asserts a stored consent record with method, timestamp, and scope; completing an under-threshold signup with no consent record on file must be impossible — the test attempts it directly against the account-creation endpoint. Pass: record exists for the consented account; the unconsented creation is rejected. Fail: block shipment. Recorded in: progress.md.
- **G-LG-073 — Configuration and freshness scan.** Verifies: LG-141, LG-152. Check (automated): `grep` the codebase and copy for hardcoded age thresholds (numeric age constants outside the market-table module) and scan the market table for rows past their review date. Pass: zero hardcoded thresholds, zero stale rows. Fail: block shipment — thresholds move into the table and stale rows are re-verified first. Recorded in: progress.md.
- **G-LG-074 — Minimisation and removal drill.** Verifies: LG-146, LG-148, LG-150. Check (automated): seed a test under-age account, trigger the actual-knowledge path, and run removal; afterwards residue queries across the database, search index, and admin views return nothing for the test subject, and the account store holds no full date of birth for determination-only accounts. Pass: zero residue, determination-only storage confirmed. Fail: block shipment. Recorded in: progress.md.
- **G-LG-075 — Neutrality and escalation review.** Verifies: LG-143, LG-149, LG-151. Check (manual): read the live age screen against the neutrality rules (no defaults, no coaching, no retry-until-pass), walk a parental review/withdrawal/deletion request through dsar-handling end to end, and confirm the children's-product escalation to counsel is recorded for this product or the stop condition is absent in writing. Pass: all three hold. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **The gate at the checkout.** The age screen sits at payment or first posting instead of signup, so an under-age user's data has been collected and profiled for weeks before the gate fires. Catch it by tracing which personal data exists before the gate step in the flow; anything beyond the gate's own input means the gate is in the wrong place.
- **"Not child-directed" as a permanent fact.** The product was declared general-audience once and the declaration is never revisited while the audience visibly fills with children. Catch it by sampling support tickets, reports, and content signals for age evidence; a rising count is actual knowledge arriving, whether or not anyone files it.
- **One screen, every locale, wrong dates.** A single English age screen with one date format serves all markets, so day/month order flips determinations for real users. Catch it by running the gate in each shipped locale with a boundary date (e.g. 05/06) and confirming the computed determination matches the intended reading.
- **Verification maximalism.** Every user is sent through ID-document verification because it feels safest, although the regime accepts a lighter method for the risk at hand. Catch it in design review: the method per market row must be the least-data method the regime accepts, and any heavier method needs a recorded reason.

## Examples

- [Example 1 — The checkbox that gated nothing](examples/example-1.md) — violates/corrects LG-142, LG-143.
- [Example 2 — One age for the whole world](examples/example-2.md) — violates/corrects LG-141.
- [Example 3 — The under-age account support found](examples/example-3.md) — violates/corrects LG-148, LG-150.

## Recall anchors

- The threshold is a table row, never a constant.
- The gate runs before collection, and it actually gates.
- A neutral screen asks; it never coaches.
- Store the determination, not the birthday.
- Discovered under-age means consent or deletion — never grandfathered.

## Checklist

- [ ] Every served market has a dated, sourced age-table row with regime, threshold, and method (LG-141, LG-152, G-LG-073).
- [ ] The age screen runs before personal-data collection and blocks or routes under-threshold users (LG-142, LG-144, G-LG-071).
- [ ] The screen is neutral: no pre-filled dates, no coaching, no retry-until-pass (LG-143, G-LG-075).
- [ ] Parental consent uses a regime-accepted method and is stored as a consent record (LG-145, G-LG-072).
- [ ] Only the determination is stored; gate data is retention-limited and never reused (LG-146, LG-147, G-LG-074).
- [ ] The actual-knowledge path suspends and removes under-age accounts, verified by residue check (LG-148, LG-150, G-LG-074).
- [ ] Parental review, withdrawal, and deletion work through dsar-handling (LG-149, G-LG-075).
- [ ] Design-code and teen-law variance is registered, and the children's-product counsel escalation is recorded (LG-151, G-LG-075).
