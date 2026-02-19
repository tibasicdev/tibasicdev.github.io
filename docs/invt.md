![The invT( Command](invt/invT.png "The invT( Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Calculates the inverse of the cumulative [Student's t-distribution](https://en.wikipedia.org/wiki/student-27s_t-distribution) function with degrees of freedom ν.|invT(*probability*, *ν*)|TI-84+/SE (OS 2.30 or greater)|2 bytes|

### Menu Location
Press:
1. 2ND DISTR to access the distribution menu
1. 4 to select invT(, or use arrows.
       
# The invT( Command

`invT(` is the inverse of the cumulative Student t distribution function: given a probability *p* and a specified degrees of freedom *v*, it will return the number *x* such that `tcdf(E-99,*x*,*v*)` is equal to *p*

```
:invT(.95,24
	1.710882023
```

## Advanced

`invT(` is meant for use with so-called "one-tailed' tests; for two-tailed tests, the proper expression to use (corresponding to the inverse of `tcdf(-*x*,*x*,*v*)`) is `invT(.5(1+*p*),*v*)`

## Formulas

Unlike the [`tpdf(`](tpdf.html) and [`tcdf(`](tcdf.html) commands, the invT( command does not have a closed-form formula. However, it can be expressed in terms of the inverse incomplete beta function.

For one degree of freedom, `invT(` is expressible in terms of simpler functions:

$$
\operatorname{invT}(p,1)=\tan\left(\pi\left(p-\frac1{2}\right)\right)$$

## Related Commands

- [`tpdf(`](tpdf.html)
- [`tcdf(`](tcdf.html)
- [`Shade_t(`](shade_t.html)
