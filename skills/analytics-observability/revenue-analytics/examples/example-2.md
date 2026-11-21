# Example 2 — Two revenue totals, one provider truth

## Before

Two dashboards disagree about October revenue, and both are quoted in the same week:

```text
Growth dashboard (analytics events):   $48,210
Finance sheet (typed from memory):     $47,500
Payment provider (settled charges):    $45,930
```

The growth team defends the event total — "the events are what users did" — and the gap is waved away as "probably fees." Nobody can say which transactions make up the $2,280 difference.

## After

The scheduled reconciliation (gate G-AN-031) diffs the event pipeline against the provider export and classifies every cent of the gap:

```text
Analytics events total:        $48,210
Refunds (event never fires):   -$1,140
Disputes lost:                   -$620
Missed webhooks (2 charges):     -$340
Test-mode checkout:              -$180
Provider total:                $45,930  ✓ explained difference: $0
```

The provider figure is the one reported (AN-061); the missed-webhook and test-mode items become pipeline fixes — a webhook replay and a source-query filter (AN-064) — not permanent footnotes.

Note: the Before violates AN-061 (the provider of record wins); the After corrects it.
