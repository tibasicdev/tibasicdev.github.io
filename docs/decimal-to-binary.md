# Decimal to Base B
|Routine Summary|Inputs|Outputs|Author|
|--- |--- |--- |--- |
|Converts a decimal (base 10) number to a number in any other integer base B.|*A* - The decimal number that you want to convert. <br>*B*/ - The base you want to convert A into.|*Ans* - The base B representation of the decimal number, in list form.|imcoraline|

```
:iPart(ln(A)/ln(B
:BfPart(int(AB^(cumSum(binomcdf(Ans,0))-Ans-1))/B
```

This routine takes a positive whole decimal number (base 10), stored in A, and converts it to the equivalent representation in base B. The representation will be in list form. For example, the decimal number 32 is the base 2 number 100000, meaning the routine would result in the list {1,0,0,0,0,0}.

**Note: This routine will not work for A<B.**

It also may be important to note that adding 0’s to the front of a number will not change the decimal equivalent. For example, both 0110101<sub>2</sub> and 110101<sub>2</sub> are equivalent to 53<sub>10</sub>. 

## Error Conditions

- **[ERR:DATATYPE](errors.html#datatype)** is thrown if A is complex or negative.
- **[ERR:DOMAIN](errors.html#domain)** is thrown if A is 0 or less than B.
- An error will not be thrown is A isn’t an integer. Nonetheless, the conversion will not work correctly. 

## Related Routines

- [Binary to Decimal](binary-to-decimal.html)
- [Binary Data Compression](binary-data-compression.html)
