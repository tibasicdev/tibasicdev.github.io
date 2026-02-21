![The tanh( Command](tanh/TANH.GIF "The tanh( Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Calculates the hyperbolic tangent of a value.|tanh(*value*)|TI-83/84/+/SE|1 byte|

### Menu Location
The tanh( command is only found in the Catalog. Press:
1. 2nd CATALOG to access the command catalog.
2. T to skip to commands starting with T.
3. Scroll down and select tanh(.
       
# The tanh( Command

Calculates the hyperbolic tangent of a value. The hyperbolic trig functions [sinh(](sinh.html), [cosh(](cosh.html), and tanh( are an analog of normal trig functions, but for a hyperbola, rather than a circle. They can be expressed in terms of real powers of [e](e-value.html), and don't depend on the [Degree](degree-mode.html) or [Radian](radian-mode.html) mode setting.

```
tanh(0)
    0
tanh(1)
    .761594156
```

Like normal trig commands, tanh( works on lists as well, but not on complex numbers, even though the function is often extended to the complex numbers in mathematics.

## Advanced Uses

The tanh( command can be used to approximate the sign function:

$$\operatorname{sgn} x=\begin{cases}-1&\text{if }x<0,\\0&\text{if }x=0,\\1&\text{if }x>0.\end{cases}$$

As the absolute value of the input becomes large, the convergence is achieved at a point closer to zero. For the function to work as intended generally, numbers having lesser orders of magnitude need to be multiplied by a factor large enough for the argument to arrive at ±16.720082053122, which is the smallest input to produce ±1 (respectively) to fourteen digits of accuracy.

```
5/12→X
    .4166666667
tanh(E9X)
    1
tanh(-E9X)
    -1
```

## Formulas

The definition of the hyperbolic tangent is:
$$\tanh{x}=\frac{e^x-e^{-x}}{e^x+e^{-x}}=\frac{e^{2x}-1}{e^{2x}+1}$$

## Related Commands

- [sinh(](sinh.html)
- [sinhֿ¹(](arsinh.html)
- [cosh(](cosh.html)
- [coshֿ¹(](arcosh.html)
- [tanhֿ¹(](artanh.html)
