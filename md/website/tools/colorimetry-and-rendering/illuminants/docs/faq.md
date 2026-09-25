---
title: Illuminants — FAQ
description: Short answers to common questions about the Standard Illuminants lab.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Illuminants FAQ

## Why does CIE A show 2856 K when the standard defines it at 2848 K?

Illuminant A is defined as a Planckian radiator at 2848 K using the 1931 value of the second radiation constant. Measured on a modern (ITS-90) Planckian locus, its CCT is 2856 K. The lab computes A the way it is defined and reports the CCT you would measure, which is why the list says 2856 K. The Data tab explains this under Illuminant A.

## Are the D65 and D50 spectra the published CIE tables?

They are reconstructed from the published CIE daylight basis functions (S0, S1, S2), which the lab holds verbatim. The reconstructions land on their published chromaticities to better than 0.0003, which is why they are marked "computed" rather than "verbatim".

## Why are the fluorescent illuminants marked as stand-ins?

The lab does not hold the CIE 15 table of fluorescent spectra. F1 to F12 are built from smooth peaks as illustrations, so their chromaticity, CCT and rendering figures describe the stand-in, not the real CIE illuminant. They are flagged wherever they appear.

## Is the CRI value a real CIE 13.3 result?

No. The 14 test colour samples are approximations, so Ra and R1–R14 are indicative only. The Methods tab shows the CIE 13.3 card as switched off for that reason.

## Why is there no TM-30 figure?

TM-30 is defined on 99 colour evaluation samples that the lab does not hold. Rather than invent a figure, the lab leaves TM-30 switched off. The Reference tab still explains what TM-30 measures.

## What is the difference between the Ohno and McCamy CCT?

McCamy's (1992) formula is a quick cubic fit that returns a number for any input, even where CCT is meaningless. Ohno's method (2014) searches a finely computed Planckian locus, returns a signed Duv, and says when the result is not valid. The lab uses Ohno for every reading and shows McCamy only on the Methods tab for comparison.

## What does a negative Duv mean?

The light sits below the Planckian locus in the uv plane, which looks slightly pink or magenta. Positive Duv is above the locus, slightly green.

## Can I use the 10° observer?

Not yet. The CIE 1964 10° colour matching functions are not held, so the option is switched off rather than silently returning 2° results.

## Can I load my own measured spectrum?

The page has no control for importing a spectrum. You can choose any standard illuminant or a blackbody at any CCT from 1,500 to 25,000 K.

## Does it work offline?

Once the page has loaded, all calculations run in your browser without a network connection. Loading the page needs one.

## Can I save my settings?

Yes. Use **Export › Share URL** for a link, or the floating **Save to Library** button to keep a preset in your Library.
