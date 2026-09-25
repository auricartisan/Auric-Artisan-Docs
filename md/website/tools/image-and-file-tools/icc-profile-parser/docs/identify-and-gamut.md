---
title: ICC Profile Parser — Identify a profile and read its gamut
description: Read the verdict and ranking, choose a reference space, and interpret the chromaticity diagram, gamut area, coverage and tone curves.
product: Website › Tools › Image and file tools › ICC Profile Parser
updated: 2026-09-25
---

# Identify a profile and read its gamut

After you load a profile on the **Lab** tab, the right-hand panel opens with **What this profile is**. This guide explains each part of it.

## The verdict

The verdict is a heading and a few sentences.

| Profile | Heading reads, for example |
|---|---|
| Has RGB colorants | "An *sRGB* profile, matrix/TRC, ICC v2.1.0" |
| No colorants, but a readable A2B table | "A *CMYK* output profile, ICC v2.0.0" |
| Anything else | "An ICC v4.3.0 display profile" |

The sentences under the heading say:

- how far the colorants sit from the closest space's primaries, in CIE 1976 u′v′, and which of two adaptation methods, Bradford or XYZ scaling, fits the profile better;
- how closely the tone curve fits that space's published transfer function, as a peak difference;
- for a profile with no colorants, which table its gamut was read from, how many grid points it has and the range of CIELAB lightness (L*) it covers;
- whether it is conformant: "It is conformant: 21 of 23 rules pass, with 2 below the level of an error", or how many rules it should satisfy do not hold.

Two extra lines can appear:

- **"This profile cannot be told apart from Rec. 709 here"** appears when two reference spaces share the same primaries and white, and the profile has no tone curve to separate them. sRGB and Rec. 709 are the usual pair.
- **"Separated from Rec. 709 by the tone curve, not by the primaries"** appears when the primaries tie and the tone curve decides.

## The ranking table

**How close, and to what** appears for profiles with RGB colorants. It ranks all six reference spaces, closest first; the first row is highlighted.

| Column | Meaning |
|---|---|
| **Space** | The reference space |
| **Primaries Δu′v′** | The largest of the three distances between the profile's colorants and the space's primaries, in CIE 1976 u′v′ |
| **Curve fit** | The largest difference between the profile's tone curve and the space's transfer function, on a 0 to 1 scale |
| **White** | Always **matched**, because the comparison is made at one white (see below) |
| **Verdict** | **this profile**, **same primaries, different curve**, **same curve, different primaries**, or a dash |

Rows are ordered by the primaries distance, and by the curve fit when two spaces tie. The note above the table reads **adapted into the PCS ·** followed by **Bradford** or **XYZ scaling**, the adaptation that fits the profile better.

### Why the white point is not a term

A conformant display profile stores its white as D50, the connection-space white, while five of the six reference spaces are defined at D65. Comparing whites directly would penalise every correct profile by the same amount. So the tool first adapts each reference space's primaries into the connection space, and only then compares them with the profile's colorants. Both sides are then at the same white, and the white cannot add a difference.

### A distance in u′v′

The CIE 1976 u′v′ diagram is a version of the CIE 1931 chromaticity diagram stretched so that equal distances look more nearly equal. The smaller the **Primaries Δu′v′**, the closer the match; compare the first row with the second to see how clearly the winner stands out.

## Choose the space to compare against

The **Compare against** menu on the left lists the six reference spaces: **sRGB**, **Rec. 709**, **Display P3**, **Adobe RGB (1998)**, **Rec. 2020** and **ProPhoto RGB**. The choice sets:

- the white dashed triangle on the chromaticity diagram;
- the dashed reference curve on the tone-response plot;
- the **area, u′v′**, **covers of it** and **area, xy** cards.

When a profile loads, the comparison switches to the closest space. The label of the menu may still show your previous choice. The first row of the ranking table names the closest space; to be certain which space the area figures refer to, choose it from the menu yourself.

Closest means closest among these six. A profile that describes a space outside the list is still ranked against them, and the distances in the table show how poor even the best match is.

## The chromaticity diagram

