![The fPart() command](68k_fpart/fpart.png "The fPart() command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Returns the fractional part of a value.|fPart(*value*)|TI-89/92/+/V200|6 bytes|

### Menu Location
Press:
1. [2nd] + [MATH] to access the [68k:math](68k:math.html) menu.
1. [RIGHT] to access the Number submenu.
1. 5 to select fPart(, or use arrows.
Alternativly, type "fPart(" with the keyboard
       
# The fPart() command

fPart(*value*) returns the fractional part of *value*. Also works on complex numbers/expressions, lists and matrices.
```
fPart(5.32)
             .32
fPart([[‾1.5,3.2][6.8,‾7.9]])
             [‾.5,.2]
             [.8,‾.9]
fPart({‾1.5,3.2,6.8,‾7.9})
              {‾.5,.2,.8,‾.9}
fPart(3.26+4.3i)
              .26+.3i
```

## Advanced Uses

To check if a number x is a whole number, you can simply check if the fPart(x)=0:
```
:If fPart(x)=0 Then
:©X is an integer
:Else
:©X is not an integer
:End
```

## Related Commands

- [68k:int(](68k:int.html)
- [68k:iPart(](68k:ipart.html)
- [68k:round(](68k:round.html)
