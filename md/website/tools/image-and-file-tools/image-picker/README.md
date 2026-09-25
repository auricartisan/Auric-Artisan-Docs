---
title: Image Picker — Overview
description: What the Image Picker does, who it is for, where to find it and how to take a first palette from a picture.
product: Website › Tools › Image and file tools › Image Picker
updated: 2026-09-25
---

# Image Picker

The Image Picker (the page is titled **Image Color Picker & Palette Tool**) turns a picture into a palette. Drop a photograph, a screenshot or a scan and the tool samples its pixels, groups them into clusters with the k-means++ method, and shows the resulting colours with the share of the picture each one takes up. For flat artwork such as logos and icons, where the picture has no more distinct colours than you asked for, it keeps the exact colours instead of averages.

Alongside the palette it sorts the colours into shadows, midtones and highlights, lists the pairs with the most contrast for text by the WCAG 2 ratio, and spots harmony relationships between the colours. A live eyedropper reads any pixel under the pointer, and a click pins it, so you can keep exact colours the clustering merged away. The **Analysis** tab charts the same palette four ways.

You can copy the palette as hex values, CSS custom properties or JSON, download it as SVG, JSON or CSV, and analyse a list of hex colours without any picture at all. Pictures are read in the page; nothing is uploaded.

## Who it is for

- Designers building a palette from a photograph, moodboard or product shot.
- Brand and editorial teams auditing the colours in a set of images.
- Developers who want an image's colours as CSS custom properties or JSON.
- Anyone who needs the exact colour of one pixel.

## Where to find it

Open https://auricartisan.com/tool/general/tools/image-picker/ in a current browser. It is listed as **Image Picker** on the Collections page at https://auricartisan.com/collections/. Nothing needs installing.

## Quick start

1. Open the tool. The **Workbench** tab is selected.
2. Drop an image anywhere on the large panel in the middle, or select the panel to choose a file (PNG, JPEG, WEBP, GIF or BMP).
3. The palette appears under **Extracted palette**, largest share first.
4. Move the **Clusters** slider to ask for more or fewer colours; the palette updates when you release it.
5. Hover the preview to read any pixel, and click to pin one under **Pinned**.
6. Select **Hex**, **CSS** or **JSON** under **Take it with you** to copy the palette, or **SVG** to download it.

## What you can do

- Extract 2 to 12 colour clusters (16 when the page first opens), at five sampling qualities, with optional merging of near-identical clusters.
- Leave out near-black or near-white pixels.
- Read any pixel as hex, RGB, HSL, relative luminance and position, and pin up to 24 exact colours.
- See each colour's share of the picture, its tone band, the eight strongest contrast pairs with WCAG ratings, and detected harmonies.
- Chart population, distribution, hue against saturation, and luminance, each viewable full screen.
- Copy hex, CSS custom properties or JSON; download SVG, JSON or CSV.
- Analyse a typed list of hex colours in RGB, HSL, CIELAB, LCH, luminance and tone band.
- Load a picture from a web address, where the server allows it.

## In this folder

- [docs/](docs/README.md) — how to use the tool.
  - [Getting started](docs/getting-started.md) — open it, the screen tour, the first palette.
  - [Extract a palette](docs/extract-a-palette.md) — loading pictures and every extraction setting.
  - [Pick exact colours](docs/pick-exact-colours.md) — the eyedropper and pins.
  - [Read contrast pairs, tone bands and harmony](docs/read-contrast-and-harmony.md) — what each readout means.
  - [Chart the palette](docs/chart-the-palette.md) — the four charts on the Analysis tab.
  - [Export and share](docs/export-and-share.md) — every copy and download format.
  - [Analyse a list of hex colours](docs/batch-analysis.md) — batch colour analysis.
  - [Reference](docs/reference.md) — every control, output and format.
  - [Troubleshooting](docs/troubleshooting.md) — symptoms, causes and fixes.
  - [FAQ](docs/faq.md) — short answers to common questions.
- [others/](others/README.md) — background material.
  - [Glossary](others/glossary.md) — terms used in this tool.
  - [Shortcuts](others/shortcuts.md) — keyboard shortcuts.
  - [Limits and accuracy](others/limits-and-accuracy.md) — how the palette is made and what it is not.
  - [Related](others/related.md) — related tools, the API and Learn articles.
  - [Release notes](others/release-notes.md) — user-facing history.
  - [Privacy](others/privacy.md) — what stays in your browser and what uses the network.
