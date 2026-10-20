---
title: Public API — Plans, credits and quotas
description: What each plan includes, how credits are charged per endpoint, rate limits, overage, spend caps, the hard ceiling, and the headers that report usage.
product: Services › Public API
updated: 2026-09-25
---

# Plans, credits and quotas

Limits follow your account plan. The rate limit, monthly credits and credit balance are pooled per account, not per key.

## What each plan includes

| Plan | API tier | Requests per minute | Credits per month | Hard ceiling | Max keys |
|---|---|---|---|---|---|
| Apprentice (free) | Free | — | Not included | — | — |
| Artisan | Paid | — | Not included | — | — |
| Specialist | Pro | 300 | 1,000,000 | 10,000,000 | 10 |
| Industrial Pro | Enterprise | 3,000 | 10,000,000 | 100,000,000 | 10 |

`GET /v1/tiers` returns the machine-readable version of this table, so a client can read its own terms instead of hard-coding them.

> **Note:** Industrial Pro was sold as "Unlimited" before 12 August 2026. Subscriptions created before that date keep that promise: they are metered at 1,000,000,000 credits a month, a hundred times the new figure, and their hard ceiling scales with that allowance. The 10,000,000 figure applies to subscriptions started on or after 12 August 2026.

## Credits

The monthly quota is counted in **credits**, not calls. One credit is one standard request; endpoints that do more work cost more, so simple colour maths does not subsidise image rendering. Every response states its cost in the `x-credits-cost` header.

- **1 credit**: Standard work: `/v1/color/convert`, `/v1/color/contrast`, `/v1/science/convert`, `/v1/accessibility/check`, `/v1/vision/simulate`, and anything not listed below
- **2–4 credits**: Generators and multi-step maths: `/v1/palette/generate`, `/v1/harmony/generate`, `/v1/gradient/generate`, `/v1/shade/scale`, `/v1/science/delta-e`, `/v1/science/temperature`, `/v1/tokens/generate`, `/v1/graphql`
- **5 credits**: `/v1/science/dossier`, and `/v1/usage/stream` (charged once when the stream opens; events are free)
- **10–12 credits**: Rendered pixels: `/v1/palette/png`, `/v1/gradient/png`, `/v1/ishihara/png`, `/v1/vision/simulate-image`, `/v1/palette/from-image`, `/v1/accessibility/from-image`
- **25 credits**: Async jobs: `POST /v1/jobs/{type}`. Polling a job with `GET /v1/jobs/id/{id}` costs 1.

The analyzer endpoints cost: `GET /v1/analyzer/stages` 1 credit, `POST /v1/analyzer/inspect` 12 credits and `POST /v1/analyzer/render` 10 credits. See [Analyzer](endpoints/analyzer.md).

A new endpoint that has not been given its own weight bills as standard work, 1 credit; nothing is free by accident. Public discovery endpoints are unmetered.

## When you run out

By default, running out of included credits stops the traffic. Further calls return `429 QUOTA_EXCEEDED` until the monthly reset. Nothing is charged.

### Pay-as-you-go overage (opt-in)

- Overage is **off** until you turn it on in the dashboard's API keys area.
- It is **prepaid**: it spends a credit balance bought in advance, at **$1.00 (₹85) per 100,000 credits**.
- If the balance will not cover a call, the call is refused with `402 INSUFFICIENT_CREDITS`. It is never served on account, and no usage produces an invoice after the fact.
- Buy credit packs in the dashboard with **Add credits**. Purchased credits do not expire at the end of the period.

In the dashboard, the overage switch reads "Off — calls stop at your included allowance. Nothing is charged." while it is off, and asks you to confirm with **Turn on paid overage** or **Keep it off**.

### Spend cap

Set a **Monthly spend cap** in money, up to $10,000. Overage stops there with `402 SPEND_CAP_REACHED`; raise the cap in the dashboard to continue.

### Hard ceiling

Independent of anything you configure, no account may spend more than **ten times its included allowance** in one month. Reaching it returns `429 HARD_CEILING_REACHED`. It is a safety stop against runaway retries and leaked keys; support can raise it.

## Reading the meter

Every response carries these headers:

| Header | Meaning |
|---|---|
| `x-ratelimit-limit` | Requests allowed per minute |
| `x-ratelimit-remaining` | Requests left this minute |
| `x-ratelimit-reset` | When the minute resets, in Unix seconds |
| `x-quota-limit` | Included credits this month |
| `x-quota-used` | Credits used this month |
| `x-quota-remaining` | Included credits left |
| `x-quota-reset` | When the monthly quota resets, in Unix seconds |
| `x-credits-cost` | What this call consumed |
| `x-credits-overage` | Only when the call was paid from the prepaid balance: the overage credits used |
| `x-overage-cost-usd` | Only with overage: 1.00 when this call opened a new 100,000-credit block, otherwise 0.00 |
| `x-credits-ceiling` | The hard ceiling |

Check usage at any time with `GET /v1/usage/me`, or full per-day, per-endpoint history with `GET /v1/usage`. A `quota.threshold` webhook fires when you cross 80% of the included allowance.

## The dashboard

The dashboard's API area shows **Usage & cost** (credits used, included credits left, overage credits and overage cost, and **Credits per day**), your **prepaid credits** balance, **Spend controls**, **Recent credit activity**, **Where the credits went**, and a live feed of recent calls once you connect a key.

## Beyond the largest plan

For volume beyond the largest credit pack, a custom rate limit or a contract, contact Auric Artisan. Billing terms for prepaid credits, including expiry, cancellation, downgrade and refunds, are in the Subscription & Billing Policy at https://auricartisan.com/legal/subscription-billing/.

## Related pages

- [Errors](errors.md), for the 429 and 402 codes
- [Usage, jobs, webhooks and GraphQL](endpoints/usage-jobs-webhooks-graphql.md)
