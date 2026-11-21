# Example 3 — Unversioned cache replaced by versioned caches with cleanup

Corrects rule **FE-284** (cache names are versioned; old caches are cleaned).

## Before

```js
// sw.js — one cache named "cache", created once and never
// cleaned. Every deploy adds files; old versions live forever,
// and users keep running whatever they cached first.
self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open("cache").then((cache) =>
      cache.addAll(["/", "/styles.css", "/app.js"])
    )
  );
});

self.addEventListener("fetch", (event) => {
  event.respondWith(
    caches.match(event.request).then((hit) => hit || fetch(event.request))
  );
});
```

## After

```js
// sw.js — the version is in every cache name, and activate
// deletes anything that is not the current version, so a
// deploy actually reaches returning users.
const VERSION = "v4";
const SHELL_CACHE = `shell-${VERSION}`;
const DATA_CACHE = `data-${VERSION}`;
const KEEP = [SHELL_CACHE, DATA_CACHE];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(SHELL_CACHE)
      .then((cache) => cache.addAll(["/", "/styles.css", "/app.js", "/offline.html"]))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys()
      .then((names) => Promise.all(
        names.filter((name) => !KEEP.includes(name)).map((name) => caches.delete(name))
      ))
      .then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", (event) => {
  event.respondWith(
    caches.match(event.request).then((hit) => hit || fetch(event.request))
  );
});
```

Note: with the before version, "we shipped a fix" is false for every returning user. Versioned names plus activate cleanup make the update drill (G-FE-143) pass: bump VERSION, deploy, and old caches are gone.
