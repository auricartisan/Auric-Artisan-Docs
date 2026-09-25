---
title: Gamut Lab — Troubleshooting
description: Fixes for common problems in the Gamut Lab.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Troubleshooting the Gamut Lab

| Symptom | Why it happens | What to do |
| --- | --- | --- |
| A space I picked earlier disappeared from the diagram | The diagram draws up to five spaces; adding a sixth drops the oldest | Tick **Show all library spaces**, or pick the space again |
| Choosing **Custom** shows nothing | The custom space does not exist until you solve it | Enter primaries and white, then select **Solve from primaries** |
| My custom space vanished after reloading | A solved Custom space is not saved | Export it (**This space**, JSON) and import it with **Add to the library** |
| Import says "Invalid JSON" | The pasted object has no `name` or no `primaries` | Use the format in [Define a custom colour space](define-a-custom-space.md) |
| Import says "Parse error: …" | The text is not valid JSON | Check quotes, commas and brackets |
| Choosing the 10° observer changes nothing | Only the CIE 1931 2° observer is used | Expected |
| The OKLab slice does not move with **Level** | In the current version the OKLab slice is fixed at L = 0.5; only the label changes | Use **Constant L\* (CIELAB)** to move through lightness |
| In the u′v′ diagram, the vertex readout colour and membership look wrong | The readout treats the clicked coordinates as CIE 1931 x, y | Switch **Diagram mode** to **CIE 1931 xy** before probing |
| The vertex readout always shows L* 100 | The probe takes the chromaticity at Y = 1, the brightest colour of that chromaticity | Expected; it describes chromaticity, not a particular lightness |
| The WebGL fill does nothing | The browser or device does not support WebGL 2, or it is disabled | Leave the fill off; the diagram works without it |
| The wireframe cannot be rotated | It is drawn at a fixed viewing angle | Expected |
| A share of "> 100%" appears | The space's primaries lie outside the spectral locus | Expected for ACES AP0 and ProPhoto RGB; read the volume instead |
| Percentages differ from other tools | Other tools often divide by a different locus area, and often in xy | See [Compare colour spaces](compare-colour-spaces.md) |
| Volume figures change between runs | They are sampled estimates | Raise **Samples** on the Compare tab; the ± spread shrinks |
| The equation box shows an odd power-law form for Rec. 2020, Adobe RGB or ProPhoto | The box simplifies those curves | Use the Transfer tab or Reference › Formulas |
| The comparison export has fewer rows than spaces | It covers only the spaces drawn on the diagram | Draw the spaces you want first |
| A long link warning appears | Links over about 1,800 characters may be cut off by some apps | Send the link as a file or shorten the view (fewer spaces) |
| **Copy to clipboard** is missing | It is hidden for PNG and link choices | Use **Download**, or **Copy the link** for links |
