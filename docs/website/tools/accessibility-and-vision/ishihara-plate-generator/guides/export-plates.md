---
title: Ishihara Plate Generator — Export plates
description: Download plates as PNG or SVG, export every plate as a ZIP, save a seeds file, and rebuild a plate from its seed.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# Export plates

Every file is built in your browser and handed straight to the download. Nothing leaves your device.

## One plate, from its card

| Button | What you get | File name |
| --- | --- | --- |
| **Download PNG** | A raster image, 4,096 pixels square, on the chosen card material | `ishihara-plate-<number>-<content>.png` |
| **Download SVG** | A vector image with one circle per dot, which scales to any print size | `ishihara-plate-<number>-<content>.svg` |
| **Copy seed** | The plate's seed, on your clipboard | — |

The page says "Rendering high-res PNG…" while it builds the PNG. For example, plate 1 showing 93 downloads as `ishihara-plate-1-93.png`.

## Every plate, from the Export tab

The **Export** tab has four actions. They cover every plate currently in the Lab.

| Action | What you get |
| --- | --- |
| **Everything at once** › **Export every plate** | One ZIP, `ishihara-plates.zip`, with a PNG (2,048 pixels), an SVG and a JSON description for each plate |
| **PNG** (Raster) › **Download every .png** | The same ZIP of every plate |
| **SVG** (Vector) › **Download every .svg** | One SVG file per plate, downloaded one after another |
| **Seeds** (Reproducible) › **Download the seeds** | A text file, `ishihara-seeds.txt`, with the seed, palette and settings of every plate |

**↓ Export All** in the Lab does the same as **Export every plate**.

Inside the ZIP, files are named by plate number, type and content, for example `plate-001-number-93.png`, `plate-001-number-93.svg` and `plate-001-number-93.json`. The JSON records the plate's ID, seed, type, content, palette, difficulty, plate shape, dot count, fine-tuning settings and its quality report.

The seeds file is a table with the columns content, seed, type, palette, difficulty, dots and quality, one row per plate.

> **Note:** Your browser may ask permission before it saves several files in a row, as **Download every .svg** does. Allow it for auricartisan.com.

## Reproduce a plate

"A seed rebuilds a plate exactly. Keep it with the file and the same settings will produce the same dots on any machine."

1. Copy the plate's seed with **Copy seed**, or read it from the seeds file.
2. Select **Custom** in the Lab.
3. Choose the same type, content, palette and difficulty, and use the same fine-tuning settings.
4. Paste the seed into **Seed (optional)** and select **Generate**.

The result: the same plate, dot for dot.

## Over the REST API

The Export tab ends with "Or ask for one over HTTP": "Three API credits a call. A separate balance from the tool's tokens." It shows an example request to `POST /v1/ishihara/plate` with a type, content, palette, difficulty and seed. See the public API documentation at https://auricartisan.com/library/documentation/api/.

## Messages

| Message | Meaning |
| --- | --- |
| "PNG downloaded" / "SVG downloaded" | The file was saved |
| "Loading ZIP library…" | The ZIP builder is loading, the first time you export |
| "Exporting all plates…" then "N plates exported as ZIP" | The ZIP is ready |
| "No plates to export" | The bench is empty |
| "ZIP library unavailable — downloading first plate as PNG" | The ZIP builder could not load, so only the first plate was saved |
