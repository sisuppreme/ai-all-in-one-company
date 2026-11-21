# Example 2 — Naming and typing a generic container diagram

## Before

The container diagram has three elements: "Frontend", "Backend", and a small cylinder labeled "DB" attached to the Backend box as an afterthought. No technologies, no queue (the system has one), no relationship labels.

## After

The diagram names and types each element: Web App [Container: Next.js] serving the browser over HTTPS/JSON; Orders API [Container: Node.js] called by the Web App over HTTPS/JSON; PostgreSQL — orders store [Container: PostgreSQL] written by the Orders API over SQL; Job Queue [Container: Redis] fed by the Orders API over AMQP-style list operations and drained by the Email Worker [Container: Node.js]. The store and the queue are containers in their own right.

## Note

Corrects AR-027 (no generic labels — elements name the actual thing) and AR-024 (data stores and queues are first-class containers).
