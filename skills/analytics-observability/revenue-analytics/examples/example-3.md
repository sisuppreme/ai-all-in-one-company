# Example 3 — The multi-currency total that meant nothing

## Before

The revenue report sums the month's charges into one cell:

```text
Total revenue: 61,480
  (USD charges: 41,200 · EUR charges: 20,280 — added as-is)
```

The EUR amounts were added at face value, as if 1 EUR = 1 USD. Next month the total drops even though both currencies grew, because the EUR share shrank. The "drop" triggers a week of investigation into a decline that never happened.

## After

Amounts stay in their transaction currency in the records, and the report shows its conversion explicitly:

```text
USD charges:            $41,200
EUR charges:            €20,280  → $21,902  (rate 1.0800, ECB ref. 2026-10-31)
Total (reporting USD):  $63,102
Refunds:                   -$940   (attributed to original charge periods)
Provider fees:           -$1,815   (shown separately, not netted)
```

The total is reproducible: anyone with the provider export and the stated rate lands on the same figure, and a mix shift can no longer masquerade as growth or decline.

Note: the Before violates AN-066 (currency is never silently converted); the After corrects it.
