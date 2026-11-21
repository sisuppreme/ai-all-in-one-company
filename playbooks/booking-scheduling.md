# Playbook — Booking & Scheduling

## Goal

Build a booking system where the schedule itself is the product: resources (people, rooms, equipment, tables) with real availability, slot holds, confirmed bookings, reminders, and cancellation/no-show flows — with a hard guarantee that a resource can never be double-booked, even under retries, races, or duplicate submits.

Modeled on the SaaS playbook (§5.6), with scheduling state promoted to a first-class design problem: availability is computed from constraints, never stored as a hand-edited calendar.

## Departments + order

Step 0 (always-on core) → D1 → D2+D7 → D3+D13+D4+D5 → D11 (if deposits/prepayment) → D14 → D12 → D7+D8 → D6 → D9

Modeled on the SaaS order; D14 and D12 are explicit steps because a booking system holds personal data and its availability queries are its hottest read path.

## Skills to load

Load this playbook's bundle first: `bundles/booking-scheduling.md`. Then, per step:

Key skills (§5.6, assigned in the Phase 6 defect loop — DR-04): `requirements-writing`, `system-design`, `frontend-core`, `api-building`, `schema-design`, `payments`, `ci-cd`.

| Skill | Bundle |
|---|---|
| project-templates, progress-tracking | `bundles/core.md` |
| secrets-management, qa-gates | `bundles/core.md` |
| requirements-writing, fact-sheet | `bundles/product-requirements.md` |
| system-design | `bundles/architecture.md` |
| frontend-core, forms | `bundles/frontend.md` |
| accessibility-audit, wcag | `bundles/accessibility-i18n.md` |
| api-building, queues-jobs, notifications | `bundles/backend.md` |
| schema-design, migrations | `bundles/database.md` |
| payments, transactional-email, sms | `bundles/integrations-payments.md` |
| privacy-laws, legal-documents | `bundles/legal-privacy.md` |
| performance-budgets | `bundles/analytics-observability.md` |
| owasp, auth-hardening | `bundles/security.md` |
| placeholder-scan | `bundles/qa-testing.md` |
| ci-cd, hosting | `bundles/devops-deployment.md` |
| technical-seo, structured-data (public booking pages) | `bundles/seo-content.md` |

Conditional: payments applies only when bookings take a deposit or full prepayment — if booking is free/reserve-only, drop D11's payments and keep transactional-email/sms for confirmations. If the product adds AI features (smart scheduling suggestions), add a D17 step before D7+D8. If it ships customer support surfaces, add a D18 step (help-center, user-onboarding) before D9.

## Docs to write first

1. `fact-sheet.md` — the scheduling facts, all owner-supplied: business hours, slot length, buffer rules, cancellation window and fees, no-show policy, reminder timing. **No policy number is invented** — a cancellation fee the owner never set does not appear in copy or code.
2. Availability model note — resources, their calendars, the source of truth for time (all times stored in UTC; display in the resource's timezone; the customer's timezone is a display concern, never a storage one).
3. `stack.md` — stack and (if applicable) payment provider.
4. `progress.md` — playbook trace and gate results.

## Step-by-step sequence

