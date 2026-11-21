# Example 3 — Everything is "high priority"

## Before

The intake form has one field, "Priority", and reporters set it themselves. Of 63 open defects, 58 are "high": a misaligned icon, two typos, a slow admin report, and one defect that corrupts invoice totals. The queue gives the team no ordering at all, so work is picked by whoever shouts loudest, and the invoice defect waits three weeks behind cosmetic fixes.

## After

Triage reclassifies the queue on two independent fields. Severity is set by technical impact: the invoice defect is severity critical (wrong money), the slow report is minor (workaround exists), the typos are trivial. Priority is set separately by business urgency: the invoice defect is priority high, a defect on the pricing page is severity minor but priority high because a launch depends on it, and the icon is low on both. The scheduled order is now readable from the fields, and no field defaults to "high".

Note: corrects QA-263 (severity is not priority).
