![The left() Command](68k_left/left.png "The left() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Returns a subsection from the left of a list or string, or the left hand side of an equation.|left(*equation*)<br>left(*list-or-string*,*length*)|This command works on all calculators.|2 bytes|
       
### Menu Location
- Press 2nd MATH to enter the MATH popup menu.
- Press 3 to enter the List submenu.
- Press 9 to select left(.
       
# The left() Command

When applied to a list or a string, left(*x*,*length*) gets the first *length* elements/characters of *x*. This is an alternative to [68k:mid()](68k:mid.html), which will do the same thing from any point in the list or string, not just the beginning.

When applied to an equation (such as x=5) or an inequality (such as x<3), left() returns the left-hand side of the equation. This only works for equations that don't get simplified: left(2+2=4) will not work, because 2+2=4 will return 'true' first.

```
:left({1,2,3,4,5},3)
           {1  2  3}
:left("TI-Basic Developer",8)
           "TI-Basic"
:left(x^2+2x+1>0)
           x^2+2*x+1
:left({1,2,3,4,5},0)
           {}
```

## Optimization

Use left() instead of mid() when the substring starts at the beginning of the list or string.

## Error Conditions

**[260 - Domain error](68k:errors.html#e260)** happens when the argument is not a list, string, or equation, or is an equation that has simplified.

## Related Commands

- [68k:mid()](68k:mid.html)
- [68k:right()](68k:right.html)
