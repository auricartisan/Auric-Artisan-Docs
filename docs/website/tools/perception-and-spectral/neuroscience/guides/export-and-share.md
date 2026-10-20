---
title: Neuroscience (Visual Pathway) — Export and share
description: Run a list of colours through the Visual Pathway's front end, download it as CSV or copy it, save the active map as PNG, download the settings and copy a link to the view.
product: Website › Tools › Perception and spectral › Neuroscience
updated: 2026-09-25
---

# Export and share

Nothing leaves the page until you press one of the buttons described here. Downloads are saved by your browser; copies go to your clipboard.

## Run a list of colours

1. Open the **Export** tab.
2. In **Colours**, enter hex colours, one per line. Commas and semicolons also separate entries. Three-digit (`#F80`) and six-digit (`#FF8800`) forms work, with or without `#`. Anything else is ignored.
3. The table updates as you type; **Run them** redraws it.

The default list is `#E03131`, `#2F9E44`, `#1971C2`, `#F59F00` and `#808080`.

The table has one row per colour: **Input** (a swatch and the hex), **L**, **M**, **S**, **L − M**, **S − (L+M)/2** and **L + M**, each to four decimals. The header note gives the number of rows. The current **Colour vision** setting on the Lab tab is applied first, at full strength, so you can see what a dichromat's cone signals would be.

Read the grey row first. Because the cone matrix gives equal L, M and S for the D65 white, a neutral has both chromatic values at zero, and the page highlights them. If a grey row shows non-zero chromatic values, a colour vision simulation is on.

## Download or copy the table

- **Download the CSV** saves `cones-opponent.csv`. It starts with comment lines, then one row per colour:

  ```text
  # visual-pathway — cone signals and opponent channels
  # chain: sRGB → linear → XYZ → LMS → opponent
  # cone table: this tool's own (L peak 590 nm, M peak 590 nm)
  # opponent axes: L-M, S-(L+M)/2, L+M — not DKL
  # geometry: 57 cm, 0.248 mm pixel pitch
  # reportable against a published table: false
  # educational approximation, not a physiological measurement
  Input,L,M,S,RG,BY,Lum
  ```

  `RG` is L − M, `BY` is S − (L+M)/2 and `Lum` is L + M. Values have six decimals.
- **Copy to clipboard** copies the same table as tab-separated text with a header row (`Input`, `L`, `M`, `S`, `RG`, `BY`, `Lum`) and four decimals, ready to paste into a spreadsheet. A message confirms **Copied**, or says **Copy blocked** if the browser refused.

If the list is empty, the page says **No colours to write** or **No colours to copy**.

## Save the active map

**Save the map** (on the Lab tab, under the readouts) saves the right-hand canvas as a 256 × 256 PNG named after the map, for example `visual-pathway-retina-on.png` or `visual-pathway-v1-orient.png`. The scale bar is not part of the image, so note its range if you need it.

## Download the settings

**Download the settings** saves `visual-pathway-settings.json`. The Export tab shows its current content under **The settings file, and what it carries**. It records:

| Field | Meaning |
|---|---|
| `tool` | `visual-pathway` |
| `stimulus` | `grating` or `testcard` |
| `spatial_frequency_cpd`, `viewing_distance_cm`, `pixel_pitch_mm`, `degrees_per_pixel` | The stimulus frequency and the geometry |
| `chain` | The colour chain used |
| `cone_table`, `cone_peaks_nm` | Whose cone curves drew the figure, and where L, M and S peak in them |
| `opponent_axes` | The three axes, marked "not DKL" |
| `stages` | The stages that ran for the current frame |
| `colour_vision` | `none`, `protan`, `deutan` or `tritan` |
| `reportable` | `true` only after you install a cone table |
| `clinical` | Always `false` |

## Copy a link to the view

**Copy a link to this view** copies an address that reopens the tool with the same stimulus, geometry, stage settings, colour vision setting, colourmap and map on screen. The message **Link copied** confirms it. The link carries these parameters: `source`, `baseHex`, `carrier`, `cpd`, `contrast`, `distanceCm`, `pitchMm`, `nOrient`, `rfSize`, `gaborCpd`, `gaborSigma`, `dogCenter`, `dogSurround`, `dogWeight`, `v4Preset`, `cvdType`, `colormap` and `viewMap`. It does not carry the pupil size, the stage checkboxes, the scale-bar setting, an installed cone table or your colour list.

## The What to take buttons

The **What to take** buttons at the top of the Export rail are shortcuts: **A list of colours** keeps you on the list, **The active map** saves the map, **The settings** downloads the JSON and **A link to this view** copies the link.

You should now have your colours' cone and opponent values in a file, with the chain and the cone table named in its header.