0. **Always-on core.** Load `bundles/core.md`; project files, `progress.md`, secrets baseline.
1. **D1 requirements.** requirements-writing centered on the booking lifecycle: browse availability → hold → confirm → remind → attend / cancel / no-show → (rebook). fact-sheet locks every policy value. *Decision points: single-resource or multi-resource? Group bookings? Recurring bookings? Each "yes" changes the data model — if the owner has not decided, stop and ask (§6.3).* (Unattended run: BOOTSTRAP's approval-points rule applies at this point — a decision recorded in the commissioning brief or `requirements.md` counts as the answer; if none is recorded and no user is reachable, follow the §6.3 stuck protocol (log-and-continue, then the safe defaults) and record the substitution in `progress.md`.)
2. **D2+D7 design.** system-design: availability is a query over bookings + resource calendars, with slot holds as short-lived records that expire; the confirm path is a transaction, not a sequence of hopeful writes (G-AR-001, G-AR-003 failure-behavior review — what happens when two customers confirm the same slot in the same second is answered here, in writing). auth-hardening for staff/customer accounts (G-SE-031) — if the product has accounts; a guest-only booking product with no accounts records G-SE-031 as N/A with the reason in `progress.md`.
3. **D3+D13+D4+D5 build.** schema-design: bookings carry a database-level overlap protection for the resource+time range (exclusion constraint or equivalent transactional guard) — G-DB-001 (schema lint), G-DB-002 (constraint-presence check) are the gates that prove the no-double-book guarantee lives in the data layer, not in application hope. api-building: booking creation is idempotent (G-BE-003 duplicate-submit test — a retried or double-clicked confirm creates exactly one booking). queues-jobs: holds expire via jobs, reminders are scheduled jobs with dead-letter handling (G-BE-091 failure-injection, G-BE-092 DLQ drill, G-BE-093 transactional-enqueue — the reminder is enqueued in the same transaction as the booking). Frontend: the booking form passes forms gates (G-FE-121 axe form rules, G-FE-123 double-submit, G-FE-124 screen-reader pass); D13 in the same step (G-AC-001) — a calendar widget that a keyboard user cannot operate is a failed booking system.
4. **D11 money & messaging (conditional).** If deposits/prepayment: payments in test mode (G-IN-001, G-IN-002), refund behavior on cancellation wired to the fact-sheet's cancellation window. *Decision point: if no payment provider has been chosen, stop and ask (§6.3).* Always: transactional-email confirmations and reminders authenticated and verified end to end (G-IN-061 authentication check, G-IN-064 end-to-end arrival test); sms reminders where used, with opt-out honored (G-IN-071 status-callback test, G-IN-072 opt-out drill). notifications preference timing respected (G-BE-133). (Unattended run: BOOTSTRAP's approval-points rule applies at this point — a decision recorded in the commissioning brief or `requirements.md` counts as the answer; if none is recorded and no user is reachable, follow the §6.3 stuck protocol (log-and-continue, then the safe defaults) and record the substitution in `progress.md`.)
5. **D14 legal/privacy.** privacy-laws register: customer contact data, retention after the appointment date, deletion path (G-LG-001, G-LG-002). legal-documents: booking terms and the cancellation policy as shipped pages — the policy page, the confirmation email, and the implemented refund behavior must state the same windows and fees.
6. **D12 performance.** performance-budgets (G-AN-101) with the availability query as a named budgeted route: it runs on every calendar view and must stay fast as booking history grows (index per schema-design, verified against production-shaped data volume).
7. **D7+D8 verification.** Security: G-SE-001 (0 criticals), G-SE-031. Concurrency rehearsal: parallel confirm attempts on one slot produce exactly one booking (the G-DB-002/G-BE-003 evidence, exercised under load, not just unit tests). Lifecycle rehearsal: book → hold expiry → reminder fired → cancel inside window (refund correct) → cancel outside window (fee per policy) → no-show recorded. QA: G-QA-111; placeholder-scan G-QA-141 (scan rendered output, not source) — demo resources and fake availability never ship.
8. **D6 deploy.** ci-cd (G-DO-001), hosting (G-DO-071). Job runner/scheduler verified live in production — a booking system whose reminder jobs silently do not run has failed at its core job.
9. **D9 finish.** technical-seo + structured-data for public service/booking pages (G-CO-001, G-CO-081) using only real services and real opening hours from the fact-sheet.

## Gates that must pass

