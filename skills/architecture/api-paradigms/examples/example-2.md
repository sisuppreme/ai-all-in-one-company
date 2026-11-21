# Example 2 — Cost controls added to a public GraphQL API

## Before

A GraphQL API that legitimately serves web and mobile clients with divergent reads is public — with no depth limit, no complexity budget, and no deprecation practice. A security review crafts a deeply nested query that fans out across resolvers and saturates the service; meanwhile an obsolete field cannot be retired because nobody tracks its usage.

## After

The server configuration gains a maximum query depth of 8 and a complexity budget enforced per operation, with persisted queries for the first-party clients. The schema adopts the spec's deprecation mechanism — the obsolete field is marked `@deprecated(reason: "Use order.total_price")` — and field-usage metrics drive its eventual removal. The limits check (G-AR-062) runs in CI so the controls cannot silently disappear.

## Note

Corrects AR-124 (a GraphQL API ships with query depth/complexity limits and a field deprecation policy; an unbounded public endpoint is a defect).
