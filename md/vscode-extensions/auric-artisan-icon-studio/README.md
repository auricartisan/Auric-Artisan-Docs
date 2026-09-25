---
title: Auric Artisan Icon Studio — Overview
description: What Auric Artisan Icon Studio is, who it is for, how to install it and where to find each guide.
product: VS Code extensions › Auric Artisan Icon Studio
updated: 2026-09-25
---

# Auric Artisan Icon Studio

Auric Artisan Icon Studio is one offline workspace in VS Code for finding icons and emoji and putting them into your code. It bundles every Auric Artisan icon collection (Modern, Drawn and Playful), 1,914 emoji and seven open-source icon sets: Phosphor, Tabler, Lucide, Remix, Heroicons, Feather and Material. In total it searches 17,234 catalog entries in 11 collections.

You can browse in a compact sidebar or open a larger editor-tab Studio. Search understands names, tags and synonyms (for example, `delete` finds trash icons), and Hindi search aliases. **Smart insert** chooses an output format from the file you are editing: a JSX element in React, a string constant in JavaScript, markup in HTML, a CSS background in stylesheets, a Markdown image in Markdown, and a data URI in JSON, YAML or Python. You can also copy an icon in an explicit format or save SVG artwork to a file.

Icon Studio does not change your Explorer file and folder icons; that is the job of [Auric Artisan File Icons](../auric-artisan-file-icons/README.md). It also includes all the Auric artwork itself, so you do not need to install the individual Auric collection extensions.

## Who it is for

- Front-end and full-stack developers who insert icons into components, pages, stylesheets or documentation.
- Designers who want to compare icon styles across many sets in one place.
- Anyone who wants emoji with skin tones, shortcodes and code points without leaving the editor.
- Teams that need a tool that works fully offline, with no account or telemetry.

## Where to find it

| Item | Value |
| --- | --- |
| Marketplace listing | https://marketplace.visualstudio.com/items?itemName=auric-artisan.auric-artisan-icon-studio |
| Extension ID | `auric-artisan.auric-artisan-icon-studio` |
| Current version | 0.1.0 |
| Requires | Visual Studio Code 1.85 or later |
| Price | Free to install and use |

```text
code --install-extension auric-artisan.auric-artisan-icon-studio
```

## Quick start

1. Install the extension.
2. Open the file you want to add an icon to and place the cursor where it should go.
3. Select **Icon Studio** in the Activity Bar.
4. Type a word into **Search your library**, for example `rocket`.
5. Optionally expand **Refine library** and pick a **Collection**, **Category** or **Style**.
6. Select **Insert** on a card. The icon is inserted in a format that suits the file.
7. Press the heart on icons you reuse so they appear under **Likes**.

## What you can do

- Search 17,234 entries across 11 collections, with synonyms and Hindi aliases.
- Filter by collection, category, style and emoji skin tone.
- Keep **Likes** and **Recent** icons, and get **For you** recommendations based on the file you are editing.
- Insert at multiple cursors, with continuation lines indented to match.
- Copy SVG artwork as SVG markup, JSX, a React component, a JavaScript string constant, a self-contained image tag, a Markdown image, CSS, a data URI or the icon ID.
- Copy Material glyphs as HTML or JSX spans, a React component, a string constant, CSS or the ligature name.
- Copy emoji as the character, a shortcode, Unicode code points or HTML entities.
- Save SVG artwork to a file.
- Preview Auric icon IDs by hovering over them in code.
- Insert a specific icon from a keybinding or macro.
- Show one Icon Studio instead of separate libraries when the Auric Modern, Drawn or Playful extensions are also installed.

## In this folder

### docs/

- [Contents of docs/](docs/README.md)
- [Getting started](docs/getting-started.md)
- [Search and browse](docs/search-and-browse.md)
- [Insert, copy and save](docs/insert-copy-and-save.md)
- [Use the Command Palette and keybindings](docs/commands-and-keybindings.md)
- [Work with the Auric collection extensions](docs/auric-collections.md)
- [Reference](docs/reference.md)
- [Troubleshooting](docs/troubleshooting.md)
- [FAQ](docs/faq.md)

### others/

- [Contents of others/](others/README.md)
- [Glossary](others/glossary.md)
- [Shortcuts and commands](others/shortcuts.md)
- [Limits and accuracy](others/limits-and-accuracy.md)
- [Related extensions and comparison](others/related.md)
- [Release notes](others/release-notes.md)
- [Privacy](others/privacy.md)
