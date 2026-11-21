# Example 3 — Provisioning as a tested procedure

## Before

Onboarding a tenant is a wiki page of SQL statements an engineer runs by
hand: insert the tenant row, insert the admin user, seed the default roles,
"don't forget the billing record." Steps are missed roughly one onboarding
in four, each miss surfacing later as a confused support ticket.

## After

Provisioning is one idempotent procedure (`provision-tenant`) that performs
every step in a transaction, writes the tenant-catalog entry, and verifies
the result by signing in as the new tenant's admin in a smoke check. It runs
in staging on every release (the provisioning drill, G-AR-093), so a code
change that breaks onboarding fails CI before it meets a customer.

Note: corrects AR-188 — new tenants are provisioned by an automated, tested procedure; manual database edits are not a provisioning path.
