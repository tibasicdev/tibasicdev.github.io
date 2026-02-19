![The Line Command](68k_line/line.png "The Line Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Draws a line between a set of two coordinates.|Line xStart, yStart, xEnd, yEnd, drawmode|This command works on all calculators.|X byte(s)|
       
### Menu Location

# The Line Command

The `line` command draws a line between two points. By default, the drawing mode is set to 1, which draws the line normally, so it doesn't have to be included if drawing a regular line.
```
Line 0, 3, 0, 9
```
## Advanced Uses
The drawmode can be set to 0 to draw a "white" line, which will remove the pixels on the path of the line.
```
Line 0, 3, 0, 9, 0 //removes the line
```
You can also invert pixels on the line using -1 as the number argument.
```
Line 0, 3, 0, 9, -1
```

## Related Commands

- [`68k:PtOn`](68k:pton.html)
- [`68k:LineVert`](68k:linevert.html)
- [`68k:LineHoriz`](68k:linehoriz.html)
