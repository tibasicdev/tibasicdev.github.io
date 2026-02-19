![The uwAxes Command](uwaxes/UWAXES.GIF "The uwAxes Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Sets the u and w sequence equations to be graphed against each other.|uwAxes|TI-83/84/+/SE|2 bytes|

### Menu Location
When [Seq](http://tibasicdev.github.io/seq-mode) mode is enabled, press:<br># 2nd FORMAT to access the format menu.<br># Use arrows to select uwAxes.
# The uwAxes Command

When uwAxes is enabled, and the calculator is in [Seq](seq-mode.html) mode, the equations u and w will be graphed against each other (that is, the points (u(*n*),w(*n*)) are graphed for the values of *n* between *n*Min and *n*Max). With this setting, sequence mode graphs are a bit like [parametric](param.html) mode, except the parameter *n* is always an integer, and recursive definitions are possible.

The equation v is ignored when in uwAxes mode.

See "Related Commands" for other possibilities of graphing sequences.

## Error Conditions

- **[ERR:INVALID](errors.html#invalid)** is thrown if either u or w is undefined.

## Related Commands

- [Time](time.html)
- [Web](web.html)
- [uvAxes](uvaxes.html)
- [vwAxes](vwaxes.html)
