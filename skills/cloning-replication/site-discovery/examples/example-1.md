# Example 1 — Discovery launched on a verbal OK

## Before

```text
Project log (excerpt)
Mon 09:05  Client call: "Sure, go ahead and map the old site."
Mon 09:20  site-discovery crawl of client-old-site.example started — 214 URLs
Mon 16:40  Wayback CDX enumeration run for the same domain
Fri 15:03  docs/clone-authorization.md created ("client authorized the
           migration") — four days after discovery finished
```

Discovery ran on a phone call. The authorization record exists, but it was written after the crawl it was supposed to permit, so nothing can prove the crawl was authorized when it happened.

## After

```text
Project file, committed before any target request:
docs/clone-authorization.md
  Authorizer: A. Client, owner of client-old-site.example
  Ground: written client authorization for a migration rebuild
  Scope: discovery crawl of client-old-site.example (URLs and structure only)
  Date: 2026-11-21

G-CL-001 pre-flight: record found, dated, in scope, commit predates run
→ crawl permitted. First crawl log entry: 2026-11-21 14:05.
```

## Note

Violates CL-001 (the authorization artifact must exist and predate the first crawl log entry; the tooling fails closed without it); corrected by committing the complete record first and letting the pre-flight gate refuse any earlier crawl.
