![The imag( Command](imag/IMAG.GIF "The imag( Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Returns the imaginary part of a complex number.|imag(*value*)|TI-83/84/+/SE|2 bytes|

### Menu Location
Press:
1. MATH to access the [math](math.html) menu.
1. RIGHT, RIGHT to access the CPX (complex) submenu.
1. 3 to select imag(, or use arrows.
       
# The imag( Command

`imag(z)` returns the imaginary part of the complex number *z*. If *z* is represented as *x*+i*y* where *x* and *y* are both real, `imag(z)` returns *y*. Also works on a list of complex numbers.
```
imag(3+4i)
     4

imag({3+4i,-2i,17})
     {4,-2,0}
```

## Related Commands

- [`real(`](real-func.html)
- [`abs(`](abs.html)
- [`angle(`](angle.html)
- [`conj(`](conj.html)
