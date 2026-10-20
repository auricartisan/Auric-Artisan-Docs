---
title: Tone Mapping — Troubleshooting
description: Fixes for common problems in the Tone Mapping lab.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Troubleshooting Tone Mapping

| Symptom | Why it happens | What to do |
| --- | --- | --- |
| My photo looks flat or unchanged by the curve | An 8-bit PNG or JPEG stops at 1.0, so there are no highlights above white for the curve to compress | Raise **Exposure**, or use the built-in HDR test scene to compare curves |
| My photo looks too dark or washed out | The source encoding does not match the file | For ordinary images choose **sRGB** encoding and **Rec.709** primaries |
| Changing **Display peak** or **Source peak** changes nothing | The seven working curves do not use the peaks | Expected. The peaks affect the retired operators and the false-colour map |
| **Soft compress** looks exactly like **Clip** | In the current version the two give the same result | Use **Preserve hue** to keep channel ratios in out-of-gamut colours |
| The HDR 1000 preset looks pale and washed out on my screen | PQ output is an HDR encoding (a display value of 1.0 is encoded as 10,000 nits), and an ordinary screen shows PQ code values as if they were sRGB | Use sRGB output for viewing on a standard display; use PQ only when exporting for HDR |
| **Linear axis**, **Log axis** or **Film stops** does not change the chart | They set the custom curve's knee, mid and shoulder | Tick **Use the custom curve instead** to see their effect |
| The custom curve fields do nothing | The custom curve is used only when its box is ticked or **Custom 1D curve** is selected | Tick **Use the custom curve instead** |
| The low-level operator does nothing | Parameters a and b start at 0 | Enter a positive **a** |
| Gamma-domain scale or Scaled Reinhard are not in the list | They are not tone curves and are no longer offered | See them on the **Operators** tab |
| The false-colour note and the map disagree | The note uses the Source peak; the map uses the Display peak | Set both peaks to the same value when reading the map |
| The split view shows only one version | Both A and B must be stored | Select **Store A** and **Store B**, then tick **Split the viewport** |
| **Analyse** says "No valid hex colours found." | Only six-digit HEX colours are read, although the box's example shows numbers | Enter values such as `#FF8800` |
| **Download the result** says "Run batch first" | No analysis has been run | Select **Analyse** first |
| The link does not restore my grade | The link records operator, exposure, source encoding, display peak, output and target primaries only | Re-enter the grade, or export the pipeline `.cube` |
| A LUT looks different from the preview in another program | A curve export carries only step 5 | Export **The whole pipeline** as `.cube` |
| Copy fails | The browser blocked clipboard access | The text is in the preview; select and copy it |
| **Reset** cleared everything | It reloads the lab with defaults | Use a stored link to return to a setup |
