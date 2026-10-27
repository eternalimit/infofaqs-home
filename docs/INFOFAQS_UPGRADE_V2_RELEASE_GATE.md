# InfoFAQs Upgrade v2.0 | Review-only release gate

Status: PRIVATE 0 HOLD. This document is a review plan, not a deployment authorization.
Scope: Part I security foundation; Part II production readiness.
Repository: eternalimit/infofaqs-home
Review branch: review/infofaqs-alpha-login-orders-20261026

## Part I: Security foundation
- Require reviewed pull requests and passing checks before merging into main.
- Inspect deployment automation and GitHub Pages/custom-domain settings.
- Inventory environment-variable *names only*, never values. Separate preview, staging, and production secrets.
- Validate least-privilege database access and Supabase row-level security before enabling accounts or orders.
- Review credentials, cookie handling, session expiry, and OAuth redirect/state validation. Do not record tokens.
- Check static pages for accidental private content, credentials, or Edition 0 material.

## Part II: Production readiness
- Confirm the actual hosting provider and deployment target. Do not assume Render.
- Validate OAuth redirect allowlists and state flow end to end with a nonprivileged test account.
- Test search query encoding, XSS-safe DOM rendering, mobile navigation, keyboard focus, and broken links.
- Treat image orders, payments, and authentication as previews until backed by tested server-side controls.
- Require rollback plan, responsible approver, explicit authorization, and a signed-off release checklist.
- Capture immutable commit SHA, exact file SHA-256 hashes from downloaded bytes, test commands, exit codes, logs, and post-release verification before claiming PASS.

## Read-only inspection receipt
- On 2026-10-26, GitHub branch comparison reported this branch 5 commits ahead of main and 0 behind, touching index.html, login.html, order-form.html, search.html.
- The attempted lookup of .github/workflows/deploy.yml returned 404. This does not prove that no workflows exist.
- PR #4 explicitly identifies login, order intake, storage, and Stripe checkout as inactive.
- Functional browser, OAuth, and production security checks have NOT been demonstrated.
- The previously generated Upgrade v2.0 HTML/PDF are documentation artifacts; their contents have not been verified against this repository.

## Release decisions
- NO MERGE. NO PRODUCTION DEPLOYMENT. NO PRIVATE MATERIAL PUBLICATION.
- No SHA-256 asserted without hashing exact bytes.
- Gate status: UNVERIFIED, review only.

## Report K — production preparation authorization (2026-10-26)
- Owner authorized production preparation and review-branch commits, conditional on passing security and browser tests.
- This authorization does NOT waive the verification gate or authorize immediate deployment.
- Current observed review diff: 6 commits ahead, 0 behind main; five changed files.
- GitHub combined statuses: no statuses returned for release-checklist commit 76a6e25c99d833f60e5b8141f9de6815c1fbbbcc.
- PR-triggered workflow runs: none returned for that commit. This is not a passing test result.
- Static inspection: login and order-form inputs disabled; search dynamic content uses textContent.
- Known issue: search result href #oauth-state lacks a corresponding visible target in search.html; resolve and browser-test before release.
- Required security gates: secret and Edition 0 leak scan, OAuth redirect/state and session tests, Supabase RLS review, XSS/input checks, headers and dependency checks.
- Required browser gates: desktop/mobile navigation, keyboard and screen-reader basics, search encoding, no broken links, negative cases, cross-browser smoke.
- Require recorded test commands, exit codes, test artifacts, exact-byte SHA-256, reviewer approval, rollback and post-deploy verification plan.
- Deployment target https://www.infofaqs.com is NOT verified by this document; do not merge or deploy until separately approved after gates pass.
- RELEASE STATE: PREPARATION AUTHORIZED; PRODUCTION HOLD; EDITION 0 HOLD.
