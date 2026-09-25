---
title: Auric Artisan Studio — Choose what to install
description: Compare the four Studio extensions, see what each install shape gives you, and learn which extension owns which feature when several are installed.
product: VS Code extensions › Auric Artisan Studio
updated: 2026-09-25
---

# Choose what to install

Auric Artisan Studio is four Marketplace extensions. Three of them contain code and do one job each; the fourth is an extension pack that installs the other three. You can install any combination. This page explains what each shape gives you.

## The four extensions at a glance

| | Auric Color | Auric Accessibility | Auric Code Health | Full Pack |
| --- | --- | --- | --- | --- |
| Marketplace ID | `auric-artisan.auric-color` | `auric-artisan.auric-a11y` | `auric-artisan.auric-codehealth` | `auric-artisan.auric-artisan` |
| Main job | Colour picking, palettes, contrast | WCAG linting and project audits | Secrets, security and hygiene checks | Installs the other three |
| Activity Bar views | Overview, Color Picker | Overview, Project Issues, Color Picker (when colour is installed) | Overview | None of its own |
| Studio spaces (on its own) | Color, Check (Contrast), Brand, Settings | Home, Check (Findings, Contrast, Preview), Settings | Health, Settings | All spaces |
| Keyboard shortcuts | Command Center, Pick / edit color | Command Center, Inspect | Command Center | Those of its members |
| Settings | 16 under `auricColor.` | 24 under `auricA11y.` | 28 under `auricCodeHealth.` | None of its own |

## What each extension does when installed alone

### Auric Color alone

- Colour hovers, swatches and pickers in more than 40 languages.
- Contrast diagnostics (underlines, quick fixes and **Fix All Contrast Issues in File**) in stylesheets, markup and components.
- The Studio opens on the **Color** space (Palette, Shades, Vision), with **Check › Contrast**, **Brand** and **Settings**.
- The Overview is a colour workbench: the file you are editing, suggestions about that file, a brand swatch row, your recent colours, **Open the color picker** and shortcuts to the Studio tools.
- There is no **Scan project** button. The status-bar score still appears once the Studio has graded the workspace in the background while you edit.

### Auric Accessibility alone

- WCAG diagnostics for markup and CSS, Inspect cards on hover, contrast diagnostics and quick fixes.
- **Scan Project for Accessibility**, the **Project Issues** view and the status-bar score.
- The Studio opens on **Home**, with **Check** (Findings, Contrast, Preview) and **Settings**.
- The agent-ready remediation plan.
- Project scans also run the code-health checks, so code-health findings appear in the Project Issues view and in reports. Code-health underlines in the editor need Auric Code Health.

### Auric Code Health alone

- Code-health underlines and quick fixes in every supported language.
- The Overview is a hygiene report: a code-health ring, seven category chips, **Report** and **health.json + SARIF**.
- The Studio opens on the **Health** space, with **Settings**.
- **Generate Project Health Report**, **Write Health Record**, the remediation plan and the command-line scanner.
- The status-bar item reads `Health` and shows the code-health score.

### The Full Pack, or any two together

When two or three code-bearing extensions are installed, they combine into one Workstation. One of them hosts a single sidebar and one Studio that contains every installed capability; the others hide their own views. See [The Workstation](workstation.md).

## Who owns which feature

When several extensions are installed, each editor-wide feature has exactly one owner, so you never see a colour swatch drawn twice or the same problem listed three times in the Problems panel.

| Feature | Owner |
| --- | --- |
| Colour swatches, colour hover and inline picker, click-to-pick, VS Code colour decorator handling | Auric Color only |
| Inspect cards on elements and CSS rules | Auric Accessibility only |
| WCAG diagnostics | Auric Accessibility only |
| Code-health diagnostics | Auric Code Health only |
| Contrast diagnostics | Auric Accessibility; Auric Color when Auric Accessibility is not installed |
| Status-bar score, live re-grading as you type, automatic background scans | The first installed of Auric Accessibility, then Auric Color, then Auric Code Health |

Commands you run yourself, such as **Scan Project for Accessibility** or **Write Health Record**, are never restricted: any installed extension that has the command can run it.

## Install commands

```text
code --install-extension auric-artisan.auric-artisan
code --install-extension auric-artisan.auric-color
code --install-extension auric-artisan.auric-a11y
code --install-extension auric-artisan.auric-codehealth
```

## Changing your mind later

You can add or remove any extension at any time from the Extensions view. The Workstation re-elects its host immediately, without reloading the window: views appear or hide, the Studio rebuilds its spaces and the Command Center lists the new set of actions. See [Manage the pack's members](../full-pack/docs/managing-members.md).

## Related

- [The Workstation](workstation.md)
- [Full Pack overview](../full-pack/README.md)
- [Reference](reference.md) for every command and setting per extension.
