# Example 3 — A static-page probe replaced by a real readiness check

## Before

The platform health check points at `/`. During a database outage the
homepage still returns 200 from the CDN cache, so the platform keeps the
broken instance in rotation and every dynamic page fails for users while the
dashboard shows the service as healthy.

## After

1. The app gains a readiness endpoint, `/health/ready`, which returns 200 only
   when the database and cache answer a real query, and 503 otherwise.
2. The platform health check is repointed from `/` to `/health/ready`.
3. In staging, the database is stopped: the readiness endpoint returns 503
   within seconds while the liveness endpoint still returns 200, and the
   platform drains the instance. The test result is recorded in progress.md.

Note: corrects DO-144 — health checks reflect the app's real ability to serve, not a page that cannot fail.
