![The not (~) Command](68k_not/not.png "The not (~) Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Reverses a condition.<br>Can also be used as a bitwise "not" on integers.|not *condition*<br>not *integer*|This command works on all calculators.|1 byte|
       
### Menu Location
- Press 2nd MATH to enter the MATH popup menu.
- Press 8 to enter the Test submenu.
- Press 7 to select not.
       
# The not (~) Command

The "not" operator reverses a condition, making it true if it had been false, and false if it had been true. You can create these conditions with the relational operators [=](68k:equal.html), [≠](68k:not-equal.html), [>](68k:greater-than.html), [≥](68k:greater-than-or-equal.html), [<](68k:less-than.html), and [≤](68k:less-than-or-equal.html), with functions such as [68k:isPrime()](68k:isprime.html), [68k:pxlTest()](68k:pxltest.html), and [68k:ptTest()](68k:pttest.html), or with any other expression that returns 'true' or 'false'. Other operators for dealing with conditions are [68k:and](68k:and.html), [68k:or](68k:or.html), and [68k:xor](68k:xor.html).

In output, it can also appear as ~, and if you type the ~ character, it will be interpreted as "not". 

```
:not 2+2=4
           false
:not x
           ~x
```

The operator can also be applied to an integer, treating it as a 32-bit signed integer (larger integers will be truncated to fit) expressed in binary. In this case, it gives the 1's complement, flipping all the bits.
```
:(not 0b1111)▶Bin
           0b11111111111111111111111111110000
:not 1000
           -1001
```

## Error Conditions



## Related Commands

- [68k:and](68k:and.html)
- [68k:or](68k:or.html)
- [68k:xor](68k:xor.html)

## See Also

- [68k:order-of-operations](68k:order-of-operations.html)
