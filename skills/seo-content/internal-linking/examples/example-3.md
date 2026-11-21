# Example 3 — Every blog post linking through a redirect

## Before

The docs moved from `/help` to `/docs` eight months ago, with a 301 redirect left in place. Forty blog posts still link to `/help/*` URLs. Every reader and crawler following those links takes an extra hop; the G-CO-102 scan reports 40 internal links resolving through redirects, and when the redirect rule is later dropped during a hosting migration, all 40 become 404s at once.

## After

The link update ships in the same change as the move: all 40 posts are rewritten to link the canonical `/docs/*` URLs directly, and the redirect is kept only for external bookmarks. The G-CO-102 scan reports zero internal links with a redirect hop, so removing the redirect later cannot break any internal path.

Note: violates CO-206 (link the canonical URL directly) and CO-208 (link changes ship with the move); corrected by updating every internal link in the same change.
