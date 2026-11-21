# Example 2 — Use case without an abuse case

## Before

> Use case UC-7: "A signed-in user opens an invoice from the invoice list and downloads the PDF at `/invoices/{id}/pdf`."
> Threats considered: "Invoice data is sensitive; route requires login. Threat closed."

The route checks only that a session exists. Any signed-in user who changes `{id}` downloads any tenant's invoice — names, addresses, and totals included.

## After

> Use case UC-7: "A signed-in user opens an invoice from the invoice list and downloads the PDF at `/invoices/{id}/pdf`."
> Abuse case AC-7: "As a signed-in user of Tenant A, I change `{id}` to an invoice belonging to Tenant B and download their PDF, harvesting customer names, addresses, and amounts."
> Threat T-14 (Elevation of privilege / Information disclosure), disposition: control + test.
> Control: the handler loads the invoice scoped by `tenant_id` from the session, never by raw ID alone; a cross-tenant ID returns 404.
> Test: `test_invoice_pdf_cross_tenant_returns_404` — authenticated as Tenant A, request Tenant B's invoice ID, assert 404 and no PDF bytes.

*Note: corrects SE-186 (an abuse case written beside the use case, in the attacker's voice).*
