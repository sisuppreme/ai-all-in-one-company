# D16 Cloning & Replication — End-to-End Example

## Scenario

A small studio is migrating its own old marketing site — the studio is the rights
holder — to a new platform. The old site is partly live, partly deleted; the rebuild
must recover what can be evidenced, design the rest in the old site's system, and
never present a designed page as a recovered one. The clone-ethics frame (D14)
governs the whole job.

## Before — the slop version

Project notes from the first attempt:

```markdown
Day 1: Crawled the old site to scope the job (client signs the contract Friday,
authorization paperwork to follow).
robots.txt disallows /internal/ — fetched those 14 pages anyway to confirm
they exist. Members' area mapped using a teammate's personal login.

Rebuild delivered:
- Home page: rebuilt from a Wayback capture; headline copy and hero photo
  pasted in unchanged "for fidelity."
- Admin console: never captured (login-gated). Assembled from a UI kit and
  delivered as a "verified clone of the admin console."
- Pricing page: report states "pixel-perfect clone" after a side-by-side look.
```

What is wrong, visibly: the crawl ran days before any authorization record
existed; robots exclusions and a login wall were treated as obstacles to route
around; the target's copy and photography shipped verbatim; and a page nobody had
ever seen was labeled a verified clone, with fidelity claimed from an eyeball
comparison.

## What the skills caught

- **BAN-LG-091 / BAN-CL-001 — Crawl first, authorize later** (defeats
  DET-CRWL-014). **LG-181 / CL-001**: a dated authorization record, committed to
  the repo and naming the target domains, precedes the first request; the crawl
  tooling checks for it and fails closed without it.
- **BAN-CL-002 — Fetching robots-disallowed paths** (defeats DET-CRWL-014).
  **CL-004**: a disallowed path is recorded as "excluded by robots" and never
  fetched; **LG-190** adds that robots silence is not a rights license either way.
- **BAN-CL-003 — Completing discovery through a login bypass** (defeats
  DET-CRWL-008). **CL-009**: gated space is recorded as gated, with its public
  evidence; it is entered only through access the client legitimately provides.
- **BAN-CL-052 — Target copy and branding shipped verbatim** (defeats
  DET-CRWL-009). **CL-106 / CL-107**: reconstructed pages render with the
  operator's own copy and assets; recovered material is a structural reference —
  length, placement, hierarchy — and every substitution is listed in the build
  notes. (For this studio's *own* migration, its own brand assets are the
  exception the D14 record covers explicitly, per LG-186.)
- **BAN-CL-051 — Fabricated page labeled a verified clone** (defeats
  DET-CRWL-013). **CL-103 / CL-104**: every inventory row is labeled `captured`,
  `inferred`, or `designed` before build, and parity claims attach to `captured`
  rows only. **LG-192**: designed pages carry no parity claim anywhere.
- **BAN-CL-061 — Eyeball verdict** (defeats DET-CRWL-002). **CL-122 / CL-132**:
  viewports and the ≥95% similarity bar are committed before the first run, and
  every fidelity claim cites its run — date, engine, viewports, per-page scores.

## After — the corrected version

The rebuild restarts inside the frame:

```markdown
## clone/authorization-record.md  (committed 2026-11-10, before any crawl)
Authorizer: studio owner, rights holder of the old site (own property — LG-182a).
Scope: oldsite.example — all public paths; asset classes: layout = recreate,
copy = owned (client's own), images = owned where the studio's, else replace,
logos/wordmarks = owned. Purpose: platform migration of the studio's own site.

## clone/inventory.md  (excerpt)
| Page            | Status   | Evidence                                   |
|-----------------|----------|--------------------------------------------|
| / (home)        | captured | Wayback capture 2026-03-14, digest logged  |
| /pricing        | captured | Wayback capture 2026-03-14, digest logged  |
| /features       | inferred | JS bundle route manifest + sitemap entry   |
| /admin (gated)  | designed | No capture exists; client-provided export  |
| /internal/*     | excluded | robots.txt Disallow — recorded, not fetched |

Fidelity run 2026-11-19 (same engine/version both sides, viewports committed
2026-11-12, bar ≥95%): / scored 97.2%, /pricing 96.1% — per-page scores with
diff images in the run report (CL-124, CL-132). /admin is delivered as
"new design in the source's system" — no parity claim (CL-104, LG-192).
One font substitution is scored as an accepted deviation with its record,
not masked away (CL-130).
```

Every asset in the harvest manifest carries exactly one rights decision —
`owned`, `licensed`, `recreate`, or `replace` — and no `licensed` row is approved
by the actor who prepared the harvest (LG-184, LG-185).

## Skills used

- [site-discovery](../skills/cloning-replication/site-discovery/SKILL.md)
- [page-reconstruction](../skills/cloning-replication/page-reconstruction/SKILL.md)
- [fidelity-verification](../skills/cloning-replication/fidelity-verification/SKILL.md)
- [design-extraction](../skills/cloning-replication/design-extraction/SKILL.md)
- [clone-ethics (D14)](../skills/legal-privacy/clone-ethics/SKILL.md)
