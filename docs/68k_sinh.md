![The sinh() Command](68k_sinh/sinh.png "The sinh() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Takes the hyperbolic sine of a number.|sinh(*value*)|This command works on all calculators.|1 byte|
       
### Menu Location
- Press 2nd MATH to enter the MATH menu.
- Press C to enter the Hyperbolic submenu.
- Press 1 to select sinh(.
       
# The sinh() Command


The sinh() command returns the [hyperbolic sine](http://mathworld.wolfram.com/hyperbolicsine.html) of a number. 

As long as the calculator is in radian [mode](68k:mode-settings.html), sinh() can be used with complex numbers according to the rule that sinh(***i***x)=sin(x)****i*** and sin(***i***x)=sinh(x)****i***. This rule only works in radian mode, and sinh() of a complex number will return a domain error when working in degrees or gradians.

Occasionally, sinh() can compute an exact result; most of the time, the calculator will leave an expression with sinh() alone unless it's in approximate mode (or you [force an approximation](68k:approx.html)). When sinh() is used with symbolic expressions, the calculator can go back and forth between the sinh() expression and its exponential equivalent.

```
:sinh(0)
           0
:expand(sinh(x))
          e^x/2-1/(2*e^x)
:comDenom(e^x/2-1/(2*e^x))
          sinh(x)
```

If sinh() is applied to a list, it will take the hyperbolic sine of every element in the list.

## Advanced Uses

The sinh() of a matrix is not (in general) the same as taking the hyperbolic sine of every element of the matrix. A different definition is used to compute the result; see [68k:matrices](68k:matrices.html#toc2). It requires the matrix to be square and diagonalizable in order to apply.

## Formulas

The definition of hyperbolic sine is given in terms of exponents:

$$ \sinh{x} = \frac{e^x-e^{-x}}{2} $$

## Error Conditions

**[230 - Dimension](68k:errors.html#e230)** happens when taking sinh() of a matrix that isn't square.
**[260 - Domain error](68k:errors.html#e260)** happens when taking sinh() of a complex number in degree or gradian mode.
**[665 - Matrix not diagonalizable](68k:errors.html#e665)** happens when taking sinh() of a matrix that isn't diagonalizable.

## Related Commands

- [68k:cosh()](68k:cosh.html)
- [68k:tanh()](68k:tanh.html)
- [sinhֿ¹()](68k:arcsinh.html)
