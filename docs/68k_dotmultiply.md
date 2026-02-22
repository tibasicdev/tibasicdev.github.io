![The .* Command](68k_dotmultiply/dotmultiply.png "The .* Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Multiples two values, using element-by-element multiplication for two matrices.|*value1* .* *value2*|This command works on all calculators.|1 byte|
       
### Menu Location
- Press 2nd MATH to enter the MATH menu.
- Press 4 to enter the Matrix submenu.
- Press K to enter the Element ops submenu.
- Press 3 to select .*.
...frankly, just typing it is way easier.
       
# The .* Command

In most cases, .* does the same thing as [*](68k:multiply.html). The difference only applies to multiplying two matrices. Whereas * uses the linear-algebra definition (see its article for details), .* does the simple thing and multiplies the matrices element by element (obviously, they must match in size for this to work). 

```
:[1,2;3,4] .* [a,b;c,d]
        [a    2*b]
        [3*c  4*d]
```

## Error Conditions

**[240 - Dimension mismatch](68k:errors.html#e240)** happens when the matrices being multiplied don't match in size.

## Related Commands

- [.+](68k:dotadd.html)
- [.-](68k:dotsubtract.html)
- [./](68k:dotdivide.html)
- [.^](68k:dotpower.html)

## See Also

- [68k:order-of-operations](68k:order-of-operations.html)
