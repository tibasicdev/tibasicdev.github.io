![The tanֿ¹( Command](arctan/TANINVERSE.GIF "The tanֿ¹( Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Returns the inverse tangent (also called arctangent)|tanֿ¹(*number*)|TI-83/84/+/SE|1 byte|

### Menu Location
Press:
1. [2nd]
1. [tanֿ¹]
       
# The tanֿ¹( Command

tanֿ¹( returns the [arctangent](http://mathworld.wolfram.com/inversetangent.html) of its argument. It is the inverse of [tan(](tan.html), which means that tanֿ¹(n) produces an angle θ such that tan(θ)=n.

Like tan(, the result of tanֿ¹( depends on whether the calculator is in [Radian](radian-mode.html) or [Degree](degree-mode.html) mode. However, unlike tangent, the result is in degrees or radians, not the argument. A full rotation around a circle is 2π radians, which is equal to 360°. The conversion of θ=tanֿ¹(n) from radians to degrees is θ*180/π and from degrees to radians is θ*π/180. The tanֿ¹( command also works on a list.

tanֿ¹( will always return a value between -π/2 and π/2 (or -90° and 90°).

In radians:
```
:tanֿ¹(1)
    .7853981634
```
In degrees:
```
:tanֿ¹(1)
    45
```

## Optimization

Expressions of the form tanֿ¹(*y**/x*) are usually better recast as R►Pθ(*x*,*y*); the latter will not fail even if *x* should happen to be equal to zero.

## Error Conditions

- **[ERR:DATA TYPE](errors.html#datatype)** is thrown if you input a complex value or a matrix.

## Related Commands

- [sin(](sin.html)
- [sinֿ¹(](arcsin.html)
- [cos(](cos.html)
- [cosֿ¹(](arccos.html)
- [tan(](tan.html)
- [R►Pθ(](r-ptheta.html)
