# Example 3 — The dashboard that never moved

## Before

```text
Admin panel → AI costs (this month)
  Writing assistant …… <one tidy figure>
  Support summarizer … <one tidy figure>
  Source: config/ai-costs.yaml, written at launch from expected volumes
  ("about N requests a day at roughly the usual price").

Actual usage tripled after a launch announcement. The panel showed the
same figures all month, because nothing in it was connected to a single
real call. The overrun was discovered from the provider invoice.
```

The numbers were estimates typed in once and rendered forever — a dashboard with frozen numbers presented as measured consumption.

## After

```text
Every wrapper call emits its trace: feature, model ID, prompt version,
tokens in, tokens out (ai-observability). The cost panel is computed
from those traces for the displayed period:

  cost(feature) = Σ tokens × price sheet
  price sheet: config/price-sheet.yaml — source: provider pricing page,
  last checked: <date recorded in the file>

Reconciliation (G-AI-093): a known set of test calls is run, and the
panel's total is recomputed from the stored traces — exact match.
The monthly report lists each feature's spend against its budget and
its unit cost per successful task (AI-190); the feature that tripled
is flagged for a routing review the week it happens, not at invoice time.
```

## Note

Violates AI-182 and AI-190 (BAN-AI-092): cost figures rendered from launch-day constants instead of metered usage. Corrected by computing every figure from per-call traces multiplied by the operator's dated price sheet, and reconciling the report against the traces.
