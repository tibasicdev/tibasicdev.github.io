![The i Command](i/I.PNG "The i Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|The mathematical symbol *i*, short for √(-1).|*i*<br><br>To enter a complex number:<br><br>*real-part*+*imag-part i*|TI-83/84/+/SE/CSE/CE|1 byte|

### Menu Location
Press 2nd *i* to paste *i*.
# The i Command

The *i* symbol is short for √(-1), and is used for complex numbers in algebra and complex analysis. On the calculator, entering *i* will not cause an error, even in [Real](real-mode.html) mode, but operations that result in a complex number (such as taking the square root of a negative number) will. If you're dealing with complex numbers, then, it's best to switch to [a+bi](a-bi.html) or [re^θi](re-thetai.html) mode.

## Advanced Uses

By using *i* in a calculation, the calculator switches to complex number mode to do it, even if in [Real](real-mode.html) mode. So √(-1) will throw an [ERR:NONREAL ANS](errors.html#nonrealans), but √(0*i*-1) will not (even though it's the same number). This can be used to force calculations to be done using complex numbers regardless of the mode setting — usually by adding or subtracting 0*i*, although more clever ways can be found. 

A good example of this technique is our [Quadratic Formula](quadratic-formula.html) routine.

## Related Commands

- [π](pi.html)
- *[e](e.html)*
- [Real](real-mode.html), [a+bi](a-bi.html), and [re^θi](re-thetai.html)

## See Also

- [Quadratic Formula](quadratic-formula.html)
