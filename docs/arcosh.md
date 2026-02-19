![The coshֿ¹( Command](arcosh/COSHINVERSE.GIF "The coshֿ¹( Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Calculates the inverse hyperbolic cosine of a value.|coshֿ¹(*value*)|TI-83/84/+/SE|1 byte|

### Menu Location
The coshֿ¹( command can only be found in the catalog. Press:
1. 2nd CATALOG to access the command catalog.
1. C to skip to commands starting with C.
1. Scroll down and select coshֿ¹(
       
# The coshֿ¹( Command

The `coshֿ¹(` function gives the inverse hyperbolic cosine of a value. `coshֿ¹(x)` is the number y such that x = `cosh(y)`.

Although `coshֿ¹(x)` can be defined for all real and complex numbers, it assumes real values only for x≥1. Since hyperbolic functions in the Z80 calculators are restricted only to real values, [ERR:DOMAIN](errors.html#domain) is thrown when x<1.

The `coshֿ¹(` command also works for lists.

```
coshֿ¹(1)
	0
coshֿ¹({2,3})
	{1.316957897 1.762747174}
```

## Error Conditions

- **[ERR:DOMAIN](errors.html#domain)** when taking the inverse cosh of a number less than 1.

## Related Commands

- [`sinh(`](sinh.html)
- [`sinhֿ¹(`](arsinh.html)
- [`cosh(`](cosh.html)
- [`tanh(`](tanh.html)
- [`tanhֿ¹(`](artanh.html)
