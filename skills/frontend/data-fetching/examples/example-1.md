# Example 1 — Per-component fetches replaced by one keyed query

## Before

```jsx
function OrderCount() {
  const [n, setN] = useState(null);
  useEffect(() => {                      // fetch #1 for /api/orders
    fetch('/api/orders').then(r => r.json()).then(d => setN(d.length));
  }, []);
  return <p>{n} orders</p>;
}

function OrderList() {
  const [orders, setOrders] = useState([]);
  useEffect(() => {                      // fetch #2 for the same endpoint
    fetch('/api/orders').then(r => r.json()).then(setOrders);
  }, []);
  return <ul>{orders.map(o => <li key={o.id}>{o.id}</li>)}</ul>;
}
```

One page, two identical requests, two independent loading states, and no
shared cache — navigate away and back and both fetch again.

## After

```jsx
import { useQuery } from '@tanstack/react-query';

const fetchOrders = () =>
  fetch('/api/orders').then(r => {
    if (!r.ok) throw new Error('orders failed');
    return r.json();
  });

export const ordersQuery = {
  queryKey: ['orders'],
  queryFn: fetchOrders,
  staleTime: 30_000, // orders change on the scale of minutes, not seconds
};

function OrderCount() {
  const { data } = useQuery(ordersQuery);
  return <p>{data?.length ?? '…'} orders</p>;
}

function OrderList() {
  const { data, isPending, isError } = useQuery(ordersQuery);
  if (isPending) return <OrderListSkeleton />;
  if (isError) return <ErrorState retryLabel="Try again" />;
  return <ul>{data.map(o => <li key={o.id}>{o.id}</li>)}</ul>;
}
```

Both components subscribe to the same key, so the endpoint is requested once,
the result is shared from the cache, and the loading and error outcomes render
through the view's state matrix instead of being re-invented per component.

Note: corrects FE-201 and FE-202 — all server reads go through the query layer, keyed by a scheme that mirrors the API.
