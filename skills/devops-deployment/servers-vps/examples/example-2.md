# Example 2 — A default server configuration hardened before launch

## Before

A fresh VPS is provisioned, the application is copied up, and the domain is
pointed at it the same evening. Still live from the stock install:

- The default vhost serves the web server's welcome page on the bare IP.
- Response headers announce the exact server and version.
- A directory under the web root returns a full file listing.
- Two unused services from the base image are running and listening.

The application works. So does everything the installer shipped.

## After

The hardening baseline runs as part of provisioning, before the first deploy:

1. Default vhost and welcome page removed; the bare IP returns 444/404.
2. Version tokens suppressed in the server configuration; headers carry no
   server version.
3. Directory listing disabled globally; the same URL now returns 403.
4. Unused services stopped, disabled, and absent from the port scan.

Verification: `curl -sI https://<domain>/` shows no version banner,
`curl -s https://<domain>/assets/` returns 403, and the external port scan
matches the architecture document's port list exactly (G-DO-061, G-DO-062).

Note: corrects DO-122 — the hardening baseline is applied before the first deploy, not after the defaults are discovered in production.
