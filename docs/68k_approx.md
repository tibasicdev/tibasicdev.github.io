![The approx() Command](68k_approx/approx.png "The approx() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Gives a decimal approximation of an expression.|approx(*expression*)|This command works on all calculators.|7 bytes|
       
### Menu Location
While on the home screen:
- Press F2 to enter the Algebra menu.
- Press 5 to paste approx(.
       
# The approx() Command

The `approx()` command forces an expression to be evaluated in approximate mode, temporarily ignoring the mode setting. It's equivalent to pressing ♦ and ENTER when performing a calculation on the home screen.

```
:approx(π)
           3.14159265359
```

When applied to a complicated expression, matrix, or list, it approximates every number that occurs there.

## Related Commands

- [`68k:exact()`](68k:exact.html)
- [`68k:round()`](68k:round.html)
