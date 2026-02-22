![The ∫() Command](68k_integral/integral.png "The ∫() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Takes the integral of an expression.|∫(*expression*,*variable*)<br>∫(*expression*,*variable*,*constant*)<br>∫(*expression*,*variable*,*lower*,*upper*)|This command works on all calculators.|2 bytes|
       
### Menu Location
Press [2nd][7] to enter ∫(.
       
# The ∫() Command

∫(*expression*,*variable*) takes the integral of *expression* (symbolically) with respect to *variable*. All other variables are treated as constant.

There are three ways to use ∫(). The syntax above returns an indefinite integral. ∫(*expression*,*variable*,*c*) does the same, but with a constant of integration, *c* (this will just get added on to the result). Finally, ∫(*expression*,*variable*,*a*,*b*) takes a definite integral from *a* to *b*. These limits can be anything, including undefined variables, ∞ and -∞, as long as they don't depend on *variable*.

```
:∫(x^2,x)
           x^3/3
:∫(x^2,x,c)
           x^3/3+c
:∫(x^2,x,a,b)
           b^3/3-a^3/3
```

Indefinite integrals are always computed exactly or not at all: if a part of the expression (or the entire expression) can't be integrated, the result will stay in terms of ∫(). However, definite integrals will sometimes be approximated, depending on the Exact/Approx [mode setting](68k:mode-settings.html):
- If EXACT, integrals will never be approximated.
- If AUTO, the calculator will approximate integrals like ∫(*e*^(-x^2),x,-1,1) that it can't compute exactly.
- If APPROX, all definite integrals will be done numerically if possible.

```
:∫(e^(-x^2),x)
           ∫(e^(-x^2),x)
:∫(e^(-x^2),x,-1,1)
           2*∫(e^(-x^2),x,0,1) (in EXACT mode)
           1.49365 (in AUTO or APPROX mode)
```

Finally, you can take multiple integrals by applying ∫() to the result of another ∫() (any number of times). The integration limits of the inner integrals can involve the variables of the outer integrals.

```
:∫(∫(x*y,x),y)
           y^2*x^2/4
:∫(∫(x*y,x,0,y),y,0,1)
           1/8
```

If the expression is a list or matrix, ∫() takes the integral of each element.

## Error Conditions

**[140 - Argument must be a variable name](68k:errors.html#e140)** happens when the variable of integration isn't a variable.
**[220 - Dependent limit](68k:errors.html#e220)** happens when the integration limits depend on the variable of integration.

## Related Commands

- *[68k:d](68k:d.html)*[()](68k:d.html) (derivative)
- [68k:nInt()](68k:nint.html)
- [∑()](68k:sigma-sum.html) (sum)
