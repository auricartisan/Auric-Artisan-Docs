---
title: Auric Artisan File System — related files
description: Jump between a file and its test, style, story, component and documentation, create missing companions, and teach Auric Files your own conventions.
product: VS Code extensions › Auric Artisan File System
updated: 2026-09-25
---

# Related files

Most source files come with *companions*: a component has a test, a stylesheet and a story; a module has documentation and type declarations. Auric Files knows the usual conventions for each framework preset, so it can open a file's companion in one step, show which ones are missing and create them.

## Go to a companion

With a file open in the editor:

| Command | Opens | Deck shortcut |
| --- | --- | --- |
| **Auric Files: Go to Related File…** | A list of every companion that exists | `Ctrl` + `Alt` + `R` |
| **Auric Files: Open Matching Test** | The file's test | `Ctrl` + `Alt` + `A`, then `Q` |
| **Auric Files: Open Matching Style** | The file's stylesheet | `Ctrl` + `Alt` + `A`, then `S` |
| **Auric Files: Open Matching Story** | The file's story | `Ctrl` + `Alt` + `A`, then `W` |
| **Auric Files: Open Matching Component** | The component a test, style or story belongs to | `Ctrl` + `Alt` + `A`, then `I` |
| **Auric Files: Open Matching Documentation** | The file's documentation | `Ctrl` + `Alt` + `A`, then `Shift` + `D` |

The shortcuts need `auricFiles.keyboard.enableDefaultShortcuts`. The same commands are in **Auric Files** › **Navigate and Paths** on a file's context menu, and in the **Inspect & navigate** group of the panel.

Navigation works in both directions: from `Button.tsx` to `Button.test.tsx`, and from the test back to the component.

## See the whole group

**Show Related File Group** lists every companion the rules expect for the file, marking which exist and which are missing. It runs from the panel's **Inspect & navigate** group.

The Properties view also lists up to six related files that exist. See [Properties, compare and export](properties-compare-export.md).

## Create missing companions

- **Auric Files: Create Related Files…** (`Ctrl` + `Alt` + `A`, then `R` with the deck) — choose which companions to create from a list.
- **Auric Files: Generate Missing Companion Files** — create every missing companion at once. If none is missing: **Every companion file already exists.**

New companions are created from the rule's template, using the preset's style language and test framework (`auricFiles.create.componentStyleLanguage`, `auricFiles.create.testFramework`).

## Relationship kinds

The built-in rules use these kinds: **Component**, **Test**, **Style**, **Story**, **Template**, **Types**, **Snapshot**, **Schema**, **Documentation**, **Barrel** (an index file that re-exports) and **Config**. Which ones apply depends on the active preset.

## Settings

| Setting | Default | What it does |
| --- | --- | --- |
| `auricFiles.related.enabled` | `true` | Resolve companions for the active file |
| `auricFiles.related.testDirectories` | `__tests__`, `tests`, `test`, `spec` | Folders searched when tests live apart from the source |
| `auricFiles.related.storyExtensions` | `.stories.tsx`, `.stories.jsx`, `.stories.ts`, `.stories.js`, `.stories.svelte`, `.stories.mdx` | Story file suffixes, tried in order |
| `auricFiles.related.rules` | none | Your own relationships (below) |

## Add your own rules

A rule connects a source pattern to one or more target patterns. Add rules for conventions the presets do not know, such as a repository layer or a generated client.

```json
{
  "auricFiles.related.rules": [
    {
      "id": "api-client",
      "kind": "client",
      "label": "Generated API client",
      "from": "{dir}/{name}.service.ts",
      "to": ["{dir}/generated/{name}.client.ts"],
      "presets": []
    }
  ]
}
```

| Field | Required | Meaning |
| --- | --- | --- |
| `id` | Yes | Identifier; a built-in rule with the same id is replaced |
| `kind` | Yes | The relationship name shown beside the companion: one of the kinds above, or your own |
| `from` | Yes | Pattern matching the source file |
| `to` | Yes | Candidate targets in priority order. Navigation opens the first that exists; generation writes the first |
| `label` | No | Wording in related-file lists |
| `presets` | No | Presets the rule belongs to; empty applies everywhere |
| `templateId` | No | Template used when the companion is generated |

### Pattern tokens

| Token | Meaning |
| --- | --- |
| `{dir}` | Zero or more leading folders, captured |
| `{name}` | The file name without extensions, so `Button.test.tsx` is read as `Button` |
| `{ext}` | The extension without its dot; defaults to the source file's own |
| `{testDir}` | Each configured test folder, in order |
| `{storyExt}` | Each configured story extension, in order |
| `{mirrorDir}` | The source folder relocated under a test root (`src/ui` becomes `tests/ui`), and back again in reverse |
| `{a,b}` | A brace set, expanded into alternatives |

Rules are read backwards too: a file matching a `to` pattern resolves back to its `from` file. Relation rules come from workspace settings, so they only apply in a trusted workspace.

## Index

Related files are found through the workspace index. Until the index is built, Properties says **Not indexed yet**; run **Auric Files: Refresh** to build it.

With a component open, **Go to Related File…** lists its companions, and choosing one opens it.
