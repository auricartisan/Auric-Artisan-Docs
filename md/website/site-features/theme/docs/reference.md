---
title: Theme — Reference
description: Every theme control, the values it sets, and how the controls interact.
product: Website › Site features › Theme
updated: 2026-09-25
---

# Theme reference

## Controls

| Control | Values | Sets System? | Scope |
|---|---|---|---|
| Header sun/moon button | Toggles light and dark | No (fixes the opposite of what you see) | Whole site |
| Settings › Appearance › **Theme** | **Light**, **Dark**, **System** | Yes | Whole site |
| Drawer › Preferences › **Theme** | **Auto**, **Light**, **Dark** | Yes (**Auto**) | Whole site |
| `Alt` + `T` | Light → Dark → System → Light | Yes | Whole site |
| Right-click › View › **Switch theme** | Toggles light and dark | No | Whole site |
| Spotlight › **Toggle light and dark** | Toggles light and dark | No | Whole site |
| Card menu › System › **Theme** | Toggles light and dark | No | Whole site |
| Kit title-bar theme button | Light, dark | — | That kit only |
| Split-view pane › **Theme** | Auto, Light, Dark | — | That pane only |

## Defaults and storage

| Item | Value |
|---|---|
| Default mode | System |
| Where it is kept | This browser |
| Shared across tabs | Yes, open tabs update when you change it |
| Applied before the page is drawn | Yes |
| In the settings export file | Yes, as `themeMode` |

## How the stored choice is read

When a page loads, the site uses, in order: the mode chosen in Settings (or the drawer, or `Alt` + `T`); otherwise the last choice made with a light/dark toggle; otherwise your device's setting.

## Messages

| Message | When |
|---|---|
| Theme: Light / Theme: Dark / Theme: System | After `Alt` + `T` |
