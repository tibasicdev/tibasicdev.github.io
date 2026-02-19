![The randBin( Command](randbin/RANDBIN.GIF "The randBin( Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Generates a random number with the binomial distribution.|randBin(*n*,*p*,*# simulations*)|TI-83/84/+/SE|2 bytes|

### Menu Location
Press:
1. MATH to access the [math](math.html) menu.
1. LEFT to access the PRB submenu.
1. 7 to select randBin(, or use arrows.
       
# The randBin( Command

randBin(*n*,*p*) generates a pseudorandom integer between 0 and *n* inclusive according to the binomial distribution B(*n*,*p*) - that is, *n* trials of an event with probability of success *p* are performed, and the number of successes is returned. randBin(*n*,*p*,*simulations*) performs the above calculation *simulations* times, and returns a list of the results. The expected (average) result is *n***p*.

*n* should be an integer greater than or equal to 1, while *p* should be a real number between 0 and 1 inclusive.

*seed*→rand affects the output of randBin(
```
0→rand
     0
randBin(5,1/2
     2
randBin(5,1/2,10
     {3 3 2 4 3 2 2 2 4 3}
```

## Formulas

The value of randBin( for a given seed can be expressed in terms of [rand](rand.html):

```
randBin(N,P)=sum(P>rand(N
```

This is identical to the output of randBin( in the sense that for the same seed, both expressions will generate the same random numbers.

## Error Conditions

- **[ERR:DOMAIN](errors.html#domain)** is triggered if the probability is not on the interval from 0 to 1.

## Related Commands

- [rand](rand.html)
- [randInt(](randint.html)
- [randNorm(](randnorm.html)
- [randM(](randm.html)
- [randIntNoRep(](randintnorep.html)
