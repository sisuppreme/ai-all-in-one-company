# Example 2 — The homepage that rebranded alone

Scenario: A project-tracking product renames from Planboard to Northbeam.
The marketing team owns the website; nobody owns a written inventory of
identity surfaces.

## Before

The team swaps the header logo, the hero colours, and the homepage headline,
screenshots the homepage and the pricing page, and announces "the rebrand is
live." The visible pages look completely new. Everything a screenshot cannot
show still carries the old identity — the visual-only swap banned by
BAN-CL-703:

- `og:image` and the Twitter card image on every page still render the
  Planboard logo, so every shared link advertises the old brand.
- The Organization JSON-LD still declares `"name": "Planboard"`, and its
  `logo` field points to a URL that still serves the old mark.
- The favicon and the installed-app icon are the old logo.
- Invoice and receipt emails still arrive from the sender name "Planboard
  Billing", and the password-reset template still opens with the old name
  and old voice.
- The downloadable onboarding PDF in the help centre is branded Planboard
  throughout, and the OAuth consent screen in the provider's console still
  shows the old name and logo.

None of these surfaces was missed through carelessness about the homepage —
they were missed because they were never listed. Under CL-702, a surface
not on the inventory is assumed missed, not assumed unaffected.

## After

The rebrand is reopened and an inventory is built first (CL-702) by crawling
the product and its repositories, covering rendered, data, downloadable,
and third-party surfaces as first-class rows. The search and sharing
surfaces are then swapped as data, not as decoration (CL-708):

| Surface | Where it lives | Fix under CL-708 / CL-702 |
|---|---|---|
| `og:image`, Twitter card image | Shared `<head>` template + social-card asset folder | New Northbeam card image deployed; fields re-validated with social-open-graph |
| Organization JSON-LD `name` / `logo` | Structured-data partial in the base layout | `name` set to the visible brand; `logo` URL updated and the file actually served at that URL replaced |
| Favicon + app icons | Static assets + web-app manifest | New mark exported at every inventoried size; manifest name updated |
| Invoice / receipt / reset emails | Transactional template set + sender-name setting | Templates swapped from the shared template source (CL-705); sender name changed to Northbeam Billing |
| Onboarding PDF | Help-centre download, v14 | Regenerated from the rebranded source and re-uploaded; old file replaced, not left alongside |
| OAuth consent screen | Identity provider's console | Name and logo changed in the provider console itself, then opened and checked there (CL-715) |

Verification is independent of how the pages look. G-CL-702 (the residue
scan) re-greps the code, the message catalogs, and the rendered HTML —
including `<title>`, meta, OG/Twitter fields, and JSON-LD — plus the
sitemap, the email templates, and the downloadable PDF, and it fetches the
declared Organization logo URL and the favicon to confirm they serve the
new mark. Every remaining "Planboard" hit must map to a recorded CL-706
exception (for example, the legal entity name in the privacy page, kept
under CL-707); an unmapped hit blocks launch. G-CL-705 later re-opens the
OAuth consent screen and the other third-party surfaces in their own
consoles, because a change in the product's codebase is not evidence that
a third-party surface changed (CL-715).

Note: corrects CL-702 and CL-708, via BAN-CL-703 — inventory every surface
before the first swap, swap search and social surfaces as structured data,
and verify the invisible surfaces separately from the visible pages.
