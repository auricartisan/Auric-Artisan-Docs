---
title: ICC Profile Parser — FAQ
description: Short answers to common questions about the ICC Profile Parser.
product: Website › Tools › Image and file tools › ICC Profile Parser
updated: 2026-09-25
---

# ICC Profile Parser FAQ

## Is my profile uploaded?

No. The file is read in the page and never sent anywhere. See [Privacy](../others/privacy.md).

## Which files can I open?

Standalone ICC profiles, usually ending `.icc` or `.icm`, of version 2 or version 4. A profile embedded in an image or PDF must be saved out as its own file first. A version other than 2 or 4 is still read, with a warning.

## Can I compare two profiles side by side?

Not on one page. The tool holds one profile at a time. To compare, save a reading of each and compare the JSON files, or open the tool in two browser tabs.

## Why does my monitor profile say "sRGB" when I calibrated a wide-gamut screen?

The verdict names the closest of six reference spaces. Check the **Primaries Δu′v′** column: if the first row's distance is large, the match is loose. Also check whether the menu under **Compare against** shows the space you expect.

## What does "matrix/TRC" mean?

The profile describes an RGB device with three colorants (a matrix) and three tone response curves (TRCs). See [Understand ICC profiles](understand-icc-profiles.md).

## Why are the stored colorants and the primaries different triangles?

Colorants are stored after adaptation to D50, the connection-space white. The primaries of the space the profile describes are recovered by reversing that adaptation. The diagram shows both so you can see the difference.

## Is "136% sRGB" coverage?

No. That kind of figure is an area ratio. The tool gives both: **area, u′v′** is the area ratio, and **covers of it** is the true share of the reference space inside the profile's gamut, which cannot exceed 100%.

## Does a clean result mean my colours are right?

It means the file is well formed. It says nothing about whether the device still behaves as the profile describes; that needs a measuring instrument and the device.

## Why is there no score out of 100?

A profile either meets the specification or it does not, and where it does not, each finding names the clause. Averaging unlike rules into one number hides which rule mattered.

## Can the tool fix or edit a profile?

No. It reads profiles and reports on them. It does not write or modify profile files.

## Can it convert colours using the profile?

No. It reads tone curves and, for CMYK and similar profiles, walks the A2B table to draw the gamut, but it does not offer colour conversion through the profile.

## Why is a named-colour profile nearly empty?

A named-colour profile is little more than its list of named colours, and the tool does not resolve those names to colours or list them on the page. For that class of profile you get the header, the tag table and the conformance findings: the shape of the data, not its content.
