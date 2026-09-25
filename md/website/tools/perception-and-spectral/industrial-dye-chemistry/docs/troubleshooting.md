---
title: Industrial Dye Chemistry (Dye in Solution) — Troubleshooting
description: Symptoms, causes and fixes for Dye in Solution: flags, refused spectra, component limits, the plot and links.
product: Website › Tools › Perception and spectral › Industrial Dye Chemistry
updated: 2026-09-25
---

# Troubleshooting Dye in Solution

## "Beer–Lambert holds" reads "no"

**Why:** the bath's absorbance is above 1 at some wavelength. Past that point real solutions depart from the law and spectrophotometers become unreliable, so the computed colour is less trustworthy.

**What to do:** lower **Concentration** or **Path length**. For the default dye at pH 3.5, the limit is reached at about 54 µM in a 1 cm path.

## Moving pH changes almost nothing

**Why:** the selected dye is one of the pH-stable presets (azo red, anthraquinone blue, yellow), whose two forms have nearly the same band, or the pH is far from the dye's pKa, where almost all of it is already in one form.

**What to do:** use an indicator preset, or move the pH to within about two units of the pKa (watch **Base fraction**).

## "Isosbestic point" is highlighted or reads "(weak)" or "none in range"

**Why:** **(weak)** means the two forms cross so deep in their tails (below 5% of the peak) that the point cannot be seen on the plot. **none in range** means they do not cross between 380 and 780 nm.

**What to do:** nothing is wrong; it describes the dye. The mid-range and high-range indicators have weak crossings.

## The plot does not change when I change concentration or path length

**Why:** the plot shows the selected dye's molar absorptivity (a property of the dye), not the bath's absorbance.

**What to do:** read **Peak absorbance** and **λmax** for the bath, or export the spectrum CSV, whose `absorbance` column is the whole bath.

## The plot shows a different dye from the one I am editing

**Why:** the plot follows the selected dye. Adding a dye selects the new one.

**What to do:** select the dye's button in **The components** list.

## A file chooser opens when I click the spectrum

**Why:** the plot is also a drop zone for measured spectra; clicking it opens the file chooser.

**What to do:** cancel the chooser if you did not mean to load a file.

## My spectrum file is refused

| Message | Fix |
|---|---|
| **No two-column numeric rows in that file** | Make sure each data line has two numbers: wavelength and molar absorptivity |
| **Not installed: fewer than eight rows** | Supply at least eight rows |
| **Not installed: covers X to Y nm; at least 420 to 680 is needed …** | Extend the scan to cover 420–680 nm |

The loader expects molar absorptivity. A file of raw absorbance loads but gives the wrong strength; convert it first (see [Use a measured spectrum](use-a-measured-spectrum.md)).

## I cannot add a fifth dye or remove the last one

**Why:** a bath holds one to four components.

**What to do:** remove or mute a dye first; to empty the bath, use **Reset the bath** and build again.

## "Inside sRGB" reads "no"

**Why:** the bath's colour under this light is more saturated, or lighter, than sRGB can show. The swatch is the nearest colour a screen can display. Pale, strongly tinted baths such as the default often fall just outside.

**What to do:** nothing; the L\*a\*b\* values are still exact for the model.

## Dominant wavelength starts with "c" and purity reads "—"

**Why:** the colour is a purple, for which no single spectral wavelength exists; the page gives the complementary wavelength instead.

**What to do:** nothing; the note under the readouts explains it.

## The sweep result looks out of date

**Why:** the sweep is not rerun when you change the bath.

**What to do:** select **Run the sweep** again on the **Method** tab before exporting.

## A link did not restore a muted dye or my measured spectrum

**Why:** links carry pH, path length, the light and each dye's preset, pKa and concentration only.

**What to do:** mute the dye and load the spectrum again after opening the link.

## I need F11, a fastness result or hazard information

**Why:** the page does not hold fluorescent illuminant tables, cannot perform physical fastness tests, and holds no toxicological data.

**What to do:** see [Limits and accuracy](../others/limits-and-accuracy.md). For hazards, read the supplier's safety data sheet.
