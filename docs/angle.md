![The angle( Command](angle/ANGLE.GIF "The angle( Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Returns the complex argument of a complex number.|angle(*z*)|TI-83/84/+/SE/CSE/CE|2 bytes|

### Menu Location
Press:
1. MATH to access the [math](math.html) menu.
1. RIGHT, RIGHT to access the CPX (complex) submenu
1. 4 to select angle(, or use arrows.
       
# The angle( Command

`angle(z)` returns the [complex argument](http://mathworld.wolfram.com/complexargument.html) (also known as the polar angle) of the complex number *z*. If *z* is represented as *x*+i*y* where *x* and *y* are both real, `angle(z)` returns R►Pθ(*x*,*y*) (which is equivalent to tanֿ¹(*y**/x*) if x is nonzero). Also works on a list of complex numbers.
```
angle(3+4i)
     .927295218
R►Pθ(3,4)
     .927295218
```

When writing a complex number *z* in the form $re^{i\theta}$ (or, equivalently, $r(\cos\theta+i\sin\theta)$), then $\theta$ is equal to the value of `angle(z)`, suitably reduced so that the result returned is in the interval $-\pi<\theta\leq\pi$.

The `angle(` command also works on [matrices](matrices.html), though not in any useful way: `angle(`[A] will return a matrix of the same size as [A], but with all elements 0. If you plan to use this, **don't**: 0[A] does the same thing, but is smaller and not as questionable (because this behavior is clearly unintentional on TI's part, and may be changed in an OS update).

## Related Commands

- [`abs(`](abs.html)
- [`conj(`](conj.html)
- [`real(`](real-func.html)
- [`imag(`](imag.html)
- [`R►Pθ(`](r-ptheta.html)
