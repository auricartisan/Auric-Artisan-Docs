---
title: Design tool plugins — Status
description: Which Auric Artisan plugins for design tools and launchers exist, what they are planned to do, and why none can be installed yet.
product: Design tool plugins
updated: 2026-09-25
---

# Design tool plugins

Auric Artisan is building small plugins that bring its colour and accessibility checks into design tools and launchers: Figma, Penpot, Sketch, Raycast and Alfred. **None of them is published yet.** There is no listing in the Figma Community, the Penpot plugin catalogue, the Raycast Store or elsewhere, and no download on auricartisan.com. This page will become full documentation for each plugin when it can be installed.

In the meantime, the same checks are available today in the [browser extension](../browser-extension/README.md), in the VS Code extensions (see the VS Code extensions section of these docs), and in the tools on https://auricartisan.com.

## What exists

| Plugin | Host | Planned purpose | Status |
|---|---|---|---|
| Auric Artisan for Figma | Figma | Audit layers for WCAG and APCA contrast, generate palettes, fix failing pairs, preview colour vision | Not published |
| Auric Artisan for Penpot | Penpot | The same audit, palette, fix and vision workflow for Penpot files | Not published |
| Auric Artisan for Sketch | Sketch on macOS | Menu commands to audit a selection, auto-fix failing pairs, generate a palette and preview colour vision | Not published |
| Auric Artisan for Raycast | Raycast on macOS | A **Check Contrast** command for any two colours, with WCAG and APCA results | Not published |
| Auric Artisan for Alfred | Alfred on macOS | A contrast check typed as `aa contrast` followed by two colours | Not published |

The site's article "Auric Artisan Plugins User Guide" (https://auricartisan.com/library/documentation/articles/2026-05-26-plugins-user-guide) describes how the plugins are intended to work. Because none of them can be installed from a store or a download today, treat that article as a preview rather than installation instructions.

## Planned capabilities in brief

These descriptions come from the site's plugins guide and may change before release.

- **Design plugins (Figma, Penpot, Sketch):** check the contrast of text against its effective background in the selected frame or layers (or the current page when nothing is selected), report the WCAG ratio and APCA Lc of failing pairs, select or outline failing layers, nudge failing colours toward a target ratio, generate palettes from a seed colour, and preview protanopia, deuteranopia, tritanopia and achromatopsia.
- **Launcher plugins (Raycast, Alfred):** check the contrast of two colours typed as HEX, `rgb()`, `hsl()` or CSS colour names, and copy the ratio, the APCA value, normalised HEX values or a summary.
- **Privacy:** the plugins are designed to run locally in their host application, without an Auric Artisan account or API key for contrast checks.

## When they are released

This folder will then hold, for each published plugin, the standard set of pages: an overview, installation from its store, getting started, every command and option, troubleshooting, an FAQ, a glossary, release notes and privacy.

## Related pages

- [Browser extension](../browser-extension/README.md)
- [Public API](../services/public-api/README.md)
