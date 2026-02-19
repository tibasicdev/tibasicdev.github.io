# Linear Regression Standard Error
|Routine Summary|Inputs|Outputs|Variables Used|
|--- |--- |--- |--- |
|Calculates the standard error associated with linear regression coefficients.|*L₁* - values of the independent variable<br>*L₂* - values of the dependent variable|*Ans* - a 2-element list containing the standard errors|L₁, L₂,|

```
:2-Var Stats
:LinReg(ax+b)
:a√((r²ֿ¹−1)/(n-2)){1,√(Σx²/n)}
```

This routine computes the standard error (uncertainty) associated with the linear regression coefficients *a* and *b* (σ<sub>*a*</sub> and σ<sub>*b*</sub>, respectively) for the regression equation *y*=*a**x*+*b*. Precisely stated, the true value of the coefficient *a* is expected to be within the interval *a*±σ<sub>*a*</sub>, and similarly for *b*.

The routine returns a two-element list; σ<sub>*a*</sub> is the first element, and σ<sub>*b*</sub> is the second element.

If one prefers to use the function [LinReg(a+bx)](linreg(a-bx).html) instead of [LinReg(ax+b)](linreg(ax-b).html), the appropriate routine is:

```
:2-Var Stats
:LinReg(a+bx)
:b√((r²ֿ¹−1)/(n-2)){√(Σx²/n),1}
```

(note that the meanings of σ<sub>*a*</sub> and σ<sub>*b*</sub> have now interchanged).

In both routines, r², a, b, n, and  Σx² are statistical variables.

## Formulas

For the fitting equation *y*=*a**x*+*b*,

$$\definecolor{darkgreen}{rgb}{0.90,0.91,0.859}\pagecolor{darkgreen}
\begin{align*}
\sigma_a&=a\sqrt{\frac{\frac1{r^2}-1}{n-2}} \\
\sigma_b&=\sigma_a\sqrt{\frac{\Sigma x^2}{n}}
\end{align*}$$

where *n* is the number of data points, *r*² is the coefficient of determination, and Σ*x*² is the sum of squares of the independent variable values.

## Error Conditions

- **[ERR:DIM MISMATCH](errors.html#dimmismatch)** is thrown if the two lists' sizes are not the same.

## Reference

Lichten, William. *Data and Error Analysis*., 2nd. ed., Prentice Hall:  Upper Saddle River, NJ, 1999.
