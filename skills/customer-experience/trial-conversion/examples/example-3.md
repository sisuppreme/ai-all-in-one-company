# Example 3 — Fake countdown

## Before

The upgrade modal shows "Hurry — your exclusive trial offer expires in 04:59!" The timer is a front-end countdown: reloading the page resets it to 5:00, it appears on every visit regardless of the user's actual trial end, and nothing about the offer changes when it reaches zero.

## After

The modal shows "Your trial ends on 4 December 2026 — 6 days left," computed from the subscription's real trial end in the billing platform. The figure is identical across sessions and reloads, decreases by real elapsed days, and when the trial ends the message is replaced by the actual post-trial state.

Violates/corrects CX-110 — any deadline shown is the user's real trial end, never a resetting timer.
