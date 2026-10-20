---
title: Chromatic Adaptation — FAQ
description: Short answers to common questions about the Chromatic Adaptation lab.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Chromatic Adaptation FAQ

## Which transform should I use?

For ICC colour management and D65 ↔ D50 conversions, Bradford is the common convention. CAT16 is the transform of the most recent CIE-lineage appearance model (CAM16). The lab does not rank them for accuracy, because that needs corresponding-colour data sets it does not hold; it shows what each one does on your pair.

## Why do Von Kries and HPE give the same result?

The lab's Von Kries matrix is the Hunt–Pointer–Estévez matrix normalised to D65. Normalising scales each row, and that scaling cancels out in M⁻¹ · diag(d) · M, so the two produce identical adaptations.

## What is XYZ scaling for?

It is the simplest possible adaptation, scaling X, Y and Z directly. It is not a model of the eye and is kept as a baseline to compare the others against.

## What does "degree of adaptation" mean?

How complete the adaptation is. At D = 1 the source white maps exactly onto the destination white. Real viewers often adapt incompletely, especially in dim or complex scenes, so values below 1 are realistic in some situations.

## How long does adaptation really take?

The lab uses Fairchild and Reniff's (1995) measurements: about half the adaptation within a second or so, and the rest with a half-life of about 30 seconds. With the default settings, 90% adaptation takes about 70 seconds. The Dynamics tab computes the exact times.

## Why does the time-course prose in Reference quote different time constants?

Some background text in the Reference section predates the current model. The time course the lab actually uses is the one on the Dynamics tab.

## Is my image uploaded?

No. The image is read and processed in your browser, and the exported PNG is created there too.

## Can I adapt a video?

No. The lab adapts one still image (or the sample sweep) at a time.

## Can I get the full adaptation matrix as numbers?

Yes. The Matrix tab shows it at the D you set, and **Export JSON** includes it for the current moment of the timeline. The **Copy as** buttons copy the transform's cone matrix M.

## Does the lab model colour appearance (CIECAM02 or CAM16)?

No. It applies the chromatic adaptation step only. The Reference notes explain how CIECAM02 would compute D from the adapting luminance and surround.
