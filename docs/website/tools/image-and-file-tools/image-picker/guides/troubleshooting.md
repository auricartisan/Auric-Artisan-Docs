---
title: Image Picker — Troubleshooting
description: Symptoms you may meet in the Image Picker, why they happen, and what to do.
product: Website › Tools › Image and file tools › Image Picker
updated: 2026-09-25
---

# Troubleshooting the Image Picker

The Image Picker does not show pop-up messages, so when something fails, the usual sign is that nothing changes. This page lists the common causes.

## Loading pictures

| Symptom | Why | What to do |
|---|---|---|
| Nothing happens after dropping or choosing a file | The file is not an image, or your browser cannot decode it | Save it as PNG or JPEG and try again. Some formats, such as HEIC or camera RAW, are not opened by every browser |
| Dropping a second picture on the preview opens it in the browser instead | The drop area is only active before a picture is loaded | Use **Replace**, or select **Reset** first to bring the drop area back |
| **Load URL** does nothing | The address is not an image, cannot be reached, or the server does not allow other sites to read its pixels | Download the image and load it with **Replace** |
| After **Load URL** the middle panel goes blank | The picture loaded, but its server does not allow its pixels to be read (cross-origin protection) | Download the image and load it as a file |
| The size line shows a much smaller working size | Pictures are shrunk to fit 800 × 500 for analysis | This is expected; the palette still covers the whole picture |

## The palette

| Symptom | Why | What to do |
|---|---|---|
| The **Clusters** label says 16 but the slider will not go past 12 | The page starts at 16; the slider covers 2 to 12 | Move the slider to choose 2 to 12, or leave it untouched to keep 16 |
| Fewer colours than the cluster count | Merging combined some, or the picture has fewer distinct colours | Lower **Merge threshold**, or accept it: flat artwork keeps its exact colours |
| Several near-identical shades | Clusters that are close are kept apart when merging is off | Raise **Merge threshold** |
| A white background or black border dominates | Those pixels are part of the picture | Turn on **Ignore light** or **Ignore dark** |
| The palette changes slightly each time | k-means++ starts from random colours | Select **Re-extract** until you are happy, then export |
| A small but important colour is missing | It covers too few pixels to form a cluster | Raise **Quality** or **Clusters**, or pin it with the eyedropper |

## Eyedropper and pins

| Symptom | Why | What to do |
|---|---|---|
| **Pin** does nothing | Moving the pointer onto the button clears the colour under it | Click directly on the preview to pin |
| A click does not add a pin | The colour is already pinned, or the pixel is transparent | Check **Pinned**; pick an opaque pixel |
| The oldest pin disappeared | Pins are capped at 24 | Copy the JSON before pinning more |
| Pins are missing from my CSS or hex copy | Only the JSON export includes pins | Copy or download the JSON |

## Copying and exports

| Symptom | Why | What to do |
|---|---|---|
| No sign that anything was copied | The page shows no confirmation | Paste to check |
| Nothing is copied | Your browser blocked clipboard access | Allow clipboard access for the site, or use the downloads on the **Actions** tab |
| The shortcut keys do nothing | Focus is in a text field, slider, switch or menu | Click an empty part of the page first |
| The page reset unexpectedly | `R` resets the workbench when focus is not in a control | Load the picture again; your settings are kept |
| The copied page link opens an empty tool | The link does not carry the picture or palette | Share the JSON, CSS or SVG instead |

## Batch analysis

| Symptom | Why | What to do |
|---|---|---|
| **No valid hex colours found.** | Nothing in the box is a hex value | Enter values such as `#D3AF37` or `D3AF37` |
| A colour's figures look wrong | It was entered with an alpha part (four or eight digits) | Use three or six digits |

## Charts

| Symptom | Why | What to do |
|---|---|---|
| **Nothing charted yet** | No picture is loaded | Load a picture on the **Workbench** |
| Bar labels are missing | There are too many clusters for the labels to fit | Open the chart full screen, or read the shares on the swatches |

For help with the site in general, see [Help](../../../../../help/README.md).
