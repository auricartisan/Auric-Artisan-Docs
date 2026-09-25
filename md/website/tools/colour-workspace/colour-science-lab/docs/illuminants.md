---
title: Color Science Lab — Illuminants
description: See one colour adapted to seven CIE illuminants with the Bradford transform, and how far it shifts under each.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Illuminants

The **Illuminants** view shows the Workbench specimen as it would appear to an observer adapted to each of seven standard lights, and measures how far it moves from its D65 appearance.

## Layout

- **The same colour, adapted** (*Bradford · from D65*): one patch per illuminant with its name, colour temperature and **ΔE00** from D65. The explanation under it: each patch is the specimen re-rendered for an observer adapted to that illuminant, using the Bradford transform.
- The verdict: the largest shift and the illuminant that causes it, with *A match made under D65 will not hold there.* when the shift is above 5, or *The colour holds reasonably across the set.*
- **Shift by illuminant** (*ΔE00 from D65*): each illuminant other than D65 with its description and shift, coloured green below 3, amber 3 to 8 and red above 8.

## The illuminants

| Illuminant | Description | Temperature |
| --- | --- | --- |
| D65 | Daylight · reference | 6504 K |
| D50 | Print viewing | 5003 K |
| D55 | Mid daylight | 5503 K |
| C | Average daylight (obsolete) | 6774 K |
| A | Incandescent | 2856 K |
| F2 | Cool white fluorescent | 4230 K |
| F11 | Narrow tri-band fluorescent | 4000 K |

## Tasks

### See which light is most risky for a colour

1. Set the specimen on the **Workbench** (or keep the current one).
2. Open **Illuminants** and read the verdict and **Shift by illuminant**.

Result: the light under which the colour changes most.

## Notes

- This view always uses the Bradford transform and the 2° observer, whatever you chose on the Workbench.
- It models adaptation of an sRGB colour, not the spectral reflectance of a real surface. Two surfaces that match under D65 can still separate under another light (metamerism) in ways only spectral data can predict.

## Related

- [The Workbench](workbench.md)
- [Illuminants tool and other colorimetry tools](../../../colorimetry-and-rendering/README.md)
- [Limits and accuracy](../others/limits-and-accuracy.md)
