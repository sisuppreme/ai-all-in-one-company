# Example 1 — Nine-slice pie replaced by a labeled bar chart

Corrects rules **FE-262** (type matches the message) and **FE-264** (no pie with more than 5 slices).

Message: "Support tickets by category last quarter — password resets are the largest category by far."

## Before

```html
<!-- A 3D pie with nine slices. Shares are unreadable, three
     slices are pulled out for decoration, and two categories
     share nearly the same color. -->
<canvas id="ticketsChart" width="480" height="320"></canvas>
<script>
  new Chart(document.getElementById("ticketsChart"), {
    type: "pie",
    data: {
      labels: ["Password reset", "Billing", "Login", "Exports", "API",
               "Mobile app", "Email", "Permissions", "Other"],
      datasets: [{
        data: [34, 18, 12, 9, 8, 6, 5, 4, 4],
        backgroundColor: ["#f00", "#0f0", "#00f", "#ff0", "#f0f",
                          "#0ff", "#fa0", "#a0f", "#0a5"]
      }]
    },
    options: { plugins: { legend: { position: "right" } } }
  });
</script>
```

## After

```html
<!-- A horizontal bar chart: categories compare directly, values
     are labeled, one accent carries the story, rest is context. -->
<figure>
  <figcaption>Password resets were the largest ticket category last quarter (34%)</figcaption>
  <svg viewBox="0 0 520 300" role="img"
       aria-label="Bar chart of support tickets by category, last quarter">
    <!-- bar width = percent × 4 px; accent for the story, gray for context -->
    <g font-size="13">
      <text x="0" y="20">Password reset</text>
      <rect x="150" y="6" width="136" height="16" fill="#2456a6"></rect>
      <text x="292" y="20">34%</text>

      <text x="0" y="50">Billing</text>
      <rect x="150" y="36" width="72" height="16" fill="#9aa3ad"></rect>
      <text x="228" y="50">18%</text>

      <text x="0" y="80">Login</text>
      <rect x="150" y="66" width="48" height="16" fill="#9aa3ad"></rect>
      <text x="204" y="80">12%</text>

      <text x="0" y="110">Exports</text>
      <rect x="150" y="96" width="36" height="16" fill="#9aa3ad"></rect>
      <text x="192" y="110">9%</text>

      <text x="0" y="140">API</text>
      <rect x="150" y="126" width="32" height="16" fill="#9aa3ad"></rect>
      <text x="188" y="140">8%</text>

      <text x="0" y="170">Mobile app</text>
      <rect x="150" y="156" width="24" height="16" fill="#9aa3ad"></rect>
      <text x="180" y="170">6%</text>

      <text x="0" y="200">Email</text>
      <rect x="150" y="186" width="20" height="16" fill="#9aa3ad"></rect>
      <text x="176" y="200">5%</text>

      <text x="0" y="230">Permissions</text>
      <rect x="150" y="216" width="16" height="16" fill="#9aa3ad"></rect>
      <text x="172" y="230">4%</text>

      <text x="0" y="260">Other</text>
      <rect x="150" y="246" width="16" height="16" fill="#9aa3ad"></rect>
      <text x="172" y="260">4%</text>
    </g>
  </svg>
  <p>Share of support tickets by category, Q3. Source: help-desk export, 1 Oct.</p>
</figure>
```

Note: the message is a comparison, so the chart is bars — ranked, directly labeled, one accent color, with the source line FE-266 requires. The pie hid exactly the comparison the message needed.
