---
title: Auric Color — Picker, palettes and contrast for VS Code
description: What Auric Color does, who it is for, how to install it, and a quick start from hover to fix.
product: VS Code extensions › Auric Artisan Studio › Auric Color
updated: 2026-09-25
---

# Auric Color — Picker, Palettes & Contrast

Auric Color turns every colour literal in your code into something you can read, understand and fix in place. Hover a colour such as `#1d4ed8`, `rgb(29 78 216)` or `oklch(0.49 0.22 264)` to see its RGB, HSL, OKLCH and Display-P3 values, its nearest CSS colour name, its contrast on white and black, and how it looks to people with colour-vision deficiency. The hover is also a picker: select a tile to change the colour, keeping the token's own syntax.

It also watches your stylesheets, markup and components for text that is too faint to read. Failing text and background pairs are underlined as you type, with a one-click fix to the nearest passing colour of the same hue, and a Contrast Studio for tuning a pair and writing the fix back to the design token it comes from. The Studio adds generators for accessible palettes, OKLCH shade scales, colour-vision previews and a brand audit on real text.

Auric Color is one of the four Auric Artisan Studio extensions. It works on its own, and joins the others in one Workstation when they are installed together. Everything runs on your machine.

## Who it is for

- Front-end developers who edit colours in CSS, Sass, CSS-in-JS, Tailwind configs or component files.
- Designers and design-system maintainers who manage colour tokens and brand palettes in code.
- Developers in any language who keep colours in code, configuration or data files: Python, Go, Rust, Java, C#, Swift, Kotlin, Dart, YAML, TOML and more than 40 others.

## Where to find it

- Marketplace ID: `auric-artisan.auric-color`
- Marketplace page: https://marketplace.visualstudio.com/items?itemName=auric-artisan.auric-color
- Install: `code --install-extension auric-artisan.auric-color`
- Version 0.1.0; VS Code 1.74 or newer. Also installed by the [Full Pack](../full-pack/README.md).

## Quick start

1. Install Auric Color from the Extensions view (`Ctrl` + `Shift` + `X`).
2. Open a stylesheet or component with colours in it. A small swatch appears before each colour literal.
3. Hover a colour. Read its values, contrast on white and black, and colour-vision preview.
4. Select a tile in the hover's **Spectrum**, **Hue**, **Alpha**, **Shades**, **Fix**, **Brand** or **Recent** rows. The colour in your code changes, in its own format, and the hover reopens on the new value.
5. Press `Ctrl` + `Alt` + `C` (`Cmd` + `Alt` + `C` on macOS) with the cursor on a colour to open the full picker beside the editor, with contrast checks, generators and an eyedropper.
6. Look for violet wavy underlines on text colours. Hover one and select **Apply fix** to reach the contrast target.
7. Run **Auric Artisan: Open Color Studio** to generate a palette, a shade scale or a colour-vision preview.

The first time you pick a colour, Auric Color may ask whether to replace VS Code's own colour picker. See [Picker modes](docs/picker-modes.md) before you answer.

## What you can do

- Read any colour's values, name, contrast and colour-vision preview in a hover, in more than 40 languages.
- Edit colours with an inline picker in the hover, a full spectrum picker beside the editor, or a picker docked in the sidebar, with HEX, RGB, HSL, HSV, OKLCH and LCH inputs and an eyedropper.
- Rewrite every occurrence of a colour in a file at once, each keeping its own format.
- Catch low-contrast text in CSS, Sass, Less, Stylus, HTML, Vue, Svelte, Astro, PHP, JSX, TSX, CSS-in-JS and Markdown, including colours from CSS custom properties and dark themes.
- Fix a pair with one click, or every failing pair in a file with one undoable edit after a preview.
- Flag pairs that pass for typical vision but weaken under colour-vision deficiency.
- Switch between WCAG 2.x ratios, APCA or both.
- Generate harmony palettes that meet a contrast target, OKLCH shade scales from 50 to 950, and export them as CSS, JSON or Tailwind.
- Preview any colour, and your project's palette, under eight kinds of colour-vision deficiency.
- Audit a brand's roles (background, surface, text, links, buttons, borders) on real text and export accessible tokens.
- Mark deliberate brand colours as intentional branding.
- Re-theme the Studio with 13 accent presets or any colour.

## In this folder

| Folder or file | What it covers |
| --- | --- |
| [docs/](docs/README.md) | Guides and reference for Auric Color. |
| [docs/getting-started.md](docs/getting-started.md) | First run and a tour of what Auric Color adds. |
| [docs/hover-and-swatches.md](docs/hover-and-swatches.md) | The colour hover, swatches and supported languages and formats. |
| [docs/color-picker.md](docs/color-picker.md) | The inline, panel and docked pickers. |
| [docs/picker-modes.md](docs/picker-modes.md) | Auric picker versus VS Code's native picker, and what each changes. |
| [docs/contrast-diagnostics.md](docs/contrast-diagnostics.md) | Contrast underlines, hovers, quick fixes and Fix All. |
| [docs/palettes-and-shades.md](docs/palettes-and-shades.md) | The Palette and Shades tools and their exports. |
| [docs/colour-vision.md](docs/colour-vision.md) | The Vision tool and colour-vision checks. |
| [docs/brand-audit.md](docs/brand-audit.md) | The Brand tool and the brand rulebook. |
| [docs/reference.md](docs/reference.md) | Every command, keybinding, setting, view and menu. |
| [docs/troubleshooting.md](docs/troubleshooting.md) | Symptoms and fixes. |
| [docs/faq.md](docs/faq.md) | Short answers. |
| [others/](others/README.md) | Glossary, shortcuts, limits and accuracy, related pages, release notes and privacy. |

Shared Studio features, such as the Command Center, the Contrast Studio and scanning, are in the [Studio docs](../docs/README.md).

Back to the [Studio overview](../README.md).
