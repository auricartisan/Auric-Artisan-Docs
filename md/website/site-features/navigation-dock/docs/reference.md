---
title: Navigation dock — Reference
description: Every control of the navigation dock with its label, action and availability.
product: Website › Site features › Navigation dock
updated: 2026-09-25
---

# Navigation dock reference

## Controls

| Control | Label (tooltip) | Action | Phone |
|---|---|---|---|
| Grip | Drag to move | Drag vertically; drag across the middle to change side | Hidden |
| Back | Back | Browser history back | Shown |
| Forward | Forward | Browser history forward | Shown |
| Reload | Reload | Reloads the page | Shown |
| Outline | Page outline | Opens or closes **On this page** | Shown |
| Split view | Open split view | Opens split view | Shown |
| Record | Record screen (Alt+Shift+R) | Opens the recorder setup | Shown |
| Copy | Copy link | Copies the current address; shows a tick | Shown |
| Share | Share | Share sheet, or copies the address and shows a tick | Shown |
| Top | Scroll to top | Smooth scroll to the top; ring shows progress | Shown |
| Bottom | Scroll to bottom | Smooth scroll to the end | Shown |
| Flip | Flip dock side | Moves the dock to the other edge | Hidden |
| Collapsed line or button | Show navigation (Navigation) | Opens the dock | Button on some phones |

**Back** and **Forward** are greyed out when there is no page in that direction, in browsers that report this (such as Chrome and Edge). In other browsers they are always available.

## States and sizes

| State | Appearance |
|---|---|
| Open (desktop) | Vertical pill of buttons, 12 pixels from the edge |
| Collapsed (desktop) | Thin gold line, 3 by 64 pixels, 4 pixels from the edge |
| Open (700 px and narrower) | Horizontal bar centred at the bottom, scrolls sideways |
| Collapsed (700 px and narrower) | 44-pixel round button, or hidden on the narrowest screens |

## Remembered settings

| Setting | Values | Default |
|---|---|---|
| Side | Left, right | Left |
| Height | 10% to 90% of the window | 50% (middle) |

Both are kept in this browser and apply on every page.

## Timings

| Behaviour | Time |
|---|---|
| Stays open after a page loads (desktop) | About 1.6 seconds |
| Collapses after the pointer leaves | About 0.5 seconds |
| Closes after opening from its round button (phone) | About 5 seconds |
| Copied tick shows for | About 1 second |
