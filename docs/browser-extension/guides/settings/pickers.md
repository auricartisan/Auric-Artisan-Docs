---
title: Browser extension — Pickers settings
description: Turn the website pickers on or off, choose which control types they enhance, respect designed controls, and list sites where they never run.
product: Browser extension › Settings
updated: 2026-09-25
---

# Pickers settings

Settings › **Pickers** controls the Auric pickers that replace a website's form controls. What the pickers do is described in [Website pickers](../on-websites/website-pickers.md).

## Switches

| Switch | Default | What it does |
|---|---|---|
| **Auric pickers on websites** | Off | The master switch: Auric panels replace the browser's own. Nothing below applies while it is off. |
| **Leave designed controls alone** | On | Controls the site restyled, or replaced with its own widget, keep their own look |

## Picker types

Thirteen chips, all on by default. The heading counts them ("13 of 13 on"). Untick a chip to keep that type native everywhere.

**Colour**, **Select**, **Multi-select**, **Suggestions**, **Date**, **Date & time**, **Month**, **Week**, **Time**, **Number**, **Range**, **File**, **Checkbox & radio** (one chip for both).

"A file picker still opens the browser's own dialog — only the button is ours."

## Never on

Sites where every picker stays native.

1. Type a site into **Add a site, e.g. example.com**. You can paste a full address; only the site name is kept, without `www.`.
2. Choose **Add**. A message confirms "Pickers stay native on example.com".
3. Remove a site with its **✕** button.

- Subdomains are included: adding `example.com` also covers `shop.example.com`.
- The list holds up to 100 sites.
- **auricartisan.com** is always on the list and cannot be removed ("has its own pickers").
- Text that is not a site address is refused ("That is not a site address"), and a site already listed says "Already on the list".

## Related pages

- [Website pickers](../on-websites/website-pickers.md)
- [For site owners](../on-websites/for-site-owners.md)
