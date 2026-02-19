![The round( Command](round/ROUND.GIF "The round( Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Truncates a number to a specified number of decimal places.|round(*value*[,*#decimals*])|TI-83/84/+/SE/CE|1 byte|

### Menu Location
Press:<br># MATH to select the [math](math.html) menu.<br># RIGHT to select the NUM submenu.<br># 2 to select round(, or use arrows.
# The round( Command

`round(*value*[,*#decimals*])` returns *value* rounded to *#decimals* decimal places. *#decimals* must be < 10. The default value for *#decimals* is 9. Also works on complex numbers, lists and matrices.

```
round(5.45,0)
     5
round(5.65,0)
     6
round(‾5.65,0)
     ‾6
round(π)-π
     4.102e-10
round(π,4)
     3.1416
round({1.5,2.4,3.8},0)
     {2,2,4}
round([[1.8,3.5,120.3][3,‾1,0.2]],0)
     [[2  4   120]
     [3  ‾1  0   ]]
```

## Advanced Uses

Sometimes, round-off error will cause the result of an expression to be slightly off of the correct integer value — for example, a result may be 5.0000000013 instead of 5. If the error is small enough, it will not even be visible if you recall the variable on the home screen. However, this is enough to cause a [`ERR:DOMAIN`](errors.html#domain) error with commands such as [`sub(`](sub.html) and [`Output(`](output.html), which require their arguments to be integers.

The easiest way to fix this problem is by wrapping the different arguments in a `[round](round.html)(` instruction. For example, instead of:

```
Output(X,1,">")
```

Try:

```
Output(round(X,0),1,">")
```

The [`int(`](int.html) command will not work here because the round-off error may be negative, such as 4.9999999986 instead of 5, in which case the number will be rounded down to 4.

## Error Conditions

- **[ERR:DOMAIN](errors.html#domain)** if the number of places to round to is not an integer 0 through 9.

## Related Commands

- [int(](int.html)
- [iPart(](ipart.html)
- [fPart(](fpart.html)
