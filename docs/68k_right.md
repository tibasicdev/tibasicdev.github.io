![The right() Command](68k_right/right.png "The right() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Returns a subsection from the right of a list or string, or the right hand side of an equation.|right(*equation*)<br>right(*list-or-string*,*length*)|This command works on all calculators.|2 bytes|
       
### Menu Location
- Press 2nd MATH to enter the MATH popup menu.
- Press 3 to enter the List submenu.
- Press B to select right(.
       
# The right() Command

When applied to a list or a string, right(*x*,*length*) gets the last (right-most) *length* elements/characters of *x*. 

When applied to an equation (such as x=5) or an inequality (such as x<3), right() returns the right-hand side of the equation. This only works for equations that don't get simplified: right(2+2=4) will not work, because 2+2=4 will return 'true' first.

```
:right({1,2,3,4,5},3)
           {3  4  5}
:right("TI-Basic Developer",9)
           "Developer"
:right(x^2+2x+1>0)
           0
:right({1,2,3,4,5},0)
           {}
```

## Error Conditions




## Related Commands

- [68k:left()](68k:left.html)
- [68k:mid()](68k:mid.html)
