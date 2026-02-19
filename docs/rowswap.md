![The rowSwap( Command](rowswap/ROWSWAP.GIF "The rowSwap( Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Swaps two rows of a matrix.|rowSwap(*matrix*,*row1*,*row2*)|TI-83/84/+/SE|1 byte|

### Menu Location
Press:
1. MATRX (on a TI-83) or 2nd MATRX (TI-83+ or higher) to access the matrix menu.
1. RIGHT to access the MATH submenu.
1. ALPHA C to select rowSwap(, or use arrows and ENTER.
       
# The rowSwap( Command

The rowSwap( command swaps two rows of a matrix and returns the result. It is an elementary row operation used in Gaussian Elimination. 

```
[[1,2][3,4]]
	[[1 2]
	 [3 4]]
rowSwap(Ans,1,2)
	[[3 4]
	 [1 2]]
```

## Advanced Uses

You can swap columns instead of rows with the aid of the <sup>T</sup> ([transpose](transpose.html)) command.

## Error Conditions

- **[ERR:INVALID DIM](errors.html#invaliddim)** is thrown if one of the row arguments isn't a valid row (larger than the matrix size, or otherwise bad)

## Related Commands

- [row+(](rowplus.html)
- [*row(](timesrow.html)
- [*row+(](timesrowplus.html)
