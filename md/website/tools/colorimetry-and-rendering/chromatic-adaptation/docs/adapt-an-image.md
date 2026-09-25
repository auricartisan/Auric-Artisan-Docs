---
title: Chromatic Adaptation — Adapt an image to a new light
description: Load a photo, adapt it between two illuminants with a chosen transform and degree of adaptation, and export the frame.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Adapt an image to a new light

Use this to see how the colours of a picture shift when it is re-expressed for a different light: for example a D65 photo prepared for a D50 print booth, or a daylight scene shown as it would appear once the eye has adapted to tungsten.

## Steps

1. Open the **Lab** tab.
2. Under **Image Source**, select **Choose image** and pick a PNG, JPEG or other image file your browser can open. The file name appears beside the button. Large images are scaled down to fit 480 × 320 pixels for processing; small images are not enlarged. The status chip shows the size used, for example "Image loaded (480×320)".
3. Under **Illuminants**, set **Source illuminant** to the light the picture was taken or balanced for. Most camera and web images are D65.
4. Set **Destination illuminant** to the light you want to adapt to. Use **Swap** to exchange the two.
5. Choose a **CAT Method**. Bradford is the common choice in colour management; CAT16 is the most recent model.
6. Set **Degree of adaptation D**. 1.00 means complete adaptation; lower values leave part of the source cast in place, as happens when the eye does not fully adapt.
7. Set the moment in time with **Time (scrubber)** (0 to 5 s), or select **Animate** to play it.
8. If bright colours clip harshly after a large shift (for example D65 to A), tick **HDR Tonemap**. It compresses values above white with a Reinhard curve (c ÷ (1 + c) on each channel in linear light) before the image is clipped to the display range.
9. With **Live** ticked, every change re-renders immediately. If you untick Live, select **Run** after each change.
10. Open **Export** and select **Export Frame (PNG)** to download the adapted image.

## What each result shows

| Result | Read it as |
| --- | --- |
| **Adapted Image** | The picture with the adaptation at the current time applied |
| **RGB Histogram (Adapted)** | How the red, green and blue values of the adapted image are distributed |
| **Adaptation Curve A(t)** | The applied adaptation over 0–5 s, with the current time and value marked |
| **Per-Pixel Adaptation State Map** | A grey strip whose brightness is the adaptation in use (white = fully adapted) |
| **LMS Cone-Channel Analysis** | The L, M and S response to the source white (light bars) and the destination white (dark bars), with the scale factor under each |
| **SPD Spectral Overlay** | The spectra of the two illuminants, with a line saying how each was obtained |

For B, C, F2, F7 and F11 the lab holds the white point but not the spectrum. The overlay then says "No spectrum held for …" and explains that the adaptation is unaffected, because only the white point is needed to adapt.

## Choosing D and time

- The adaptation applied at time t starts from an initial state of 0.1 and moves towards your D along the measured time course. After 5 s it has covered about 55% of that distance.
- To see the fully adapted result, you would need a later time than the Lab timeline offers. Use the **Dynamics** tab to read when adaptation reaches 50% and 90%, and use the [Matrix tab](compare-transforms-and-copy-matrices.md), which shows the matrix at the D you set.

## Tips

- The share link on the **Export** tab stores the illuminants, method, D and time, but not the image. Send the image separately.
- **Copy Link** copies the page's current address, which only includes settings if the page was opened from a share link.
- Keyboard: `Space` plays or pauses and `R` resets the time, when the focus is not in a text field. See [Shortcuts](../others/shortcuts.md).

## Result

You have an adapted version of your image at a chosen moment of adaptation, plus a PNG of it.
