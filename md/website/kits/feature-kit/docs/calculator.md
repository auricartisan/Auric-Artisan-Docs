---
title: Feature Kit — Calculator
description: Use the Feature Kit's Scientific Calculator: keypads, the expression bar, angle mode, memory, copying results and history.
product: Website › Kits › Feature Kit
updated: 2026-09-25
---

# Use the calculator

The **Scientific Calculator** gives you two ways to calculate: a keypad (which you can also drive from your keyboard) and an expression bar for full expressions with variables, your own functions and calculus. Both share one result display, one `ans` value and one history.

Open it from the Feature Kit menu with the **Scientific Calculator** card or the `1` key.

## The screen, top to bottom

1. **Display.** A small expression line, a large result line, and the angle buttons **RAD** and **DEG**.
2. **Expression bar.** A long text box with a calculator icon and an **ƒx** button at its right end. Its placeholder reads `f(x) = x^2 · integral(sin(x), 0, pi) · solve(x^2−2, 1)`.
3. **Function reference.** Hidden until you select **ƒx**.
4. **Variables strip.** Appears once you have defined a variable or a function.
5. **Graph** and **History** areas. Hidden until you select **Graph** or **History** in the title bar.
6. **Keypad tabs:** **Basic**, **Scientific**, **Programmer**.
7. **Memory row:** **MC**, **MR**, **M+**, **M−**.
8. **Keypad** for the selected tab.

## Calculate with the keypad

1. Select keys, or type on your keyboard while the cursor is not in a text box.
2. Watch the result line: it previews the answer as you type.
3. Select **=** or press `Enter` to finish. The result becomes `ans`, and the calculation goes into the history.

After a result, typing a digit starts a new calculation. Typing an operator adds it to the end of the expression you just worked out, not to the result, so `2+3` followed by `×2` becomes `2+3×2`. To build on a result, start with **Ans** instead: `Ans×2`.

Keyboard keys the keypad understands:

| Key | Enters |
|---|---|
| `0` to `9` | The digit |
| `+` `-` `*` `/` | Add, subtract, multiply (shown as ×), divide (shown as ÷) |
| `.` | Decimal point |
| `(` `)` | Brackets |
| `^` | Power |
| `%` | Remainder (modulo) |
| `!` | Factorial |
| `Enter` or `=` | Work out the expression |
| `Backspace` | Delete the last character |
| `Delete` | Clear everything |

If an expression cannot be worked out, the result line shows the reason, such as `Division by zero`, and flashes red.

## The three keypads

Select a tab to switch keypad. Which tabs you see depends on the site's tool visibility mode, set in the [Advanced Kit](../../advanced-kit/README.md):

| Mode | Tabs shown |
|---|---|
| Basic | **Basic** only |
| Advanced | **Scientific** and **Programmer** |
| Everything or Custom | All three |

### Basic keypad

```text
C    (    )    ÷
7    8    9    ×
4    5    6    −
1    2    3    +
0         .    =
```

**C** clears the expression. The Basic keypad has no backspace key; use `Backspace` on your keyboard.

### Scientific keypad

```text
d/dx   ∫      solve  Σ      Π
nCr    gcd    lcm    x̄      σ
sin    cos    tan    π      e
sin⁻¹  cos⁻¹  tan⁻¹  φ      ^
ln     log    log₂   √      ∛
exp    |x|    n!     %      ⌫
C      (      )      ÷      ×
7      8      9      −      +
4      5      6      .      Ans
1      2      3      0      =
```

Function keys insert the function name and an opening bracket, for example **sin** inserts `sin(` and **d/dx** inserts `diff(`. Close the bracket yourself. **x̄** inserts `mean(`, **σ** inserts `stdev(`, **|x|** inserts `abs(`, **√** inserts `sqrt(`, **∛** inserts `cbrt(`, **log₂** inserts `log2(`, **Σ** inserts `sum(` and **Π** inserts `product(`. **π**, **e** and **φ** insert the constants. **n!** adds the factorial sign. **Ans** inserts the previous result. **⌫** deletes one character.

What each function does is listed in [Calculator functions](calculator-functions.md).

### Programmer keypad

```text
AND   OR    XOR   NOT
<<    >>    0x    0b
A     B     C     D
E     F     ⌫     AC
7     8     9     +
4     5     6     −
1     2     3     ×
0           .     =
```

