---
title: Ishihara Plate Generator — Limits and accuracy
description: What the Ishihara Plate Generator's scores measure, how far to trust them, and why the plates are not a colour-vision test.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# Limits and accuracy

## Not a colour-vision test

The page is explicit: "Not a colour-vision test. These plates are illustrative. A screen is not colour-calibrated and a real Ishihara examination is printed, lit and administered under controlled conditions. For diagnosis, see an eye-care professional."

In particular:

- **Screens differ.** Colour, brightness, gamut and night modes change what a plate looks like. The same file looks different on two screens.
- **Printing differs.** Paper, ink and light change colours again. A printed plate from this tool is not a calibrated plate.
- **Examinations are controlled.** A real test controls lighting, viewing distance and timing, and uses validated plates. These plates are not validated against people with colour-vision deficiencies.

## What the scores measure

- Colour distances are calculated in **OKLab** between the average figure colour and the average background colour.
- Deficiencies are simulated with the **Brettel, Viénot and Mollon (1997)** model for protanopia, deuteranopia and tritanopia. A simulation models a typical, complete (dichromatic) deficiency; milder forms and individual differences are not modelled.
- The quality score weighs four components (density .24, figure ratio .20, separation .32, concealment .24). It describes how well a plate is built, not whether it would detect a deficiency in a real person.
- A plate passes when density, figure share and separation are in range and the score is at least 45.

## Previews

The **CVD Preview** and the per-plate **Protan**, **Deutan** and **Tritan** switches show the same simulation. They are an illustration of how a plate might look, not what any particular person sees.

## Reproducibility

A seed reproduces a plate exactly only with the same type, content, palette, difficulty and fine-tuning settings. The export ZIP includes a JSON description of every plate for this reason.

## Nothing is kept

Plates exist only while the page is open. Export or keep seeds for anything you need later.
