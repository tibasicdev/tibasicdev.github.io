![The randMat() Command](68k_randmat/randmat.png "The randMat() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Generates a random matrix.|randMat(*rows*,*columns*|This command works on all calculators.|1 byte|
       
### Menu Location
- Press 2nd MATH to enter the MATH popup menu.
- Press 7 to enter the Probability submenu.
- Press 7 to select randMat(.
       
# The randMat() Command

The randMat() command generates a random matrix: randMat(*rows*,*columns*) generates a *rows* by *columns* matrix whose entries are random integers between -9 and 9.

```
:RandSeed 0
:randM(3,2)
           [4  -2]
           [0  -7]
           [8  8 ]
```

## Advanced Uses

Using the [68k:RandSeed](68k:randseed.html) command makes the random matrix entirely predictable: after setting the random seed to some value, the same random matrix will be returned every time (assuming the size is the same). See the RandSeed page for details of how random numbers are generated.

## Error Conditions



## Related Commands

- [68k:rand()](68k:rand.html)
- [68k:randNorm()](68k:randnorm.html)
- [68k:randPoly()](68k:randpoly.html)
- [68k:RandSeed](68k:randseed.html)
