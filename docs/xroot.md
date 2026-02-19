![The ×√ Command](xroot/XROOT.GIF "The ×√ Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Takes the *x*th root of an input.|*A* <sup>x</sup>√ *B*|TI-83/84/+/SE|1 byte|

### Menu Location
While editing a program, press:<br># MATH to open the [math](math.html) menu<br># 5 or use the arrow keys to select
# The ×√ Command

This command takes the *x*th root of a number.  If used on a list, it will return a list with the *x*th root of each element.  Also valid are the forms *list*<sup>×</sup>√*x* and *list1*<sup>×</sup>√*list2*.

```
:2×√4
		2
:5×√2
		1.148698355

:3×√{1,‾8,27}
		{1 ‾2 3}
		
:{3,2}×√{8,9}
		{2 3}
		
Real mode:
:4×√‾1
	<returns error>

a+bi mode:
:4×√‾1
		.7071067812+.7071067812i
```

See the notes on the [^](power.html) command for an explanation on how <sup>×</sup>√ behaves depending on whether its input is real or complex.

## Optimization

If you want to take the second or third root of a number, use [√(](square-root.html) or [³√(](cube-root.html) instead.

```
:2×√X
can be
:√(X
```

## Error Conditions

- **[ERR:NONREAL ANS](errors.html#N)** if you try to take an even root of a negative number or list element in Real mode.

## Related Commands

- [√(](square-root.html)
- [³√(](cube-root.html)
- [^](power.html)
