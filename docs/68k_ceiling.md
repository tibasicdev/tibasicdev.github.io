![The ceiling() Command](68k_ceiling/ceiling.png "The ceiling() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Returns the ceiling of a number.|ceiling(*value*)|This command works on all calculators.|1 byte|
       
### Menu Location
- Press 2nd MATH to enter the MATH popup menu.
- Press 1 to enter the Number submenu.
- Press 7 to select ceiling(.
       
# The ceiling() Command

The `ceiling()` command rounds a number up to the nearest integer at least as large as the number. For instance, `ceiling(π)` returns 4, while `ceiling(-π)` returns -3.

There are several commands available to round a number to an integer in slightly different ways:

- [`68k:int()`](68k:int.html) and [`68k:floor()`](68k:floor.html) — like `ceiling()`, but round down instead.
- [`68k:iPart()`](68k:ipart.html) — truncates a number to just its integer part (or, if you prefer, rounds a number toward 0).
- [`68k:round()`](68k:round.html) — rounds to a specific place value, not just to an integer, but `round(x,0)` will round x to the nearest integer, up or down.

`ceiling()` can also be applied to complex numbers, lists, and matrices, rounding everything that there is to round in each of them.

```
:ceiling(3)
           3
:ceiling({-π,π})
           {-3  4}
```

## Related Commands

- [`68k:floor()`](68k:floor.html)
- [`68k:int()`](68k:int.html)
- [`68k:iPart()`](68k:ipart.html)
- [`68k:round()`](68k:round.html)
