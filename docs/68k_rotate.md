![The rotate() Command](68k_rotate/rotate.png "The rotate() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Rotates a string, list, or binary integer.|rotate(*object*,*places*)|This command works on all calculators.|2 bytes|
       
### Menu Location
- Press 2nd MATH to enter the MATH menu.
- Press E to enter the Base submenu.
- Press C to select rotate(.
       
# The rotate() Command

When rotate() is applied to lists or strings, it moves every element or character over, moving the displaced elements over to the other end. By default, it shifts everything right one space, and moves the rightmost element to the beginning.

A second argument gives the direction and number of places to rotate the list or string. Positive numbers are rotations to the left, and negative numbers are rotation to the right, so the default action rotate(*object*) is equivalent to rotate(*object*,-1). Here are some examples:

```
:rotate({1,2,3,4,5})
           {5  1  2  3  4}
:rotate("Hello")
           "oHell"
:rotate({1,2,3,4,5},2)
           {3  4  5  1  2}
:rotate("TI-Basic",-3)
           "sicTI-Ba"
```

rotate() can also be used on integers, treating them as a sequence of bits (this makes the most sense when expressing them in binary). In this case, the integer is expressed as a 32-bit signed integer (larger integers are truncated), whose bits are then rotated.

As with lists and strings, the default action of rotate() is to rotate the integer one position right. A second argument gives the direction and number of places to rotate the list or string. Positive numbers are rotations to the left, and negative numbers are rotations to the right.

```
:shift(0b00000000000000000000000011111111)▶Bin
           0b10000000000000000000000001111111
:rotate(1,10)
           1024
```

## Related Commands

- [68k:▶Bin](68k:-bin.html) 
- [68k:shift()](68k:shift.html)
