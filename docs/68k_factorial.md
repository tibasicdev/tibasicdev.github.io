![The ! Command](68k_factorial/factorial.png "The ! Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Takes the factorial of a number.|*number*!|This command works on all calculators.|1 byte|
       
### Menu Location
N/A

       
# The ! Command

The ! operator takes the factorial of a number: for a positive, whole number, n! is defined as n*(n-1)*(n-2)*...*3*2*1. As a special case, 0! is defined to be 1.

The factorial has a special meaning in combinatorics: n! is the number of ways you can order n objects. For instance, 3!=6 because there are 6 ways to order 3 objects:
- A B C
- A C B
- B A C
- B C A
- C A B
- C B A

As can be expected, factorials get very large very quickly. The calculator can only compute an exact integer result for factorials up to 299!, and an approximate result for factorials up to 449!. Beyond that, the numbers involved are replaced by ∞ (infinity) in expressions.

While there are some formulas to define factorials of non-integer values, the calculator doesn't use them. It will leave an expression like (1/2)! unsimplified. However, the factorial of a number less than or equal to -1 will be "undef".

```
:5!
           120
:299!
           1020191707388... (600 more digits)
:449!
           3.85193e997
:(-2)!
           undef
```

## Related Commands

- [68k:nCr()](68k:ncr.html)
- [68k:nPr()](68k:npr.html)

## See Also

- [68k:order-of-operations](68k:order-of-operations.html)
