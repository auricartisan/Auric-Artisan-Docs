---
title: Image Picker — FAQ
description: Short answers to common questions about the Image Picker.
product: Website › Tools › Image and file tools › Image Picker
updated: 2026-09-25
---

# Image Picker FAQ

## Is my picture uploaded?

No. A picture you load from a file is read in the page and never leaves the tab. When you use **Load URL**, your browser fetches the image from that address, as it would for any web page. See [Privacy](../others/privacy.md).

## Why do I get different colours each time I extract?

The k-means++ method starts from randomly chosen colours, so two runs on the same picture can settle on slightly different averages. Flat artwork with few colours is not affected, because its exact colours are used.

## Why is a colour I can see not in the palette?

The palette holds the colours that cover the most of the picture. A small detail may not make up enough pixels to become a cluster. Raise **Clusters** or **Quality**, or pin the colour with the eyedropper.

## Are the swatches real pixel colours?

For flat artwork with no more distinct colours than the cluster count, yes. For photographs, each swatch is the average of a cluster of similar pixels, and may not match any single pixel exactly. Pins are always exact pixels of the working copy.

## How many colours can I extract?

The slider goes from 2 to 12. When the page first opens it uses 16 until you move the slider.

## Does the contrast check mean the pairs are accessible?

It gives the WCAG 2 contrast ratio and rating for the strongest eight pairs, as a first pass. Test the exact text and background pair you plan to use, at its real size, in a dedicated contrast tool.

## What colour space are the Lab and LCH values in?

CIELAB and its LCH form, calculated from sRGB with a D65 white.

## Can I compare palettes from two pictures?

The **History** count keeps track of how many extractions you have run, but the page does not show a side-by-side comparison. Export the JSON of each picture and compare the files.

## Can I share my palette with a link?

**Copy page link** copies the page address only. Share the CSS, JSON or SVG instead.

## Is there an API for this?

Yes. The line under the page heading gives the REST endpoint, `POST /v1/palette/from-image`, and its cost in API credits, with a link to its documentation. API credits are separate from tool tokens. See [Public API](../../../../../services/public-api/README.md).
