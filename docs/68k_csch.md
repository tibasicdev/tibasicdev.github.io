![The csch() Command](68k_csch/csch.png "The csch() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Takes the hyperbolic cosecant of a number.|csch(*value*)|This command requires a calculator with AMS version 2.07 or higher (it will also work on any TI-89 Titanium or Voyage 200 calculator)|1 byte|
       
### Menu Location
- Press 2nd MATH to enter the MATH menu.
- Press C to enter the Hyperbolic submenu.
- Press 4 to select csch(.
       
# The csch() Command


The `csch()` command returns the [hyperbolic cosecant](http://mathworld.wolfram.com/hyperboliccosecant.html) of a number. Along with 11 other trig and hyperbolic functions, it was added in AMS version 2.07; on earlier versions, `csch(x)` can be replaced by 1/[`68k:sinh(`](68k:sinh.html)x).

As long as the calculator is in radian [mode](68k:mode-settings.html), `csch()` can be used with complex numbers according to the rule that csch(***i***x)=-csc(x)****i*** and csc(***i***x)=-csch(x)****i***. This rule only works in radian mode, and `csch()` of a complex number will return a domain error when working in degrees or gradians.

Occasionally, `csch()` can compute an exact result; most of the time, the calculator will leave an expression with `csch()` alone unless it's in approximate mode (or you [force an approximation](68k:approx.html)). When `csch()` is used with symbolic expressions, the calculator can go back and forth between the `csch()` expression and its exponential equivalent.

```
:csch(0)
           undef
:expand(csch(x))
          1/(e^x+1)+1/(e^x-1)
:comDenom(1/(e^x+1)+1/(e^x-1))
          1/sinh(x)
```

If `csch()` is applied to a list, it will take the hyperbolic cosecant of every element in the list. However, it can't be applied to matrices the way `sinh()` can (this is probably an oversight; all the trig and hyperbolic functions that were present in all AMS versions work with matrices, but the ones added in version 2.07 do not).

## Formulas

The definition of hyperbolic cosecant is, by analogy with [`68k:csc()`](68k:csc.html), the reciprocal of [`68k:sinh()`](68k:sinh.html):



## Error Conditions



## Related Commands

- [`68k:sech()`](68k:sech.html)
- [`68k:coth()`](68k:coth.html)
- [`cschֿ¹()`](68k:arccsch.html)
