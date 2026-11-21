# support-ticketing

## Metadata

- **Owner department:** D18 Customer Experience (CX)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://developer.zendesk.com/api-reference/ticketing/tickets/tickets ; https://www.intercom.com/help/en/articles/732390-set-your-default-office-hours ; https://www.intercom.com/help/en/articles/732436-share-your-expected-response-time
- **Depends on:** none — standalone: intake channels, ticket fields, statuses, and SLA targets are configured from the operator's own support commitments and tooling, set directly; no other skill's output is an input. It feeds in-app-chat and feedback-loops.
- **Feeds into:** in-app-chat, feedback-loops

## When to use / Do NOT use

- **Use when:** setting up or auditing any support intake channel (email address, web form, chat escalation, API); writing public copy that states support hours or response times; configuring ticket fields, statuses, SLA targets, or closure behavior.
- **Do NOT use when:** the work is the chat widget's own behavior (use in-app-chat — its escalations land here as tickets), self-service articles (use help-center), or post-resolution surveys (use feedback-loops).

## Rules

1. **CX-001 — One intake, one queue.** Every support channel — email, web form, chat escalation, API — creates a ticket in the single ticketing system. A channel that cannot create a ticket is not launched as a support channel.
2. **CX-002 — Required fields at creation.** Every ticket carries requester, assignee or unassigned-queue marker, priority, type, and tags at creation. A ticket missing requester or type is a configuration defect, not an agent error.
3. **CX-003 — One defined lifecycle.** Tickets move only through the defined statuses (New → Open → Pending → Solved → Closed). A new status is added only by a recorded configuration change, never improvised per ticket.
4. **CX-004 — Immediate acknowledgment with reference.** Ticket creation triggers an automatic acknowledgment to the requester containing the ticket reference the customer can quote. The reference resolves to that ticket in the system and in the customer's own request view.
5. **CX-005 — Promises come from configuration.** Every published response-time or support-hours statement equals the SLA and office-hours values configured in the ticketing tool. Copy states no number the tool is not configured to measure against.
6. **CX-006 — No unstaffed promises.** If no SLA is staffed, public copy states the operator's actual support hours and days instead of a response-time number. "24/7 support" appears only when a staffed rota covering those hours exists in the configuration.
7. **CX-007 — SLA targets from real hours.** SLA targets are set per priority from the hours the operator actually works. A target the operator's real schedule cannot meet is never configured, however good it would look in copy.
8. **CX-008 — Public replies and internal notes are separate.** Public replies and internal notes are distinct fields; internal notes are never customer-visible, and the customer-facing view is re-checked after any template, permission, or field change.
9. **CX-009 — The customer can track their ticket.** From the acknowledgment reference, the customer can view their own ticket's current status and the public reply history. A ticket the customer cannot track fails the intake test.
10. **CX-010 — Solved is not Closed.** On resolution the ticket moves to Solved and the customer receives a resolution notice stating a reopen window. It moves to Closed only when the customer confirms resolution or the stated window lapses with no reply.
11. **CX-011 — Triage by priority and age.** Incoming tickets are worked from queue views ordered by priority, then age. No ticket remains in New past the configured first-response target without a named owner.
12. **CX-012 — Configuration changes are retested.** Any change to intake forms, triggers, SLA values, or office hours reruns the end-to-end intake test (G-CX-001) and the copy-vs-config diff (G-CX-002) before it goes live.

## BAN list

- **BAN-CX-001 — Dead-end intake.** Banned: a contact form or support address that stores nothing, sends nothing, and notifies nobody while remaining live. Defeats: DET-CON-028. Bad: the Contact page form posts to an endpoint that discards submissions, under copy reading "We reply within 24 hours." Instead: wire the form to create a ticket with an automatic acknowledgment (CX-001, CX-004), or remove the form and the claim. Severity: BLOCK.
- **BAN-CX-002 — Placeholder or unmonitored support address.** Banned: publishing a support address that is a placeholder (support@example.com) or routes to an inbox nobody reads. Defeats: DET-CON-005. Bad: the footer lists help@example.com, which bounces, while the real inbox is an unlisted personal account. Instead: publish only addresses that create tickets in the system (CX-001) and pass the end-to-end intake test (G-CX-001). Severity: BLOCK.
- **BAN-CX-003 — Promise that differs from the configuration.** Banned: public copy stating response times or support hours that differ from the SLA and office-hours values configured in the tool. Defeats: DET-CON-014. Bad: the pricing page promises "replies within 1 hour" while the tool's configured first-response SLA is 24 hours on weekdays. Instead: set the configuration first, then copy its values verbatim (CX-005, CX-007). Severity: BLOCK.
- **BAN-CX-004 — Invented support metrics.** Banned: publishing measured-sounding support figures — average response time, satisfaction percentage — that no ticketing or survey system produces. Defeats: DET-CON-011. Bad: the support page claims "Average response: 12 minutes · 98% customer satisfaction" with no SLA reporting or CSAT survey behind either number. Instead: publish only figures the configured systems actually report, or publish no figure (CX-005). Severity: BLOCK.
- **BAN-CX-005 — Silent close.** Banned: moving a ticket to Closed at resolution with no resolution notice and no reopen path for the customer. Defeats: DET-CON-028. Bad: an agent marks a ticket Closed after fixing the issue; the customer's first news is the survey email, and their reply opens a new, unlinked ticket. Instead: move to Solved, send the resolution notice with the stated reopen window, and close only on confirmation or lapse (CX-010). Severity: BLOCK.

