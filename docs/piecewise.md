![The piecewise( Command](piecewise/piecewise(.png "The piecewise( Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Graphs up to 5 piecewise expressions.|(expression, condition [,expression, condition]) <br><br>Up to 5 (expression,condition) pieces are allowed.|TI-84+CE OS 5.3|2 bytes|

### Menu Location
1: While editing a program, press [math]<br><br>2: Then press [alpha] [apps] (B) or scroll down.
# The piecewise( Command

The `piecewise(` command is a new addition in the release of OS 5.3 for the TI-84 Plus CE. As implied, it allows for the graphing of piecewise functions in the Y= editor. The example code demonstrates how this works from within a program.

```
:ClrDraw
:Input "Y1=",Str1
:Input "Y2=",Str2
:Str1→Y1
:Str2→Y2
:FnOff
:"piecewise(Y1,X≥0,Y2,X<0→Y3
:DispGraph
```

## Advanced Uses

One use of the `piecewise(` function is to evaluate an expression for a given value of X. For example:

```
:piecewise(X²+2,X≥0
```

This code will return the value of the expression if X≥0. So if X=0, then the program will return a value of 2. If X=3, it will return a value of 11. If X=-5, it will return an error.

## Optimization

This command can simplify and compact the usage of piecewise expressions in programs. If you have less than 6 conditions that will never overlap, and they all affect a single variable, you can use the `piecewise(` command to make your code smaller, as shown below. Beware of comparability, though.

```
:If X<2
:Then
:4.5X→N
:Else
:8X+3→N
:End
can be
:piecewise(4.5X,X<2,8X+3,X≥2→N
```

## Error Conditions

- **[ERR:INVALID](errors.html#invalid)** is thrown if expressions are not defined.
- **[ERR:DATA TYPE](errors.html#data-type)** is thrown if a quotation mark is not placed before a piecewise command that is to be stored to an equation variable.

## See Also

- [Technique: Piecewise Expressions](piecewise-expressions.html)
