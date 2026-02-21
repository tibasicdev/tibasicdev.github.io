# Graphics Commands
We are dealing with a graphing calculator after all, so it makes sense that there are lots of graphics commands to talk about. Although the graphical capabilities of the calculator are limited (a monochrome LCD with either 160x100 or 240x128 resolution) these commands allow programmers to squeeze everything out of the screen that they can.

This page is divided into two sections: "Drawing commands" for general tasks like drawing lines, circles, or individual pixels, and "Graphing commands" which deal with the graphs of various functions. If you're not interested in the math aspects of graphics, you might want to skip the second section, especially at first reading.

However, all functions discussed on this page share a common aspect: their difference from normal graphing. When an [equation variable](68k:system-variables.html#equation) is graphed, the result is semi-permanent: using a command like [68k:ClrDraw](68k:clrdraw.html) to clear the screen, or changing some setting, can do nothing more than cause the graph to be redrawn. However, all of the commands on this page produce "drawn items" which disappear permanently when the screen is cleared. 

## Drawing Commands

If you want to draw an image on the screen, you have two choices. First, you can build it up from simple shapes like dots, circles and lines. This may work great for an user interface, but it pretty much limits you to stick figures when you want to draw anything more complicated. So the other option is to have a picture already stored in a variable, and just display it to the screen as you need to. We'll cover both of these in order.

A universally useful drawing command is [68k:ClrDraw](68k:clrdraw.html): this clears everything drawn on the graphscreen.

### Point vs. Pixel

TI-Basic allows two ways of specifying a location on the screen: "point" coordinates and "pixel" coordinates. The point coordinates are the ones that you see most often: they are the coordinates determined by the graphing window, with (xmin,ymin) being the bottom left corner and (xmax,ymax) the top right. Because the graphing window has to be initialized if you want to use these in a logical way, this is NOT usually the best type of coordinate to use.

The alternative is pixel coordinates ("pixel" refers to the individual dots that make up the calculator screen). The graphscreen is made up of 77 rows and 159 columns of pixels, and 103 rows and 239 columns on a widescreen calculator (this ignores the rightmost column of pixels, which can't be drawn to). So the pixel coordinates refer to each pixel by the pair (row,column). This is actually the reverse of the point coordinates: the first number determines the vertical location, and the second number the horizontal location. The rows and columns are numbered starting from 0, and the 0th row is the top row. So (0,0) refers to the top left pixel of the graphscreen, and (76,158) or (102,238) refers to the bottom right pixel.

For pretty much every drawing command, you have to specify a location on the graphscreen at which to draw. You can choose either type of coordinate (although your life will be simpler with pixel coordinates) — for every point command, there's a matching pixel command, and vice versa (with an exception we'll get to later).

For example, you can draw a line with the Line command, and the syntax will be:
```
Line x1,y1,x2,y2
```
Or you can use the PxlLine command, with the syntax:
```
PxlLine row1,col1,row2,col2
```

The following table gives you all the simple drawing commands in their two forms:

| Point Coordinates | Pixel Coordinates |
| --- | --- |
| [68k:Circle](68k:circle.html) | [68k:PxlCrcl](68k:pxlcrcl.html) |
| [68k:Line](68k:line.html) | [68k:PxlLine](68k:pxlline.html) |
| [68k:LineHorz](68k:linehorz.html) | [68k:PxlHorz](68k:pxlhorz.html) |
| [68k:LineVert](68k:linevert.html) | [68k:PxlVert](68k:pxlvert.html) |
| [68k:PtChg](68k:ptchg.html) | [68k:PxlChg](68k:pxlchg.html) |
| [68k:PtOff](68k:ptoff.html) | [68k:PxlOff](68k:pxloff.html) |
| [68k:PtOn](68k:pton.html) | [68k:PxlOn](68k:pxlon.html) |
| [68k:ptTest()](68k:pttest.html) | [68k:pxlTest()](68k:pxltest.html) |
| [68k:PtText](68k:pttext.html) | [68k:PxlText](68k:pxltext.html) |

### Sprites

Using picture variables, you can store a rectangular image of any size, to be displayed on the screen later. In video game language, such an image is often called a sprite. 

The several commands that deal with picture variables are covered in-depth in the [68k:Sprites](68k:sprites.html) article ([68k:CyclePic](68k:cyclepic.html) is described in the [68k:Animation](68k:animation.html) article because, you guessed it, it lets you display an animated image). One important thing to note is that they only use pixel coordinates — another reason to use these. 

The seven sprite commands are:
- [68k:AndPic](68k:andpic.html)
- [68k:CyclePic](68k:cyclepic.html)
- [68k:NewPic](68k:newpic.html)
- [68k:RclPic](68k:rclpic.html)
- [68k:RplcPic](68k:rplcpic.html)
- [68k:StoPic](68k:stopic.html)
- [68k:XorPic](68k:xorpic.html)

## Graphing Commands

The usual way of graphing is to store to an equation variable such as y1(x), and then simply go to the graph screen (where you can resize the window and other fun stuff). For the convenience of programmers, any sort of graph manipulation you can choose from a menu is also available as a command. The 68k calculators also provide another way of graphing, probably more suitable to programmers, which draws a graph of a specific expression.

### Graphing Expressions

These simulate graphing an equation from any graphing mode. Of special note is the [68k:Graph](68k:graph.html) command — unlike the other commands, which can be erased with [68k:ClrDraw](68k:clrdraw.html) or any other way of refreshing the screen, the output of Graph can only be erased by [68k:ClrGraph](68k:clrgraph.html) or by going to the Y= screen to re-enable the normal Y= functions.

- [68k:ClrGraph](68k:clrgraph.html)
- [68k:DrawFunc](68k:drawfunc.html)
- [68k:DrawInv](68k:drawinv.html)
- [68k:DrawParm](68k:drawparm.html)

- [68k:DrawPol](68k:drawpol.html)
- [68k:DrawSlp](68k:drawslp.html)
- [68k:DrwCtour](68k:drwctour.html)

- [68k:Graph](68k:graph.html)
- [68k:LineTan](68k:linetan.html)
- [68k:Shade](68k:shade.html)




### Zoom Commands

The zoom commands resize the graphing window determined by xmin, xmax, ymin, and ymax. For the most part, these four variables are all they change. The exception is [68k:ZoomStd](68k:zoomstd.html), which restores certain other values to their defaults, and [68k:ZoomSto](68k:zoomsto.html) and [68k:ZoomRcl](68k:zoomrcl.html), which back up and restore all [window variables](68k:system-variables.html#window).

- [68k:ZoomBox](68k:zoombox.html)
- [68k:ZoomData](68k:zoomdata.html)
- [68k:ZoomDec](68k:zoomdec.html)
- [68k:ZoomFit](68k:zoomfit.html)
- [68k:ZoomIn](68k:zoomin.html)

- [68k:ZoomInt](68k:zoomint.html)
- [68k:ZoomOut](68k:zoomout.html)
- [68k:ZoomPrev](68k:zoomprev.html)
- [68k:ZoomRcl](68k:zoomrcl.html)

- [68k:ZoomSqr](68k:zoomsqr.html)
- [68k:ZoomStd](68k:zoomstd.html)
- [68k:ZoomSto](68k:zoomsto.html)
- [68k:ZoomTrig](68k:zoomtrig.html)




### Graph Manipulation

These final commands are more or less miscellaneous. Their uniting characteristic is that they deal with the graph of an actual equation variable (the ones you edit in the Y= screen). Of these, [68k:FnOff](68k:fnoff.html) is probably the one to remember: it turns off all equation variables without actually deleting them.

- [68k:BldData](68k:blddata.html)
- [68k:FnOff](68k:fnoff.html)
- [68k:FnOn](68k:fnon.html)
- [68k:RclGDB](68k:rclgdb.html)
- [68k:StoGDB](68k:stogdb.html)
- [68k:Style](68k:style.html)
- [68k:Table](68k:table.html)
- [68k:Trace](68k:trace.html)
