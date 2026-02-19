![The cosh() Command](68k_cosh/cosh.png "The cosh() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Takes the hyperbolic cosine of a number.|cosh(*value*)|This command works on all calculators.|1 byte|
       
### Menu Location
- Press 2nd MATH to enter the MATH menu.<br>* Press C to enter the Hyperbolic submenu.<br>* Press 2 to select cosh(.
# The cosh() Command


The `cosh()` command returns the [hyperbolic cosine](http://mathworld.wolfram.com/hyperboliccosine.html) of a number. 

As long as the calculator is in radian [mode](68k:mode-settings.html), `cosh()` can be used with complex numbers according to the rule that cosh(***i***x)=cos(x) and cos(***i***x)=cosh(x). This rule only works in radian mode, and `cosh()` of a complex number will return a domain error when working in degrees or gradians.

Occasionally, `cosh()` can compute an exact result; most of the time, the calculator will leave an expression with `cosh()` alone unless it's in approximate mode (or you [force an approximation](68k:approx.html)). When `cosh()` is used with symbolic expressions, the calculator can go back and forth between the `cosh()` expression and its exponential equivalent.

```
:cosh(0)
           1
:expand(cosh(x))
          e^x/2+1/(2*e^x)
:comDenom(e^x/2+1/(2*e^x))
          cosh(x)
```

If `cosh()` is applied to a list, it will take the hyperbolic cosine of every element in the list.

## Advanced Uses

The `cosh()` of a matrix is not (in general) the same as taking the hyperbolic cosine of every element of the matrix. A different definition is used to compute the result; see [68k:matrices](68k:matrices.html#toc2). It requires the matrix to be square and diagonalizable in order to apply.

## Formulas

The definition of hyperbolic cosine is given in terms of exponents:



## Error Conditions





## Related Commands

- [`68k:sinh()`](68k:sinh().html)
- [`68k:tanh()`](68k:tanh().html)
- [`coshֿ¹()`](68k:arccosh.html)
