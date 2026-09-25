---
title: Tokens
description: What Auric Artisan tokens pay for, how much each plan includes, when included tokens expire, how to claim and check them, and how they differ from API credits.
product: Website › Account and billing
updated: 2026-09-25
---

# Tokens

Tokens meter the work that runs on Auric Artisan's servers when you start it from a website tool — for example rendered page analyses, snapshots and whole-site accessibility crawls in the Analyzer. Everything that runs in your browser is free and unmetered. Tokens belong to your account, so you need to be signed in to have or spend them.

## How many tokens each plan includes

| Plan | Included tokens | Renews? |
| --- | --- | --- |
| Apprentice (free) | 100, once | No — a one-time starter grant |
| Artisan | 250 a month | Yes, each billing month |
| Specialist (coming soon) | 1,000 a month | Yes, each billing month |
| Industrial Pro (coming soon) | 2,500 a month | Yes, each billing month |

One token is sized at a reference rate of about $0.10 of metered work. The pricing page describes the Artisan allowance as "250 pages a month however you spend them — a 24-page crawl costs 24".

## What a run costs

The Analyzer shows the token cost of a run beside the button that starts it — "This run", the cost, and your balance — before you spend anything. After a site scan it shows a receipt: what was authorised, what was scanned, what was charged, and anything returned (pages that failed are free, and tokens held for pages a site did not have are given back). The Analyzer's own guide explains the costs of each kind of run: [Analyzer](../../tools/accessibility-and-vision/analyzer/README.md).

If you do not have enough, the meter says how many more you need, for example "3 more than you have." For a site scan it offers the number of pages your balance can cover.

## Claim your tokens

1. Sign in.
2. Open the Analyzer at https://auricartisan.com/tool/analyzer/.
3. In its token meter, select **Claim 100 free tokens** (signed out, the button reads **Sign in · 100 free tokens** and takes you to sign in first).

Result: the meter shows your balance. The starter grant is given once per account; clearing your browser's data does not give you a second one, and the balance you had comes back when you sign in again.

On a paid plan, the dashboard's **Tool tokens** card tells you when "This period's allowance is waiting to be claimed."

## Check your balance

Your balance is in two places:

- **Dashboard** › **Overview** › **Tool tokens** — the balance, "of 250 a month" (or "tokens" for the one-time grant), a bar for this period's included tokens, and a note such as "250 of these lapse at the end of the period." See [Overview section](dashboard-overview.md#tool-tokens).
- **The Analyzer's token meter** — your balance next to the cost of the run you are about to start.

## Expiry

- **Included monthly tokens** expire at the end of the billing period in which they were granted. They do not roll over. When a new period starts, a new allowance is granted.
- **The Apprentice starter grant** does not expire, and it does not refresh when it is spent.
- **Purchased tokens** do not expire at the period boundary, according to the Subscription and Billing Policy. Token packs are not on sale today, so today every token comes with a plan.
- When you spend tokens, the included (expiring) ones are used first.

## When you run out

Server-backed runs stop; everything that runs in your browser keeps working. The Analyzer says "You're out of tokens." Your options are to wait for your next monthly allowance, or to move to a plan with a larger allowance. Top-ups are not on sale; if you expect to pass your allowance, the pricing page asks you to tell Auric Artisan what you need through the contact page.

## Tokens are not API credits

| | Tokens | API credits |
| --- | --- | --- |
| Pays for | Server-backed work you start in a tool on the website | Requests your own code makes to the REST API |
| One unit | One unit of metered tool work, about $0.10 | One standard API request; heavier endpoints cost 2–25 |
| Included | 100 once on Apprentice; 250, 1,000 or 2,500 a month | None on Apprentice or Artisan; 1,000,000 or 10,000,000 a month |
| When it runs out | Server-backed runs stop | Calls are refused, unless you turned on prepaid overage |

Neither pays for the other. Running out of tokens never stops your API calls, and running out of API credits never stops a crawl.

## Refunds and tokens

Refunding a plan payment also removes the tokens that purchase granted. See [Refunds](refunds.md).

## Related

- [Plans and pricing](plans-and-pricing.md)
- [API credits and spend controls](api-credits-and-spend.md)
- [Subscription and Billing Policy summary](../../company-and-legal/docs/subscription-and-billing-policy.md)
