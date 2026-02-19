![The ZBox Command](zbox/ZBOX.GIF "The ZBox Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Zooms in to a smaller graphing window defined by a box drawn by the user.|ZBox|TI-83/84/+/SE|1 byte|

### Menu Location
Press:<br># ZOOM to access the zoom menu.<br># ENTER to select ZBox.
# The ZBox Command

The ZBox command allows the user to select a smaller window within the current graphing window to zoom in to. To select the window, use the arrow keys and ENTER to select one corner of the window; then as you use the arrow keys and ENTER to select the other corner, a rectangle of the window's dimensions will be shown.

It's not recommended to use this in most programs, because entering an empty window (with no width or no height) will cause an error and exit the program without letting it clean up.


## Error Conditions

- **[ERR:INVALID](errors.html#invalid)** occurs if this command is used outside a program.
- **[ERR:ZOOM](errors.html#zoom)** is thrown if an empty window is selected (with no width or no height)

## Related Commands

- [Zoom In](zoom-in.html)
- [Zoom Out](zoom-out.html)
