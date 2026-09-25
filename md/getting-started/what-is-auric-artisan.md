---
title: What Auric Artisan is
description: A plain overview of the Auric Artisan website, its tools and libraries, the VS Code extensions, the browser extension and the developer services.
product: Getting started
updated: 2026-09-25
---

# What Auric Artisan is

Auric Artisan is a colour-science and accessibility platform built by one independent developer in India. It brings together practical colour tools, accessibility checks, colour-vision simulations, learning material and developer services, and it publishes the same colour engine in several places: the website at https://auricartisan.com, a set of Visual Studio Code extensions, and a browser extension.

The platform's own motto is "Tools That Respect Intelligence": the tools show their working, name the models they use and state their limits, so you can check a number rather than take it on trust.

## The website

The website is the largest part of Auric Artisan. It has four kinds of content.

### Tools

Interactive tools that run in your browser. The header's **Tools** menu groups them as follows (names as shown on the site):

| Group | Tools |
| --- | --- |
| Core tools | Portfolio Builder, Portfolio Index, Analyze URLs, Vision Simulation, Design System Generator, Color Science Lab, Basic Tools, Personalization Generator |
| Creative utilities | Image Picker, Font Library, Icon Library, Generate ASCII Art, Generate Ishihara Plates |
| Colour science | Illuminants, Chromatic Adaptation, Gamut Mapping |
| Gamut and rendering | Gamut Explorer, HDR Gamut Plot, Tonal Steps Tints and Shades, Tone Mapping |
| Perception | Perception and Vision, Neuroscience, Psychophysics Engine |
| Spectral | Material Lighting, Industrial Dye Chemistry |
| Utilities | LUT Lab, ICC Parser, Collage Maker, M-Gradient Palette, SVG Recolor |

**All Tools** (https://auricartisan.com/collections/) lists every tool in one place. Every tool is free to use; see [The free-tools model](free-tools-model.md).

The tools are documented one by one under [Website tools](../website/tools/README.md).

### Libraries

Browsable, checkable collections of colour data, each under **Learn** › **Libraries** in the header:

- **Color Library** — named colours and colour systems.
- **Palette Library** — curated palettes.
- **Gradient Library** — perceptual gradients.
- **Harmony Library** — colour relationships with the maths shown.
- **Shade Library** — tonal scales built in OKLCH (a colour space designed so that equal steps look equally different).
- **Accessibility Library** — tested accessible colour pairs.

**My Library** (under **Workspace**) holds the palettes, gradients, reports and exports you save from the tools. See [Library](../website/library/README.md).

### Learning and reference

- **Learning Hub** — lessons on colour science and accessible design, many with live interactive figures.
- **Accessibility Compliance** — WCAG checks and guidance.
- **Blog**, **Documentation** and **Changelog** — articles, technical guides and release notes.

### Your own pages

- **Portfolio Builder** lets you build and publish a public page of your work; **Portfolio Index** is a directory of published portfolios. See [Portfolio](../website/portfolio/README.md).
- An optional **account** adds a dashboard, cross-device sign-in, plan purchases and API keys. See [Account and billing](../website/account-and-billing/README.md).

## The VS Code extensions

Seventeen free extensions for Visual Studio Code, listed at https://auricartisan.com/vscode/ and on the Visual Studio Marketplace under the publisher `auric-artisan`. They cover colour themes, file and library icons, emoji, colour and WCAG linting, a secrets scanner, a live server, a file organiser, a font hub and a code formatter. The site describes every one as free, needing no account and sending no telemetry.

Two extension packs install most of them in one step:

```text
code --install-extension auric-artisan.auric-artisan-icon-pack
code --install-extension auric-artisan.auric-artisan
```

See [VS Code extensions](../vscode-extensions/README.md).

## The browser extension

A colour, accessibility and developer toolkit for your browser: an eyedropper, contrast checks, palettes, an accessibility audit, an element inspector and vision simulation, all working on the page you are looking at. The extension page (https://auricartisan.com/extension.html) describes version 1.0.1 as having 18 tools, 80 accessibility rules and 12 vision simulations, with English and हिन्दी interfaces and no network calls or telemetry. It installs from the Chrome Web Store (which also serves Edge, Opera, Brave and Vivaldi) and from Firefox Add-ons. Press `Alt` + `Shift` + `A` to open it on the current tab.

See [Browser extension](../browser-extension/README.md).

## Services for developers

- **Public REST API** — programmatic access to colour conversion, palettes, contrast, vision simulation, rendering and more, metered in API credits. API access is part of the Specialist plan and above. See [Public API](../services/public-api/README.md).
- **Font and icon delivery** — the Font Library and Icon Library on the website offer CDN-ready code for embedding their fonts and icons. See [Font CDN](../services/font-cdn/README.md) and [Icon CDN](../services/icon-cdn/README.md).
- **Design-tool plugins** — see [Design-tool plugins](../design-tool-plugins/README.md) for the plugins you can actually install.

## What Auric Artisan is not

The site is explicit about its limits, and so are these docs:

- It is an independent private platform, not a government body, standards organisation or certification laboratory.
- Vision simulations and the Ishihara-style plate generator are for learning and design. They are not medical tests and do not diagnose anything.
- Web analysis results are guidance. They are not a certified accessibility audit, security audit or penetration test.
- Colour-science outputs are grounded in published CIE and W3C methods, but they do not replace calibrated instruments for colour-critical industrial work.

## Related

- [How the pieces fit](how-the-pieces-fit.md)
- [Choose where to start](choose-where-to-start.md)
- The official About page, summarised in [About Auric Artisan](../website/company-and-legal/docs/about.md)
