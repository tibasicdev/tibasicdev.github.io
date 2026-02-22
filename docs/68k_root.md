![The root() Command](68k_root/root.png "The root() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Takes the *n*<sup>th</sup> root of a value.|root(*value*,*n*)|This command requires a TI-89 Titanium or Voyage 200 calculator with AMS version 3.10 or higher.|2 bytes|
       
### Menu Location
- Press 2nd MATH to enter the MATH popup menu.
- Press 1 to enter the Number submenu.
- Press D to select root(.
       
# The root() Command

The root() command takes *n*<sup>th</sup> roots: root(x,2) is the square root of x, root(x,3) is the cubic root, etc. (*n* doesn't have to be a whole number, or even real). Since root(x,n) is equivalent to x^(1/n), there was never any real need for this command, but it was added in the last AMS update for the Voyage 200 and TI-89 Titanium because users complained about not being able to do this calculation.

As far as complex roots are concerned: if taking a root of a real number, root() will return the real branch if there is one. If taking the root of a complex number, it will always return the principal branch.

```
:root(x,2)
           √(x)
:root(1024,10)
           2
```

## Advanced Uses

The command uses the same routines as the [^](68k:power.html) operator, so it works in all the same ways. This means it can be applied to lists (element-wise), and to matrices either through repeated multiplication (e.g. if taking the 1/100<sup>th</sup> root of a matrix, which ends up being its 100<sup>th</sup> power) or by diagonalizing the matrix first (see [68k:matrices](68k:matrices.html#toc2) for mor information about this method). If you want to take the *n*<sup>th</sup> root of every element of a matrix, use the [.^](68k:dotpower.html) command.

## Optimization

You can save a few bytes of space by using root(x,n) instead of x^(1/n); however, this optimization is a bit dodgy. It requires AMS 3.10 to use, so if you're planning on releasing the program anywhere, it will only work on the TI-89 Titanium and the Voyage 200, and even then it might require updating the OS. It's probably not worth it, unless the program is for personal use only.

## Error Conditions

**[230 - Dimension](68k:errors.html#e230)** happens when non-square matrices are used with root().
**[230 - Domain error](68k:errors.html#e230)** happens when a matrix is raised to an integer power not in the range -32768..32767.
**[665 - Matrix not diagonalizable](68k:errors.html#e665)** happens when diagonalization (used to compute most uses of root() with matrices) fails.
**[800 - Non-real result](68k:errors.html#e800)** happens when there is no real result to return, and the calculator is in real number mode.
**[890 - Singular matrix](68k:errors.html#e890)** happens when raising a matrix with no inverse to a negative power.

## Related Commands

- [^](68k:power.html) (exponentiation)
- [68k:solve()](68k:solve.html)
- [√()](68k:square-root.html)
