---
title: Auric Color — Picker modes
description: Choose between the Auric picker and VS Code's native colour picker, and learn exactly which VS Code settings each mode changes.
product: VS Code extensions › Auric Artisan Studio › Auric Color
updated: 2026-09-25
---

# Picker modes

VS Code has its own colour picker: in CSS (and in other languages when an extension provides colours) it draws small **colour decorators** before colour values and opens a draggable picker when you hover or click them. VS Code offers no way for an extension to replace that picker, so two pickers would stack on top of each other. Auric Color solves this with a **picker mode**.

## The three set-ups

| Set-up | How to get it | Swatches | Clicking a colour | Hover |
| --- | --- | --- | --- | --- |
| **Auric picker** (default) | `colorPicker.mode` = `auric`, `colorPicker.nativeHoverPicker` = `false` | Auric's swatches | Auric's inline picker in the hover (or per `colorPicker.clickAction`) | Full Auric hover with Spectrum, Hue and Alpha rows |
| **Auric with VS Code's sliders** | `colorPicker.mode` = `auric`, `colorPicker.nativeHoverPicker` = `true` | VS Code's decorators | The hover, per `colorPicker.clickAction` | VS Code's draggable picker above Auric's readouts (no Spectrum, Hue or Alpha rows) |
| **VS Code native picker** | `colorPicker.mode` = `decorators` | VS Code's decorators | VS Code's picker | Auric's readouts with only **Shades** and **Brand** rows |

In the last two set-ups Auric Color supplies the colours it detects to VS Code's picker in non-CSS languages too, so VS Code's picker also works in JavaScript, TypeScript, HTML, Vue, Svelte, JSON, Markdown and the other supported languages. VS Code's picker then offers the colour in hex, `rgb()`, `hsl()`, `hwb()`, `oklch()`, `oklab()`, `lch()`, `lab()` and `color(display-p3 …)`, starting with the token's own format.

## What Auric mode changes in your settings

> **Important:** In the default **Auric picker** set-up, Auric Color sets VS Code's `editor.colorDecorators` setting to `false` in your **user** settings, and also overrides a workspace or folder value that says otherwise. It does this when it starts, and again whenever the setting is switched back on while Auric mode is active (for example by Settings Sync or another extension), when you switch editors, and when the VS Code window regains focus.

This turns off VS Code's decorators in every language, for every workspace, while Auric Color is installed in this mode. Only Auric Color touches this setting; the other Studio extensions never do.

If you uninstall Auric Color, `editor.colorDecorators` stays `false`. Before uninstalling, run **Restore native color picker (use VS Code's)**, or afterwards set `"editor.colorDecorators": true` in your settings.

## Switch mode

### Choose Color Picker Mode

1. Run **Auric Artisan: Choose Color Picker Mode** (also on the editor's right-click menu, and **Picker mode** in the colour hover).
2. The list **Auric Artisan color picker mode** offers:
   - **Auric picker (default)**: Auric's own inline picker in the hover plus accessibility tools; VS Code's colour decorators turn off.
   - **VS Code native picker**: keeps `editor.colorDecorators` on so clicking a colour opens VS Code's draggable picker, with Auric's hover, scan, contrast and accessibility tools on top.
3. Your choice is saved to your user settings: `colorPicker.mode`, `colorPicker.swatches` and `colorPicker.inlineSwatches` are set to match, and `editor.colorDecorators` is switched off or on.

A message confirms the result:

| Result | Message |
| --- | --- |
| Auric picker | **Auric Artisan: using the Auric spectrum picker. VS Code Color Decorators are off.** |
| Auric with VS Code's sliders | **Auric Artisan: hover any color for the draggable picker plus Auric's accessibility tools.** |
| VS Code native picker | **Auric Artisan: using VS Code Color Decorators with Auric hover, scan, and contrast tools.** |

### One-step commands

| Command | What it sets |
| --- | --- |
| **Disable native color picker (use Auric Artisan)** | `nativeHoverPicker` off, Auric mode, VS Code's decorators off |
| **Restore native color picker (use VS Code's)** | `nativeHoverPicker` on, native mode, VS Code's decorators on; also stops the first-pick question below |

### The first-pick question

If VS Code's decorators are on when you first run **Pick / edit color** in Auric mode, Auric Color asks **Auric Artisan can replace VS Code's native color picker with its own. Turn off the native color decorators?**

| Answer | Result |
| --- | --- |
| **Use Auric Artisan picker** | Switches to the Auric picker set-up |
| **Keep native** | Switches to the VS Code native picker set-up |
| **Don't ask again** | Changes nothing and does not ask again |

The question is asked only once.

## Click behaviour in Auric mode

`auricColor.colorPicker.clickAction` controls what a mouse click on a colour literal does (keyboard cursor moves never trigger it):

| Value | Studio label | Click does |
| --- | --- | --- |
| `inlinePicker` (default) | Inline hover picker | Shows the hover with the inline picker |
| `fullEditor` | Spectrum picker panel | Opens the picker panel beside the editor (or updates the docked picker when it is open) |
| `off` | Click disabled | Only moves the cursor |

You can also set this in Studio › Settings › **Color picker**. The older setting `colorPicker.autoOpen` still works: when it is `true` and `clickAction` has never been set, clicks open the picker panel. Prefer `clickAction`.

## Related

- [The colour pickers](color-picker.md)
- [Hover and swatches](hover-and-swatches.md)
- [Troubleshooting](troubleshooting.md)
