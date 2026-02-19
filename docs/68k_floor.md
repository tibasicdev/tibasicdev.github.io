![The floor() Command](68k_floor/floor.png "The floor() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Returns the floor of a number.|floor(*value*)|This command works on all calculators.|1 byte|
       
### Menu Location
- Press 2nd MATH to enter the MATH popup menu.
- Press 1 to enter the Number submenu.
- Press 6 to select floor(.
       
# The floor() Command

The floor() command rounds a number down to the nearest integer less than or equal to the number. For instance, floor(π) returns 3, while floor(-π) returns -4. 

The command is an alias for [68k:int()](68k:int().html): they do the exact same thing. The calculator prefers using floor() (in fact, int() will be converted to floor() in symbolic expressions); int() is left over from earlier calculator models. Other rounding commands include:
- [68k:ceiling()](68k:ceiling().html) — like floor(), but always rounds up (to the next higher integer).
- [68k:iPart()](68k:ipart().html) — truncates a number to just its integer part (or, if you prefer, rounds a number toward 0).
- [68k:round()](68k:round().html) — rounds to a specific place value, not just to an integer, but round(x,0) will round x to the nearest integer, up or down.

floor() can also be applied to complex numbers, lists, and matrices, rounding everything that there is to round in each of them.

```
:floor(3)
           3
:floor({-π,π})
           {-4  3}
```

## Related Commands

- [68k:ceiling()](68k:ceiling().html)
- [68k:int()](68k:int().html)
- [68k:iPart()](68k:ipart().html)
- [68k:round()](68k:round().html)
