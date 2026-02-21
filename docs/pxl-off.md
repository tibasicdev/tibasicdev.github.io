![The Pxl-Off( Command](pxl-off/PXL-OFF.GIF "The Pxl-Off( Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Turns off a pixel on the graph screen.|Pxl-Off(*row*,*column*)|TI-83/84/+/SE|1 byte|

### Menu Location
While editing a program press:
1. 2nd PRGM to enter the DRAW menu
2. RIGHT to enter the POINTS menu
3. 5 to choose Pxl-Off(, or use arrows
       
# The Pxl-Off( Command

The Pxl-Off( command is used to turn off the pixel at the given (Y,X) coordinates. Please note that the coordinates are switched around so that the row comes first and then the column — it's (Y,X) instead of (X,Y) like the [Pt-Off(](pt-off.html) command. Also note that the (0,0) point is the upper left corner of the Graph screen.

In addition to being easier to use because it is not affected by the window settings (meaning you don't have to set them when using the command), Pxl-Off( is faster than its equivalent Pt-Off( command, so it should generally be used instead whenever possible.

## Error Conditions

- **[ERR:DOMAIN](errors.html#domain)** is triggered if the coordinates are not whole numbers or not in the right range ([0..62] for row, [0..94] for column). These bounds are also affected by split screen mode.

## Related Commands

- [Pxl-On(](pxl-on.html)
- [Pxl-Change(](pxl-change.html)
- [pxl-Test(](pxl-test.html)
- [Pt-Off(](pt-off.html)
