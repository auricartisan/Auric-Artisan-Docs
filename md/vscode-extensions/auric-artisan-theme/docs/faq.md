---
title: Auric Artisan Theme — FAQ
description: Short answers to common questions about Auric Artisan Theme and Theme Studio.
product: VS Code extensions › Auric Artisan Theme
updated: 2026-09-25
---

# Frequently asked questions

## Is the theme free?

Yes. The extension is free to install and use.

## How many themes are there?

54: ten accents each for Obsidian, Midnight, Parchment and Porcelain, six each for Dusk and Forest, and two high-contrast builds. See [Choose a theme](choose-a-theme.md).

## Do I need Theme Studio to use the themes?

No. The themes work like any other VS Code colour theme. Theme Studio is optional.

## Does Theme Studio have a preview mode?

No. Every edit applies live. The Preview tab only compares palettes. Save a preset or export JSON before large experiments.

## Is there undo?

There is no undo history. Use the per-dial and per-slot reset buttons, **Reset all**, or load a saved preset.

## Where are my changes stored?

Dials are VS Code user settings under `auricTheme.*`. Colour overrides and presets are stored by the extension on this machine. The extension also writes theme-scoped entries into VS Code's colour customisation settings so the changes show. See [Privacy](../others/privacy.md).

## Will my customisation sync to other machines?

Dials are ordinary settings, so they follow VS Code Settings Sync if you use it. Presets and colour overrides are local; move them with customisation JSON (see [Save, share and export](save-share-and-export.md)).

## Why did my accent colour get darker on a light theme?

On light themes the accent is darkened until it clears your minimum contrast. The brand gold, for example, is too light to read as text on the cream Parchment canvas.

## Does the theme affect other colour themes?

No. Customisations are scoped to the Auric theme names and do nothing when another theme is active. Unrelated theme blocks in your settings are left alone.

## What does "Surprise Me" change?

It clears your dials, then picks a random accent, syntax palette, surface warmth, separation, bracket style and tab style from curated choices. Your colour overrides are kept. Reset if you do not like the result.

## Can I use my customised theme without the extension?

Yes. Run **Export as Theme File…** to save a standalone VS Code colour theme JSON file.

## Can the interface be in Hindi?

Yes. Use the **Auto · English · हिन्दी** switch in Theme Studio or the sidebar. See [Interface language](interface-language.md).

## Does it work in remote, untrusted or virtual workspaces?

Yes. The extension declares support for untrusted and virtual workspaces.
