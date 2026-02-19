![The coth() Command](68k_coth/coth.png "The coth() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Takes the hyperbolic cotangent of a number.|coth(*value*)|This command requires a calculator with AMS version 2.07 or higher (it will also work on any TI-89 Titanium or Voyage 200 calculator)|1 byte|
       
### Menu Location
- Press 2nd MATH to enter the MATH menu.
- Press C to enter the Hyperbolic submenu.
- Press 6 to select coth(.
       
# The coth() Command


The `coth()` command returns the [hyperbolic cotangent](http://mathworld.wolfram.com/hyperboliccotangent.html) of a number. Along with 11 other trig and hyperbolic functions, it was added in AMS version 2.07; on earlier versions, `coth(x)` can be replaced by 1/`tanh(x)`.

As long as the calculator is in radian [mode](68k:mode-settings.html), coth() can be used with complex numbers according to the rule that coth(***i***x)=-cot(x)****i*** and cot(***i***x)=-coth(x)****i***. This rule only works in radian mode, and `coth()` of a complex number will return a domain error when working in degrees or gradians.

Occasionally, `coth()` can compute an exact result; most of the time, the calculator will leave an expression with `coth()` alone unless it's in approximate mode (or you [force an approximation](68k:approx.html)). When `coth()` is used with symbolic expressions, the calculator can go back and forth between the `coth()` expression and its exponential equivalent.

```
:coth(0)
           undef
:expand(coth(x))
          -1/(e^x+1)+1/(e^x-1)+1
:comDenom(1-2/((e^x)^2+1))
          1/tanh(x)
```

If `coth()` is applied to a list, it will take the hyperbolic cotangent of every element in the list. However, it can't be applied to matrices the way `tanh()` can (this is probably an oversight; all the trig and hyperbolic functions that were present in all AMS versions work with matrices, but the ones added in version 2.07 do not).

## Formulas

The definition of hyperbolic cotangent is, by analogy with [`68k:cot()`](68k:cot().html), the ratio of [`68k:cosh()`](68k:cosh().html) and [`68k:sinh()`](68k:sinh().html):



## Error Conditions



## Related Commands

- [`68k:sech()`](68k:sech().html)
- [`68k:csch()`](68k:csch().html)
- [`cothֿ¹()`](68k:arccoth.html)
