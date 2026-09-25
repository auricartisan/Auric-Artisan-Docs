---
title: API credits and spend controls
description: How Auric Artisan API credits are counted, what is included, buying prepaid credits, paid overage, the monthly spend cap, the hard ceiling, and the usage panels in the dashboard.
product: Website › Account and billing
updated: 2026-09-25
---

# API credits and spend controls

The REST API is metered in API credits. This page explains the rules and the dashboard panels that show and control them: **Usage & cost**, **Credits & spend**, **Where the credits went** and **Live usage**, all under **Plan & Usage** on plans with API access. The API itself is documented in [Public API](../../../services/public-api/README.md).

API credits are not tokens. Tokens pay for server work you start in a website tool; API credits pay for calls your own code makes. Neither pays for the other.

## How credits are counted

- One credit is one standard request. Heavier endpoints cost more, "so a caller doing simple color maths is not subsidising one rendering images", as the pricing page puts it.
- Credits are counted per account, not per key. Every key you create draws on the same allowance and the same prepaid balance.

| Request type (pricing page) | Credits | Examples |
| --- | --- | --- |
| Standard | 1 | Colour conversion, contrast check, vision simulation |
| Generators | 2–4 | Palette, harmony, gradient, shade scale, design tokens |
| Colour dossier | 5 | All 63 colour spaces plus a locus search, in one call |
| Rendered PNG | 10–12 | Palette, gradient and Ishihara images; image analysis |
| Async job | 25 | Batch work queued and run on Auric Artisan's clock |

The API documentation lists the cost of every endpoint: https://auricartisan.com/library/documentation/api/#api-limits.

## What is included

| Plan | Included credits a month | Rate limit |
| --- | --- | --- |
| Apprentice | None — API not included | — |
| Artisan | None — API not included | — |
| Specialist | 1,000,000 | 300 requests a minute |
| Industrial Pro | 10,000,000 | 3,000 requests a minute |

- The allowance refreshes at the start of each billing month and does not roll over.
- Neither allowance is unlimited. The pricing page notes that, sustained around the clock, they work out at roughly 22 and 224 credits a minute, so a busy plan meets the monthly allowance before the per-minute rate limit.
- On Apprentice and Artisan, a key authenticates but is refused on metered endpoints.
- **Industrial Pro before 12 August 2026:** Industrial Pro used to be sold with unlimited API requests. Subscriptions started before that date keep that allowance, which the Subscription and Billing Policy says is metered at 1,000,000,000 credits a billing month.

## When the allowance runs out

By default, calls stop: the API answers with a 429 response saying the allowance is used up and when it resets. Nothing is billed.

If you want calls to continue past the allowance, you can turn on paid overage. It is:

- **off by default** — nothing is charged until you turn it on;
- **prepaid** — it spends credits you have already bought, at $1.00 (₹85) per 100,000 credits;
- **never invoiced afterwards** — if your balance cannot cover a call, the call is refused rather than served on account.

Two safety nets apply:

- **Your monthly spend cap**, if you set one: overage stops when it is reached.
- **The hard ceiling**: independently of any setting, each account is limited in one month to ten times its included allowance, as a backstop against runaway loops or a leaked key. Support can raise it.

## Credits & spend panel

### Your balance

The large figure is your prepaid credit balance ("prepaid credits"). The line under it says what it is worth, for example "Worth $5.50 of overage at $1.00 (₹85) per 100,000 credits. Credits never expire." With no balance it says "No prepaid credits. Overage cannot run without them, so calls stop at the included allowance — nothing is ever invoiced after the fact."

### Buy prepaid credits

1. In **Credits & spend**, select **Add credits**. The pack picker opens.
2. Choose a pack. Prices are shown in your currency (the same choice as the pricing page):

   | Pack | Price (USD) | Price (INR) | Bonus |
   | --- | --- | --- | --- |
   | 100,000 credits | $1 | ₹85 | — |
   | 550,000 credits | $5 | ₹425 | 10% more credits |
   | 2,400,000 credits | $20 | ₹1,700 | 20% more credits |
   | 13,000,000 credits | $100 | ₹8,500 | 30% more credits |

3. The Razorpay checkout opens ("Opening checkout…"). Pay as you would for a plan.
4. The panel reports "Payment confirmed — 13,000,000 credits are being added." and then "13,000,000 credits added." (the figure matches your pack). If the balance takes a moment, it says "Payment confirmed. The balance will update shortly — reload if it has not."

If you close the checkout: "Checkout was not completed. Nothing has been charged."

