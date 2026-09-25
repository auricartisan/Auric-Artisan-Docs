---
title: Auric Icons: Modern — Reference
description: Every command, keybinding, setting, view, icon ID, pack, category and library control in Auric Icons: Modern 0.12.1.
product: VS Code extensions › Auric Icons: Modern
updated: 2026-09-25
---

# Auric Icons: Modern reference

This reference describes version 0.12.1 as published on the Visual Studio Marketplace.

## Commands

Category in the Command Palette: **Auric Icons: Modern**.

### File icon theme

| Command | ID | What it does |
| --- | --- | --- |
| Configure… | `auricIcons.configure` | Menu for folder colour, icon pack, arrows, saturation, opacity, detection and restore. |
| Select Icon Pack | `auricIcons.selectIconPack` | Choose None, Angular, NestJS, React / Redux or Vue / Pinia. |
| Select Folder Colour | `auricIcons.selectFolderColor` | Choose a preset or custom hex folder colour. |
| Toggle Explorer Arrows | `auricIcons.toggleExplorerArrows` | Show or hide the Explorer chevrons. |
| Detect Auric Artisan Workspace | `auricIcons.detectWorkspace` | Report whether the workspace has `.auric-artisan/` or `.auricignore`. |
| Restore Default Settings | `auricIcons.restoreDefaults` | Clear all Modern theme settings. |
| Activate Icon Theme | `auricIcons.activate` | Set **Auric Icons: Modern** as the file icon theme. |

### Icon Library

| Command | ID | What it does |
| --- | --- | --- |
| Open Icon Library | `auricIcons.library.openExplorer` | Opens the **Icon Studio — Library** editor tab. |
| Search Icons | `auricIcons.library.searchIcons` | Choose an icon, then an action. |
| Insert SVG at Cursor | `auricIcons.library.insertSvg` | Choose an icon and insert it. |
| Smart Insert Icon (matches active language) | `auricIcons.library.smartInsert` | Choose an icon and insert it with language-aware output. |
| Copy Icon As… (JSX, CSS, Markdown, Data URI, Image tag) | `auricIcons.library.copyAs` | Choose an icon and one of nine formats. |
| Insert from Likes | `auricIcons.library.showFavorites` | Choose a liked icon and insert it. |
| Insert from Recent | `auricIcons.library.showRecents` | Choose a recent icon and insert it. |
| Toggle Like for an Icon | `auricIcons.library.toggleFavorite` | Like or unlike an icon. |
| Clear Likes, Recents and Learned Recommendations | `auricIcons.library.resetPersonalization` | Asks for confirmation, then resets personalisation. |
| Copy SVG | `auricIcons.library.copySvg` | Choose an icon and copy raw SVG. |
| Save SVG As… | `auricIcons.library.saveSvg` | Choose an icon and save it as a file. |
| Open SVG Source | `auricIcons.library.openSource` | Choose an icon and open its SVG. |

Icon Library commands are hidden from the Command Palette while another extension hosts the shared library. They still work from keybindings and forward to the host.

## Keybindings

| Keys (Windows and Linux) | Keys (macOS) | Command | When |
| --- | --- | --- | --- |
| `Ctrl` + `Alt` + `I` | `Cmd` + `Alt` + `I` | Smart Insert Icon | Editor focused and Modern hosts the library |
| `Ctrl` + `Alt` + `R` | `Cmd` + `Alt` + `R` | Insert from Recent | Editor focused and Modern hosts the library |

In the Icon Library view: `/` focuses search; `Escape` clears it; in dropdowns, arrow keys move and `Escape` closes.

## Settings

### File icon theme

| Setting | Type | Values or range | Default | What it does |
| --- | --- | --- | --- | --- |
| `auricIcons.folderColor` | string | `default` or a hex colour | `default` | Folder colour. `default` is the Auric gold. Folders only. |
| `auricIcons.activeIconPack` | string | `none`, `angular`, `nest`, `react`, `vue` | `none` | Framework pack layered over the base set. |
| `auricIcons.autoDetect` | boolean | `true`, `false` | `true` | Offer the theme once in Auric Artisan workspaces. |
| `auricIcons.hidesExplorerArrows` | boolean | `true`, `false` | `false` | Hide Explorer chevrons. |
| `auricIcons.saturation` | number | 0 to 2 | 1 | Colour saturation multiplier; 0 is greyscale. |
| `auricIcons.opacity` | number | 0.1 to 1 | 1 | Icon opacity. |
| `auricIcons.files.associations` | object | `{ "*.ext" or filename: icon ID }` | `{}` | Map files to icons; `none` removes a mapping. |
| `auricIcons.folders.associations` | object | `{ folder name: icon ID }` | `{}` | Map folders to icons; open and closed applied together. |

