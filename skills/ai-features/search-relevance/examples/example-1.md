# Example 1 — The same eight results for every query

## Before

```ts
// SearchBar.tsx — "Search the catalog"
const CATALOG_PREVIEW = [
  { id: 1, name: "Trail Shoes" }, { id: 2, name: "Rain Jacket" },
  { id: 3, name: "Wool Socks" },  { id: 4, name: "Day Pack" },
  { id: 5, name: "Head Lamp" },   { id: 6, name: "Water Filter" },
  { id: 7, name: "Tent 2P" },     { id: 8, name: "Stove" },
];

export function search(query: string) {
  const q = query.trim().toLowerCase();
  const hits = CATALOG_PREVIEW.filter((p) => p.name.toLowerCase().includes(q));
  return hits.length > 0 ? hits : CATALOG_PREVIEW; // "never show an empty page"
}
```

Every query is answered from an eight-item array baked into the page: a nonsense query returns the full list, and a product added to the real catalog this morning can never be found.

## After

```ts
// server/routes/search.ts — queries reach the real index
export async function search(query: string, filters: ActiveFilters) {
  const result = await searchIndex.query({
    text: query,
    filters,
    ranking: rankingConfig.current, // versioned signals + weights (AI-132)
  });
  logSearchQuery({ query, filters, resultCount: result.total }); // feeds AI-123/AI-124
  return result; // total === 0 renders the recovery state, never a fixture (AI-126)
}
```

The query runs against the server index over the full dataset, counts come from the same query as the results, and a record created through the product is findable immediately.

## Note

Corrected under AI-131: returning a hard-coded list regardless of the query violates BAN-AI-061 (DET-FAKE-008); a real search varies with the query and the data, and an honest empty result beats a canned full one.
