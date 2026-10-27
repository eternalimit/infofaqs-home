# InfoFAQs SMS confirmation bot | review-only v0.1

Status: PRIVATE 0 HOLD. No SMS has been sent. No production deployment.

## Architecture
- Browser confirmation button calls a same-origin authenticated server endpoint `POST /api/sms/confirm`.
- Server verifies the signed-in user's identity, explicit opt-in, CSRF/origin, request schema, and rate limit.
- Server reads `SMS_PROVIDER_API_KEY` and `SMS_FROM_NUMBER` from its secret store. Never put credentials in HTML, GitHub, logs, or client JavaScript.
- Server uses an approved SMS provider API (provider not yet selected). T-Mobile cellular service alone does not expose an authorized sending API to this application.
- Destination is configured server-side for the opted-in account; do not accept arbitrary recipient numbers from public clients.
- Store provider message ID, timestamp, consent record, request ID, and delivery status without storing secrets or full message content.
- Webhook verifies provider signature before changing status to delivered/failed. An API accepted response is not a delivery receipt.
- Use idempotency keys and per-user throttling to prevent duplicate messages.

## UI contract (not yet enabled)
`Confirm by SMS` button stays disabled until authentication, consent, backend, and provider are configured and tested. Show status `NOT SENT`, `ACCEPTED`, `DELIVERED`, or `FAILED` only from verified server receipts.

## Required test gates
1. Unauthorized request rejected.
2. Missing consent rejected.
3. CSRF/origin rejection verified.
4. Invalid destination rejected.
5. Duplicate requests idempotent.
6. Rate limit enforced.
7. Provider timeout and failure handled.
8. Spoofed delivery webhook rejected.
9. No secrets exposed in client or logs.
10. Real sandbox or approved test message has recorded provider ID and delivery outcome.

## Deployment gate
Review branch only. No merge, deployment, real SMS, or private Edition 0 publication without verified security/browser tests and separate production authorization.
