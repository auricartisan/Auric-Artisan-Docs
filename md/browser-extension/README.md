---
title: Browser extension — Overview
description: What the Auric Artisan browser extension is, who it is for, where to get it and how to start using it.
product: Browser extension
updated: 2026-09-25
---

# Auric Artisan browser extension

Auric Artisan for the browser puts colour, accessibility and front-end tools on every page you open. You pick a colour from the screen, check a colour pair against WCAG and APCA contrast, audit a whole page for accessibility problems, inspect any element, read a site's design tokens, and see the page as people with different kinds of vision see it. It is one extension, published as **Auric Artisan**, and every tool ships in the same install: there is no paid edition and no second download.

The extension runs entirely on your device. It has no account, no sign-in, no analytics and makes no network requests of its own. Everything you pick, audit or save stays in your browser's extension storage. The only traffic it causes is a page you choose to open, such as a link to auricartisan.com or a web search you start from the right-click menu.

The tools live in a workspace you open from the toolbar icon or dock beside the page in the browser's side panel (the sidebar in Firefox). The workspace has a **Home** screen and four spaces, **Colour**, **Check**, **Code** and **Saved**, and a search field that finds any tool, setting or auricartisan.com page. Two optional features work on websites themselves, and both are off until you turn them on: Auric pickers for a page's form controls, and a right-click menu built around what you clicked. The interface is available in English and Hindi (हिन्दी).

> **Note:** These pages describe version 1.0.2. To see which version you have, open your browser's extensions page. Changes that are built but not yet released are listed as upcoming in the [release notes](others/release-notes.md).

## Who it is for

- **Designers** who need to sample colours from live sites, build scales and harmonies, and check that a palette is readable.
- **Front-end and full-stack developers** who inspect elements, copy CSS and selectors, and export colours and tokens as CSS, Tailwind, SwiftUI, Jetpack Compose or Android code.
- **Accessibility specialists and testers** who audit pages against WCAG 2.2 A and AA, check contrast in WCAG and APCA, and simulate colour-vision deficiencies and low vision.
- **Students and colour enthusiasts** who want to read a colour in twelve formats and learn how colour spaces relate.

## Where to find it

| Browser | Where to get it |
|---|---|
| Chrome, Brave, Vivaldi, Arc | Chrome Web Store: https://chromewebstore.google.com/detail/auric-artisan/bpmkaljljnlmbjfbmkbbbgiinlbpcocp |
| Microsoft Edge, Opera | The same Chrome Web Store listing, or the Edge or Opera package from https://auricartisan.com/extension |
| Firefox 115 and later | Firefox Add-ons: https://addons.mozilla.org/en-US/firefox/addon/auric-artisan/ |
| Safari on macOS | Not published. You can convert the Chromium package yourself with Xcode. |

The product page is https://auricartisan.com/extension. It also offers the packages as ZIP files for anyone who prefers to load the extension from a folder. The extension is free. Full steps for each browser are in [Install](docs/install/README.md).

## Quick start

1. Install the extension from your browser's store (see [Install](docs/install/README.md)) and pin **Auric Artisan** to the toolbar.
2. Open a normal web page, then click the toolbar icon or press `Alt` + `Shift` + `A`. The first-run tour shows you around in five steps.
3. On **Home**, choose **Pick a colour** and click any pixel on the screen. The colour opens in the Picker in twelve formats.
4. Press `Alt` + `Shift` + `C` to open **Contrast**. Enter a text colour and a background colour, then choose **Fix text** to find the nearest colour that passes.
5. On **Home**, choose **Audit**. The page is checked against WCAG 2.2 A and AA; choose **Outline on page** to see where the contrast problems are.
6. On **Home**, choose **Inspect**, then click anything on the page. Press `C` to copy its CSS.
7. Press `Alt` + `Shift` + `V` to see the page with a deuteranopia simulation. Press it again to clear it.
8. Choose **Open the side panel** in the header if you want the workspace to stay open while you browse.

## What you can do

- Pick any pixel on screen and read it as HEX, RGB, HSL, HSV, HWB, CMYK, LAB, LCH, OKLAB, OKLCH, XYZ or Display P3.
- Copy a colour as code for CSS, wide-gamut CSS, Tailwind v4, SwiftUI, Jetpack Compose or Android.
- Read every colour a page uses and export it as Tailwind, `@theme`, SCSS, W3C design tokens, JSON, ASE, SVG or PNG.
- Build a palette from an image or a capture of the visible tab.
- Build gradients, mix colours, generate harmonies and Tailwind or Material scales, and convert between formats.
- Check any colour pair in WCAG 2.2 and APCA, and find the nearest passing text or background colour in one click.
- Audit a page with the 78 WCAG 2.2 A and AA rules of an 80-rule engine plus a fast contrast scan, and export the results as JSON or CSV.
- See the page through twelve simulations: eight colour-vision deficiencies and four low-vision conditions.
- Inspect any element: contrast first, then its box model, colours, layout, type, effects, accessibility and CSS.
- Read a site's design tokens: CSS variables, type scale and fonts.
- Keep a colour library, a history of your last 50 colours and a vault of code snippets.
- Give a website's form controls Auric pickers, and use a right-click menu that knows what you clicked.
- Use the whole interface in English or Hindi.

## In this folder

- [docs/](docs/README.md) — how to install and use the extension
  - [Getting started](docs/getting-started.md)
  - [Install](docs/install/README.md): Chrome and Chromium browsers, Edge, Opera, Firefox, Safari, loading from a ZIP, updating and removing
  - [Surfaces](docs/surfaces/README.md): the popup, Home, search, the side panel, what appears on the page, the element inspector
  - [Colour tools](docs/colour/README.md): Picker, Page palette, Image, Gradient, Mix, Harmony, Scale, Convert
  - [Check tools](docs/check/README.md): Contrast, Vision, Audit, the audit rules, Findings
  - [Code tools](docs/code/README.md): Inspect, Tokens, Snippets, code export
  - [Saved](docs/saved/README.md): Library, History, On the web
  - [On websites](docs/on-websites/README.md): website pickers, the colour picker on pages, the right-click menu, items in the browser's menu, notes for site owners
  - [Workflows](docs/workflows/README.md): end-to-end tasks
  - [Settings](docs/settings/README.md): every section of Settings
  - [Hindi interface](docs/hindi-interface.md)
  - [Permissions](docs/permissions.md)
  - [Reference](docs/reference.md)
  - [Troubleshooting](docs/troubleshooting.md)
  - [FAQ](docs/faq.md)
- [others/](others/README.md) — background material
  - [Glossary](others/glossary.md)
  - [Keyboard shortcuts](others/shortcuts.md)
  - [Limits and accuracy](others/limits-and-accuracy.md)
  - [Related tools](others/related.md)
  - [Release notes](others/release-notes.md)
  - [Privacy](others/privacy.md)
