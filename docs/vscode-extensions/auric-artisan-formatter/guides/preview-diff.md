---
title: Auric Artisan Formatter — preview formatting as a diff
description: See the formatted result beside your source in a read-only editor, compare the changes, and apply or discard them.
product: VS Code extensions › Auric Artisan Formatter
updated: 2026-09-25
---

# Preview formatting as a diff

The native preview shows what formatting would do before your file changes. It opens a read-only copy of the formatted result in a normal VS Code editor beside your source; no Studio panel opens.

## Open a preview

1. Focus the source file in the editor.
2. Use any of these:
   - **Auric Formatter: Preview Formatting as a Diff** (`Ctrl` + `Alt` + `Shift` + `F`; `Cmd` + `Alt` + `Shift` + `F` on macOS);
   - the **Preview Formatting as a Diff** button in the editor title bar;
   - right-click with nothing selected and choose **Preview Formatting as a Diff**;
   - **Preview beside editor** in Formatter Studio.
3. A read-only tab named **Preview — *file name*** opens beside the source, with the same language highlighting.

With text selected, only the selection is formatted in the preview (it may grow to a complete syntax unit).

If formatting fails or the safety gate refuses the change, no preview opens and a warning says why, for example **Auric Formatter: the safety gate refused this change**.

## Act on the preview

The preview shows CodeLens links at the top and buttons in the editor title bar:

| Control | What it does |
| --- | --- |
| **Apply formatting** | Replace the source with the preview, after confirming **Apply formatting to *file*?** (**The source stays unsaved. You can undo this edit.**) |
| **Compare changes** | Open VS Code's diff editor, **Formatting changes — *file***, source on the left and result on the right |
| **Discard preview** | Close the preview; the source is unchanged |
| **Full file · refresh preview** (or **Selection preview · refresh from source**) | Format the source again and update the preview |

When the result is the same as the source, the first CodeLens reads **No formatting changes** and opens the comparison instead.

The same actions are commands: **Apply Formatting Preview**, **Compare Formatting Changes**, **Discard Formatting Preview** and **Refresh Formatting Preview**. The title-bar buttons appear only while a preview is focused.

## Stale previews

The preview is tied to the exact version of your source. If you edit the source after opening it:

- the CodeLens changes to **Source changed — refresh preview**;
- **Apply** and **Compare** refuse with **The source changed. Refresh the preview before applying.**

Refresh, review again, then apply. A preview can never overwrite a different document or a newer version of the same one.

## Limits

- Up to 24 previews can be open at once; beyond that you are asked to close or discard one first.
- Focus the source editor, not a preview, before creating a preview: **focus the source editor to create a preview.**
- If you close the source file, **Refresh** asks you to reopen it.

After **Apply formatting**, the source shows the formatted text, unsaved, and the preview closes.
