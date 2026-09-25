---
title: Chromatic Adaptation — Troubleshooting
description: Fixes for common problems in the Chromatic Adaptation lab.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Troubleshooting Chromatic Adaptation

| Symptom | Why it happens | What to do |
| --- | --- | --- |
| The image area is dark and says "No image yet" | No image has been loaded | Select **Generate the sample sweep** or **Choose an image** |
| Nothing changes when I move a slider | **Live** is off, or no image is loaded | Tick **Live**, or select **Run** after changes |
| The image hardly changes at 0 s | Adaptation starts at 0.1 and grows with time | Move **Time (scrubber)** towards 5 s |
| The image is only partly adapted even at 5 s and D = 1 | The measured slow phase has a 30 s half-life, so at 5 s about 55% of the change has happened | Expected. The **Matrix** tab shows the matrix at the D you set; the **Dynamics** tab shows when 90% is reached |
| Display Gamma, the per-pixel scales, Local radius, Local strength, Mix, Tile factor or Target FPS change nothing | These controls are not applied in the current version; they are only recorded in the JSON export | See [Reference](reference.md#controls-with-no-visible-effect-in-the-current-version) |
| The GPU box (or `G`) changes nothing | Processing always runs on the CPU | Expected |
| The state map is a flat grey | The per-pixel model has no effect in the current version, so every pixel has the same adaptation | Expected. Its brightness equals the adaptation in use |
| The SPD overlay says "No spectrum held" | B, C, F2, F7 and F11 spectra are not held | The adaptation is still correct, because it uses the tabulated white point |
| Bright colours clip after a large shift such as D65 to A | Adapted values exceed the sRGB range and are clipped | Tick **HDR Tonemap** to compress highlights first, or choose a smaller shift |
| My photo looks smaller or softer | Images are scaled to fit 480 × 320 for processing | Expected. The exported PNG is at the processing size |
| **Run Batch** says "Enter valid hex values" | No six-digit HEX lines were found | Enter values such as `#735244` or `735244`, one per line |
| Only 50 of my colours appear | The batch is capped at 50 | Split the list and run it in parts |
| The share link opens without my image | Links carry settings only | Send the image separately |
| **Copy Link** gave a link without my settings | Copy Link copies the page's current address | Use **Generate** under Share URL instead |
| Copying fails with "Copy failed" | The browser blocked clipboard access | Allow clipboard access, or copy the text from the field manually |
| Dropping a file on **Install a table** does nothing | The drop area is not active in the current version | No workaround; the lab uses its built-in tables |
| Space, R, C or G does nothing | The focus is in a text box, slider or list | Click an empty part of the page first |
| A chart is too small to read | — | Double-click it, or select its **Fullscreen** button; `Esc` closes |
