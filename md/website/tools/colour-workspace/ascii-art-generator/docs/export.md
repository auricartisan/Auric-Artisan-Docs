---
title: ASCII Art Generator — Copy, export and batch
description: Copy the art, download it as TXT, PNG, SVG, HTML, JSON, CSV or ANSI, export several files at once, and render a list of words in one go.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Copy, export and batch

Every file is built in your browser and handed straight to your downloads. Nothing is uploaded.

## Copy

- **Copy** under the art copies the plain characters. The message reads **Copied!**
- **Copy for terminal** in the **ANSI** card copies the art with colour codes, for pasting into a terminal. The message reads **Copied with colour — paste into a terminal**, or just **Copied** if colour is off.

Paste plain text into a place that uses a monospaced font (a code block, a terminal, a text editor), or the columns will not line up.

## Download one format

Open the **Export** tab. Each card has a download button.

| Card | Button | File | What it contains |
| --- | --- | --- | --- |
| **TXT** | **Download .txt** | ascii-art.txt | The characters, one line per row, with filters applied. |
| **PNG** | **Download .png** | ascii-art.png | A picture of the art. |
| **SVG** | **Download .svg** | ascii-art.svg | Vector art with selectable characters. |
| **HTML** | **Download .html** | ascii-art.html | A standalone web page. The only download that keeps colour as coloured text. |
| **JSON** | **Download .json** | ascii-research.json | The characters and every setting that produced them. |
| **CSV** | **Download .csv** | ascii-analysis.csv | How often each character appears. |
| **ANSI** | **Download .ans** | ascii-art.ans | The characters with 24-bit colour codes for terminals. |

A message confirms each download, for example **TXT exported**. If nothing has been converted yet, it reads **Nothing to export**.

### Match the download to the render

The PNG, SVG and HTML downloads are built from a render, so choose the matching **Render** chip on the **Lab** tab first:

| For | Show this render first | Otherwise |
| --- | --- | --- |
| PNG | **Canvas** | The PNG is drawn from the last HTML render if there has been one, or from the text using the output font, **Ink** and **Paper**. |
| SVG | **SVG** | The SVG reuses the last SVG render or SVG download if there has been one, or wraps the last HTML render, or draws the text in black on white. |
| HTML | **HTML** | The page contains the last HTML render if there has been one, or the plain text in black on white. |

Without that step, a PNG, SVG or HTML download can show an earlier version of the art. See [Troubleshooting](troubleshooting.md).

### The HTML file

With an HTML render, the file is a page on a black background holding the coloured characters on your paper colour. It opens in any browser.

### The JSON file

It records the time, the source (image, text or webcam), the render mode, the characters in the ramp, every option, the text of the art, the timings of the last twenty conversions and the glyph densities. It does not include the source picture. The generator cannot load a JSON file back in; keep it as a record of the settings, or use it in your own code.

### The CSV file

Three columns, **Character**, **Count** and **Frequency** (per cent), sorted from the most common character down. Line breaks are not counted. The card on the page also mentions density per glyph, but the file holds frequencies only; the densities are in the JSON file.

### The ANSI file

A text file whose colour runs are 24-bit terminal colour codes, with a reset at the end of every line. Print it in a terminal that supports true colour (for example with `cat ascii-art.ans` on macOS or Linux) and the picture appears in colour.

It needs **From image** colour. With **Mono**, **Download .ans** shows **Turn colour on first — ANSI carries the image's colours** and saves nothing. After a successful download the message reads **Saved ascii-art.ans — cat it in a terminal**.

## Export several files at once

**Export all six**, in the left column of **Export**, downloads five files one after another: the TXT, PNG, SVG, JSON and CSV files. It does not include the HTML or ANSI files; download those from their cards. Your browser may ask whether to allow several downloads from the page.

## Batch: render a list of words

The **Batch** box takes one line of text per row, for example:

```
AURIC
ARTISAN
ASCII
```

**Render each line** converts each line as **Text** source, with the current text font and conversion settings, and fills **Batch results** with a table of **Input** (the first 30 characters), **Cols**, **Rows**, **Chars** and **Time (ms)**. With nothing in the box it reads **No inputs**.

Batch measures; it does not produce files or change the art on the stage. It does leave the last line of the list in the **Text** box on the **Lab** tab.

## Save to your Library

On this page, the Library's **Save to Library** stores the current art and your settings in your Auric Artisan Library, and opening the item later puts them back. See the [Library Kit](../../../../kits/library-kit/README.md).

## Related

- [Render modes and full screen](render-modes.md)
- [Troubleshooting](troubleshooting.md)
- [Privacy](../others/privacy.md)
