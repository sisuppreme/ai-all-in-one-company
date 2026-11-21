# Example 2 — A browser timer replaced by the provider lifecycle

## Before

Trials are run by the frontend. Signup stores `trialEndsAt` in the database
and the plan flag in the browser:

```ts
if (localStorage.plan === "pro" && Date.now() < trialEndsAt) {
  unlockProFeatures();
}
```

No subscription exists at the provider. Consequences arrive one by one:
editing local storage grants Pro indefinitely; a customer whose clock is
wrong loses access mid-trial; nobody is warned before "conversion," because
nothing ever converts — and nothing can be canceled, because there is
nothing at the provider to cancel.

## After

The trial is a provider subscription from the first minute:

1. Signup creates a trialing subscription at the provider, configured with
   the plan's trial length and the explicit no-card trial-end outcome
   (pause). The local row mirrors it and carries the provider subscription
   ID and period end.
2. The signup page showed the terms before account creation: 14 days, no
   card required, Pro at the catalog price afterward only if a card is
   added.
3. Three days before the end, the provider's trial-will-end event triggers
   the warning email naming the date and the price.
4. Entitlement middleware reads only the mirrored status. Browser storage
   holds no plan flag, and no code path compares a local date to decide
   access.

Note: corrects IN-022 — no local timer or client flag grants, extends, or revokes access; the provider lifecycle does (BAN-IN-012, BAN-IN-015).
