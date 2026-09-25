---
title: Kits — The page utilities bar
description: How the launcher bar in the bottom-left corner opens every kit, how it looks on a phone, and how it closes.
product: Website › Kits
updated: 2026-09-25
---

# The page utilities bar

The page utilities bar is the one place every kit opens from. It sits in the bottom-left corner of every page. Closed, it is a single round button; open, it is a row of labelled launchers.

## Closed and open

**Closed**, the bar is one round button with a gold outline. Its tooltip reads **Page utilities**: "Show navigation, settings, and the Feature, Menu, Advanced, Status and Library kits."

**Open**, the bar becomes a single card with one cell per launcher. Each cell shows an icon with a one-word name under it:

| Cell | What it opens | Tooltip |
|---|---|---|
| **Close** | Folds the bar away. This is the same round button, relabelled while the bar is open. | Hide page utilities |
| **Feature** | [Feature Kit](../feature-kit/README.md) | Calculator, converter, graph tools, and feedback. |
| **Menu** | [Menu Kit](../menu-kit/README.md) | Open site navigation, grouped pages, and quick search. |
| **Advanced** | [Advanced Kit](../advanced-kit/README.md) | Choose Basic, Advanced, or Everything tool visibility. |
| **Status** | [Status Kit](../status-kit/README.md) | View the current page status and scan page status entries. |
| **Library** | [Library Kit](../library-kit/README.md) | Browse, search and restore everything you have saved across the tools. |
| **Navigate** | The page navigation dock | Back, forward, reload, outline, split view and jump to top or bottom. |
| **Settings** | The site settings panel | Settings |

Thin dividers separate the three groups: the **Close** button, the five kits, and the two page controls (**Navigate** and **Settings**). **Navigate** and **Settings** are site features rather than kits; see [Site features](../../site-features/README.md).

## Open the bar and a kit

1. Select the round **Page utilities** button.
2. Select a launcher, for example **Status**.

The bar folds away and the kit opens. On a desktop screen the kit panel appears in the bottom-left corner, just above the round button, unless you have moved it before.

## Close the bar

Any of these folds the bar back into its round button:

- Select **Close**, the first cell.
- Press `Esc`.
- Click anywhere on the page outside the bar.
- Select any launcher. The kit opens and the bar closes.

Folding the bar away does not close any kit. The tooltip says so: "Put the bar away. The kits stay where they are."

## Launchers of open kits

While a kit is open, its launcher shows a cross instead of its icon. Selecting it closes the kit.

The Feature Kit, the Advanced Kit and the Library Kit go one step further: while one of them is open, its launcher gets a gold tint and stays on screen beside the round button even after the bar folds away, so you can close the kit from there. For the Menu Kit and the Status Kit, open the bar again or use the kit's own **Close** button.

## Loading

Each kit loads the first time you open it on a page. Until it has loaded, its launcher is dimmed, shows a busy pointer and ignores further clicks. Hovering over a launcher or giving it keyboard focus starts loading early, so the kit usually opens without a wait.

## On a phone

On screens 580 pixels wide or narrower, the bar changes shape:

- The round button is slightly smaller and sits closer to the corner.
- Open, the bar stretches across the bottom of the screen and wraps into two rows. The top row holds the five kits. A thin line separates it from the bottom row, which holds **Navigate**, **Settings** and **Close**.
- While the bar is open, the page gains extra space at the bottom, so the end of the page is not hidden under the bar.
- The page navigation dock does not show its own collapsed tab on a phone. Open it with **Navigate**.

Kit panels also adapt: on a phone every kit opens across the full width of the screen, less a small margin on each side.

## Keyboard use

- `Tab` reaches the round button like any other button. Press `Enter` or `Space` to open the bar, then `Tab` through the launchers.
- `Esc` closes the bar.
- Several kits have their own shortcuts that work without the bar. See [Keyboard shortcuts](../others/shortcuts.md).

## Accessibility

- The round button announces itself as **Show page utilities** or **Hide page utilities** and reports whether the bar is expanded.
- The bar is a toolbar named **Page utility launchers**.
- Each launcher has a visible name as well as an icon, and a gold focus ring when it has keyboard focus.
- If your system asks for reduced motion, the bar opens and closes without animation.

## Related

- [Panel controls](panel-controls.md) — what you can do with a kit once it is open
- [Troubleshooting](troubleshooting.md) — if the bar or a launcher does not respond
