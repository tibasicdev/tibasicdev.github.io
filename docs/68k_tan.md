![The tan() Command](68k_tan/tan.png "The tan() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Takes the tangent of a number (usually, an angle).|tan(*angle*)|This command works on all calculators.|1 byte|
       
### Menu Location
Press the TAN button to enter tan(.
       
# The tan() Command


The `tan()` command returns the [tangent](http://mathworld.wolfram.com/tangent.html) of an angle measure. Naturally, the result depends on the angle [`mode`](68k:setmode.html) the calculator is in: `radian`, `degree`, or (in AMS version 3.10) `gradian`. You can also use one of the `<sup>[r](68k:radian.html)</sup>`, [`°`](68k:degree.html), `<sup>[G](68k:gradian.html)</sup>` marks to specify an angle mode.

For many common angles, `tan()` can compute an exact result. Other angles, the calculator will leave alone unless it's in approximate mode (or unless you make it approximate), and then it will give a decimal approximation. As long as the calculator is in `radian` [mode](68k:mode-settings.html), `tan()` can be used with complex numbers as well.


```
:tan(60°)
           √3
:tan(x+π)
          tan(x)
:tan(ix)
          tanh(x)*i
```

If `tan()` is applied to a list, it will take the tangent of every element in the list.

## Advanced Uses

The `tan()` of a matrix is not (in general) the same as taking the tangent of every element of the matrix. A different definition is used to compute the result; see [68k:matrices](68k:matrices.html#toc2). It requires the matrix to be square and diagonalizable in order to apply.

## Error Conditions

**[230 - Dimension](68k:errors.html#e230)** happens when taking `tan()` of a matrix that isn't square.
**[260 - Domain error](68k:errors.html#e260)** happens when taking `tan()` of a complex number in degree or gradian mode.
**[665 - Matrix not diagonalizable](68k:errors.html#e665)** happens when taking `tan()` of a matrix that isn't diagonalizable.

## Related Commands

- [`68k:sin()`](68k:sin.html)
- [`68k:cos()`](68k:cos.html)
- [`tanֿ¹()`](68k:arctan.html)
