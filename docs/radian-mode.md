![The Radian Command](radian-mode/RADIAN.GIF "The Radian Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Puts the calculator in Radian mode.|Radian|TI-83/84/+/SE/CE|1 byte|

### Menu Location
While editing a program, press:
1. MODE to access the mode menu.
2. Use arrows and ENTER to select Radian.
       
# The Radian Command

The Radian command puts the calculator into Radian mode, where the inputs and/or outputs to trig functions are assumed to be radian angles.

Angles measured in radians range from 0 to 2[π](pi.html). They are defined as the arc length of the arc, on a unit circle (circle with radius 1), that corresponds to the angle when it is placed in the center. This definition actually only differs from [degree](degree-mode.html) measurements by a constant factor.

To convert from a degree angle to a radian angle, multiply by 180/π. To go the other way, and get a radian angle from a degree angle, multiply by π/180.

The following commands are affected by whether the calculator is in Radian or [Degree](degree-mode.html) mode:

The input is differently interpreted:
- [P►Rx(](p-rx.html), [P►Ry(](p-ry.html)
- [sin(](sin.html), [cos(](cos.html), [tan(](tan.html)

The output is differently expressed:
- [angle(](angle.html)
- [R►Pθ(](r-ptheta.html)
- [sinֿ¹(](arcsin.html), [cosֿ¹(](arccos.html), [tanֿ¹(](arctan.html)
- [►Polar](polar-display.html) (and complex numbers when in [re^θi](re-thetai.html) mode)
- <sup>[r](radian-symbol.html)</sup>, [°](degree-symbol.html)

However, some commands are notably unaffected by angle mode, even though they involve angles, and this may cause confusion. This happens with the [SinReg](sinreg.html) command, which assumes that the calculator is in Radian mode even when it's not. As a result, the regression model it generates will graph incorrectly in Degree mode.

Also, complex numbers in polar form are an endless source of confusion. The angle( command, as well as the polar display format, are affected by angle mode. However, complex exponentials (see the [e^(](e-exponent.html) command), defined as $e^{i\theta}=\cos\theta+i\sin\theta$, are evaluated as though in Radian mode, regardless of the angle mode. This gives mysterious results like the following:
```
Degree:re^θi
		Done
e^(πi)
		1e^(180i)
Ans=e^(180i)
		0 (false)
```

Overall, it's better to put your calculator in Radian mode when dealing with polar form of complex numbers, especially since no mathematician would ever use degrees for the purpose anyway.

## Optimization

It's sometimes beneficial to use the <sup>[r](radian-symbol.html)</sup> command instead of switching to Radian mode. The <sup>r</sup> symbol will make sure a number is interpreted as a radian angle, even in degree mode, so that, for example:

```
Degree
..................[[/span]]Done
sin(π)
..................[[/span]].0548036651
sin(π<sup>r</sup>)
..................[[/span]]0
```


This is smaller when only one trig calculation needs to be done. Also, it doesn't change the user's settings, which are good to preserve whenever possible.

## Related Commands

- [Degree](degree-mode.html)
- <sup>[r](radian-symbol.html)</sup>
- [°](degree-symbol.html)
