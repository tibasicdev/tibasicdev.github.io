![The ►Polar Command](polar-display/POLAR.GIF "The ►Polar Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Formats a complex value in polar form when displaying it.|*value*►Polar|TI-83/84/+/SE|2 bytes|

### Menu Location
Press:<br># MATH to access the math menu.<br># RIGHT RIGHT to access the CPX submenu.<br># 7 to select ►Polar, or use arrows and ENTER.
# The ►Polar Command

The ►Polar command can be used when displaying a complex number on the home screen, or with the [Disp](disp.html) and [Pause](pause.html) commands. It will then format the number as though [re^θi](re-thetai.html) mode were enabled. It also works with lists.

```
i
	i
i►Polar
	1e^(1.570796327i)
{1,i}►Polar
	{1 1e^(1.570796327i)}
```

It will also work when displaying a number by putting it on the last line of a program by itself. It does **not** work with [Output(](output.html), [Text(](text.html), or any other more complicated display commands.

To actually separate a number into the components of polar form, use [abs(](abs.html) and [angle(](angle.html).

## Error Conditions

- **[ERR:SYNTAX](errors.html#syntax)** is thrown if the command is used somewhere other than the allowed display commands.
- **[ERR:DATA TYPE](errors.html#datatype)** is thrown if the value is real.

## Related Commands

- [►Frac](-frac.html)
- [►Dec](-dec.html)
- [►Rect](-rect.html)
