# Example 2 — Pipeline-built preview

## Before

The platform's automatic previews were disabled because they were "slow." Instead, a developer runs a script from a laptop whenever a reviewer asks for a look:

```bash
# deploy-preview.sh — run locally, uploads the working tree
npm run build && rsync -r dist/ server:/srv/preview/
```

The preview shows uncommitted local changes, exists in no commit, and cannot be rebuilt by anyone else.

## After

Previews are a job in the same pipeline that builds staging and production. On every PR the pipeline builds the PR head commit once, deploys that artifact to the preview target, stamps it with build metadata, and comments the URL on the PR:

```yaml
preview:
  needs: build
  if: github.event_name == 'pull_request'
  steps:
    - uses: actions/download-artifact@v4
      with: { name: app-dist }
    - run: ./scripts/deploy-preview.sh dist/ "$PR_NUMBER" "$GITHUB_SHA"
    # deploy-preview.sh publishes dist/ plus build-info.json { "commit": $GITHUB_SHA }
```

What reviewers see is exactly the artifact the pipeline produced for that commit.

Note: corrects DO-024 — the preview is built by the same artifact path as production.
