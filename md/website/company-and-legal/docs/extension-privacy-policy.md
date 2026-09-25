---
title: Browser Extension Privacy Policy — summary
description: A plain-language summary of the privacy policy for the Auric Artisan browser extension — what it accesses, what it stores locally, its permissions and what it never does.
product: Website › Company and legal
updated: 2026-09-25
---

# Browser Extension Privacy Policy

Official page: https://auricartisan.com/legal/extension-privacy/ — version 1.0, effective and last updated 27 July 2026. **The official policy is authoritative.** The website itself is covered by the separate [Privacy Policy](privacy-policy.md).

## Key points

- The extension only touches page content when you use a tool on that page.
- Settings, saved colours and history live in your browser's extension storage.
- No analytics, no telemetry, and no page data is transmitted anywhere.
- Nothing is sold, rented or shared — "there is nothing to sell".
- Three permissions are optional and requested only when you turn on the feature that needs them.

## Section by section

1. **Scope** — The colour, accessibility and developer toolkit for Chromium-based browsers (Chrome, Edge) and Firefox.
2. **What it accesses**
   - *Page content, only when you act* — the eyedropper, contrast and accessibility audits, vision filters, element inspector and palette extraction read the page at the moment you use them; nothing scans in the background.
   - *Settings and library* — kept in the browser's local extension storage.
   - *Optional account sync* — if you connect the extension to an Auric Artisan account in future, only what you choose to sync would be sent. No account is required and nothing syncs by default.
3. **What it never does** — No analytics or telemetry; no sending of page data (colour maths, audits and simulations run locally; page content, URLs, screenshots and results never leave your device); no sale or sharing of data. "In short: all processing is local; the extension makes no network requests with your data."
4. **Permissions**

   | Permission | Required or optional | Why |
   | --- | --- | --- |
   | Host access | Required | Run tools on the page you use them on |
   | Scripting | Required | Add the tool script when needed |
   | Storage | Required | Your settings and library |
   | Clipboard write | Required | Copy colour values and snippets |
   | Context menus | Required | Tool shortcuts in the right-click menu |
   | Side panel (Chrome) | Required | Dock the workspace |
   | Clipboard read | Optional | **Paste** in the custom menu |
   | Downloads | Optional | **Save As** from the menu |
   | Sessions | Optional | Reopen a closed tab |

   The optional ones are requested only when you turn on the custom context menu, and you can decline or revoke them in your browser.

5. **Storage and deletion** — Everything is in local extension storage. Clear the colour library and history from the extension's settings, or uninstall to remove everything.
6. **Changes** — A version that changes what the extension accesses or stores will come with an updated policy, and material changes will be noted in the store listing's changelog.
7. **Contact** — Through the contact page.

## Related

- [Browser extension](../../../browser-extension/README.md)
- [Privacy overview](../../../help/privacy.md)
