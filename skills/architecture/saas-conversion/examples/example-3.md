# Example 3 — Billing retrofitted in shadow, with explicit grandfathering

Scenario (hypothetical): "FormField," a form-builder that one agency's
clients have used free for two years as part of a services bundle, is
converting to paid multi-tenant SaaS. Billing does not exist yet: access is
granted by a `plan` column an account manager edits by hand. Prices and
dates below are the fictional plan's own terms, stated so the example is
checkable.

## Before

The conversion branch adds a paywall in the same release as the tenancy
work. On deploy day it reads the existing `plan` column — copied months ago
from a spreadsheet — and enforces it: tenants marked `free` are capped at
three forms, and everyone else is prompted for a card. Nobody has created
a customer or subscription for any tenant in the payment provider, because
"we'll sync that once people start paying."

That is billing switched on before the mirror exists (BAN-AR-134): the
first enforcement error walls off a paying-by-invoice client whose
spreadsheet row was stale, while several tenants keep unlimited access
because there is no subscription object that could ever charge them. It
violates AR-272 (enforcement before the provider mapping is built and
reconciled) and AR-273 (existing customers' terms changed by a data
migration, with no notice and no written grandfathering).

## After

Billing is built in shadow, reconciled, and only then enforced:

1. **The tenant is the billable entity (AR-272).** A provider customer is
   created per tenant — one for the legacy agency tenant, one per client
   tenant — never per individual user. Subscription state is mirrored from
   the provider into the app, and entitlement is read from that mirror,
   following the subscriptions skill. The hand-edited `plan` column stops
   being a source of truth the day the mirror starts.
2. **Shadow reconciliation while nothing changes.** For two weeks the
   mirror runs alongside the legacy behavior: the app still grants access
   exactly as before, and a nightly job diffs mirrored subscription state
   against a live provider read and against what each tenant actually has.
   It catches two mismatches — a tenant whose card payment had failed
   (mirror said `active`, provider said `past_due`) and a tenant with two
   provider customers from a duplicate signup — both fixed in the mapping,
   not by changing anyone's access.
3. **Grandfathering written down per cohort (AR-273).** The plan states,
   before any enforcement:
   - The legacy agency tenant keeps its bundled price (no separate charge)
     and its current limits indefinitely while the services contract runs.
   - Existing client tenants keep unlimited forms at no charge until
     1 March of the following year, with notice sent at least 60 days
     before; after that date they move to the standard Starter plan at the
     price named in the notice, executed as a communicated plan change
     through subscriptions — not as a side effect of this migration.
   - Silence would have meant existing terms continue; here nothing is
     left silent.
4. **Enforcement per cohort, gated (G-AR-135).** Before the pilot cohort's
   paywall and plan limits switch on, the gate diffs every tenant in the
   cohort: provider customer exists, mirrored state matches the provider,
   granted entitlement matches the grandfathering terms above, and the
   conversion itself has issued zero charges. The gate passes with zero
   mismatches, so enforcement enables for the pilot cohort only; the
   remaining cohorts follow as their own reconciliations pass. The day the
   billing code shipped, nobody's access changed.

Note: corrects AR-272 and AR-273 — billing is retrofitted onto the tenant
with the provider mapping built and reconciled in shadow, existing
customers are grandfathered with named prices, limits, and dates, and
enforcement waits for the G-AR-135 reconciliation to pass per cohort
(BAN-AR-134).
