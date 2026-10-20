---
title: Auric Artisan Icon Pack — Troubleshooting
description: What to do when a pack member did not install, or when using alternative marketplaces or local builds.
product: VS Code extensions › Auric Artisan Icon Pack
updated: 2026-09-25
---

# Troubleshooting

| Symptom | Why it happens | What to do |
| --- | --- | --- |
| An included extension did not install. | A network problem, an organisation policy, or an older VS Code version blocked it. | Open the pack's **Extension Pack** section, find the missing member and check its installation error. Verify marketplace access and that VS Code is 1.85 or later. |
| I installed the pack VSIX offline and the members are missing. | A pack VSIX is not an offline bundle; it only lists the members. | Connect to the marketplace, or install each member's own VSIX. |
| I use an alternative marketplace and members are missing. | Each member must be published there under the same ID. | Check whether each member is available in your marketplace. Installing the pack does not move extensions between registries. |
| I installed local development builds and the pack reinstalls members. | VS Code identifies extensions by publisher and name, not folder name. | Confirm your builds use the exact IDs listed in the [reference](reference.md). |
| I only see one icon library view, not three. | Modern, Drawn and Playful merge into one library when co-installed. | This is expected. Use the **Library** filter to pick a collection. |
| An icon library view disappeared after installing Icon Studio. | Icon Studio hosts the Auric collections by default. | Set `auricIconStudio.hostFamilyLibraries` to `false` to show their views. |
| I want to remove one member. | Members are ordinary extensions. | Uninstall or disable it in the Extensions view. |

For problems inside a member extension, see that extension's troubleshooting page.
