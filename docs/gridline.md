![The GridLine Command](gridline/GridLine.png "The GridLine Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Enables a grid of colored lines on the graph screen.|GridLine [*color#*]|TI-84+ CSE/CE|2 bytes|

### Menu Location
Press:
1. 2nd FORMAT to access the graph format menu.
2. Use arrows and ENTER to select GridLine.
       
# The GridLine Command

The `GridLine` command enables a grid of colored lines on the graph screen (you can disable it with the [`GridOff`](gridoff.html) command). How fine or coarse the grid is depends on the [`Xscl`](system-variables.html#window) and [`Yscl`](system-variables.html#window) variables. Drawing the grid just involves plotting points all the horizontal and vertical lines that intersect points of the form (A×`Xscl`, B×`Yscl`) that are in the graphing window. The grid can be colored based on any color variable or value.

## Advanced Uses

`GridLine` can be used to shade the entire screen if `Yscl` is small enough that the lines on the grid are one pixel apart:
```
:ΔY→Yscl
:GridLine RED
```

This is one of the shortest ways to shade the screen, although [`Shade(`](shade.html) can be used for a (usually) even shorter way. However, using `GridLine` is also very slow: the fastest way involves the [`Horizontal`](horizontal.html) or the [`Vertical`](vertical.html) commands in a [`For(`](for.html) loop.

You could also use `GridLine` to draw the playing grid for a Dots and Boxes game.

## Related Commands

- [GridOn](gridon.html)
- [GridOff](gridoff.html)
- [GridDot](griddot.html)
- [AxesOn](axeson.html)
- [AxesOff](axesoff.html)
