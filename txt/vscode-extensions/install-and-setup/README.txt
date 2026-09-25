==============================================================================
INSTALL AND SET UP THE AURIC ARTISAN VS CODE EXTENSIONS
==============================================================================
How to install, update, disable, remove and configure any of the seventeen
Auric Artisan extensions for Visual Studio Code.
Area: VS Code extensions › Install and setup   Updated: 2026-09-25

Auric Artisan publishes seventeen extensions for Visual Studio Code under the
publisher name `auric-artisan`. They cover colour themes, file icons, icon and
emoji libraries, colour and accessibility tooling, code health, a live
development server, a file workspace, a font hub and a code formatter. Every
extension is free and installs on its own. Two of them are extension packs: a
pack contains no features of its own and simply installs a group of other
extensions in one step.

This folder covers everything that is the same for all seventeen: finding and
installing an extension, installing from the command line or from a VSIX file,
using the packs, installing in editors built on VS Code (Cursor, Windsurf,
VSCodium), updating, disabling and removing, where settings live, how Settings
Sync treats them, switching the interface to Hindi where an extension supports
it, and where to report a problem.

The guides for what each extension does live in that extension's own folder.
This folder only gets you to the point where the extension is installed and
configured the way you want.

WHO IT IS FOR
=============

  - Anyone installing an Auric Artisan extension for the first time.
  - Teams that want to install the same set of extensions on several machines,
    or share settings through a repository.
  - People using Cursor, Windsurf, VSCodium or another editor based on VS
    Code.
  - Anyone who needs to update, roll back, disable or remove an extension, or
    report a problem.

WHERE TO FIND THE EXTENSIONS
============================

  - The Visual Studio Marketplace, publisher `auric-artisan`. Each extension
    has a page at
    `https://marketplace.visualstudio.com/items?itemName=<extension ID>`.
  - The Auric Artisan VS Code page: https://auricartisan.com/vscode/
  - Inside VS Code: the Extensions view (`Ctrl` + `Shift` + `X`).

The full list of extension IDs, with the minimum VS Code version each one
needs, is in the reference [docs/reference.txt].

To install from a terminal, pass the extension ID to the VS Code command-line
launcher:

    code --install-extension auric-artisan.auric-artisan-live

QUICK START
===========

  1. Open VS Code and check its version under Help › About (on macOS, Code ›
     About Visual Studio Code). Compare it with the minimum in the reference
     [docs/reference.txt].
  2. Open the Extensions view with `Ctrl` + `Shift` + `X`.
  3. Type the exact ID with the `@id:` prefix, for example
     `@id:auric-artisan.auric-artisan-formatter`, and clear any other filter
     such as `@installed`.
  4. Check that the publisher shown under the name is Auric Artisan
     (`auric-artisan`), then select Install.
  5. Open the Command Palette (`Ctrl` + `Shift` + `P`) and type the
     extension's command prefix, for example `Auric Formatter`, to see its
     commands.
  6. Open File › Preferences › Settings and search for the extension's setting
     prefix (for example `auricFormatter`) to review its options.
  7. If VS Code asks whether you trust the folder you opened, read Settings,
     sync and workspace trust [docs/settings-and-sync.txt] before you answer:
     several extensions limit what they do in an untrusted folder.

WHAT YOU CAN DO
===============

  - Install any extension from the Extensions view, the command line or a VSIX
    file.
  - Install a whole group in one step with the Icon Pack or the Studio Full
    Pack.
  - Install in Cursor, Windsurf, VSCodium and other editors based on VS Code.
  - Update, roll back to an earlier version, disable or uninstall an
    extension.
  - Choose between user settings and workspace settings, and share a
    configuration with a team.
  - Keep extensions and settings in step across machines with VS Code Settings
    Sync.
  - Use the extensions in Hindi where they support it: Auric Artisan Live,
    Auric Artisan Theme and Auric Artisan Emoji.
  - Get support, with the information support needs.

IN THIS FOLDER
==============

  - docs/ [docs/README.txt] — the guides.
    - Getting started: install from the Extensions view
      [docs/getting-started.txt]
    - Install from the command line [docs/install-from-command-line.txt]
    - Install from a VSIX file [docs/install-from-vsix.txt]
    - The two extension packs [docs/extension-packs.txt]
    - Cursor, Windsurf, VSCodium and other editors
      [docs/forks-and-other-editors.txt]
    - Update, disable and uninstall [docs/update-disable-uninstall.txt]
    - Settings, sync and workspace trust [docs/settings-and-sync.txt]
    - Use an extension in Hindi [docs/display-language-hindi.txt]
    - Get support [docs/get-support.txt]
    - Reference: all seventeen extension IDs [docs/reference.txt]
    - Troubleshooting [docs/troubleshooting.txt]
    - FAQ [docs/faq.txt]
  - others/ [others/README.txt] — supporting material.
    - Glossary [others/glossary.txt]
    - Shortcuts and commands [others/shortcuts.txt]
    - Compatibility and limits [others/limits-and-accuracy.txt]
    - Privacy [others/privacy.txt]
    - Related extensions and pages [others/related.txt]
