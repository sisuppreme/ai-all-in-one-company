# Example 1 — Prose budget to numeric budget file

## Before

From the project plan, "Performance" section:

> Pages should load fast and stay lightweight. Avoid heavy pages.

No budget file exists in the repo. The checkout template ships 900 KB of JavaScript and a 4 MB hero video, and nothing flags either, because no number was ever set.

## After

`performance-budget.json` committed at the repo root, one entry per template:

```json
{
  "templates": {
    "checkout": {
      "lcp_ms": 2500,
      "inp_ms": 200,
      "cls": 0.1,
      "javascript_kb": 300,
      "total_weight_kb": 1200,
      "image_weight_kb": 500,
      "requests": 60,
      "third_party": { "javascript_kb": 100, "requests": 10 }
    }
  },
  "api_p95_ms": { "POST /checkout": 800 }
}
```

The checkout template now breaches the JavaScript and image lines, which is the budget doing its job: the breach exits by fixing the weight or by a written waiver, not by silence.

Note: corrects AN-201 and AN-202 — budgets are numeric limits in a committed file, per template.