### Icon Library

| Setting | Type | Values or range | Default | What it does |
| --- | --- | --- | --- | --- |
| `auricIcons.library.defaultVariant` | string | `auto`, `color`, `mono`, `outline`, `duotone` | `auto` | Variant for Command Palette actions; `auto` follows the file. |
| `auricIcons.library.pageSize` | number | 24 to 240 | 72 | Cards streamed per batch. |
| `auricIcons.library.smartInsert` | boolean | `true`, `false` | `true` | Language-aware output for Insert. |
| `auricIcons.library.recommendations.enabled` | boolean | `true`, `false` | `true` | Recommendations for the file you are editing. |
| `auricIcons.library.recommendations.limit` | number | 4 to 24 | 12 | Icons in the recommendation rail. |
| `auricIcons.library.showGuide` | boolean | `true`, `false` | `true` | Smart guide tips at the top of the library. |
| `auricIcons.library.density` | string | `comfortable`, `compact` | `comfortable` | Card size. |
| `auricIcons.library.hoverPreview` | boolean | `true`, `false` | `true` | Hover previews for icon IDs in code. |

Values set under the retired `auricArtisanIcons.*` names are still honoured as fallbacks for library settings.

## Views and menus

| Place | Contents |
| --- | --- |
| Activity Bar | **Auric Icons: Modern** container with the **Icon Library** view (hidden when another extension hosts). |
| View title bar | **Open Icon Library**, **Smart Insert Icon**, **Insert from Likes**; **…** menu: **Clear Likes, Recents and Learned Recommendations**. |
| Editor tab | **Icon Studio — Library**. |
| File icon theme | **Auric Icons: Modern** (theme ID `auric-artisan-modern-icon`). |

## File icon theme contents

| Item | Count |
| --- | --- |
| Theme icons | 408 |
| File extensions mapped | 265 |
| Exact filenames mapped | 462 |
| Folder names mapped | 265 |
| Framework pack icons | 26 (Angular 8, NestJS 9, React / Redux 6, Vue / Pinia 3) |

## Icon IDs for associations

Use these values in `auricIcons.files.associations` and `auricIcons.folders.associations`.

### File icon IDs

Languages: `javascript`, `typescript`, `python`, `java`, `csharp`, `cpp`, `c`, `go`, `rust`, `php`, `ruby`, `swift`, `kotlin`, `shell`, `powershell`, `sql`, `dart`, `scala`, `elixir`, `erlang`, `haskell`, `clojure`, `fsharp`, `ocaml`, `lua`, `r`, `julia`, `perl`, `groovy`, `objectivec`, `zig`, `nim`, `crystal`, `solidity`, `assembly`, `fortran`, `vlang`, `haxe`, `prolog`, `racket`, `scheme`, `vala`, `coffeescript`, `vbnet`, `pascal`, `cobol`, `matlab`, `batch`.

Web and markup: `html`, `css`, `sass`, `less`, `stylus`, `jsx`, `tsx`, `vue`, `svelte`, `astro`, `handlebars`, `ejs`, `pug`, `liquid`, `wasm`.

Data and config: `json`, `jsonc`, `json5`, `yaml`, `toml`, `xml`, `csv`, `tsv`, `graphql`, `protobuf`, `avro`, `parquet`, `geojson`, `ini`, `env`, `tsconfig`, `jsconfig`, `package-json`, `package-lock`, `eslint`, `prettier`, `editorconfig`, `biome`, `stylelint`, `babel`, `npmrc`.

Build and packages: `webpack`, `vite`, `rollup`, `parcel`, `esbuild`, `tailwind`, `postcss`, `makefile`, `cmake`, `gradle`, `maven`, `cargo`, `gemfile`, `pyproject`, `gomod`, `composer`, `nuget`, `podfile`, `swiftpm`.

Frameworks and platforms: `nextjs`, `nuxt`, `angular`, `remix`, `gatsby`, `svelte-config`, `capacitor`, `electron`, `tauri`, `flutter`, `docker`, `docker-compose`, `kubernetes`, `helm`, `terraform`, `ansible`, `pulumi`, `vagrant`, `jenkins`, `github-actions`, `gitlab-ci`, `circleci`, `travis`, `procfile`, `firebase`, `vercel`, `netlify`, `cloudflare`, `supabase`, `aws`.

