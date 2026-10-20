---
title: Advertise — Destination and tracking
description: How to set the destination address of an Auric Artisan ad campaign, with UTM auto-tagging, custom URL parameters and tracking macros.
product: Website › Advertise
updated: 2026-09-25
---

# Destination and tracking

The **Destination URL** in the first step is where every click on your ad lands. Below it, **Destination & tracking** builds the full address that clicks will actually use, called the **Final URL**.

## The destination address

- Type the address of your landing page. If you type a bare domain such as `your-product.com`, it becomes `https://your-product.com` when you leave the field.
- **Display link** shows the short form of the address that goes with the ad: the site and the start of the path.
- **Test link ↗** opens the final address with sample values in place of the macros, so you can check it loads. It appears once the address is valid.

### What the builder checks

| Message | Meaning |
| --- | --- |
| **Enter a destination URL.** | The field is empty. |
| **That doesn't parse as a complete URL — include https://.** | The address is incomplete. |
| **Only http(s) destinations can be served.** | The address uses another scheme. |
| **Credentials inside the URL are not allowed.** | The address contains a user name or password. |
| **That hostname doesn't look reachable.** | The site name is not a full domain. |

These stop you continuing. Two warnings let you continue:

- **Not secure (http) — browsers may warn your visitors. Prefer https.**
- **Link shorteners hide the real destination from the Ad Library — use the final URL.** This appears for common shorteners such as bit.ly and tinyurl.com.

When all is well, the status reads **Looks good — clicks go straight to this URL.**, or **Looks good —** followed by how many tracking parameters **will ride along on every click.**

## Auto-tagging

**Auto-tagging** adds UTM parameters to the final address, so visits from the campaign show up attributed in your analytics. It is on by default. Untick it to send clicks to the address exactly as you typed it, plus any custom parameters.

| Parameter | Default |
| --- | --- |
| `utm_source` | `auricartisan` |
| `utm_medium` | `adssense` |
| `utm_campaign` | Made from your campaign name, for example `summer-product-launch` |
| `utm_content` | `{placement}` |
| `utm_term` | `{zone}` |

Edit any value, up to 60 characters. An empty value is left out. Leave `utm_campaign` empty to keep it following the campaign name.

## Custom URL parameters

Select **+ Add parameter** to add your own name and value, up to five parameters.

- A name can use letters, numbers, dots, dashes and underscores, up to 32 characters. Otherwise the builder says **Custom parameter names can only use letters, numbers, dot, dash and underscore.**
- A value can be up to 200 characters and can include macros.
- A parameter with the same name as a UTM parameter replaces it.
- Parameters already in your destination address are kept.
- Select **✕** to remove a parameter.

## Tracking macros

Macros are placeholders that are filled in each time the ad is shown. Select a macro chip to insert it where your cursor was in the tracking fields.

| Macro | Replaced with |
| --- | --- |
| `{placement}` | The unit that served the click: `leader`, `rect`, `strip` or `infeed`. |
| `{zone}` | The zone this campaign runs on. |
| `{campaign}` | Your campaign's order ID. |
| `{clickid}` | A unique ID for each ad shown, for attribution. |

## The final URL

**Final URL** shows the complete address, with the macros still in braces. This is the address that appears as **Destination** in the review step and in your booking request.

For example, with the defaults, a destination of `https://your-product.com/` and the campaign name "Summer product launch", the final URL is:

`https://your-product.com/?utm_source=auricartisan&utm_medium=adssense&utm_campaign=summer-product-launch&utm_content={placement}&utm_term={zone}`
