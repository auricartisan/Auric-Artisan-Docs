---
title: Feature Kit — Calculator functions
description: The complete expression language of the Feature Kit calculator: operators, numbers, functions, constants, variables, your own functions, calculus, statistics and programmer features.
product: Website › Kits › Feature Kit
updated: 2026-09-25
---

# Calculator functions

This page lists everything you can type into the calculator's expression bar. The keypad uses the same rules; it simply types the symbols for you.

## How expressions are read

- **Spaces are ignored.** `2 + 3` and `2+3` are the same. This also means `sin 30` is read as the unknown name `sin30`; always use brackets: `sin(30)`.
- **Multiplication must be written.** Type `2*pi`, not `2pi`. A missing operator gives `Unexpected token after expression`.
- **Names are case-sensitive.** `sin` works, `SIN` does not; `NA` is Avogadro's number, `na` is not defined.
- **Brackets must balance.** A missing `)` gives `Expected )`.

### Operators

From the loosest to the tightest binding:

1. `|` bitwise OR
2. `xor( )` bitwise exclusive OR, written after a value: `5 xor(3)`
3. `&` bitwise AND
4. `<<` and `>>` bit shifts
5. `+` and `-` (the keypad's `−` is the same as `-`)
6. `*` or `×`, `/` or `÷`, and `%`
7. A leading `-` or `+` sign
8. `^` power, which groups from the right
9. `!` factorial

Things that follow from this order:

- `-2^2` is `-4`, because the power is worked out before the sign.
- `2^3^2` is `2^9`, which is `512`.
- `2^-1` is `0.5`.
- `%` is the **remainder**, not a percentage: `10 % 3` is `1`. To take 15% of 80, type `80*15/100`.
- Dividing by zero gives the error `Division by zero`. A remainder by zero gives `NaN`.

### Numbers

| You type | Meaning | Example result |
|---|---|---|
| `42`, `3.14`, `.5` | Decimal numbers | `.5` is `0.5` |
| `2e3`, `1.5E-4` | Scientific notation | `2000`, `0.00015` |
| `0xFF` | Hexadecimal (digits 0 to 9 and A to F) | `255` |
| `0b1010` | Binary (digits 0 and 1) | `10` |

Because `e` is also a constant, a number cannot end in a bare `e`: `2e` gives `Invalid numeric literal`. Write `2*e` for two times e.

## Functions

Call a function with brackets and separate arguments with commas: `atan2(1, 1)`. Calling with the wrong number of arguments gives a message such as `sin expects 1 argument` or `stdev expects at least 2 arguments`.

### Trigonometry

Angles follow the **RAD** or **DEG** setting on the display.

| Function | Returns |
|---|---|
| `sin(a)`, `cos(a)`, `tan(a)` | Sine, cosine, tangent of angle `a` |
| `asin(v)`, `acos(v)`, `atan(v)` | Inverse sine, cosine, tangent, as an angle |
| `atan2(y, x)` | The angle of the point (x, y), as an angle |
| `sinh(v)`, `cosh(v)`, `tanh(v)` | Hyperbolic sine, cosine, tangent (not affected by RAD or DEG) |
| `asinh(v)`, `acosh(v)`, `atanh(v)` | Inverse hyperbolic functions (not affected by RAD or DEG) |
| `deg(r)` | Converts radians to degrees: `deg(pi)` is `180` |
| `rad(d)` | Converts degrees to radians: `rad(180)` is `3.14159265359` |

### Powers, roots and logarithms

| Function | Returns |
|---|---|
| `sqrt(v)` | Square root. `sqrt(-1)` gives `NaN` |
| `cbrt(v)` | Cube root |
| `nthroot(v, n)` | The nth root. An odd root of a negative number is negative: `nthroot(-27, 3)` is `-3` |
| `pow(a, b)` | `a` to the power `b`, the same as `a^b` |
| `exp(v)` | e to the power `v` |
| `ln(v)` | Natural logarithm |
| `log(v)` | Base-10 logarithm: `log(1000)` is `3` |
| `log2(v)` | Base-2 logarithm |
| `logb(v, base)` | Logarithm in any base: `logb(8, 2)` is `3` |

### Rounding and sizes

| Function | Returns |
|---|---|
| `abs(v)` | Absolute value |
| `round(v)` | Nearest whole number |
| `roundto(v, digits)` | Rounded to that many decimal places. Negative digits round to tens, hundreds and so on: `roundto(1234.5, -2)` is `1200` |
| `floor(v)`, `ceil(v)` | Round down, round up |
| `trunc(v)` | Drop the fractional part |
| `sign(v)` | `-1`, `0` or `1` |
| `mod(a, b)` | Remainder of `a` divided by `b`, the same as `a % b` |
| `max(a, b, ...)`, `min(a, b, ...)` | Largest, smallest of any number of values |
| `clamp(v, low, high)` | `v` limited to the range: `clamp(15, 0, 10)` is `10` |
| `hypot(a, b, ...)` | Square root of the sum of squares: `hypot(3, 4)` is `5` |

### Factorials and counting

| Function | Returns |
|---|---|
| `n!` or `fact(n)` | Factorial. Works for non-whole numbers too, through the gamma function: `0.5!` is `0.886226925453` |
| `gamma(v)` | The gamma function: `gamma(5)` is `24` |
| `nPr(n, r)` or `npr(n, r)` | Permutations: ordered choices of `r` from `n` |
| `nCr(n, r)` or `ncr(n, r)` | Combinations: unordered choices of `r` from `n` |

### Number theory

| Function | Returns |
|---|---|
| `gcd(a, b, ...)` | Greatest common divisor of any number of values (rounded to whole numbers first) |
| `lcm(a, b, ...)` | Least common multiple of any number of values |
| `isprime(n)` | `1` if `n` is prime, otherwise `0` |
| `nextprime(n)` | The first prime greater than `n` |
| `fib(n)` | The nth Fibonacci number: `fib(10)` is `55` |

### Statistics

Each takes any number of values: `mean(4, 8, 15, 16, 23, 42)`.

| Function | Returns |
|---|---|
| `mean(...)` or `avg(...)` | Arithmetic mean |
| `median(...)` | Middle value (mean of the two middle values for an even count) |
| `stdev(...)` | Sample standard deviation. Needs at least 2 values |
| `stdevp(...)` | Population standard deviation |
| `variance(...)` | Sample variance. Needs at least 2 values |
| `varp(...)` | Population variance |
| `geomean(...)` | Geometric mean |
| `rms(...)` | Root mean square |
| `total(...)` | Sum of the values |

### Random numbers

| Function | Returns |
|---|---|
| `rand()` | A random number from 0 up to, but not including, 1 |
| `randint(a, b)` | A random whole number from `a` to `b`, both included |

### Bitwise (programmer) functions

These work on whole numbers as 32-bit values. Results show in decimal.

- `a & b` — bits set in both.
- `a | b` — bits set in either.
- `xor(a, b)`, or `a xor(b)` — bits set in one but not both: `xor(5, 3)` is `6`.
- `not(a)` — every bit flipped: `not(0)` is `4294967295`.
- `a << n` and `a >> n` — shift left or right by `n` bits: `1 << 4` is `16`.

## Constants

| Name | Value | Meaning |
|---|---|---|
| `pi` or `π` | 3.14159… | Pi |
| `e` | 2.71828… | Euler's number |
| `phi` or `φ` | 1.61803… | The golden ratio |
| `tau` | 6.28318… | Two pi |
| `inf` | ∞ | Infinity |
| `c` | 299792458 | Speed of light, m/s |
| `G` | 6.6743e-11 | Gravitational constant, SI units |
| `g0` | 9.80665 | Standard gravity, m/s² |
| `NA` | 6.02214076e23 | Avogadro constant, per mole |
| `kB` | 1.380649e-23 | Boltzmann constant, J/K |
| `qe` | 1.602176634e-19 | Elementary charge, C |
| `me` | 9.1093837015e-31 | Electron mass, kg |
| `mp` | 1.67262192369e-27 | Proton mass, kg |
| `eps0` | 8.8541878128e-12 | Vacuum permittivity, F/m |
| `mu0` | 1.25663706212e-6 | Vacuum permeability, N/A² |
| `ans` | Your last result | Updated after each calculation |

You cannot assign a new value to a constant's name: `pi = 3` gives an error.

## Variables

Store a value with `name = expression`:

1. Type `r = 4` and press `Enter`. The display shows `4`, and a chip **r = 4** appears under the expression bar.
2. Type `pi*r^2` and press `Enter`. The display shows `50.2654824574`.

- A name starts with a letter or an underscore and can continue with letters, digits and underscores.
- Assigning to an existing name replaces its value.
- Using a name that has no value gives `Unknown variable: name`.
- Variables last until you leave or reload the page, or until you select **Clear** in the variables strip.

## Your own functions

Define a function with `name(parameters) = expression`:

1. Type `f(x) = x^2 + 1` and press `Enter`. The display shows `ƒ f(x) defined`, and a chip **ƒ f(x)** appears.
2. Type `f(3)` and press `Enter`. The display shows `10`.

- Functions can take several parameters: `area(w, h) = w*h`, then `area(3, 4)`.
- The body can use constants, built-in functions, variables and your other functions.
- Variables in the body are read when you call the function. With `h(x) = a*x`, changing `a` changes what `h(5)` returns.
- Calling with the wrong number of values gives a message such as `f expects 1 argument`.
- You cannot reuse the name of a built-in function or constant: `sin(x) = 2` gives `Cannot redefine sin`. Defining a function you already made replaces it.
- A function that calls itself stops with `Recursion too deep` after 128 levels.
- Your functions also work in the graph and inside calculus functions.
- Functions last until you leave or reload the page, or until you select **Clear**.

## Calculus and series

These functions take an expression as their first argument and work it out many times with a changing variable. By default the variable is `x`. You can name a different variable as an extra argument.

### Derivatives

| You type | Returns |
|---|---|
| `diff(expr, at)` | The slope (first derivative) of `expr` with respect to `x`, at `x = at` |
| `diff(expr, var, at)` | The same, with respect to the variable `var` |
| `derivative(...)` | Another name for `diff` |
| `diff2(expr, at)` or `diff2(expr, var, at)` | The second derivative |

Examples: `diff(x^3, 2)` shows `12.0000000001` (exactly 12 in theory); `diff(sin(x), 0)` shows `1`. Derivatives are estimated numerically, so the last digits can show tiny rounding noise, more so for `diff2`.

### Integrals

| You type | Returns |
|---|---|
| `integral(expr, a, b)` | The area under `expr` from `x = a` to `x = b` |
| `integral(expr, var, a, b)` | The same, integrating over `var` |
| `integrate(...)` | Another name for `integral` |

Examples: `integral(sin(x), 0, pi)` is `2`; `integral(t^2, t, 0, 3)` is `9`; `integral(1/x, 1, e)` is `1`. When `a` equals `b` the result is `0`; when `a` is greater than `b` the result changes sign.

### Solving equations

`solve` finds a value of the variable that makes the expression equal to zero.

| You type | How it searches |
|---|---|
| `solve(expr, guess)` | Starts at `guess` and homes in on a nearby root |
| `solve(expr, low, high)` | Searches between `low` and `high`. Best when the expression changes sign in that range |
| `solve(expr, var, guess)` or `solve(expr, var, low, high)` | The same, for a variable other than `x` |
| `root(...)` | Another name for `solve` |

Examples: `solve(x^2 - 9, 1)` is `3`; `solve(cos(x) - x, 0, 1)` is `0.739085133215`.

- To solve `f(x) = 5`, move everything to one side: `solve(f(x) - 5, 1)`.
- If there is no nearby root, you see `solve: no convergence (try lo, hi bounds)`. Try a different guess, or give a range that brackets the root. Some expressions, such as `x^2 + 1`, have no real root at all.
- If the range you give does not change sign, `solve` starts from its middle and searches as if you had given a guess.
- A result within a hair of a whole number is shown as that whole number.

### Sums and products

| You type | Returns |
|---|---|
| `sum(expr, var, from, to)` | `expr` added up for `var` = `from`, `from + 1`, and so on to `to` |
| `product(expr, var, from, to)` | `expr` multiplied together over the same range |

Examples: `sum(k^2, k, 1, 10)` is `385`; `product(k, k, 1, 5)` is `120`; `sum(1/2^n, n, 0, 50)` is `2`.

- `from` and `to` are rounded to whole numbers, and swapped if `from` is larger.
- A range of more than 1,000,000 steps gives `sum: too many terms` (or `product: too many terms`).

### Rules shared by calculus functions

- The variable you name can reuse a constant's name inside the function: `sum(e, e, 1, 3)` is `6`.
- They can be nested: `integral(diff(x^2, x), 0, 1)` is `1`.
- Very heavy expressions stop with `Expression too complex` instead of freezing the page.

## How results are shown

- Whole numbers under 10^15 show in full.
- Other results show up to 12 significant digits, with trailing zeros removed.
- Very small (under 10^-10) or very large (over 10^15) results show in scientific notation, for example `1.2345678901e+17`.
- Results are rounded to 14 significant digits internally, so `0.1+0.2` shows `0.3`.
- Infinite results show as `∞` or `-∞`; undefined results show as `NaN`.
- In the expression bar, a result with a small exact fraction also shows the fraction, such as `0.875 = 7/8`.

See [Limits and accuracy](../others/limits-and-accuracy.md) for the ranges each function can handle.
