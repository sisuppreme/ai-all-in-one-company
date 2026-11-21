# Example 2 — The unscoped export, scoped and tested

## Before

The CSV export endpoint was written by a different developer than the list
endpoint. The list is tenant-scoped; the export runs
`SELECT * FROM invoices WHERE paid = true` with no tenant filter, because
"exports are internal." A tenant admin who finds the URL downloads every
tenant's paid invoices.

## After

The export query runs under the same platform-enforced scoping as every
other path (row-level security keyed to the request's tenant context), so
the missing filter returns the tenant's own rows only. The cross-tenant
test suite gains an export case: tenant A's credentials request the export
and the test asserts the file contains zero of tenant B's invoice IDs.

Note: corrects AR-184 — every query path, including admin, reporting, export, and background jobs, is scoped by tenant; an unscoped path is a blocker defect.
