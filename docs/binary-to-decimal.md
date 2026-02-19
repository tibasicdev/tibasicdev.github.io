# Binary To Decimal
|Routine Summary|Inputs|Outputs|Variables Used|Author|
|--- |--- |--- |--- |--- |
|Converts a binary (base 2) number to a decimal (base 10) number.|*Ans* - The binary number that you want to convert expressed as a list, stored in Ans.|*Ans* - The decimal representation of the binary number.|Ans, A|imcoraline|

```
:sum(seq(Ans(dim(Ans)-A)2^A,A,0,dim(Ans)-1
```

This routine takes a positive whole binary number (base 2), expressed as a list, and converts it to the equivalent decimal (base 10) representation. To express a binary number in a list, you simply put commas in between each digit, and then surround that with list brackets. For example, the binary number 101101 expressed a list would be {1,0,1,1,0,1}. To learn how to convert a binary number to a decimal number, vice versa, and even see how to convert to and from other bases besides binary and decimal, see the [Binary and Hexadecimal](binandhex.html) page.

It also may be important to note that adding 0’s to the front of a binary number will not change the decimal equivalent. For example, both 0110101<sub>2</sub> and 110101<sub>2</sub> are equivalent to 53<sub>10</sub>. 

## Error Conditions

- **[ERR:DATA TYPE](errors.html#datatype)** is thrown if the list has an imaginary number in it. 
- An error will not be thrown the list is not a binary number, or if any element in the list is negative or non-whole. Nonetheless, the conversion will not work correctly.

## Related Routines

- [Decimal to Binary](decimal-to-binary.html)
- [Binary Data Compression](binary-data-compression.html)
