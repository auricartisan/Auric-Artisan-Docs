---
title: Tonal Steps — Overview
description: What the Tonal Steps, Tints and Shades tool does, who it is for, where to find it and how to build your first ramp.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Tonal Steps

Tonal Steps builds a lightness **ramp** from one colour: a sequence of steps running from white, through versions of your colour, to black. Alongside it the tool builds **tints** (your colour mixed towards white), **shades** (towards black), **tones** (towards grey), a **neutral ladder** of greys, and a 50–950 or 50–900 **key set** of the kind design systems use.

Two ramp engines are offered. **HSL lightness** spaces the steps evenly in HSL lightness. **Equal luminance** spaces them evenly in relative luminance, the quantity WCAG contrast is built on, with an easing exponent to bunch steps where you want them. Tints, shades, tones and key sets are mixed in the space you choose: CIELAB, OKLab, HSL or linear sRGB.

Every step is measured: OKLab lightness, WCAG 2.2 contrast ratio and APCA-W3 0.1.9 Lc against white, black or your base colour. A Ramps view compares the engines and reports how even each ramp is in three measures. Exports give CSS custom properties, an SCSS map, JSON or CSV, each with a header recording how the ramp was made.

## Who it is for

- Designers building colour scales for a design system or brand.
- Front-end developers who need ramp tokens with known contrast against white and black.
- Accessibility specialists checking which steps meet WCAG AA or AAA, or an APCA Lc level.
- Students comparing HSL, CIELAB and OKLab mixing.

## Where to find it

- Address: https://auricartisan.com/tool/general/gamut-and-rendering/tonal-steps-tints-shades/
- In the tool collection (https://auricartisan.com/collections/) under **Gamut & Rendering**, as **Tonal Steps, Tints & Shades**.

## Quick start

1. Open https://auricartisan.com/tool/general/gamut-and-rendering/tonal-steps-tints-shades/.
2. Type your colour in **Base colour**, for example `#D3AF37`, or use the picker.
3. Choose a **Ramp engine**: **HSL lightness** or **Equal luminance**.
4. Set **Steps** (3 to 21; default 11).
5. Read each step's HEX, OKLab L and contrast against white.
6. Under **Also show**, tick **Tints — toward white** and **Shades — toward black**.
7. Open **Contrast** to see every step's WCAG rating and APCA Lc.
8. Open **Export**, choose **The ramp** as **CSS**, and select the download button.

## What you can do

- Build an HSL-lightness or equal-luminance ramp of 3 to 21 steps, with easing.
- Build tints, shades, tones and a neutral ladder, mixed in CIELAB, OKLab, HSL or linear sRGB.
- Read each step's OKLab L and WCAG ratio, and the base colour's HEX, RGB, HSL, CIELAB, LCh, OKLab L and luminance.
- Compare the engines side by side and measure evenness in OKLab L, CIELAB L* or relative luminance.
- Build 50–950 and 50–900 key sets.
- Check every step's WCAG 2.2 ratio and rating and APCA-W3 Lc against white, black or the base.
- Export CSS, SCSS, JSON, CSV or a link; analyse a list of colours.

## In this folder

- [docs/](docs/README.md) — how to use the tool
  - [Getting started](docs/getting-started.md)
  - [Build a ramp](docs/build-a-ramp.md)
  - [Make tints, shades, tones and key sets](docs/tints-shades-tones.md)
  - [Check contrast](docs/check-contrast.md)
  - [Export tokens](docs/export-tokens.md)
  - [Reference](docs/reference.md)
  - [Troubleshooting](docs/troubleshooting.md)
  - [FAQ](docs/faq.md)
- [others/](others/README.md) — background and supporting pages
  - [Glossary](others/glossary.md)
  - [Shortcuts](others/shortcuts.md)
  - [Limits and accuracy](others/limits-and-accuracy.md)
  - [Related tools](others/related.md)
  - [Release notes](others/release-notes.md)
  - [Privacy](others/privacy.md)
