![The ZInteger Command](zinteger/http://tibasicdev.wdfiles.com/local—files/zinteger/zoominteger_movie.gif width="200" "The ZInteger Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Zooms to a square window with all-integer coordinates.|ZInteger|TI-83/84/+/SE|1 byte|

### Menu Location
Press:<br># ZOOM to access the zoom menu.<br># 8 to select ZInteger, or use arrows and ENTER.
# The ZInteger Command

When ZInteger is chosen as a menu option outside a program, it asks for a point on the graph screen. This point's coordinates are rounded to the nearest integer point. Then the [window variables](system-variables.html#window) are changed so the window is centered at this point, and so that the coordinates of every pixel are integers. ΔX and ΔY, the distances between two pixels next to each other, are both 1.

The above process modifies Xmin, Xmax, Ymin, and Ymax. Xscl and Yscl are also modified: both are set to 10. No other variables are modified (unless you count ΔX and ΔY, which are affected as they are defined).

The ZInteger command (usable in a program only) has a slightly different effect: instead of allowing you to choose a point, it automatically uses the point that is the current center.

## Advanced Uses

A graph window commonly used in programming can be created by using the [ZStandard](zstandard.html) and ZInteger commands:
```
:ZStandard
:ZInteger
```

## Error Conditions

- **[ERR:INVALID](errors.html#invalid)** occurs if this command is used outside a program.

## Related Commands

- [ZDecimal](zdecimal.html)
- [ZStandard](zstandard.html)
- [ZSquare](zsquare.html)

## See Also

- [Friendly Graphing Windows](friendly-window.html)
