![The R►Pθ( Command](r-ptheta/RTOPTHETA.GIF "The R►Pθ( Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|R►Pθ( calculates the angle coordinate (in polar coordinates) given the Cartesian coordinates.|R►Pθ(*x*,*y*)|TI-83/84/+/SE|1 byte|

### Menu Location
Press:
1. 2nd ANGLE to access the angle menu.
2. 6 to select R►Pθ(, or use arrows and ENTER.
       
# The R►Pθ( Command

R►Pθ( (Rectangular to polar θ) takes the (*x*,*y*) (Cartesian) coordinate, and returns the angle that the ray  from (0,0) to (*x*,*y*) makes with the positive x-axis. This is the θ-coordinate of the same point in (*r*,*θ*) (polar) mode. The identity used for this conversion is tan(*θ*)=*y**/x*, with the correct inverse being chosen depending on the quadrant that the point is in. The range of the angle returned is -π<*θ*≤π. R►Pθ( can also be used on lists.

R►Pθ( is equivalent to the atan2() instruction seen in C/++ and FORTRAN.

```
R►Pθ(3,4)
	.927295218
tanֿ¹(4/3)
	.927295218
R►Pθ(0,{1,-1})
	{1.570796327, -1.57096327}
```

R►Pθ( is affected by [Degree](degree-mode.html) and [Radian](radian-mode.html) mode in its output, which is an angle measured in degrees or radians respectively.

## Advanced Uses

If you want the result to always be a radian angle, regardless of mode settings, you can divide the result by 1<sup>[r](radian-symbol.html)</sup>:
```
R►Pθ(x,y)/1^^r
```

If you want the result to always be a degree angle, regardless of mode settings, you can divide the result by 1[°](degree-symbol.html):
```
R►Pθ(x,y)/1°
```

## Error Conditions

- **[ERR:DATA TYPE](errors.html#datatype)** is thrown if you input a complex argument.
- **[ERR:DIM MISMATCH](errors.html#dimmismatch)** is thrown if two list arguments have different dimensions.

## Related Commands

- [P►Rx(](p-rx.html)
- [P►Ry(](p-ry.html)
- [R►Pr(](r-pr.html)
- [angle(](angle.html)
- [tanֿ¹(](tan-¹.html)
