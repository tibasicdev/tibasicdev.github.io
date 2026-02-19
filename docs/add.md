![The + Command](add/ADD.GIF "The + Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Returns the sum of two numbers, or joins two strings together.|*value1* + *value2*<br><br>*string1* + *string2*|TI-83/84/+/SE|1 byte|

### Menu Location
Press  [+]
       
# The + Command

The + (add) operator takes two numbers, variables, or expressions and adds their values together, thus returning a single new value. The + operator appears lower in the order of operations than both [*](multiply.html) and [/](divide.html), so if those appear in an expression, they will be executed first. In addition,  the [-](subtract.html) operator has the same order of operations as +, so the calculator simply executes them left to right in the order that they appear.

```
:1+1
           2

:5→X
:2+3X
           17

:2→A:3→B
:A/B+B/A
           2.166666667
```

## Advanced Uses

The + operator is overloaded (meaning it has more than one function) by the calculator, and it can be used to put [strings](strings.html) together. The strings can consist of whatever combination of text and characters that you want, but it unfortunately does not allow you to join a string to a number (i.e., "Hello5" cannot be made with "Hello"+5).

```
:"HELLO"+"WORLD
           "HELLOWORLD

:"TI"+"-"+"BASIC
           "TI-BASIC
```

## Related Commands

- - ([subtract](subtract.html))
- * ([multiply](multiply.html))
- / ([divide](divide.html))
