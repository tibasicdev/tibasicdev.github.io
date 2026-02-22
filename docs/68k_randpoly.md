![The randPoly() Command](68k_randpoly/randpoly.png "The randPoly() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Generates a random polynomial.|randPoly(*var*,*deg*)|This command works on all calculators.|1 byte|
       
### Menu Location
- Press 2nd MATH to enter the MATH popup menu.
- Press 7 to enter the Probability submenu.
- Press 8 to select randPoly(.
       
# The randPoly() Command

The randPoly() command generates a random polynomial. randPoly(*var*,*deg*) generates a random polynomial in variable *var* of degree *deg*. The coefficients of each power of *var* are random integers from -9 to 9.

```
:RandSeed 0
:randPoly(x,5)
           4*x^5-2*x^4-7*x^2+8*x+8
```

## Advanced Uses

Using the [68k:RandSeed](68k:randseed.html) command makes the resulting polynomial entirely predictable: every time you set the random seed to some variable, you will get the same random coefficients afterwards. Also see RandSeed for details of how random numbers are generated.

## Error Conditions

**[260 - Domain error](68k:errors.html#e260)** happens when the value of *deg* is not between 0 and 99.

## Related Commands

- [68k:rand()](68k:rand.html)
- [68k:randMat()](68k:randmat.html)
- [68k:randNorm()](68k:randnorm.html)
- [68k:RandSeed](68k:randseed.html)
