---
title: Browser extension — Browser menu items
description: The Auric Artisan entries added to the browser's own right-click menu and toolbar-icon menu, what each does, and how to turn them off.
product: Browser extension › On websites
updated: 2026-09-25
---

# Browser menu items

Separately from the optional custom menu, the extension adds a few entries to the **browser's own** right-click menu, on pages and on the extension's toolbar icon. They are on by default.

## The entries

| Entry | What it does |
|---|---|
| **Inspect element** | Starts the element inspector on the page |
| **Extract page palette** | Opens the extension at Page palette and reads the page's colours |
| **Audit contrast on page** | Outlines the page's contrast problems, then opens the extension at Audit and runs it |
| **Simulate · Protanopia** | Filters the page for protanopia |
| **Simulate · Deuteranopia** | Filters the page for deuteranopia |
| **Simulate · Tritanopia** | Filters the page for tritanopia |
| **Simulate · Achromatopsia** | Filters the page for achromatopsia |
| **Clear vision filter** | Removes the vision filter |

The entries are translated when the interface is set to Hindi.

If the extension's popup cannot open by itself, open it within 30 seconds and it goes straight to the tool you chose. After 30 seconds the request is dropped, so an old action never runs later on another page.

## Turn them off

Turn off Settings › Right-click › **Items in the browser's menu** ("Add Auric Artisan entries to the browser's own right-click menu too."). The entries disappear at once.

## Related pages

- [Right-click menu](right-click-menu.md), the optional custom menu
- [Vision](../check/vision.md)
