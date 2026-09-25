---
title: LUT Lab — LUT concepts
description: What a lookup table is, 1D and 3D LUTs, grid sizes, domains, sample order, interpolation, clipping and 8-bit precision.
product: Website › Tools › Image and file tools › LUT Lab
updated: 2026-09-25
---

# LUT concepts

This page explains the ideas behind LUT Lab's controls and figures.

## What a LUT is

A lookup table (LUT) is a list that says, for a set of input colours, what each should become. Software applies it to every pixel of an image or video. Because it is just a table of numbers, a LUT carries a look or a conversion from one program to another without carrying the program's settings.

A LUT does not know what the colours mean. It works on whatever numbers it is given, so a LUT made for one kind of footage gives the wrong result on another. LUT Lab applies LUTs to ordinary 8-bit sRGB values, the kind of colour a web page or a JPEG holds.

## 1D and 3D LUTs

| | 1D LUT | 3D LUT |
|---|---|---|
| What it maps | Each channel on its own: red in to red out, green to green, blue to blue | Every combination of red, green and blue to a new colour |
| Can express | Brightness, contrast, gamma, per-channel curves, colour casts that depend only on each channel | Anything a 1D can, plus hue shifts, saturation changes and effects that mix channels |
| Size | N rows, each holding a red, green and blue output | N × N × N rows |
| Keyword in `.cube` | `LUT_1D_SIZE` | `LUT_3D_SIZE` |

A 3D LUT of size N is a cube of N points along each axis. The number of rows grows quickly:

| Size | Rows in a 3D LUT |
|---|---|
| 17 | 4,913 |
| 33 | 35,937 |
| 65 | 274,625 |

Bigger cubes follow a curved transform more closely and make larger files. 17, 33 and 65 are the customary sizes.

## The domain

A `.cube` may declare the range of input values its table covers with `DOMAIN_MIN` and `DOMAIN_MAX`. Without them, the domain is 0 to 1 on every channel.

LUT Lab's input is always an 8-bit sRGB pixel, which spans exactly 0 to 1. If a file declares a wider domain, for example 0 to 4 for high-dynamic-range footage, only part of its table can be reached from here. LUT Lab tells you what share is reachable, for example **reachable 25.0%**, and adds a note to the file card.

## Sample order

A 3D `.cube` lists its rows with the red index changing fastest, then green, then blue. The first rows are red 0, 1, 2… at green 0 and blue 0. A program that reads or writes the order the other way round swaps the red and blue axes, which gives a plausible-looking but wrong result. LUT Lab reads and writes red fastest, as the format requires, and the **Method** tab shows the first eight rows of a 2 × 2 × 2 table in order.

## Interpolation

An input colour rarely lands exactly on a grid point. For a 3D LUT, LUT Lab finds the small cube of eight grid points around the input and blends them, first along red, then green, then blue. This is trilinear interpolation. For a 1D LUT, it blends the two neighbouring rows of each channel. An input exactly on a grid point reads that point.

A straight-line transform, such as an identity (a LUT that changes nothing), is reproduced exactly at any size. Curves are only approximated between grid points, which is why larger cubes are more faithful to curved looks.

## Clipping

A pixel is **clipped** when the transform drives one of its channels to 0 or 255 that was not already there. Clipping loses detail: highlights driven to white can no longer be told apart, and neither can shadows driven to black.

This is different from asking whether an output channel is at 0 or 255. A pure red pixel has green and blue at 0 before any transform, so it is not a casualty when a transform leaves it alone. LUT Lab's clip figure counts only pixels the transform actually pushed to an end.

## 8-bit precision

LUT Lab reads pixels from, and draws them to, a canvas at 8 bits per channel: 256 levels, from 0 to 255. Every value it writes into a `.cube` is therefore one of 256 levels divided by 255, written to the six decimal places the format uses. The file's header says so, because a `.cube` has no field of its own for precision, and a table written from 8 bits otherwise looks the same as one written from 32.

### When grid points land on 8-bit values

A 3D grid of size N has points at 0, 1/(N−1), 2/(N−1) … 1. These land exactly on 8-bit values only when N−1 divides 255. Within the sizes LUT Lab writes, that is true for 2, 4, 6, 16, 18 and 52, and not for the customary 17, 33 and 65. At the other sizes, each grid point is written to the nearest 8-bit value, up to half a step away. An 8-bit image put through the file is unchanged by this; an application reading the file at higher precision sees the small gap.

## Stylisations and transforms

LUT Lab separates two kinds of look:

- A **stylisation** is a curve someone designed because it looks good. It has no definition to check against. Five of the built-in looks are stylisations.
- A **transform** claims to convert between two defined things and can be checked against its definition. The Reinhard tone-map is the one built-in transform.

## Measuring colour difference

LUT Lab measures how far a transform moved each colour with CIEDE2000 (ΔE₀₀), the CIE's standard formula for colour difference, computed in CIELAB with a D65 white. Zero means no change, and larger numbers mean larger visible changes.
