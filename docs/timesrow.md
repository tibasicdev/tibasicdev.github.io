![The *row( Command](timesrow/TIMESROW.GIF "The *row( Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Multiplies a row by a scalar.|*row(*factor*,*matrix*,*row*)|TI-83/84/+/SE|1 byte|

### Menu Location
Press:
1. MATRX (on a TI-83) or 2nd MATRX (TI-83+ or higher) to access the matrix menu.
2. RIGHT to access the MATH submenu.
3. ALPHA E to select *row(, or use arrows and ENTER.
       
# The *row( Command

The *row( command multiplies a row of a matrix by a scalar factor and returns the result. It is an elementary row operation used in Gaussian Elimination. 

```
[[1,2][3,4]]
	[[1 2]
	 [3 4]]
*row(10,Ans,1)
	[[10 20]
	 [3  4 ]]
```

## Advanced Uses

You can multiply columns instead of rows with the aid of the <sup>T</sup> ([transpose](transpose.html)) command.

## Error Conditions

- **[ERR:INVALID DIM](errors.html#invaliddim)** is thrown if the row argument isn't a valid row (is larger than the size of the matrix, or otherwise bad)

## Related Commands

- [rowSwap(](rowswap.html)
- [row+(](rowplus.html)
- [*row+(](timesrowplus.html)
