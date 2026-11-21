# Example 3 — Canvas-only chart given a data-table alternative

Corrects rule **FE-268** (every chart ships an accessible alternative).

## Before

```html
<!-- A canvas bitmap and nothing else. Screen readers get silence,
     search engines get nothing, and the numbers exist only as pixels. -->
<canvas id="signups" width="600" height="300"></canvas>
<script>
  drawLineChart(document.getElementById("signups"),
    [120, 150, 142, 190, 230, 265]); // Jan–Jun, unlabeled, unsourced
</script>
```

## After

```html
<!-- The canvas stays for sighted users; the same data ships as a
     real table the chart points to with aria-describedby. -->
<figure>
  <figcaption>Signups grew from 120 in January to 265 in June</figcaption>
  <canvas id="signups" width="600" height="300"
          role="img" aria-describedby="signups-table"
          aria-label="Line chart of monthly signups, January to June"></canvas>
  <table id="signups-table">
    <caption>Monthly signups, January–June. Source: product analytics export, 1 July.</caption>
    <thead>
      <tr><th scope="col">Month</th><th scope="col">Signups</th></tr>
    </thead>
    <tbody>
      <tr><th scope="row">January</th><td>120</td></tr>
      <tr><th scope="row">February</th><td>150</td></tr>
      <tr><th scope="row">March</th><td>142</td></tr>
      <tr><th scope="row">April</th><td>190</td></tr>
      <tr><th scope="row">May</th><td>230</td></tr>
      <tr><th scope="row">June</th><td>265</td></tr>
    </tbody>
  </table>
</figure>
```

Note: the before version fails gate G-FE-131 — a chart root with no table or text alternative. The after version carries the identical numbers in markup, so the chart's message survives without sight or canvas support.
