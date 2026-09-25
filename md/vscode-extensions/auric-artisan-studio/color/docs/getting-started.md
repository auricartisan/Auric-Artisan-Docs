---
title: Auric Color — Getting started
description: Install Auric Color, read and edit your first colour, fix your first contrast problem, and find every place Auric Color shows up.
product: VS Code extensions › Auric Artisan Studio › Auric Color
updated: 2026-09-25
---

# Getting started with Auric Color

## Install

1. Open the Extensions view (`Ctrl` + `Shift` + `X`).
2. Search for `auric-artisan.auric-color` and select **Install**. Or run `code --install-extension auric-artisan.auric-color`.

Auric Color starts when VS Code finishes loading. You need VS Code 1.74 or newer.

> **Important:** In its default mode, Auric Color replaces VS Code's own colour decorators (the small squares VS Code draws before colours in CSS) with its own swatches and picker. To do this it sets `editor.colorDecorators` to `false` in your user settings as soon as it starts, and sets it back to `false` if it is turned on again while this mode is active. To keep VS Code's own picker instead, run **Auric Artisan: Restore native color picker (use VS Code's)**. See [Picker modes](picker-modes.md).

## Read a colour

1. Open a file that contains a colour, such as a CSS file with `color: #1d4ed8;`.
2. A small swatch appears before the colour value, and the value gets a faint tinted outline.
3. Hover the value. The hover shows the colour's hex value, its nearest CSS name, its RGB, HSL, OKLCH and Display-P3 values, its contrast on white and on black, and how it looks with protanopia, deuteranopia and tritanopia.

See [Hover and swatches](hover-and-swatches.md) for every part of the hover.

## Change a colour

1. Hover the colour. The top of the hover is a picker: a **Spectrum** of shades at the colour's hue, a **Hue** strip, an **Alpha** strip, **Shades**, **Fix** (versions that pass AA and AAA on white and black), **Brand** and **Recent**.
2. Select any tile. The value in your file changes, written in the same format it was in (hex stays hex, `oklch()` stays `oklch()`), and the hover reopens on the new colour.
3. To type an exact value, select **Type exact…** at the top of the hover.
4. For the full picker, select **Spectrum picker**, or press `Ctrl` + `Alt` + `C` (`Cmd` + `Alt` + `C` on macOS) with the cursor on the colour.

See [The colour pickers](color-picker.md).

## Fix a contrast problem

1. In a stylesheet or component, a text colour that is too faint for its background gets a violet wavy underline.
2. Hover it. The card leads with the verdict, for example `2.32 : 1 — fails WCAG AA for normal text`, then shows the nearest passing colour of the same hue.
3. Select **Apply fix**, or press `Ctrl` + `.` and choose **Fix contrast → #767676 (4.54:1)**.

To fix every failing pair in the file, run **Auric Artisan: Fix All Contrast Issues in File**. See [Contrast diagnostics](contrast-diagnostics.md).

## Where Auric Color appears

| Place | What you get |
| --- | --- |
| Editor | Swatches, colour hovers with a picker, contrast underlines, quick fixes |
| Activity Bar, **Auric Color** | **Overview** (the colour workbench) and a collapsed **Color Picker** view |
| Status bar | A score item, which shows a score once the Studio has graded the workspace; **Auric: N in this file** when the open file has contrast findings |
| Editor right-click menu | **Pick / edit color**, **Generate Accessible Palette** and **Check Contrast of Selection** (with a selection), **Choose Color Picker Mode**, **Mark Line as Intentional Branding (Toggle)** |
| Studio (**Auric Artisan: Open Color Studio**) | **Color** (Palette, Shades, Vision), **Check** (Contrast), **Brand** and **Settings** |
| Command Center (`Ctrl` + `Alt` + `.`) | Colour actions and your recent colours |

### The Overview (colour workbench)

The Overview shows the file you are editing and its findings, a suggestion when the file has two or more fixable pairs, a row of brand swatches, your recent colours, **Open the color picker**, and shortcuts to **Contrast**, **Palette**, **Shades**, **Vision**, **Rulebook** and **Icon Studio**. See [The Overview view](../../docs/overview-view.md#the-colour-workbench).

### The Studio

**Auric Artisan: Open Color Studio** opens the Studio on **Color › Palette**. The other spaces are **Check › Contrast** (the [Contrast Studio](../../docs/contrast-studio.md)), **Brand** and **Settings**. See [The Studio](../../docs/studio.md).

## With the other Studio extensions

When Auric Accessibility is installed too, it hosts the shared Workstation: Auric Color's own views are hidden and its tools appear in Auric Accessibility's sidebar and Studio. Auric Color still draws the swatches, colour hovers and pickers. Contrast underlines are then published by Auric Accessibility instead. See [The Workstation](../../docs/workstation.md).

## Next steps

- [Palettes and shades](palettes-and-shades.md)
- [Colour vision](colour-vision.md)
- [The brand audit](brand-audit.md)
- [Reference](reference.md)
