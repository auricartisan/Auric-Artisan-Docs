---
title: Gamut Lab — Define a custom colour space
description: Enter your own primaries and white point, derive the RGB ↔ XYZ matrices, and keep, import or export the space.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Define a custom colour space

Use this to check a display's measured primaries, a camera's native gamut, or a proposed working space.

## How the matrices are derived

Given the xy chromaticities of the red, green and blue primaries and of the white point, the lab:

1. turns each primary into XYZ with Y = 1;
2. builds a matrix with those three columns;
3. solves for the scale of each column that makes RGB (1, 1, 1) equal the white point;
4. applies the scales to get the RGB → XYZ matrix;
5. inverts it to get the XYZ → RGB matrix.

This is the standard construction (as described by Bruce Lindbloom), so a custom space gets exactly the same treatment as a published one.

## Enter and solve

1. On the **Lab** tab, set **Working color space** to **Custom**.
2. Under **Primaries (xy)**, type the **R**, **G** and **B** x and y values, and the **W** (white point) x and y. The fields accept four decimal places.
3. Select **Solve from primaries**.
4. Read **RGB ↔ XYZ matrices**: the RGB → XYZ and XYZ → RGB matrices, then the triangle's **Area (xy)** and **Area % sRGB**.
5. **White point XYZ** shows the white as X, Y, Z with Y = 1, for reference.
6. Your triangle is drawn on the diagram as **Custom**.

A custom space made this way uses the sRGB transfer curve. It lasts until you reload the page. To keep it, export it with **This space** (below) while **Custom** is the working space, then import the JSON into the library.

## Keep it in the library

The **Export** tab has a library table listing every standard space and any you have added. Standard spaces show **Load**; your spaces show **Load** and **Del**. Your spaces are kept in this browser's storage, so they are there next time you open the lab on the same device and browser.

To add a space to the library, import it:

1. Open **Export**.
2. Paste a colour space definition into **Bring one in**. The format is:

```json
{
  "name": "MyDisplay",
  "label": "My display",
  "primaries": { "r": [0.680, 0.320], "g": [0.265, 0.690], "b": [0.150, 0.060] },
  "whitePoint": [0.3127, 0.3290],
  "gamma": "sRGB"
}
```

   `name` and `primaries` are required; `label` defaults to the name and `gamma` to `sRGB`.
3. Select **Add to the library**. The status line says "Imported: MyDisplay", or "Invalid JSON" or "Parse error: …" if something is wrong.
4. Select **Load** in the library table to draw the space and make it the working space.

The `gamma` value names the transfer curve: `sRGB`, `BT.2020`, `ROMM`, `AdobeRGB`, `PQ`, `HLG`, `linear`, or a number such as `2.2` for a pure power law.

## Export a space

1. On **Export**, under **What to take**, choose **This space** (the working space) or **Every space** (all of them, including imports).
2. The format is **JSON**. **Exactly what you will get** previews the file and its size.
3. Select **Download** (the button names the file, for example `gamut-lab-srgb.json`) or **Copy to clipboard**.

An exported space contains `name`, `label`, `primaries`, `whitePoint`, `gamma`, `rgb2xyz`, `xyz2rgb` and `area` (the xy triangle area). It can be pasted back into **Bring one in**.

## Result

You have a custom space with verified matrices, drawn beside the standards, saved in your browser and portable as JSON.
