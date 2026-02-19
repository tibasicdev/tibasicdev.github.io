![The + Command](68k_add/add.png "The + Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Returns the sum of two numbers.|*value1* + *value2*|This command works on all calculators.|1 byte|
       
### Menu Location
Press the [+] key to paste +.
# The + Command

The + operator adds two numbers, variables, or expressions together. Order of operations dictates that it's calculated after [*](68k:multiply.html) and [/](68k:divide.html), and at the same time as [-](68k:subtract.html).

The + operator can also be used on lists and matrices. For the most part, it behaves in the intuitive way, distributing the operation over each element. However, adding a number to a matrix (in either order) behaves differently: the number is only added along the main diagonal of the matrix. For "normal" addition that applies to every element of the matrix, see [.+](68k:dotadd.html).

```
:1+1
           2
:5→x
:2+3*x
           17
:[1,2;3,4]+100
           [101  2]
           [3  104]
```

## Related Commands

- [-](68k:subtract.html) (subtract)
- [*](68k:multiply.html) (multiply)
- [/](68k:divide.html) (divide)

## See Also

- [68k:Order of Operations](68k:order-of-operations.html)
