![The nPr Command](npr/NPR.GIF "The nPr Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Calculates the combinatorial number of permutations.|*a* nPr *b*|TI-83/84/+/SE|1 byte|

### Menu Location
Press:
1. MATH to access the [math](math.html) menu.
1. LEFT to access the PRB submenu.
1. 2 to select nPr, or use arrows.
       
# The nPr Command

nPr is the number of permutations function, defined as *a* nPr *b* = *a*!/(*a*-*b*)!, where *a* and *b* are nonnegative integers. The function also works on lists.

**Tip**: nPr has a higher priority in evaluation than operators such as + or *: for example, 5X nPr 10 will be interpreted as 5(X nPr 10) and not as (5X) nPr 10. You might wish to use parentheses around complex expressions that you will give to nPr as arguments.

```
6 nPr 4
     360
```

The combinatorial interpretation of *a* nPr *b* is the number of ways to choose *b* objects in order, when there are *a* objects in total. For example, when giving 1st, 2nd, and 3rd place awards in a competition between 10 teams, there are 10 nPr 3 different ways to assign the awards.

## Error Conditions

- **[ERR:DIM MISMATCH](errors.html#dimmismatch)** is thrown when applying nPr to two lists that have different dimensions.
- **[ERR:DOMAIN](errors.html#domain)** is thrown for negative integers or decimals.

## Related Commands

- [nCr](ncr.html)
- [!](factorial.html)
