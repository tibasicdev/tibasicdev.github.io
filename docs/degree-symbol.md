![The ° (Degree Symbol) Command](degree-symbol/DEGREE%20(SYMBOL).GIF "The ° (Degree Symbol) Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|If the calculator is in radian mode, the ° (degree) symbol converts an angle to radians.|*angle*°|TI-83/84/+/SE|1 byte|

### Menu Location
Press:
1. [2nd]
1. [Angle]
1. [Enter] or [1]
       
# The ° (Degree Symbol) Command

Normally, when the calculator is in radian mode, the trigonometric functions only return values calculated  in radians. With the ° symbol you can have the angle evaluated as if in degree mode because it converts the angle into radians.

You can insert the degree symbol by pressing [2ND] [ANGLE] [ENTER].

One full rotation around a circle is 2π radians, which is equal to 360°. To convert an angle in radians to degrees you multiply by 180/π, and to convert from degrees to radians multiply by π/180.

In radian mode:
```
sin(45)		\\ actually calculating sin(2578.31)
	.8509035245
sin(45°)
	.7071067812
```

In degree mode:

```
sin(45)
	.7071067812
sin(45°)
	.7071067812	\\ There's no difference when in degrees
```

## Converting Degrees, Minutes & Seconds

The degree symbol also allows you to convert degrees, minutes and seconds into decimal degrees. For example:

```
90°30'
       90.5
90°30'09"
       90.5025
```

The minute symbol is inserted by pressing [2ND] [ANGLE] [2]. The seconds symbol is inserted via [ALPHA] [+].

To convert back the other way (decimal to degrees-minutes-seconds) use the [`►DMS`](dms.html) command, accessed via [2ND] [ANGLE] [4]:

```
90.5025►DMS
       90°30'09"
```

## Optimization

When you only call the trig function once in a program and want it calculated in degrees, instead of changing the mode you can just use ° to save one-byte (the newline from using the command Degree)

```
:Degree
:sin(X)
can be
:sin(X°)
```

## Related Commands

- <sup>[r](radian-symbol.html)</sup> (radian symbol)
- [►DMS](dms.html)
