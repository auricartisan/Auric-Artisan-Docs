---
title: Auric Artisan Icon Studio — Reference
description: Every command, keybinding, setting, collection, style, output format, view and control in Auric Artisan Icon Studio 0.1.0.
product: VS Code extensions › Auric Artisan Icon Studio
updated: 2026-09-25
---

# Icon Studio reference

This reference describes version 0.1.0 as published on the Visual Studio Marketplace.

## Commands

Category in the Command Palette: **Auric Icon Studio**.

| Command | ID | What it does |
| --- | --- | --- |
| Open Icon Studio | `auricIconStudio.openStudio` | Opens the editor-tab Studio beside the active editor, or reveals it and focuses search. |
| Search All Icons… | `auricIconStudio.searchIcons` | Quick Pick over the whole catalog, then an action list. |
| Smart Insert Icon (matches active language) | `auricIconStudio.smartInsert` | Quick Pick, then insert with smart output. |
| Copy Icon As… | `auricIconStudio.copyAs` | Quick Pick, then a format list; copies. |
| Save Icon as SVG… | `auricIconStudio.saveSvg` | Quick Pick of SVG icons; saves through a dialog. |
| Insert from Likes | `auricIconStudio.insertFavorite` | Quick Pick of liked icons; runs the click action. |
| Insert from Recent | `auricIconStudio.insertRecent` | Quick Pick of recent icons; runs the click action. |
| Clear Likes, Recents and Learned Recommendations | `auricIconStudio.clearPersonalization` | Asks for confirmation, then resets personalisation. |
| Insert Icon by ID | `auricIconStudio.insertIcon` | Inserts a given icon; for keybindings and macros. Hidden from the Command Palette. |

## Keybindings

| Keys (Windows and Linux) | Keys (macOS) | Command | When |
| --- | --- | --- | --- |
| `Ctrl` + `Alt` + `I` | `Cmd` + `Alt` + `I` | Smart Insert Icon | Editor has focus and Icon Studio's shortcuts are active. |
| `Ctrl` + `Alt` + `R` | `Cmd` + `Alt` + `R` | Insert from Recent | Editor has focus and Icon Studio's shortcuts are active. |

Icon Studio's shortcuts are active when it hosts the Auric collections (the default) or when none of Modern, Drawn and Playful is installed.

### Keys inside Icon Studio

| Key | Action |
| --- | --- |
| `/` | Focus and select the search box. |
| `Escape` | In search: clear it. In an open dropdown: close it and return focus. |
| `Arrow Up`, `Arrow Down` | Open a dropdown from its button; move between options. |
| `Home`, `End` | First or last dropdown option. |
| `Tab` | Closes open dropdowns. |

## Settings

| Setting | Type | Values or range | Default | What it does |
| --- | --- | --- | --- | --- |
| `auricIconStudio.clickAction` | string | `insert`, `copy`, `insertAndCopy` | `insert` | Action when you choose an icon from a Quick Pick (Likes, Recent). |
| `auricIconStudio.smartInsert` | boolean | `true`, `false` | `true` | Language-aware output for Insert. |
| `auricIconStudio.size` | number | 0 to 512 | 0 | Width and height in SVG and font output; 0 keeps the native size. |
| `auricIconStudio.color` | string | `currentColor` or `#rrggbb` | `currentColor` | Colour for monochrome output. |
| `auricIconStudio.strokeWidth` | number | 0.5 to 4 | 2 | Stroke width for Tabler, Lucide and Feather. |
| `auricIconStudio.emojiSkinTone` | string | `none`, `light`, `mediumLight`, `medium`, `mediumDark`, `dark` | `none` | Default emoji skin tone. |
| `auricIconStudio.density` | string | `comfortable`, `compact` | `comfortable` | Card size in the grid. |
| `auricIconStudio.pageSize` | number | 24 to 240 | 96 | Cards loaded per batch as you scroll. |
| `auricIconStudio.recommendations.enabled` | boolean | `true`, `false` | `true` | The **For you** view and Quick Pick recommendations. |
| `auricIconStudio.hoverPreview` | boolean | `true`, `false` | `true` | Previews for Auric icon IDs in code. |
| `auricIconStudio.hostFamilyLibraries` | boolean | `true`, `false` | `true` | Hide the separate Modern, Drawn and Playful library views while Icon Studio is installed. |

Search Settings for `@ext:auric-artisan.auric-artisan-icon-studio` to see them all.

## Views and menus

| Place | Contents |
| --- | --- |
| Activity Bar | **Icon Studio** container with the **Icon Studio** view. |
| View title bar | **Open Icon Studio**, **Search All Icons…**, **Insert from Likes**; in the **…** menu, **Clear Likes, Recents and Learned Recommendations**. |
| Editor right-click menu | **Smart Insert Icon (matches active language)** (writable editors only). |
| Editor tab | "Icon Studio", opened beside the active editor. |

## Studio controls

