![The ^ Command](power/POWER.GIF "The ^ Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Raises a number to a power.|*x*^*y*|TI-83/84/+/SE|1 byte|

### Menu Location
Press [^]
# The ^ Command

The ^ operator is used to raise a number to a power. It can be used with numbers, expressions, and lists. It can be used for taking nonnegative integer powers of square matrices (up to the 255th power only, however), but not for negative powers (use [ֿ¹](inverse.html) instead) or matrix exponentials (which the TI-83+ cannot do).

In general, *x*^*y* returns the same results as *e*^(*y**ln(*x*)). For expressions of the form *x*^(*p**/q*), where *p* and *q* are integers and *q* is an odd number, the principal branch is returned if *x* is complex, but the real branch is returned if *x* is a negative real number.

```
(-1)^(1/3)
		-1
(-1+0i)^(1/3)
		.5+.8660254038i
```

## Optimization

When raising 10 or *[e](e-value.html)* to a power, use the [10^(](ten-exponent.html) and *[e^(](e-exponent.html)* commands instead. Similarly, use the [²](2.html), [³](3.html), or [ֿ¹](inverse.html) commands for raising a number to the 2, 3, or -1 power.

## Error Conditions

- **[ERR:DOMAIN](errors.html#domain)** is thrown when calculating 0^0, or raising 0 to a negative power.
- **[ERR:NONREAL ANS](errors.html#nonrealans)** is thrown in [Real](real-mode.html) mode if the result is complex (and the operands are real)

## Related Commands

- [*](multiply.html), [/](divide.html), [×√](xroot.html)
- [10^(](ten-exponent.html), *[e^(](e-exponent.html)*
