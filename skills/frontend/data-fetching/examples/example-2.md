# Example 2 — Stale response overwriting a newer view

## Before

```jsx
function SearchResults({ term }) {
  const [results, setResults] = useState([]);
  useEffect(() => {
    fetch(`/api/search?q=${term}`)
      .then(r => r.json())
      .then(setResults);      // whichever response arrives LAST wins
  }, [term]);
  return <ResultsList results={results} />;
}
```

The user types "harbor", then deletes it and types "dock". The "harbor"
request is slower; it resolves after the "dock" response and overwrites the
list — the screen shows harbor results under a search box that says "dock".

## After

```jsx
import { useQuery } from '@tanstack/react-query';

function SearchResults({ term }) {
  const { data, isPending } = useQuery({
    queryKey: ['search', term],          // the key IS the parameter
    queryFn: ({ signal }) =>
      fetch(`/api/search?q=${encodeURIComponent(term)}`, { signal })
        .then(r => {
          if (!r.ok) throw new Error('search failed');
          return r.json();
        }),
    enabled: term.length > 0,
  });
  // Only the current key's data is ever rendered for this term; the
  // superseded request is aborted and its response can never land here.
  if (isPending) return <ResultsSkeleton />;
  return <ResultsList results={data} />;
}
```

Because rendering is bound to the current query key — and the stale request is
cancelled through its `AbortSignal` — arrival order no longer matters.

Note: corrects FE-204 — requests are keyed or cancellable so a stale response cannot overwrite a newer view.
