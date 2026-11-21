# D18 Customer Experience — End-to-End Example

## Scenario

"NoteNest," a small note-taking SaaS run by one operator, launches its customer
surfaces: a support page, a contact form, a 14-day trial, and a public status page.
Every promise on those surfaces must be one the operator's actual configuration
and hours can keep — because a solo operator's honest cadence beats a borrowed
one they cannot staff.

## Before — the slop version

Support page copy:

```markdown
## We're here 24/7
Average response: 12 minutes · 98% customer satisfaction
Email us any time — we reply within 1 hour, day or night.

[Contact form]  → posts to an endpoint that discards submissions
```

Trial and status surfaces:

```markdown
Pricing page: "14 days free — no card required!"
  Reality: signup creates a paid subscription on day one; a banner calls it
  a trial. Upgrade modal: "Your trial offer expires in 04:59" — the timer
  resets to 5:00 on every visit. First charge lands on day 15 with no reminder.

Status page header: "99.99% uptime over the last 90 days"
  Reality: the page was created last week; no monitor history exists.
  During a 40-minute checkout outage it read "All systems operational."
```

What is wrong, visibly: the support promises (24/7, 1 hour, 12 minutes, 98%) are
invented — the ticketing tool is configured for weekday responses and no
satisfaction survey exists; the contact form is a dead end; the "trial" has no
trial state, its countdown is fake, and the first charge arrives unannounced; and
the status page displays an uptime figure with no measurement behind it while
claiming all-operational mid-outage.

## What the skills caught

- **BAN-CX-003 — Promise that differs from the configuration** (defeats
  DET-CON-014) and **BAN-CX-004 — Invented support metrics** (defeats
  DET-CON-011). **CX-005**: every published response-time or hours statement
  equals the SLA and office-hours values configured in the ticketing tool;
  **CX-006**: with no staffed rota, copy states actual support hours instead of
  "24/7."
- **BAN-CX-001 — Dead-end intake** (defeats DET-CON-028). **CX-001 / CX-004**:
  every channel creates a ticket in the single queue, and creation triggers an
  acknowledgment carrying the reference the customer can track (CX-009).
- **BAN-CX-051 — Fake trial** (defeats DET-FAKE-003). **CX-103**: signup creates
  an actual trial subscription with an explicit trial end in the billing
  platform; **CX-102**: configuration matches copy exactly, or release blocks.
- **BAN-CX-053 — Fake countdown** (defeats DET-FAKE-018). **CX-110**: any
  countdown is computed from the user's real trial end and stops at zero.
- **BAN-CX-052 — Silent first charge** (defeats DET-CON-028). **CX-105**: the
  trial-will-end event drives a reminder naming the charge date and amount
  before any charge; **CX-106** grounds conversion in ROSCA — clear disclosure,
  express informed consent, simple cancellation — and **CX-108** makes cancelling
  take no more steps than starting.
- **BAN-CX-084 — Uptime figure with no measurement** (defeats DET-CON-011) and
  **BAN-CX-081 — All-operational during an outage** (defeats DET-CON-015).
  **CX-167**: displayed states come from the monitoring source or the incident
  owner's posts; **CX-163 / CX-164**: the first post goes out on confirmed
  impact, carrying what is known, what is not, and the next update time.

## After — the corrected version

Support page copy, generated from the ticketing configuration (CX-005, CX-012):

```markdown
## Support
Support hours: Monday–Friday, 09:00–17:00 (PKT). We aim to send a first
response within one business day. Every message creates a ticket, and you
will receive its reference number immediately so you can track it here.
```

Trial, with the billing platform as the source of truth:

```markdown
Signup screen (shown before commit, CX-101):
"Your 14-day free trial starts today. The first charge of $12 will be made
on 2026-12-05, then monthly. A card is required now. We will email you a
reminder three days before the first charge."
  → the subscription is created in trial state with that exact end (CX-103);
    the trial-will-end event sends the promised reminder (CX-105);
    cancelling is one in-product action, effective immediately for billing,
    with access to the stated trial end (CX-108).
```

Status page, configured before it is needed (CX-172):

```markdown
Components listed: Sign-in, Dashboard, Checkout — customer-facing
capabilities only, no internal service or vendor names (CX-161).
No uptime percentage is displayed until the monitor has real history
to compute one from (CX-167).

Incident post (holding template, CX-164):
"Checkout: some customers cannot complete payment. Impact confirmed at
14:05. Cause is not yet known. Next update by 15:00."
  → the stated cadence is one this operator can actually staff (CX-166).
```

## Skills used

- [support-ticketing](../skills/customer-experience/support-ticketing/SKILL.md)
- [trial-conversion](../skills/customer-experience/trial-conversion/SKILL.md)
- [status-communications](../skills/customer-experience/status-communications/SKILL.md)
- [churn-prevention](../skills/customer-experience/churn-prevention/SKILL.md)
- [help-center](../skills/customer-experience/help-center/SKILL.md)
