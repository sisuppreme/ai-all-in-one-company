# Example 3 — Retiring a hand-written wiki for a generated reference

## Before

Alongside the OpenAPI document, a wiki carries hand-written pages restating every endpoint. The wiki says `POST /orders` responds 200 with a `total` field; the spec and the service say 201 with `total_price`. Both are linked from the developer portal, and integrators file bugs against whichever one they read.

## After

The wiki's endpoint pages are deleted. The reference is generated from the OpenAPI document on every release, so paths, fields, and status codes cannot drift from the contract. The human-written layer remains, in the docs site where it belongs: the authentication walkthrough, one runnable example per endpoint group, the error catalog, and the changelog. The wiki keeps only a pointer to the generated reference.

## Note

Corrects AR-101 (the reference is generated from the OpenAPI document, never hand-maintained in parallel) and AR-106 (humans write only the layer generation cannot).
