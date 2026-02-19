![The Pxl-On( Command](pxl-on/PXL-ON.GIF "The Pxl-On( Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Turns on a pixel on the graph screen.|Pxl-On(*row*,*column*)|TI-83/84/+/SE|1 byte|

### Menu Location
While editing a program press:<br># 2nd PRGM to enter the DRAW menu<br># RIGHT to enter the POINTS menu<br># 4 to choose Pxl-On(, or use arrows
# The Pxl-On( Command

The Pxl-On( command is used to turn on the pixel at the given (Y,X) coordinates. Please note that the coordinates are switched around so that the row comes first and then the column — it's (Y,X) unlike the (X,Y) of the [Pt-On(](pt-on.html) command. Also note that the (0,0) point is the upper left corner of the Graph screen.

In addition to being easier to use because it is not affected by the window settings (meaning you don't have to set them when using the command), Pxl-On( is faster than its equivalent Pt-On( command, so it should generally be used instead whenever possible.

## Error Conditions

- **[ERR:DOMAIN](errors.html#domain)** is triggered if the coordinates are not whole numbers or not in the right range ([0..62] for row, [0..94] for column). These bounds are also affected by split screen mode.

## Related Commands

- [Pxl-Off(](pxl-off.html)
- [Pxl-Change(](pxl-change.html)
- [pxl-Test(](pxl-test.html)
- [Pt-On(](pt-on.html)
