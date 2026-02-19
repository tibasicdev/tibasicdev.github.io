![The ClrIO Command](68k_clrio/clrio.png "The ClrIO Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Clears the program IO screen|Use on the homescreen or in a program. Invalid in a function.|This command works on all calculators.|2 bytes|
       
### Menu Location

       
# The ClrIO Command

This is used to clear the IO buffer (not the home screen). The IO buffer is where any `Output()`, `Disp`, `Pause`, and any other commands that use the I/O buffer display results.
```
:ClrIO
:Disp "Hello"
```

## Related Commands

- [`68k:ClrDraw`](68k:clrdraw.html)
- [`68k:ClrHome`](68k:clrhome.html)
