![The sin() Command](68k_sin/sin.png "The sin() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Takes the sine of a number (usually, an angle).|sin(*angle*)|This command works on all calculators.|1 byte|
       
### Menu Location
Press the SIN button to enter sin(.
# The sin() Command


The sin() command returns the [sine](http://mathworld.wolfram.com/sine.html) of an angle measure. Naturally, the result depends on the angle [mode](68k:setmode.html) the calculator is in: radian, degree, or (in AMS version 3.10) gradian. You can also use one of the <sup>[r](68k:radian.html)</sup>, [°](68k:degree.html), <sup>[G](68k:gradian.html)</sup> marks to specify an angle mode.

For many common angles, sin() can compute an exact result. Other angles, the calculator will leave alone unless it's in approximate mode (or unless you make it approximate), and then it will give a decimal approximation. As long as the calculator is in radian [mode](68k:mode-settings.html), sin() can be used with complex numbers as well.

```
:sin(30°)
           1/2
:sin(x+2π)
          sin(x)
:sin(πi/2)
          sinh(π/2)*i
```

If sin() is applied to a list, it will take the sine of every element in the list.

## Advanced Uses

The sin() of a matrix is not (in general) the same as taking the sine of every element of the matrix. A different definition is used to compute the result; see [68k:matrices](68k:matrices.html#toc2). It requires the matrix to be square and diagonalizable in order to apply.

## Error Conditions





## Related Commands

- [68k:cos()](68k:cos().html)
- [68k:tan()](68k:tan().html)
- [sinֿ¹()](68k:arcsin.html)
