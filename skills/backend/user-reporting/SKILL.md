# user-reporting

## Metadata

- **Owner department:** D4 Backend & APIs (BE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Trust & Safety Professional Association curriculum, content moderation simulation — https://www.tspa.org/curriculum/ts-curriculum/content-moderation-simulation/
- **Depends on:** api-building, backend-auth
- **Feeds into:** content-moderation, admin-tools

## When to use / Do NOT use

- **Use when:** users can see or affect each other's content, accounts, or messages — every such surface needs a reporting intake whose records a moderation queue can actually work. This skill owns the intake and the record.
- **Do NOT use when:** the work is queue operations or enforcement policy itself — that is D7's content-moderation, consuming the records this skill creates. The staff surface that displays the queue is admin-tools. Do not substitute a contact form or a support inbox for a reporting channel.

## Rules

1. **BE-141 — A report is a record.** Every report action writes a structured record — reporter, target (content or account), category, context snapshot, timestamp — before any confirmation is shown to the reporter.
2. **BE-142 — In-product, per item.** Every user-generated surface offers a report action on the item and on the account. A generic contact page is not a reporting channel.
3. **BE-143 — The reporter stays anonymous.** The reported party never learns who reported them — not in a notification, not in an appeal, not in any surface.
4. **BE-144 — Severe categories jump the queue.** Child safety, credible threats, and illegal material route to the escalation path immediately, ahead of arrival order. Nothing severe waits behind spam flags.
5. **BE-145 — Every report reaches a decision.** A report moves through visible states (received → under review → decided) and cannot silently expire. Aging past the tier's SLA is surfaced by the queue-aging check, never absorbed quietly.
6. **BE-146 — Decisions cite policy.** Every enforcement action (label, reduce, remove, suspend, ban) records the policy clause it rests on, the deciding actor, and the timestamp.
7. **BE-147 — Actions are appealable.** The sanctioned user can appeal from the notice they receive; the appeal re-enters the queue as a fresh review of the same record.
8. **BE-148 — The reporter gets closure, not detail.** The reporter receives a received/decided signal. Enforcement specifics are never disclosed to the reporter.
9. **BE-149 — Reports are data.** Report records are queryable, so repeat-offender patterns and coordinated-reporting (brigading) patterns are computed from them. A sudden spike against one target is reviewed as a pattern before mass enforcement.
10. **BE-150 — Context is snapshotted.** The reported content is captured as it stood at report time. Editing or deleting the original afterward cannot erase the evidence under review.
11. **BE-151 — Intake validates the target.** The target is resolved and authorized server-side at intake: it must exist and be visible to the reporter. Reports against nonexistent or invisible targets are rejected, never queued.

## BAN list

- **BAN-BE-071 — The dead report button.** Banned: a report action that writes nothing, or sends an email to an unmonitored inbox, while showing "Thanks, we will review this." Defeats: DET-FAKE-015. Bad: the report dialog confirms submission; no table, queue, or monitored inbox anywhere receives it. Instead: persist the structured record (BE-141) and route it to the moderation queue before confirming to the reporter. Severity: BLOCK.
- **BAN-BE-072 — Phantom enforcement.** Banned: marking a report "actioned — user banned" in the queue while no enforcement is applied to the account. Defeats: DET-FAKE-010. Bad: a moderator clicks Ban, the toast says done, and the account posts again an hour later. Instead: enforcement calls the same account service the product uses, and the report can close only after the account's new state is verified. Severity: BLOCK.
- **BAN-BE-073 — Unvalidated report targets.** Banned: creating a report from a client-supplied target ID without verifying the target exists and is visible to the reporter. Defeats: DET-CODE-019. Bad: a script files 500 reports against random UUIDs and three against a rival's listing by guessed ID, flooding the queue and manufacturing a "pattern". Instead: resolve and authorize the target server-side at intake (BE-151); reject what the reporter cannot see. Severity: WARN.
- **BAN-BE-074 — Silent report expiry.** Banned: reports auto-closing or dropping off the queue when they age, with no decision recorded. Defeats: DET-FAKE-011. Bad: a nightly job deletes undecided reports older than 30 days; reporters were told a review would happen. Instead: undecided reports age into escalation (BE-145); a report leaves the queue only through a recorded decision. Severity: BLOCK.

## Gates

- **G-BE-071 — End-to-end report trace.** Verifies: BE-141, BE-145, BE-146. Check: automated in staging — file a report as a test user, read the record back from the queue store, record a decision with a policy citation, and assert the reporter's closure signal exists. Pass: record, decision, citation, and closure all present. Fail: block shipment. Recorded in: progress.md.
- **G-BE-072 — Forged-target rejection test.** Verifies: BE-151. Check: automated — submit reports against a random UUID and against a real record the reporter cannot see. Pass: both rejected, no queue records created. Fail: block shipment. Recorded in: progress.md.
- **G-BE-073 — Queue-aging check.** Verifies: BE-145. Check: automated — seed staging with an undecided report older than its tier SLA and run the aging query. Pass: the report is flagged and escalated, not deleted or ignored. Fail: block shipment. Recorded in: progress.md.
- **G-BE-074 — Severity-routing test.** Verifies: BE-144. Check: automated — file a spam report, then a child-safety report; read the escalation queue. Pass: the severe report is routed to escalation first, ahead of the earlier spam report. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **The warm black hole.** The UI thanks the reporter warmly and the record exists — but the queue view is a page no one has opened since launch. Catch it: check the queue's last-reviewed timestamp; a reporting feature with no reviewer is a promise nobody keeps.
- **Category soup.** Dozens of free-text categories, so every pattern query returns noise and nothing aggregates. Catch it: list the distinct categories in the last month of reports; free-text entries are the tell.
- **Enforcement by vibes.** Decisions recorded as "handled" with no policy cited, leaving appeals and audits nothing to check. Catch it: sample decided reports; a decision without a policy clause fails BE-146 on sight.
- **Retaliation blindness.** A brigading wave against one user is actioned report-by-report, punishing the campaign's target. Catch it: before enforcing on a target with a sudden report spike, open the pattern view (BE-149) — the spike is evidence about the reporters, not only the reported.

## Examples

- [Example 1 — A report button that writes the record](examples/example-1.md) — corrects BE-141.
- [Example 2 — Severity routing at intake](examples/example-2.md) — corrects BE-144.
- [Example 3 — A decision with a policy citation and closure](examples/example-3.md) — corrects BE-146.

## Recall anchors

- A report is a record, not an email.
- The reported party never learns who reported.
- Severe categories jump the queue, always.
- No decision without a policy citation.
- Every report ends decided — never expired, never deleted.

## Checklist

- [ ] Every user-generated surface has a per-item and per-account report action (BE-142).
- [ ] End-to-end report trace passes in staging (G-BE-071).
- [ ] Forged and invisible targets are rejected at intake (G-BE-072).
- [ ] Severe categories route to escalation immediately (G-BE-074).
- [ ] Decisions cite policy and sanctions are appealable (BE-146, BE-147).
- [ ] The reporter receives closure without enforcement detail (BE-148).
- [ ] The aging check flags overdue reports for escalation; none expire silently (G-BE-073).
