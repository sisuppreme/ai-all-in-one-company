# Example 3 — The page that existed only after JavaScript

## Before

A product page renders its description, price, and links with client-side
JavaScript. A developer checks view-source, sees the empty container
`<div id="app"></div>`, and is told "Google runs JavaScript, it will be
fine." Nobody verifies the rendered result. In production, robots.txt —
copied from a tutorial — contains `Disallow: /static/js/`, so the crawler
can never fetch the bundle that builds the page. The indexed version is an
empty shell: no text, no links, no canonical.

## After

The page is checked the way the rule requires: URL Inspection's rendered
HTML. The rendered output confirms the failure — the container is empty and
the canonical is absent. Two fixes follow:

1. robots.txt stops blocking the render assets: the `/static/js/` Disallow
   line is removed (CO-004).
2. The template moves to server rendering for its indexable content, so the
   primary text ships in the initial HTML (CO-002).

The rendered-HTML check is re-run and now shows the full description, price,
links, and a self-referencing canonical. The template is added to the
rendered-content verification sample for every future release.

Note: corrects CO-003 — JavaScript-dependent content is verified in the rendered HTML, never assumed from source or local builds.
