![The intDiv() Command](68k_intdiv/intdiv.png "The intDiv() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Returns the whole number part of a division.|intDiv(*dividend*,*divisor*)|This command works on all calculators.|1 byte|
       
### Menu Location
N/A

# The intDiv() Command

The integer division command, intDiv(a,b) returns the whole number portion of a/b: this is equal to [iPart(](68k:ipart.html)a/b). Although this operation is most useful for dividing whole numbers, this definition works for any number, whole or decimal, real or complex.

```
:intDiv(125,3)
           41
:intDiv(-125,3)
           -41
:intDiv(125,π)
           39
```

## Advanced Uses

The intDiv() command also works for [lists](68k:lists.html) and [matrices](68k:matrices.html). Used with a list or matrix and a number, intDiv() is applied to the number paired with every element of the list or matrix. Used with two lists or two matrices, which must match in size, intDiv() is applied to matching elements of the list or matrix.

------

Use intDiv() and [remain()](68k:remain.html) for the quotient and remainder results of long division, respectively.

## Optimization

Constructions like iPart(a/b) should be replaced with intDiv(a,b): this is smaller and faster. 

## Error Conditions



Division by zero does not throw an error; an undefined value is returned instead.

## Related Commands

- [/](68k:divide.html)
- [remain()](68k:remain.html)
- [iPart()](68k:ipart.html)
