# Example 2 — Five wordings, one defect

## Before

Five open tickets describe the same failure in different words: "payment spins forever", "checkout hangs after card entry", "order never confirms", "pay button does nothing", "stuck on processing". Each is triaged separately, each marked severity "medium", and two are closed as duplicates with no link to anything. The queue reads as five small problems, so the defect waits behind cosmetic work while it blocks every card payment.

## After

Triage reproduces the hang, identifies one canonical defect — "Payment confirmation never returns after card authorization" — and links the other four reports to it as duplicates. The canonical defect shows a duplicate count of 4, which is read as user-impact signal: severity stays high, priority rises, and the defect takes the next fix slot. No report was closed silently; every duplicate still resolves to the canonical record.

Note: corrects QA-265 (duplicates link, never vanish).
