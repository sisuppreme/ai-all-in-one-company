# dsar-handling

## Metadata

- **Owner department:** D14 Legal & Privacy (LG)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng/ ; https://cppa.ca.gov/regulations/pdf/20230329_final_regs_text.pdf ; https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/dealing-requests-individuals_en
- **Depends on:** privacy-laws, audit-trails
- **Feeds into:** compliance-audit, age-requirements

## When to use / Do NOT use

- **Use when:** building or reviewing the flows for access, export, rectification, erasure, restriction, or objection requests; wiring the request log, response clocks, or processor deletion instructions; testing the intake path.
- **Do NOT use when:** the question is which rights apply in a market at all (use privacy-laws to derive the obligations register first), or a request raises a contested exemption or a novel legal call — stop and require qualified counsel; this skill is implementation guidance, not legal advice.

## Rules

1. **LG-041 — Lifecycle as a state machine.** Every request moves through recorded states: received → identity verified → in progress → delivered / refused / closed. A request that exists only in an inbox or a chat thread is not being handled; it is being lost.
2. **LG-042 — Two intake channels minimum.** The product offers at least two ways to submit a request (for example an in-product flow and a published email address), and neither forces account creation beyond what the applicable regime permits; an account holder may be routed through the account, a non-account requester may not be forced to create one.
3. **LG-043 — Clock starts at receipt, from configuration.** The receipt timestamp is written by the system when the request arrives, and the response deadline is computed from the regime table in the project file (window, extension length, extension-notice rule) — never hardcoded in code or prose, and never tracked in a person's calendar.
4. **LG-044 — Aging alerts at 50% and 80%.** The request log raises an alert when an open request passes 50% and 80% of its configured window without a recorded outcome; an extension is valid only if its notice was sent inside the original window and the notice event is logged.
5. **LG-045 — Proportionate identity verification.** Verification matches the sensitivity of what the request exposes: an authenticated session suffices for an in-account export; a request arriving by email is verified through a channel the account already trusts. Never collect more personal data to verify than the request itself would expose, and never ask for identity documents by default.
6. **LG-046 — Unverifiable means refused with reasons, not dropped.** If identity cannot be verified proportionately, the request is refused in writing, stating the reason and the route to complain to the supervisory authority or regulator named in the project file, and the refusal is logged like any other outcome.
7. **LG-047 — Search covers every store.** Fulfilment searches the primary database, search indexes, analytics stores, file storage, and every processor listed in the processor register that holds the subject's data. An export assembled from the main database alone is incomplete by construction.
8. **LG-048 — Export is the subject's real records, in a usable format.** Delivery is a machine-readable export (for example JSON or CSV plus human-readable copies) generated from the subject's actual records at fulfilment time. A template, a screenshot of the profile page, or a hand-written summary is not an export.
9. **LG-049 — Rectification writes through.** A correction updates the record in the primary store and propagates to derived stores and processors that hold the same field; the requester can see the corrected value in the product afterwards. A note appended to a ticket while the record stays wrong is not rectification.
10. **LG-050 — Erasure executes; it never hides.** Erasure deletes or irreversibly anonymizes the subject's records in the primary store, search indexes, analytics, and file storage, sets the profile unrecoverable (not flagged invisible), and instructs every processor to delete, filing each processor's confirmation with the request record.
11. **LG-051 — Backups follow the documented rotation.** Where backups cannot be edited in place, the erased subject is access-suppressed immediately and deleted when the backup rotates, per the retention schedule recorded in the project file; the suppression entry is part of the request record, so a restore cannot silently resurrect the data without the suppression being re-applied.
12. **LG-052 — Every request is logged with its outcome.** The request log records requester reference, request type, channel, receipt timestamp, verification method, deadline, extension notices, delivery or refusal, processor confirmations, and closure date, retained for at least the period the applicable regime's row in the project file specifies. If it is not logged, it did not happen.

## BAN list

