![Augment](68k_augment/sample.png "Augment")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|returns a new list or matrix that is list2/matrix2 appended to list1/matrix1|augment(list1,list2)<br>augment(matrix1, matrix2)<br>augment(matrix1; matrix2)|This command works on all calculators.|? byte(s)|
       
### Menu Location
- Press 2nd MATH to enter the MATH popup
- Press 4 to enter the Matrix submenu
- Press 7 to select augment(
       
# Augment

when lists are used as arguments, a list is returned that is list2 appended to list1. When matrices are used, if a comma is used to separate arguments, the matrices must have equal row dimensions and matrix2 is appended to matrix1 as new columns. If a semicolon is used, the matrices must have equal column dimension and matrix2 is appended to matrix1 as new rows.

```
augment({1,⁻3,2},{5,4})
          {1,⁻3,2,5,4}
:[1,2:3,4]→M1
          [1,2:3,4]
:[5,6]→M2
          [5,6]
:augment(M1,M2)
          [1,2,5:3,4,6]
:[5,6]→M2
          [5,6]
:augment(M1;M2)
          [1,2:3,4:5,6]
```

## Advanced Uses

------

Separate unrelated advanced uses with a horizontal bar.

## Optimization

## Error Conditions

**[240 - Dimension mismatch](68k:errors.html#e240)** happens when either the rows or columns of the matrix do not align. See above..



## Related Commands
