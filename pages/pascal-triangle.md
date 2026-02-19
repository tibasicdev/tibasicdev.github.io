# Pascal's Triangle
|Routine Summary|Inputs|Outputs|Variables Used|Download|
|--- |--- |--- |--- |--- |
|Returns the *R*<sup>th</sup> row of Pascal's triangle|*R* - The requested row of Pascal's triangle|*Ans* - Contains the row, as a list|R, Ans|[file pascaltriangle.zip]|

```
:{1
:If R
:2^Rbinompdf(R,.5
```

This routine uses the [binompdf(](binompdf.html) command to generate a row of [Pascal's triangle](https://en.wikipedia.org/wiki/pascal_triangle). Each number in Pascal's triangle is gotten by adding the two numbers above it, like such:

```
....1 
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
```

By tradition, the rows are numbered starting with 0, so that 1 is actually the "zeroth" row, while the first row is 1 1.

The binompdf( method of calculating rows of Pascal's triangle relies on one of its many properties: if a coin is flipped R times, then the number of heads (or the number of tails) flipped is distributed in the same way as the rows of the pascal's triangle, and the binompdf( command computes precisely such probabilities.

We multiply by 2^R to convert the probabilities to whole numbers. Unfortunately, binompdf( doesn't work for the R=0 case, so we make it a special case (if you never need to compute this case, you can omit this, turning the routine into a single statement).

Another way to get the number is to use the [nCr](ncr.html) command. N nCr K returns the K<sup>th</sup> element of the N<sup>th</sup> row (here, K is also numbered starting from 0). This can be done using the following line of code:

```
:seq(R nCr K,K,0,R
```

This goes through a line a gets every value of R nCr K and puts all results into a list. This routine is smaller than the one above, but is also slower.

## Error Conditions

- **[ERR:DOMAIN](errors.html#domain)** is thrown if *R* is negative, or not a whole number.

## Related Routines

If one outputs Pascal's triangle to a graph with even numbers as white dots and odd numbers as black dots, the outcome will be Sierpinski's triangle. Another way to generate Sierpinski's triangle is found below:

- [Sierpinski-Triangle](sierpinski-triangle.html)
