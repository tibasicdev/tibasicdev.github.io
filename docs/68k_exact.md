![The exact() Command](68k_exact/exact.png "The exact() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Gives the exact value of an expression.|exact(*expression*)|This command works on all calculators.|6 bytes|
       
### Menu Location
- Press [2nd] [MATH] to enter the [68k:math](68k:math.html) menu.
- Press 1 to open the Number submenu, or use arrows
- Press [ENTER] to past exact(

Alternativly, for ti-92/+/v200, type "exact(" using the keyboard.
       
# The exact() Command

The `exact()` command forces an expression to be evaluated in exact mode, temporarily ignoring the mode setting.

```
:exact(15.376)
           1922/125
```

When applied to a complicated expression, matrix, or list, it forces every number that occurs there to be in exact form.

## Related Commands

- [`68k:approx()`](68k:approx().html)
- [`68k:round()`](68k:round().html)
