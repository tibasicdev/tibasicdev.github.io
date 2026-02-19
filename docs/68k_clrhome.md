![The ClrHome Command](68k_clrhome/clrhome.png "The ClrHome Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Clears the home screen.|ClrHome|This command works on all calculators.|2 bytes|
       
### Menu Location
N/A

# The ClrHome Command

The `ClrHome` command clears the home screen — not the I/O screen where the result of commands like [`68k:Disp`](68k:disp.html) or [`68k:Output`](68k:output.html) is displayed (you'd need [`68k:ClrIO`](68k:clrio.html) for that), but the screen where you run programs and evaluate expressions. This isn't usually something you want a program to clear, so this isn't a very exciting command.

It also has the drawback that the `ClrHome` command itself (or the program it's used in) is displayed on the home screen *after* it is cleared, so the end result is not a blank screen but something like what you see in the screenshot to the right.

Finally, `ClrHome` cannot be used inside a function, because functions aren't allowed to modify the state of the calculator.

## Error Conditions



## Related Commands

- [`68k:ClrIO`](68k:clrio.html)
- [`68k:ClrDraw`](68k:clrdraw.html)
- [`68k:DispHome`](68k:disphome.html)
