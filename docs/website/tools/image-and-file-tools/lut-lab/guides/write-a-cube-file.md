---
title: LUT Lab — Write a .cube file
description: Export the transform in force as a 3D or 1D .cube at any size, understand the header and round-trip accuracy, and save the hue sweep, report and share link.
product: Website › Tools › Image and file tools › LUT Lab
updated: 2026-09-25
---

# Write a .cube file

The **Export** tab writes the transform currently shown on the **Lab** tab: a look at its strength and exposure, or a loaded `.cube` file.

## Save a .cube

1. On the **Lab** tab, set up the transform you want: choose a look and its **Strength**, or load a `.cube`.
2. Open the **Export** tab.
3. Choose **Kind**: **3D cube** (default) or **1D curve**.
4. Set **Size** from 2 to 65 (default 33). The label shows, for example, **33³** for a 3D cube.
5. Check the lines under the slider: **rows**, **file size** and **file name**, and the note on whether the grid lands on 8-bit values.
6. Select **Save the .cube**. Your browser downloads the file, for example `auric-teal-and-orange-33.cube`, and a message confirms it.

To paste the table somewhere instead, select **Copy it**. The message reads **Copied the .cube**, or **The clipboard refused** if clipboard access is blocked.

The file name is `auric-`, the transform's name in lower case with spaces and symbols turned into hyphens, the size, and `-1d` for a 1D curve.

## 3D cube or 1D curve

| Kind | What it captures | Rows |
|---|---|---|
| **3D cube** | The full transform: every mix of red, green and blue | Size³ |
| **1D curve** | Only what the transform does to neutral greys, written as a curve per channel | Size |

A 1D curve is made by sending greys through the transform and recording each output channel. Any effect that depends on how channels mix, such as a hue shift or a change in saturation, is lost. **Mono contrast**, for example, cannot be expressed as a 1D curve: the curve would leave colours coloured. Use **1D curve** only for transforms that act on each channel separately, such as **Film soft** or **Log-ish lift**.

## Choosing a size

- **17**, **33** and **65** are the sizes most programs expect.
- Larger sizes follow curved transforms more closely and make larger files; a 65³ cube has 274,625 rows.
- Sizes **2**, **4**, **6**, **16**, **18** and **52** place every grid point exactly on an 8-bit value. At other sizes, grid points are written to the nearest 8-bit value, up to half a step away. The note under the slider says which applies.

## The file preview

**The file, as it will be written** shows the first 26 lines of the file, a count of the lines not shown, and the last row. Above it, **What the file will say about itself** explains why the header states the precision.

A saved file looks like this:

```text
# Auric Artisan — LUT lab
# https://auricartisan.com/tool/general/tools/lut-lab/
#
# Transform: Teal and orange
# Kind: stylisation
#
# Sample order: red varies fastest, then green, then blue.
# Precision: this pipeline is 8-bit end to end. Every value below
# is one of 256 levels written to six decimals;
# the decimals are the format's, not this tool's resolution.
# (size-1) does not divide 255, so the grid nodes fall between code values and
# are written to the nearest one - up to half a code out. An 8-bit result is
# unaffected; anything reading this file at higher precision is not.
TITLE "Auric Artisan — Teal and orange"
LUT_3D_SIZE 33
DOMAIN_MIN 0.0 0.0 0.0
DOMAIN_MAX 1.0 1.0 1.0

0.000000 0.000000 0.121569
…
```

| Part | Meaning |
|---|---|
| Lines starting with `#` | Comments: the tool, the transform, its kind, strength and exposure when they apply, sample order and precision |
| `TITLE` | "Auric Artisan — " and the transform's name |
| `LUT_3D_SIZE` or `LUT_1D_SIZE` | The size you chose |
| `DOMAIN_MIN`, `DOMAIN_MAX` | Always 0 to 1 |
| Data rows | Red, green and blue output, six decimals, red index changing fastest |

A **Strength** below 100% adds a `Strength:` line, and the tone-map adds an `Exposure:` line. For a loaded file, the `Transform:` line gives the file's title or name. A 1D curve, or a 3D cube at a size whose grid lands on 8-bit values, leaves out the three lines about grid nodes. The first data row shown is what **Teal and orange** does to black: it lifts the blue.

## Round trips: what survives

Two different questions are worth separating.

1. **Do the numbers survive the file?** Yes. A table written here and read back here reproduces every value to the six decimals the format writes.
2. **Does an identity come back as an identity?** For an 8-bit picture, yes, at every size: an identity table written here and applied back to an 8-bit image leaves every pixel unchanged. But at sizes where the grid does not land on 8-bit values (including 17, 33 and 65), the values in the file sit up to half an 8-bit step off the exact grid. An application reading the file at higher precision sees an identity that is very nearly, but not exactly, one.

The **Round trip** section of the **Method** tab shows both measurements.

### Resampling a loaded file

While a loaded `.cube` is applied, the export resamples it: every grid point of the new table is an 8-bit input looked up in your file with trilinear interpolation, and the result is rounded to 8 bits. The new file follows the original closely but is not a bit-for-bit copy, and a 1D export keeps only what the file does to greys. Keep your original file.

## Other exports

| Button | File | Contents |
|---|---|---|
| **Hue sweep, CSV** | `auric-lut-lab-hue-sweep.csv` | The 72-colour hue ring: shift in hue, lightness and chroma, ΔE₀₀, and whether clipped |
| **Report, JSON** | `auric-lut-lab-report.json` | The transform, the scene, the figures under the pair, the pipeline and the Data register |

### The hue sweep CSV

```text
# Auric Artisan — LUT lab, hue sweep
# transform,Teal and orange
# constant L*,60
# requested C*,40
hue_deg,hue_shift_deg,lightness_shift,chroma_shift,dE00,clipped
0,1.9855,-0.2300,1.3764,0.9428,no
```

One row per test colour, every 5° from 0 to 355. Shifts and differences have four decimal places. The row shown is the first row for **Teal and orange**.

### The report JSON

| Field | Contents |
|---|---|
| `tool`, `url`, `generated` | The tool, its address, and when the report was made |
| `transform` | Name, whether it is a look or a file, the look, strength and exposure |
| `scene` | A drawn scene's id, or your picture's file name |
| `image` | Pixel count, mean, 95th-percentile and largest ΔE₀₀, clipped share, and the old test's share |
| `pipeline` | 256 levels per channel, the sample order, and a note on precision |
| `register` | The status, source and table of every **Data** tab entry |

## Share your settings

**Copy a link to this setting** on the **Lab** tab copies an address that restores the scene, look, strength, exposure, and the export size and kind. For example:

```text
https://auricartisan.com/tool/general/tools/lut-lab/?scene=patches&look=film-soft&s=0.5&e=2&n=33&k=3D
```

The link does not carry a loaded `.cube` or your own picture. Whoever opens it must load those again.
