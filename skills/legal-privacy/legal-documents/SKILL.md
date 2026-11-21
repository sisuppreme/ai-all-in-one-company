# legal-documents

## Metadata

- **Owner department:** D14 Legal & Privacy (LG)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng
- **Depends on:** privacy-laws, fact-sheet
- **Feeds into:** cookie-consent, dsar-handling, compliance-audit, audit-trails

## When to use / Do NOT use

- **Use when:** drafting or updating the terms of service, privacy notice, or cookie policy; publishing a new document version; recording acceptance at signup or on a material change; checking published documents against the data inventory, processor register, and feature list.
- **Do NOT use when:** the document needs a legal decision — a novel clause, a contested rights position, sector-regulated wording. This skill drafts from the product's own registers and marks the output as a draft for qualified counsel; it never gives legal advice and never presents a generated document as reviewed law (LG-070).

## Rules

1. **LG-061 — Documents derive from the registers, or not at all.** Terms, the privacy notice, and the cookie policy are generated from this product's data inventory/RoPA, processor register, and feature list — never from a generic template. If a register input is missing or stale, the skill stops and names the gap instead of drafting around it.
2. **LG-062 — The notice carries the full information set.** The privacy notice states everything GDPR Articles 13/14 require — controller identity and contact, purposes, lawful basis per purpose, data categories, recipients/processors, transfers, retention, the rights available and how to exercise them — in plain language per Article 12(1).
3. **LG-063 — Every version is stored in full.** Each published version has a version ID and an effective date, and its complete text is archived at publication. Superseded versions remain retrievable: a dispute is answered with the exact text that user accepted.
4. **LG-064 — Acceptance is an event, not a sentence.** Acceptance is stored as a record — user, document, version, timestamp, mechanism — captured at signup. "By using this site you agree" with no stored record does not count as acceptance.
5. **LG-065 — Material changes are noticed and re-accepted.** A material change (new purpose, processor, or data category; a change to user rights or to how data is shared) is published as a new version with an effective date and a change notice, and existing users pass a re-acceptance flow before the new version binds them.
6. **LG-066 — Documents trail the registers, mechanically.** A new processor, data category, or purpose without a corresponding document update blocks release. A register change produces a document diff for review; the notice's processor and data-category lists are the same data as the registers, rendered — not a second hand-maintained copy.
7. **LG-067 — Template residue is a defect class.** A published document contains no other company's name, no bracketed or unfilled placeholders, and no product or feature names that are not this product's.
8. **LG-068 — Annexes attach only when the feature exists.** Sector and feature annexes (payments, user-generated content, minors) are included only while the feature ships. An annex for a removed or unbuilt feature is removed in the same release that removes the feature.
9. **LG-069 — Written for the user who must act on it.** Documents name this product and its controller, use defined terms consistently, and state every contact and rights route exactly as it works in the product. Copy a non-lawyer cannot parse fails, however complete it is.
10. **LG-070 — Counsel review is a recorded step.** The initial version and every material change carry draft status until a qualified legal review is recorded (reviewer, date, version reviewed). Publication before that record exists is a release defect, not a shortcut.
11. **LG-071 — Every route named in a document is live.** The privacy contact, the DSAR intake route, and any opt-out path named in a document are monitored and working. A document that routes a rights request to an unmonitored address or a dead form is a false statement, not a typo.
12. **LG-072 — The live text is the version of record.** The published page is identical to the archived version it claims to be. Corrections and edits ship as a new version under LG-063/LG-065; nobody edits a live document in place.

## BAN list

- **BAN-LG-031 — Notice describes another product's practices.** Banned: a privacy notice that names data the product does not collect, or omits data it does, because the text came from a template or a similar product. Defeats: DET-CON-014. Bad: the notice promises "we never collect location data" while the app stores GPS check-ins, and describes health records the product has never held. Instead: generate every practice statement from the data inventory and processor register, and fail loudly on a missing register input (LG-061). Severity: BLOCK.
- **BAN-LG-032 — Foreign names and placeholders in published text.** Banned: publishing a document containing another company's name, a bracketed placeholder such as `[Company Name]`, or a template's example product. Defeats: DET-CON-017. Bad: the terms greet users of "ShopSphere Inc." and set the governing law of "[State]" on a live page. Instead: run the residue lint (G-LG-032) and fill every field from this product's own records before publication (LG-067). Severity: BLOCK.
- **BAN-LG-033 — Agreement claimed with no acceptance record.** Banned: relying on "by using this site you agree" (or an equivalent sentence) as the only evidence of acceptance — no stored version, no timestamp, no mechanism. Defeats: DET-CON-028. Bad: a dispute asks which terms a user accepted; the only answer is a footer sentence and a "last updated" date. Instead: store the acceptance event at signup and on material change, and answer disputes from the archive (LG-064, LG-063). Severity: BLOCK.
- **BAN-LG-034 — Silent in-place change of a binding document.** Banned: editing live terms or a live notice — new clause, same version ID and effective date — with no change notice and no re-acceptance. Defeats: DET-CON-018. Bad: an arbitration clause appears in the terms overnight; the page still reads "Version 1.0, effective March 1" and no user was told. Instead: publish a new version with a new effective date, notify users, and run the re-acceptance flow for material changes (LG-065, LG-072). Severity: BLOCK.
- **BAN-LG-035 — Versions of a document that contradict each other.** Banned: serving different markets, locales, or surfaces different live versions of the same document whose substance disagrees (different processors named, different retention stated). Defeats: DET-CON-015. Bad: the English notice lists three processors; the translated notice, two versions behind, lists five — including one the product stopped using. Instead: one version of record per document, translations generated from it, and the diff gate run across every served variant (LG-066, G-LG-031). Severity: WARN.

