# Example 3 — The request nobody clocked

## Before

```text
From: a user, via the "Privacy questions" web form
Subject: Please send me all the data you hold on me

Support flow: the message lands in a shared inbox. Someone replies
"we'll look into it." No ticket, no date recorded, no deadline.
Seven weeks later the user writes again, angry — and nobody can say
when the request arrived or what has been done with it.
```

## After

```text
Request DSAR-2026-0142 — type: access — channel: web form
Received:        2026-11-03 09:14 (system timestamp)
Identity:        verified 2026-11-03 via account email challenge (proportionate)
Deadline:        computed from regime table in project file
Aging alerts:    50% — 2026-11-17 (auto) · 80% — 2026-11-26 (auto)
Search:          primary DB ✓ · search index ✓ · analytics ✓ · processors 2/2 ✓
Delivered:       2026-11-24 — JSON + CSV export, download confirmed
Closed:          2026-11-24 — outcome: delivered
```

## Note

Corrected under LG-043 and LG-052: the clock starts at a system-recorded receipt, the deadline comes from the configured regime table, aging alerts fire automatically (LG-044), and the whole handling is one log record — not an inbox thread (BAN-LG-023, BAN-LG-025).
