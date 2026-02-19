![The Zoom Out Command](zoom-out/ZOOMOUT.GIF width="192" height="128" style="border: 1px solid black;" "The Zoom Out Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Zooms to a larger graphing window with the same center.|Zoom Out|TI-83/84/+/SE|1 byte|

### Menu Location
Press:
1. ZOOM to access the zoom menu.
1. 3 to select Zoom Out, or use arrows and ENTER.
       
# The Zoom Out Command

Outside a program, the Zoom Out tool allows you to pick a point on the graph screen and change the graphing window to a larger one centered at that point. The Zoom Out command, used in a program, also changes the graphing window to a larger one, but doesn't let you pick a point — it uses the center of the screen.

The variables [XFact](system-variables.html#window) and [YFact](system-variables.html#window) are used to determine how much the graphing window changes: the total width of the screen, Xmax-Xmin, is multiplied by XFact, and the total height, Ymax-Ymin, is multiplied by YFact. Because you can't store a value less than 1 to either of these variables, the screen is guaranteed to get no smaller.

Aside from Xmin, Xmax, Ymin, and Ymax, no window variables are modified by this command (although ΔX and ΔY change [as they are defined](system-variables.html#window)).

## Error Conditions

- **[ERR:INVALID](errors.html#invalid)** occurs if this command is used outside a program.
- **[ERR:ZOOM](errors.html#zoom)** is thrown if an overflow occurs calculating the new window dimensions (the window is too big)

## Related Commands

- [Zoom In](zoom-in.html)
- [ZBox](zbox.html)
