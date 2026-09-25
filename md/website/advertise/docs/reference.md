---
title: Advertise — Reference
description: Every control, option, price, limit and message in the AdsSense campaign builder and the Ad Library.
product: Website › Advertise
updated: 2026-09-25
---

# Advertise reference

## Formats

| Format | Size | INR a day | USD a day | Typical CTR |
| --- | --- | --- | --- | --- |
| **Leaderboard** | 728×90 | ₹399 | $5 | ~0.4% |
| **Medium Rectangle** | 300×250 | ₹499 | $6 | ~0.7% |
| **Native In-Feed Card** | Card, artwork 720×600 | ₹649 | $8 | ~1.2% |
| **Panels & Search Strip** | 320×100 | ₹299 | $4 | ~0.5% |

The daily prices are the "from" prices; the zone, flight and share change the total.

## Zones

| Zone | Estimated views a day |
| --- | --- |
| **Homepage** | ~1,400 |
| **Learn library (113 articles)** | ~2,600 |
| **Tools & workspaces** | ~1,900 |
| **Collections · Blog · Docs** | ~1,100 |
| **Run of site (everywhere)** | ~7,000 |

## Step 1: Basics

| Control | What it does | Values or range | Default |
| --- | --- | --- | --- |
| **Campaign name** | Your own name for the campaign. | 2 to 80 characters | Empty |
| **Brand / company** | Who runs the campaign; also the studio's fallback headline. | 2 to 80 characters | Empty |
| **Destination URL** | Where clicks land. | http or https; the field takes up to 500 characters | Empty |
| **Display link** | Short form of the destination. | — | — |
| **Test link ↗** | Opens the final address with sample macro values. | — | — |
| **Auto-tagging** | Adds UTM parameters. | On, off | On |
| `utm_source` … `utm_term` | UTM values. | Up to 60 characters each | See below |
| **+ Add parameter** | Adds a custom parameter. | Up to 5; name up to 32, value up to 200 characters | None |
| Macro chips | Insert a macro in the last-used tracking field. | `{placement}`, `{zone}`, `{campaign}`, `{clickid}` | — |
| **Final URL** | The complete click address. | — | — |
| **What should this campaign do?** | Sets a goal and applies its recommendations. | **Brand awareness**, **Site traffic**, **Product launch** | **Brand awareness** |

Default UTM values: `utm_source=auricartisan`, `utm_medium=adssense`, `utm_campaign` from the campaign name, `utm_content={placement}`, `utm_term={zone}`.

## Step 2: Format

| Control | What it does | Values | Default |
| --- | --- | --- | --- |
| Format cards | Choose the format. | The four formats | **Leaderboard** |
| **Recommended** badge | Marks the format your goal recommends. | — | — |

## Step 3: Creative

| Control | What it does | Values or range | Default |
| --- | --- | --- | --- |
| **Creative source** | Studio or upload. | **Design it here**, **Choose a file** | **Design it here** |
| **Headline** | Main line. | Up to 40 characters | Brand name |
| **Supporting line** | Second line. | Up to 60 characters | "Reach people who work in color" |
| **Call to action** | Button text. | Up to 20 characters | "LEARN MORE" |
| **Creative description** | Screen-reader description. | Up to 120 characters | Made from the brand name |
| **Background** | Background colour. | Any colour | #FFF8EC |
| **Accent** | Border, mark and button colour. | Any colour | #D3AF37 |
| **Text** | Text colour. | Any colour | #1F2937 |
| Upload area | Takes artwork. | PNG, JPG, WebP, SVG; up to 300 KB | — |
| **Remove** | Clears the uploaded file. | — | — |
| **Live preview** | Shows the creative at the format's ratio. | — | — |

## Step 4: Audience

