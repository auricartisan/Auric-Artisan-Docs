---
title: Auric Artisan File Icons — Reference
description: Every command, setting, menu, view, theme, colour and Studio control in Auric Artisan File Icons 0.1.1.
product: VS Code extensions › Auric Artisan File Icons
updated: 2026-09-25
---

# Auric Artisan File Icons reference

This reference describes version 0.1.1 as published on the Visual Studio Marketplace.

## File icon themes

| Theme name | Theme ID | Artwork |
| --- | --- | --- |
| Auric Artisan File Icons: Facet | `auric-artisan-file-icons-facet` | 500 SVGs |
| Auric Artisan File Icons: Playful | `auric-artisan-file-icons-playful` | 500 SVGs |
| Auric Artisan File Icons: Modern | `auric-artisan-modern-icon` | 464 SVGs |

## Commands

Category in the Command Palette: **Auric Artisan File Icons**.

| Command | ID | What it does |
| --- | --- | --- |
| Activate Facet Icon Theme | `auricFileIcons.activate` | Sets Facet as the file icon theme. |
| Activate Playful Icon Theme | `auricFileIcons.activatePlayful` | Sets Playful as the file icon theme. |
| Activate Modern Icon Theme | `auricFileIcons.activateModern` | Sets Modern as the file icon theme. |
| Open File Icon Studio | `auricFileIcons.openStudio` | Opens the Studio editor tab beside the editor. |
| Open File Icon Studio Settings | `auricFileIcons.configure` | The **Configure Auric Artisan File Icons** menu. |
| Choose Folder Color | `auricFileIcons.pickFolderColor` | Folder colour presets or a custom hex. |
| Toggle Explorer Arrows | `auricFileIcons.toggleExplorerArrows` | Shows or hides the Explorer chevrons. |
| Insert Icon into Code… | `auricFileIcons.quickInsert` | Picker of icons in the active style; inserts in `insertFormat`. |
| Set File or Folder Icon | `auricFileIcons.assignResourceIcon` | Assigns an icon to the selected Explorer resource. |
| Clear Custom File or Folder Icon | `auricFileIcons.clearResourceIcon` | Removes that assignment. |
| Configure Smart Icon Detection | `auricFileIcons.smart.configure` | Smart detection menu. |
| Refresh Smart Icon Matches | `auricFileIcons.smart.refresh` | Clears cached matches. |
| Explain Smart Icon Match | `auricFileIcons.smart.inspect` | Explains the match for the selected resource. |
| Toggle Smart Icon Detection | `auricFileIcons.smart.toggle` | Turns smart detection on or off. |
| Apply Detected Folder Icon | `auricFileIcons.smart.applyDetectedFolderIcon` | Saves the detected folder icon as an association. |
| Scan Workspace for Folder Icons | `auricFileIcons.smart.scanWorkspace` | Scans first-level folders and assigns detected icons. |
| Restore Icon Defaults | `auricFileIcons.restoreDefaults` | Confirms, then clears appearance, associations and smart settings. |
| Apply Icon Profile | `auricFileIcons.profiles.apply` | Applies a built-in or saved profile. |
| Save Current Icon Profile | `auricFileIcons.profiles.save` | Saves your current set-up as a profile. |
| Delete Saved Icon Profile | `auricFileIcons.profiles.delete` | Deletes a saved profile. |
| Export Icon Profile to Clipboard | `auricFileIcons.profiles.export` | Copies the current profile JSON. |
| Import Icon Profile from Clipboard | `auricFileIcons.profiles.import` | Imports profile JSON. |
| Show Icon Theme Diagnostics | `auricFileIcons.diagnostics` | Writes a report to the **Auric Artisan File Icons** output channel. |
| Import Legacy Playful Settings… | `auricFileIcons.migratePlayful` | Copies missing settings from the old Playful extension. |
| Import Modern File Icon Settings… | `auricFileIcons.migrateModern` | Copies missing Modern file-theme settings. |

There are no default keybindings. Assign your own in **Keyboard Shortcuts**.

## Menus

| Menu | Item | When shown |
| --- | --- | --- |
| Explorer right-click › **Auric File Icons** | **Open File Icon Studio** | Always |
| Explorer right-click › **Auric File Icons** | **Explain Smart Icon Match** | An Auric file icon theme is active |
| Explorer right-click › **Auric File Icons** | **Apply Detected Folder Icon** | On folders, with an Auric theme active |
| Explorer right-click › **Auric File Icons** | **Set File or Folder Icon** | An Auric file icon theme is active |
| Explorer right-click › **Auric File Icons** | **Clear Custom File or Folder Icon** | An Auric file icon theme is active |
| Editor right-click | **Insert Icon into Code…** | A writable editor has focus |

## Views

| Place | Contents |
| --- | --- |
| Activity Bar | **Auric File Icons** container with the **File Icon Studio** view. |
| Editor tab | **File Icon Studio**, opened beside the active editor. |
| Output | **Auric Artisan File Icons** channel for diagnostics. |

## Settings