- **0x** starts a hexadecimal number and **0b** a binary one, for example `0xFF` or `0b1010`. **A** to **F** enter hexadecimal digits.
- **AND** and **OR** combine numbers bit by bit. **<<** and **>>** shift bits left and right.
- **XOR** inserts `xor(` and **NOT** inserts `not(`. The Programmer keypad has no bracket keys, so type the closing `)` on your keyboard. For example `5 xor(3)` gives `6`.
- **AC** clears the expression.
- Results always show in decimal: `0xFF` shows `255`.

## Calculate with the expression bar

The expression bar takes a whole expression as text, including things the keypad cannot enter.

1. Select the expression bar.
2. Type an expression, for example `mean(4, 8, 15, 16, 23, 42)`.
3. Press `Enter`.

The expression appears on the display's top line and the result on the large line. The result becomes `ans` and goes into the history.

When a result has a tidy exact fraction, the display shows it too: `0.875` shows as `0.875 = 7/8`. Fractions are found for denominators up to 10,000.

While the cursor is in the expression bar, keys go to the bar, not to the keypad. Use the bar for:

- variables: `r = 4`, then `pi*r^2`;
- your own functions: `f(x) = x^2 + 1`, then `f(3)`;
- calculus and series: `diff(x^3, 2)`, `integral(sin(x), 0, pi)`, `solve(x^2-2, 1)`, `sum(k^2, k, 1, 10)`;
- statistics and number theory: `stdev(2, 4, 4, 5)`, `gcd(12, 18)`, `isprime(97)`.

The full language is in [Calculator functions](calculator-functions.md).

## The function reference (ƒx)

Select **ƒx** at the end of the expression bar to show a panel of insertable chips, grouped by topic. Selecting a chip adds its text to the end of the expression bar.

| Group | Chips |
|---|---|
| Calculus | **diff(x², at)**, **diff2**, **∫ integral(f, a, b)**, **solve(f, guess)**, **Σ sum(f, n, 1, 99)**, **Π product** |
| Statistics | **mean**, **median**, **stdev**, **variance**, **geomean**, **rms** |
| Numbers | **gcd**, **lcm**, **isprime**, **nextprime**, **fib**, **nCr**, **nPr**, **roundto(x, digits)**, **nthroot(x, n)**, **logb(x, base)** |
| Define | **x = 5**, **f(x) = x^2**, **ans** |
| Constants | **π**, **e**, **φ**, **τ**, **c (light)**, **G**, **g₀**, **Nᴀ**, **kʙ** |

Select **ƒx** again to hide the panel.

## The variables strip

After you define a variable or a function, a strip of chips appears under the expression bar:

- A variable chip shows its value, for example **r = 4**. Selecting it inserts `r` into the expression bar.
- A function chip shows **ƒ** and its name, for example **ƒ f(x)**. Hovering shows its definition. Selecting it inserts `f(`.
- **Clear** removes every variable and function you have defined.

Variables and functions last until you leave or reload the page. They are not saved.

## Angle mode: RAD and DEG

**RAD** (the default) treats angles in radians; **DEG** treats them in degrees. The setting affects `sin`, `cos` and `tan` (their input) and `asin`, `acos`, `atan` and `atan2` (their output). It also applies to the graph. It resets to **RAD** each time the page loads.

## Memory keys

| Key | What it does |
|---|---|
| **MC** | Clears the memory to 0 |
| **MR** | Adds the memory value to the end of the current expression |
| **M+** | Adds the number on the result line to the memory |
| **M−** | Subtracts the number on the result line from the memory |

Memory lasts until you leave or reload the page.

## Copy a result

Select the large result line. A **Copied!** message confirms that the result is on your clipboard. Only the decimal result is copied, not the fraction.

## Use the history

1. Select **History** (the clock icon) in the title bar. The history area opens under the graph area, newest calculation first.
2. Each entry shows the expression and `= result`.
3. Select an entry, or focus it and press `Enter`, to load it back into the keypad display. Press `Enter` (with the cursor outside text boxes) or **=** to work it out again.
4. Select the bin icon on an entry to delete that calculation.
5. Select the bin icon in the **History** heading to delete every calculation. There is no confirmation.

The history keeps your last 100 calculations in your browser, including calculations from the keypad and the expression bar. When it is empty it reads **No calculations yet**. Select **History** again to hide it.

## Related

- [Calculator functions](calculator-functions.md) — the full list of what you can type
- [Graphing](graphing.md) — plot a function
- [Limits and accuracy](../others/limits-and-accuracy.md) — precision and numeric limits
- [Troubleshooting](troubleshooting.md) — what each error message means
