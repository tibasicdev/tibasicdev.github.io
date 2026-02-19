![newMat](68k_newmat/newmat.png "newMat")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|returns a new matrix filled with 0s given the dimensions provided|newMat(rows,cols)<br>newMat(rows,cols)|This command works on all calculators.|~8 byte(s)|
       
### Menu Location
- Press 2nd MATH to enter the MATH popup<br>* Press 4 to enter the Matrix submenu<br>* Press F ( Alpha
# newMat

When integers are used as arguments, newMat() returns an empty matrix of the specified dimensions filled with zeros. When any type other than integers are used as as arguments, newMat returns a Data Type error. 

```
newMat(3,2)
          [[0,0][0,0][0,0]]
```

## Advanced Uses

------

Can be used to pre-allocate matrices for programs.

## Optimization

## Error Conditions



## Related Commands
