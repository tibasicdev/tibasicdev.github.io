![The shift() Command](68k_shift/shift.png "The shift() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Shifts the elements of a list, string, or binary integer.|shift(*object*[,*places*])|This command works on all calculators.|2 bytes.|
       
### Menu Location
- Press 2nd MATH to enter the MATH popup menu.
- Press E to enter the Base submenu.
- Press B to select shift(.
       
# The shift() Command

When shift() is applied to lists or strings, it moves every element or character over, removing the elements that were shifted off the end, and filling in empty spaces with an undefined value: undef for lists and a space for strings. The default action is to shift everything one element right.

A second argument gives the direction and number of places to shift the list or string. Positive numbers are shifts to the left, and negative numbers are shifts to the right, so the default action shift(*object*) is equivalent to shift(*object*,-1). Here are some examples:

```
:shift({1,2,3,4,5})
           {undef  1  2  3  4}
:shift("Hello")
           " Hell"
:shift({1,2,3,4,5},2)
           {3  4  5  undef  undef}
:shift("TI-Basic",-3)
           "   TI-Ba"
```

shift() can also be used on integers, treating them as a sequence of bits (this makes the most sense when expressing them in binary). In this case, the integer is expressed as a 32-bit signed integer (larger integers are truncated), which is then bit-shifted. 

When shifting right, the integer is sign extended: that is, the new bits introduced are 1 if the original leftmost bit was 1, and 0 if the original leftmost bit was 0. This preserves the sign of the integer. When shifting left, the integer is zero extended: the new bits are always 0.

As with lists and strings, the default action of shift() is to shift the integer one position right. A second argument gives the direction and number of places to shift the list or string. Positive numbers are shifts to the left, and negative numbers are shifts to the right.

```
:shift(0b00000000000000000000000011111111)▶Bin
           0b00000000000000000000000001111111
:shift(0b10000000000000000000000011111111)▶Bin
           0b11000000000000000000000001111111
:shift(1,10)
           1024
```

## Related Commands

- [68k:▶Bin](68k:-bin.html) 
- [68k:rotate()](68k:rotate().html)
