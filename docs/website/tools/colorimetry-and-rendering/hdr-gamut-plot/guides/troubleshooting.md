---
title: HDR Gamut Plot — Troubleshooting
description: Fixes for common problems in the HDR Gamut Plot.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Troubleshooting the HDR Gamut Plot

| Symptom | Why it happens | What to do |
| --- | --- | --- |
| Changing **Working colour space** changes nothing | The control is not applied in the current version | Use **Overlay gamuts** to choose which spaces are drawn |
| Choosing the 2015 10° observer changes nothing | The locus is always the CIE 1931 2° observer's | Expected |
| **ICtCp marker** draws nothing | Not applied in the current version | No workaround |
| The **Tone mapping operator** menu changes nothing | Not applied in the current version | Use the [Tone Mapping](../../tone-mapping/README.md) lab |
| PQ does not change when I move **Peak brightness** | PQ is absolute; the peak does not scale it | Expected. Choose HLG or a gamma curve to see the peak's effect |
| The HLG reading is marked **Adjusted** | Dim or bright surround applies this tool's own factor | Choose **Reference dark** for BT.2100's value |
| The EOTF comparison chart does not follow my settings | It is drawn once when the page loads | Use **Tone curve output** for your settings |
| My image does not appear on the diagram | The current version reports the image's occupancy as text under the drop area; it does not scatter the pixels on the diagram | Read the results under **Plot an image on it** |
| The image readout shows no nits | A PNG or JPEG does not record absolute luminance | Expected; the tool will not invent one |
| Every image shows 100% of pixels inside all three gamuts | Untagged images are read as sRGB, which sits inside P3 and Rec.2020 | Read the occupancy figures, which do vary |
| Large images look squashed in the analysis | The image is reduced to at most 1,024 pixels on each side, which can change its proportions | Proportions do not affect chromaticity occupancy |
| **Convert to ICtCp** says "No valid hex colours found." | Only six-digit HEX values are read | Use values such as `#FF0000` |
| **Download the result** did not download a file | It copies the CSV to your clipboard | Paste it into a spreadsheet or text file |
| Copying failed | The browser blocked clipboard access | Allow clipboard access, or select the table and copy manually |
| Pressing 1–4 or A does nothing | The focus is in a text box, slider or list | Click an empty area of the page first |
| My shared link opens with different overlays | Links carry axes, peak, curve and plane only | Set the other controls again |
| Shares differ from published figures | The tool divides by its own drawn locus area | See [Compare broadcast gamuts](compare-broadcast-gamuts.md) |
