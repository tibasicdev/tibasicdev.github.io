# Number Factorization
|Routine Summary|Inputs|Outputs|Variables Used|Author|Download|
|--- |--- |--- |--- |--- |--- |
|Returns the factors of a number.|*X* - the number you want to factor|*L₁* - the factors of the number|X, L₁, Ans|Weregoose|[file numberfactors.zip]|

```
:{1→L₁
:Repeat Ans=1
:2:While fPart(X/Ans
:Ans+1
:End
:Ans→L₁(1+dim(L₁
:X/Ans→X
:End
```

[Number factorization](https://en.wikipedia.org/wiki/factorization) breaks a number up into its *factors* - smaller numbers that that are multiplied together to create the number. For example, the number 100 can be broken up into the factors 2*2*5*5. It can also be represented as 10*10, or 5*20, but for the sake of completeness, this routine finds *prime factors* — which can't be broken down themselves (2*2*5*5 is such a factorization, since there's no way to factor 2 or 5, but 5*20 isn't, since 20 can still be factored).

In order to start collecting the factors of the number, we create a [list](lists.html) with the initial factor of 1 (because 1 is a factor for every number). We then begin looping through numbers, starting with 2, to find the next factor. The way we determine if we have a factor is by dividing the original number by the respective number we are at, and checking if there is a remainder.

If there is a remainder, we know that the number is not a factor, and we then increment it and continue looping. If there is no remainder, however, we have found a factor, and thus the loop will end. We then add that factor as the next element in our factors list, and divide the original number by that factor and set the result as the new number.  This gets repeated over and over again until we have our list of factors.

The factors list should be generated pretty quickly, but it all depends on the original value that you chose for X; a smaller value will be faster, and likewise a larger value will be slower. In addition, if you try starting with a negative number or a number with a decimal part, then the program will not work correctly.

When you are done using L₁, you should [clean it up](cleanup.html) at the end of your program.
