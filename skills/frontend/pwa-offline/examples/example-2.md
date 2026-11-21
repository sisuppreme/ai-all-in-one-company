# Example 2 — Browser error offline replaced by a designed offline page

Corrects rule **FE-285** (the offline experience is designed).

## Before

```js
// sw.js — the shell is precached, but a failed navigation is
// never intercepted, so offline opens show the browser's
// default "no internet" error page. This is BAN-FE-141.
self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open("shell-v1").then((cache) =>
      cache.addAll(["/", "/styles.css", "/app.js"])
    )
  );
});

self.addEventListener("fetch", (event) => {
  event.respondWith(caches.match(event.request).then((hit) => hit || fetch(event.request)));
});
```

## After

```js
// sw.js — the offline page is part of the precached shell, and
// failed navigations are answered with it.
const SHELL = ["./", "/styles.css", "/app.js", "/offline.html"];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open("shell-v2").then((cache) => cache.addAll(SHELL))
  );
});

self.addEventListener("fetch", (event) => {
  if (event.request.mode === "navigate") {
    event.respondWith(
      fetch(event.request).catch(() => caches.match("/offline.html"))
    );
    return;
  }
  event.respondWith(
    caches.match(event.request).then((hit) => hit || fetch(event.request))
  );
});
```

```html
<!-- offline.html — a real page in the product's design system,
     stating the honest offline scope (FE-287). -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>You are offline — TaskBoard</title>
  <link rel="stylesheet" href="/styles.css">
</head>
<body>
  <main>
    <h1>You are offline</h1>
    <p>Pages you have already visited are still available.
       New changes will sync when you reconnect.</p>
    <button onclick="location.reload()">Try again</button>
  </main>
</body>
</html>
```

Note: the before version technically "has a service worker" but the user's offline experience is the browser's error. The after version makes offline a designed state of the product, which gate G-FE-142 verifies.
