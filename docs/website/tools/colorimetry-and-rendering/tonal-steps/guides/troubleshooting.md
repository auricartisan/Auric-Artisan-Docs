---
title: Tonal Steps — Troubleshooting
description: Fixes for common problems in Tonal Steps, Tints and Shades.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Troubleshooting Tonal Steps

| Symptom | Why it happens | What to do |
| --- | --- | --- |
| My base colour is not in the ramp | The engines step lightness or luminance evenly from white to black; the base rarely lands exactly on a step. The base note says "not a step" | Expected. Use the key sets, where 500 is always your colour, or tints and shades, which start from it |
| Changing **Mix in** does not change the ramp | The mixing space applies to tints, shades, tones and key sets, not to the main ramp | Tick a set under **Also show** to see the effect |
| **sRGB linear** gives the same result as OKLab | In the current version the sRGB linear option mixes in OKLab | Use CIELAB or HSL for a visibly different mix |
| **Easing γ** does nothing | Easing applies only to Equal luminance and the neutral ladder | Switch the engine to **Equal luminance** |
| The **Equal contrast** engine is missing | It produces the same ramp as Equal luminance, so it is not offered on the Lab tab | Use Equal luminance; the Ramps tab shows both |
| Pressing `3` shows a ramp that looks like Equal luminance | `3` selects the Equal contrast engine, which gives the same colours | Expected |
| The base colour field ignores my value | It needs a six-digit HEX with `#` | Type a value such as `#D3AF37` |
| The **Metric** choice on Contrast changes nothing | Both WCAG and APCA figures are always shown | Read the column you need |
| The contrast export ignores my **Against** choice | Exports list contrast against both white and black | Use the Contrast tab for the base colour |
| **Download the result** did not save a file | It copies the analysis as CSV to your clipboard | Paste it where you need it |
| "No valid hex colours found." | The list has no six-digit HEX values | Put one value per line, for example `2563eb` |
| Copying fails | The browser blocked clipboard access | Allow clipboard access, or select the preview and copy manually |
| `1`, `2`, `3` or `R` do nothing | The focus is in a field or slider | Click an empty part of the page first |
| Colours differ from the Tailwind or Material palettes | The key sets borrow the key names only | Expected; they are this tool's own ladders |
| OKLab L values differ from an older export | Earlier versions fed OKLab gamma-encoded values; OKLab now receives linear sRGB | Re-export; new files note `oklab_input=linear_srgb` |
| APCA values differ from an older export | APCA-W3 0.1.9 now runs as published | Turn on **Show the difference** to compare |
