![The randM( Command](randm/RANDM.GIF "The randM( Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Creates a matrix of specified size with the entries random integers from -9 to 9.|randM(*# rows*, *# columns*)|TI-83/84/+/SE|1 byte|

### Menu Location
Press:
1. MATRX (TI-83) or 2nd MATRX (TI-83+ or higher) to access the matrix menu
2. RIGHT to access the MATH submenu.
3. 6 to select randM(, or use arrows.
       
# The randM( Command

randM(*M*, *N*) generates an M by N matrix whose entries are pseudorandom integers between -9 and 9 inclusive.

*seed*→rand affects the output of randM(.

```
0→rand
	0
randM(3,3)
	[[9  -3 -9]
	 [4  -2 0 ]
	 [-7 8  8 ]]
```

If you actually cared about the bounds of the random numbers, this command would not be very useful, since it's hard to manipulate the matrix to yield uniformly spread random numbers in a different range.

## Formulas

The entries of randM( are actually the outputs of successive calls to randInt(-9,9), filled in starting at the bottom right and moving left across each row from the last row to the first.

## Error Conditions

- **[ERR:INVALID DIM](errors.html#invaliddim)** is thrown if the number of rows or columns of the matrix isn't an integer 1-99.

## Related Commands

- [rand](rand.html)
- [randInt(](randint.html)
- [randNorm(](randnorm.html)
- [randBin(](randbin.html)
- [randIntNoRep(](randintnorep.html)
