---
title: Public API — Authentication
description: How to authenticate with the Auric Artisan API — API keys, the CLI's OAuth bearer token, keeping keys safe, and revoking them.
product: Services › Public API
updated: 2026-09-25
---

# Authentication

Every metered endpoint requires a credential. Requests without a valid one receive `401 Unauthorized`. Endpoints marked "None" in the [Reference](reference.md) are public and unmetered.

## Methods

| Method | How to send it | Best for |
|---|---|---|
| API key (recommended) | The `x-api-key: aa_…` header, or the `?key=aa_…` query parameter | Servers, scripts and CI; create keys in the dashboard |
| OAuth bearer | `Authorization: Bearer <token>`, from the CLI's device flow | The `auric` command-line tool and interactive tools |

Prefer the header. A key in a query string can end up in server logs and browser history.

```bash
curl https://api.auricartisan.com/v1/usage/me -H "x-api-key: aa_YOUR_KEY"
```

## Keys are secret

- The full key is displayed **once**, when you create it. It is stored only as a SHA-256 hash, so nobody, including Auric Artisan, can recover it later. If you lose it, create a new one.
- Keep keys out of source code and front-end code. Load them from environment variables or a secret store, as the examples do with `$AURIC_API_KEY`.
- Each successful request updates the key's "last used" time, which you can check in the dashboard to spot a key in use where it should not be.

## Several keys

You can hold up to **10** active keys, for example one per service or environment. Rate limits, monthly credits and the credit balance are pooled **per account**, not per key: ten keys share one allowance, so splitting traffic across keys does not raise your limits.

## Revoke a key

If a key leaks, revoke it in the dashboard with **Revoke**. Revocation takes effect within a minute. Requests with a revoked key then receive `401`.

## Plan and access

A valid key on a plan without API access authenticates, but metered endpoints refuse it with `402 PLAN_UPGRADE_REQUIRED`. See [Plans, credits and quotas](plans-credits-and-quotas.md).

## Related pages

- [Getting started](getting-started.md)
- [Errors](errors.md)
- The account documentation, in the website section of these docs, covers the dashboard itself: [Account and billing](../../../website/account-and-billing/README.md)
