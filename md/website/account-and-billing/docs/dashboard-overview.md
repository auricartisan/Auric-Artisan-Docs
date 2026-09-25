---
title: Dashboard — Overview section
description: Every part of the Overview section of the Auric Artisan dashboard — the statement, your saved work, next steps, quick links and the side column.
product: Website › Account and billing
updated: 2026-09-25
---

# Overview section

The **Overview** is the first section of the dashboard (https://auricartisan.com/auth/dashboard/#overview). It answers "is my account in order?" first, then shows your work, then suggests what to do next. Everything it shows is read from your account and from this browser; a part with nothing true to say is left out rather than filled with zeros.

On a wide screen the Overview has a main column and a side column. On a screen narrower than about 1,024 pixels, the side column moves to the top because it holds the things you most need to act on.

## The statement

The statement opens the main column.

- **Statement** — the heading is the current month and year.
- A one-line summary appears when there is something to say, for example "One key is doing the work." or "3 keys are in use."

Below it is a ledger. A row appears only when it has a real value:

| Row | Shows |
| --- | --- |
| **Plan** | Your plan name |
| **Credits used** | API credits used this billing period, with the period as a note (plans with API access, once usage has loaded) |
| **Credits left** | Included API credits left, with "N days left in the period" |
| **Your work** | The number of items you have saved, with a note such as "12 palettes · 3 collections · 40 KB"; or **Nothing yet** |
| **Two-factor authentication** | **On**, or **Not set up** with a **Set it up** button that opens Security & Privacy |

If rows are left out, a line says so, for example "3 more rows appear here once there is something to put in them — credits, storage, a published page."

Whether your portfolio is published is shown in the **Profile** section, on the **Public portfolio** card.

When API usage has loaded, a small table, **Where the credits went**, lists the endpoints that used the most credits.

At the foot, **Plan & usage in full** opens the Plan & Usage section.

## Your work

- The heading counts what you have saved, for example "12 things you made.", or reads "Nothing here yet."
- The line under it reads "Palettes, scales and gradients from your Universal Library, newest first." or, when empty, "Anything you save from a tool lands here. Open a tool and make something."
- **Open the library** (or **Open the tools** when empty) takes you there.
- Up to twelve tiles show your newest saved items. Each tile shows the colours as swatches, the name, up to two hex values and how long ago it changed. Select a tile to open the library.

The count comes from the library saved in this browser. Work saved in another browser is not included.

## Next

Up to three suggestion cards, each with a button and a **×** to dismiss it. Suggestions only appear when they apply:

| Card | Shown when | Button |
| --- | --- | --- |
| **Turn on two-factor** | Two-step verification is off (highlighted as the most urgent) | **Set it up** |
| **Group your work** | You have more than two saved items and no collections | **Open the library** |
| **Make an API key** | You have no API keys | **Create a key** |

Dismissing a card hides it in this browser. Clearing the browser's site data brings dismissed cards back.

> **Note:** API keys work only on plans that include API access (Specialist and above). On other plans, **Make an API key** leads to a section that explains the API is not part of your plan.

## Start something

A row of quick links: **Colour tools**, **Palettes**, **Gradients**, **Shades**, **Contrast**, **Analyse a page** and **All tools**.

## The side column

### Finish setting up

A checklist of four items, with a progress ring and a count such as "2 of 4 done":

1. **Add your name**
2. **Choose a username**
3. **Verify your email**
4. **Add a profile photo**

Each unfinished item has a button (**Add**, **Pick** or **Verify**) that opens the Profile section. The card disappears once all four are done.

### Tool tokens

Your token balance for server-backed tool work.

- The large figure is your balance.
- Beside it: "of 250 a month" (for example) on a plan with a monthly allowance, or "tokens" on the free plan's one-time grant.
- The bar shows how much of this period's included allowance is left. It is hidden for a one-time grant, which never expires.
- The note explains the balance, for example "250 of these lapse at the end of the period.", "100 do not expire.", or "This period's allowance is waiting to be claimed."

The card is hidden if you have no balance and no allowance. See [Tokens](tokens.md).

### This device

Shows the browser and operating system you are using now, for example "Chrome on Windows", with **Active now**.

## Related

- [Getting started with the dashboard](getting-started.md)
- [Profile section](profile.md)
- [Plan & Usage section](plan-and-usage.md)
- [Security & Privacy section](security-and-privacy.md)
