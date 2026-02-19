![The randNorm( Command](randnorm/RANDNORM.GIF "The randNorm( Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Generates a random normally-distributed number with specified mean and standard deviation.|randNorm(*µ*,*σ*,[*n*])|TI-83/84/+/SE|2 bytes|

### Menu Location
Press:
1. MATH to access the [math](math.html) menu.
1. LEFT to access the PRB submenu.
1. 6 to select randNorm(, or use arrows.
       
# The randNorm( Command

randNorm(*µ*,*σ*) generates a normally-distributed pseudorandom number with [mean](mean.html) *µ* and [standard deviation](stddev.html) *σ*. The result returned will most probably be within the range *µ*±3*σ*. randNorm(*µ*,*σ*,*n*) generates a list of *n* normally-distributed pseudorandom numbers with mean *µ* and standard deviation *σ*.

*seed*→rand affects the output of randNorm(.
```
0→rand
     0
randNorm(0,1)
     -1.585709623
randNorm(0,1,3)
     {-1.330473604 1.05074514 -.0368606663}
```

Although a theoretical normally distributed variable could take on any real value, numbers on a calculator have a limited precision, which leads to a maximum range of approximately *µ*±7.02*σ* for values of randNorm(.

## Optimization

When the mean is 0 and the standard deviation 1, [invNorm(](invnorm.html)rand) and invNorm(rand(N)) save space over randNorm(0,1) and randNorm(0,1,N) respectively.

## Formulas

The value of randNorm( for a given seed can be expressed in terms of [rand](rand.html):

```
randNorm(µ,σ)=µ-σinvNorm(rand
```

This is identical to the output of randNorm( in the sense that for the same seed, both expressions will generate the same random numbers.

The following formula can be used to get a target interval where A and B are two real intervals.

```
µ=(A+B)/2
σ=(-A+B)/6
```

## Related Commands

- [rand](rand.html)
- [randInt(](randint.html)
- [randBin(](randbin.html)
- [randM(](randm.html)
- [randIntNoRep(](randintnorep.html)
