---
title: Auric Artisan Theme — Reference
description: Every command, keybinding, setting, theme, look, accent, palette, colour slot and Theme Studio control in Auric Artisan Theme 0.2.0.
product: VS Code extensions › Auric Artisan Theme
updated: 2026-09-25
---

# Auric Artisan Theme reference

This reference describes version 0.2.0 as published on the Visual Studio Marketplace.

## Commands

All commands appear in the Command Palette under the category **Auric Theme**.

| Command | ID | What it does |
| --- | --- | --- |
| Open Theme Studio | `auricTheme.openStudio` | Opens (or reveals) the Auric Theme Studio editor tab. |
| Switch Variant… | `auricTheme.selectTheme` | Quick Pick of all 54 themes with polarity and canvas colour; sets VS Code's colour theme. |
| Cycle Variant | `auricTheme.cycleVariant` | Switches to the next of the 54 variants. |
| Choose Accent Colour… | `auricTheme.pickAccent` | Quick Pick of the 17 named accents; sets `auricTheme.accent.preset`. |
| Choose Look… | `auricTheme.pickLook` | Quick Pick of the 11 looks; applies the look. |
| Choose Syntax Palette… | `auricTheme.pickPalette` | Quick Pick of the 9 syntax palettes; sets `auricTheme.syntax.palette`. |
| Choose Interface Language… | `auricTheme.chooseInterfaceLanguage` | Auto (VS Code), English or Hindi for the Studio and sidebar. |
| Toggle Italics | `auricTheme.toggleItalics` | Switches `auricTheme.syntax.italics` between `off` and `standard`. |
| Surprise Me | `auricTheme.randomize` | Clears your dials and applies a random curated accent, palette, warmth, separation, bracket and tab style. |
| Reset Everything | `auricTheme.resetAll` | After a confirmation dialog, clears every dial and the active variant's colour overrides. |
| Show Contrast Report | `auricTheme.showAudit` | Opens the read-only "Auric contrast report" text document. |
| Copy Customisation to Clipboard | `auricTheme.copyCustomization` | Copies the customisation JSON. |
| Apply Customisation from Clipboard | `auricTheme.pasteCustomization` | Imports customisation JSON from the clipboard. |
| Export as Theme File… | `auricTheme.exportThemeFile` | Saves a standalone colour theme JSON file. Needs an Auric theme active. |
| Save Current as Preset… | `auricTheme.savePreset` | Asks for a name and saves a preset. |
| Load Preset… | `auricTheme.loadPreset` | Quick Pick of saved presets; loads the chosen one. |
| Apply Now | `auricTheme.applyNow` | Re-applies the customisation immediately. Hidden from the Command Palette; you can bind it to a key. |

Commands that change the theme only work while an Auric theme is active. Otherwise VS Code shows "Auric Theme customisations apply to the Auric Artisan themes. Pick one first." with a **Choose theme** button.

## Keybindings

| Keys (Windows and Linux) | Keys (macOS) | Command |
| --- | --- | --- |
| `Ctrl` + `Alt` + `;` | `Cmd` + `Alt` + `;` | Open Theme Studio |
| `Ctrl` + `Alt` + `'` | `Cmd` + `Alt` + `'` | Cycle Variant |

Both work anywhere in VS Code. Change them in **Keyboard Shortcuts** (`Ctrl` + `K`, `Ctrl` + `S`).

### Keys inside Theme Studio

| Key | Action |
| --- | --- |
| `1` to `6` | Select Looks, Dials, Colours, Audit, Share or Preview. |
| Arrow keys, `Home`, `End` | Move between tabs when a tab has focus. |
| `/` | Go to the Colours tab and focus the colour filter. |
| `Escape` | Close an open dropdown or picker; in the colour filter, clear the filter. |
| `Enter` | In the preset name box, save the preset. |

Number keys and `/` are ignored while you type in a field or while a dropdown or picker is open.

### Keys in controls

| Control | Keys |
| --- | --- |
| Dropdowns | Arrow keys, typeahead, `Enter` to choose, `Escape` or a click outside to close. Long lists have a search box. |
| Sliders | Arrow keys; `Shift` for larger steps; `Page Up`, `Page Down`, `Home`, `End`; double-click resets. |
| Colour picker plane | Arrow keys adjust saturation and brightness; `Shift` for larger steps. |
| Swatch grids | Arrow keys move between swatches. |

