---
title: Full Pack — Troubleshooting
description: Problems with installing, updating or removing the Auric Artisan Studio Full Pack, and what to do.
product: VS Code extensions › Auric Artisan Studio › Full Pack
updated: 2026-09-25
---

# Full Pack troubleshooting

For problems with the Studio's features, see the [Studio troubleshooting page](../../docs/troubleshooting.md).

### The pack installed but I see only one Auric icon

**Why:** The three members form one Workstation hosted by Auric Accessibility; the other two hide their own views.

**What to do:** Nothing is wrong. Use the **Auric Accessibility** sidebar; it includes colour and code health. See [The Workstation](../../docs/workstation.md).

### One member is missing after installing the pack

**Why:** The member failed to install (for example, a network interruption while VS Code downloaded it), or it was uninstalled or disabled later.

**What to do:** Open the Extensions view, search for the member's ID (`auric-artisan.auric-color`, `auric-artisan.auric-a11y` or `auric-artisan.auric-codehealth`), and install or enable it.

### The pack will not install

**Why:** Your VS Code is older than 1.74, or VS Code cannot reach the Marketplace.

**What to do:** Update VS Code, check your connection or proxy, and try again. Offline, install each member's package file with **Extensions: Install from VSIX…** instead.

### I only want some of the tools

**What to do:** Disable or uninstall the members you do not need; the others keep working. See [Manage the pack's members](managing-members.md). Or uninstall the pack and install only the extension you want.

### Members show different versions

**Why:** One member updated before the others.

**What to do:** Update all three from the Extensions view so they share one version.

### After uninstalling the pack, the tools are still there

**Why:** The members are separate extensions and may remain installed.

**What to do:** Uninstall the remaining members from the Extensions view if you no longer want them.
