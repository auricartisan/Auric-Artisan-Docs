---
title: Public API — Errors
description: The Auric Artisan API's error format, every error code with its HTTP status, what each means, and how to respond.
product: Services › Public API
updated: 2026-09-25
---

# Errors

Errors are JSON with a stable `code` and a human-readable `message`. Most include a `request_id`; quote it when you contact support about a specific call.

```json
{
  "error": {
    "code": "INVALID_INPUT",
    "message": "seed: not a number"
  },
  "request_id": "daebcbed-508b-4d4d-91ef-87ee99d32f03"
}
```

## Error codes

| Status | Code | Meaning and what to do |
|---|---|---|
| 400 | `INVALID_INPUT` | A parameter is missing or malformed; the message names the field |
| 400 | `INVALID_JSON` | The body is not valid JSON |
| 401 | `UNAUTHORIZED` or `UNAUTHENTICATED` | No key, or a missing, invalid or revoked key |
| 402 | `PLAN_UPGRADE_REQUIRED` | A valid key on a plan without API access; included from Specialist upward |
| 402 | `INSUFFICIENT_CREDITS` | Overage is on but the prepaid balance will not cover the call. Top up. |
| 402 | `SPEND_CAP_REACHED` | Your monthly overage spend cap was reached. Raise it in the dashboard. |
| 402 | `CREDIT_DEBIT_FAILED` | The balance could not be debited, so the request was not served and nothing was charged. Retry. |
| 403 | `FORBIDDEN` | A valid key without rights for this route |
| 404 | `NOT_FOUND` | Unknown endpoint or resource id. `GET /v1` lists every endpoint. |
| 405 | `METHOD_NOT_ALLOWED` | Right path, wrong method; the `Allow` header lists what is accepted |
| 413 | `PAYLOAD_TOO_LARGE` | The body is over the limit (4 MB for image endpoints) |
| 429 | `RATE_LIMITED` | Per-minute rate exceeded. Wait for `Retry-After`. |
| 429 | `IP_RATE_LIMITED` | Too many requests from one address, whatever the key |
| 429 | `QUOTA_EXCEEDED` | Included monthly credits used up and overage off. Enable it, or wait for the reset. |
| 429 | `HARD_CEILING_REACHED` | Ten times the included allowance was reached this month; contact support |
| 500 | `INTERNAL` | An unexpected server error. Quote the `request_id`. |
| 503 | `NOT_CONFIGURED` | An optional part of the service is not enabled |
| 503 | `ENFORCEMENT_UNAVAILABLE` | Limits could not be checked, so nothing was executed. Retry later. |

The API reference lists the 401 code as both `UNAUTHENTICATED` (in the endpoint tables) and `UNAUTHORIZED` (in the errors section); handle 401 by status rather than by code.

Some endpoints have their own codes, such as `UNKNOWN_SPACE` (404) for `/v1/science/spaces/:key`, `UNKNOWN_CONDITION` for `/v1/vision/conditions/:slug`, `VALIDATION_ERROR` for an unknown collection id, and the analyzer's codes on [Analyzer](endpoints/analyzer.md).

## 429 or 402: which is which

The split is by what you should do:

- **429** means back off and retry. The condition resets on its own, at the time in `retry-after` and `details.resets_at`. Official SDKs already retry on it.
- **402** means only a money decision unblocks it: a top-up, a raised spend cap or a plan upgrade. Retrying without one is pointless.

Every refusal names its remedy in `details.remedy`: `enable_overage`, `buy_credits`, `raise_spend_cap` or `contact_support`, alongside `credits_used`, `credits_included`, `credits_this_request` and `resets_at`.

```json
{
  "error": {
    "code": "INSUFFICIENT_CREDITS",
    "message": "Pay-as-you-go is on, but the prepaid credit balance is empty. Top up to continue — nothing is billed after the fact.",
    "details": {
      "tier": "pro",
      "credits_used": 1000010,
      "credits_included": 1000000,
      "credits_this_request": 10,
      "resets_at": "2026-09-01T00:00:00.000Z",
      "remedy": "buy_credits",
      "credits_needed": 10
    }
  },
  "request_id": "daebcbed-508b-4d4d-91ef-87ee99d32f03"
}
```

## Handling errors well

- Branch on `error.code`, not on `message`, which may change.
- On 429, wait for `retry-after` before retrying; do not retry in a tight loop.
- On 402, log `details.remedy` so someone can act on it.
- Watch `x-quota-remaining` to slow down before you run out.

## Related pages

- [Plans, credits and quotas](plans-credits-and-quotas.md)
- [Troubleshooting](troubleshooting.md)
