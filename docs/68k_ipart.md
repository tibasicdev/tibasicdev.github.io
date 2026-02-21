![The iPart() Command](68k_ipart/ipart.png "The iPart() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Returns the integer part of a number.|iPart(*value*)|This command works on all calculators.|1 byte|
       
### Menu Location
- Press 2nd MATH to enter the MATH popup menu.
- Press 1 to enter the Number submenu.
- Press 4 to select iPart(.
       
# The iPart() Command

The iPart() command returns the integer part of a number (removing all the digits after the decimal). Another way of thinking about it is it rounds a number towards 0: positive numbers get rounded down to an integer, and negative numbers get rounded up to an integer.

There are several other rounding commands available, which work in subtly different ways:
- [68k:ceiling()](68k:ceiling.html) always rounds up to the next higher integer.
- [68k:floor()](68k:floor.html) always rounds down to the next lower integer. [68k:int()](68k:int.html) does the same thing as [68k:floor()](68k:floor.html).
- [68k:round()](68k:round.html) rounds to any given place value, including to an integer; it rounds up or down, whichever is nearest. 

However, iPart() is the only one that has a counterpart [68k:fPart()](68k:fpart.html) which returns the fractional part of a number. This follows the rule that iPart(x)+fPart(x) always equals x.

Using iPart() on the result of a division — iPart(x/y) — is useful so often that there's a specific command, [68k:intDiv()](68k:intdiv.html), for doing so. 

iPart() can also be applied to complex numbers, lists, and matrices, rounding everything that there is to round in each of them.

```
:iPart(3)
           3
:iPart({-π,π})
           {-3  3}
```

## Related Commands

- [68k:ceiling()](68k:ceiling.html)
- [68k:floor()](68k:floor.html)
- [68k:fPart()](68k:fpart.html)
- [68k:intDiv()](68k:intdiv.html)
