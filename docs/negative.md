![The ‾ Command](negative/NEGATIVE.GIF "The ‾ Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Returns the negative value of a number.|‾*value*|TI-83/84/+/SE|1 byte|

### Menu Location
Press [(-)]
# The ‾ Command

The ‾ (negative) operator takes one number, variable, or expression and negates its value, thus returning the negative equivalent of it. The ‾ operator appears higher in the order of operations than both the [relational](operators.html#relational) and [logical](operators.html#logical) operators, so it will be executed first. In addition, it has the same order of operation as the other [math](operators.html#math) operators, so the calculator simply executes them left to right in the order that they appear.

```
:‾1
           -1

:5→X
:‾3(X+2
           -21

:‾2→A:‾3→B
:AB
           6
```

## Optimization

When adding a negative number to a positive number, switch the two numbers around and change the addition to subtraction. This allows you to get rid of the ‾ sign and save a byte.

```
:‾A+B→C
can be
:B-A→C
```
This is not always the case, however: if you subtract a command that uses a lot of parentheses and is followed by a newline/colon/STO→ arrow, it'd save space to put the subtraction at the beginning of the line. For instance:
```
:inString(Ans,sub(Str1,1,1+int(log(A))))-1
can be
:‾1+inString(Ans,sub(Str1,1,1+int(log(A
```

## Error Conditions

If an **[ERR:SYNTAX](errors.html#syntax)** is being thrown near a subtraction or negation where there should be no errors, check to make sure that ‾ (negation) and - (subtraction) were not swapped by mistake.

## Related Commands

- + ([add](add.html))
- - ([subtract](subtract.html))
- * ([multiply](multiply.html))
- / ([divide](divide.html))
