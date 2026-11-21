# Example 1 — Splitting a mega-diagram into C4 levels

## Before

One diagram tries to serve everyone: it shows the user, the whole system, all containers, the components inside two of them, and a handful of classes — 60 elements in one picture. New team members cannot read it, and because editing it is painful, it has not been updated in months.

## After

Two diagrams replace it. Level 1 (system context): the Customer, the Shop System as a single box, and the external Stripe and email-provider systems with labeled, directional relationships. Level 2 (containers): Web App, Worker, PostgreSQL store, Redis queue, and the two external systems, every line labeled with its protocol. A Level 3 diagram is added only for the Worker, whose job-routing internals are non-obvious. Each diagram carries a legend.

## Note

Corrects AR-021 (produce only the levels the audience needs) and AR-026 (one view per diagram, with a legend).