- **BAN-LG-021 — Delete that only hides.** Banned: a "Delete account" or erasure flow that sets a hidden/deactivated flag while the subject's records remain queryable in the database, indexes, or admin views. Defeats: DET-FAKE-011. Bad: `UPDATE users SET visible = false` followed by a "Your account has been deleted" confirmation screen. Instead: execute LG-050 erasure across all stores and prove it with the residue query in G-LG-021. Severity: BLOCK.
- **BAN-LG-022 — Export that fabricates the file.** Banned: a download/export button that returns a static template, sample data, or a file generated from anything other than the requesting subject's live records. Defeats: DET-FAKE-019. Bad: "Download my data" serves a pre-built `export-sample.json` with placeholder fields for every user. Instead: generate the export from the subject's records at fulfilment time under LG-048. Severity: BLOCK.
- **BAN-LG-023 — Request form that submits nowhere.** Banned: a privacy-request form or "contact us about your data" page whose submissions are stored nowhere, emailed to an unmonitored address, or acknowledged without creating a logged request with a clock. Defeats: DET-FAKE-015. Bad: the form shows "Request received" but writes only to a spreadsheet nobody owns. Instead: submission creates the state-machine record under LG-041 and starts the clock under LG-043. Severity: BLOCK.
- **BAN-LG-024 — Verification that harvests.** Banned: demanding identity documents, selfies, or new personal data disproportionate to the request — for example requiring a passport scan to export a newsletter subscription record. Defeats: DET-NONE — no DET parameter names this signal; pattern owned by this skill. Bad: the export flow's first step is "upload government ID" for an account that holds only an email address and preferences. Instead: verify proportionately under LG-045 through channels the account already trusts. Severity: BLOCK.
- **BAN-LG-025 — Silent deadline slip.** Banned: letting a request pass its configured deadline, or extending it, without the extension notice and logged reason the regime table requires. Defeats: DET-NONE — no DET parameter names this signal; pattern owned by this skill. Bad: a request sits for seven weeks; the requester is told "still processing" only after they chase twice. Instead: aging alerts fire under LG-044 and any extension notice is sent inside the original window and logged under LG-052. Severity: BLOCK.

## Gates

- **G-LG-021 — DSAR drill (access + erasure).** Verifies: LG-047, LG-048, LG-050, LG-051. Check (automated): create a test account with known records in the database, search index, and analytics store; submit an access request and then an erasure request through the real product flow; assert (a) the export contains every known test record, and (b) after erasure, residue queries against the database, index, analytics store, and admin views return zero rows for the test subject, and the backup-suppression entry exists. Pass: both assertions hold. Fail: block shipment. Recorded in: progress.md.
- **G-LG-022 — Clock and aging check.** Verifies: LG-043, LG-044. Check (automated): query the request log for open requests; each must carry a receipt timestamp and a deadline computed from the regime table, and a test request seeded at 85% of its window must appear in the aging-alert output. Pass: zero open requests without a computed deadline; seeded request alerts. Fail: block shipment. Recorded in: progress.md.
- **G-LG-023 — Intake-path test.** Verifies: LG-041, LG-042. Check (automated + manual): submit one test request through each published intake channel; each must create a logged state-machine record with a receipt timestamp within the same session, and the confirmation shown to the requester must match the logged record's reference. Pass: every channel produces a logged, clocked record. Fail: block shipment — a broken intake path is a compliance failure, not a UX bug. Recorded in: progress.md.
- **G-LG-024 — Request-log completeness audit.** Verifies: LG-046, LG-052. Check (manual): sample the last ten closed requests (or all, if fewer); each record must show verification method, outcome (delivered or refused with reasons and complaint route), processor confirmations for erasures, and closure date, and the log's retention setting must meet the regime table's minimum. Pass: zero incomplete records. Fail: block shipment until the log is remediated. Recorded in: progress.md.

## Anti-patterns

- **Inbox as the system of record.** Requests are "handled" from a shared mailbox with no log, so nobody can say how many are open or late. Catch it by asking for the open-request count — if it requires reading email, the state machine does not exist.
- **One-store confidence.** The export looks complete because it came from the main database, while the analytics tool and the search index quietly keep their copies. Catch it by comparing the export's sources against the processor register, store by store.
- **Deadline known by one person.** The clock lives in a team member's head or personal calendar; their holiday becomes a breach. Catch it by checking whether the deadline survives in the log with no human attached.
- **Helpful over-collection.** Support asks for "a bit more ID, just to be safe" on every request, slowly building an identity-document store nobody registered. Catch it by sampling verification evidence against what each request type actually exposes.

## Examples

- [Example 1 — The delete that only hid](examples/example-1.md) — violates/corrects LG-050.
- [Example 2 — The export that wasn't](examples/example-2.md) — violates/corrects LG-048.
- [Example 3 — The request nobody clocked](examples/example-3.md) — violates/corrects LG-043, LG-052.

## Recall anchors

- If it is not logged, it did not happen.
- The clock starts at receipt and lives in the system, not in a calendar.
- Verify proportionately — never harvest identity to prove identity.
- Erasure is proven by absence, not by a confirmation screen.
- An export is the subject's real records, generated when asked.

## Checklist

- [ ] Both intake channels create logged, clocked requests (LG-041, LG-042, G-LG-023).
- [ ] Deadlines compute from the regime table in the project file — no hardcoded windows (LG-043).
- [ ] Aging alerts fire at 50% and 80% of the window (LG-044, G-LG-022).
- [ ] Verification method per request type is proportionate and documented (LG-045).
- [ ] Refusals state reasons and the complaint route, and are logged (LG-046).
- [ ] DSAR drill passes: complete export, zero post-erasure residue (LG-047–LG-051, G-LG-021).
- [ ] Sampled closed requests have complete log records, including processor confirmations (LG-052, G-LG-024).
