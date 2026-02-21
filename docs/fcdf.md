![The Fcdf( Command](fcdf/FCDF.GIF "The Fcdf( Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Calculates the *F*-distribution probability betwen *lower* and *upper* for specified numerator and denominator degrees of freedom.|Fcdf(*lower*, *upper*, *numerator df*, *denominator df*|TI-83/84/+/SE|2 bytes|

### Menu Location
Press:
1. 2ND DISTR to access the distribution menu
2. 9 to select Fcdf(, or use arrows.
Press 0 instead of 9 on a TI-84+/SE with OS 2.30 or higher.
       
# The Fcdf( Command

`Fcdf(` is the *F*-distribution cumulative density function. If some random variable follows this distribution, you can use this command to find the probability that this variable will fall in the interval you supply.

The arguments *lower* and *upper* express the interval you're interested in. The arguments *numerator df* and *denominator df*, often written *d<sub>1</sub>* and *d<sub>2</sub>*, specify the *F*-distribution, written as `F(`*d<sub>1</sub>*,*d<sub>2</sub>*`)`.

## Advanced

Often, you want to find a "tail probability" - a special case for which the interval has no lower or no upper bound. For example, "what is the probability x is greater than 2?". The TI-83+ has no special symbol for infinity, but you can use E99 to get a very large number that will work equally well in this case (E is the decimal exponent obtained by pressing [2nd] [EE]). Use E99 for positive infinity, and -E99 for negative infinity.

## Formulas

As with other continuous distributions, `Fcdf(` can be expressed in terms of the probability density function:

$$\operatorname{Fcdf}(a,b,d_1,d_2) = \int_a^b \operatorname{Fpdf}(x,d_1,d_2) \, dx$$

## Related Commands

- [`Fpdf(`](fpdf.html)
- [`ShadeF(`](shadef.html)
