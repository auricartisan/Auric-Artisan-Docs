---
title: Basic Color Tools — Overview
description: What Basic Color Tools is, who it is for, where to find it and how to start using its panel workspace and the site-wide Colour Tools.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Basic Color Tools

Basic Color Tools is a workspace for everyday colour work on the Auric Artisan website. It brings seven small tools together on one page: **Palette Studio**, **Palette Remix**, **Gradient Maker**, **Color Picker**, **Color Battle**, **Collage Maker** and **Quick Converter**. Each tool opens as a floating panel with a controls sidebar on the left and a work area on the right. You can keep up to five panels open at once, move and resize them, dock them, and switch between them without leaving the page.

The same folder also documents the **Colour Tools** workbench: fourteen further floating tools (such as **Color Inspector**, **Contrast System** and **CMYK Soft-Proof**) that you can open on any page of the site from the right-click menu, with `Ctrl` + `Shift` + `C`, or by adding `?color=` to a page address. When a page cannot open those tools, the site sends you to Basic Color Tools instead, so the two belong together.

Everything runs in your browser. Palettes, gradients, colours and collages are computed on your device, images you add are read locally, and your preferences (favourites, level, last view) are remembered in your browser's local storage. You can save results to your Auric Artisan Library and reopen them in the right tool later.

## Who it is for

- Designers who need a quick palette, gradient or colour conversion without opening a large application.
- Front-end developers who want CSS, SCSS, Tailwind or JSON output for a palette or gradient.
- Accessibility reviewers who want contrast ratios, WCAG pass levels and colour-vision previews next to the palette they are building.
- Students and colour enthusiasts who want to see a colour in many formats and colour spaces at once.

## Where to find it

- Page: https://auricartisan.com/tool/basic-tools/ (the short address https://auricartisan.com/basic-tools also opens it).
- The Colour Tools workbench: right-click anywhere on a page of the site and use the **Colour tools** group, or press `Ctrl` + `Shift` + `C`.
- No sign-in is needed to use the tools. Saving to the Library uses your Library; see [Import, export and the Library](docs/import-export-and-library.md).

## Quick start

1. Open https://auricartisan.com/tool/basic-tools/. The page opens on the **Workspace** view.
2. In the **Open a tool** list on the left, select **Palette Studio**. It opens as a panel on the stage to the right.
3. Select **Generate** (or press `Space` while the panel is focused) until you like the palette.
4. Hover over a colour and select the lock button to keep it, then generate again: locked colours stay put.
5. Open the **Contrast Matrix** or **WCAG Pairs** tab in the panel to check contrast between your colours.
6. In the **Export** section of the sidebar, select **CSS** to copy the palette as CSS custom properties, or **PNG** to download an image of it.
7. Open **Gradient Maker** from the list as well. Both panels stay open side by side; drag a title bar to arrange them.
8. Select **Save to Library**, the floating button near the bottom-right corner of the page, to keep the focused panel's result for later.

## What you can do

- Generate palettes from thirteen harmony and accessibility modes, lock colours, edit them in OKLCH and extract colours from an image.
- Remix a set of seed colours into four styled variant palettes.
- Build linear, radial and conic gradients with any number of stops, perceptual interpolation and easing, then export CSS, SVG, PNG (1600 px or 4K), JSON or a Tailwind snippet.
- Pick one colour and read it in HEX, RGB, HSL, HSV, OKLCH, Lab, XYZ and CMYK, with harmonies, colour-vision previews and contrast against common backgrounds.
- Score two palettes against each other for contrast, perceptual separation and colour-vision resilience.
- Compose local images into one of 29 collage layouts and export a 4K PNG.
- Convert any colour between fourteen notations and compare two colours by ΔE and contrast.
- Open fourteen more colour tools over any page through the Colour Tools workbench.
- Save results to your Library and reopen them later in the matching tool.

## In this folder

- [docs/](docs/README.md) — how to use the workspace and every tool.
  - [Getting started](docs/getting-started.md) — open the page, tour the screen, make a first palette.
  - [Workspace and panels](docs/workspace-and-panels.md) — the three views, the catalogue, search and level, favourites, panel windows.
  - [Import, export and the Library](docs/import-export-and-library.md) — every export format, the share link, Save to Library and restoring.
  - [Panel tools](docs/panel-tools/README.md) — one guide per workspace tool.
  - [Colour Tools workbench](docs/colour-tools/README.md) — the fourteen site-wide colour tools and their launcher.
  - [Reference](docs/reference.md) — every control, option, range and format.
  - [Troubleshooting](docs/troubleshooting.md) — symptoms, causes and fixes.
  - [FAQ](docs/faq.md) — short answers to common questions.
- [others/](others/README.md) — supporting material.
  - [Glossary](others/glossary.md) — the colour and accessibility terms used here.
  - [Shortcuts](others/shortcuts.md) — keys and mouse gestures.
  - [Limits and accuracy](others/limits-and-accuracy.md) — what the numbers mean and what they are not.
  - [Related](others/related.md) — related tools, libraries and Learn articles.
  - [Privacy](others/privacy.md) — what stays on your device and what is stored.
