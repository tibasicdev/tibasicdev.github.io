![The rand() Command](68k_rand/rand.png "The rand() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Generates a random number.|rand() or rand(*n*)|This command works on all calculators.|2 bytes|
       
### Menu Location
- Press 2nd MATH to enter the MATH popup menu.
- Press 7 to enter the Probability submenu.
- Press 4 to paste rand(.
       
# The rand() Command

The rand() command generates a random number. It can be used in one of two ways:
- rand() gives a random real number between 0 and 1.
- rand(*n*) gives a random integer between 1 and *n*.

By adding or multiplying appropriately, you can change these bounds. For example, 10rand() gives a random real number between 0 and 10, and rand(9)-5 gives a random number between -4 and 4.

[L'Ecuyer's algorithm](http://portal.acm.org/citation.cfm?doid-62959.62969) is used by TI calculators to generate pseudorandom numbers.

```
:RandSeed 0
:rand()
           .943597402492
:rand()
           .908318860975
:rand(10)
           2
```

## Advanced Uses

Using the [68k:RandSeed](68k:randseed.html) command makes the random numbers entirely predictable: after setting the random seed to some value, the same random numbers will be returned every time.

## Error Conditions



## Related Commands

- [68k:RandSeed](68k:randseed.html)
- [68k:randNorm()](68k:randnorm().html)
- [68k:randMat()](68k:randmat().html)
- [68k:randPoly()](68k:randpoly().html)