## Gates

- **G-CX-001 — End-to-end intake test.** Verifies: CX-001, CX-004, CX-009. Check (automated): a scripted smoke test submits a test request from an external address through each intake channel and asserts: a ticket is created with a reference ID, the acknowledgment arrives at the requester address containing that reference, the ticket appears in the agent queue, a test reply reaches the requester, and the customer status view shows the ticket. Run on launch and on every support-config change. Pass: every assertion true for every channel. Fail: block shipment. Recorded in: progress.md.
- **G-CX-002 — Copy-vs-config diff.** Verifies: CX-005, CX-006, CX-007. Check (automated): grep all public copy for response-time and availability statements (patterns: "within", "24/7", "business hours", "response time" near "support"/"reply"/"respond") and diff each stated value against the SLA and office-hours values exported from the ticketing tool's configuration. Pass: every published value equals a configured value, and no 24/7 claim exists without a covering rota. Fail: block shipment. Recorded in: progress.md.
- **G-CX-003 — Field and lifecycle audit.** Verifies: CX-002, CX-003. Check (automated): query the ticketing API for all tickets created in the last 30 days; assert every ticket has requester, priority, and type set, and a status inside the defined lifecycle set. Pass: zero tickets missing a required field or carrying an undefined status. Fail: block shipment until the intake configuration is fixed and the audit re-runs clean. Recorded in: progress.md.
- **G-CX-004 — Visibility separation test.** Verifies: CX-008. Check (automated): on a test ticket, add an internal note containing a unique marker string, then load every customer-visible surface — the customer's ticket view, the acknowledgment, and a status email — and search each for the marker. Pass: the marker appears on no customer-visible surface. Fail: block shipment. Recorded in: progress.md.
- **G-CX-005 — Solved-to-Closed flow test.** Verifies: CX-010. Check (automated): scripted test resolves a test ticket and asserts: a resolution notice is sent to the requester, the ticket sits in Solved rather than Closed, a requester reply inside the window returns it to Open, and it reaches Closed only after requester confirmation or window lapse. Pass: every transition behaves as specified. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **Reply from a personal inbox.** An agent answers from their own email instead of from the ticket, so the thread leaves the record and the next agent starts blind. Catch it by sampling closed tickets for resolutions whose replies exist only outside the system.
- **Note in the reply box.** Internal commentary ("customer is confused again") drafted in the public reply field, one misclick from being sent. Catch it by checking the field label before typing — internal text starts in the notes field from the first keystroke.
- **Priority inflation.** So many tickets are marked Urgent that the priority field stops meaning anything and triage quietly becomes first-come-first-served. Catch it by reviewing the priority distribution on a fixed cadence; a top priority holding a large share of volume means the triage rules are not being applied.
- **Zombie New queue.** Tickets sit in New because the working view sorts by newest first and older tickets scroll out of sight. Catch it by keeping the triage view sorted by age within priority and surfacing any ticket older than the first-response target without an owner.

## Examples

- [Example 1 — The form that went nowhere](examples/example-1.md) — violates/corrects CX-001, CX-004 (BAN-CX-001).
- [Example 2 — "24/7 support" from a one-person operation](examples/example-2.md) — violates/corrects CX-005, CX-006 (BAN-CX-003).
- [Example 3 — Closed without a word](examples/example-3.md) — violates/corrects CX-010 (BAN-CX-005).

## Recall anchors

- If it doesn't create a ticket, it isn't a support channel.
- The promise is a configuration value, not copy.
- Every submission gets a reference the customer can quote.
- Internal notes never face the customer.
- Solved is not Closed — the customer closes the loop.

## Checklist

- [ ] Every intake channel creates a ticket in the one system (CX-001, G-CX-001).
- [ ] The acknowledgment is automatic, immediate, and carries the ticket reference (CX-004, G-CX-001).
- [ ] The customer can view their ticket's status from the reference (CX-009, G-CX-001).
- [ ] Every published response-time and hours statement matches the configured SLA and office hours (CX-005, G-CX-002).
- [ ] No 24/7 or response-time claim exists without staffing behind it (CX-006, CX-007).
- [ ] Required fields and lifecycle statuses verified on recent tickets (CX-002, CX-003, G-CX-003).
- [ ] Internal notes proven invisible on every customer surface (CX-008, G-CX-004).
- [ ] Solved → resolution notice → reopen window → Closed flow tested end to end (CX-010, G-CX-005).
