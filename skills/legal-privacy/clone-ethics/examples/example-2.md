# Example 2 — "Licensed", approved by the harvester

## Before

```text
Harvesting manifest (excerpt)
hero-team.jpg        licensed   approver: harvest-run-7   note: "was on old site"
studio-tour.mp4      licensed   approver: harvest-run-7   note: "client asset?"
vendor-font.woff2    licensed   approver: harvest-run-7   note: —
```

The same run that harvested the assets also approved them as `licensed`, on the strength of "they were already on the site" — no license text, no scope, no transferability check.

## After

```text
Harvesting manifest (excerpt)
hero-team.jpg        replace    approver: D14-review      note: stock photo, no
                                  license on file; shoot or license fresh
studio-tour.mp4      licensed   approver: D14-review      evidence:
                                  docs/rights/studio-tour-grant.pdf — client's own
                                  production, grant covers migration reuse
vendor-font.woff2    replace    approver: D14-review      note: vendor license is
                                  non-transferable; substitute an open font
```

Each `licensed` row now carries attached evidence and a separate approver; anything without evidence defaults to `replace`.

## Note

Violates LG-184 and LG-185 (every asset needs an approved rights decision, and `licensed` can never be self-approved by the harvesting flow); corrected by routing decisions to a separate approver with evidence attached.
