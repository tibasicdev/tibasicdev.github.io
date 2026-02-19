![The tcdf( Command](tcdf/TCDF.GIF "The tcdf( Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Calculates the Student's *t* probability betwen *lower* and *upper* for degrees of freedom ν.|tcdf(*lower*, *upper*, *ν*)|TI-83/84/+/SE|2 bytes|

### Menu Location
Press:
1. 2ND DISTR to access the distribution menu
1. 5 to select tcdf(, or use arrows.
Press 6 instead of 5 on a TI-84+/SE with OS 2.30 or higher.
       
# The tcdf( Command

tcdf( is the Student's *t* cumulative density function. If some random variable follows this distribution, you can use this command to find the probability that this variable will fall in the interval you supply.

Unlike [normalcdf(](normalcdf.html), this command only works for the standardized distribution with mean 0 and standard deviation 1. To use it for non-standardized values you will have to standardize them by calculating (X-μ)/σ (where μ is the mean and σ the standard deviation). Do this for both *lower* and *upper*. 

## Advanced

Often, you want to find a "tail probability" - a special case for which the interval has no lower or no upper bound (the form frequently used in one-tailed tests). For example, "what is the probability x is greater than 2?". The TI-83+ has no special symbol for infinity, but you can use E99 to get a very large number that will work equally well in this case ([E](e-ten.html) is the decimal exponent obtained by pressing [2nd] [EE]). Use E99 for +∞, and -E99 for -∞.

Alternatively, you can exploit the identity

$$\operatorname{tcdf}(-\infty,0,\nu)=\frac1{2}$$

(similarly for the interval from 0 to ∞)

and thus

$$\operatorname{tcdf}(-\infty,x,\nu)=\frac1{2}+\operatorname{tcdf}(0,x,\nu)$$

For the form used in two-tailed tests, the following identity may be useful:

$$\operatorname{tcdf}(-x,x,\nu)=2\operatorname{tcdf}(0,x,\nu)$$

## Formulas

As with any other continuous distribution, tcdf( can be defined in terms of the probability density function, [tpdf(](tpdf.html):

$$\operatorname{tcdf}(a,b,\nu)=\int_a^b \operatorname{tpdf}(t,\nu)\mathrm{d}t$$

The function can also be expressed in terms of an [incomplete beta function](http://mathworld.wolfram.com/incompletebetafunction.html).

For one degree of freedom (ν=1), tcdf( is expressible in terms of simpler functions:

$$\operatorname{tcdf}(a,b,1)=\frac1{\pi}\left(\tan^{-1}\left(b\right)-\tan^{-1}\left(a\right)\right)$$

This is the so-called Cauchy distribution.

## Related Commands

- [tpdf(](tpdf.html)
- [invT(](invt.html)
- [Shade_t(](shade_t.html)
