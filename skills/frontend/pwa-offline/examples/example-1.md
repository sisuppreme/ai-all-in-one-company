# Example 1 — Cache-everything handler replaced by per-resource strategies

Corrects rule **FE-283** (every resource class has a named strategy).

## Before

```js
// sw.js — one handler for everything: cache-first forever.
// API responses go stale, navigations break offline, and
// nothing ever expires. This is BAN-FE-142.
self.addEventListener("fetch", (event) => {
  event.respondWith(
    caches.match(event.request).then((hit) => hit || fetch(event.request))
  );
});
```

## After

```js
// sw.js — strategy per resource class:
// app shell + static assets: cache-first (precached, versioned)
// data (API GET): network-first, falling back to cache
// navigations: network-first, falling back to the offline page
const VERSION = "v3";
const SHELL_CACHE = `shell-${VERSION}`;
const DATA_CACHE = `data-${VERSION}`;

self.addEventListener("fetch", (event) => {
  const { request } = event;
  const url = new URL(request.url);

  if (request.mode === "navigate") {
    event.respondWith(
      fetch(request).catch(() => caches.match("/offline.html"))
    );
    return;
  }

  if (url.pathname.startsWith("/api/")) {
    event.respondWith(
      fetch(request)
        .then((response) => {
          const copy = response.clone();
          caches.open(DATA_CACHE).then((cache) => cache.put(request, copy));
          return response;
        })
        .catch(() => caches.match(request))
    );
    return;
  }

  // Static assets and everything else: cache-first.
  event.respondWith(
    caches.match(request).then((hit) => hit || fetch(request))
  );
});
```

Note: the before handler cannot tell a price from a PNG — everything is stale at the same rate. The after version gives each class the strategy the written strategy table names.
