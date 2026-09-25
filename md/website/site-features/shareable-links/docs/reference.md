---
title: Shareable links — Reference
description: Exactly what is and is not saved in a page's address, and how it is restored.
product: Website › Site features › Shareable links
updated: 2026-09-25
---

# Shareable links reference

## Saved after `#p=`

| Item | Detail |
|---|---|
| Scroll position | Vertical and horizontal; not saved when within 4 pixels of the top-left |
| Text, number and other input fields | Their values, in the page's main content and in the Settings panel |
| Drop-down lists and text areas | Their values |
| Checkboxes and radio buttons | On or off |
| Tabs, toggles and pressed buttons | Which are selected |
| Editable text areas | Their text |
| Open panels | Settings panel, Feature Kit, Menu Kit, Advanced Kit, Status Kit |
| Appearance settings | Only those that differ from their defaults: accent, theme mode, text size, comfort switches, eye rest, screen saver, clock format, seconds, date and date format |
| Tool state | On tools that save their own extra state |

Only controls that have an identity on the page (an id or a name) can be saved.

## Not saved

| Item | Why |
|---|---|
| Passwords | Never recorded |
| File choosers | Files cannot be put in a link |
| Search boxes | Excluded |
| Hidden fields and buttons | Not user input |
| Disabled controls | Not in use |
| Areas a page marks as private | Excluded by the page |
| Controls outside the main content (other than Settings) | Out of scope |
| Language | Use `?lang=` instead |

## Timing and size

| Behaviour | Value |
|---|---|
| Update delay | About 0.34 seconds after a change |
| History | Replaces the current entry; adds no Back steps |
| Maximum length | About 3,600 characters; beyond that only scroll position and open panels are kept |
| Restore retries | For a few seconds, for parts that load late |

## When it does not write

- When the address already has another `#` part (a section anchor, the Vision Simulation state, a shared library item). The site still restores its own `#p=` if present.
- On pages that turn the feature off.
- Inside split view panes, each pane keeps its own state, which is included in the `#split=` address.

## Other parameters

| Parameter | Effect |
|---|---|
| `?lang=hi` / `?lang=en` | Opens the page in Hindi or English and remembers it |
| `?color=`, `?colour=`, `?hex=` | Opens the colour inspector with that colour |
| `on=`, `bg=`, `against=`, `vs=` | Background colour for the inspector |
| `#split=` | Restores split view |
| `/search/?q=` | Opens the search page with a query |
