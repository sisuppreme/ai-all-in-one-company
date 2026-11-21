# Example 1 — GraphQL proposed for plain CRUD, REST chosen instead

## Before

A new public API for a single web client is proposed as GraphQL "for flexibility." The surface is plain resource CRUD — products, orders, invoices — with one client whose reads are fixed and known. Nobody names a second client type or a divergent read shape. The team is about to take on schema governance, query-cost control, and a deprecation policy for no consumer benefit.

## After

ADR-0012 records the evaluation: interaction shape = resource CRUD, one client, fixed reads. GraphQL's entry condition (multiple client types needing divergent, client-shaped reads) is not met, so the REST default applies and the API is designed per api-architecture. The ADR names the trigger that would reopen the question: a second client platform (mobile) whose read shapes demonstrably diverge from the web client's.

## Note

Corrects AR-122 (REST is the default for resource CRUD and public APIs) and AR-123 (GraphQL is adopted only when its entry condition is met and named in the ADR).
