![The sech() Command](68k_sech/sech.png "The sech() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Takes the hyperbolic secant of a number.|sech(*value*)|This command requires a calculator with AMS version 2.07 or higher (it will also work on any TI-89 Titanium or Voyage 200 calculator)|1 byte|
       
### Menu Location
- Press 2nd MATH to enter the MATH menu.<br>* Press C to enter the Hyperbolic submenu.<br>* Press 5 to select sech(.
# The sech() Command


The `sech()` command returns the [hyperbolic secant](http://mathworld.wolfram.com/hyperbolicsecant.html) of a number. Along with 11 other trig and hyperbolic functions, it was added in AMS version 2.07; on earlier versions, `sech(x)` can be replaced by 1/`cosh(x)`.

As long as the calculator is in radian [mode](68k:mode-settings.html), `sech()` can be used with complex numbers according to the rule that `sech(***i***x)`=`sec(x)` and `sec(***i***x)`=`sech(x)`. This rule only works in radian mode, and `sech()` of a complex number will return a domain error when working in degrees or gradians.

Occasionally, `sech()` can compute an exact result; most of the time, the calculator will leave an expression with `sech()` alone unless it's in approximate mode (or you [force an approximation](68k:approx.html)). When `sech()` is used with symbolic expressions, the calculator can go back and forth between the `sech()` expression and its exponential equivalent.

```
:sech(0)
           1
:expand(sech(x))
          2*e^x/((e^x)^2+1)
:comDenom(2*e^x/((e^x)^2+1))
          1/cosh(x)
```

If `sech()` is applied to a list, it will take the hyperbolic secant of every element in the list. However, it can't be applied to matrices the way `cosh()` can (this is probably an oversight; all the trig and hyperbolic functions that were present in all AMS versions work with matrices, but the ones added in version 2.07 do not).

## Formulas

The definition of hyperbolic secant is, by analogy with [`68k:sec()`](68k:sec().html), the reciprocal of [`68k:cosh()`](68k:cosh().html):



## Error Conditions



## Related Commands

- [`68k:csch()`](68k:csch().html)
- [`68k:coth()`](68k:coth().html)
- [`sechֿ¹()`](68k:arcsech.html)
