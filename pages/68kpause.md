![The Pause Command](68k_pause/pause.png "The Pause Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Pauses the program until ENTER is pressed, optionally displaying text on the I/O screen.|:Pause [*expression*]|This command works on all calculators.|3 bytes|
       
### Menu Location
Starting in the program editor:<br>* Press F2 to enter the Control menu.<br>* Press 8 to enter the Transfers submenu.<br>* Press 1 to select Pause.
# The Pause Command

Used by itself without parameters, `Pause` temporarily suspends the program until the ENTER key is pressed, displaying an indicator to that effect in the lower right corner of the screen. When ENTER is pressed, the program continues running from the next command in order.

`Pause` can also be given any expression as a parameter. In this case, it will display the expression on a new line on the Program I/O screen (just like [`68k:Disp`](68k:disp.html)), and then pause the program as above. Unlike `Disp`, however, it can only display one thing.

## Optimization

Make sure to give Pause an argument if using it with Disp:
```
:Disp x
:Pause

can be

:Pause x
```

## Related Commands

- [`68k:Disp`](68k:disp.html)
- [`68k:getKey()`](68k:getkey().html)
- [`68k:Output`](68k:output.html)
