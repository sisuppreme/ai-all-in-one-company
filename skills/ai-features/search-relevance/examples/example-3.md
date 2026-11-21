# Example 3 — The zero-result dead end

## Before

```tsx
// ResultsPage.tsx
export function ResultsPage({ results, query }: Props) {
  return (
    <main>
      <SearchBox initialValue={query} />
      <Grid>
        {results.map((r) => (
          <Card key={r.id} item={r} />
        ))}
      </Grid>
    </main>
  );
}
```

When nothing matches, the grid renders empty space: no message, no sign of the three facet filters still applied from an earlier session, and no way to clear them. The user concludes search is broken; the zero-result query is not logged anywhere, so the team never learns it happened.

## After

```tsx
// ResultsPage.tsx — zero results are a state, not an absence
export function ResultsPage({ results, query, filters }: Props) {
  if (results.total === 0) {
    return (
      <main>
        <SearchBox initialValue={query} />
        <ActiveFilters filters={filters} onClear={clearFilters} />
        <EmptyState
          title={`No results for "${query}"`}
          body="Nothing matches with the current filters. Try removing a filter or checking the spelling."
          actions={[
            { label: "Clear all filters", onClick: clearFilters },
            { label: "Browse the full catalog", href: "/catalog" },
          ]}
        />
      </main>
    );
  }
  return (/* normal results grid */);
}
```

The empty state names the query, shows the active filters with a one-action clear, and offers a broader path; the query was already logged server-side, so it enters the next zero-result triage (AI-123) and the judged set.

## Note

Corrected under AI-126 and AI-127: a blank results area with invisible active filters violates BAN-AI-064 (DET-UX-025); zero results must explain themselves, show their constraints, and offer a working way out.