- **No-double-book (blocking):** G-DB-001, G-DB-002, G-BE-003 — overlap protection in the data layer, idempotent confirm, proven under parallel attempts.
- **Lifecycle jobs:** G-BE-091, G-BE-092, G-BE-093 — holds expire, reminders fire, failures land in the DLQ visibly.
- **Messaging:** G-IN-061, G-IN-064, G-BE-131, G-BE-133; SMS where used: G-IN-071, G-IN-072.
- **Money (if deposits):** G-IN-001, G-IN-002 — test-mode verified, cancellation refunds match policy.
- **Forms/accessibility:** G-FE-121, G-FE-123, G-FE-124, G-AC-001, G-AC-005 — WCAG 2.2 AA pass.
- **Legal:** G-LG-001, G-LG-002; published cancellation policy matches implemented behavior.
- **Security/QA:** G-SE-001 (0 critical findings), G-QA-111, G-QA-141.
- **Performance/deploy:** G-AN-101, G-DO-001, G-DO-071.

## Failure handling

- **Parallel-confirm rehearsal produces two bookings:** release blocker. The fix belongs in the data layer (constraint/transaction isolation per schema-design), never in a UI lock or a "please wait" spinner. Re-run the rehearsal at higher concurrency after the fix.
- **Reminder jobs fail or land in the DLQ during rehearsal (G-BE-092):** fix the job path before deploy; a booking system that cannot remind is a no-show generator. If the failure is the email/SMS provider, the fallback channel fires and the failure is alerted — silently dropping reminders is not an option.
- **Policy mismatch (page vs email vs behavior):** behavior and copy are reconciled to the fact-sheet before launch; if the fact-sheet itself is wrong, the owner corrects it (§6.3) — the build never edits policy on its own.
- **Timezone defect found in testing (booking stored/displayed an hour off):** audit every stored time for the UTC rule; a single local-time write path invalidates the whole calendar and is fixed at the writer, per schema-design's single-writer discipline.
- **Any other gate fails:** fix in the owning department, re-run, record both results in `progress.md`.

## Definition of done

Double-booking is impossible at the data layer and proven under parallel load; the full lifecycle (hold, confirm, remind, cancel both sides of the window, no-show) rehearsed with correct money and messages; published policies match behavior exactly; calendar fully operable by keyboard and screen reader; reminder jobs verified running in production; deployed (G-DO-071) with all gates above green. **Pre-provisioning complete:** where no production environment exists yet, the project may be recorded as *pre-provisioning complete* when every gate except the provisioning-waived ones is green, each waived gate is recorded as a provisioning waiver per §6.3, and the unblocking conditions are listed in `progress.md` — the deployment requirements above remain open until the environment exists. One evidence set in that list is human-required: the screen-reader pass (G-FE-124) can only be evidenced by a human with a real screen reader, so an autonomous run records the gate's agent-evidence form and the Definition of Done stays open on that item until the human pass is recorded in progress.md.

## Worked mini-example — appointment booking for a dental clinic

1. Core loaded; fact-sheet records: 3 dentists (resources), 30-minute slots, 10-minute buffer, free cancellation to 24h before, reminders at 24h and 2h (owner-set values).
2. D1: lifecycle scoped; group/recurring bookings answered "no" by the owner — data model stays single-resource.
3. D2: availability = query over bookings + dentist calendars; holds expire after 10 minutes; confirm is one transaction. G-AR-003 answers the same-second race: the database decides, one winner.
4. Build: exclusion constraint on (dentist, time range) passes G-DB-002; booking POST is idempotent (G-BE-003).
5. Jobs: hold-expiry and both reminders enqueue transactionally (G-BE-093); a killed worker drill lands one reminder in the DLQ and it is retried visibly (G-BE-092).
6. Messaging: confirmation email arrives end to end (G-IN-064); SMS opt-out drill passes (G-IN-072).
7. D14: cancellation policy page, confirmation email, and refund behavior all state the same 24-hour window.
8. Rehearsal: 20 parallel confirms on one slot → exactly 1 booking, 19 honest "just taken" responses.
9. D7+D8: G-SE-001 clean; G-AC-002 keyboard walk completes a booking; G-QA-141 clean.
10. Deploy (G-DO-071); a real test booking on production fires its 2h reminder via the live scheduler.
