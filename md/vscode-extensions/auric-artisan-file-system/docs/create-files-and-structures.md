---
title: Auric Artisan File System — create files and structures
description: Create single files and folders, sibling and child files, and whole nested structures in one line with braces and ranges.
product: VS Code extensions › Auric Artisan File System
updated: 2026-09-25
---

# Create files and structures

All creation commands are in the **Create** group of the workspace panel, the **Auric Files** › **Create** submenu and the Command Palette. They need a trusted workspace.

| Command | Use it to |
| --- | --- |
| **New File…** | Create one file (or a folder, with a trailing `/`) |
| **New Folder…** | Create one folder, including nested paths |
| **New Sibling File** | Create a file next to the selected file |
| **New Child File** | Create a file inside the selected folder |
| **Batch Create Files…** | Create many files from comma-separated paths |
| **Batch Create Folders…** | Create many folders from comma-separated paths |
| **Batch Structure…** | Type a mixed structure of files and folders |
| **New File from Template…** | Create from a template. See [Templates and generators](templates-and-generators.md) |
| **New from Framework Preset…** | Create from a preset or custom generator. See [Templates and generators](templates-and-generators.md) |
| **Create Related Files…** | Create a file's test, style, story and other companions. See [Related files](related-files.md) |

For creation directly in the root of a single-folder workspace, use the native Explorer's **New File** and **New Folder**; the panel's target actions need a file or subfolder as their target.

## New file or folder

1. Run **Auric Files: New File…** (`Ctrl` + `N` with the Explorer focused) or **New Folder…** (`Ctrl` + `Shift` + `N`).
2. **Choose the destination folder.** The first entry is the current target; the rest are folders in the workspace.
3. Type the name. For **New File…**, a trailing `/` creates a folder. Nested paths such as `components/ui/Button.tsx` create the missing folders too (turn this off with `auricFiles.create.createIntermediateDirs`).
4. If `auricFiles.create.defaultTemplate` names a template, the new file is filled from it; otherwise it is empty.
5. The file opens in the editor (`auricFiles.create.openAfterCreate`), with the cursor at the template's cursor marker if it has one.

These are Auric's versions of the Explorer shortcuts while the Explorer has focus. VS Code's own **New File** and **New Folder** buttons in the Explorer title bar are unchanged.

## Sibling and child files

- **New Sibling File** creates a file in the same folder as the selected file. It is offered for files.
- **New Child File** creates a file inside the selected folder. It is offered for folders.

## Batch creation

Batch creation turns one line of text into many paths.

1. Run **Batch Create Files…**, **Batch Create Folders…** or **Batch Structure…** (`Ctrl` + `Alt` + `B` with the Explorer focused).
2. Choose the destination folder.
3. Type the paths (see the syntax below). Mistakes are reported as you type.
4. For files, **Choose the content used for every new file**: **Empty files**, the configured default template, or any template.
5. Review the preview. It lists every path as **Ready to create** or **Already exists — the configured conflict policy will apply**, with a summary such as **6 items planned · 1 conflict**. Untick anything to skip and press `Enter`.
6. If the operation touches at least `auricFiles.safety.confirmBulk` paths (5 by default), confirm **Create *N* items?**.

### Syntax

| You type | You get |
| --- | --- |
| `a.ts, b.ts` | Two files; commas separate targets |
| `src/lib/util.ts` | A nested path; missing folders are created |
| `docs/` | A folder (trailing slash) |
| `folder:assets` | A folder, stated explicitly |
| `file:LICENSE` | A file, stated explicitly |
| `src/{Button,Card}/index.ts` | `src/Button/index.ts` and `src/Card/index.ts` |
| `src/{Button,Card}/{index.ts,styles.css}` | Four files: every combination |
| `tests/case-{1..3}.ts` | `case-1.ts`, `case-2.ts`, `case-3.ts` |
| `tests/case-{01..03}.ts` | `case-01.ts`, `case-02.ts`, `case-03.ts` (leading zeros keep the width) |
| `step-{0..10..5}.md` | `step-0.md`, `step-5.md`, `step-10.md` (a step size) |
| `section-{a..c}.md` | `section-a.md`, `section-b.md`, `section-c.md` (letters) |
| `a\{1\}.ts` | A file literally named `a{1}.ts`; a backslash before a brace or comma makes it literal |
| `src\components\Button.tsx` | Backslashes elsewhere are treated as folder separators, so Windows paths work |

Each line can hold several comma-separated targets, and you can type several lines. Braces that are neither a list nor a range, such as `{png}`, are kept literally.

To take the input literally, with no brace expansion, turn off `auricFiles.create.expandBraces`.

### Limits

- One target may expand to at most 1,000 paths; beyond that it is rejected with **expands to more than 1000 paths**.
- One batch creates at most 2,000 paths; it stops with **Stopped after 2000 paths; narrow the input and try again**.
- Duplicate paths in the input are created once.
- Invalid names (for example characters Windows does not allow) are reported and skipped.

## What happens to existing files

A path that already exists is a *conflict*. The preview marks it, and the configured conflict policy decides the outcome; nothing is overwritten silently. Paths matching `auricFiles.safety.protectedPaths` cannot be touched at all.

Every creation is recorded in the operation history, so **Undo Last File Operation** can reverse it.

When a batch finishes, the new folders and files appear in the Explorer and the first new file opens in the editor.
