---
title: Feature Kit — Limits and accuracy
description: How precise the Feature Kit's calculator, graph, converter and date tools are, the ranges they handle, and where they approximate.
product: Website › Kits › Feature Kit
updated: 2026-09-25
---

# Limits and accuracy

The Feature Kit is a quick-use toolbox. Its results are good for everyday design, development and study work. They are not certified for engineering, medical, legal or financial use.

## Calculator precision

- The calculator uses the browser's standard double-precision numbers, which hold about 15 to 17 significant digits.
- Every result is rounded to 14 significant digits to hide floating-point artefacts, so `0.1+0.2` shows `0.3`.
- Results are displayed with up to 12 significant digits. Whole numbers under 10^15 are shown in full.
- Results smaller than 10^-10 or larger than 10^15 are shown in scientific notation.
- Numbers beyond about 1.8 × 10^308 become `∞`.
- There are no complex numbers; operations with no real answer give `NaN`.

## Exact fractions

The fraction hint in the expression bar (such as `0.875 = 7/8`) is found by searching for a fraction with a denominator up to 10,000 that matches the result to within about one part in 10^11. A shown fraction is exact for that decimal; no fraction is shown when none fits. The hint does not appear for keypad results.

## Calculus

All calculus functions are numerical estimates, not symbolic algebra.

| Function | Method | What to expect |
|---|---|---|
| `diff` | Five-point difference with a step scaled to the point | Very close, but the last displayed digits can show rounding noise, for example `diff(x^3, 2)` shows `12.0000000001` |
| `diff2` | Three-point second difference | Fewer correct digits, for example `diff2(x^3, 2)` shows `12.0000029666` |
| `integral` | Adaptive Simpson's rule, refining up to 22 levels | Very accurate for smooth functions; less reliable across spikes, jumps or infinities inside the range |
| `solve` with a guess | Newton's method, up to 100 steps | Finds the root nearest the guess, if any; can miss roots or jump to another one |
| `solve` with a range | Repeated halving, up to 200 steps | Reliable when the expression changes sign in the range; otherwise falls back to a guess at the midpoint |
| `sum`, `product` | Direct addition or multiplication | Exact up to floating-point rounding; at most 1,000,000 terms |

Results within 10^-10 of a whole number are snapped to that whole number by `solve`.

## Other calculator ranges

| Function | Limit |
|---|---|
| `n!`, `fact(n)` | Above 170 the result is `∞` |
| `fib(n)` | Above 1,476 the result is `∞` |
| `nextprime(n)` | Up to 9 × 10^15 |
| `isprime(n)` | Checks by trial division; very large numbers take longer |
| Bitwise operations | Work on 32-bit whole numbers |
| `stdev`, `variance` | Need at least 2 values |
| Your own functions | Up to 128 nested calls |
| Any expression | Stops with `Expression too complex` after about 5 million steps |
| `rand`, `randint` | Use the browser's general-purpose random numbers, not suitable for security |

## Graph

- The graph samples the expression once per horizontal pixel, so very fast oscillations can look jagged or be missed.
- Points where the expression is undefined or infinite are left as gaps.
- Zoom ranges from 5 to 5,000 pixels per unit.

## Unit Converter

- Most categories convert through a base unit with a fixed factor per unit; results are rounded for display to 12 significant digits.
- **Temperature** uses exact formulas through kelvin.
- **Fuel Economy** uses fixed factors (for example 1 US mpg = 0.425144 km/L) and handles the inverse units, such as litres per 100 km.
- **Sound Level** uses approximations: decibels (dB), decibel-milliwatts (dBm) and phons are treated as equal, and sones use the rule that 40 phons is 1 sone and every 10 phons doubles loudness. Treat these as rough equivalents, not physical conversions.
- Metric prefixes from yocto (10^-24) to yotta (10^24) are generated for units that take them.

## Date & Time

- Dates and times use your device's clock and time zone.
- **Months (≈)** and **Years (≈)** are averages (30.437 and 365.25 days), not calendar months or years.
- **Business days** counts Monday to Friday and ignores public holidays.
- **Hours** in the Difference tab is days × 24; it ignores the time of day and daylight-saving changes.
- **Unix (s)** in the Calendar tab uses the date and time you set, in your local time zone.
- World clocks rely on your browser's time zone data.

## Developer Tools

- Hashes and HMAC use your browser's built-in cryptography and match standard implementations.
- JWT decoding does not verify signatures.
- The cron explanation reads standard five-field cron only (no seconds or year field, and no `L`, `W` or `#` extensions). Next runs are in your local time zone.
- The regular expression tool lists the first 200 matches and stops after 10,000.
- The Epoch tool reads 1 to 10 digits as seconds and exactly 13 digits as milliseconds; 11- or 12-digit numbers are read as dates, which usually fails.
