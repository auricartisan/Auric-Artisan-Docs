---
title: Menu Kit — Reference
description: Every control, tab, section, state and message in the Menu Kit.
product: Website › Kits › Menu Kit
updated: 2026-09-25
---

# Menu Kit reference

## Launcher

| Control | What it does | Default |
|---|---|---|
| **Menu** launcher (four-square icon) | Opens or closes the kit. Announces itself as **Open start menu** or **Close start menu** | Closed |
| `Ctrl` + `M` | Same as the launcher | — |
| Tooltip | "Open site navigation, grouped pages, and quick search." | — |

## Title bar

| Control | What it does | Values | Default |
|---|---|---|---|
| **Menu Kit** title | Drag the title bar to move the kit | — | Bottom-left corner |
| Status chip | The site's release status; tooltip "Auric Artisan is [status]." | For example **Beta** | **Beta** at the time of writing |
| **Focus mode** | Keeps the kit open across pages and when other kits open | On or off; remembered | Off |
| **Theme** | Switches the menu between light and dark ("Switch this menu between light and dark mode.") | Light or dark; remembered | Follows the site |
| **Resize** | Normal (680 px wide) or expanded (up to 820 px wide) | Remembered | Normal |
| **Minimize** | Collapses the kit to its title bar; select the bar to restore | — | — |
| **Close** | Closes the kit ("Close Menu Kit.") | — | — |

## Search bar

| Control | What it does |
|---|---|
| **Search Auric Artisan…** | Type to switch to the results list; has focus when the kit opens |
| **ESC** hint | Shown while the box is empty |
| Clear button (cross) | Shown while the box has text; clears it ("Clear search") |
| Result count | **N results** while searching |

## Tabs

| Tab | Tooltip |
|---|---|
| **Tools** | Show Tools pages. |
| **Design** | Show Design pages. |
| **Analyze** | Show Analyze pages. |
| **Account** | Show Account pages. |
| **Library** | Show Library pages. |
| **Company** | Show Company pages. |
| **Trust** | Show Trust pages. |

The tab row shows text labels; it scrolls sideways when it does not fit. The last tab used is remembered. Tabs with no visible pages in the current mode are hidden.

## Sections

| Tab | Section | Pages |
|---|---|---|
| Tools | Recommended | All Tools, Collections, URL Analyzer, Basic Color Tools, ASCII Art, Icon Library, Design System Generator, Color Foundations |
| Tools | Most Used | Up to 8 Tools-tab pages, by how often you open them |
| Tools | Start Here | All Tools, Collections, URL Analyzer, Basic Color Tools, ASCII Art, Icon Library, Design System Generator, Portfolio Builder, Portfolio Index |
| Tools | Search | Search, Search Console |
| Tools | General Color Tools | Color Foundations, General Tools Hub, Illuminants, Gamut Explorer, Tonal Steps, Tints and Shades, Perception and Vision, Spectral Tools Hub |
| Design | Color Science Lab | Color Science Lab, Personalization Generator, Ishihara Plate Generation |
| Design | Colorimetry | Colorimetry Hub, Chromatic Adaptation Dynamics, Gamut Mapping |
| Design | Gamut and Rendering | Gamut and Rendering Hub, HDR Gamut Plot, Tone Mapping |
| Design | Perception and Neuroscience | Perception and Neuroscience Hub, Neuroscience of Color, Psychophysical Experiment Engine |
| Design | Spectral and Material Tools | Industrial Dye Chemistry, Material Lighting |
| Design | Utility Labs | Collage Maker, Image Picker, ICC Profile Parser, LUT Lab, M-Gradient Palette, SVG Recolor |
| Analyze | Vision Simulation | Vision Deficiency Simulator |
| Account | Account and Sign In | Sign In, Create Account, Forgot Password, Reset Password, Dashboard, Profile, Portfolio, Settings, Sessions, API Keys, Billing, Invoice Receipt, Device Approval, Verify Email |
| Library | Library | Documentation, Changelog, Blog, Learn, Workspace, Color Library, Palette Library, Gradient Library, Harmony Library, Shades Library, Accessibility Library |
| Company | Company | About, Pricing, Contact, FAQ, Timeline, Accessibility, Projects |
| Trust | Legal and Security | Legal Hub, Acceptable Use Policy, Content and Intellectual Property, Cookies, Data Retention and Deletion, Licenses, Privacy, Refund, Security, Subscription and Billing, Terms, Transparency |

Section headings show an icon, the name, the number of pages and a chevron; select one to collapse or expand it. Collapsed sections are remembered.

The **Workspace** tile in the Library tab opens the [Library Kit](../../library-kit/README.md) instead of leaving the page.

## Tiles

| Part | Meaning |
|---|---|
| Illustration or icon | The page's artwork |
| Name | The page's name |
| Tooltip | The page's description |
| Small dot | This is the page you are on; tooltip **You are here** |

## Results list (while searching)

| Part | Meaning |
|---|---|
| Icon or illustration | The page or action |
| Name | Page name or action name |
| Second line | The page's section, or the action's description |
| **Open ↵** | A page; `Enter` opens it |
| **Action ↵** | A quick action; `Enter` runs it |

Quick actions: **Copy current URL**, **Scroll to top**, **Go home**, **Go back**, **Reload page**, **Open a random tool**, **Toggle menu theme**. See [Search and quick actions](search-and-quick-actions.md).

## Footer

| Control | What it does |
|---|---|
| Key hints | **Ctrl K** Search · **Esc** Close (**⌘** on a Mac) |
| Home icon | Goes to the Auric Artisan home page ("Go to the Auric Artisan home page.") |

## States and messages

| Message | When |
|---|---|
| **Loading menu** — "Reframing tools by intent." | The list of pages is loading |
| **Menu unavailable** — "Failed to load menu data." and **Failed to load menu.** | The list of pages could not be downloaded |
| **No matching pages** — "Try a different search, or switch to another category." with **Clear search** | Nothing to show in the current tab |
| **No matches for** "…" | A search found nothing |
