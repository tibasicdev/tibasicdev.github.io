![The - Command](68k_subtract/subtract.png "The - Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Returns the difference of two numbers.|*value1* - *value2*|This command works on all calculators.|1 byte|
       
### Menu Location
Press the [-] key to paste -.
# The - Command

The - operator subtracts two numbers, variables, or expressions. Order of operations dictates that it's calculated after [*](68k:multiply.html) and [/](68k:divide.html), and at the same time as [+](68k:add.html).

The - operator can also be used on lists and matrices. For the most part, it behaves in the intuitive way, distributing the operation over each element. However, subtracting a number from a matrix (or a matrix from a number) behaves differently: the number is only subtracted along the main diagonal of the matrix. For "normal" subtraction that applies to every element of the matrix, see [.-](68k:dotsubtract.html).

```
:1-1
           0
:5→x
:2-3x
           -13
:[1,2;3,4]-100
           [-99  2]
           [3  -96]
```

## Related Commands

- [+](68k:add.html) (add)
- [*](68k:multiply.html) (multiply)
- [/](68k:divide.html) (divide)

## See Also

- [68k:Order of Operations](68k:order-of-operations.html)
