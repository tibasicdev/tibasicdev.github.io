![The a+bi Command](a-bi/APLUSBI.GIF "The a+bi Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Puts the calculator into a+b*i* mode.|a+b*i*|TI-83/84/+/SE|1 byte|

### Menu Location
Press:
1. MODE to access the mode menu.
1. Use the arrow keys and ENTER to select a+b*i*
       
# The a+bi Command

The `a+b*i*` command puts the calculator into rectangular complex number mode. This means that:
- Taking square roots of negative numbers, and similar operations, no longer returns an error.
- Complex results are displayed in the form `a+b*i*` (hence the name of the command)

This is the standard way of displaying complex numbers, though they can also be displayed in polar form (see [`re^θi`](re-thetai.html) for more details). To extract the coefficients a and b, use the [`real(`](real-func.html) and [`imag(`](imag.html) commands.

## Advanced Uses

Rather than switch to a+b*i* mode, you might want to force the calculations to use complex numbers by making the original argument complex. The general way to do this is by adding +0*i* to the number. However, there may be an optimization in any particular case. See the [quadratic formula](quadratic-formula.html) routine for a good example of this.

```
Real
		Done
√(-1)	
		(causes an error)
√(-1+0i)		
		i
```

## Related Commands

- [`Real`](real-mode.html)
- [`re^θi`](re-thetai.html)

## See Also

- [Quadratic Formula](quadratic-formula.html)