| Control | Options or behaviour |
| --- | --- |
| View chips | **Library**, **For you**, **Likes** (count), **Recent** (count). |
| Search your library | Synonym-aware search; `/` to focus; `Escape` to clear. |
| Refine library | Collapsed in the sidebar, open in the editor tab. |
| Collection | **All collections** or one of 11. |
| Category | **All categories** or one category. |
| Style | Shown for a single multi-style collection; **Default** or a style. |
| Skin tone | Shown for all collections or Emoji; six tones. |
| Reset filters | Clears search and refinements; keeps the current view. |
| Card | Artwork (inserts), heart (like), badge, name, category, **Insert**, **Copy**, **As…**, quick formats. |
| Load more | Shown only if automatic loading is unavailable. |

## Collections

| ID | Collection | Group | Entries | Styles (ID: label) | Default style | Licence |
| --- | --- | --- | --- | --- | --- | --- |
| `modern` | Modern | Auric Artisan | 720 | color, mono, outline, duotone | color | Auric Artisan Free Use Licence |
| `drawn` | Drawn | Auric Artisan | 480 | color, mono, outline, duotone | color | Auric Artisan Free Use Licence |
| `playful` | Playful | Auric Artisan | 1,225 | color, outline, filled, small | color | Auric Artisan Free Use Licence |
| `emoji` | Emoji | Emoji | 1,914 | none plus five tones | none | MIT (data); glyphs drawn by your system |
| `phosphor` | Phosphor | Open source | 1,512 | thin, light, regular, bold, fill, duotone | regular | MIT |
| `tabler` | Tabler | Open source | 5,093 | outline, filled | outline | MIT |
| `lucide` | Lucide | Open source | 1,714 | regular | regular | ISC |
| `remix` | Remix | Open source | 1,689 | line, fill | line | Remix v1.0 |
| `heroicons` | Heroicons | Open source | 324 | 24/outline, 24/solid, 20/solid, 16/solid | 24/outline | MIT |
| `feather` | Feather | Open source | 287 | regular | regular | MIT |
| `material` | Material | Open source | 2,276 | outlined, round, sharp, regular, twotone | outlined | Apache-2.0 |

Total: 17,234 entries.

## Output formats

| Kind | Format ID | Label |
| --- | --- | --- |
| SVG | `raw` | SVG markup (plain format) |
| SVG | `jsx` | JSX element |
| SVG | `jsxComponent` | React component |
| SVG | `js` | JavaScript string constant |
| SVG | `img` | Image tag (self-contained) |
| SVG | `markdown` | Markdown image |
| SVG | `css` | CSS background |
| SVG | `dataUri` | Data URI |
| SVG | `name` | Icon ID |
| Material | `html` | HTML span (plain format) |
| Material | `jsx` | JSX span |
| Material | `jsxComponent` | React component |
| Material | `js` | JavaScript string constant |
| Material | `css` | CSS declarations |
| Material | `name` | Ligature name |
| Emoji | `emoji` | Emoji character (plain format) |
| Emoji | `shortcode` | Shortcode |
| Emoji | `unicode` | Unicode code points |
| Emoji | `html` | HTML entities |

## Smart insert by language

| Language IDs | SVG output | Material output |
| --- | --- | --- |
| `javascriptreact`, `typescriptreact`, `mdx` | JSX element | JSX span |
| `javascript`, `typescript` | JavaScript string constant | JavaScript string constant |
| `html`, `vue`, `svelte`, `astro`, `php`, `handlebars`, `razor`, `erb`, `django-html`, `jinja`, `blade`, `xml`, `svg` | SVG markup | HTML span |
| `markdown` | Markdown image | HTML span |
| `css`, `scss`, `sass`, `less`, `stylus`, `postcss` | CSS background | CSS declarations |
| `json`, `jsonc`, `yaml`, `toml`, `python` | Data URI | HTML span |
| Anything else | SVG markup | HTML span |

Emoji always insert as the character.

## Limits

| Item | Limit |
| --- | --- |
| Recent icons kept | 60 |
| Liked icons kept | 500 |
| For you view | Up to 96 icons |
| Quick Pick results | 200 with a search term; 300 without |
| Hover preview size | 48 pixels |

## Messages you may see

| Message | Meaning |
| --- | --- |
| … copied — open an editor to insert it. | No editor was available, so the output was copied. |
| … is an emoji character and has no SVG file to save. | Only SVG artwork can be saved. |
| … is a font glyph and has no SVG file to save. | Material icons cannot be saved as SVG. |
| Icon Studio: like an icon first — press the heart on any card. | **Insert from Likes** found no likes. |
| Icon Studio: no recent icons yet. | **Insert from Recent** found no recent icons. |
| Icon Studio: unknown icon id … | **Insert Icon by ID** received an ID that is not in the catalog. |
| VS Code could not apply the edit. | The editor rejected the insertion, for example because it is read-only. |
