---
title: ICC Profile Parser — Understand ICC profiles
description: The concepts you need to read an ICC profile: classes, colour spaces, the connection space, tags, versions, intents, colorants, curves and tables.
product: Website › Tools › Image and file tools › ICC Profile Parser
updated: 2026-09-25
---

# Understand ICC profiles

This page explains the parts of an ICC profile that the ICC Profile Parser shows you. It is a short primer, not a replacement for the specification, ICC.1:2010 (also published as ISO 15076-1:2010).

## What a profile is for

A colour management system converts colours from one device to another, for example from a camera to a monitor, or from a monitor to a printing press. It does this in two halves. Each device has a profile that converts between the device's own colour values and a shared, device-independent space called the **profile connection space** (PCS). Converting from device A to device B means going from A into the PCS with A's profile, then out of the PCS with B's profile.

An ICC profile is the file that holds one of those halves. It has three parts:

1. a 128-byte **header** that says what kind of profile it is;
2. a **tag table** that lists the pieces of data inside;
3. the **tag data** itself: curves, matrices, tables and text.

## The profile connection space

The PCS is either CIE XYZ or CIELAB, always relative to the D50 illuminant, a standard daylight white at about 5000 K. The header's **PCS** field says which. D50 is fixed by the specification, which is why the tool checks that the header's PCS illuminant is D50 and that a display profile's media white point is the PCS white.

## Device classes

The header's class field says what the profile describes. The tool shows the four-character code and its name.

| Code | Class | What it describes |
|---|---|---|
| `scnr` | Input | A capture device such as a scanner or camera |
| `mntr` | Display | A monitor or other display |
| `prtr` | Output | A printer or press |
| `link` | DeviceLink | A direct conversion from one device to another, with no PCS in between |
| `spac` | ColorSpace | Conversion between the PCS and a standard colour space |
| `abst` | Abstract | An effect applied within the PCS, such as a look |
| `nmcl` | NamedColor | A list of named colours, such as a spot-colour book |

## Data colour space and channels

The **data space** is the colour space of the device values: RGB, CMYK, Grayscale, CIELAB, or a multi-ink space such as `6CLR` (six colours). The tool shows the channel count beside it, for example **RGB · 3 ch** or **CMYK · 4 ch**.

## Versions

Two major versions are in use: version 2 (for example 2.1.0 or 2.4.0) and version 4 (for example 4.3.0). The version is stored in bytes 8 and 9 of the header: byte 8 is the major version, and byte 9 holds the minor version and the bug-fix level. The tool shows it as major.minor.bug-fix. In version 4, every profile must carry the media white point tag and should carry a profile ID. In version 2, the white point is required for most classes but not all, and the profile ID is optional.

## Rendering intents

A rendering intent is the strategy for handling colours one device can show and another cannot. The header records one of these four values.

| Value | Intent | In short |
|---|---|---|
| 0 | Perceptual | Compresses the whole gamut so relationships between colours are kept |
| 1 | Media-relative colorimetric | Keeps in-gamut colours exact relative to the paper or display white; clips the rest |
| 2 | Saturation | Keeps colours vivid, for charts and graphics |
| 3 | ICC-absolute colorimetric | Keeps in-gamut colours exact, including the white of the medium |

## Tags

Every piece of data in a profile is a **tag**: a four-character signature, such as `wtpt` or `rTRC`, that points to a block of data at an offset in the file. The block starts with its own four-character **type**, such as `XYZ ` or `curv`, which says how to read it. The tool's tag table shows the signature, type, offset and size of every tag.

The specification allows two tags to point to the same block of data. Press profiles use this to store an identical table once, for example when the perceptual and saturation tables are the same. The tool reports this as sharing, not as a fault. What is a fault is a block that partly overlaps another without being the same block.

### Tags you will often see

| Signature | Name | What it holds |
|---|---|---|
| `desc` | Profile description | The profile's name as software shows it |
| `cprt` | Copyright | Copyright text |
| `wtpt` | Media white point | The white of the medium, as XYZ |
| `rXYZ`, `gXYZ`, `bXYZ` | Red, green, blue colorants | The XYZ of each primary, adapted to D50 |
| `rTRC`, `gTRC`, `bTRC` | Red, green, blue tone curves | How each channel's values map to light |
| `kTRC` | Grey tone curve | The tone curve of a greyscale profile |
| `chad` | Chromatic adaptation | The 3×3 matrix used to adapt the colorants to D50 |
| `A2B0`, `A2B1`, `A2B2` | Device-to-PCS tables | Perceptual, colorimetric and saturation conversions into the PCS |
| `B2A0`, `B2A1`, `B2A2` | PCS-to-device tables | The same three intents, out of the PCS |
| `gamt` | Gamut | A table that says whether a PCS colour is in the device gamut |
| `pseq` | Profile sequence | For a DeviceLink, the profiles it was built from |
| `ncl2` | Named colour | The named colours of a NamedColor profile |

Many display profiles made by calibration software also carry `vcgt`, a private tag that is not part of ICC.1:2010. The tool lists it in the tag table but does not read it.

## Two ways to describe a device

**Matrix/TRC profiles** describe an RGB device with three colorants and three tone response curves (TRCs). Most display and RGB working-space profiles, including sRGB, are built this way. The tool's verdict calls these "matrix/TRC".

**LUT-based profiles** describe a device with lookup tables in the `A2B` and `B2A` tags. Every CMYK press profile is built this way, and some RGB profiles are too. The tool's verdict calls an RGB profile without colorants "LUT".

## Colorants are not primaries

The colorants in `rXYZ`, `gXYZ` and `bXYZ` are stored after adaptation to the D50 connection space. They are therefore not the chromaticities of the colour space's primaries. For sRGB, the stored green colorant sits about 0.021 away in the CIE 1931 xy diagram from sRGB's published green primary.

To recover the real primaries, the tool reverses the adaptation. When the profile carries a `chad` tag, the tool uses the inverse of that matrix, which recovers them exactly. When it does not, the tool assumes the adaptation was the Bradford transform from the white of the space being compared, and says so. Bradford is the chromatic adaptation method the `chad` tag conventionally carries; some older profiles instead scale XYZ directly, and the tool tests both and reports which fits better.

## Tone response curves

A TRC maps a channel's device value (0 to 1) to linear light (0 to 1). The specification allows several forms, all of which the tool reads:

- **Identity**: output equals input.
- **Gamma**: a single power, for example 2.2.
- **Table**: a list of sampled values, read with straight-line interpolation between them.
- **Parametric**: one of five formulas with up to seven parameters, which can express a gamma with a linear segment near black, as sRGB uses.

## The profile ID

Bytes 84 to 99 of the header may hold a profile ID: an MD5 checksum of the whole file, calculated with the flags, rendering intent and ID fields set to zero. If the ID is present and matches, the file has not been changed since the ID was written. Version 4 profiles should carry one; in version 2 the field is usually all zeros, which the tool reports as **not carried**.

## What a profile cannot tell you

A profile describes a device as it was when the profile was made. It is not the device. A perfectly formed profile can describe a monitor that has drifted since it was calibrated. Checking the device itself needs a measuring instrument; see [Limits and accuracy](../others/limits-and-accuracy.md).
