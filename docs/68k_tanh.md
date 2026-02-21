![The tanh() Command](68k_tanh/tanh.png "The tanh() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Takes the hyperbolic tangent of a number.|tanh(*value*)|This command works on all calculators.|1 byte|
       
### Menu Location
- Press 2nd MATH to enter the MATH menu.
- Press C to enter the Hyperbolic submenu.
- Press 3 to select tanh(.
       
# The tanh() Command


The tanh() command returns the [hyperbolic tangent](http://mathworld.wolfram.com/hyperbolictangent.html) of a number.

As long as the calculator is in radian [mode](68k:mode-settings.html), tanh() can be used with complex numbers according to the rule that tanh(***i***x)=tan(x)****i*** and tan(***i***x)=tanh(x)****i***. This rule only works in radian mode, and tanh() of a complex number will return a domain error when working in degrees or gradians.

Occasionally, tanh() can compute an exact result; most of the time, the calculator will leave an expression with tanh() alone unless it's in approximate mode (or you [force an approximation](68k:approx.html)). When tanh() is used with symbolic expressions, the calculator can go back and forth between the tanh() expression and its exponential equivalent.

```
:tanh(0)
           0
:expand(tanh(x))
          1-2/((e^x)^2+1)
:comDenom(1-2/((e^x)^2+1))
          tanh(x)
```

If tanh() is applied to a list, it will take the hyperbolic tangent of every element in the list.

## Advanced Uses

The tanh() of a matrix is not (in general) the same as taking the hyperbolic tangent of every element of the matrix. A different definition is used to compute the result; see [68k:matrices](68k:matrices.html#toc2). It requires the matrix to be square and diagonalizable in order to apply.

## Formulas

The definition of hyperbolic cotangent is, by analogy with [68k:tan()](68k:tan.html), the ratio of [68k:sinh()](68k:sinh.html) and [68k:cosh()](68k:cosh.html):



## Error Conditions





## Related Commands

- [68k:sinh()](68k:sinh.html)
- [68k:cosh()](68k:cosh.html)
- [tanhֿ¹()](68k:arctanh.html)
