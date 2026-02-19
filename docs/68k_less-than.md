![The < Command](68k_less-than/lessthan.png "The < Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Tests if one value is smaller than another.|*value1*<*value 2*|This command works on all calculators.|1 byte|
       
### Menu Location
Press [2nd][<] to enter <.
       
# The < Command

The < operator compares two values, returning true if the right side is greater, and false otherwise. It is a basic building block of the conditions used by commands such as [68k:If](68k:if.html), [68k:when()](68k:when().html), and [68k:While](68k:while.html). The results of < and the other relational operators ([=](68k:equal.html), [≠](68k:not-equal.html), [>](68k:greater-than.html), [≥](68k:greater-than-or-equal.html), and [≤](68k:less-than-or-equal.html)) can be combined with the [68k:and](68k:and.html), [68k:or](68k:or.html), [68k:xor](68k:xor.html), and [68k:not](68k:not.html) operators to create more complicated conditions.

It returns a single value for most types of data, and returns false if the two sides are mismatched in type: comparing a single number to a list, for instance, or comparing two lists that are of a different size. The only exception is when comparing two [68k:lists](68k:lists.html) or two [68k:matrices](68k:matrices.html) of the same size: in that case, it compares them element-by-element, and returns a list or matrix of true/false values.

```
:3<4
           true
:3<2
           false
:{1,2,3}<{3,2,1}
           {true  false  false}
```

If either side or both contains undefined variables, < will wait to return a value. You can do math with the resulting inequality, and if an operation makes sense, it will be applied to both sides: for instance, if x<y, then you can negate it to get -x>-y. An operation will not be applied to both sides if it wouldn't be consistent with the previous inequality: for example, you can't square both sides, since even if x<y the comparison between x^2 and y^2 could go in any order. You can also extract the two halves of the inequality with [68k:left()](68k:left().html) and [68k:right()](68k:right().html).

## Advanced Uses

The < operator can also compare strings. It does so by comparing the [68k:character codes](68k:character-codes.html) of each character, and orders the strings by the first difference it finds. This ideally means that the strings are ordered by dictionary order: for example, "aardvark"<"apple", since it would come later in the dictionary. 

However, the problem is that all uppercase letters have a smaller character code than lowercase letters, so this only holds true if the strings are the same case. Otherwise, strange results can happen: for instance, "Apple"<"aardvark", since "A" comes before "a".

## Related Commands

- [=](68k:equal.html) (equal)
- [≠](68k:not-equal.html) (not equal)
- [>](68k:greater-than.html) (greater than)
- [≥](68k:greater-than-or-equal.html) (greater than or equal)
- [≤](68k:less-than-or-equal.html) (less than or equal)

## See Also

- [68k:order-of-operations](68k:order-of-operations.html)
- [68k:character-codes](68k:character-codes.html)