## Settings

All settings are application-wide (they apply to every window). Dials are written to your user settings.

### General

| Setting | Type | Values | Default | What it does |
| --- | --- | --- | --- | --- |
| `auricTheme.interfaceLanguage` | string | `auto`, `en`, `hi` | `auto` | Language of Theme Studio and the sidebar. |

### Theme dials

| Setting | Type | Values or range | Default | What it does |
| --- | --- | --- | --- | --- |
| `auricTheme.look` | string | `signature`, `gallery`, `atelier`, `foundry`, `bullion`, `nocturne`, `vitrine`, `clarity`, `patina`, `ember`, `sapphire` | `signature` | Named starting point; other dials layer on top. |
| `auricTheme.accent.preset` | string | `inherit`, 17 accents (see below), `custom` | `inherit` | Accent colour the theme is re-keyed onto. |
| `auricTheme.accent.custom` | string | Hex colour | empty | Used only when the accent is `custom`. |
| `auricTheme.accent.intensity` | number | 0 to 200, step 5 | 100 | Scales accent-tinted washes, borders and selections. |
| `auricTheme.accent.applyToChrome` | string | `off`, `statusBar`, `activityBar`, `both`, `full` | `off` | Fills workbench bars with the accent. `full` adds the title bar. |
| `auricTheme.surface.depth` | number | −4 to 4, step 1 | 0 | Sinks or lifts every surface. |
| `auricTheme.surface.warmth` | number | −100 to 100, step 5 | 0 | Tints neutral surfaces towards amber or slate. |
| `auricTheme.surface.separation` | string | `flat`, `subtle`, `standard`, `layered` | `standard` | Tonal distance between editor, sidebar, panel and bars. |
| `auricTheme.surface.borders` | string | `none`, `hairline`, `visible`, `strong`, `gold` | `hairline` | Divider strength; `gold` uses accent-tinted dividers. |
| `auricTheme.text.contrast` | string | `soft`, `standard`, `high`, `maximum` | `standard` | Moves the whole foreground ramp. |
| `auricTheme.text.comments` | string | `whisper`, `muted`, `standard`, `prominent` | `standard` | Comment emphasis. |
| `auricTheme.syntax.palette` | string | `jewel`, `vivid`, `pastel`, `mono`, `bullion`, `classic`, `warm`, `cool`, `duotone` | `jewel` | Token hue assignment. |
| `auricTheme.syntax.saturation` | number | 0 to 200, step 5 | 100 | Token saturation; 0 is greyscale. |
| `auricTheme.syntax.italics` | string | `off`, `comments`, `standard`, `expressive` | `standard` | How much code is italic. |
| `auricTheme.syntax.bold` | string | `off`, `declarations`, `standard`, `expressive` | `standard` | How much code is bold. |
| `auricTheme.editor.cursor` | string | `accent`, `contrast`, `syntax`, `custom` | `accent` | Caret, multi-cursor and terminal cursor colour. |
| `auricTheme.editor.cursorColor` | string | Hex colour | empty | Used only when Cursor is `custom`. |
| `auricTheme.editor.selection` | number | 20 to 200, step 5 | 100 | Scales selection, occurrence, word and find highlights together. |
| `auricTheme.editor.currentLine` | string | `off`, `subtle`, `standard`, `bordered`, `accent` | `standard` | How the caret's line is marked. |
| `auricTheme.editor.bracketPairs` | string | `off`, `subtle`, `accent`, `rainbow`, `vivid` | `rainbow` | Six bracket colour levels and their guides. |
| `auricTheme.editor.indentGuides` | string | `off`, `subtle`, `standard`, `rainbow` | `rainbow` | Indent guide colours. |
| `auricTheme.editor.whitespace` | string | `faint`, `subtle`, `visible` | `subtle` | Whitespace marks (when `editor.renderWhitespace` is on). |
| `auricTheme.editor.inlayHints` | string | `ghost`, `subtle`, `chip` | `chip` | Inlay hint backdrop. |
| `auricTheme.editor.stickyScroll` | string | `flush`, `raised`, `bordered` | `raised` | Sticky headers in editor, panel, sidebar and terminal. |
| `auricTheme.chrome.tabStyle` | string | `underline`, `overline`, `block`, `accent-block`, `minimal` | `overline` | How the active editor tab is marked. |
| `auricTheme.chrome.statusBar` | string | `chrome`, `deep`, `accent`, `transparent` | `chrome` | Status bar fill. |
| `auricTheme.chrome.activityBar` | string | `deep`, `chrome`, `accent`, `transparent` | `deep` | Activity bar fill. |
| `auricTheme.chrome.titleBar` | string | `deep`, `chrome`, `accent` | `deep` | Title bar fill (custom title bar style only). |
| `auricTheme.chrome.sidebar` | string | `raised`, `flush`, `deep` | `raised` | Side bar fill. |
| `auricTheme.chrome.dimInactive` | boolean | `true`, `false` | `false` | Pushes unfocused tabs, editors and selections back. |
| `auricTheme.terminal.palette` | string | `auric`, `classic`, `vivid`, `muted`, `monochrome` | `auric` | ANSI terminal palette. |
| `auricTheme.terminal.background` | string | `editor`, `panel`, `deep` | `editor` | Terminal backdrop. |
| `auricTheme.effects.shadows` | string | `off`, `subtle`, `standard`, `deep` | `standard` | Shadows under widgets and overlays. |
| `auricTheme.effects.focusRing` | string | `subtle`, `standard`, `strong` | `standard` | Keyboard focus ring strength. |
| `auricTheme.a11y.enforceContrast` | boolean | `true`, `false` | `true` | Contrast guard on or off. |
| `auricTheme.a11y.minContrast` | number | 3 to 7, step 0.5 | 4.5 | Minimum ratio for text and syntax. |
| `auricTheme.a11y.auditOnApply` | boolean | `true`, `false` | `true` | Audit and warn on every apply. |

