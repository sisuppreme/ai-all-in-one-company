# Example 1 — The MRR number typed into the deck

## Before

The monthly update deck carries a revenue slide built by hand:

```text
MRR: $12,400
Revenue (October): $13,050
```

Both figures were typed from a spreadsheet the founder maintains. The spreadsheet was last updated three weeks ago; since then 14 subscriptions churned and 9 started. The deck, the spreadsheet, and the payment provider now hold three different numbers, and the deck's is the one investors saw.

## After

The slide is generated from the reporting query over the provider's records, under the written definition:

```text
Metric: mrr_collected
Definition: sum of the current period's successful subscription charges,
            net of refunds attributed to their original charge period;
            trials and past-due subscriptions contribute 0.
Source: payment provider charge + refund records (live mode only)
Last reconciliation: 2026-11-01 06:00 — unexplained difference $0.00
```

The figure moves when subscriptions change, and the slide states its source and freshness instead of presenting a typed constant.

Note: the Before violates AN-071 (figures are computed, never typed); the After corrects it.
