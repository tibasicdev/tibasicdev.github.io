![The ZoomFit Command](zoomfit/http://tibasicdev.github.io/local—files/zoomfit/ZoomFit_Example.gif "The ZoomFit Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Zooms to a graphing window that works for the currently graphed equations.|ZoomFit|TI-83/84/+/SE|2 bytes|

### Menu Location
Press:<br># ZOOM to access the zoom menu.<br># 0 to select ZoomFit, or use arrows and ENTER.
# The ZoomFit Command

The ZoomFit zooms to the smallest window that contains all points of the currently graphed equations. In [Func](func.html) mode, this means that it calculates the minimum and maximum Y-value for the current Xmin to Xmax range, and sets Ymin and Ymax to those values (Xmin and Xmax remain unchanged). In other graphing modes, this process is done for both X and Y over the range of T, θ, or *n*.

## Optimization

When graphing an equation with ZoomFit, the calculator will first calculate all points to find the minimum and maximum, then calculate all the points again to graph it. This can be time consuming if the equation is very complicated, and in that case doing part of the process manually might be faster if you reuse the points.

## Error Conditions

- **[ERR:INVALID](errors.html#invalid)** is thrown if this command is using outside a program (although the menu option, of course, is fine).
- **[ERR:WINDOW RANGE](errors.html#windowrange)** is thrown when the window ends up being empty (if the function is constant, for example)

## Related Commands

- [ZoomStat](zoomstat.html)
- [ZBox](zbox.html)
