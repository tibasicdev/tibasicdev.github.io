![The vwAxes Command](vwaxes/VWAXES.GIF "The vwAxes Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Sets the v and w sequence equations to be graphed against each other.|vwAxes|TI-83/84/+/SE|2 bytes|

### Menu Location
When [Seq](http://tibasicdev.github.io/seq-mode) mode is enabled, press:<br># 2nd FORMAT to access the format menu.<br># Use arrows to select vwAxes.
# The vwAxes Command

When vwAxes is enabled, and the calculator is in [Seq](seq-mode.html) mode, the equations v and w will be graphed against each other (that is, the points (v(*n*),w(*n*)) are graphed for the values of *n* between *n*Min and *n*Max). With this setting, sequence mode graphs are a bit like [parametric](param.html) mode, except the parameter *n* is always an integer, and recursive definitions are possible.

The equation u is ignored when in vwAxes mode.

See "Related Commands" for other possibilities of graphing sequences.

## Error Conditions

- **[ERR:INVALID](errors.html#invalid)** is thrown if either v or w is undefined.

## Related Commands

- [Time](time.html)
- [Web](web.html)
- [uvAxes](uvaxes.html)
- [uwAxes](uwaxes.html)
