![The ‾ Command](68k_negative/negative.png "The ‾ Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Negates an expression.|‾*expression*|This command works on all calculators.|1 byte|
       
### Menu Location
Press the ‾ key to enter ‾.
       
# The ‾ Command

The ‾ operator gives the negative of the value immediately following it. It's not to be confused with the [-](68k:subtract.html) operator, which subtracts two numbers — while on paper you'd generally use the same symbol for -2 and 4-2, the calculator has two different symbols, and negation is represented by the slightly shorter and higher dash.

You can also use ‾ to negate lists and matrices, which will negate each element, as expected.
```
:1+‾1
           0
:‾(x-1)
           ‾x+1
:‾[1,2;3,4]
           [‾1  ‾2]
           [‾3  ‾4]
```

Other pages on this site will use - to mean both subtraction and negation, where it isn't confusing.

## Related Commands

- [+](68k:add.html) (add)
- [-](68k:subtract.html) (subtract)

## See Also

- [68k:order-of-operations](68k:order-of-operations.html)
