---
title: Browser extension — Privacy
description: What the Auric Artisan browser extension keeps, where, for how long, what uses the network, and how to delete it.
product: Browser extension
updated: 2026-09-25
---

# Privacy

**The extension collects nothing and sends nothing.** There are no accounts, no analytics and no network requests of its own. Everything it keeps stays in your browser. The only traffic it causes is a page you choose to open.

The full policy is at https://auricartisan.com/legal/extension-privacy/.

## Promises

1. **No network requests.** No analytics, tracking, crash reporting, remote settings or remote code.
2. **No accounts.** Nothing to sign in to, and no identifiers.
3. **Nothing leaves your device unless you click.** Links, web searches and translations open only when you choose them.
4. **Nothing is written to websites' storage.** On a page, the extension does not read or write the site's cookies, local storage or databases.
5. **Page-changing features are opt-in.** The website pickers and the custom right-click menu stay off until you turn them on.

The Firefox package declares to Mozilla, in its manifest, that it collects no data.

## What is kept, and where

Everything below lives in your browser profile. None of it is synced or sent.

| Data | Contains page content? | Kept until |
|---|---|---|
| Settings | No | You reset them or uninstall |
| Colour history (50) | Colours only | You clear it |
| Library colours (500) and palettes | Colours only | You delete them |
| Snippets (200) | Yes: the code you saved, and the address and site of the page it came from | You delete them |
| Last inspected element | Yes: its selector, styles, colours, accessibility details and up to 12 KB of its markup | The next inspection replaces it |
| Right-click menu preferences (quick bar, layout, row height) | No | You reset them |
| Picker preferences, the language, and the last tool in each space | No | You uninstall |
| A queued shortcut or menu command | No | Read once; dropped after 30 seconds |
| Audit results, page palettes, tokens, findings | Yes | The popup or side panel closes |

The last inspected element is capped in size, so a page cannot fill your extension storage.

## What uses the network

Each of these is an ordinary page visit that **you** start. The extension itself sends nothing.

| When | Opens | What the address contains |
|---|---|---|
| You install the extension | auricartisan.com, once, marked as an install visit | Nothing about you or your pages |
| You follow a link to auricartisan.com (wordmark, Home, On the web, search results) | That page | The page's address only |
| Page palette › **Open** | auricartisan.com's palette library | The palette's hex colours |
| Right-click menu › **Search the web** | Google, Bing, DuckDuckGo, Wikipedia, YouTube or Google Images | The text you selected |
| Right-click menu › **Translate** | Google Translate | The text you selected |
| Right-click menu › **Translate page** | Google Translate | The page's address |

QR codes, screenshots, colour maths, audits, vision simulations and image palettes are all made on your device. Images you drop into Image are never uploaded.

## Backups

**Download a backup** saves a file you control. It contains your settings, history, library and snippets, and snippets include the addresses of the pages they came from. Nothing is uploaded.

## Delete your data

| To delete | Do this |
|---|---|
| History and library | Settings › Data › **Clear history & library** |
| All snippets | Code › Snippets › **Clear all** |
| Settings | Settings › Data › **Reset all settings** |
| Everything | Uninstall the extension |

## Safety measures

- Addresses a page passes to the browser for downloading or opening must be ordinary web, data or blob addresses; others are refused.
- Translations can never inject code into the extension's panels.
- Backups and pasted settings are checked and capped before they are saved.
- Live CSS changes only the element you inspect, and **Reset** or **Stop** restores it.

## Related pages

- [Permissions](../docs/permissions.md)
- [Data settings](../docs/settings/data.md)
