![The angle() Command](68k_angle/angle.png "The angle() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Returns the angle of *expression*, interpreting *expression* as a complex number.|angle(*expression*)|This command works on all calculators.|X byte(s)|
       
### Menu Location
- Press 2nd MATH to enter the MATH popup menu.
- Press 5 to enter the Complex submenu.
- Press 4 to select angle(
       
# The angle() Command


The `angle()` command returns the angle of a complex number. The argument may be an expression, a list, or a matrix. In the case of a lists and matrices, each element is evaluated individually and the result is outputted to the corresponding element of a matrix or list of the same dimensions as the original.

```
:angle(2i)
      pi/2
:angle({2i,3+i})
      {pi/2  tan^-1(1/3)}
:angle([[2i,3+i][i+7,2i]])
      [pi/2  tan^-1(1/3)]
      [tan^-1(1/7)  pi/2]
```
