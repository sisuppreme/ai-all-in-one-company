# Example 2 — A complete deprecation package for retiring v1

## Before

The team decides v1 will be "turned off soon." A blog post mentions it once. There is no sunset date, no migration guide, and v1 responses carry no headers. Four months later v1 is switched off; two partners discover it from their own monitoring.

## After

Before the window opens, three artifacts land together: (1) the changelog entry — "v1 is deprecated as of 2026-03-01 and will be removed on 2026-09-01; migrate per the v1→v2 guide"; (2) the migration guide itself, mapping every v1 field and endpoint to its v2 equivalent; (3) the running service — every v1 response now carries `Deprecation: Mon, 01 Mar 2026 00:00:00 GMT` and `Sunset: Tue, 01 Sep 2026 00:00:00 GMT`. Removal is scheduled only after 2026-09-01 and a traffic check showing no remaining v1 consumers.

## Note

Corrects AR-086 (deprecation requires the sunset date, the migration path, and the consumer notification before the window starts) and AR-087 (removal waits for the announced date and the consumer check).
