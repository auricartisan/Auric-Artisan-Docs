---
title: HDR Gamut Plot — FAQ
description: Short answers to common questions about the HDR Gamut Plot.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# HDR Gamut Plot FAQ

## What is the difference between PQ and HLG?

PQ (SMPTE ST 2084) is absolute: each signal value means a specific luminance, up to 10,000 nits, and displays that cannot reach it must tone-map. HLG (ARIB STD-B67 / BT.2100) is relative: the display applies a system gamma based on its own peak, which makes HLG backward-compatible with standard displays.

## What does a PQ signal of 0.5 mean?

About 92 cd/m², on any display that can show it.

## Why is HLG's system gamma 1.2?

That is its value for a 1,000-nit display under BT.2100: γ = 1.2 + 0.42 × log10(L_W ÷ 1000). It rises for brighter displays and falls for dimmer ones.

## Are the dim and bright surround settings standard?

No. The multipliers 0.95 and 0.90 are this tool's own. Readings made with them are marked Adjusted.

## Why can't the tool tell me the peak brightness of my image?

An ordinary 8-bit PNG or JPEG stores code values with no record of the light they stood for. Absolute luminance needs an HDR format with PQ or HLG and mastering metadata, or a format such as OpenEXR, which the tool does not read.

## Why do ICtCp and Jzazbz use different quantisers?

ICtCp uses ST 2084 as written. Jzazbz's authors raised the curve's exponent by a factor of 1.7 (p = 134.034375). The tool runs each with its own.

## Is the "ACES Filmic" operator the Academy's transform?

No. It is Krzysztof Narkowicz's 2016 curve fit that approximates the look of the ACES output transforms. The Reference section says so.

## Why 33.6%, 45.6% and 63.6% rather than the usual figures?

They are shares of the spectral locus the tool draws (the CIE 1931 2° locus, 65 points from 380 to 700 nm). Commonly quoted figures use a smaller locus area.

## Does it work with HDR displays?

The tool draws its charts in standard sRGB, so it does not need an HDR display. It explains HDR numerically rather than showing HDR images.
