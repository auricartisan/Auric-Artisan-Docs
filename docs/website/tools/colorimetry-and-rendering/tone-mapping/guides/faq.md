---
title: Tone Mapping — FAQ
description: Short answers to common questions about the Tone Mapping lab.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Tone Mapping FAQ

## Which curve should I use?

For a photographic look with gentle highlight roll-off, Hable filmic or the Narkowicz fit are common choices. Reinhard is simple and never clips, but never reaches pure white. Compare them on the Operators tab at mid-grey and scene white before deciding.

## Is "Narkowicz fit" the ACES tone mapper?

No. It is Krzysztof Narkowicz's 2016 curve fit that approximates the look of the ACES output transforms. The Academy's own transforms are not implemented.

## What happened to the BT.2446 operators?

The two operators once labelled BT.2446 Method A and Method C did not implement ITU-R BT.2446. One multiplied by a small constant and turned the frame nearly black; the other could never exceed a 10% linear grey. They are renamed Gamma-domain scale and Scaled Reinhard, shown on the Operators tab, and no longer offered in the Lab.

## What is the difference between scene-referred and display-referred?

Scene-referred values describe light in the scene and can exceed 1. Display-referred values are 0 to 1 of what the display can show. The lab treats a linear source as scene-referred and anything encoded (sRGB, PQ, HLG, gamma) as display-referred.

## Why ACEScg as the default working space?

ACEScg is a wide, linear working space designed for rendering and compositing. Grading in it and converting to the display at the end is common practice. You can choose Rec.709, Display P3 or Rec.2020 instead.

## Which export reproduces the preview?

The whole-pipeline 3D `.cube`. The curve export holds only the tone curve.

## Can I load an EXR or HDR file?

The lab reads images your browser can decode (such as PNG and JPEG), which are 8-bit. It does not read OpenEXR or Radiance HDR files.

## Can I save and reload my settings as a file?

Not in the current version. Use the link, or the floating **Save to Library** button, which stores an image of the frame.

## Is my image uploaded?

No. It is decoded and processed in your browser.
