---
title: Auric Artisan Theme — Getting started
description: Install the theme, switch to an Auric variant, tour Theme Studio and make your first live customisation.
product: VS Code extensions › Auric Artisan Theme
updated: 2026-09-25
---

# Getting started with Auric Artisan Theme

This guide takes you from installation to a first saved customisation in a few minutes.

## Before you begin

- You need Visual Studio Code 1.75 or later.
- The extension works in untrusted and virtual workspaces.
- Customisations only apply while one of the Auric Artisan themes is active. If another theme is active, the customisation commands ask you to pick an Auric theme first.

## 1. Install the extension

1. Open the Extensions view with `Ctrl` + `Shift` + `X`.
2. Search for **Auric Artisan Theme** (publisher **auric-artisan**).
3. Select **Install**.

You can also run this in a terminal:

```text
code --install-extension auric-artisan.auric-artisan-theme
```

After installation, VS Code may show the **Make it yours** walkthrough on its Welcome page. It has four steps: **Pick a variant**, **Change the gold**, **Open the Studio** and **Keep it readable**. Each step has a button that runs the matching command.

## 2. Switch to an Auric theme

1. Open the Command Palette with `Ctrl` + `Shift` + `P`.
2. Run **Auric Theme: Switch Variant…**.
3. The list shows all 54 themes. Each entry shows whether it is dark or light and the hex value of its canvas (the editor background). The theme you are using is marked **current**.
4. Select a theme. VS Code switches immediately.

You can also use VS Code's own **Preferences: Color Theme** picker. Every Auric theme starts with **Auric Artisan —**, for example **Auric Artisan — Midnight Sapphire**.

When an Auric theme is active, a status bar item appears on the right with a paint-can icon and the short theme name, for example **Obsidian Gold**. An asterisk after the name means you have customised the theme. Hover over it to see how many dials and colours you have changed; select it to open Theme Studio.

## 3. Open Theme Studio

Use any of these:

- Press `Ctrl` + `Alt` + `;` (`Cmd` + `Alt` + `;` on macOS).
- Run **Auric Theme: Open Theme Studio** from the Command Palette.
- Select the status bar item.
- In the **Auric Theme** view in the Activity Bar, select **Open Theme Studio**.

Theme Studio opens as an editor tab called **Auric Theme Studio**.

## 4. Tour the Studio

From top to bottom, the Studio shows:

| Area | What it shows |
| --- | --- |
| Top bar | The Auric Artisan brand, a link to auricartisan.com, the **Auto · English · हिन्दी** language switch and an **Applied live** chip. |
| Introduction | "Make it yours." with an **Explore colours →** button that jumps to the Colours tab. |
| Active theme card | The current theme name, **Applied live**, a **Dark** or **Light** chip and an **As shipped** or **Customised** chip. |
| Metrics | **Built-in variants**, **Theme dials**, **Colour slots** and **Your changes** (modified dials plus colour overrides). |
| Tabs | Six numbered tabs: **Looks**, **Dials**, **Colours**, **Audit**, **Share**, **Preview**. The Audit tab shows a badge when pairs fail. |
| Tab content | The cards for the selected tab. |
| Footer | **Reset all**, **Randomize**, **Settings** and a count such as "2 overrides · 3 dials changed". |

Press the number keys `1` to `6` to jump between tabs, or use the arrow keys, `Home` and `End` while a tab has focus. Press `/` to jump to the colour search on the Colours tab.

If something about the theme cannot be applied, a banner under the tabs lists the problem.

## 5. Make a first change

1. Select the **Dials** tab.
2. In the **Accent** card, select the **Sapphire** swatch under **Accent colour**.
3. Watch the editor: tab rules, selections, focus rings and every accent-derived colour move to blue at once.
4. In the **Syntax** card, open **Syntax palette** and choose **Cool**.
5. A dot and a reset button appear beside each dial you changed. The footer count now shows two dials changed.

## 6. Check it is still readable

1. Select the **Audit** tab.
2. The top card shows the worst pair in the theme and either **All clear** or the number of failing pairs.
3. Scroll the **Measured pairs** table. Failing pairs are listed first.

See [Check contrast](check-contrast.md) for how to read the table.

## 7. Save your work

1. Select the **Share** tab.
2. In **Presets**, type a name such as "Blue work" and select **Save** (or press `Enter`).
3. The preset appears under **Saved** with the date and time.

You can now experiment freely. To return, select **Load** beside the preset.

## Result

Your editor is using an Auric theme with your chosen accent and syntax palette, the contrast audit has checked every text pair, and your set-up is saved as a named preset.

## Next steps

- [Choose a theme](choose-a-theme.md) — explore the families.
- [Looks and dials](looks-and-dials.md) — every dial explained.
- [Edit individual colours](edit-colours.md) — fine control over 107 slots.
- [Save, share and export](save-share-and-export.md) — move your theme between machines.
