# Example 2 — Truncated, unsourced bars replaced by a zero-based sourced chart

Corrects rules **FE-263** (bar axes start at zero) and **FE-266** (labels, units, source, date).

Message: "Customer satisfaction was nearly identical across both plans last year."

## Before

```html
<!-- Axis starts at 40: the 44% bar towers over the 41% bar,
     manufacturing a difference the data does not contain.
     No units, no source, no date. -->
<svg viewBox="0 0 300 200" role="img" aria-label="Satisfaction chart">
  <rect x="60"  y="20"  width="60" height="160" fill="#2456a6"></rect>
  <rect x="180" y="80"  width="60" height="100" fill="#9aa3ad"></rect>
  <text x="70"  y="195">Pro 44%</text>
  <text x="185" y="195">Basic 41%</text>
</svg>
```

## After

```html
<!-- Zero-based axis: the bars now honestly show a 3-point gap.
     Axis, units, source, and date are all on the chart. -->
<figure>
  <figcaption>Satisfaction was nearly identical on both plans in 2025</figcaption>
  <svg viewBox="0 0 300 220" role="img"
       aria-label="Bar chart: satisfied customers, Pro plan 44 percent, Basic plan 41 percent">
    <!-- scale: 100% = 160 px, baseline at y=180 -->
    <line x1="40" y1="180" x2="290" y2="180" stroke="#444"></line>
    <rect x="80"  y="109.6" width="60" height="70.4" fill="#2456a6"></rect>
    <rect x="190" y="114.4" width="60" height="65.6" fill="#9aa3ad"></rect>
    <text x="88"  y="100">44%</text>
    <text x="198" y="105">41%</text>
    <text x="80"  y="198">Pro</text>
    <text x="190" y="198">Basic</text>
    <text x="40"  y="214">Share of customers rating 4 or 5 out of 5</text>
  </svg>
  <p>Source: annual customer survey, n = 1,204, fielded November 2025.</p>
</figure>
```

Note: the before version is BAN-FE-132 — a 40-point baseline turned a 3-point gap into a visual rout. Zero-based, the same data tells the true story, and the source line makes it checkable.
