![The sinֿ¹( Command](arcsin/SININVERSE.GIF "The sinֿ¹( Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Returns the inverse sine (also called arcsine)|sinֿ¹(*number*)|TI-83/84/+/SE|1 byte|

### Menu Location
Press:<br># [2nd]<br># [sinֿ¹]
# The sinֿ¹( Command

sinֿ¹( returns the [arcsine](http://mathworld.wolfram.com/inversesine.html) of its argument. It is the inverse of [sin(](sin.html), which means that sinֿ¹(z) produces an angle θ such that sin(θ)=z.

Like sin(, the result of sinֿ¹( depends on whether the calculator is in [Radian](radian-mode.html) or [Degree](degree-mode.html) mode. However, unlike sine, the result is in degrees or radians, not the argument. A full rotation around a circle is 2π radians, which is equal to 360°. The conversion of θ=sinֿ¹(n) from radians to degrees is θ*180/π and from degrees to radians is θ*π/180. The sinֿ¹( command also works on lists.

The sinֿ¹( function can be defined for all real and complex numbers; however, the function assumes real values only in the closed interval [-1,1]. Because the trigonometric functions and their inverses in the Z80 calculators are restricted only to real values, the calculator will throw [ERR:DOMAIN](errors.html#domain) if the argument is outside of this interval, no matter what the mode setting may be.

In radians:
```
:sinֿ¹(1)
	1.570796327
```
In degrees:
```
:sinֿ¹(1)
	90
```

## Advanced Uses

Since the function sine itself doesn't have the restrictions that arcsine does, and since arcsine is the inverse of sine, you can use sinֿ¹(sin( to keep a variable within a certain range (most useful on the [graph screen](graphscreen.html)). Here is an example for a game like [pong](pong.html). The ball travels between -6 and 6.

You could use a flag like this:
```
:If 6=abs(X		\\ X is the position
:-D→D		\\ D is the direction
:X+D→X		\\ new position
:Pt-On(-54,X,"=")
```

An easier way to do this, without needing a flag or even an If statement, is using sinֿ¹(sin(
```
:X+1→X		\\ Note: the calculator is in degree mode
:Pt-On(-54,sinֿ¹(sin(15X))/15,"=")	\\ 15 is used because sinֿ¹ ranges from [-90,90]
										and X from [-6,6],  so 90/6=15
```

## Error Conditions

- **[ERR:DATA TYPE](errors.html#datatype)** is thrown if you input a complex value or a matrix.
- **[ERR:DOMAIN](errors.html#domain)** is thrown if you supplied an argument outside the interval [-1,1]

## Related Commands

- [sin(](sin.html)
- [cos(](cos.html)
- [cosֿ¹(](arccos.html)
- [tan(](tan.html)
- [tanֿ¹(](arctan.html)
