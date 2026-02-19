# Index Finder
|Routine Summary|Inputs|Outputs|Author|
|--- |--- |--- |--- |
|Returns the index number of an element searched for within a list|*X* - Element that it's finding<br>*L₁* - List that's being searched<br>*N* - The occurrence to search for|*Ans* - Index number of element searched.|RogueBantha, CubeBag|

```
//Finds first occurrence of X in L₁
1+sum(not(cumSum(L₁=X

//Finds last occurrence of X in L₁
max((L₁=X)cumSum(1 or L₁

// Finds the Nth occurrence of X in L₁
1+sum(N>cumSum(L₁=X
```

Given a value in `X`, this code will search `L₁` and return the index number of the desired occurrence of `X`.

## Error Conditions
If `L₁` does not contain `X`, the first and third routines will both return `1+[dim(](dim.html)L₁)`; the second will return zero.
