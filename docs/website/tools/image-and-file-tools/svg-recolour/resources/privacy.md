---
title: SVG Recolour — Privacy
description: What SVG Recolour does with your SVG files, and how it handles active content.
product: Website › Tools › Image and file tools › SVG Recolour
updated: 2026-09-25
---

# Privacy

## Your file stays in your browser

- An SVG you drop, choose or paste is read and parsed by the page itself, in your browser. It is not uploaded.
- Finding colours, rewriting them, the checks and the previews all happen on your device.
- Exported files are created in the browser and saved by your browser's normal download.
- The clipboard is written only when you select a copy button.

## Active content

An SVG is a document, not just a picture, and can contain scripts, event handlers and `javascript:` links. Because this tool is often used on files other people send, the previews on the page are drawn from a copy with that content removed, and a notice lists what was removed. The file's scripts are not run by the page.

The exported file is rewritten from your original, so it still contains any active content the original had. If you do not trust the file, remove that content in an editor before using the export elsewhere.

## Nothing is kept after you leave

The tool does not store your file, your mappings or your settings. Loading another file, reloading or leaving the page clears them.

## What the report contains

The report contains counts of elements and colours, every colour mapping and the values left alone. It does not contain the SVG markup.

## The page itself

SVG Recolour is a normal page on auricartisan.com. Site-wide features such as sign-in, preferences and any consent-based services follow the site's own privacy policy and your cookie choices; see [Help](../../../../../help/README.md).
