![The toString( Command](tostring/toString.png "The toString( Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Returns the string representation of the value of the input.|toString(*value*)|TI-84+ CE OS 5.2|2 bytes|

### Menu Location
This command is found only in the Catalog. Press:
1. 2ND CATALOG to enter the catalog
1. T to go to commands starting with T
1. Scroll down to toString(.
       
# The toString( Command

The `toString(` command, given any value including real numbers, complex numbers, lists, or matrices, returns the string representation of the value of the input.

```
toString(1337       //returns "1337"

toString({1,2,3}    //returns "{1,2,3}"

toString([[1,2][3,4]]   //returns "[[1,2][3,4]]"

toString(√-1     //returns imaginary number "i"
```


`toString(` has less limitations than the [`eval(`](eval.html) command. It can handle lists, matrices, and complex numbers. Another difference from `eval(` is that `toString(` is affected by display mode changes like [`Fix`](fix.html).

`toString(` replaces the old [number-to-string](number-to-string.html) routine previously used prior to OS 5.2.

## Error Conditions

- **[ERR:DATA TYPE](errors.html#datatype)** is thrown when the input is a string.
- **[ERR:NONREAL ANSWERS](errors.html#nonrealans)** is thrown when the input is a complex number and your calculator is in REAL mode.
- **[ERR:SYNTAX](errors.html#syntax)** is thrown when trying to evaluate a command that doesn't return a value.

## Related Commands

- [`eval(`](eval.html)
- [`expr(`](expr.html)
