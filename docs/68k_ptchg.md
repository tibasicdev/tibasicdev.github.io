![The PtChg Command](68k_ptchg/ptchg.png "The PtChg Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Inverts a point on the graph screen.|PtChg *x*, *y*|This command works on all calculators.|2 bytes|
       
### Menu Location
N/A

       
# The PtChg Command

The `PtChg` command inverts a point on the graph screen — drawing it if it isn't already there, and erasing it otherwise. It uses point coordinates, which means that the result is determined by [window variables](68k:system-variables.html#window): the x-coordinate must be between xmin and xmax, and the y-coordinate must be between ymin and ymax (with (xmin,ymin) being the bottom left and (xmax,ymax) the top right corner).

Unlike pixel commands such as [`68k:PxlChg`](68k:pxlchg.html), however, `PtChg` won't give an error if the coordinates happen to be outside these bounds — it simply won't have any effect.

## Advanced Uses

`PtChg` can also be used with two lists of the same size. In that case, it will invert the points for every pair of elements (xlist[n], ylist[n]). This can be used as an alternative to plots (see [`68k:NewPlot`](68k:newplot.html)) to plot a set of points.

## Related Commands

- 
- [`68k:PtOn`](68k:pton.html)
- [`68k:PtOff`](68k:ptoff.html)
- [`68k:PxlOn`](68k:pxlon.html)
- [`68k:PxlOff`](68k:pxloff.html)
- [`68k:PxlChg`](68k:pxlchg.html)