## Gates

- **G-LG-031 — Document-vs-register diff.** Verifies: LG-061, LG-066. Check (automated): in CI, extract the processor names and data categories named in the privacy notice and diff them against the processor register and the RoPA; repeat for every served locale/surface variant. Pass: zero names or categories present in one source and absent from the other. Fail: block shipment until the register or the document is corrected. Recorded in: progress.md.
- **G-LG-032 — Template-residue lint.** Verifies: LG-067. Check (automated): scan the publishable document set for bracketed placeholders (`\[…\]`, `{{…}}`, "Lorem", "TODO"), and for any organization or product name not in the project's approved-names list from the fact-sheet. Pass: zero hits. Fail: block publication. Recorded in: progress.md.
- **G-LG-033 — Acceptance-record test.** Verifies: LG-064, LG-065. Check (automated): create a test account in staging and assert an acceptance row exists carrying user ID, document ID, version, timestamp, and mechanism; then publish a test material change and assert the re-acceptance prompt fires and its acceptance is recorded as a second row. Pass: both rows exist with all fields. Fail: block shipment. Recorded in: progress.md.
- **G-LG-034 — Version-archive integrity check.** Verifies: LG-063, LG-072. Check (automated): hash each live legal page and compare against the archived text of the version it declares; assert every superseded version's full text is present in the archive. Pass: every live hash matches its declared version and the archive is complete. Fail: block shipment — the live page is replaced from the archive or republished as a new version. Recorded in: progress.md.
- **G-LG-035 — Counsel-review and live-read check.** Verifies: LG-070, LG-062, LG-071. Check (manual): confirm a counsel-review record (reviewer, date, version) exists for the current version and each material change, with no version published while in draft status; then read the live privacy notice against the data inventory end to end and exercise each contact and rights route it names. Pass: review records complete, no practice in the inventory missing from the notice or vice versa, every named route answers. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **Generator-of-the-month.** Each update re-runs a fresh online template generator, so wording oscillates between versions and the archive stops meaning anything. Catch it by diffing consecutive versions: if the structure changed more than the practices did, the document was regenerated, not revised.
- **Annex hoarding.** Payments, UGC, or minors clauses are kept "just in case" after the feature is removed or before it is built. Catch it by walking the feature list against the annex list at every release; an annex with no live feature behind it comes out in that release.
- **Legal-review theater.** A review is recorded, but counsel was sent a summary or a diff excerpt instead of the full text of the version. Catch it in the review record: it names the full version text reviewed, or the review does not count.
- **Acceptance amnesia.** A user deletes an account and later re-registers; the team treats the first account's acceptance rows as covering the new account. Catch it in the acceptance store: acceptance is keyed to the account and the signup event, so a new account with no row of its own is unaccepted by construction.

## Examples

- [Example 1 — The policy copied from another product](examples/example-1.md) — violates/corrects LG-061.
- [Example 2 — "By using this site you agree"](examples/example-2.md) — violates/corrects LG-064.
- [Example 3 — The terms that changed overnight](examples/example-3.md) — violates/corrects LG-065.

## Recall anchors

- Documents are rendered from the registers, never written from a template.
- Acceptance is a stored event: user, version, timestamp, mechanism.
- A material change means a new version, a notice, and re-acceptance.
- The live page is byte-identical to the archived version it claims to be.
- Every document ships as a draft until counsel review is recorded.

## Checklist

- [ ] Terms, privacy notice, and cookie policy generated from the current data inventory, processor register, and feature list (LG-061, G-LG-031).
- [ ] Privacy notice carries the full Articles 13/14 information set in plain language (LG-062).
- [ ] Current version archived in full with version ID and effective date; superseded versions retrievable (LG-063, G-LG-034).
- [ ] Acceptance events stored at signup with user, version, timestamp, mechanism (LG-064, G-LG-033).
- [ ] Material changes published as new versions with change notice and re-acceptance (LG-065).
- [ ] Residue lint clean: no foreign names, placeholders, or clauses for unshipped features (LG-067, LG-068, G-LG-032).
- [ ] Counsel-review record exists for the current version; no version published in draft status (LG-070, G-LG-035).
- [ ] Every contact and rights route named in the documents tested live (LG-071).
