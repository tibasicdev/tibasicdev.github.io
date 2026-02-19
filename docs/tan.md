![The tan( Command](tan/TAN.GIF "The tan( Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Returns the tangent of a real number.|tan(*angle*)|TI-83/84/+/SE|1 byte|

### Menu Location
Press TAN
# The tan( Command

tan(θ) calculates the [tangent](http://mathworld.wolfram.com/tangent.html) of the angle θ, which is defined by $\tan \theta=\frac{\sin \theta}{\cos \theta}$

The value returned depends on whether the calculator is in [Radian](radian-mode.html) or [Degree](degree-mode.html) mode.  A full rotation around a circle is 2π radians, which is equal to 360°. The conversion from radians to degrees is angle*180/π and from degrees to radians is angle*π/180. The tan( command also works on a list of real numbers.

Since tangent is defined as the quotient of sine divided by cosine, it is undefined for any angle such that cos(θ)=0.

In radians:
```
tan(π/4)
    1
```

In degrees:
```
tan(45)
    1
```


## Advanced Uses

You can bypass the mode setting by using the [°](degree-symbol.html) (degree) and <sup>[r](radian-symbol.html)</sup> (radian) symbols. These next two commands will return the same values no matter if your calculator is in degrees or radians:

```
tan(45°)
    1
```
```
tan(π/4¹ )
    1
```

## Error Conditions

- **[ERR:DATA TYPE](errors.html#datatype)** is thrown if you supply a matrix or a complex argument.
- **[ERR:DOMAIN](errors.html#domain)** is thrown if you supply an angle of π/2±nπ (in radians, where n is an integer) or 90±180n (in degrees, where n is an integer), or when the input is ≥1E12.


## Related Commands

- [sin(](sin.html)
- [sinֿ¹(](arcsin.html)
- [cos(](cos.html)
- [cosֿ¹(](arccos.html)
- [tanֿ¹(](arctan.html)
