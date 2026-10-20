---
title: Auric Artisan Icon Studio — Insert, copy and save
description: Insert icons with smart, language-aware output, copy them in an explicit format, save SVG files and preview Auric icon IDs on hover.
product: VS Code extensions › Auric Artisan Icon Studio
updated: 2026-09-25
---

# Insert, copy and save

Every card has three main actions and three quick format buttons.

| Button | What it does |
| --- | --- |
| **Insert** (or select the artwork) | Inserts into the editor. With smart insert on, the format follows the file's language. |
| **Copy** | Copies the plain format: SVG markup for SVG artwork, an HTML span for Material, the character for emoji. |
| **As…** | Opens a list of every format for that icon; the plain format is marked **default**. |
| Quick buttons | SVG artwork: **JSX**, **URI** (data URI), **CSS**. Material: **JSX**, **CSS**, **HTML**. Emoji: **Code** (shortcode), **U+** (code points), **HTML** (entities). |

After each action, a status message confirms what happened, for example "Rocket copied as data uri."

## Insert into your file

1. Open a writable file and place one or more cursors, or select text to replace.
2. In Icon Studio, select **Insert** on a card.
3. The output is inserted at every cursor. Selected text is replaced. If the output has several lines, each continuation line gets the same indentation as the cursor's line.

Icon Studio inserts into the active editor or, if you clicked into the Studio, the last text editor you used. If no editor is available, the output is copied instead.

### Smart insert

Smart insert is on by default (`auricIconStudio.smartInsert`). It picks the format from the editor's language:

| Editing in | SVG artwork becomes |
| --- | --- |
| React JSX or TSX, MDX | A JSX element |
| JavaScript, TypeScript | A JavaScript string constant |
| HTML, Vue, Svelte, Astro, PHP, Handlebars, Razor, ERB, Django templates, Jinja, Blade, XML, SVG | SVG markup |
| CSS, SCSS, Sass, Less, Stylus, PostCSS | A CSS background |
| Markdown | A Markdown image |
| JSON, JSONC, YAML, TOML, Python | A data URI |
| Any other language | SVG markup |

- **Material** glyphs become a JSX span in React, a string constant in JavaScript or TypeScript, CSS declarations in stylesheets, and an HTML span elsewhere.
- **Emoji** are always inserted as the character.

Turn smart insert off to always insert the plain format. The **Smart Insert Icon** command always uses smart output.

> **Note:** Smart insert chooses a format. It does not configure your application or guarantee valid syntax at every cursor position. Check quotes, surrounding code and accessibility labels.

## Copy in an explicit format

1. Select **As…** on a card, or run **Auric Icon Studio: Copy Icon As…**.
2. Choose a format from the list.

| Icon type | Formats |
| --- | --- |
| SVG artwork | SVG markup, JSX element, React component, JavaScript string constant, Image tag (self-contained), Markdown image, CSS background, Data URI, Icon ID |
| Material glyph | HTML span, JSX span, React component, JavaScript string constant, CSS declarations, Ligature name |
| Emoji | Emoji character, Shortcode, Unicode code points, HTML entities |

Material icons never export as SVG. Material markup needs the matching Material font in your application; the Studio's preview font is not added to your project.

## Control the output

These settings shape SVG and font output:

| Setting | Effect |
| --- | --- |
| `auricIconStudio.size` | Width and height written into the output. `0` (default) keeps the native size: 64 for Auric artwork, 24 for most open-source sets. Range 0 to 512. |
| `auricIconStudio.color` | `currentColor` (default, follows the text colour where it is used) or a six-digit hex colour for monochrome output. |
| `auricIconStudio.strokeWidth` | Stroke width for stroke-based sets (Tabler, Lucide, Feather). Auric artwork keeps its drawn strokes. Range 0.5 to 4, default 2. |
| `auricIconStudio.emojiSkinTone` | Default skin tone for emoji that support one. |

SVG output gets `role="img"` and an `aria-label` with the icon name when the artwork has no accessible name of its own. Review the label and change it if the icon is decorative or needs a better description.

## Save an SVG file

1. Run **Auric Icon Studio: Save Icon as SVG…** and choose an icon, or choose **Save as SVG…** in the **Search All Icons…** action list.
2. A save dialog opens with the name `<icon-id>.svg` in your first workspace folder (or your home folder).
3. Choose a location and select **Save icon**.

Only SVG artwork can be saved. Emoji are characters and Material icons are font glyphs, so they have no SVG file to save.

## Hover previews in code

Hover over a recognised Auric icon ID, such as `files-blank-document-drawn-0001`, in any file. The hover shows a 48-pixel preview, the icon name and description, its ID, collection and category, and an **Open in Icon Studio** link.

- If the Auric extension that owns that collection (Modern, Drawn or Playful) is installed, Icon Studio leaves the hover to it, so you never see two previews.
- A hover only previews; it never changes your file.
- Turn previews off with `auricIconStudio.hoverPreview`.

## Result

The icon is in your file (or on your clipboard, or saved as an `.svg` file) in the format you need, and it appears under **Recent**.
