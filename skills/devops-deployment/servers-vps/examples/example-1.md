# Example 1 — An in-place hotfix replaced by an artifact deploy

## Before

A pricing page shows the wrong plan name in production. The operator SSHs
into the VPS, opens the deployed template in a text editor, and fixes the
name in place. The site is correct within minutes.

The fix exists only on that server. It is not in the repo, not in any build,
and the next deploy — built from the repo — silently restores the wrong name.
Nobody can say which other "quick fixes" the live files carry that the repo
does not.

## After

The same fix, done as a deploy:

1. The plan name is corrected in the repo and committed.
2. CI builds a new release artifact: `releases/2026-11-21-3/`.
3. The deploy script installs the artifact into its own release directory
   and flips the `current` symlink to it; the proxy reloads.
4. The previous release directory stays on disk. If the new release misbehaves,
   rollback is one symlink flip back — no rebuild, no editor, no guesswork.

The live server and the repo now agree, and the fix survives every future
deploy.

Note: corrects DO-126 — deploys land as artifacts in versioned release directories, never as in-place edits on the live server.
