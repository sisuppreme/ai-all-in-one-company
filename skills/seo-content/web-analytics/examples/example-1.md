# Example 1 — The "AI traffic" line nobody could reproduce

## Before

The monthly SEO report goes out with a new line near the top: "AI Overview
visits: 1,240 (+18% MoM)". It looks precise, so nobody questions it. When a
teammate tries to find the figure in Search Console, it is not there — no
report, filter, or dimension produces it. The number came from a dashboard
widget that estimated a share of overall clicks and labeled the estimate as
visits. Two decisions (a brief and a refresh) were already justified with it.

## After

The line is cut and the report is reissued. AI-feature appearances are
reported the way Google reports them: inside Search Console's overall
Performance data, described as part of that total, never split out. Every
figure in the reissued report carries its platform, property, report, and
date range, and the G-CO-124 audit re-pulls two of them to the same values.
The brief and refresh the invented line justified are re-decided on the
real query and page data — one survives, one does not.

Note: corrects CO-248 — AI-feature traffic is read where Google reports it, inside overall Performance data; a standalone "AI traffic" figure is invented and fails BAN-CO-121.
