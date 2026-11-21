# Example 1 — Done on attempt, corrected to done on gate result

## Before

progress.md carries the entry:

"2026-11-21 — Payments checkout: done."

The checkout was written and clicked through once in development with a
successful test card. No gate ever ran. The decline path was never tested —
and in fact a declined card also lands on the "Payment successful" screen,
because no provider response is checked.

## After

The entry is corrected in the same change that fixes it:

1. The item reverts to in progress; "done" is withdrawn the moment the
   missing gate result is noticed.
2. The payments checkout gate runs: a known decline test card must decline
   visibly, and a successful payment must record the provider's payment ID.
   It fails on the decline card, the handler is fixed, and the gate re-runs.
3. progress.md records the result under the item: gate ID, "pass",
   2026-11-21, with the two test outcomes named.
4. Only then does the entry read "done" — and it links the checkout module
   the gate ran against.

The status was wrong for a day. The correction is visible in the file's
history, and "done" now means something a reader can re-check.

Note: corrects PM-142 — a step is done when its gate result is recorded, never when it was merely attempted.
