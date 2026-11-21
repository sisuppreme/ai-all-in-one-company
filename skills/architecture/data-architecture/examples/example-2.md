# Example 2 — One writable home for the customer email

## Before

The customer's email is stored in `users.email` (written by the account
service) and in `billing_customers.email` (written by the billing import).
Support updates the address in the account screen; invoices keep going to the
old address, and neither team can say which copy is right.

## After

`users.email` is the single writable home, owned by the account service.
Billing holds a read model, `billing_customers.email_snapshot`, refreshed by
the `UserEmailChanged` event, with a stated staleness bound of 5 minutes.
Billing code has no write path to the snapshot except the event consumer, and
the data-architecture notes name `users` as the source of truth.

Note: corrects AR-144 — the same fact has exactly one writable home; copies are read models with a named synchronization mechanism and a stated staleness bound.