For a profile with RGB colorants, the left plot is headed **Chromaticity · CIE 1931 xy** and marked **2° observer**. The horseshoe outline is the spectral locus, the chromaticities of pure spectral light from 380 to 700 nm. Inside it:

| Mark | What it is |
|---|---|
| Blue dashed triangle | The colorants as stored in the profile, adapted to D50 |
| Gold solid triangle, lightly filled | The primaries recovered from those colorants |
| White dashed triangle | The space you are comparing against, adapted into the connection space |
| White dot | The profile's media white point |

The caption under the plots says how the primaries were recovered: with the profile's own `chad` tag, or with the Bradford transform from an assumed white because the profile carries no `chad` tag.

## The tone-response plot

The right plot, **Tone response**, marked **device → linear**, draws each tone curve from input value 0 to 1 against linear light 0 to 1: red, green and blue curves, a gold grey curve for `kTRC`, and a dashed curve for the transfer function of the space you are comparing against. A curve that lies on the dashed line matches that space's published transfer function.

The reference curves are: the piecewise sRGB function for sRGB and Display P3; a 2.4 power for Rec. 709; the Adobe RGB power of 563/256 (about 2.2); the Rec. 2020 function; and the ProPhoto (ROMM) 1.8 power with a short straight section near black.

The plot is shown only for profiles with RGB colorants.

## Profiles with no colorants

A CMYK press profile, and other LUT-based profiles, carry no colorants and no tone curves. For these, when the profile has an `A2B1` or `A2B0` table in the lut8 or lut16 format, the tool reads every grid point of that table, converts it to CIELAB, and draws the outline of the result.

- The plot is headed **Gamut · CIELAB a*b* hull**, with the a* axis across and the b* axis up, and rings every 20 units.
- The tone-response plot is hidden.
- The caption names the table and the number of grid points, for example 6,561 for a table of 9 × 9 × 9 × 9.
- The area cards show a dash, because area in u′v′ applies only to RGB triangles.

No gamut is drawn when the table has more than 200,000 grid points, is incomplete, does not have three output channels, or uses one of the version 4 table formats (`mAB ` or `mpet`).

## The figure cards

| Card | Meaning |
|---|---|
| **version** | The ICC version, major.minor.bug-fix |
| **conformance** | **clean** (nothing raised), **no errors** (only warnings or notes), or the number of errors |
| **tags** | How many tags the tag table lists |
| **area, u′v′** | The area of the profile's primaries triangle as a percentage of the reference space's triangle, in CIE 1976 u′v′ |
| **covers of it** | The share of the reference space's triangle that lies inside the profile's triangle |
| **area, xy** | The same area ratio computed in CIE 1931 xy, shown for comparison |

### Area is not coverage

**area, u′v′** answers "how big is this gamut compared with that one?" It can exceed 100%: Adobe RGB is larger than sRGB. **covers of it** answers "how much of that space can this profile reproduce?" It is a real overlap and cannot exceed 100%. A figure such as "136% sRGB" in marketing material is an area ratio, not coverage.

### Why u′v′ rather than xy

The CIE 1931 xy diagram stretches the greens and squeezes the blues and reds, so areas measured on it do not match what people see. The **area, xy** card is kept because it is the figure much of the industry quotes. Measured across the reference spaces, xy overstates Adobe RGB by 18.2 percentage points and Rec. 2020 by 16.8, and understates ProPhoto RGB by 14.4, compared with u′v′.

## The Method tab

The **Method** tab explains each step in five sections, chosen with the buttons under **The chain**:

| Section | What it shows |
|---|---|
| **The header** | Bytes 8 to 11 of the loaded profile, labelled, and how they make the version number |
| **Colorant vs primary** | How far sRGB's stored colorants sit from its primaries, and why both adaptation methods are tested |
| **Identification** | Why the white point is taken out of the comparison, and the order of the steps |
| **Gamut area** | Every reference space's area as a percentage of sRGB in xy and in u′v′, and its coverage of sRGB |
| **A profile with no colorants** | How the gamut is read from an A2B table; with such a profile loaded, its figures |
