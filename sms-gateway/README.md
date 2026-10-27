# SMS Gateway prototype (review branch only)

Node.js 20+ server in `sms-gateway/server.mjs`. Sends through Twilio REST API to a fixed, server-configured destination. No public website integration or production deployment has occurred.

## Configuration (secret manager, not GitHub)
- `SMS_OPERATOR_TOKEN`: long random private operator bearer token
- `SMS_TO_NUMBER`: destination in E.164 format (e.g. +1 followed by ten digits)
- `TWILIO_ACCOUNT_SID`: provider account SID
- `TWILIO_AUTH_TOKEN`: provider secret
- `TWILIO_FROM_NUMBER`: provider-authorized sending number
- `PORT`: optional, defaults to 8787

Run locally with `node sms-gateway/server.mjs`. The server binds to localhost. Example request from a trusted operator environment only:

```bash
curl -X POST http://127.0.0.1:8787/api/sms/confirm \
  -H "Authorization: Bearer $SMS_OPERATOR_TOKEN" \
  -H 'Content-Type: application/json' \
  --data '{"confirm":true,"consent":true}'
```

HTTP 202 means the SMS provider accepted the request, **not** that the phone received the SMS. This prototype has no delivery webhook. It intentionally has no public website button yet: putting the operator bearer token in browser code would expose a credential.

## Security release blockers
- Real account and sender provisioned; destination consent verified; opt-out/STOP and applicable messaging compliance handled.
- Authenticated operator UI backed by a server session, CSRF protection, durable rate limiting and idempotency.
- Persisted, redacted audit receipts and signature-verified provider delivery webhooks.
- Negative tests, browser tests, deployment-specific secrets, TLS, monitoring, and rollback.
- A separate explicit production approval. PRIVATE Edition 0 stays 0 HOLD.

**Status: UNVERIFIED. No live SMS sent. No production deployment.**
