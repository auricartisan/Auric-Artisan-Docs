---
title: Full Pack — Manage the pack's members
description: Enable, disable, update and uninstall the extensions the Full Pack installs, and see what the Workstation does in each case.
product: VS Code extensions › Auric Artisan Studio › Full Pack
updated: 2026-09-25
---

# Manage the pack's members

The Full Pack is a convenience bundle, not a single product. Its three members are ordinary extensions, so VS Code's usual controls work on each one separately.

## Disable a member

1. Open the Extensions view (`Ctrl` + `Shift` + `X`).
2. Find the member, for example **Auric Code Health — Secrets, TODOs & Risk**.
3. Select the gear icon, then **Disable** (for all workspaces) or **Disable (Workspace)** (for this workspace only).
4. If VS Code asks you to restart extensions or reload the window, do so.

The other members keep working. To turn it back on, choose **Enable** or **Enable (Workspace)** in the same menu.

## Uninstall a member

1. In the Extensions view, select the gear icon on the member.
2. Select **Uninstall**.

The pack and the other members stay installed. To get the member back, install it again by its ID, or reinstall the pack.

## Update members

Members update like any other extension, automatically if you have auto-update on, or from the Extensions view. All Studio extensions share one version number, so keeping them on the same version avoids surprises in the shared `.auric-artisan` folder.

## What the Workstation does when members change

The Workstation re-elects its host as soon as the set of installed or enabled members changes, without a reload. Views appear or hide, an open Studio tab rebuilds with the new spaces, and diagnostics move to their new owner.

| Members left | Host | What you lose |
| --- | --- | --- |
| All three | Auric Accessibility | Nothing |
| Accessibility and Color | Auric Accessibility | Code-health underlines, the Health space, **Report**, **SARIF**, the CI gate card; project scans still list code-health findings |
| Accessibility and Code Health | Auric Accessibility | Colour hovers, swatches and pickers, **Fix All Contrast Issues in File**, the Color and Brand spaces, recent colours |
| Color and Code Health | Auric Color | WCAG diagnostics, Inspect, the Project Issues view, **Scan project**, the Home space; the Overview becomes the colour workbench |
| Accessibility only | Auric Accessibility | Everything colour-specific and code-health underlines |
| Color only | Auric Color | Everything accessibility- and code-health-specific |
| Code Health only | Auric Code Health | Everything colour- and accessibility-specific |

Contrast diagnostics move to Auric Color when Auric Accessibility is removed, and back when it returns.

## Uninstall the pack

Select the gear icon on **Auric Artisan Studio — Full Pack** and choose **Uninstall**. Afterwards, check the **Installed** list in the Extensions view to see which members remain, and uninstall any you no longer want.

Uninstalling extensions does not delete the `.auric-artisan` folder from your workspaces. Delete it yourself if you no longer need it.

## Related

- [The Workstation](../../docs/workstation.md)
- [Choose what to install](../../docs/choosing-an-install.md)
- [Troubleshooting](troubleshooting.md)
