![The GridOn Command](gridon/GRIDON.GIF "The GridOn Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Enables the grid on the graph screen.|GridOn|TI-83/84/+/SE|2 bytes|

### Menu Location
Press:
1. 2nd FORMAT to access the graph format menu.
1. Use arrows and ENTER to select GridOn.
       
# The GridOn Command

The `GridOn` command enables a grid on the graph screen (you can disable it again with the [`GridOff`](gridoff.html) command). How fine or coarse the grid is depends on the [`Xscl`](system-variables.html#window) and [`Yscl`](system-variables.html#window) variables. Drawing the grid just involves plotting points all the points of the form (`A*Xscl`, `B*Yscl`) that are in the graphing window. The grid is often used in games such as Dots & Boxes, Tic-Tac-Toe, and 2D puzzles.

On the TI-84+CSE and TI-84+CE, an additional argument may be used to set the color of the grid:

```
:GridOn GRAY
```

Like other drawing commands, the color may be replaced by its numerical value (ranging from 10 to 24).

## Advanced Uses

`GridOn` can be used to shade the entire screen if `Xscl` and `Yscl` are small enough that the points on the grid are one pixel apart:
```
:ΔX→Xscl
:ΔY→Yscl
:GridOn
```

This is one of the shortest ways to shade the screen, although [`Shade(`](shade.html) can be used for a (usually) even shorter way. However, using `GridOn` is also very slow: the fastest way involves the [`Horizontal`](horizontal.html) or the [`Vertical`](vertical.html) commands in a [`For(`](for.html) loop (or the [`BackgroundOn`](backgroundon.html) command for color calculators).

## Related Commands

- [`GridOff`](gridoff.html)
- [`GridDot`](griddot.html)
- [`GridLine`](gridline.html)
- [`AxesOn`](axeson.html)
- [`AxesOff`](axesoff.html)
