---
title: Accessibility Library — FAQ
description: Short answers to common questions about the Accessibility Library.
product: Website › Library › Colour libraries › Accessibility Library
updated: 2026-09-25
---

# Accessibility Library FAQ

## What contrast do I need?

Under WCAG 2: 4.5:1 for normal body text (AA), 3:1 for large text (at least 18 point, or 14 point bold) and for user-interface components and graphics, and 7:1 for body text at AAA.

## What is APCA?

The Advanced Perceptual Contrast Algorithm, a newer contrast measure developed for the draft WCAG 3. It gives a lightness contrast value, Lc, from about −108 to 106; the sign shows polarity (negative for light text on dark). Higher absolute values mean more readable text. The page shows it alongside the WCAG 2 ratio.

## Why does the line curve?

Because contrast depends on luminance, and luminance depends on hue as well as lightness: yellows and greens are much brighter than blues and purples at the same OKLCH lightness.

## What is the Vision margin?

How far apart the two colours stay when viewed as someone with each of eight colour vision deficiencies, cataracts or low vision would see them, taking the worst case, on a 0-to-1 scale. A low margin means the pair can merge for some people even if its contrast ratio passes.

## What is the index for?

It is a reproducible set of five million scored pairs. Any record id, such as `acc_91`, always gives the same pair, so you can cite it in an audit.

## Is anything sent to a server?

No. Every figure on the page is computed in your browser. See [Privacy](../others/privacy.md).

## Can I automate this?

Yes, through the site's REST API. The page's **All of this from your own code** section links to the guide and the endpoint reference. See [Public API](../../../../../services/public-api/README.md).

## Do I need an account?

Not to use the page. An API key (from your dashboard) is needed only for the API.
