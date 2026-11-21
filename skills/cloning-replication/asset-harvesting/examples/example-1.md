# Example 1 — Photo library shipped vs. recreate verdict

## Before

The rebuild's gallery ships with 46 product photographs bulk-downloaded from the target site's media folder. The manifest has one line — "images: from old site" — with no per-file rows and no rights decisions. The photographs are a photographer's copyrighted work; the client licenses the site's text from its agency but never held the photo rights.

## After

Each photograph has a manifest row (source URL, capture date, checksum) and a rights decision. The license check finds the photo rights sit with the photographer, not the client, so all 46 rows are decided `recreate`: the rebuild ships with a new shoot of the client's own products in the same slots and crops the design system specifies. The harvested originals stay in the WARC capture as evidence and never enter the ship folders; G-CL-034 verifies none of them did.

## Note

Corrected under CL-066: only `owned`/`licensed` assets ship as-is — copyrighted photography is recreated or replaced, never silently reused (BAN-CL-032).
