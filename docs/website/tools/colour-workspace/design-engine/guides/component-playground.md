---
title: Design System Generator — Use the component playground
description: Try your generated tokens on a live, clickable component gallery, and change the preview's theme, density, corners, elevation, button shape and viewport.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Use the component playground

The **Components** tab draws a complete interface gallery with your generated tokens, and it works: tabs switch, menus open, switches toggle, modals and drawers open and close, toasts appear, steppers count and ratings set. It is the fastest way to notice that muted text is too light, that the primary is too close to the info colour, or that the corners feel wrong.

## What is in the gallery

Choose a category with the chips above the stage. **✦ All** shows every category in this order:

| Category | What it contains |
| --- | --- |
| **Navigation** | A navigation bar, **Tabs**, **Breadcrumbs**, **Pagination**, **Steps / wizard** |
| **Buttons** | **Variants**, **Sizes & icon buttons**, **Loading, block & FAB** |
| **Forms** | **Text & select**, **Choice & toggles**, **Slider, stepper & rating**, **Tags, upload & OTP** |
| **Feedback** | **Alerts**, **Toast, banner & tooltip**, **Progress & loading**, **Validation & empty** |
| **Data** | **Stat tiles**, **Data table**, **List & avatars**, **Timeline** |
| **Overlays** | **Modal & drawer**, **Dropdown menu**, **Command palette**, **Consent & popover** |
| **Commerce** | **Product card**, **Pricing**, **Cart & checkout** |
| **Marketing** | A hero, **Feature grid**, **Testimonial**, **Newsletter & FAQ** and a closing section |
| **Industry** | An **Industry showcase**: a small branded app screen written for one industry |

### The Industry showcase

The showcase is a short app screen (app name, navigation, a headline figure, a call to action, data rows and a trust chip) written for one of the fourteen industries. A row of chips lets you switch the scene independently of the industry you generated with, so you can check that a fintech palette still reads on a wellness screen. It starts on your industry, or on SaaS when the industry is **Auto**.

## The preview controls

The bar above the chips changes how the preview looks without changing the generated system. These settings are not saved, shared or exported.

| Control | Options | Effect |
| --- | --- | --- |
| **Theme** | **Light**, **Dark** | Draws the preview with the light or dark roles. Only the themes your colour mode includes are offered. |
| **Density** | **Compact**, **Cozy**, **Spacious** | Padding, gaps, font size and control height inside the preview. Separate from the brief's Density. |
| **Corners** | **Auto**, **Sharp**, **Soft**, **Round**, **Pill** | Tries another corner family without regenerating. |
| **Elevation** | **None**, **Flat**, **Auto**, **Deep** | Removes, flattens, keeps or deepens the shadows. **Deep** moves every surface up one shadow level. |
| **Buttons** | **Auto**, **Square**, **Pill** | Button corner radius only. |
| **Viewport** | **Fluid**, Desktop, Tablet, Mobile | Frames the gallery at a fixed width (the desktop, tablet and mobile buttons are icons with tooltips), and the narrow frames stack the gallery in one column. |
| **↺ Reset** | — | Returns density, corners, elevation, buttons and viewport to their defaults. It keeps your theme and category. |

## Tasks

### Check the system in dark mode

1. Make sure **Colour mode** in the brief is **Both** or **Dark**.
2. On **Components**, set **Theme** to **Dark**.
3. Look at **Feedback** and **Data**: muted text, borders and alert backgrounds are where dark themes usually struggle.

Result: the gallery drawn with the dark roles. To see the numbers, open the full audit and choose **Dark**; see [Check contrast with the audit](contrast-audit.md).

### Decide on a corner style

1. Change **Corners** between **Sharp**, **Soft**, **Round** and **Pill** and watch the cards, inputs and buttons.
2. When you like one, set **Corner style** in the brief to the matching option so it reaches the tokens.

Result: a corner family chosen by eye, then made real in the system.

### Check a phone layout

Set **Viewport** to Mobile. The gallery is framed at phone width and stacks into one column.

## Things to know

- Changing any input in the brief rebuilds this tab from scratch. An open modal, a typed value or a toggled switch is reset.
- Avatars, product images and figures in the gallery are placeholders.
- Switches respond to `Enter` and `Space` as well as clicks. Clicking outside an open menu closes it; clicking a modal's backdrop closes the modal.

## Related

- [Read the system](read-the-system.md)
- [Set the brief](set-the-brief.md)
- [Reference](reference.md)
