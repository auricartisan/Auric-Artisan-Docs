---
title: ASCII Art Generator — Overview
description: What the ASCII Art Generator is, who it is for, where to find it, and how to turn a picture or a word into character art and take it away as text, image or code.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# ASCII Art Generator

The ASCII Art Generator turns a picture into character art: rows of letters, symbols, blocks or Braille dots whose density follows the light and dark of the image. You drop in a photo, a screenshot or a logo, or type a word, and the art appears straight away and updates as you change anything.

Five ready-made looks cover most needs. Behind **Fine tuning** sit the controls that decide how the picture is read: seven character sets or your own ramp, the cell shape, brightness model, gamma and contrast, three sampling methods, Floyd–Steinberg and Bayer dithering, edge-aware glyph choice, the output font, filters such as flip, rotate and frame, and a seed. The art can be shown as plain text, colour HTML, a canvas image or SVG.

Everything happens in your browser. Pictures are read and converted on your device and are not uploaded. You can copy the art, or download it as TXT, PNG, SVG, HTML, JSON, CSV or a colour ANSI file for terminals. An **Analysis** tab and a **Compare** tab measure the character sets and the render for anyone who wants to know why the art looks the way it does.

## Who it is for

- Developers who want a banner for a README, a terminal or a commit message.
- Designers and artists making text-based artwork or retro graphics.
- Teachers and students exploring how images are sampled and dithered.
- Anyone who wants a picture of themselves, a pet or a logo in characters.

## Where to find it

- Page: https://auricartisan.com/tool/ascii/ (the short address https://auricartisan.com/ascii also opens it).
- No sign-in is needed.
- The masthead links to the **Developer reference**, the technical write-up of the engine.

## Quick start

1. Open https://auricartisan.com/tool/ascii/.
2. Select **Choose a file** and pick a photo, or drop one onto the tool, or paste a screenshot with `Ctrl` + `V` (`Cmd` + `V` on a Mac). No picture to hand? Select **Try an example**.
3. Under **Look**, try **Classic**, **Blocks**, **Fine**, **Bold** and **Line art**.
4. Move the **Detail** slider to set how many characters wide the art is.
5. Under **Colour**, choose **From image** to colour each character from the picture.
6. Select **Copy** under the art, or open the **Export** tab and download the format you need.

## What you can do

- Convert an image (PNG, JPEG, GIF, WebP, BMP, SVG or TIFF, up to 20 MB) or a line of text. The page also has a webcam source, but the camera cannot currently be used on this site; see [Choose a source](docs/sources.md).
- Pick a look, or fine-tune character set, shape, tone, sampling, dithering, edges, type and filters.
- Show the result as text, colour HTML, a canvas image or SVG, and view it full screen.
- Measure the character sets, the edge field, character frequencies and render times.
- Render a list of words in one go and time each one.
- Export as TXT, PNG, SVG, HTML, JSON, CSV and ANSI.

## In this folder

- [docs/](docs/README.md) — how to use the generator.
  - [Getting started](docs/getting-started.md)
  - [Choose a source](docs/sources.md)
  - [Looks, colour and detail](docs/looks-colour-and-detail.md)
  - [Fine tuning](docs/fine-tuning.md)
  - [Render modes and full screen](docs/render-modes.md)
  - [Charts, benchmark and Compare](docs/charts-and-compare.md)
  - [Copy, export and batch](docs/export.md)
  - [Reference](docs/reference.md)
  - [Troubleshooting](docs/troubleshooting.md)
  - [FAQ](docs/faq.md)
- [others/](others/README.md) — supporting material.
  - [Glossary](others/glossary.md)
  - [Shortcuts](others/shortcuts.md)
  - [Limits and accuracy](others/limits-and-accuracy.md)
  - [Related](others/related.md)
  - [Privacy](others/privacy.md)
