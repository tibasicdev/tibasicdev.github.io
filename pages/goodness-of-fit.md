# χ² Goodness-of-fit Test
|Routine Summary|Inputs|Outputs|Variables Used|Download|
|--- |--- |--- |--- |--- |
|Performs a chi-square goodness-of-fit test, to determine if an observation fits a distribution.<br><br>The TI-84+ and TI-84+ SE have a command, [χ²GOF-Test(](http://tibasicdev.github.io/chisquaregof-test), that does the same thing.|*L₁* - observed counts of the outcomes<br>*L₂* - expected counts of their outcomes, or their distribution|*X* - the χ² statistic for the data.<br>*F* - the df (degrees of freedom) statistic.<br>*P* - the probability value of the test.|L₁, L₂, X, F, P|[file gof-test.zip]|

```
:L₂sum(L₁)/sum(L₂→L₂
:sum((L₁-L₂)²/L₂→X
:dim(L₁)-1→F
:χ²cdf(X,E99,F→P
```

This routine tests the null hypothesis that the variation between the observed and expected distributions is due to random chance alone. The value of P is the probability that such variation would occur, assuming the null hypothesis. You would reject this null hypothesis if this value is too low, and conclude that the variable you're measuring doesn't vary according to the expected distribution.

First, we must normalize L₂, the expected distribution, to have the same sum as L₁. We do this by multiplying by the sum of L₁, and dividing by the original sum of L₂. You can omit this line if L₂ already has the same sum, or optimize it to L₂sum(L₁→L₂ if it's a probability distribution (and hence has a sum of 1).

Then, we calculate the χ² statistic (according to the formula given at the bottom of the page). The number of degrees of freedom is just defined to be one less than the number of outcomes. Then, we calculate the probability that χ² would have a value this high by chance alone, by using the [χ²cdf(](chisquarecdf.html) command to calculate the probability mass between this value and infinity (we can't actually put in infinity, but we use the value E[[/size]]99, which is close enough for our purposes — the error introduced by this is too small for the calculator to evaluate).

An example: suppose you want to test if your six-sided die is fair. You threw the die 60 times, and recorded the results: a 1 came up 13 times, a 2 came up 10 times, a 3 came up 6 times, a 4 came up 9 times, a 5 came up 8 times, and a 6 came up 14 times. This is the observed frequency. The expected frequency is that the results would be even: each side would come up 10 times. Therefore, we set L₁ to {13,10,6,9,8,14} and L₂ to {10,10,10,10,10,10}.

The output is the following:
```
χ²=4.6
p=.4666162743
df=5
```

Because the value of p is high, it's perfectly plausible that the null hypothesis is true: p>0.05, so the data is not significant on a 5% level. We don't have enough evidence to reject the null hypothesis, so we conclude that the die is fair.

## Formulas

The formula for calculating the χ² statistic: (O<sub>i</sub> is the observed count of the ith outcome, and E<sub>i</sub> is the expected count)
$$
\chi_{n-1}^2 = \sum_{i=1}^n \frac{(O_i-E_i)^2}{E_i}$$

## Error Conditions

- **[ERR:DIM MISMATCH](errors.html#dimmismatch)** is thrown if the two lists' sizes aren't the same.
- **[ERR:DOMAIN](errors.html#domain)** is thrown if the lists have only one element or if the values in the observed list are not integers.
