![The PrintScreen Command](printscreen/PRINTSCREEN.GIF width="192" height="128" style="border: 1px solid black;" "The PrintScreen Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|This command doesn't exist. A [token](http://tibasicdev.github.io/tokens) for it does, though.|PrintScreen|TI-82|1 byte|

### Menu Location
This command requires a hex editor to access.
       
# The PrintScreen Command

On the TI-82, the PrintScreen command could be found in the I/O submenu of the PRGM menu. According to the TI-82 manual, it "prints the current screen on a printer attached to an IBM®-compatible computer or a Macintosh® if you are using TI-GRAPH LINK™ software". Aside from this potential interaction with computers, it was otherwise equivalent to [Pause](pause.html).

On the TI-83 series calculators or higher, a token is still set aside for the PrintScreen command. However, the command doesn't actually do anything, and will cause an error if you try to use it. It's not accessible through any menus, though, so that's okay.

The only potential use is to save on memory if you ever need to display "PrintScreen" somewhere - you can display this token instead.

## Error Conditions

- **[ERR:INVALID](errors.html#invalid)** occurs if this statement is used outside a program.
- **[ERR:INVALID](errors.html#invalid)** also occurs if this statement is used inside a program.
