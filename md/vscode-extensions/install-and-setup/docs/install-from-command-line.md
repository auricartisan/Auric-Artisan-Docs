---
title: Install Auric Artisan extensions from the command line
description: Use the VS Code command-line launcher to install, list, update and remove Auric Artisan extensions, including all seventeen at once.
product: VS Code extensions › Install and setup
updated: 2026-09-25
---

# Install from the command line

VS Code ships a command-line launcher called `code`. It can install and remove extensions without opening the Extensions view, which is useful for setting up a new machine, scripting a team's setup, or installing all seventeen Auric Artisan extensions in one go. It downloads from the Visual Studio Marketplace, so it needs a network connection.

## Make sure `code` is available

- **Windows and Linux.** The installer normally adds `code` to your `PATH`. Open a new terminal and run `code --version`.
- **macOS.** In VS Code, open the Command Palette (`Cmd` + `Shift` + `P`) and run **Shell Command: Install 'code' command in PATH**, then open a new terminal.
- **VS Code Insiders** uses `code-insiders` instead of `code`.

If `code --version` prints a version number, you are ready.

## Install one extension

1. Open a terminal.
2. Run `code --install-extension` followed by the extension ID:

   ```text
   code --install-extension auric-artisan.auric-artisan-formatter
   ```

3. Wait for the message that the extension was successfully installed.
4. If VS Code is already open, the extension appears under **Installed** in the Extensions view. Reload the window (**Developer: Reload Window**) if it does not show at once.

## Install the two packs

```text
code --install-extension auric-artisan.auric-artisan-icon-pack
code --install-extension auric-artisan.auric-artisan
```

The first installs Auric Icons: Modern, Drawn and Playful and Auric Artisan Emoji. The second installs Auric Color, Auric Accessibility and Auric Code Health. See [The two extension packs](extension-packs.md).

## Install all seventeen

This is the same grouped list the Auric Artisan VS Code page offers. You can paste the lines into a terminal one group at a time, or all at once.

```text
# Themes and file icons
code --install-extension auric-artisan.auric-artisan-theme
code --install-extension auric-artisan.auric-artisan-file-icon

# Icons and emoji. The Icon Pack alone installs Modern, Drawn, Playful and Emoji.
code --install-extension auric-artisan.auric-artisan-icon-pack
code --install-extension auric-artisan.auric-artisan-modern-icon
code --install-extension auric-artisan.auric-icons-drawn
code --install-extension auric-artisan.auric-icons-playful
code --install-extension auric-artisan.auric-artisan-emoji
code --install-extension auric-artisan.auric-artisan-icon-studio
code --install-extension auric-artisan.auric-artisan-icon-lib

# Colour, accessibility and code health. The Full Pack alone installs all three.
code --install-extension auric-artisan.auric-artisan
code --install-extension auric-artisan.auric-color
code --install-extension auric-artisan.auric-a11y
code --install-extension auric-artisan.auric-codehealth

# Workspace tools
code --install-extension auric-artisan.auric-artisan-live
code --install-extension auric-artisan.auric-artisan-file-system
code --install-extension auric-artisan.auric-artisan-font-hub
code --install-extension auric-artisan.auric-artisan-formatter
```

Lines that begin with `#` are comments; most shells ignore them. In Windows Command Prompt, remove the comment lines before pasting.

Installing an extension that a pack has already installed does nothing harmful: `code` reports that it is already installed.

## Other useful flags

These are standard VS Code launcher flags. They work the same for every extension.

| Command | What it does |
| --- | --- |
| `code --install-extension <id>` | Install the latest version of an extension |
| `code --install-extension <id>@<version>` | Install a specific published version, for example `auric-artisan.auric-artisan-live@0.2.0` |
| `code --install-extension <id> --force` | Update an installed extension to the latest version without a prompt |
| `code --install-extension <path-to-file>.vsix` | Install from a downloaded VSIX file |
| `code --list-extensions` | List the IDs of every installed extension |
| `code --list-extensions --show-versions` | List installed extensions with their versions |
| `code --uninstall-extension <id>` | Remove an extension |

To see only the Auric Artisan extensions you have installed, filter the list. In PowerShell:

```text
code --list-extensions --show-versions | Select-String auric-artisan
```

In a POSIX shell such as bash or zsh:

```text
code --list-extensions --show-versions | grep auric-artisan
```

## Profiles

VS Code profiles keep separate sets of extensions and settings. The launcher installs into the default profile unless you name one with `--profile "<profile name>"`. If an extension seems missing after a command-line install, check which profile the VS Code window is using (the gear menu at the bottom of the Activity Bar shows it).

The IDs are listed with their minimum VS Code versions in the [reference](reference.md). When a command succeeds you see a line saying the extension was successfully installed, and the extension appears in the Extensions view.
