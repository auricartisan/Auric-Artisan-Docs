---
title: Auric Artisan Theme — Overview
description: What the Auric Artisan Theme extension for VS Code is, who it is for, how to install it and where to find each guide.
product: VS Code extensions › Auric Artisan Theme
updated: 2026-09-25
---

# Auric Artisan Theme

Auric Artisan Theme is a colour theme collection for Visual Studio Code. It ships 54 ready-made themes in six surface families (Obsidian, Midnight, Parchment, Porcelain, Dusk and Forest) plus two high-contrast builds, one dark and one light. Every theme is keyed to a single accent colour, so the whole workbench can be re-coloured in one step.

The extension also adds a live editor for the theme, called **Theme Studio**. Theme Studio has six tabs (**Looks**, **Dials**, **Colours**, **Audit**, **Share** and **Preview**). It gives you 11 complete looks, 37 theme dials and 107 individually editable colour slots. Every change applies to your editor straight away, and a contrast guard keeps text readable while you experiment.

A compact **Auric Theme** view in the Activity Bar gives you quick access to variants, accents, looks and the contrast status without opening the full Studio. Theme Studio and the sidebar can be shown in English or Hindi, independently of VS Code's own display language.

## Who it is for

- Developers who want a warm, carefully balanced theme that works in dark, light and high-contrast settings.
- Designers and front-end developers who want to tune an editor theme precisely, down to a single colour slot.
- Accessibility-minded users who want every text colour checked against WCAG contrast ratios and APCA values.
- Hindi-speaking users who prefer a Hindi interface in the Studio and sidebar.

## Where to find it

| Item | Value |
| --- | --- |
| Marketplace listing | https://marketplace.visualstudio.com/items?itemName=auric-artisan.auric-artisan-theme |
| Extension ID | `auric-artisan.auric-artisan-theme` |
| Current version | 0.2.0 |
| Requires | Visual Studio Code 1.75 or later |
| Price | Free to install and use |

Install from a terminal:

```text
code --install-extension auric-artisan.auric-artisan-theme
```

Or open the Extensions view (`Ctrl` + `Shift` + `X`), search for **Auric Artisan Theme** and select **Install**.

## Quick start

1. Install the extension.
2. Open the Command Palette (`Ctrl` + `Shift` + `P`) and run **Auric Theme: Switch Variant…**.
3. Pick a theme, for example **Auric Artisan — Obsidian Gold**. The editor changes immediately.
4. Run **Auric Theme: Open Theme Studio**, or press `Ctrl` + `Alt` + `;` (`Cmd` + `Alt` + `;` on macOS).
5. On the **Looks** tab, choose a starting look such as **Signature** or **Clarity**.
6. On the **Dials** tab, adjust the accent, surfaces, syntax palette and other dials. Changes apply live.
7. Open the **Audit** tab to check that every text colour still meets your contrast minimum.
8. On the **Share** tab, save a named preset so you can return to this set-up later.

## What you can do

- Choose from 54 themes: 10 accents each for Obsidian, Midnight, Parchment and Porcelain, 6 each for Dusk and Forest, and 2 high-contrast builds.
- Re-key the whole theme onto any of 17 accents, or onto a custom hex colour.
- Start from one of 11 looks, then layer 37 dials on top: surfaces, text, syntax palette, italics and bold, cursor, selection, brackets, indent guides, workbench bars, terminal palette, shadows, focus ring and accessibility guard.
- Override any of 107 colour slots with a custom colour picker (hex, saturation and brightness, hue, opacity and RGB channels).
- Audit 81 foreground and background pairs with WCAG ratios and APCA Lc values, in the Studio or as a plain-text contrast report.
- Compare the shipped palette with your current palette and copy the result as CSS custom properties.
- Save, load and delete named presets; copy or paste your customisation as JSON; export a standalone VS Code colour theme file.
- Switch the Studio and sidebar between **Auto**, **English** and **हिन्दी** without reloading.

## In this folder

### docs/

- [Contents of docs/](docs/README.md)
- [Getting started](docs/getting-started.md) — install, switch theme, the screen tour, your first customisation.
- [Choose a theme](docs/choose-a-theme.md) — the six families, the high-contrast builds and every way to switch.
- [Looks and dials](docs/looks-and-dials.md) — start from a look and tune the 37 dials.
- [Edit individual colours](docs/edit-colours.md) — the Colours tab and the colour picker.
- [Check contrast](docs/check-contrast.md) — the Audit tab, the contrast report and the contrast guard.
- [Compare and preview](docs/compare-and-preview.md) — the Preview tab and CSS export.
- [Save, share and export](docs/save-share-and-export.md) — presets, JSON customisation and theme files.
- [The Theme sidebar](docs/theme-sidebar.md) — the Activity Bar view in detail.
- [Interface language](docs/interface-language.md) — English and Hindi.
- [Reference](docs/reference.md) — every command, setting, keybinding, dial, slot and option.
- [Troubleshooting](docs/troubleshooting.md)
- [FAQ](docs/faq.md)

### others/

- [Contents of others/](others/README.md)
- [Glossary](others/glossary.md)
- [Shortcuts and commands](others/shortcuts.md)
- [Limits and accuracy](others/limits-and-accuracy.md)
- [Related tools and extensions](others/related.md)
- [Release notes](others/release-notes.md)
- [Privacy](others/privacy.md)
