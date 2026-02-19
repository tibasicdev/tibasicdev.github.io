# Number Concatenation
|Routine Summary|Inputs|Outputs|Variables Used|Author|Download|
|--- |--- |--- |--- |--- |--- |
|Concatenates two whole numbers together.|*M* - the first number<br>*N* - the second number|*O* - the concatenated number|M, N, O|DarkerLine|[file numberconcatenation.zip]|

```
:N+M10^(1+int(log(N→O
```

With our two numbers stored in M and N respectively, we add the first number to the second number by raising it to the 10<sup>th</sup> power, with the exponent being how many digits are in the number. We then store this result to a new variable for later use.

We can figure out how many digits are in a number by using the 1+int(log( trick. This trick works with any positive whole numbers, and if you add [abs(](abs.html) after [log(](log.html), it will also work with negative numbers. Unfortunately, it does not work with decimals.
