---
title: Settings, Settings Sync and workspace trust for Auric Artisan extensions
description: Where Auric Artisan extension settings live, how to share them with a team, what Settings Sync carries between machines, and what each extension does in an untrusted folder.
product: VS Code extensions › Install and setup
updated: 2026-09-25
---

# Settings, sync and workspace trust

Every Auric Artisan extension is configured through normal VS Code settings, and three of them also read a project file you can commit to a repository. This page explains where each kind of setting lives and how they combine.

## User settings and workspace settings

VS Code keeps settings at several levels. A value at a more specific level wins.

| Level | Where it is stored | Applies to |
| --- | --- | --- |
| Default | Inside the extension | Everyone, until changed |
| User | Your personal `settings.json` | Every window you open, in the current profile |
| Workspace | `.vscode/settings.json` in the open folder, or the `.code-workspace` file | Only that folder or workspace |
| Folder | `.vscode/settings.json` in one folder of a multi-root workspace | Only that folder |

To edit them:

1. Open **File** › **Preferences** › **Settings** (`Ctrl` + `,`).
2. Choose the **User** or **Workspace** tab at the top.
3. Search for the extension's settings prefix, for example `auricLive`, or type `@ext:auric-artisan.auric-artisan-live` to show only that extension's settings.
4. To edit the JSON directly, run **Preferences: Open User Settings (JSON)** or **Preferences: Open Workspace Settings (JSON)**.

### Setting scope

Each setting declares a *scope*, which limits the levels where it can be set:

- **application** — user settings only. It applies to every window. Examples: all Auric Artisan Theme settings and the Emoji `auricEmoji.interfaceLanguage` setting.
- **window** — user or workspace settings. Most File System, Font Hub, icon-library and Studio settings use this scope, as do a few Live settings such as `auricLive.interfaceLanguage`.
- **resource** — user, workspace or folder settings, so each folder in a multi-root workspace can differ. Almost all Live settings and every Formatter setting use this scope.

The Settings editor only shows a setting under the tabs where it is allowed.

## Project configuration files

Three extensions also read a file in the project, so a repository can carry its own setup. A project file wins over VS Code settings for that project.

| Extension | Project files | Details |
| --- | --- | --- |
| Auric Artisan Live | `auric.live.json` (name set by `auricLive.configFile`), `.auricignore-live` | Keys are the setting names without the `auricLive.` prefix; comments and trailing commas are allowed |
| Auric Artisan Formatter | `.auricformatrc` (several forms), `auric.format.json`, an `auricFormatter` key in `package.json`, `.auricformatignore`; also reads Prettier files and `.editorconfig` | See the Formatter's configuration guide |
| Auric Artisan File System | Template folders, `.auric/templates` and `.vscode/templates` by default | Relationship rules and generator profiles live in settings |

## Sharing a setup with a team

1. Commit `.vscode/settings.json` with the workspace-level values you agree on.
2. Commit the project files above where they apply.
3. Recommend the extensions: create `.vscode/extensions.json` with their IDs. VS Code then offers to install them when someone opens the folder.

```json
{
  "recommendations": [
    "auric-artisan.auric-artisan-formatter",
    "auric-artisan.auric-artisan-live"
  ]
}
```

Settings with **application** scope cannot be shared this way; each person sets them in their own user settings.

## Settings Sync

VS Code Settings Sync copies your user-level setup between machines through your Microsoft or GitHub account. It is part of VS Code, not of the Auric extensions.

1. Select the Accounts icon in the Activity Bar and choose **Backup and Sync Settings…** (older versions say **Turn on Settings Sync…**).
2. Tick what to sync. **Extensions** and **Settings** matter here.
3. Sign in.

What happens to Auric Artisan extensions:

- **Installed extensions** sync, including whether each one is enabled or disabled.
- **User settings** sync, including every `auricLive.*`, `auricFormatter.*` and other Auric user-level value.
- **Workspace settings and project files do not sync.** They travel with the repository instead.
- **Stored extension data does not sync.** Favourites, recents, selections, likes, tags, groups, operation history and similar data that an extension keeps in VS Code's extension storage stay on the machine where you created them. The Auric extensions do not register any of this data for Settings Sync.

To stop one Auric setting from syncing, add its ID to the VS Code setting `settingsSync.ignoredSettings`. To stop one extension from syncing, add its ID to `settingsSync.ignoredExtensions`.

## Workspace trust

When you open a folder for the first time, VS Code may ask whether you trust its authors. In an untrusted folder, VS Code runs in *Restricted Mode*, and extensions that run code or read project configuration can limit themselves. You can change your answer later with **Workspaces: Manage Workspace Trust**.

- **Auric Artisan Live** — static serving, live reload and request inspection still work, on this machine only. Running commands, CGI (PHP), proxying, file-backed mocks, custom certificates and listening on your network need trust, even when a project file turns them on.
- **Auric Artisan File System** — browsing, search, filtering and related-file navigation still work. Creating, renaming, moving, duplicating and deleting files are disabled until you trust the folder.
- **Auric Artisan Formatter** — configuration files are read, but JavaScript configuration files and formatter plugins are not run.
- **Auric Artisan Font Hub** — fully supported. It only writes files after an explicit save or editor command.
- **Auric Artisan Theme, File Icons, Emoji, Icon Studio and Icon Hub** — fully supported.

For the other extensions, the **Manage Workspace Trust** page lists which installed extensions are limited or disabled in Restricted Mode.

## Remote and virtual workspaces

- Auric Artisan Live needs a real file system and a local port. It does not support virtual workspaces (folders opened from a remote repository without a local copy).
- Auric Artisan File System works in virtual workspaces with limits: revealing in the operating system's file manager, content hashing for duplicate detection and the native trash are not available there.
- Auric Artisan Formatter supports virtual workspaces.

After configuring, your values appear in the Settings editor under the tab you chose, and the extension uses them the next time it acts.
