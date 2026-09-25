---
title: Color Library — FAQ
description: Short answers to common questions about the Color Library.
product: Website › Library › Colour libraries › Color Library
updated: 2026-09-25
---

# Color Library FAQ

## How many colours are in the atlas?

8,192. The number never changes as you filter; the counters show how many of the 8,192 match.

## Does it cover every colour?

No. The atlas is a fixed, generated set of 8,192 colours spread across the sRGB range. Your exact colour may not be in it, which is why **Start from a colour you already have** finds the nearest ones.

## Which contrast formula does it use?

The WCAG 2 contrast ratio, from 1:1 to 21:1, measured against pure white (`#FFFFFF`) and pure black (`#000000`). 4.5:1 is the AA threshold for normal body text and 7:1 is AAA.

## What is ΔE?

A number for how different two colours look. The Color Library uses CIE76, the straight-line distance between two colours in CIE Lab. Under about 2.3, most people cannot see a difference.

## Can I test a colour against a background other than white or black?

Not in the Color Library. Use the Contrast Checker or the Accessibility Library for any pair of colours. See [Related](../others/related.md).

## Are the emotion, mood and art-movement labels scientific?

No. They are descriptive labels assigned when the atlas was generated, useful for browsing by feel. The contrast, luminance and chroma figures are measurements.

## Do I need an account?

No. Everything works signed out. Saved colours stay in your browser.

## Can I use the colours commercially?

Colour values themselves are not ownable. For the terms that apply to the site and its content, see [Company and legal](../../../../company-and-legal/README.md).

## Is there an API?

Yes. The heading links to the site's API reference, and the **Automate this** note names the API call that does the same job. See [Public API](../../../../../services/public-api/README.md).

## Does it work offline?

It needs a connection to load the atlas. Once loaded, filtering, sorting and exporting happen in your browser. Opening a colour's full record may fetch a little more data.
