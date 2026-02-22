# The T (Transpose) Command
![T.GIF](T.GIF "")

**Command Summary**

This command calculates the transpose of a matrix.

**Command Syntax**

*matrix*<sup>T</sup>

**Menu Location**

Press:
1. MATRX (on the 83) or 2nd MATRX (83+ or higher) to access the Matrix menu.
2. LEFT to access the MATH submenu
3. 2 to select <sup>T</sup>, or use arrows

**Calculator Compatibility**

TI-83/84/+/SE

**Token Size**
 
[1 byte](tokens.html)


The <sup>T</sup> command is used to calculate the transpose of a matrix: it flips a matrix along its main diagonal. This means that the (i,j)th element becomes the (j,i)th element, and vice versa. As a result, the transpose of an M by N matrix is an N by M matrix.

```
[[1,2,3][4,5,6]{$br}
            	[[1 2 3]
             	 [4 5 6]{$br}
Ans<sup>T</sup>
            	[[1 4]
             	 [2 5]
             	 [3 6]{$br}
```

## Advanced Uses

In addition to its many uses in linear algebra, the <sup>T</sup> operation is useful to programmers: with operations such as [Matr►list(](matr-list.html) and [augment(](augment.html), which normally deal with columns, <sup>T</sup> allows you to use rows instead. See the "Related Commands" section for the commands that this is useful for.

## Related Commands

- [augment(](augment.html)
- [cumSum(](cumsum.html)
- [Matr►list(](matr-list.html)
- [rowSwap(](rowswap.html) (and other row operations)
