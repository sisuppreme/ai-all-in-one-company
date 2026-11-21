# Example 3 — Four pages, four grace periods

## Before

The product's terms say past_due customers keep read-only access during
the grace window. Nobody implemented that rule in one place. The
dashboard checks `status === 'active'` and locks the user out entirely;
the export endpoint checks only that the user is signed in and serves
full data; the mobile app caches "Pro" from before the failure and
never re-checks; the billing page shows "All good" because it compares
a local `nextBillingDate` against today. Four surfaces, four different
answers to the same question — and the one the customer was promised in
the terms is none of them.

## After

One rule, read from one place:

1. The terms state the rule once: during past_due, access is read-only
   until the sequence ends.
2. Entitlement is a single server-side check that reads the mirrored
   subscription state and the past_due rule; web, mobile, API, and
   exports all call it — none keeps a local copy of the logic or the
   state.
3. Read-only is enforced at that check, so a past_due user can open
   and export their existing data but cannot create or change anything,
   on every surface identically.
4. When the sequence ends, the same check applies the end state; when
   payment recovers, the same check restores full access. No surface
   changes code either way.

Note: corrects IN-087 — one written past_due access rule enforced identically everywhere; a UI-only or per-page access cut is banned (BAN-IN-044).
