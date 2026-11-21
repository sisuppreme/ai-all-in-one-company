# Example 2 — "24/7 support" from a one-person operation

## Before

```text
Pricing page:
  "Every plan includes 24/7 support — replies within the hour."

Reality:
  Operator: one person, support checked Mon–Fri, roughly
  09:00–18:00 local. Ticketing tool: vendor default settings,
  no SLA configured, no office hours set, no rota.
  Fact sheet entry for support hours: none.
```

The copy promises round-the-clock, one-hour support that no configuration measures and no staffing covers — a fabricated operational claim.

## After

```text
Ticketing tool configuration (set first):
  Office hours: Mon–Fri 09:00–18:00 (operator's timezone)
  First-response SLA: 1 business day (normal), 4 business
  hours (urgent) — targets the operator's real schedule meets.

Pricing page (copied from the configuration):
  "Support hours: Monday–Friday, 9:00–18:00. We reply within
  one business day; urgent issues within 4 business hours."

G-CX-002 copy-vs-config diff: both published values match the
exported SLA and office-hours configuration. No 24/7 claim
remains anywhere on the site.
```

## Note

Corrected under CX-005 and CX-006 (BAN-CX-003): the promise is set in the tool from the operator's real hours first, and public copy states those configured values — or the actual hours with no number when nothing is staffed.
