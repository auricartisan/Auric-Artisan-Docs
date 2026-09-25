---
title: The two Auric Artisan extension packs
description: What the Icon Pack and the Studio Full Pack install, how to install them, and how to keep only the parts you want.
product: VS Code extensions › Install and setup
updated: 2026-09-25
---

# The two extension packs

An *extension pack* is an extension that contains no features of its own. It lists other extensions, and installing it installs all of them. Auric Artisan publishes two.

| Pack | Extension ID | Installs | Minimum VS Code |
| --- | --- | --- | --- |
| Auric Artisan Icon Pack | `auric-artisan.auric-artisan-icon-pack` | Auric Icons: Modern, Auric Icons: Playful, Auric Artisan Emoji, Auric Icons: Drawn | 1.85 |
| Auric Artisan Studio — Full Pack | `auric-artisan.auric-artisan` | Auric Color, Auric Accessibility, Auric Code Health | 1.74 |

Note the Full Pack's ID: it is the bare `auric-artisan.auric-artisan`, not `auric-artisan.auric-artisan-studio`.

## Icon Pack

The Icon Pack installs the four creative libraries together:

- Auric Icons: Modern — `auric-artisan.auric-artisan-modern-icon`
- Auric Icons: Drawn — `auric-artisan.auric-icons-drawn`
- Auric Icons: Playful — `auric-artisan.auric-icons-playful`
- Auric Artisan Emoji — `auric-artisan.auric-artisan-emoji`

The pack adds nothing of its own. Each library keeps its own commands and settings. When more than one icon collection is installed, they merge into one Icon Studio instead of adding separate sidebars.

## Studio Full Pack

The Full Pack installs the three focused Studio extensions:

- Auric Color — `auric-artisan.auric-color`
- Auric Accessibility — `auric-artisan.auric-a11y`
- Auric Code Health — `auric-artisan.auric-codehealth`

You can enable or disable each of the three independently.

## Install a pack

1. Open the Extensions view (`Ctrl` + `Shift` + `X`).
2. Search for the pack's ID with the `@id:` prefix, for example `@id:auric-artisan.auric-artisan-icon-pack`.
3. Select **Install**. VS Code installs the pack and every extension it lists.

Or, in a terminal:

```text
code --install-extension auric-artisan.auric-artisan-icon-pack
code --install-extension auric-artisan.auric-artisan
```

The pack's page in the Extensions view has an **Extension Pack** tab that lists its members.

## Keep only some members

- **Disable a member you do not want.** Find it in the Extensions view and select **Disable**. The rest of the pack keeps working.
- **Uninstall a member.** You can uninstall an individual member. VS Code may reinstall it if you later reinstall or update the pack.
- **Remove the whole set.** Uninstalling a pack offers to uninstall the extensions it installed as well. Read the prompt and choose accordingly.
- **Install members individually instead.** If you only want one or two, skip the pack and install those IDs directly.

## Packs and VSIX files

A pack installed from a VSIX file only fetches its members if the editor can reach the Visual Studio Marketplace. In Cursor, Windsurf, VSCodium or an offline machine, install each member's VSIX. See [Install from a VSIX file](install-from-vsix.md).

After installing a pack, the Extensions view lists the pack and each of its members under **Installed**.
