# Example 1 — The two-day "winner"

## Before

The pricing-page headline test launched on Monday with no register entry and no end date. On Wednesday morning the dashboard showed variant B ahead by 18% on signups at p = 0.04, on roughly 400 visitors per variant. The test was stopped, B was shipped to all traffic, and the weekly report announced: "New headline wins — +18% conversions." Three weeks later, signup rate sat exactly where it had been before the test.

## After

The experiment is registered before launch (EXP-014): hypothesis — "Visitors hesitate because the headline names the product, not the outcome; an outcome headline will raise completed signups"; primary metric — completed signup rate; pre-computed sample — 6,200 visitors per variant; split 50/50; end date — 14 days after launch, covering two full weekly cycles. Interim dashboards are not read for decisions. At the horizon, the SRM check passes (p = 0.42), and the read shows B at +2.1% with a 95% confidence interval of −3.4% to +7.6%: inconclusive. The register entry records the inconclusive-extend decision and the follow-up hypothesis; nothing ships, and no win is reported.

Note: corrects CO-263 (no peeking decisions — the read happens at the pre-registered horizon) and CO-266 (SRM check passed before any result was read).
