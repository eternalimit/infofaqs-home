# QA1 release gate — InfoFAQs marketplace preview

**Scope:** Only `qa1`. This is a static public-safe prototype, not a working marketplace. **0 HOLD**.

## Verified implementation
- `marketplace-preview.html`: responsive navigation, three public placeholder categories, in-memory demo cart, disabled membership action, owner-access notice.
- `tests/test_marketplace_preview.py`: offline structural and negative checks. Run with `python3 -m unittest discover -s tests -v`.

## Explicitly not complete
- No server-side authentication, role-based owner authorization, session security, membership database, account confirmation, payment provider, real orders, cart persistence, refund workflow, merchant onboarding, tax calculation, or email delivery.
- No reviewed WATT 100 content and no complete page inventory.
- No browser-based accessibility/mobile tests, penetration test, privacy review, deployment/rollback rehearsal, or independent production validation.

## Required gates before production
1. Audit all repository files and dependencies for protected content and credentials; rotate any exposed credentials.
2. Establish private backend and secret storage; implement default-deny authorization with negative tests.
3. Implement payment flow through a provider and verify webhooks using test credentials only.
4. Implement consent, privacy, customer support, accessibility, email verification, backups, monitoring, and rollback.
5. Run automated unit, integration, browser, security, and adversarial tests with exact commands, outputs, and hashes.
6. Reconcile branch divergence; obtain explicit owner approval for any merge and separate approval for deployment.

**Never rely on robots directives, client-side controls, or HTML meta tags as access control.** Do not modify `main` or `robots.txt`; do not deploy.
