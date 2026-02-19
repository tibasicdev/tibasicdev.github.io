# Decimal To Fraction (alternative)
------

|Routine Summary|Inputs|Outputs|Variables Used|Author|
|--- |--- |--- |--- |--- |
|Converts a decimal into a fraction|*Ans* - Decimal input|*Ans* - Numerator (1), Denominator (2)|A, B, Ans|12Me21|

```
:Ans→A:1→B
:While fPart(A
:10A→A:10B→B
:End
:{A,B}/gcd(abs(A),B
```

It starts by setting up a fraction with the input as the numerator and 1 as the denominator. After that, it multiplies both by 10 until the numerator is an integer, and then simplifies the fraction.

## Error Conditions

- **[ERR:DATA TYPE](errors.html#datatype)** is thrown if Ans is an imaginary or complex number
- **[ERR:DOMAIN](errors.html#reserved)** is thrown if Ans has more than 11 digits after the decimal.

## Related Routines

- [Decimal to Fraction ](decimal-to-fraction.html)