Testing and docs: `test`, `jest`, `cypress`, `playwright`, `storybook`, `coverage`, `markdown`, `mdx`, `readme`, `license`, `changelog`, `contributing`, `codeowners`, `text`, `pdf`.

Other: `git`, `sqlite`, `prisma`, `migration`, `image`, `svg`, `video`, `audio`, `font`, `model3d`, `design`, `archive`, `binary`, `executable`, `library`, `certificate`, `key`, `default`, `code`.

Auric Artisan: `auric-ignore`, `auric-scan-cache`, `auric-health`, `sarif`, `auric-history`, `auric-remediation`, `auric-report`.

### Folder icon IDs

`src`, `app`, `lib`, `packages`, `modules`, `node-modules`, `components`, `pages`, `routes`, `views`, `layouts`, `templates`, `controllers`, `models`, `services`, `repositories`, `middleware`, `hooks`, `store`, `types`, `schemas`, `graphql`, `api`, `server`, `client`, `utils`, `assets`, `public`, `images`, `icons`, `fonts`, `audio`, `video`, `styles`, `scripts`, `config`, `env`, `database`, `migrations`, `seeds`, `test`, `mocks`, `coverage`, `storybook`, `benchmark`, `docs`, `examples`, `build`, `dist`, `cache`, `temp`, `logs`, `generated`, `git`, `github`, `gitlab`, `ci`, `docker`, `kubernetes`, `helm`, `terraform`, `cloud`, `aws`, `azure`, `gcp`, `firebase`, `vercel`, `netlify`, `auric-artisan`, `swatches`, `security`, `certificates`, `i18n`, `mobile`, `android`, `ios`, `desktop`, `electron`, `javascript`, `typescript`, `python`, `rust`, `java`, `go`, `react`, `vue`, `angular`, `svelte`, `next`, `nuxt`, `wasm`, `default`, `root`.

## Icon Library contents

| Item | Value |
| --- | --- |
| Icons | 720 (420 Simple Modern, 300 Sharp Modern) |
| Variants | Color, Mono, Outline, Duotone |
| Categories | 33 |
| Unique concepts | 520 |

Categories: Files and document types; Folders and organization; Coding and development; Artificial intelligence; Data and databases; Cloud and hosting; Cybersecurity; Communication; Social interaction; User accounts and profiles; Business and finance; E-commerce; Marketing; Gaming and Entertainment; Sports and Fitness; Shopping and Products; Devices and Hardware; Internet and Networking; Settings and Controls; Alerts and Notifications; Actions and Gestures; Status and Feedback; Accessibility; Time and History; Search and Discovery; Relationships and Community; Legal and Administration; Logistics and Delivery; Agriculture and Gardening; Space and Astronomy; Holidays and Celebrations; Abstract Concepts; Experimental and Decorative Symbols.

## Library controls

| Control | Options |
| --- | --- |
| Search | Free text, synonyms, fuzzy ranking. |
| Library | **All libraries** or one collection (only when merged). |
| Category | **All categories** or one of 33. |
| Style | **All styles**, **Modern**, **Sharp** (plus other collections' styles when merged). |
| Variant | **Auto**, **Color**, **Mono**, **Outline**, **Duotone** (plus **Filled** and **Small** when Playful is merged). |
| Preview surface | **Auto**, **Light**, **Dark**. |
| Chips | **All**, **✦ For you**, **♥ Likes**, **↺ Recent**. |
| Card buttons | Artwork (open source), heart, **Insert**, **Copy**, **Save**, **JSX**, **URI**, **Source**. |
| Rail | **✦ Recommended for this file** with **Refresh**; selecting a rail card inserts it. |

## Limits

| Item | Limit |
| --- | --- |
| Recent icons | 60 |
| Liked icons | 500 |
| Quick Pick results | 200 with a search term; 400 without |
| Smart guide tips shown | Up to 4 |

## Messages you may see

| Message | Meaning |
| --- | --- |
| Auric Icons: Modern updated — … Reload to apply? | Theme settings changed; reload to see them. |
| Auric Icons: Modern: could not apply customisation — … The default icons remain active. | A setting could not be applied; the original icons stay in place. |
| Open a text editor before inserting an SVG. | No text editor was available for insertion. |
| … like an icon first — open the library and press the heart. | **Insert from Likes** found no likes. |
| … no recent icons yet. | **Insert from Recent** found none. |
| This workspace uses Auric Artisan (found …). | Workspace detection offer. |
