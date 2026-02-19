![The cumSum() Command](68k_cumsum/CUMSUM.png "The cumSum() Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Calculates cumulative sums of a list or of the columns of a matrix.|cumSum(*list or matrix*)|TI-89/92/+/v200|7 bytes|

### Menu Location
Press:<br># 2nd [MATH] to access the [68k:math](68k:math.html) menu.<br># 3 to access the list submenu, or use arrows.<br># 7 to select cumSum(), or use arrows.<br><br>Alternatively, type cumSum( with the keyboard.
# The cumSum() Command

`cumSum(` calculates the cumulative sums of a list, or of the columns of a matrix, and outputs them in a new list or matrix variable.

For a list, this means that the Nth element of the result is the sum of the first N elements of the list, and the N-1th element of the result is the sum of the first N-1 elements, and so on:
```
cumSum({1,3,5,7,9})
	{1 4 9 16 25}
```

For a matrix, `cumSum(` is applied to each column in the same way as it would be for a list (but numbers in different columns are never added):
```
cumSum([[0,1,1][0,1,3][0,1,5][0,1,7]])
	[[0 1 1]
	 [0 2 4]
	 [0 3 9]
	 [0 4 16]]
```

## Advanced Uses

For a matrix, if you want to sum up the rows instead of the columns, use the `<sup>T</sup>` ([`68k:transpose`](68k:transpose.html)) command.
```
(cumSum([[0,1,1][0,1,3][0,1,5][0,1,7]]ᵀ))ᵀ
	[[0 1 2]
	 [0 1 4]
	 [0 1 6]
	 [0 1 8]]
```

## Related Commands

- `<sup>T</sup>` ([`68k:transpose`](68k:transpose.html))
