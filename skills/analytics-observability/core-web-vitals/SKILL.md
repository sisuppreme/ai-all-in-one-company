# core-web-vitals

## Metadata

- **Owner department:** D12 Analytics & Observability (AN)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** web.dev, "Web Vitals" — https://web.dev/articles/vitals ; PROJECT_ANATOMY.md, "Performance budgets"
- **Depends on:** product-analytics (owns the RUM collection pipeline and consent gating), performance-budgets (owns the numeric budget file and CI enforcement)
- **Feeds into:** performance-optimization (owns the fix loop), dashboards, alerting

## When to use / Do NOT use

- **Use when:** measuring, reporting, or fixing a web product's Core Web Vitals — setting up real-user monitoring, reading a field report, deciding whether a template passes, or diagnosing a failing LCP, INP, or CLS.
- **Do NOT use when:** the question is the numeric budget file or its CI assertions (performance-budgets owns budgets; this skill owns the field verdict the budgets mirror), the hands-on optimization change itself (performance-optimization owns the fix loop; D3/D4/D5 own implementation), or synthetic load testing of APIs (D8 load-testing owns test craft).

## Rules

1. **AN-221 — Field data is the verdict.** A template's Core Web Vitals status is its real-user field data at the 75th percentile over a rolling 28-day window, against the web.dev thresholds: LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1. Lab data diagnoses; it never overrules a failing field score and is never reported as the user experience.
2. **AN-222 — Report per template and per device class.** Field results are reported for each key page template (home, listing, detail, checkout, app shell — the project's template inventory), separately for mobile and desktop. No site-wide blended figure is published; the average of a fast homepage and a slow checkout is a lie about both.
3. **AN-223 — All three must be good to pass.** A template passes only when LCP, INP, and CLS are all in the "good" band at p75. Two good vitals do not compensate for one poor one, and a template's status names the failing vital, not just "slow."
4. **AN-224 — Every key template is instrumented.** Real-user monitoring (the web-vitals library or the platform's RUM) collects LCP, INP, and CLS on every template in the inventory, tagged with template, device class, and country. A template with no field data is reported as unmeasured — never as passing.
5. **AN-225 — Reproduce in the lab before fixing.** For each failing template, a throttled lab run (a mid-tier mobile device profile on a throttled network, not the office desktop) reproduces the failure mode before optimization work begins. No reproduction, no fix attempt: a lab run that cannot reproduce the field failure is evidence the diagnosis is wrong.
6. **AN-226 — Decompose the metric before fixing it.** Diagnosis names the dominant subpart: LCP decomposes into time to first byte, resource load delay, resource load duration, and element render delay; INP into the long tasks blocking the main thread; CLS into the specific elements that shift. Fixes target the dominant subpart, never "the metric" in the abstract.
7. **AN-227 — INP is the responsiveness vital.** Budgets, reports, and fixes are written against INP, which replaced FID as the responsiveness vital on March 12, 2024. No document, budget, or dashboard tracks FID as a current vital; a stale FID reference is a defect to remove, not a metric to report.
8. **AN-228 — CLS fixes are structural.** Width and height (or aspect-ratio space) are reserved for images, embeds, ads, and async slots before they load. Content is never injected above existing rendered content except in direct response to user input within the same interaction.
9. **AN-229 — The LCP element is named and prioritized per template.** Each template's report names its LCP element. That resource is prioritized — discoverable in the initial HTML, not lazy-loaded, not behind a client-side render chain — and hero media is sized to the template's budget, not shipped at source weight.
10. **AN-230 — Every fix is verified in the field.** A fix ships with the field window that will judge it: the template's p75 is re-read over the following 28-day window (or the shorter stated window once enough visits accumulate). A fix that does not move field p75 is reverted or reworked, not celebrated on the strength of its lab run.
11. **AN-231 — Low-traffic templates report "insufficient data."** When a template lacks the visits to form a meaningful p75, the report says so and judges it on the lab-plus-RUM hybrid: throttled lab runs plus whatever field samples exist, over a longer window. Thresholds never silently pass — or fail — on noise.
12. **AN-232 — Breaches become tracked defects.** The field report runs on a recorded cadence. Any template outside "good" opens a defect naming the template, the failing vital, and its p75; the defect closes only on field evidence under AN-230, not on a lab screenshot.

## BAN list

- **BAN-AN-111 — Lab score as the verdict.** Banned: reporting a Lighthouse score or a desktop lab timing as the product's Core Web Vitals result, in a status report, README, or sales page. Defeats: DET-INF-011. Bad: the launch report announces "Performance: 98" from one desktop Lighthouse run on the office connection while field mobile LCP p75 is 4.6 s. Instead: report field p75 per template and device class against the AN-221 thresholds; cite lab runs only as diagnosis. Severity: BLOCK.
- **BAN-AN-112 — Homepage-only measurement.** Banned: measuring, optimizing, or quoting vitals for the homepage alone while the templates users actually convert on go unmeasured. Defeats: DET-VIS-044. Bad: the homepage is tuned to a 1.8 s LCP for the launch screenshot; the checkout template — never instrumented — runs a 5 s LCP for a month. Instead: instrument and report every template in the inventory (AN-222, AN-224) before quoting any vitals figure. Severity: BLOCK.
- **BAN-AN-113 — The site-wide blended number.** Banned: publishing one averaged vitals figure for the whole site, blending templates and device classes into a single passing score. Defeats: DET-INF-011. Bad: "Average LCP 2.3 s — good" across the site, computed over a homepage that takes 90% of traffic, while the mobile product page sits at 4.1 s. Instead: publish the per-template, per-device-class table (AN-222); the worst key template is the headline, not the mean. Severity: BLOCK.
- **BAN-AN-114 — Unbudgeted hero payload.** Banned: shipping hero media at source weight — a multi-megabyte autoplay video or uncompressed banner image — because it "looked fine" on a fast connection. Defeats: DET-INF-027. Bad: a 4 MB hero video ships; on the office fiber it paints instantly, on real mobile networks it is the LCP element at 6 s. Instead: size hero media to the template budget, compress and poster-frame video, and verify under the throttled lab profile (AN-225, AN-229). Severity: BLOCK.
- **BAN-AN-115 — Late injection above rendered content.** Banned: inserting banners, cookie notices, promo bars, or async embeds above already-rendered content so the page jumps under the reader's finger. Defeats: DET-VIS-039. Bad: a promo bar loads two seconds after first paint and pushes the article — and the button the user was tapping — down by its full height; CLS p75 is 0.31. Instead: reserve the slot's space before render or overlay without reflowing content (AN-228). Severity: WARN.

## Gates

- **G-AN-111 — Field report check.** Verifies: AN-221, AN-222, AN-223. Check: automated — a scheduled job queries the RUM store for the trailing 28 days and emits, per template in the inventory and per device class, the p75 of LCP, INP, and CLS against the thresholds (LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1). Pass: every key template is "good" on all three vitals, or carries an open defect under AN-232. Fail: block any release note or status report that claims performance health; open the defects. Before a production environment is provisioned, this gate's disposition is a recorded provisioning waiver per the §6.3 protocol; it unblocks when the production site is live, real-user monitoring is collecting field data, and the first 28-day window has matured. Recorded in: progress.md.
- **G-AN-112 — RUM integrity check.** Verifies: AN-224, AN-231. Check: automated — for each template, compare RUM beacon volume to pageview volume for the same window; flag any template whose beacon ratio falls below the project's stated coverage floor, and mark templates below the p75 sample floor as "insufficient data." Pass: every key template is either measured at or above the floor or explicitly reported unmeasured/insufficient. Fail: block the field report from marking that template passing. Recorded in: progress.md.
- **G-AN-113 — Lab reproduction and template lab run.** Verifies: AN-225, AN-226, AN-229. Check: automated — run Lighthouse CI (`lhci autorun`) against a staging build for every key template under the throttled mobile profile, asserting the budget file's LCP and CLS values on the median of multiple runs; for each field-failing template, confirm the lab run reproduces the failing vital and the report names its dominant subpart. Pass: all key templates are lab-run, and every field failure has a reproduction plus a named subpart. Fail: block optimization work on unreproduced failures. Recorded in: progress.md.
- **G-AN-114 — Threshold and vital currency check.** Verifies: AN-221, AN-227. Check: automated — grep the repo's budgets, reports, and dashboards for "FID" as a tracked vital and for threshold values; assert the only responsiveness vital is INP and the asserted thresholds read LCP 2.5 s, INP 200 ms, CLS 0.1. Pass: zero FID references as a current vital and thresholds match. Fail: block the change until the stale vital or threshold is corrected. Recorded in: progress.md.
- **G-AN-115 — Field verification of fixes.** Verifies: AN-230. Check: automated — for each closed vitals defect, pull the template's field p75 for the post-fix window and compare it with the pre-fix p75 recorded on the defect. Pass: the failing vital moved into "good," or the defect is reopened as reverted/reworked with the reason recorded. Fail: the defect cannot close on lab evidence alone. Recorded in: progress.md.

## Anti-patterns

- **Score chasing.** Reloading the lab tool with different settings, extensions disabled, or a faster profile until a green number appears, then screenshotting that run. Catch it: ask which field window the claim rests on — if the answer is a lab run, it is not a result (AN-221).
- **Optimizing the metric in the abstract.** "Improve LCP" work that compresses everything a little instead of decomposing the failing template first. Catch it: require the named dominant subpart (AN-226) before any fix is scheduled.
- **The quiet template.** Attention and fixes concentrate on the homepage because it is the demo surface, while a low-traffic template fails unnoticed. Catch it: read the field report's worst row first, not its first row (AN-222).
- **Premature celebration.** A fix announced as done the day it merges, weeks before field data can judge it. Catch it: every fix names its judging window up front (AN-230); until that window reads, the status is "awaiting field verdict."

## Examples

- [Example 1 — The 4 MB hero video that "looked fine on the office connection"](examples/example-1.md) — violates/corrects AN-221.
- [Example 2 — "Average LCP 2.3 s" while mobile checkout failed](examples/example-2.md) — violates/corrects AN-222.
- [Example 3 — The promo bar that pushed the page under the reader's finger](examples/example-3.md) — violates/corrects AN-228.

## Recall anchors

- Field is the verdict; lab is the flashlight.
- Per template, per device class — never one blended number.
- All three good, or the template is failing.
- Unmeasured is not passing.
- A fix is done when field p75 moves, not when it merges.

## Checklist

- [ ] Field p75 for LCP, INP, and CLS is reported per key template, mobile and desktop separately, over the rolling 28-day window (G-AN-111).
- [ ] Every key template is instrumented, or explicitly reported unmeasured / insufficient data (G-AN-112).
- [ ] Every field-failing template has a throttled lab reproduction and a named dominant subpart (G-AN-113).
- [ ] No budget, report, or dashboard tracks FID; thresholds read LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1 (G-AN-114).
- [ ] Each template's LCP element is named, prioritized, and sized to budget (AN-229).
- [ ] Images, embeds, and async slots reserve their space before load; nothing injects above rendered content (AN-228).
- [ ] Every closed vitals defect closed on post-fix field evidence, not a lab run (G-AN-115).
- [ ] Every template outside "good" has an open tracked defect naming the failing vital and its p75 (AN-232).
