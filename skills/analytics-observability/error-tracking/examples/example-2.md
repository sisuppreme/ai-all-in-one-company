# Example 2 — The release nobody could debug

## Before

A production release ships from CI with no source-map upload step and no release tag configured in the tracker SDK:

```yaml
# release pipeline
- run: npm run build
- run: npm run deploy
# (no source-map upload; SDK initialized with defaults)
```

Errors do arrive in the tracker, but every stack is minified offsets (`a.b.c at chunk-4f2.js:1:18342`), no event says which release produced it, and the team cannot tell whether the deploy caused the spike or merely coincided with it. Debugging is guesswork, and release health cannot be computed at all.

## After

The release pipeline uploads the maps for the exact build it deploys, and the SDK is initialized from the repo's versioned configuration:

```yaml
# release pipeline
- run: npm run build
- run: tracker-cli releases files "$RELEASE" upload-sourcemaps dist/ --url-prefix "~/dist"
- run: npm run deploy
```

```js
tracker.init({ release: process.env.RELEASE, environment: process.env.APP_ENV });
```

Stacks now read as source code, every event carries its release and environment, and the CI gate (G-AN-082) fails the deploy if the upload step did not run for that release.

Note: the Before violates AN-164 (source maps ship with the release) and AN-165 (release and environment tags are mandatory); the After corrects both.
