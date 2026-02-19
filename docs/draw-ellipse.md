# Draw Ellipse
|Routine Summary|Inputs|Outputs|Variables Used|Author|Download|
|--- |--- |--- |--- |--- |--- |
|Draws an ellipse with specified coordinates.|(A,B) - upper left corner, in pixels<br>(C,D) - lower right corner, in pixels|Ellipse inscribed in the rectangle from (A,B) to (C,D)|A,B,C,D for input<br>∟X and ∟Y store a sin/cos look-up table<br>Plot1 to store the unit circle<br>Pic1 to preserve background|Mikhail Lavrov (DarkerLine)|http://mpl.unitedti.org/?p=13 http://mpl.unitedti.org/?p=13|

**Setup:**
```
:cos(.1πcumSum(binomcdf(20,0→X
:sin(.1πcumSum(binomcdf(20,0→Y
:Plot1(xyLine,∟X,∟Y,(dot)
:PlotsOff
```
**Main code:**
```
:StorePic 1
(:ZoomSto)
:-(B+D)/abs(D-B→Xmin
:(A+C-124)/abs(C-A→Ymin
:2/abs(D-B→ΔX
:2/abs(C-A→ΔY
:PlotsOn 1
:RecallPic 1
:StorePic 1
:PlotsOff
(:ZoomRcl)
:RecallPic 1
```

To use the routine, add the setup code to the beginning of your program. Then, to draw an ellipse, initialize (A,B) and (C,D) to be opposite corners of an imagined rectangle, in pixel coordinates, and run the main code of the routine. The ellipse will be drawn inside this rectangle (much like the functionality of the circle tool in Paint). Unlike built-in pixel commands, this routine doesn't require the pixels to be on-screen: you can use negative coordinates, and coordinates past the 62nd row and 94th column - of course, if you do, then the off-screen part of the ellipse won't be drawn.

As for speed, the routine is far faster than the [Circle(](circle.html) command. If you use Circle( with its undocumented fourth argument, that is a bit faster still - but doesn't allow you as much control over the shape of the ellipse as this routine does.

This routine draws an ellipse given its pixel coordinates in two overall steps:
1. First, it calculates the window dimensions so that the unit circle (centered at the origin, with radius 1) will be stretched to the required pixel coordinates.
1. Next, it draws the unit circle.

If the unit circle is stretched to fit in the rectangle from (A,B) to (C,D) then we know the following: 
- The vertical distance from A to C (in pixel rows) should be equivalent to the window distance 2 (from -1 to 1). This allows us to solve for ΔY.
- The horizontal distance from B to D (in pixel columns) should also be equivalent to the window distance 2. This allows us to solve for ΔX.
- The pixel most nearly corresponding to the midpoint between (A,B) and (C,D) should be equivalent to the point (0,0), the center of the circle. Given ΔX and ΔY, this allows us to solve for Xmin and Ymin.

The exact math isn't significant, but it gives rise to the formulas you see in the routine. Note that by using the [abs(](abs.html) command, we ensure that the order of the two points (A,B) and (C,D) isn't important: you can switch A and C, or B and D, and still get the same circle.

The code for actually drawing the circle uses a [look-up table](lookuptables.html) for sine and cosine (which defines 20 points spaced around the circle). The table is calculated in the setup code, and then an [xyLine plot](plotn.html#xyline) is initialized, which will connect these 20 points when graphed. Now, to draw the unit circle, all that needs to be done is to enable the plot, using the [PlotsOn](plotson.html) command. This actually draws a 20-gon, rather than a circle, but the difference is imperceptible even on large circles.

The rest of the code is necessary to preserve the graph screen as the window changes and Plot1 is enabled and disabled (which causes the screen to be cleared), using [StorePic](storepic.html) and [RecallPic](recallpic.html). Optionally, you can also preserve the window dimensions, using [ZoomSto](zoomsto.html) and [ZoomRcl](zoomrcl.html) — this is useful if your program mixes pixel and point commands.

The routine uses three fairly large variables to do its work: ∟X, ∟Y, and Pic1. ∟X and ∟Y need to be preserved from the setup code to whenever the routine is called; Pic1 is only used temporarily. It's a good idea to [clean up](cleanup.html) all three by [deleting](delvar.html) them at the end of the program.
