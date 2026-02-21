![The Zoom In Command](zoom-in/ZOOMIN.GIF width="192" height="128" style="border: 1px solid black;" "The Zoom In Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Zooms to a smaller graphing window with the same centre.|Zoom In|TI-83/84/+/SE|1 byte|

### Menu Location
Press:
1. ZOOM to access the zoom menu.
2. 2 to select Zoom In, or use arrows and ENTER.
       
# The Zoom In Command

Outside a program, the Zoom In tool allows you to pick a point on the graph screen and change the graphing window to a smaller one centered at that point. The Zoom In command, used in a program, also changes the graphing window to a smaller one, but doesn't let you pick a point — it uses the center of the screen.

The variables [XFact](system-variables.html#window) and [YFact](system-variables.html#window) are used to determine how much the graphing window changes: the total width of the screen, Xmax-Xmin, is divided by XFact, and the total height, Ymax-Ymin, is divided by YFact. Because you can't store a value less than 1 to either of these variables, the screen is guaranteed to get no larger.

Aside from Xmin, Xmax, Ymin, and Ymax, no window variables are modified by this command (although ΔX and ΔY change [as they are defined](system-variables.html#window)).

## Error Conditions

- **[ERR:INVALID](errors.html#invalid)** occurs if this command is used outside a program.
- **[ERR:WINDOW RANGE](errors.html#windowrange)** is thrown if the window is zoomed in beyond the level of the calculator's precision.

## Related Commands

- [Zoom Out](zoom-out.html)
- [ZBox](zbox.html)