| Setting | Type | Values or range | Default | What it does |
| --- | --- | --- | --- | --- |
| `auricFileIcons.fileColor` | string | `default`, `#rgb`, `#rrggbb` | `default` | Recolours every file icon. |
| `auricFileIcons.folderColor` | string | `default`, `#rgb`, `#rrggbb` | `default` | Recolours every folder pair. |
| `auricFileIcons.saturation` | number | 0 to 2 | 1 | Saturation multiplier; 0 is greyscale. |
| `auricFileIcons.brightness` | number | 0.5 to 1.5 | 1 | Brightness multiplier. |
| `auricFileIcons.opacity` | number | 0.2 to 1 | 1 | Icon opacity. |
| `auricFileIcons.hidesExplorerArrows` | boolean | `true`, `false` | `false` | Hides Explorer chevrons. |
| `auricFileIcons.files.associations` | object | `*.ext`, `parent/*.ext`, filename or `parent/name` to icon ID | `{}` | File associations; `none` removes a match. |
| `auricFileIcons.folders.associations` | object | folder or `parent/folder` to icon ID | `{}` | Folder associations. |
| `auricFileIcons.folders.rootAssociations` | object | root name to icon ID | `{}` | Workspace-root associations. |
| `auricFileIcons.smart.enabled` | boolean | `true`, `false` | `true` | Smart decorations on or off. |
| `auricFileIcons.smart.folders` | boolean | `true`, `false` | `true` | Classify folders. |
| `auricFileIcons.smart.files` | boolean | `true`, `false` | `true` | Classify small text files. |
| `auricFileIcons.smart.style` | string | `badgeAndColor`, `badge`, `color`, `tooltip` | `badgeAndColor` | Decoration style. |
| `auricFileIcons.smart.propagate` | boolean | `true`, `false` | `false` | Propagate child decorations to parents. |
| `auricFileIcons.smart.watch` | boolean | `true`, `false` | `true` | Watch project markers and refresh. |
| `auricFileIcons.smart.maxFileSize` | integer | 1024 to 262144 | 65536 | Largest file inspected, in bytes. |
| `auricFileIcons.smart.maxFolderEntries` | integer | 25 to 2000 | 250 | Child names considered per folder. |
| `auricFileIcons.smart.cacheSeconds` | integer | 1 to 3600 | 15 | Cache duration. |
| `auricFileIcons.smart.scanLimit` | integer | 1 to 250 | 80 | Folders checked by the workspace scan. |
| `auricFileIcons.smart.exclusions` | array | folder names or wildcards | 13 common folders | Never inspected. |
| `auricFileIcons.smart.rules` | array | rule objects | `[]` | Custom rules, run before built-ins. |
| `auricFileIcons.hover.enabled` | boolean | `true`, `false` | `true` | Code hovers for icon tokens. |
| `auricFileIcons.insertFormat` | string | `svg`, `jsx`, `img`, `css` | `svg` | Default code format. |
| `auricFileIcons.modernPack` | string | `none`, `angular`, `nest`, `react`, `vue` | `none` | Modern framework associations. |

Default exclusions: `.git`, `node_modules`, `vendor`, `dist`, `build`, `out`, `coverage`, `.next`, `.nuxt`, `.cache`, `.turbo`, `target`, `__pycache__`.

## Theme colours

Ten colours for smart decorations can be changed in `workbench.colorCustomizations`: `auricFileIcons.smart.auric`, `.framework`, `.language`, `.infrastructure`, `.test`, `.docs`, `.data`, `.generated`, `.security` and `.custom`. See [Smart detection](smart-detection.md#category-colours) for their defaults.

## File Icon Studio controls

| Tab | Control | Options or action |
| --- | --- | --- |
| Library | **Search icons** | Free text, up to 150 characters. |
| Library | **Artwork style** | Facet, Playful, Modern. |
| Library | **Show** | Files & folders, Files, Folders. |
| Library | **Code format** | Inline SVG, JSX, HTML image, CSS background. |
| Library | **Open folder artwork** | Shows folders in their open state. |
| Library | **Use … in Explorer** | Activates the chosen style. |
| Library | Card | **Insert**, **Copy**, inspector; **Load more icons**. |
| Appearance | **Modern framework pack** | No framework pack, Angular, NestJS, React, Vue. |
| Appearance | **File color**, **Folder color** | Swatch, hex field, **Reset**. |
| Appearance | **Saturation**, **Brightness**, **Opacity** | Sliders. |
| Appearance | **Hide Explorer arrows** | Check box. |
| Appearance | Buttons | **Apply appearance**, **Restore defaults…**. |
| Workspace | Smart Explorer matches | **Enable smart detection**, **Configure**, **Refresh**, **Scan folders…**. |
| Workspace | Profiles | **Apply profile…**, **Save current…**, **Export**, **Import…**, **Delete saved…**. |
| Workspace | Insert from a code hover | **Enable code hovers**. |
| Workspace | Import existing file settings | **Import Modern file settings**, **Import legacy settings…**, **Diagnostics**. |
| Inspector | Buttons | **Insert into code**, **Copy code**, **Copy hover token**. |
| Header | Buttons | **auricartisan.com ↗**, **↗** (open in editor tab), **⚙** (all extension settings). |

Keys: `/` focuses search; dropdown pickers support arrow keys, `Home`, `End` and `Escape`.

## Artwork and mappings

| Item | Facet | Playful | Modern |
| --- | --- | --- | --- |
| SVG assets | 500 | 500 | 464 |
| File designs | 200 | 200 | 219 |
| Folder pairs | 150 | 150 | 114 |
| Mappings | 270 extensions, 453 filenames, 84 language IDs, 357 folder aliases | Same as Facet | Its own mappings and 4 framework packs |

## Diagnostics report

**Show Icon Theme Diagnostics** lists the version, active theme, workspace trust, remote host, folder count, asset counts, your appearance values, association counts, smart detection settings and limits, the number of custom rules and saved profiles. It omits filenames and file contents.

## Limits

| Item | Limit |
| --- | --- |
| Search text | 150 characters |
| Smart badge | 2 characters |
| Profile import | 256 KiB |
| Profile name | 80 characters |
