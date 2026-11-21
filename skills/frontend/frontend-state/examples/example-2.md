# Example 2 — Filters lost on refresh moved into the URL

## Before

```jsx
function ReportsPage() {
  const [status, setStatus] = useState('open');
  const [page, setPage] = useState(1);
  // Filtering 200 support tickets by status and page lives only in memory.
  // Refresh, the back button, or sharing the link resets both values,
  // so a link sent to a colleague shows them a different view.
}
```

## After

```jsx
import { useSearchParams } from 'react-router-dom';

function ReportsPage() {
  const [params, setParams] = useSearchParams();
  const status = params.get('status') ?? 'open';
  const page = Number(params.get('page') ?? 1);

  const setStatus = (next) =>
    setParams({ status: next, page: '1' }); // changing filter resets paging

  // The URL is now the state: /reports?status=open&page=2 survives
  // refresh, works with back/forward, and shares exactly this view.
}
```

The component's interface is unchanged for the user, but the state now lives
where shareable state belongs — in the URL — instead of in memory that any
navigation destroys.

Note: corrects FE-186 — shareable view state (filters, pagination) lives in the URL.
