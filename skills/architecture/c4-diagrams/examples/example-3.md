# Example 3 — Updating a diagram in the same change as the architecture

## Before

A pull request replaces the in-house payments container with a third-party hosted checkout. The code, config, and tests change; the container diagram is left for "a later cleanup." For two releases the diagram shows a payments service the company no longer runs, and a new hire builds a runbook against it.

## After

The same pull request updates the container diagram source: the Payments Service container is removed, the hosted checkout appears as an external system with a synchronous HTTPS/JSON call out and an asynchronous webhook relationship in, and ADR-0019 (adopt hosted checkout) links the updated diagram in its consequences section.

## Note

Corrects AR-029 (a diagram is updated in the same change that alters the architecture, and the ADR links the diagram).
