# Example 1 — The crawl that started before the paperwork

## Before

```text
Project log (excerpt)
Mon 09:12  site-discovery crawl of client-old-site.example — 214 pages inventoried
Mon 11:40  asset-harvesting run — 96 images, full copy deck exported
Fri 15:03  docs/clone-authorization.md created: "Client authorized the migration
           of their site, including all pages and assets." (no authorizer named,
           no scope, no ground stated)
```

The crawl and harvest ran four days before any authorization existed; the record was written afterward to describe what had already happened, and it names nobody.

## After

```text
Project file, committed before any target request:
docs/clone-authorization.md
  Authorizer: A. Client, owner of client-old-site.example
  Right to authorize: site owner (registrant and business owner of record)
  Ground: LG-182(b) — written client authorization
  Scope: client-old-site.example — layout, behavior, copy, and the client's own
         brand assets, for migration to the new build only
  Date: 2026-11-21

G-LG-091 pre-flight: record found, dated, in scope → crawl permitted.
First crawl log entry: 2026-11-21 14:05 (after the record's commit).
```

## Note

Violates LG-181 and LG-183 (authorization must be a pre-committed artifact naming the authorizer, their right, and the scope); corrected by committing the complete record first and letting the pre-flight gate refuse any earlier crawl.
