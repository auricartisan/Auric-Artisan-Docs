---
title: Split view — Reference
description: Every split view control, value, default, shortcut and message.
product: Website › Site features › Split view
updated: 2026-09-25
---

# Split view reference

## Pane controls (one set per pane)

| Control | Label | Action |
|---|---|---|
| Tab | Live view / Companion | Page title and load state; double-click to rename |
| Back | Back | History back in this pane |
| Forward | Forward | History forward in this pane |
| Reload | Reload | Reloads this pane |
| Address bar | Live pane URL / Companion URL | Type or choose a destination; `Enter` loads, `Ctrl` + `Enter` opens a new tab |
| More (three dots) | More pane controls | Opens the menu below |

## More menu

| Control | Values | Default |
|---|---|---|
| **Theme** | Auto, Light, Dark | Auto |
| **Viewport** | Desktop, Tablet (820 px), Phone (400 px) | Desktop |
| **Zoom** | 100%, 125%, 150%, 75% (cycles in that order) | 100% |
| **Focus this pane** | On, off | Off |
| **Maximize** | On, off | Off |
| **Open in new tab** | — | — |
| **Copy URL** | — | — |

## Global controls

| Control | Label (tooltip) | Action | Key |
|---|---|---|---|
| Performance chip | Performance metrics | Shows FPS; hover for details; click to pin | — |
| Layout | Toggle layout | Side by side or stacked | `Alt` + `V` |
| Swap | Swap panes | Trade sides | `Alt` + `S` |
| Compare | Compare | Overlay and highlight differences | — |
| Mirror | Mirror | Load the live page into the companion | — |
| Route links | Route links | Live-pane links open in the companion | — |
| Scroll sync | Scroll sync | Mirror scrolling between panes | — |
| Equal split | Equal split | Reset to 50 / 50 | `Alt` + `E` |
| Close | Close | Exit split view | `Esc` |

## Divider

| Behaviour | Value |
|---|---|
| Snap points | 25%, 33%, 50%, 66%, 75% |
| Minimum pane size | 80 pixels |
| Double-click | Equal split |
| Remembered | Separately for side-by-side and stacked |

## Keyboard

| Keys | Action |
|---|---|
| `Ctrl` + `Shift` + `D` | Open or close split view |
| `Esc` | Close a More menu; else close split view |
| `Alt` + `1` / `Alt` + `2` | Focus the live / companion pane |
| `Alt` + `V` | Toggle layout |
| `Alt` + `S` | Swap panes |
| `Alt` + `E` | Equal split |
| `Alt` + click a link | Open it in the other pane (or open split view with it) |

`Alt` + `V`, `Alt` + `S` and `Alt` + `E` are ignored while you type in an address bar.

## Performance panel

| Reading | Meaning |
|---|---|
| **FPS** | Frames drawn per second |
| **Frame time** | Milliseconds per frame |
| **CPU busy (long tasks)** | Share of the last second spent on long tasks |
| **Event-loop lag** | Delay before the page can respond, in milliseconds |
| **JS heap (RAM)** | Memory used by page scripts, where the browser reports it |
| **DOM nodes · live** / **· pane 2** | Number of page elements in each pane |

## Recent destinations

Up to 10 site pages, most recent first.
