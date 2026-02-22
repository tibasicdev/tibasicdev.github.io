![The randNorm() Command](68k_randnorm/randnorm.png "The randNorm() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Generates a random normally-distributed number.|randNorm(*mean*,*std-dev*)|This command works on all calculators.|1 byte|
       
### Menu Location
- Press 2nd MATH to enter the MATH popup menu.
- Press 7 to enter the Probability submenu.
- Press 5 to select randNorm(.
       
# The randNorm() Command

The randNorm() command generates a random number that is normally distributed, with a given mean (first parameter) and standard deviation (second parameter). This means that on average, randNorm(x,y) will give a result of about x; it's 95% certain to be within 2*y of x.

See [68k:rand()](68k:rand.html) and [68k:RandSeed](68k:randseed.html) for more details on the random number generator.

## Formula

The formula for randNorm() is different from the one used by the TI-83 series. To generate normally-distributed values from the output of rand(), the calculator uses the polar form of the [Box-Muller transform](https://en.wikipedia.org/wiki/box-muller_transform). The algorithm goes as follows:

First, generate two uniformly distributed numbers *u* and *v* in [-1,1]. Keep doing this until the result lies in the unit circle; the point (0,0), though it's unlikely to occur, is discarded as well. Let *s* equal *u*<sup>2</sup>+*v*<sup>2</sup>. 

Usually, Box-Muller is used to produce two normally-distributed random numbers, by the formula below. The TI only uses the second of the results:
$$ z_0=u\cdot\sqrt{\frac{-2\ln s}{s}}\hspace{2em}z_1=v\cdot\sqrt{\frac{-2\ln s}{s}} $$

The result is distributed according to the standard normal distribution: that is, with mean 0 and standard deviation 1. It's easy to get any other normal distribution by scaling: multiplying by the standard deviation, and then adding the mean.

In TI-Basic, the code for randNorm(μ,σ) would be:
```
:Loop
: 2*rand()-1→u
: 2*rand()-1→v
: u^2+v^2→s
: If 0<s and s<1
:  Return μ+σ*v*√(-2*ln(s)/s)
:EndLoop
```

## Related Commands

- [68k:rand()](68k:rand.html)
- [68k:randMat()](68k:randmat.html)
- [68k:randPoly()](68k:randpoly.html)
- [68k:RandSeed](68k:randseed.html)
