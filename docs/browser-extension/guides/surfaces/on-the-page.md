---
title: Browser extension — On the page
description: Everything the extension can draw on a website, when it appears, how it is isolated from the site, and how to remove it.
product: Browser extension › Surfaces
updated: 2026-09-25
---

# On the page

Most of the extension lives in the popup and side panel. A few features appear on the website itself. This page lists each one, when it appears, and how to make it go away.

## What can appear on a page

| What | Appears when | Goes away when |
|---|---|---|
| **Element inspector**: a highlight box, a card and a bar at the bottom | You start Inspect (Home, Code › Inspect, the right-click menu or a shortcut) | You press `Esc` (twice if a card is pinned), choose **Stop**, or go to another page |
| **Vision filter**: the page recoloured or blurred, with a small status strip | You choose a simulation in Check › Vision, the browser's right-click menu, or press `Alt` + `Shift` + `V` | You choose **Clear**, **Clear vision filter**, press `Alt` + `Shift` + `V` again, or reload |
| **Side-by-side comparison**: half the page filtered | You choose **Side-by-side** in Check › Vision, or **Side by side** in the right-click menu | You clear the filter |
| **Audit outlines**: a red or amber outline and a label on each flagged piece of text | **Outline on page**, **Outline issues after an audit**, or **Audit contrast on page** in the browser's menu | After 15 seconds, or when you run the outlines again |
| **Live CSS preview**: your CSS applied to one element | You choose **Apply to page** in Code › Inspect › Live CSS | You choose **Reset** or **Stop** |
| **Website pickers** | Settings › Pickers › **Auric pickers on websites** is on | You turn the setting off, or add the site to **Never on** |
| **Custom right-click menu** | Settings › Right-click › **Custom right-click menu** is on and you right-click | You press `Esc`, click away, or run an action |
| **Screen eyedropper** | You choose **Pick from page** or **Pick a colour** (Chromium only) | You click a pixel or press `Esc` |

## The audit outlines

In this version, the outlines mark the page's own elements:

- **Red** outlines mark text that fails its contrast threshold.
- **Amber** outlines mark borderline text that passes but by less than 1.5.
- Each outline carries a label with the measured ratio and the one it needs, such as `3.12:1 needs 4.5:1`, and "+ manual review" where the text sits on an image, gradient or shadow.

They clear themselves after 15 seconds. Running them again replaces the old set.

## Kept apart from the site

The inspector card, the website pickers, the colour picker on pages and the right-click menu each live in their own isolated area of the page (a shadow root). The site's CSS cannot change how they look, and their styles cannot change the site's layout. They also follow your theme and accent colour.

- The extension never writes to a website's storage: it does not read or change the site's cookies, local storage or databases.
- The inspector's Live CSS changes only the element you inspect, and **Reset** or **Stop** restores it exactly.
- A page removing an element you pinned does not leave a stale card: the inspector lets go of it.

## Where nothing appears

- **Browser pages and the web stores.** Extensions cannot run there.
- **Frames inside a page.** The extension's page script runs in the top page only, so content inside an embedded frame is not inspected, audited or given pickers.
- **auricartisan.com.** The website pickers and the custom right-click menu stay off there, because the site has its own.

## Related pages

- [Element inspector](inspector.md)
- [Vision](../check/vision.md)
- [Audit](../check/audit.md)
- [On websites](../on-websites/README.md)
