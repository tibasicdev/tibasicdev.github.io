![The isPrime() Command](68k_isprime/isprime.png "The isPrime() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|
|--- |--- |--- |
|Returns true for prime arguments and false for composite arguments.|isPrime(*expression*)|This command works on all calculators.|
       
### Menu Location

# The isPrime() Command

The isPrime() command returns a Boolean value based on whether or not the passed argument is prime or not.  True is returned for prime numbers and false is returned for composite numbers.  A number is prime if its divisors are only 1 and itself.  For instance, the number 23 is considered prime because no two positive integers but 1 and 23 can multiply to get 23.  For the calculator, 1 isn't considered prime.

```
isPrime(23)
       true
isPrime(24)
       false
```

## Algorithm

According to TI, the algorithm run by the calculators is as follows:

"The algorithms used by the TI-89 family, TI-92 family, and Voyage 200 calculators divides by successive primes through the largest one less than 216. It does not actually keep a table or use a sieve to create these divisors, but cyclically adds the sequence of increments 2, 2, 4, 2, 4, 2, 4, 6, 2, 6 to generate these primes plus a few extra harmless composites.

TI-92 Plus and TI-89 family start the same way, except that they stop this trial division after trial divisor 1021, then switch to a relatively fast Monte-Carlo test that determines whether the number is certainly composite or is almost certainly prime. The isPrime() function stops at this point returning either false or (almost certainly) true."
