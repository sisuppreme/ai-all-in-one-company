# Example 2 — Missing catch-all replaced by a designed 404 route

Corrects rule **FE-224** (unknown paths render the designed 404).

## Before

```jsx
// routes.jsx — no catch-all. An unmatched path renders the
// layout shell with an empty <Outlet />: header, footer, blank middle.
const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />,
    children: [
      { index: true, element: <Home /> },
      { path: "pricing", element: <Pricing /> },
    ],
  },
]);
```

## After

```jsx
// routes.jsx — a catch-all route renders the designed 404 view
// inside the layout, with a path back into the product.
function NotFound() {
  return (
    <main>
      <h1>Page not found</h1>
      <p>The page you are looking for does not exist or has moved.</p>
      <Link to="/">Go to the home page</Link>
      <Link to="/pricing">See pricing</Link>
    </main>
  );
}

const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />,
    children: [
      { index: true, element: <Home /> },
      { path: "pricing", element: <Pricing /> },
      { path: "*", element: <NotFound /> },
    ],
  },
]);
```

Note: the blank-shell version fails DET-UX-010 on any typo'd or stale link; the catch-all turns a dead end into a designed view with a way back in.
