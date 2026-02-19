![The ►Frac Command](frac/FRAC.GIF "The ►Frac Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Displays the fractional value of a number|*Decimal*►Frac|TI-83/84/+/SE/CE|1 byte|

### Menu Location
While editing a program, press:
1. MATH to open the [math](math.html) menu
1. ENTER or 1 to select.
       
# The ►Frac Command

`►Frac` attempts to display the input in fraction form.  It only works on the [home screen](homescreen.html) outside a program, or with the [`Disp`](disp.html) and [`Pause`](pause.html) commands in a program. It takes up to 12 decimal places of a non-terminating decimal to find the corresponding fraction. The decimal input is returned if `►Frac` fails to find the fraction form.

For a more versatile algorithm for finding fractions, see the [Decimal to Fraction](decimal-to-fraction.html) routine.

```
.333►Frac
		.333
.333333333333►Frac
		 1/3
```

## Related Commands

- [`►Dec`](-dec.html)

## See Also

- [Decimal to Fraction](decimal-to-fraction.html)