### Option meanings

| Setting | Option | Meaning |
| --- | --- | --- |
| Separation | `flat` / `subtle` / `standard` / `layered` | One value for all panes / barely-there steps / shipped hierarchy / exaggerated steps. |
| Borders | `none` / `hairline` / `visible` / `strong` / `gold` | No dividers / shipped 8% divider / clearly drawn / hard edges / accent-tinted. |
| Text contrast | `soft` / `standard` / `high` / `maximum` | Lower (still AA) / shipped / pushes body and muted apart / every foreground to the edge. |
| Comment emphasis | `whisper` / `muted` / `standard` / `prominent` | As quiet as the floor permits / quieter / shipped / first-class text. |
| Italics | `off` / `comments` / `standard` / `expressive` | None / comments and doc comments / plus parameters, interfaces, decorators, attributes and `this` / plus keywords, storage modifiers and types. |
| Bold | `off` / `declarations` / `standard` / `expressive` | None / definition sites only / declarations, headings and invalid tokens / plus keywords and types. |
| Cursor | `accent` / `contrast` / `syntax` / `custom` | Accent colour / white or black, whichever reads harder / the function-name colour / Cursor colour. |
| Current line | `off` / `subtle` / `standard` / `bordered` / `accent` | None / faint fill / shipped fill and edge / edge only / accent-tinted fill. |
| Bracket pairs | `off` / `subtle` / `accent` / `rainbow` / `vivid` | Punctuation colour / low chroma / stepped along the accent / shipped six colours / maximum separation. |
| Indent guides | `off` / `subtle` / `standard` / `rainbow` | None / one neutral / neutral with accent active guide / shipped six levels. |
| Whitespace marks | `faint` / `subtle` / `visible` | Barely visible / shipped / clearly readable. |
| Inlay hints | `ghost` / `subtle` / `chip` | Text only / faint backdrop / shipped tinted chip. |
| Sticky scroll | `flush` / `raised` / `bordered` | Canvas colour / slightly lifted / lifted with a hard bottom edge. |
| Active tab | `underline` / `overline` / `block` / `accent-block` / `minimal` | Accent rule at bottom / at top (shipped) / tone only / accent fill / foreground only. |
| Status bar | `chrome` / `deep` / `accent` / `transparent` | Shipped neutral / matches activity bar / accent fill / canvas colour. |
| Activity bar | `deep` / `chrome` / `accent` / `transparent` | Shipped darkest / matches status bar / accent fill / merges into sidebar. |
| Title bar | `deep` / `chrome` / `accent` | Shipped darkest / matches status bar / accent fill. |
| Side bar | `raised` / `flush` / `deep` | Shipped, lifted / same as editor / matches activity bar. |
| Terminal background | `editor` / `panel` / `deep` | Shipped / merges into panel / darker than editor. |
| Shadows | `off` / `subtle` / `standard` / `deep` | None / barely there / shipped / heavy. |
| Focus ring | `subtle` / `standard` / `strong` | Quieter but visible / accent at full strength / maximum contrast. |

