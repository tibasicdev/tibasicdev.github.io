![The = Command](68k_equal/equal.png "The = Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Tests if two values are equal.|*value1*=*value 2*|This command works on all calculators.|1 byte|
       
### Menu Location
Press the [=] key to enter =.
# The = Command

The = operator compares two values, returning true if they're equal, and false otherwise. It is a basic building block of the conditions used by commands such as [68k:If](68k:if.html), [68k:when()](68k:when().html), and [68k:While](68k:while.html). The results of = and the other relational operators ([≠](68k:not-equal.html), [>](68k:greater-than.html), [≥](68k:greater-than-or-equal.html), [<](68k:less-than.html), and [≤](68k:less-than-or-equal.html)) can be combined with the [68k:and](68k:and.html), [68k:or](68k:or.html), [68k:xor](68k:xor.html), and [68k:not](68k:not.html) operators to create more complicated conditions.

It returns a single value for most types of data, and returns false if the two sides are mismatched in type: comparing a single number to a list, for instance, or comparing two lists that are of a different size. The only exception is when comparing two [68k:lists](68k:lists.html) or two [68k:matrices](68k:matrices.html) of the same size: in that case, it compares them element-by-element, and returns a list or matrix of true/false values.

```
:2+2=4
           true
:2+2=5
           false
:{1,2,3}={1,4,3}
           {true  false  true}
```

If either side or both contains undefined variables, = will wait to return a value unless it's something clearly true for any value of the variable (for instance, x=x). You can do math with the resulting equation (most operations will be applied to both sides), and extract the two halves of it with [68k:left()](68k:left().html) and [68k:right()](68k:right().html).

## Optimization

Testing "If x=true" is redundant in most cases; you can shorten that to "If x". Similarly, "If x=false" can be "If not x".

## Related Commands

- [≠](68k:not-equal.html) (not equal)
- [>](68k:greater-than.html) (greater than)
- [≥](68k:greater-than-or-equal.html) (greater than or equal)
- [<](68k:less-than.html) (less than)
- [≤](68k:less-than-or-equal.html) (less than or equal)

## See Also

- [68k:order-of-operations](68k:order-of-operations.html)