Purchased credits do not expire at the end of a period and are not removed if your plan ends; they become spendable again if the account returns to a plan with API access. The price is set by Auric Artisan when the order is created, never by the page.

> **Note:** Credits belong to plans with API access. On a plan without it, the picker says: "Prepaid API credits are part of the Specialist plan, which is not on sale yet. Nothing to buy here until it is — your existing balance, if you have one, is unaffected." Check your plan can spend credits before you buy them.

### Turn on paid overage

1. Under **Spend controls**, select the **Paid overage** switch.
2. A confirmation appears: **This will let calls spend money.** It restates the rate and your current balance.
3. Select **Turn on paid overage** to confirm, or **Keep it off**.

Result: the switch reads "On — past the included allowance, calls spend prepaid credits at $1.00 per 100,000." and a warning line reminds you paid usage is on.

To turn it off, select the switch again. Turning it off takes effect at once and needs no confirmation: "Off — calls stop at your included allowance. Nothing is charged." On a plan without API access, the switch is disabled: "Not available on this plan — calls stop at the included allowance."

### Set a monthly spend cap

1. Under **Monthly spend cap**, type an amount in US dollars, from 0 to 10,000.
2. Select **Save**.

Result: "Saved." The note under the field says how many credits of overage the cap allows this month, for example "Overage stops after 500,000 credits this month.", and names the plan's hard ceiling. A cap of **0** means "no cap of your own — the plan's hard ceiling still applies". The cap limits overage only; it never restricts your included allowance.

If the amount is out of range: "Enter a cap between $0 and $10,000."

### Recent credit activity

Once there is activity, a list shows the last eight movements, each with a label, date and signed amount: **Plan grant**, **Credits added**, **API usage**, **Refund**, **Adjustment** or **Expired**.

## Usage and cost

The **Usage & cost** panel is labelled with the current month. It needs one of your API keys to read the figures from the API (see [Live usage](#live-usage)); until then it says "Paste an API key in the live usage panel below to measure this billing period." with a **Connect a key** button.

| Figure | Meaning |
| --- | --- |
| Credits used, "of N credits included" | This period's use against the allowance, with a bar and a marker for where an even pace would be |
| **Credits used** | Credits used this period |
| **Projected by period end** | Where the current pace ends the month (highlighted if it passes the allowance) |
| **Included credits left** | What remains of the allowance |
| **Days left in period** | Days until the allowance refreshes |
| **Overage credits** | Credits used past the allowance |
| **Overage cost** | What that overage cost, in US dollars |

A note under the bar summarises, for example "64% of the allowance used with 9 days to go — ahead of an even pace." or "120,000 credits past the included allowance, costing $2.00."

**Credits per day** charts each day of the period. Select **Show as table** for a table of **Day**, **Calls**, **Credits** and **Errors** (also the accessible version of the chart). Before any calls: "No calls recorded in this billing period yet."

Other messages: "That key was refused. It may have been revoked — connect another one below." and "Could not reach the API just now. Your usage is still being recorded." (with **Try again**).

The four figures at the top of the console — **Active Keys**, **Requests Today**, **Rate Limit / min** and **Monthly Usage** (percentage of the allowance) — come from the same data.

## Where the credits went

A table of **Endpoint**, **Calls**, **Credits** and **Share of spend** for the current month. Before any calls: "Nothing to break down yet — this fills in once calls are recorded against the account."

## Live usage

**Live usage** shows calls arriving in real time.

1. Paste one of your API keys into **API key** (it starts `aa_live_`).
2. Select **Watch traffic**.

The key is "Kept in this browser tab only — never written to disk, never sent anywhere but the API." The same key also fills in **Usage & cost**.

Once connected (status "Live" and your tier):

- Four figures: **Calls in window**, **Calls / min**, **Error rate** and **p95 latency** (the time within which 95% of calls finished).
- **Busiest endpoints**, as bars.
- **Recent calls**: time, method, path, status, latency and cost in credits. Tick **Errors only** to filter; select **Pause** (and **Resume**) to hold the feed.
- "Connected. Make a request and it will appear here." while waiting.
- **Disconnect** forgets the key.

The feed holds the last 100 calls and resets when the API is redeployed; durable history is available from the API itself. Status messages include "Connecting…", "Reconnecting…" and "Could not connect — check the key." On a plan without API access the panel reads "Live usage becomes available once your plan includes API access." with **See plans**.

## Related

- [API keys](api-keys.md)
- [Plan & Usage section](plan-and-usage.md)
- [Refunds](refunds.md) — unused prepaid credits within 7 days
- [Subscription and Billing Policy summary](../../company-and-legal/docs/subscription-and-billing-policy.md)
