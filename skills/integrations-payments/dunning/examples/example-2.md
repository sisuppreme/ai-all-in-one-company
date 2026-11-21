# Example 2 — The update link that saved nothing

## Before

The dunning email's "Update your card" link opens a form inside the app.
Its handler stores the new card's last four digits in a local
`payment_methods` table for display and shows "Card updated ✓". It never
calls the provider. The retry schedule keeps charging the old, declined
card at the provider, every attempt fails, and the customer — who did
exactly what the email asked, twice — is canceled at the end of the
window and learns why from support.

## After

The update path writes to the provider and proves it:

1. The link is a signed, hosted update page: no full login required,
   the link itself carries short-lived authorization.
2. Submitting the new card replaces the payment method at the provider
   through the provider's own elements, so card data never touches the
   app's servers.
3. A successful update immediately triggers a retry of the open
   invoice — the customer sees the charge succeed and the banner clear
   in the same session, not at the next scheduled attempt.
4. The mirror converges from the payment-succeeded webhook; the
   sequence halts and no further dunning notices are sent.

Note: corrects IN-086 — the payment-update path stores the new card at the provider and retries immediately; an update that persists nothing is banned (BAN-IN-042).
