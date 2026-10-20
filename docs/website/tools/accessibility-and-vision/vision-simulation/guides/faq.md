---
title: Vision Lab — FAQ
description: Short answers to common questions about the Vision Lab.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# Vision Lab FAQ

## Is it free?

Yes. Every simulation is free on every plan. The free plan counts up to 25 simulations a day opened from the Catalogue; paid plans lift that cap. The Workbench, Compare, Palette audit and Analytics are free to use.

## Is it a medical tool?

No. The page says: "Educational visualisation only. Not a medical simulation, a diagnostic tool, or a substitute for professional eye care — and screen colours are not calibrated." It cannot diagnose or test anyone's vision.

## Which models does it use?

For the colour-vision conditions, the published models of Brettel (1997), Viénot (1999) and Machado (2009), calculated in linear light. You can switch between them in the Workbench and in each panel.

## What is the difference between per-colour and field conditions?

A per-colour condition changes each colour in a predictable way, so every colour has an exact answer. A field condition changes how and where you see, such as blur, dark patches or a lost half of the visual field; colour may survive while the field does not.

## What does the severity score mean?

It is an estimated visual-impact score from 1 to 10. It orders the collection; it is not a clinical grade and does not rank anyone's sight.

## What does the severity slider do?

It sets how strongly the model is applied, from 0 (normal vision) to 100% (full expression). As the page puts it, severity is a dial on the model, not a milder diagnosis.

## How do I check a whole palette?

Use **Palette audit**. It checks every pair of up to 24 colours under all 17 colour conditions and suggests lightness fixes for pairs that merge. See [Audit a palette](audit-a-palette.md).

## Are my images uploaded?

No. The page says: "Whatever you drop stays on your machine — the pipeline runs in this tab and nothing is uploaded."

## Can I share what I am looking at?

Yes: **Copy link to this view** (Workbench), **Copy link** (Catalogue) or **Copy link to this sheet** (Compare). See [Links, saving and exports](links-saving-and-exports.md).

## How is this different from the Analyzer's Simulation section?

The [Analyzer](../../analyzer/README.md) previews a whole web page under six filters. The Vision Lab goes much deeper: 78 conditions, severities, models, measurements, a palette audit and image input.

## Can I automate it?

The palette audit is available from the REST API as `POST /v1/vision/audit`, at 5 API credits per call. See the public API documentation at https://auricartisan.com/library/documentation/api/.
