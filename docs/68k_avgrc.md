![Avgrc](68k_avgrc/sample.png "Avgrc")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Returns the forward-difference quotient (average<br>rate of change).|avgRC(expression1, var [,h])|This command works on all calculators.|? byte(s)|
       
### Menu Location
This command can only be found in the CATALOG
       
# Avgrc

AvgRC() returns an expression equal to the following formula:

$$
\frac{f(x+h)-f(x)}{h}$$

h is the step value, which defaults to 0.001.

```
:avgRC(f(x),x,h)
           (f(x+h)-f(x))/h
:avgRC(sin(x),x,h)|x=2
          sin(h+2)-sin(2)/h
:avgRC(x^2-x+2,x)
          2.*(x-.4995)
:avgRC(x^2-x+2,x,.1)
          2.*(x-.45)
:avgRC(x^2-x+2,x,3)
          2*(x-1)
```

------

## Error Conditions

## Related Commands

- Command 1
- Command 2
- Command 3 

## See Also

- Design Concept 1
- Design Concept 2
- Technique 1
