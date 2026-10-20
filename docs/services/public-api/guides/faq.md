---
title: Public API — FAQ
description: Short answers to common questions about the Auric Artisan REST API.
product: Services › Public API
updated: 2026-09-25
---

# FAQ

### Which plans include the API?

Specialist and Industrial Pro. Apprentice (free) and Artisan do not include it.

### Can I try it before buying?

Yes, partly. The discovery endpoints are open without a key: `GET /v1`, `GET /v1/catalog`, `GET /v1/openapi.yaml`, `GET /v1/docs`, `GET /v1/tiers`, `GET /v1/health` and `GET /v1/webhooks/events`.

### How many keys can I have?

Up to 10 active keys. They share one allowance, because limits are pooled per account.

### What is a credit?

The unit the monthly quota is counted in. A standard request costs 1 credit; heavier work costs more, up to 25 for an async job. Each response says what it cost in `x-credits-cost`.

### What happens when I run out?

Calls return `429 QUOTA_EXCEEDED` until the monthly reset, and nothing is charged, unless you turned on prepaid overage.

### Can I be billed unexpectedly?

No. Overage is off by default, spends only credits bought in advance, stops at a spend cap you set, and stops unconditionally at ten times your included allowance. Nothing is invoiced after the fact.

### Do purchased credits expire?

Purchased credits do not expire at period end. Full terms are in the Subscription & Billing Policy.

### Is the API the same as the website tools?

It uses the same engines where it can, but some things differ. The analyzer endpoints read a page's source and refuse checks that need a browser, such as contrast; the website's Analyzer runs pages in your browser. API credits and the website's tool tokens are separate balances.

### Why does the analyzer return no overall score?

Because a markup-only run cannot measure every category, and averaging a subset would give a misleading number. You get the measured categories in `category_scores` and a list of `unscored_categories`.

### Which standards does the accessibility check support?

`/v1/accessibility/check` accepts `WCAG 2.1`, `WCAG 2.2`, `WCAG 3.0`, `Auric SD Flexible`, `Auric SD Strict`, or `all`, the default.

### Is there a client library?

The documentation lists a JavaScript package (`@auric-artisan/api`), a Python package (`auric-artisan`), a CLI (`@auric-artisan/cli`), an MCP server, a Postman collection and GraphQL. See [SDKs and tooling](sdks-and-tooling.md).

### Can I call the API from a web page?

Only with care: a key in front-end code is visible to anyone. Call the API from your server and keep the key secret.

### How do I cite a colour pair or palette?

Use its record id, such as `acc_2j` or `pal_1z`. Records are derived from a published seed, so anyone can recover the same record with the matching `/:id` endpoint.
