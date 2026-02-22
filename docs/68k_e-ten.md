![The EE Command](68k_e-ten/E.png "The EE Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|The E symbol is used for entering numbers in scientific notation.|*mantissa* E *exponent*|This command works on all calculators.|1 byte|
       
### Menu Location
Press [2nd][EE] to paste the E command.
       
# The EE Command

The `E` symbol is used for entering numbers in scientific notation: it's short for *10^. Like TI-83 Basic, the exponent of `E` must be a constant integer, however unlike TiBz80 the range of values is not finite.

The `E` symbol is used in display by the calculator for approximations of very small numbers, or when in [`Sci`](sci.html) (scientific) or [`Eng`](eng.html) (engineering) mode. Interestingly, the calculator will opt to display large numbers without approximation, but it will only solve for a maximum of 12 decimal places before rounding or using `E`.

Unlike the exponent of `E`, the mantissa (a special term for the A in A*10^B, in scientific notation) isn't limited to constants alone: it can be a real or complex variable or expression, a list, a matrix, or even omitted entirely (and then it will be assumed to equal 1). The reason for this versatility is simple: internally, only the exponent is taken to be an actual argument for this command. The rest of the calculation is done through implied multiplication.

```
5E3
                  5000
E‾5
                  .00001
```

## Optimization

Don't add the mantissa when it's 1: 

```
1E5
could be
E5
```

In addition, `E`2 or `E`3 can be used as shorthand ways of writing 100 and 1000 respectively. This could be continued, in theory, for higher powers of 10, but those aren't necessary as often.

## Related Commands

- [`^`](power.html)
- [`e^(`](e-exponent.html)