| Control | What it does | Values | Default |
| --- | --- | --- | --- |
| **Where it runs** | Chooses the zone. | The five zones | **Run of site (everywhere)** |
| **Creative context** | Guides the creative review. | Up to 3 of **Designers**, **Developers**, **Color scientists**, **Educators**, **Studios & teams** | None (**Everyone**) |
| **Frequency cap** | Most views per visitor per session. | **1 / session**, **2 / session**, **3 / session** | **2 / session** |

## Step 5: Budget

| Control | What it does | Values | Default |
| --- | --- | --- | --- |
| **Flight length** | How long it runs. | **1 week**, **2 weeks** (save 5%), **1 month** (save 15%), **3 months** (save 28%) | **1 month** |
| **Start date** | First day, from 00:00 IST, after creative approval. | Tomorrow or later | Tomorrow |
| **Share of voice** | Share of eligible renders reserved. | **25% share**, **50% share**, **100% takeover** | **50% share** |
| **Currency** | Currency of the quote. | **INR ₹**, **USD $** | **INR ₹** |
| **Promo code** | Applies a discount. | Up to 24 characters | Empty |

## Step 6: Review

| Control | What it does | Values | Default |
| --- | --- | --- | --- |
| **Campaign summary** | Every choice and the total. | — | — |
| **Billing email** | Where receipts and updates go. | A valid email address | Empty |
| Policy checkbox | Accepts the creative and acceptable-use policy and the refund policy. | Ticked, unticked | Unticked |

## Quote panel

| Item | Meaning |
| --- | --- |
| **Step N/6** | The current step. |
| **Base run**, **Flight discount**, **Promo**, **Tax**, **Total** | The price lines. Discount, promo and tax lines show only when they apply. |
| **impressions**, **est. uniques**, **est. clicks**, **eff. CPM** | The delivery estimate. |
| **Complete campaign to request booking** | The button before every step is complete. |
| **Request campaign — total (pay on approval)** | Sends the booking request. |

## Messages

| Message | When |
| --- | --- |
| **Add a campaign name to continue.** | Campaign name under 2 characters. |
| **Add the brand or company running this campaign.** | Brand under 2 characters. |
| **Enter a destination URL.** | Destination empty. |
| **That doesn't parse as a complete URL — include https://.** | Destination incomplete. |
| **Only http(s) destinations can be served.** | Another scheme. |
| **Credentials inside the URL are not allowed.** | User name or password in the address. |
| **That hostname doesn't look reachable.** | Not a full domain. |
| **Not secure (http) — browsers may warn your visitors. Prefer https.** | Warning for http. |
| **Link shorteners hide the real destination from the Ad Library — use the final URL.** | Warning for a shortener. |
| **Custom parameter names can only use letters, numbers, dot, dash and underscore.** | Bad parameter name. |
| **Choose an artwork file or switch to the creative studio.** | Upload chosen, no file. |
| **Choose a PNG, JPG, WebP or SVG image.** | Wrong file type. |
| **That file is over 300 KB — please compress it.** | File too large. |
| **That file could not be read as an image.** | Damaged or unreadable file. |
| **Artwork removed. Choose a new file to continue.** | After **Remove**. |
| **Choose a valid campaign start date.** | Start date missing or in the past. |
| **Enter a valid billing email.** | Billing email not valid. |
| **Accept the creative and refund policies before checkout.** | Policy box unticked. |
| **unknown code** | Promo code not recognised. |
| **Sending booking request…** | Request on its way. |
| **Request received. We confirm availability and send a Razorpay payment link within 1 business day — your campaign goes live after payment.** | Request sent. |
| **Could not send the request — please email ads@auricartisan.com with your campaign details.** | Request failed. |

## Ad Library controls

| Control | What it does | Values | Default |
| --- | --- | --- | --- |
| **Search advertiser or text…** | Filters by advertiser, text or landing address. | Any text | Empty |
| Format chips | Filter by format. | **All formats**, **Leaderboard**, **Rectangle**, **In-feed**, **Strip** | **All formats** |
| Status chips | Filter by status. | **All**, **Active**, **Ended** | **All** |
| **Report this ad** | Opens the contact page. | — | — |
