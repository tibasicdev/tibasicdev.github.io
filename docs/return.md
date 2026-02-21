![The Return Command](return/RETURN_ANIMATED.GIF "The Return Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Stops the program and returns the user to the home screen. If the program is a subprogram, however, it just stops the subprogram and returns program execution to the parent program.|Return|TI-83/84/+/SE|1 byte|

### Menu Location
Press:
1. PRGM to enter the PRGM menu
2. ALPHA SIN to choose Return, or use arrows
       
# The Return Command

When the Return command is used in a program it exits the program (terminating the program execution) and returns the user to the home screen. If it is encountered within [loops](while.html), the loops will be stopped.

There is some distinction when using Return with [subprograms](subprograms.html): the Return command will stop the program execution of the subprogram, and program execution will go back to the calling program, continuing right after the subprogram call. If this functionality is not desired, then you should use the [Stop](stop.html) command instead. Generally, though, you should use Return instead of Stop.

```
:ClrHome
:Input "Guess:",A
:Stop
Replace Stop with Return
:ClrHome
:Input "Guess:",A
:Return
```

## Optimization

You don't have to put a Return command at the end of a program or subprogram if you can organize the program so that it just naturally quits. When the calculator reaches the end of a program, it will automatically stop executing as if it had encountered a Return command (the Return is implied).

```
:ClrHome
:Input "Guess:",A
:Return
Remove the Return
:ClrHome
:Input "Guess:",A
```

## Error Conditions

- **[ERR:INVALID](errors.html#invalid)** occurs if this statement is used outside a program.

## Related Commands

- [prgm](prgm.html)
- [Stop](stop.html)

## See Also

- [Subprograms](subprograms.html)
