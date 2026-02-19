![The or Command](or/OR.GIF "The or Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Returns the truth value of *value1* or *value2* being true.|*value1* or *value2*|TI-83/84/+/SE|1 byte|

### Menu Location
Press:
1. 2nd TEST to access the test menu.
1. RIGHT to access the LOGIC submenu.
1. 2 to select or, or use arrows and ENTER.
       
# The or Command

**or** takes two numbers or expressions, and checks to see if *either one* is True.  If both are False, it returns 0.  If at least one is True, it returns 1.  **or** is commutative (i.e. the order of arguments does not matter). As with **[and](and.html)**, you can use variables and expressions, and use multiple **or**'s together.
```
:0 or 1-1
           0

:0 or -1
           1

:2 or 6*4
           1

:0 or 1 or 0
           1
```

## Related Commands

- [and](and.html)
- [xor](xor.html)
- [not(](not.html)
