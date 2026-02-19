![The Thick Command](thick/Thick.png "The Thick Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Converts all lines to Thick (2-3 pixel wide) lines|The command is called by itself with no additional arguments|TI-84+CSE/CE|2 bytes|

### Menu Location
Go to the Catalog, press [ALPHA][4], and scroll down.
       
# The Thick Command

The Thick command converts all lines in the current function type to be drawn using a 2-3 pixel wide line (hence "Thick"). This mode is the default line drawing mode. It can be called on the homescreen or in a program. 

```
:AxesOff
:GridOff
:Thick
```

## Error Conditions

- **[ERR:SYNTAX](errors.html#syntax)** is thrown if any character is included in the same line as the Thick command.

## Related Commands

- [Thin](http://www.tibasicdev.github.io/thin)
