# privacy-laws

## Metadata

- **Owner department:** D14 Legal & Privacy (LG)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng ; https://cy.ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/accountability/records-of-processing-and-lawful-basis/
- **Depends on:** fact-sheet
- **Feeds into:** legal-documents, cookie-consent, dsar-handling, data-residency, compliance-audit

## When to use / Do NOT use

- **Use when:** a product enters a market, adds a feature, data category, user type, or processor; building or re-verifying the obligations register, the data map (RoPA), the lawful-basis register, or the retention schedule; deciding whether a processing purpose may be built at all.
- **Do NOT use when:** the question needs a legal decision — novel processing, children's, health, finance, or biometric data, a contested rights call, regulator contact. This skill produces engineering artifacts for qualified counsel to confirm; it never gives legal advice and never declares a product compliant (LG-011).

## Rules

1. **LG-001 — Register before features.** Before build, enumerate markets served × data categories processed × user types in the obligations register; each cell records the governing regime, the obligations it creates, and the product requirement satisfying each. A market or feature with no register row does not ship.
2. **LG-002 — The register is data, not prose.** Register rows carry: market, regime, obligation, requirement, owner, lawful basis, last-verified date, review date. If coverage cannot be checked mechanically from the table, the register is an essay and fails.
3. **LG-003 — Lawful basis per purpose.** Every processing purpose has a recorded lawful basis (GDPR Article 6, or the applicable regime's equivalent permission) assigned per purpose, never per product, before the purpose is built.
4. **LG-004 — The data map is the source.** Every personal-data category in the data map (RoPA) has a purpose, a lawful basis, and a retention period; the register derives from the data map, and the two never disagree silently — a mismatch is a defect in one of them.
5. **LG-005 — Minimisation at the schema level.** A form field, column, or event property with no registered purpose is removed from the form and schema, not excused in policy prose.
6. **LG-006 — Triggers are tested, not assumed.** DPIA triggers (GDPR Article 35) and DPO/representative triggers (Articles 37–39) are tested explicitly for each product and the outcome recorded, including "not triggered, because…" with the reasoning.
7. **LG-007 — Retention is a schedule, not an intention.** Every data category has a retention period in the register and a deletion or anonymisation mechanism that actually runs; "kept as long as needed" is not a retention period.
8. **LG-008 — Variance is stated, never averaged.** Where regimes conflict (e.g. a retention duty against an erasure right), the conflict is logged in the register and escalated to counsel; nobody resolves it by picking the convenient rule.
9. **LG-009 — Every legal statement is dated and sourced.** Each register row names its source and last-verified date; a row past its review date is treated as unverified and blocks reliance until re-verified.
10. **LG-010 — Scope is explicit.** Deep profiles ship for GDPR and CCPA/CPRA only. Every other regime is a register-format entry marked "register before serving"; no output implies coverage the register does not contain.
11. **LG-011 — Escalation stops are hard stops.** Children's products, health/finance data, biometric processing, novel processing, contested rights calls, and any regulator contact stop the work: the output is the artifact set plus "this needs qualified counsel." The skill never declares a product "GDPR compliant" or equivalent.
12. **LG-012 — Change re-derives the register.** A new market, feature, processor, data category, or user type triggers a register update before release; the register is re-run on change, not on an annual ritual.

## BAN list

- **BAN-LG-001 — Compliance claimed without a tested process.** Banned: publishing "GDPR compliant", "fully compliant", or an equivalent badge in marketing, docs, or the product when no tested control supports the exact wording. Defeats: DET-CON-012. Bad: the pricing page carries a "100% GDPR Compliant" badge; the register has no DSAR flow and no retention schedule behind it. Instead: publish only what a dated audit artifact proves, worded as what was tested, when, and against what (LG-011). Severity: BLOCK.
- **BAN-LG-002 — Privacy artifacts copied from another product.** Banned: a data map, register, or notice derived from a template or another product's documents instead of this product's own inventory. Defeats: DET-CON-014. Bad: the data map lists "patient records" copied from a healthcare template while omitting the analytics identifiers this product actually stores. Instead: derive every row from this product's data map and feature list (LG-001, LG-004). Severity: BLOCK.
- **BAN-LG-003 — Erasure on paper, hiding in the product.** Banned: recording an erasure right or retention limit in the register while the implemented flow only hides the profile or flags the record and keeps the data reachable. Defeats: DET-FAKE-011. Bad: the register promises erasure within one month; "Delete account" sets `hidden = true` and the record still appears in admin search and exports. Instead: implement erasure against the stores the register names, verified by a residue check (LG-007). Severity: BLOCK.
- **BAN-LG-004 — Rights promised with no process behind them.** Banned: a privacy notice or register that promises access, erasure, or objection rights while no working intake and handling flow exists. Defeats: DET-CON-028. Bad: the notice says "email us to delete your data"; the address is unmonitored and no request has ever been actioned or logged. Instead: ship the intake channel, the clock, and the handling flow first, then write the promise (LG-001). Severity: BLOCK.
- **BAN-LG-005 — Regime values hardcoded as eternal constants.** Banned: baking a consent age, a response clock, or an adequacy status into code or copy as an undated constant with no source or review date. Defeats: DET-CON-018. Bad: the signup flow hardcodes "age 16" for every market and the help page states a response deadline copied when the register was first drafted. Instead: keep every such value in the dated, sourced register table and read it as per-market configuration (LG-009). Severity: WARN.

## Gates

- **G-LG-001 — Register coverage check.** Verifies: LG-001, LG-003. Check (automated): script the register against product config and the data map — every market in config and every processing purpose in the data map must have a register row with non-empty regime, lawful-basis, and owner fields. Pass: zero uncovered markets or purposes. Fail: block shipment. Recorded in: progress.md.
- **G-LG-002 — Data-map completeness check.** Verifies: LG-004, LG-005, LG-007. Check (automated): every data-map row asserts a stated purpose, lawful basis, and retention period; every personal-data field found in schemas and forms (`grep` the schema/form definitions against the data map's category list) maps to a data-map row. Pass: no category missing a basis or retention, no unmapped field. Fail: block shipment — the unmapped field is removed or registered first. Recorded in: progress.md.
- **G-LG-003 — Review-date lint.** Verifies: LG-009. Check (automated): scan the register for rows whose review date is earlier than today. Pass: zero stale rows. Fail: block reliance on the stale rows until re-verified against their sources; the compliance-audit checklist stays open meanwhile. Recorded in: progress.md.
- **G-LG-004 — Processor tripwire.** Verifies: LG-012. Check (automated): diff the dependency/SDK list and third-party endpoints in the build against the register's processor rows. Pass: every processor in the build has a register row. Fail: block shipment — a new analytics or processor SDK with no row is unregistered processing. Recorded in: progress.md.
- **G-LG-005 — Trigger and escalation review.** Verifies: LG-006, LG-008, LG-011. Check (manual): read the register's trigger section and conflict log — every DPIA/DPO trigger test has a recorded outcome, every regime conflict has an escalation entry, and every LG-011 stop condition is either absent (with the check recorded) or escalated to counsel. Pass: all three hold in writing. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **Launch-week register.** The register is written after the features exist, describing whatever was built instead of constraining it. Catch it by comparing register row dates against feature commit dates; rows that postdate their features were paperwork, not engineering.
- **One-regime copy-paste.** GDPR rows are duplicated for every market with the regime name swapped. Catch it by sampling a non-GDPR row and asking which of its obligations actually differ; if none do, the row was never derived.
- **Aspirational register.** Rows describe the processing the team intends someday, not the processing running today. Catch it by tracing one row to the live schema and one live field back to a row; either direction failing means the register is fiction in one direction.
- **Verified by confidence.** A reviewer bumps a row's last-verified date because "nothing changed" without opening the source. Catch it in review: a re-verification names what was compared against the source text, or the date does not move.

## Examples

- [Example 1 — The purpose with no lawful basis](examples/example-1.md) — violates/corrects LG-003.
- [Example 2 — The compliant badge](examples/example-2.md) — violates/corrects LG-011.
- [Example 3 — The field collected just in case](examples/example-3.md) — violates/corrects LG-005.

## Recall anchors

- No register row, no ship: markets and purposes are enumerated before build.
- Lawful basis is per purpose, never per product.
- A field with no purpose is deleted, not policy-washed.
- Conflicts are logged and escalated, never averaged away.
- This skill builds artifacts for counsel; it never declares compliance.

## Checklist

- [ ] Every market, feature, and user type has a register row (LG-001, G-LG-001).
- [ ] Every processing purpose has a recorded lawful basis (LG-003).
- [ ] Every data-map category states purpose, lawful basis, and retention period (LG-004, LG-007, G-LG-002).
- [ ] No form or schema field lacks a registered purpose (LG-005).
- [ ] DPIA and DPO trigger tests recorded, including negative outcomes (LG-006, G-LG-005).
- [ ] No register row is past its review date (LG-009, G-LG-003).
- [ ] No LG-011 stop condition is un-escalated; no public compliance claim lacks a tested control (LG-011, BAN-LG-001).
