---
title: Eye rest — Reference
description: Every eye-rest control, value, default and message.
product: Website › Site features › Eye rest
updated: 2026-09-25
---

# Eye rest reference

## Settings panel (Comfort)

| Control | Values | Default |
|---|---|---|
| **Eye-rest reminders** | On, off | Off |
| **Reminder interval** | **20m**, **35m**, **45m**, **60m** | 20m |

## Reminder card

| Element | Text or values |
|---|---|
| Title | **Time to look away** |
| Sentence | "You have been at this for N minutes. S seconds looking into the distance is enough." |
| Main actions | **Rest now**, **Later** |
| Quiet actions | **Change**, **Not this session**, **Turn these off** |
| Auto-dismiss | 60 seconds, shown by an emptying bar |

## Timing view (after Change)

| Element | Values | Default |
|---|---|---|
| Title | **How often, and how long** | — |
| **Remind me every** | **20m**, **35m**, **45m**, **60m** | Your Reminder interval |
| **Rest for** | **5s**, **10s**, **15s**, **20s**, **25s**, **30s** | 30s (resets on each page load) |
| Actions | **Rest now**; quiet **Later**, **Turn these off** | — |
| Auto-dismiss | 60 seconds | — |

## Rest screen

| Element | Text |
|---|---|
| Heading | **Look past the screen** |
| Instruction | "Something about twenty feet away — a doorway, a window, the far wall. The screen will brighten when the rest is over." |
| Countdown | Seconds remaining |
| Progress | Horizon line shrinking to the centre (still with reduced motion) |
| Button | **End early** |

## End screen

| Element | Text |
|---|---|
| Kicker | **Rest complete** |
| Heading | **Welcome back** |
| Line | "Next reminder in N minutes." |
| Duration | About 2.6 seconds, then the page returns |

## What each way of stopping does

| Action | Effect | Lasts |
|---|---|---|
| **Later** | Closes the card; next reminder after a full interval | Until the next reminder |
| **End early** | Stops the rest; next countdown starts | Until the next reminder |
| **Not this session** | No reminders | Until this browser tab is closed |
| **Turn these off** | No reminders | Until a setting change while the Settings switch is on |
| Settings switch off | No reminders | Until you switch it on |
