---
title: Feature Kit — Privacy
description: What the Feature Kit keeps in your browser, what it sends, and how to remove it.
product: Website › Kits › Feature Kit
updated: 2026-09-25
---

# Feature Kit privacy

The Feature Kit runs in your browser. Apart from feedback you choose to send and the unit list it downloads, nothing leaves your device.

## Kept in your browser

| What | Details | How to remove it |
|---|---|---|
| Calculator history | Your last 100 calculations: the expression, the result and the time | **History** > bin icon in the heading |
| Notes | Every note's text, title and last-saved time | **Delete** on each note |
| Recent dates | The last 8 dates you picked in the Calendar tab | Clear the site's data in your browser |
| Kit preferences | Position, expanded size, Focus mode, the tool that was open while Focus mode was on, and the kit theme | Clear the site's data |
| Feedback | Each submission, kept so it can be retried until delivered, along with when you were last prompted and how often you dismissed prompts | Clear the site's data |

## Not kept

- Calculator variables, functions you define and the memory value (cleared when you leave or reload the page).
- The angle setting (**RAD** or **DEG**) and the graph's **y =** expression.
- Anything you type into the Unit Converter or the Developer Tools.
- Text in the feedback form until you send it.

## Sent over the network

| When | What is sent or fetched |
|---|---|
| You open the Unit Converter for the first time on a page | The kit downloads the unit list from auricartisan.com. Nothing about you is sent |
| You submit feedback | Your rating (1 to 5), your comment or answers, the path of the page you were on (for example `/tool/analyzer/`), and which tool you used last in the kit. If you are signed in, the feedback is linked to your account |

The Developer Tools never send what you paste. Hashes, HMAC signatures and UUIDs are computed by your browser.

## Feedback delivery

Feedback is saved on your device first and then sent. If sending fails, it stays on your device and is retried automatically, for example when your connection comes back. Feedback written while signed in to one account is only sent while that same account is signed in.

## Related

- [Privacy for all kits](../../others/privacy.md)
- The site's privacy policy: https://auricartisan.com/legal/privacy/
