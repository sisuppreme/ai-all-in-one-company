# Example 1 — The find-and-replace rename

Scenario: BillNest, a live invoicing SaaS, is renamed to Tallyro under a signed
decision record (CL-701). The registered legal entity, BillNest Ltd, does not
change. The product's best-performing landing page is `/billnest-pricing`,
linked from partner sites and indexed under that exact path.

## Before

On launch morning a developer runs a repository- and CMS-wide substitution of
"BillNest" → "Tallyro" and ships the result the same day. This is the global
find-and-replace banned by BAN-CL-701, and it breaks four different surfaces
in four different ways from a single command:

- The URL slug is renamed with everything else: `/billnest-pricing` becomes
  `/tallyro-pricing`, with no redirect. Partner links, bookmarks, and the
  indexed URL now return a 404 — a direct violation of CL-704, which says a
  rebrand changes presentation, not addressing.
- The Terms page now names "Tallyro Ltd" as the contracting party. No such
  entity exists; the registered company is still BillNest Ltd, so brand copy
  has been substituted into a legal surface.
- The 2024 changelog entry "BillNest raises its free-plan invoice limit" is
  rewritten to claim Tallyro did so in 2024, before the new name existed —
  historical content falsified as a side effect.
- A third-party integration key containing the string `billnest` is renamed
  in a config file, so the integration stops matching the value registered
  in the provider's console and fails silently.

None of this is caught before launch, because there was no inventory to check
the change against: nobody had written down, per surface, what the old value
was, what the new value should be, or who owned the change (CL-703).

## After

The rename is re-run under CL-703 and CL-704, one inventory row at a time.
Each row states where the old identity lives, the exact replacement value,
and an owner; rows with no decided new value are marked `blocked` and hold
that surface's schedule instead of being guessed at swap time.

| Surface | Old value | New value | Decision | Owner |
|---|---|---|---|---|
| Landing-page URL | `/billnest-pricing` | — | `keep` under CL-704; not a migration item | Web lead |
| Header logo + wordmark | BillNest logo, `logo-header.svg` | Tallyro logo from the CL-701 record | Swap via shared component (CL-705) | Design-system owner |
| Terms, contracting party | BillNest Ltd | BillNest Ltd | `keep` — legal reviewer confirms the entity is unchanged (CL-707) | Legal reviewer |
| 2024 changelog entry | "BillNest raises…" | "BillNest raises…" | `kept by exception` — historical archive under CL-706 | Content owner |
| Integration key | `billnest` (provider-registered) | — | `keep` under CL-704; identifiers do not change for identity alone | Integrations owner |
| In-app name strings | `app.name = "BillNest"` in `en` / `ur` / `ar` catalogs | `"Tallyro"` in all three catalogs | Swap in the message catalogs, once (CL-705, CL-710) | i18n owner |

The URL row is the point of the exercise: because the inventory forces an
explicit decision per surface, `/billnest-pricing` is recorded as `keep`
before any edit happens, instead of being renamed because a text tool
could not tell a slug from a headline.

Verification: G-CL-701 diffs a fresh crawl and catalog grep for "BillNest"
against the inventory — every hit must map to a row, and no row may still be
`blocked`. G-CL-703 then diffs the production URL set before and after
launch and asserts `/billnest-pricing` still returns its pre-launch status,
with zero new 404s on the top landing pages.

Note: corrects CL-703 and CL-704, via BAN-CL-701 — swap per inventory row,
where each surface's context decides whether and how it changes; never
rename by global substitution, and never rename a URL for identity alone.
