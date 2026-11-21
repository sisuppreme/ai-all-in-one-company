# Example 1 — From three generic boxes to a real container design

## Before

ARCHITECTURE.md contains a single diagram: three boxes labeled "Frontend", "Backend", and "Database", joined by two unlabeled arrows. No users, no external systems, no protocols. The actual system is a web application, a background worker, a PostgreSQL database, a Redis queue, and a Stripe integration — none of which appear.

## After

The container diagram (Mermaid, kept in the repo) shows: the Customer (person); the Web App (container, serves HTTPS/JSON to the browser); the Worker (container, consumes jobs over AMQP from the Redis queue); the PostgreSQL database (container, written only by the Web App over SQL); the Redis queue (container); and Stripe (external system, called synchronously over HTTPS/JSON for checkout, webhooks received asynchronously). Every arrow carries its protocol label.

## Note

Corrects AR-001 (every container corresponds to a real deployable unit or store) and AR-002 (every arrow carries a protocol or format label).
