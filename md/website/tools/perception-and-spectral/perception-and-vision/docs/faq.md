---
title: Perception and Vision — FAQ
description: Short answers to common questions about Perception Vision.
product: Website › Tools › Perception and spectral › Perception and Vision
updated: 2026-09-25
---

# Perception and Vision FAQ

## Can I use this to diagnose colour blindness?

No. It simulates how an image might appear to someone with a condition; it does not test anyone's vision. The settings file and CSV carry `clinical: false` and "not a clinical measurement".

## Which colour vision simulation does it use?

The Viénot, Brettel and Mollon (1999) projection, applied in cone space: sRGB is decoded, converted to CIE XYZ and then to cone signals with the Hunt-Pointer-Estévez matrix, projected, and converted back. The **Simulation** tab shows every matrix.

## Does a severity of 0.5 simulate anomalous trichromacy?

Not as a physiological model. Between 0 and 1 the page blends linearly between normal vision and full dichromacy. The Machado, Oliveira and Fernandes (2009) model would be needed for anomalous trichromacy, and the page does not implement it. The **Mild deuteranomaly** preset uses this blend at 0.40.

## Why does white stay white under protanopia?

Because it should: people with a colour vision deficiency see neutrals as neutral. The grey ramp under the frame checks this for every change.

## What is daltonising?

A recolouring that moves information from a colour axis a dichromat cannot see into one they can. Tick **Daltonise instead of simulate** to preview it. It changes colours for everyone, so it is a preview of a correction filter, not a design fix.

## How accurate are the night-vision, lens, cataract and acuity simulations?

They show that an effect exists and its direction, not its size for any person. Their constants are the tool's own; see [Limits and accuracy](../others/limits-and-accuracy.md).

## Why is there no contrast sensitivity mode?

An earlier "CSF overlay" mode applied a contrast sensitivity curve to the distance from the image centre instead of to spatial frequency, and at its own defaults produced a black frame. It was withdrawn. The **Modes** tab shows what it did and what a real one would need.

## Can I check a whole palette at once?

Yes. Paste the hex colours into the **Export** tab. Rows whose **Simulated** hex values match or nearly match are colours the simulated viewer cannot tell apart. See [Check a palette and export](check-a-palette-and-export.md).

## Does my image get uploaded?

No. The image is read and processed in your browser. See [Privacy](../others/privacy.md).

## Why does the camera option not work?

The site does not currently allow its pages to use the camera. Use a screenshot or photo instead.

## GPU or CPU: which should I use?

Either. The colour calculation is the same, and the page checks the two against each other. The GPU is faster; the CPU is used automatically without WebGL2.
