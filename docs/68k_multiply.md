![The * Command](68k_multiply/multiply.png "The * Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Returns the multiplication of two numbers.|value1 * value2|This command works on all calculators.|1 byte|
       
### Menu Location
Press the [*] key to paste *.
       
# The * Command

The * operator multiplies two numbers, variables, or expressions. In many cases, it's implied — 5x, for instance, will be assumed to be 5*x. There are two exceptions: long variable names — xy will be interpreted as a single variable, not as x*y — and function calls — f(x) will be interpreted as f() applied to x, not as f*x.

Multiplication has higher priority than [+](68k:add.html) and [-](68k:subtract.html), so it will be done before them; it has the same priority as [/](68k:divide.html).

```
:x*y
		x*y
:2*2
		4
```

## Advanced Uses

Multiplying matrices is not the same as multiplying their individual elements (which the [.*](68k:dotmultiply.html) operator does). To multiply two matrices, the first must have the same number of columns as the second has rows. The product of an MxN matrix with an NxP matrix will be an MxP matrix, whose (a,b)<sup>th</sup> entry will be the [dot product](68k:dotp().html) of the a<sup>th</sup> row of the first matrix with the b<sup>th</sup> column of the second.

## Error Conditions



## Related Commands
- [-](68k:subtract.html) (subtract)
- [+](68k:add.html) (Add)
- [/](68k:divide.html) (divide)

## See Also

- [68k:Order of Operations](68k:order-of-operations.html)
