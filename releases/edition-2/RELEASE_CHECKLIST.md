# InfoFAQs Edition 2 — release candidate checklist

Status: REVIEW ONLY. Edition 1 remains public; Edition 0 remains private.

Copyright: © 2026 Richard Nathan Stein. All rights reserved.
Edition Check Sum designation: 2026.0.1.0.0.1.1

## Five independent release gates
1. Original source and private mirror byte-for-byte SHA-256 equality, with actual input bytes and receipts.
2. Current PR commit CI, security and desktop/mobile browser tests, with linked successful runs.
3. Authoritative DNS, Cloudflare SSL/TLS, apex/www HTTPS and canonical redirects, verified externally and against authenticated settings.
4. Hosting identity and exact production artifact SHA-256, confirmed against the intended release commit.
5. Privacy and regression review preserving private Edition 0, CATBOT 100, 10 FAQs, Human Green Button, and working Edition 1 navigation.

Do not claim PASS for untested checks. Do not merge, deploy, switch Edition 1 to Edition 2, change Cloudflare configuration, or activate protected controls until all gates PASS and separate release authorization is recorded.

## Evidence observed 2026-11-07
- https://infofaqs.com/ accessible via public web inspection; displays Edition 1.
- www host returned a checking-service 502; cause not determined.
- robots.txt and sitemap.xml inaccessible via checking service; cause not determined.
- PR #31 staged copyright metadata only; not a live release.

## Edition 2 acceptance
Public page must use truthful release language, retain all protected content, use the approved copyright attribution, preserve working links, and produce independently verifiable post-deploy receipts.
