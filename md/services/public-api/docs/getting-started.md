---
title: Public API — Getting started
description: Get an API key from your dashboard, make a first request, and read the response and its usage headers.
product: Services › Public API
updated: 2026-09-25
---

# Getting started

This page takes you from no key to a working request.

## 1. Check your plan

The API is a paid feature, included from the **Specialist** plan upward:

| Plan | API access |
|---|---|
| Apprentice (free) | Not included |
| Artisan | Not included |
| Specialist | Included |
| Industrial Pro | Included |

A key created on a plan without API access authenticates, but metered endpoints refuse it with `402 PLAN_UPGRADE_REQUIRED`, and the response names the upgrade path. In the dashboard, key creation says "Available from the Specialist plan" until you upgrade.

You can still explore without a key. These discovery endpoints are open to everyone: `GET /v1`, `GET /v1/catalog`, `GET /v1/openapi.yaml`, `GET /v1/docs`, `GET /v1/tiers` and `GET /v1/health`.

## 2. Create a key

1. Sign in and open your dashboard at https://auricartisan.com/auth/dashboard/. The API documentation calls this **Dashboard › API Keys**.
2. Under **Your API Keys**, choose **Create your first key** (or **Create key** if you already have one).
3. Type a name in **Key name (e.g. "CI pipeline")** and choose **Create**.
4. Copy the key and store it somewhere safe, such as a password manager or your deployment's secret store. "This is the only time the full key is shown."

Keys start with `aa_`. You can hold up to 10 active keys, and **Revoke** any of them instantly.

## 3. Make a first request

Send the key in the `x-api-key` header:

```bash
# Convert a color to OKLCH
curl -X POST https://api.auricartisan.com/v1/color/convert \
  -H "x-api-key: aa_YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"color": "#d3af37", "to": "oklch"}'
```

The response is JSON:

```json
{"input":{"rgb":[211,175,55],"hex":"#d3af37"},"to":"oklch",
 "value":[0.7655,0.1384,91.55]}
```

Tool endpoints accept JSON through `POST` and reply in JSON. Collection and discovery endpoints use `GET` with query parameters.

## 4. Read the headers

Every response carries your live consumption, so a client can throttle itself:

```text
x-ratelimit-limit: 300            # requests allowed per minute
x-ratelimit-remaining: 297
x-ratelimit-reset: 1783502302     # unix seconds
x-quota-limit: 1000000            # included credits this month
x-quota-used: 412
x-quota-remaining: 999588
x-quota-reset: 1785091200         # unix seconds
x-credits-cost: 10                # what this call consumed
```

See [Plans, credits and quotas](plans-credits-and-quotas.md) for what each one means.

## 5. Check your usage

```bash
curl https://api.auricartisan.com/v1/usage/me -H "x-api-key: aa_YOUR_KEY"
```

```json
{"tier":"pro","plan":"specialist","auth_type":"api_key",
 "limits":{"rate_per_minute":300,"monthly_quota":1000000},
 "this_month":{"slot":"2026-08","used":412}}
```

`used` counts credits, not calls.

## 6. Explore

- `GET /v1` lists every endpoint with the current version.
- `GET /v1/catalog` returns every endpoint with its parameters and examples, as JSON.
- `GET /v1/docs` is the interactive reference; `GET /v1/openapi.yaml` is the OpenAPI 3.1 document.
- `GET /v1/methods/:tool` lists the algorithms a tool supports, for example `/v1/methods/harmony`.
- `GET /v1/formats` lists every export format.

## Next steps

- [Endpoints](endpoints/README.md) by group
- [Request examples](examples.md)
- [Errors](errors.md)
