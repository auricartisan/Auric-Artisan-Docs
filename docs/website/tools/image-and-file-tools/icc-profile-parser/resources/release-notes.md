---
title: ICC Profile Parser — Release notes
description: User-facing history of the ICC Profile Parser.
product: Website › Tools › Image and file tools › ICC Profile Parser
updated: 2026-09-25
---

# Release notes

## 4 June 2026 — ICC Profile Reading

The earlier engine was replaced by the current workbench, titled **ICC Profile Reading**, with six tabs: **Lab**, **Method**, **Conformance**, **Data**, **Export** and **Reference**. The site's earlier user guide carries a notice that it describes the engine replaced on this date.

What changed for you:

- **The version is read correctly.** The version now comes from the whole of byte 8 and the two halves of byte 9, as the specification says. Profiles are no longer reported as version 0.2 or 0.4, and no longer flagged for an "unusual" version.
- **Shared tag data is allowed.** Two tags pointing at one data block, which the specification permits, are shown as sharing rather than reported as corrupt. A partial overlap is still an error.
- **Identification works on conformant profiles.** Reference spaces are adapted into the connection space before comparing, so a correct D50 white no longer counts against a profile. The ranking shows primaries distance, curve fit and white separately instead of one blended score.
- **Colorants and primaries are drawn separately.** The diagram shows the stored colorants, the primaries recovered from them, and the reference space.
- **Area in u′v′, and coverage.** Gamut area is given in CIE 1976 u′v′ with the xy figure beside it, and true coverage is shown separately from the area ratio.
- **CMYK and other LUT profiles get a gamut.** The gamut of a profile without colorants is drawn from its A2B table as a CIELAB hull.
- **No score out of 100.** Each finding carries a severity and the clause it enforces; a profile is conformant or it is not.
- **Damaged tags no longer stop the reading.** A tag that cannot be decoded, or a truncated table, becomes a finding and the rest of the profile is read.
- **The profile ID is recomputed** and compared with the stored one.

## 25 May 2026 — earlier version

The ICC Profile Parser user guide was published in the site's documentation library. It describes the earlier engine and is now marked as superseded.
