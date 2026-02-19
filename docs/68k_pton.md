![The PtOn Command](68k_pton/pton.png "The PtOn Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Draws a point on the graph screen.|PtOn *x*, *y* <br>*or* <br>PtOn {*x1, x2, x3*}, {*y1, y2, y3*}|This command works on all calculators.|2 bytes|
       
### Menu Location
N/A

       
# The PtOn Command

The `PtOn` command draws a point on the graph screen. It uses point coordinates, which means that the result is determined by [window variables](68k:system-variables.html#window): the x-coordinate must be between xmin and xmax, and the y-coordinate must be between ymin and ymax (with (xmin,ymin) being the bottom left and (xmax,ymax) the top right corner).

Unlike pixel commands such as [`68k:PxlOn`](68k:pxlon.html), however, `PtOn` won't give an error if the coordinates happen to be outside these bounds — it simply won't have any effect (exactly the same as the 83+ version of [`Pt-On`](pt-on.html)).

## Advanced Uses

`PtOn` can also be used with two lists of the same size. In that case, it will draw the points for every pair of elements (xlist[n], ylist[n]). This can be used as an alternative to plots (see [`68k:NewPlot`](68k:newplot.html)) to plot a set of points.

## Related Commands

- [`68k:PtOff`](68k:ptoff.html)
- [`68k:PtChg`](68k:ptchg.html)
- [`68k:PxlOn`](68k:pxlon.html)
- [`68k:PxlOff`](68k:pxloff.html)
- [`68k:PxlChg`](68k:pxlchg.html)
