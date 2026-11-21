# audit-trails

## Metadata

- **Owner department:** D14 Legal & Privacy (LG)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng/ ; https://cppa.ca.gov/regulations/pdf/20230329_final_regs_text.pdf
- **Depends on:** privacy-laws, logging
- **Feeds into:** compliance-audit, dsar-handling, cookie-consent, legal-documents, clone-ethics

## When to use / Do NOT use

- **Use when:** building or reviewing the record of regulated actions — consent grants and withdrawals, policy acceptances, DSAR lifecycle events, data exports, refunds and billing adjustments, admin access to personal data, permission changes, and D14 rights/authorization decisions — including the trail store's integrity, access control, and retention.
- **Do NOT use when:** the record is application telemetry — request logs, error traces, performance metrics (that is D12's logging skill; this skill owns only the compliance-grade record of who did what to regulated data and systems), or the question is whether an action was lawful in the first place (derive that in privacy-laws; the trail records the basis, it does not create it). This skill is implementation guidance, not legal advice.

## Rules

1. **LG-161 — The regulated-action inventory is explicit.** The project file lists every action type that must write a trail entry — at minimum: consent grant/withdrawal, policy acceptance, DSAR receipt/extension/delivery/refusal/closure, data export, refund and billing adjustment, admin access to personal data, permission or role change, and each D14 rights/authorization decision (including clone-ethics records). An action type not on the list is a coverage gap to close, not an exemption.
2. **LG-162 — The entry is written in the same flow as the action.** The trail entry is created inside the transaction or service call that performs the action, so the action cannot complete without its entry. An action that "happened but has no entry" is treated as not having validly happened, and the flow surfaces the failure instead of proceeding silently.
3. **LG-163 — Every entry is complete.** Each entry carries: actor (user, admin, or system process, with role), action, subject/target (whose data or which record), trusted timestamp, and the basis reference — the document version accepted, the consent scope granted, the register row or rule the decision applied, and the approver where one exists. An entry missing any field fails G-LG-081.
4. **LG-164 — Entries are append-only.** No entry is ever edited or deleted in place. A correction is a new entry that references the original entry's ID, states what was wrong, and carries its own actor and timestamp; both entries remain readable.
5. **LG-165 — The store is tamper-evident.** Entries are protected by append-only storage plus hash-chaining (each entry's hash covers the previous entry's hash) or WORM storage where the risk warrants; the application role holds no UPDATE or DELETE grant on the trail store. Integrity is verified on a schedule under G-LG-083, not assumed.
6. **LG-166 — Timestamps come from a trusted server clock.** Entry times are written by the server at the moment of the action. A client-supplied time (from a browser, a form, or an imported record) is stored, if at all, as a labeled claim field — never as the entry's timestamp.
7. **LG-167 — The basis is recorded, not just the outcome.** A decision entry names the rule, register row, or approval it rests on (for example "rights decision: replace, approved per clone-ethics record REF-EXAMPLE-04"). An outcome with no basis is an incomplete entry and fails audit sampling.
8. **LG-168 — Access to the trail is itself trailed.** Reading, searching, or exporting the trail writes a trail entry naming the reader and the query scope. Trail read access is limited to the named roles in the project file; the trail is never exposed through a general admin screen or an unauthenticated endpoint.
9. **LG-169 — The trail has its own retention schedule.** Each entry category is retained for the period its obligation specifies in the project file (for example, CCPA request records at least 24 months; consent records for as long as the processing they justify continues, plus the limitation period the register names) and purged on schedule — never earlier, and never kept indefinitely by default.
10. **LG-170 — The trail is personal data and is treated as such.** The trail sits inside the data inventory with access control and minimisation applied: entries record references and identifiers needed for accountability, not copies of the underlying personal data. How a DSAR reaches the trail, and how erasure interacts with trail retention duties, is resolved per regime in the project file — never improvised per request.
11. **LG-171 — Trail health is reviewed on a cadence.** On the schedule compliance-audit sets, a reviewer samples entries against real actions (a refund in the billing system, a closed DSAR, a consent withdrawal) and confirms each has a complete, correctly based entry; every gap becomes a finding with an owner and a remediation date.
12. **LG-172 — No claim outruns the trail.** Product copy, sales material, and audit answers may claim only the recording the trail actually performs ("every refund is logged with actor and reason" only if refunds are on the LG-161 inventory and pass G-LG-081). A claim with no passing gate behind it is removed, not softened.

## BAN list

- **BAN-LG-081 — Trail kept in ephemeral logs.** Banned: regulated actions recorded only in application console output, a rotating log file, or an analytics event stream that ages out — anywhere the record can vanish with a restart or a retention default. Defeats: DET-INF-013. Bad: consent withdrawals are visible via `console.log("consent withdrawn", userId)` and unrecoverable after the host's 7-day log rotation. Instead: write the entry to the append-only trail store in the same flow as the action, under LG-162 and LG-165. Severity: BLOCK.
- **BAN-LG-082 — History edited in place.** Banned: UPDATE or DELETE statements against existing trail entries — to fix a typo, reassign an actor, tidy a timestamp, or remove an embarrassing decision. Defeats: DET-CON-028. Bad: an admin runs `UPDATE audit_log SET actor = 'system' WHERE id = 1042` so a manual refund looks automated. Instead: leave the original untouched and append a correction entry referencing it, under LG-164. Severity: BLOCK.
- **BAN-LG-083 — Trail readable by anyone, reads unrecorded.** Banned: a trail viewer, export, or API route available to all staff accounts (or worse, unauthenticated), whose reads write no entry — so the most sensitive metadata in the product can be browsed invisibly. Defeats: DET-INF-021. Bad: `/admin/audit` renders for every support login and logs nothing when opened. Instead: restrict reads to the named roles and trail every read under LG-168. Severity: BLOCK.
- **BAN-LG-084 — Backfilled trail presented as contemporaneous.** Banned: reconstructing entries after the fact — from tickets, chat, or memory — and storing them with the action's original date as if they were written when the action happened. Defeats: DET-CON-014. Bad: after an incident, a week of admin data accesses is "rebuilt" into the trail with last week's timestamps. Instead: record the reconstruction honestly — entries carry the true write time, name the source they were reconstructed from, and the gap itself is filed as a finding under LG-171. Severity: BLOCK.
- **BAN-LG-085 — Retention shorter than the recorded schedule.** Banned: a purge job, storage tier, or vendor default that deletes trail categories before the period the project file records for them — for example request records destroyed at 90 days where the applicable regime's row requires at least 24 months. Defeats: DET-CON-015. Bad: the privacy notice promises request records are kept for two years while the trail store's lifecycle policy expires them in a quarter. Instead: set purge rules per category from the schedule under LG-169 and verify them under G-LG-085. Severity: BLOCK.

## Gates

- **G-LG-081 — Action-coverage test.** Verifies: LG-161, LG-162, LG-163, LG-167. Check (automated): in staging, perform each action type on the LG-161 inventory — accept a policy version, grant and withdraw consent, file/extend/deliver/close a DSAR, export data, issue a refund, open a subject's record as an admin, change a permission, record a rights decision — then query the trail and assert exactly one complete entry per action with actor, action, subject, server timestamp, and basis reference populated. Pass: zero missing or incomplete entries. Fail: block shipment. Recorded in: progress.md.
- **G-LG-082 — Tamper test.** Verifies: LG-164, LG-165. Check (automated): in a staging copy of the trail, (a) attempt UPDATE and DELETE on an existing entry using the application role's credentials — both must be denied; (b) modify one historical entry's field directly at the storage layer, then run the integrity verification — the modification must be detected and located. Pass: writes denied and the planted modification flagged. Fail: block shipment. Recorded in: progress.md.
- **G-LG-083 — Integrity verification job.** Verifies: LG-165. Check (automated): a scheduled job recomputes the hash chain (or verifies WORM attestations) across the full trail and reports any gap, break, or sequence anomaly; the job's own result is filed with its run date. Pass: chain verifies end to end with zero anomalies. Fail: block shipment and raise an incident — a broken chain is treated as a security event, not a data-quality note. Recorded in: progress.md.
- **G-LG-084 — Trail-access audit.** Verifies: LG-168, LG-170. Check (automated + manual): open the trail viewer and run a search and an export as an authorized role, and attempt the same as an unauthorized role; assert the authorized reads each produced a trail entry naming reader and scope, the unauthorized attempts were refused, and the current role list matches the project file. Pass: all reads trailed, all unauthorized access refused, role list exact. Fail: block shipment. Recorded in: progress.md.
- **G-LG-085 — Retention conformance check.** Verifies: LG-169. Check (automated): for each entry category, compare the oldest surviving entry's age and the store's purge configuration against the schedule in the project file; assert no category is purged before its recorded period and every category has a purge rule. Pass: zero early purges and zero categories without a rule. Fail: block shipment until configuration matches the schedule. Recorded in: progress.md.

## Anti-patterns

- **Audit theater.** A beautiful trail dashboard exists, but half the regulated actions never write to it because they were built before the trail was. Catch it by picking three real actions from the last week — not from the inventory document — and searching for their entries.
- **The log that logs everything except decisions.** Technical events are captured in detail while approvals, refusals, and rights calls live in chat threads. Catch it by sampling decision-type entries specifically; they are the ones an auditor asks for first.
- **One giant retention.** Every category is set to "keep forever" to avoid thinking about schedules — which quietly turns the trail into an unbounded personal-data store. Catch it by checking whether any category has a purge rule that has ever actually run.
- **Timestamps that agree too well.** Entries for a messy real-world process all land on round hours or in perfect sequence days later — the signature of backfill. Catch it by plotting entry write times against the actions they claim to record.

## Examples

- [Example 1 — The refund nobody recorded](examples/example-1.md) — violates/corrects LG-162, LG-163.
- [Example 2 — The entry that got "fixed"](examples/example-2.md) — violates/corrects LG-164, LG-165.
- [Example 3 — The trail everyone could read](examples/example-3.md) — violates/corrects LG-168.

## Recall anchors

- If it is not in the trail, it did not validly happen.
- Append-only: corrections are new entries, never edits.
- The trail records the basis, not just the outcome.
- Reading the trail is a trailed act.
- D12 logs the machine; this trail answers for the humans and the system acting on regulated data.

## Checklist

- [ ] The LG-161 inventory lists every regulated action type, including rights/authorization decisions (LG-161).
- [ ] Entries are written in the same flow as the action and are complete: actor, action, subject, timestamp, basis (LG-162, LG-163, LG-167, G-LG-081).
- [ ] The store denies UPDATE/DELETE to the application role and the tamper test detects a planted edit (LG-164, LG-165, G-LG-082).
- [ ] The integrity verification job runs on schedule and its results are filed (LG-165, G-LG-083).
- [ ] Timestamps are server-written; client times, if kept, are labeled claims (LG-166).
- [ ] Trail reads are role-restricted and themselves trailed (LG-168, G-LG-084).
- [ ] Every category has a retention period and a working purge rule matching the project file (LG-169, G-LG-085).
- [ ] The trail is in the data inventory, minimised, with per-regime DSAR/erasure treatment recorded (LG-170).
