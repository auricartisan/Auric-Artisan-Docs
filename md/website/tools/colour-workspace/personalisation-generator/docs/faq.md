---
title: Personalization Generator — FAQ
description: Short answers to common questions about the Personalization Generator.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Frequently asked questions

## Do I need an account?

No. The generator runs in your browser without signing in. Saving to your Library uses your Auric Artisan Library.

## Is the brief read by an AI?

No. The brief is split into words, and each word is compared with the names of built-in reference palettes. A match makes that reference palette more likely to be drawn on. Your pool, style chips and use case steer the sweep far more. See [Tune the sweep](tune-the-sweep.md).

## Where do the generated colours come from?

From your pool, from built-in reference palettes that match your styles, use case and brief, and from small variations of both, arranged on a colour relationship such as Analogous or Triadic. Every candidate is then scored and only the best are kept.

## Will I get the same results if I run the same settings again?

Usually not. Each sweep starts from a different random seed, so results vary from run to run. Save or download the results you like.

## Are my results saved?

Your pool and settings are remembered in your browser. The results are not: each visit starts with a fresh quick sweep. See [Export, save and share](export-and-save.md).

## Can I load a JSON snapshot back in?

No. The JSON is a record of your settings and results for your own use. To carry a palette back in, save it to your Library and open it in the generator, or add its HEX values to the pool.

## What does the score mean?

It is how well a palette fits your settings: closeness to your pool, harmony, fit with your styles, variety, contrast and colour-vision safety, weighted by your sliders. A score of 85 under one set of settings is not comparable with 85 under another. See [Palettes, gradients, typography, UI pairs and posters](result-tabs.md).

## Is a high-scoring palette guaranteed to pass WCAG?

No. Contrast is part of the score, not a requirement. Check the contrast bars on each palette card, **The leader, checked**, the **UI Pairs** grades and the **Tokens** audit, and test your final colour pairs in your own designs.

## Are the design tokens ready to use in code?

They are ordinary CSS custom properties and JSON, and you can paste them into a project. Review them first: the roles are chosen automatically, and the status colours (success, warning, danger, info) are made up when the palette has no suitable colour.

## Can I use my own fonts in the Typography tab or the Studio?

No. The type systems are fixed. The page shows them with the fonts installed on your device.

## Can I export the posters or mockups as images?

No. You can copy their CSS and save their settings to your Library.

## Can I automate the generator?

Yes. The Public API offers the same generation as **POST /v1/personalize/system**, at 14 API credits per call. See the [Public API](../../../../../services/public-api/README.md).

## Does it work on a phone?

Yes. The columns stack on narrow screens. Large sweeps take longer on slower devices; lower **Search depth** if it feels slow.

## Related

- [Troubleshooting](troubleshooting.md)
- [Getting started](getting-started.md)
