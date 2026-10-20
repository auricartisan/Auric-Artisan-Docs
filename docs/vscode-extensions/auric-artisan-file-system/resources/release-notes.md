---
title: Auric Artisan File System — release notes
description: What changed in each published version of Auric Artisan File System.
product: VS Code extensions › Auric Artisan File System
updated: 2026-09-25
---

# Release notes

## 0.1.0 (11 September 2026)

The first Marketplace release.

### A new file workspace

- An editor-sized **Auric Files** workspace and a matching compact **Auric Files** section in the Explorer.
- File tools in seven searchable groups (**Create**, **Inspect & navigate**, **Edit & batch**, **Organise**, **Find & filter**, **History & recovery**, **Workspace**), with keyboard-operable sections that close their siblings, and **Collapse all**.
- Workspace summaries, the selected resource and a resource picker.
- VS Code's own Explorer and the **Quick Actions…** list are kept.

### Graphical Properties

- Compact Explorer hovers replace long metadata tooltips.
- A **Properties** view with **General**, **Organisation** and **Access & history** cards, path copying, tag editing and group actions.
- Index-dependent information and cached Git state are labelled; unavailable owner and permission details are never made up.

### Cleaner menus and safer targeting

- One **Auric Files** submenu on Explorer and editor context menus, with **File Properties** kept directly in the Explorer menu.
- Multi-selection in the Explorer is kept when opening the workspace.
- A selection outside the workspace can no longer fall back to a different file for file actions.
- Icon tools for the optional Facet and Playful icon themes.

### File-system capabilities

- Native Explorer creation, rename, sorting, multi-selection and file badges.
- Structured batch creation, templates and ten framework presets.
- Related-file discovery and generation.
- Guarded move, copy and duplicate, batch rename, extension conversion, compare and merge, and selection export.
- Search, filters, duplicate and empty-file review, tags, groups and profiles.
- Undo and redo of operations, the workspace trash and restoration.
