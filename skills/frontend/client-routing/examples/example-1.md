# Example 1 — State-flag navigation replaced by real routes

Corrects rule **FE-222** (no state-flag navigation).

## Before

```jsx
// App.jsx — views are state, not URLs. Refresh resets to home,
// the settings view cannot be linked, and Back leaves the app.
import { useState } from "react";

export default function App() {
  const [page, setPage] = useState("home");
  return (
    <div>
      <nav>
        <button onClick={() => setPage("home")}>Home</button>
        <button onClick={() => setPage("settings")}>Settings</button>
      </nav>
      {page === "home" && <Home />}
      {page === "settings" && <Settings />}
    </div>
  );
}
```

## After

```jsx
// routes.jsx — every view is a route with a real URL.
// Refresh, deep links, and Back/Forward all land on the correct view.
import { createBrowserRouter, RouterProvider, Link, Outlet } from "react-router-dom";

function Layout() {
  return (
    <div>
      <nav>
        <Link to="/">Home</Link>
        <Link to="/settings">Settings</Link>
      </nav>
      <Outlet />
    </div>
  );
}

const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />,
    children: [
      { index: true, element: <Home /> },
      { path: "settings", element: <Settings /> },
    ],
  },
]);

export default function App() {
  return <RouterProvider router={router} />;
}
```

Note: the state-flag version made `/settings` un-linkable and un-refreshable; the router version gives every view a URL, so FE-222's refresh/deep-link/back test can pass.