## Looks

`signature` Signature, `gallery` Gallery, `atelier` Atelier, `foundry` Foundry, `bullion` Bullion, `nocturne` Nocturne, `vitrine` Vitrine, `clarity` Clarity, `patina` Patina, `ember` Ember, `sapphire` Sapphire. See [Looks and dials](looks-and-dials.md#apply-a-look) for descriptions.

## Accents

| ID | Name | Hex | Hint |
| --- | --- | --- | --- |
| `gold` | Auric Gold | `#D3AF37` | The brand. Warm, metallic, the default. |
| `champagne` | Champagne | `#E4CE8F` | Gold, lifted and softened. |
| `brass` | Brass | `#C9A227` | Deeper and greener than the brand gold. |
| `bronze` | Bronze | `#C08A4A` | Warm metal, less yellow. |
| `copper` | Copper | `#CA7A4E` | Orange-forward metal. |
| `ember` | Ember | `#E0764A` | Hot orange. |
| `rose` | Rose | `#E08AA0` | Soft pink-red. |
| `crimson` | Crimson | `#E06A6A` | Red without the alarm. |
| `amethyst` | Amethyst | `#B48AE6` | Violet jewel tone. |
| `iris` | Iris | `#8E9BF0` | Blue-violet. |
| `sapphire` | Sapphire | `#6BA3E8` | Classic editor blue. |
| `azure` | Azure | `#4FB6E0` | Bright cyan-blue. |
| `patina` | Patina | `#5CC9B4` | Aged copper. Cool and calm. |
| `emerald` | Emerald | `#5CC489` | Green jewel tone. |
| `moss` | Moss | `#A3C46A` | Yellow-green. |
| `platinum` | Platinum | `#C5C8CE` | Cool neutral metal. |
| `graphite` | Graphite | `#9A9A9A` | No hue at all. Fully monochrome UI. |

The listed hex values are the accent keys. On light themes the accent is darkened automatically until it clears your minimum contrast.

## Syntax palettes

| ID | Name | Description |
| --- | --- | --- |
| `jewel` | Jewel | The shipped palette: gold and champagne callables, amber constants, orchid keywords, patina types, sage strings. |
| `vivid` | Vivid | The same hues pushed to the edge of the gamut. |
| `pastel` | Pastel | Low chroma, lifted lightness. |
| `mono` | Monochrome | Almost no hue; lightness carries meaning. |
| `bullion` | Bullion | Every token on the accent hue, separated by lightness and chroma. |
| `classic` | Classic | Blue keywords, green strings, teal types. |
| `warm` | Warm | Gold, amber, copper and rose; no cool tokens. |
| `cool` | Cool | Patina, sapphire and amethyst; gold only in the chrome. |
| `duotone` | Duotone | The accent and its complement only. |

## Terminal palettes

| ID | Name | Description |
| --- | --- | --- |
| `auric` | Auric | Matches the syntax palette; yellow is the accent. |
| `classic` | Classic | Conventional ANSI hues, tuned for the canvas. |
| `vivid` | Vivid | Higher chroma across all sixteen. |
| `muted` | Muted | Lower chroma. |
| `monochrome` | Monochrome | Greyscale, separated by lightness only. |

## All 54 themes

The theme ID is what VS Code stores in `workbench.colorTheme`.

| Family | Theme IDs (display name: Auric Artisan — Family Accent) |
| --- | --- |
| Obsidian | `obsidian-gold`, `obsidian-sapphire`, `obsidian-rose`, `obsidian-amethyst`, `obsidian-patina` |
| Obsidian (cont.) | `obsidian-emerald`, `obsidian-ember`, `obsidian-crimson`, `obsidian-iris`, `obsidian-graphite` |
| Midnight | `midnight-gold`, `midnight-sapphire`, `midnight-rose`, `midnight-iris`, `midnight-amethyst` |
| Midnight (cont.) | `midnight-patina`, `midnight-emerald`, `midnight-ember`, `midnight-crimson`, `midnight-graphite` |
| Parchment | `parchment-gold`, `parchment-rose`, `parchment-ember`, `parchment-emerald`, `parchment-sapphire` |
| Parchment (cont.) | `parchment-amethyst`, `parchment-patina`, `parchment-crimson`, `parchment-iris`, `parchment-graphite` |
| Porcelain | `porcelain-sapphire`, `porcelain-amethyst`, `porcelain-patina`, `porcelain-rose`, `porcelain-iris` |
| Porcelain (cont.) | `porcelain-graphite`, `porcelain-gold`, `porcelain-emerald`, `porcelain-ember`, `porcelain-crimson` |
| Dusk | `dusk-gold`, `dusk-sapphire`, `dusk-rose`, `dusk-amethyst`, `dusk-iris`, `dusk-graphite` |
| Forest | `forest-gold`, `forest-patina`, `forest-emerald`, `forest-ember`, `forest-rose`, `forest-graphite` |
| High contrast | `obsidian-gold-high-contrast` (dark), `porcelain-gold-high-contrast` (light) |

The order in this table is the order used by **Cycle Variant**. Obsidian, Midnight, Dusk and Forest are dark; Parchment and Porcelain are light.

## Colour slots

107 slots in 12 groups. Kind: **solid** (no transparency), **alpha** (transparency allowed) or **either**.

| Group | Slots (path — label) |
| --- | --- |
| Surfaces (solid) | `bg.deepest` Deepest, `bg.base` Canvas, `bg.raised` Raised, `bg.chrome` Chrome |
| Surfaces (cont.) | `bg.overlay` Overlay, `bg.overlayRaised` Overlay raised, `bg.inset` Inset, `bg.tint` Warm tint |
| Text (solid) | `fg.default` Body, `fg.muted` Muted, `fg.subtle` Subtle, `fg.faint` Faint, `fg.onAccent` On accent |
| Text (cont.) | `fg.inverse` Inverse |
| Lines | `line.subtle` Hairline, `line.default` Divider, `line.strong` Strong, `line.control` Control edge (either) |
| Lines (cont.) | `line.gold` Gold hairline, `line.goldStrong` Gold edge (alpha); `line.focus` Focus ring (solid) |
| Accent | `accent.base` Accent, `accent.bright` Emphasis, `accent.deep` Deep, `accent.onAccent` On accent (solid) |
| Accent (cont.) | `accent.soft` Soft wash, `accent.softer` Softer wash, `accent.wash` Faintest wash (alpha) |
| States (alpha) | `state.hover` Hover, `state.active` Active, `state.selected` Selected |
| States (cont.) | `state.selectedInactive` Selected (blurred), `state.drop` Drop target |
| Selection (alpha) | `sel.text` Selection, `sel.textInactive` Selection (blurred), `sel.highlight` Occurrences |
| Selection (cont.) | `sel.word` Word (read), `sel.wordWrite` Word (write), `sel.find` Find match, `sel.findOther` Find others |
| Selection (cont.) | `sel.range` Range, `sel.line` Current line, `sel.lineBorder` Current line edge |
| Semantics (solid) | `sem.error` Error, `sem.errorStrong` Error (loud), `sem.warn` Warning, `sem.warnStrong` Warning (loud) |
| Semantics (cont.) | `sem.info` Info, `sem.infoStrong` Info (loud), `sem.ok` Success, `sem.okStrong` Success (loud) |
| Semantic washes (alpha) | `soft.error` Error wash, `soft.warn` Warning wash, `soft.info` Info wash, `soft.ok` Success wash |
| Terminal (solid) | `ansi.black`, `ansi.red`, `ansi.green`, `ansi.yellow`, `ansi.blue`, `ansi.magenta`, `ansi.cyan`, `ansi.white` |
| Terminal (cont.) | `ansi.brightBlack` to `ansi.brightWhite`: the eight bright versions of the colours above |
| Source control (solid) | `git.added` Added, `git.modified` Modified, `git.deleted` Deleted, `git.untracked` Untracked |
| Source control (cont.) | `git.ignored` Ignored, `git.conflict` Conflicting, `git.submodule` Submodule |
| Source control (cont.) | `git.stageDeleted` Staged delete, `git.stageModified` Staged modify |
| Syntax (solid) | `syntax.comment` Comment, `syntax.punctuation` Punctuation, `syntax.operator` Operator |
| Syntax (cont.) | `syntax.variable` Variable, `syntax.property` Property, `syntax.parameter` Parameter |
| Syntax (cont.) | `syntax.string` String, `syntax.stringAlt` String (alt), `syntax.escape` Escape, `syntax.number` Number |
| Syntax (cont.) | `syntax.constant` Constant, `syntax.keyword` Keyword, `syntax.control` Control flow, `syntax.storage` Storage |
| Syntax (cont.) | `syntax.fn` Function, `syntax.method` Method, `syntax.type` Type, `syntax.interface` Interface |
| Syntax (cont.) | `syntax.tag` Tag, `syntax.attribute` Attribute, `syntax.regexp` Regexp, `syntax.invalid` Invalid |
| Syntax (cont.) | `syntax.deprecated` Deprecated, `syntax.heading` Heading, `syntax.link` Link, `syntax.quote` Quote |
| Effects (alpha) | `shadow` Shadow |

Lines `line.subtle`, `line.default`, `line.strong` and `line.control` accept either kind.

## Theme Studio controls by tab

| Tab | Controls |
| --- | --- |
| Looks | **The set**: 11 look swatches with a count. Selecting a look applies it; selecting the active look again restarts from it. |
| Dials | **Search dials by name or setting…**, **Dial visibility** (**All dials**, **Modified only**), match count, ten group cards with group reset, per-dial modified dot and reset. |
| Colours | **Filter by name or path**, 12 collapsible groups with counts, a colour field per slot, **Shipped** comparison and revert per overridden slot. |
| Audit | Worst-pair card with **All clear** or "{n} failing", **Measured pairs** table (Pair, Ratio, APCA, Minimum, Result), **How to read this**. |
| Share | **Export** (JSON, **Copy**, **Refresh**), **Import** (paste box, **Import**, **Clear**), **Presets** (name box, **Save**, **Saved** list with **Load** and delete). |
| Preview | **Comparison view** (**Side by side**, **As shipped**, **Your palette**), **Copy palette as CSS**, specimens and changed-slot count. |

Studio-wide: language switch, **Explore colours →**, metrics, **Reset all** (asks **Reset everything?**, confirm within four seconds), **Randomize**, **Settings**.

## Other surfaces

| Surface | Details |
| --- | --- |
| Status bar item | Right side. Paint-can icon and short theme name; `*` when customised. Tooltip shows dials and colours changed. Opens Theme Studio. Hidden when a non-Auric theme is active. |
| Activity Bar view | **Auric Theme** container with the **Theme** view. See [The Theme sidebar](theme-sidebar.md). |
| Contrast report | Read-only text document "Auric contrast report". |
| Walkthrough | **Make it yours**: **Pick a variant**, **Change the gold**, **Open the Studio**, **Keep it readable**. |

## Messages you may see

| Message | Meaning |
| --- | --- |
| Auric Theme customisations apply to the Auric Artisan themes. Pick one first. | A non-Auric theme is active. Select **Choose theme**. |
| Auric Theme: {n} colour pairs no longer meet your contrast minimum. | Audit on apply found failures. Select **Show report**. |
| Reset every Auric Theme dial and colour override? | Confirmation for **Reset Everything**. Select **Reset**. |
| Auric Theme: could not save auricTheme.… — … | VS Code refused to write a setting, for example because `settings.json` has a syntax error. |
| VS Code rejected a settings key: … | VS Code refused a colour customisation key. |
| Bad hex colour: … | A colour value is not valid hex. |
| Auric Theme: no saved presets yet. | **Load Preset…** found no presets. |
| Auric Theme: switch to an Auric Artisan theme first. | **Export as Theme File…** needs an Auric theme active. |

## Files and formats

| Item | Format |
| --- | --- |
| Customisation | JSON with `$schema`, `version`, `generator`, `name`, `theme`, `knobs` and `overrides`. |
| Theme file | VS Code colour theme JSON; default name `<theme-id>-custom-color-theme.json`. |
| CSS palette | A `:root` block of `--auric-<slot-path>` custom properties. |
