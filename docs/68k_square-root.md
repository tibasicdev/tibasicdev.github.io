![The √() Command](68k_square-root/square-root.png "The √() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Takes the square root of a number.|√(*number*)|This command works on all calculators.|1 byte|
       
### Menu Location
N/A

       
# The √() Command

The √() command takes the square root of a value: √(x) is a number that, when multiplied by itself, gives x. It's a special case of the [^](68k:power.html) and [68k:root()](68k:root().html) commands: √(x) = x^(1/2) = root(x,2).

Unless the calculator is in approximate [mode](68k:mode-settings.html), or you force it to approximate (by pressing ♦+ENTER, or using [68k:approx()](68k:approx().html)), it won't try to evaluate all square roots: it will take the square root of perfect squares, otherwise, it will just take out all the square factors (for instance, √(20) is simplified to 2√(5)).

For positive numbers, √() will return the positive square root; more generally, if the result is complex (and if the calculator is in complex number mode), the result of √() will be the one with non-negative real part. 
```
:√(16)
           4
:√(-12)
           2*√(3)*i
```
If the square root of a list is taken, it will take the square root of every element of the list.

## Advanced Uses

The √() of a matrix is not (in general) the same as taking the square root of every element of the matrix. A different definition is used to compute the result; see [68k:matrices](68k:matrices.html#toc2). It requires the matrix to be square and diagonalizable in order to apply.

## Error Conditions





## Related Commands

- [^](68k:power.html)
- [.^](68k:dotpower.html)
- [68k:root()](68k:root().html)
