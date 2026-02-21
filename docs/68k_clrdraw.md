![The ClrDraw Command](68k_clrdraw/clrdraw.png "The ClrDraw Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Clears the graph screen, redrawing any functions, plots, or axes/grid/labels.|ClrDraw|This command works on all calculators.|2 bytes|
       
### Menu Location
N/A

       
# The ClrDraw Command

The `ClrDraw` command clears away anything drawn on the graph screen — that is, the result of any of the [68k:graphics](68k:graphics.html) commands, except for [`68k:Graph`](68k:graph.html) (which you can only clear with [`68k:ClrGraph`](68k:clrgraph.html)). It also leaves alone any functions or plots (which are disabled by [`68k:FnOff`](68k:fnoff.html) and [`68k:PlotsOff`](68k:plotsoff.html), respectively), as well as axes, labels, a grid, etc. (which can be disabled by the [`68k:setGraph()`](68k:setgraph.html) command).

Be warned that it doesn't update the screen. For example, if you run the following program:
```
:circ()
:Prgm
:Circle 0,0,5
:ClrDraw
:EndPrgm
```
it will draw a circle and then end on the graph screen with the circle still drawn. The screen will actually update the next time you change something on the graph screen; you can also use [`68k:DispG`](68k:dispg.html) to update it (although in the program above, [`68k:DispHome`](68k:disphome.html) might be more appropriate).

## Related Commands

- [`68k:ClrGraph`](68k:clrgraph.html)
- [`68k:ClrHome`](68k:clrhome.html)
- [`68k:ClrIO`](68k:clrio.html)

## See Also

- [68k:setup-and-cleanup](68k:setup-and-cleanup.html)
