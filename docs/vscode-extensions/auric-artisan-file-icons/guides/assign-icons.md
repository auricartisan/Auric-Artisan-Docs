---
title: Auric Artisan File Icons — Assign icons to files and folders
description: Give a file, folder, extension or pattern its own icon from the Explorer or in settings, and clear it again.
product: VS Code extensions › Auric Artisan File Icons
updated: 2026-09-25
---

# Assign icons to files and folders

An **association** tells the icon theme which icon to show for a name. You can create associations from the Explorer or write them in settings.

## From the Explorer

The Explorer actions appear when one of the Auric Artisan File Icons themes is active.

1. Right-click a file or folder in the Explorer.
2. Open **Auric File Icons** and select **Set File or Folder Icon**.
3. Choose the scope:

| Resource | Scope options |
| --- | --- |
| A file, for example `app.config.ts` | **Exact filename**, **All \*.config.ts files**, **Only parent/\*.config.ts**, **Only parent/app.config.ts** |
| A file with no extension | **Exact filename**, **Only parent/name** |
| A folder | **All folders named "…"**, **Only "parent/folder"** |
| A workspace root folder | No choice: it is set as a workspace-root association. |

4. Choose an icon from the list (titled **Set icon for …**). Search by name or ID. The list shows icons for the Modern style when Modern is active, otherwise Facet's icons.
5. VS Code confirms, for example "TypeScript assigned to All \*.config.ts files." Select **Reload** when asked.

Associations made this way are saved in the workspace settings, so they apply to this project only.

### Clear an assignment

1. Right-click the same file or folder.
2. Open **Auric File Icons** › **Clear Custom File or Folder Icon**.
3. Choose the same scope you used. If there is nothing to clear for that scope, you see "No custom icon is assigned to …".

## In settings

Values are shipped icon IDs. The Explorer picker is the easiest way to find a valid ID.

```json
{
  "auricFileIcons.files.associations": {
    "*.feature": "test",
    "server/*.log": "log",
    "PROJECT_NOTES": "markdown"
  },
  "auricFileIcons.folders.associations": {
    "domain": "models",
    "app/domain": "database"
  },
  "auricFileIcons.folders.rootAssociations": {
    "my-monorepo": "packages"
  }
}
```

| Setting | Keys accepted |
| --- | --- |
| `auricFileIcons.files.associations` | `*.ext`, `parent/*.ext`, an exact filename, or `parent/name`. |
| `auricFileIcons.folders.associations` | A folder name, or `parent/folder`. Closed and open icons are applied together. |
| `auricFileIcons.folders.rootAssociations` | The name of a workspace root folder. |

- Use the value `none` to remove a built-in match.
- A parent pattern matches the **direct** parent only, not any folder higher up.

## Turn a detected project type into an icon

If smart detection recognises a folder (for example a Rust project), you can make that permanent:

1. Right-click the folder, open **Auric File Icons** and select **Apply Detected Folder Icon**.
2. The matching folder icon is assigned. If nothing is detected, you see "No project type was detected in this folder."

To do this for many folders, see [Scan the workspace](smart-detection.md#scan-the-workspace-for-folder-icons).

## Result

After a reload, the chosen files and folders show the icons you assigned in the active Auric style.
