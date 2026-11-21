# Example 1 — Hand-carried deploy replaced by artifact promotion

Demonstrates: DO-042 (no manual deploy steps) and DO-043 (build once, promote unchanged).

## Before

Release note in the project chat: "Deployed v1.4 — uploaded the new `dist/` folder over SFTP to the server, ran `npm install` on the box just in case, restarted the service. Looks fine." The live version maps to no commit and no artifact; when a hotfix is needed, nobody can rebuild what is running or return to what ran before.

## After

CI builds one container image per merge, tagged with the commit SHA and recorded by digest. Staging deploys digest `sha256:9f2c…`; after staging passes, the production environment job promotes the same digest behind its protection rules. The deploy record reads: digest, SHA, strategy (rolling), trigger, timestamp — and the previous digest stays available for immediate redeploy.
