![The arcLen() Command](68k_arclen/arclen.png "The arcLen() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Returns the arc length of *expression1* from *start* to *end* with respect to variable *var*.|arcLen(*expression1*,*var*,*start*,*end*)|This command works on all calculators.|X byte(s)|
       
### Menu Location
Describe how to get the command from a menu.
       
# The arcLen() Command

The `arcLen()` command uses the integral arc length formula to calculate the arc length of a function over the specified interval.

```
arcLen(cos(x),x,0,π)
                              3.82019...
```

## Advanced Uses

The `arcLen()` command also works on lists of expressions:
```
arcLen({sin(x),cos(x)},x,0,π)
                         {3.820...  3.810...}
```

------

Separate unrelated advanced uses with a horizontal bar.

## Optimization

This section includes both ways to optimize use of the command, and other common pieces of code that this command can replace in an optimization. Make sure to mention if the optimization improves speed of the program, size, or both. Sample code should be included too, preferably in the following format:

```
:∫(√(1+d(f(x),x)²),x,a,b)
can be
:arcLen(f(x),x,a,b)
```

## Related Commands

- [`∫()`](68k:integral.html) (integral)
- [`d()`](68k:d.html) (derivative)
