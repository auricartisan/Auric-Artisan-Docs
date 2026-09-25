---
title: Psychophysical Experiment Engine — FAQ
description: Short answers to common questions about the Psychophysics Bench.
product: Website › Tools › Perception and spectral › Psychophysical Experiment Engine
updated: 2026-09-25
---

# Psychophysics Bench FAQ

## Is this a vision test?

No. It measures a contrast threshold on your screen under your conditions, as a teaching and exploration instrument. It is not calibrated, not clinical and not a diagnosis.

## Which staircase should I use?

**1-up / 2-down — 70.7%** for most purposes: it is the standard transformed up-down rule and converges at a stated percentage. **3-down / 1-up — 79.4%** converges higher and takes longer. The other three are the tool's own or not adaptive.

## Why does the threshold come with a percentage?

Because the probability of a correct answer rises gradually with contrast. A threshold is the contrast at a chosen point on that curve, so it means nothing without the point.

## Is the Bayesian tracker QUEST?

No. It works on a log scale with a stated prior, like QUEST, but its slope, lapse rate and prior width are the tool's choices rather than estimated or taken from previous measurements, so it carries its own name.

## Is the accelerated staircase PEST?

No. PEST is a sequential procedure driven by a statistical test; the accelerated staircase simply halves its step at reversals and doubles it after three moves in one direction.

## Does it fit a psychometric function, compute d′ or give a confidence interval?

Not on screen in the current version. The Data register describes a logistic fit with guess and lapse rates, d′ and criterion for yes/no sessions, and a trial bootstrap, but no readout shows them. Export the session (when the Export tab opens) and fit the data in your own software.

## Why is my threshold different every run?

Staircase estimates vary from run to run; attention, fatigue, lighting and viewing distance add more. Average several runs under the same conditions.

## Can I use a different number of alternatives, same/different or odd-one-out?

No. Those tasks were withdrawn because they could not score trials correctly. The Paradigms tab says what each would need.

## Why does the page ask for my viewing distance and pixel pitch?

Spatial frequency in cycles per degree and an envelope size in degrees depend on both. Without them the frequency would change with every screen and seat.

## Does it measure my screen's gamma?

No. It assumes the sRGB standard curve, and every export says so. The **Drop a measured gamma table** area on the Data tab is not active in the current version.

## Why can I not download my results?

At the time of writing the **Export** tab does not open. See [Export your data](export-your-data.md) for workarounds.

## Is anything I do sent anywhere?

No. Trials are run and stored in the page until you leave or start another run. See [Privacy](../others/privacy.md).
