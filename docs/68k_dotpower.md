![The .^ Command](68k_dotpower/dotpower.png "The .^ Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Raises a value to a power, doing this element-by-element for matrices.|*base* .^ *exponent*|This command works on all calculators.|1 byte|
       
### Menu Location
- Press 2nd MATH to enter the MATH menu.<br>* Press 4 to enter the Matrix submenu.<br>* Press K to enter the Element ops submenu.<br>* Press 1 to select .+.<br>...frankly, just typing it is way easier.
# The .^ Command

The .^ operator is generally the same as [^](68k:power.html), except when dealing with matrices. While ^ does quite a lot of matrix-specific stuff (check out its page for more information), .^ just applies it element-by-element:
```
:[a,b;c,d] .^ 2
           [a^2  b^2]
           [c^2  d^2]
```

The command can handle any choice of matrix and scalar as the base and exponent. However, if you're raising a constant number to a matrix power, be careful that the dot in .^ is not confused for a decimal point, by adding extra spaces:
```
:2.^[a,b;c,d]
           Error: Data type
:2 .^ [a,b;c,d]
           [2^a  2^b]
           [2^c  2^d]
```

Although this doesn't come up often, be aware that .^, like ^, is evaluated from right to left: a.^b.^c is calculated as a.^(b.^c), not as (a.^b).^c.

## Error Conditions



## Related Commands

- [.+](68k:dotadd.html)
- [.-](68k:dotsubtract.html)
- [.*](68k:dotmultiply.html)
- [./](68k:dotdivide.html)

## See Also

- [68k:order-of-operations](68k:order-of-operations.html)
