# Example 2 — Developer's-jurisdiction assumption vs. full jurisdiction map

## Before

Launch checklist, accessibility line:

> "Team is based outside the EU/US, so no accessibility law applies. Target: none. Reviewer: —"

The product sells e-commerce services to EU consumers and is bidding on a US state-government contract. No jurisdiction map exists.

## After

`docs/legal/jurisdiction-map.md` (excerpt):

| Market | Sector / customer | Instrument | Pinned standard | Required artifact | Reviewer | Review date |
|---|---|---|---|---|---|
| EU (DE, FR) | E-commerce, consumers | EAA (Directive (EU) 2019/882) via national transpositions | EN 301 549 V3.2.1 → WCAG 2.1 AA | Accessibility statement | D14 counsel | 2026-11-21 |
| US federal/state | Public procurement | Section 508; ADA Title II rule | WCAG 2.0 AA (508 contract pin); WCAG 2.1 AA (Title II) | ACR/VPAT per contract | D14 counsel | 2026-11-21 |

Build target remains WCAG 2.2 AA; conformance is documented against each pinned version under AC-064.

Note: applicability is derived from the users' markets and the customer's sector, recorded row by row, per AC-061.
