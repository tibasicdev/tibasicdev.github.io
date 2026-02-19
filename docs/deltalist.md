![The ΔList( Command](deltalist/DELTALIST.GIF "The ΔList( Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Calculates the differences between consecutive terms of a list.|ΔList(*list*)|TI-83/84/+/SE|2 bytes|

### Menu Location
Press:
1. 2nd LIST to access the list menu.
1. RIGHT to access the OPS submenu.
1. 7 to select ΔList(, or use arrows.
       
# The ΔList( Command

`ΔList(` calculates the differences between consecutive terms of a list, and returns them in a new list.

```
ΔList({0,1,4,9,16,25,36})
	{1 3 5 7 9 11}
```

## Advanced Uses

The ΔList( command is very nearly the inverse of the [cumSum(](cumsum.html) command, which calculates the cumulative sums of a list. For any list, `ΔList(cumSum(*list*))` will return the same list, but without its first element:
```
ΔList(cumSum({1,2,3,4,5,6,7}))
    {2 3 4 5 6 7}
```

Removing the first element would otherwise be a difficult procedure involving the [seq(](seq-list.html) command, so this is a useful trick to know.

If a list is sorted in ascending order, `min(ΔList(*list*))` will return 0 (false) if there are repeating values in the list, and a value corresponding to true if they are all distinct. The number of repeating elements can be determined similarly via `1+sum(0≠ΔList(*list*))` (again, so long as the list is sorted).

## Error Conditions

- **[ERR:INVALID DIM](errors.html#invaliddim)** is thrown if `ΔList(` is run on a single element list.

## Related Commands

- [`sum(`](sum.html)
- [`cumSum(`](cumsum.html)
- [`augment(`](augment.html)
