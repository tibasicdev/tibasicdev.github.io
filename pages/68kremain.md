![The remain() Command](68k_remain/remain.png "The remain() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Returns the remainder of a division.|remain(*dividend*,*divisor*)|This command works on all calculators.|1 byte|
       
### Menu Location
- Press 2nd MATH to enter the math popup menu.<br>* Press 1 to enter the Number submenu.<br>* Press A to select remain(.
# The remain() Command

The remain() command returns the remainder of a division: remain(A,B) is calculated as A-B*[68k:intDiv(](68k:intdiv.html)A,B) which in turn is equivalent to A-B*[68k:iPart(](68k:ipart.html)A/B). Although this operation is most useful for dividing whole numbers, this definition works for any number, whole or decimal, real or complex. Additionally, remain(X,0) is defined as X.

The related [68k:mod()](68k:mod().html) command returns the same results for positive numbers, however, they disagree when negative integers enter the mix. The result of mod() is defined just as remain(), but with [68k:int()](68k:int().html) instead of iPart(). This means that remain() gives a negative answer if the dividend is negative, and mod() gives a negative answer if the divisor is negative.

```
:remain(125,3)
           2
:remain(-125,3)
           -2
:remain(2*i+1,i+1)
           i
```

The remain() command also works for [lists](68k:lists.html) and [matrices](68k:matrices.html). Used with a list or matrix and a number, remain() is applied to the number paired with every element of the list or matrix. Used with two lists or two matrices, which must match in size, remain() is applied to matching elements of the list or matrix.

## Advanced Uses

Use [68k:intDiv()](68k:intdiv().html) and remain() for the quotient and remainder results of long division, respectively.

## Error Conditions



## Related Commands

- [68k:intDiv()](68k:intdiv().html)
- [68k:mod()](68k:mod().html)
- [68k:iPart()](68k:ipart().html)
