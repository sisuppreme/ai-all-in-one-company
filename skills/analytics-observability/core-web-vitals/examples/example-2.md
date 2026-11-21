# Example 2 — "Average LCP 2.3 s" while mobile checkout failed

## Before

The monthly performance summary publishes one number for the whole site:

```text
Core Web Vitals: LCP 2.3 s average — GOOD. INP 180 ms. CLS 0.08.
```

The average is computed over all templates and both device classes, weighted by traffic — and the homepage takes most of the traffic. Blended away inside it: the mobile checkout template runs LCP p75 of 4.1 s and the mobile product template runs INP p75 of 340 ms. The two templates where users pay are failing, and the summary certifies them healthy.

## After

The summary publishes the per-template, per-device-class table, and the worst key template is the headline:

```text
Template      Device   LCP p75   INP p75   CLS p75   Status
home          mobile   2.1 s     170 ms    0.06      good
home          desktop  1.4 s     120 ms    0.04      good
product       mobile   2.9 s     340 ms    0.09      FAILING (INP)
product       desktop  1.9 s     150 ms    0.05      good
checkout      mobile   4.1 s     210 ms    0.07      FAILING (LCP)
checkout      desktop  2.4 s     160 ms    0.06      good
Headline: checkout (mobile) is the worst key template — defect opened.
```

Note: the Before violates AN-222 (report per template and per device class; no site-wide blended figure); the After corrects it.
