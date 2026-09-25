---
title: Install an Auric Artisan extension from a VSIX file
description: Download an Auric Artisan extension as a VSIX package and install it in VS Code or an editor that cannot reach the Visual Studio Marketplace.
product: VS Code extensions › Install and setup
updated: 2026-09-25
---

# Install from a VSIX file

A *VSIX file* is the package format for VS Code extensions: a single file ending in `.vsix` that contains everything the extension needs. Installing from a VSIX is the route to use when your editor cannot reach the Visual Studio Marketplace, for example Cursor, Windsurf or VSCodium, or a machine with restricted network access.

## When to use this route

- Your editor is based on VS Code but searches a different gallery (see [Cursor, Windsurf, VSCodium and other editors](forks-and-other-editors.md)). The Auric Artisan extensions are published only on the Visual Studio Marketplace; they are not on Open VSX.
- You need to install on a computer without direct Marketplace access.
- You want to keep a copy of a specific version.

A VSIX installed this way does not update itself from the Marketplace in an editor that cannot reach it. You repeat these steps for each new version.

## Step 1: download the VSIX

Every published version of every Auric Artisan extension can be downloaded from the Marketplace at an address of this form:

```text
https://marketplace.visualstudio.com/_apis/public/gallery/publishers/auric-artisan/vsextensions/<extension-name>/<version>/vspackage
```

- `<extension-name>` is the part of the ID after `auric-artisan.`, for example `auric-artisan-live`.
- `<version>` is the version number, for example `0.2.1`. The versions available at the time of writing are in the [reference](reference.md). The **Version History** tab of the extension's Marketplace page lists every version.

For example, to download Auric Artisan Live 0.2.1:

```text
https://marketplace.visualstudio.com/_apis/public/gallery/publishers/auric-artisan/vsextensions/auric-artisan-live/0.2.1/vspackage
```

Open the address in a browser, or download it from a terminal. Save the file with a `.vsix` extension, for example `auric-artisan-live-0.2.1.vsix`. Some browsers save it without an extension; rename it if so.

> **Note:** An extension pack only lists other extensions. Installing a pack from a VSIX in an editor that cannot reach the Marketplace does not fetch its members. Download and install each member's VSIX instead. The members are listed in [The two extension packs](extension-packs.md).

## Step 2: install the file

Use any one of these three methods.

**From the Command Palette**

1. Open the Command Palette with `Ctrl` + `Shift` + `P`.
2. Run **Extensions: Install from VSIX…**.
3. Choose the `.vsix` file and select **Install**.

**From the Extensions view**

1. Open the Extensions view with `Ctrl` + `Shift` + `X`.
2. Select the **…** (Views and More Actions) menu at the top of the view.
3. Choose **Install from VSIX…** and pick the file.

**From a terminal**

```text
code --install-extension auric-artisan-live-0.2.1.vsix
```

Use the launcher for your editor if it is not VS Code. See [Cursor, Windsurf, VSCodium and other editors](forks-and-other-editors.md).

## Step 3: confirm

1. Open the Extensions view and select **Installed**.
2. Find the extension and check the version on its page.
3. Open the Command Palette and type the extension's command prefix (listed in [Getting started](getting-started.md)).

## Things to know

- **Minimum editor version.** A VSIX still declares the lowest VS Code version it supports. If your editor reports an older VS Code version, installation fails with a message that the extension is not compatible. See [Troubleshooting](troubleshooting.md).
- **Replacing a version.** Installing a VSIX of a different version replaces the installed one. You may be asked to reload the window.
- **Only download from the Marketplace or Auric Artisan.** A VSIX runs code on your machine. Get it from the Marketplace address above, or from Auric Artisan support.

When this works, the extension is listed under **Installed** with the version you downloaded, and its commands appear in the Command Palette.
