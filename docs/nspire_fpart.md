![Fpart](nspire_fpart/sample.png "Fpart")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|
|--- |--- |--- |
|Returns the fractional part of a value.|fPart(*value*)|If this is only available on certain versions of the nspire|

### Menu Location
Describe how to get the command from a menu.

# Fpart
fPart(*value*) returns the fractional part of *value*. Also works on complex numbers, lists and matrices.
```
fPart(5.32)
             .32
fPart(4/5)
              .8
fPart(‾5.32)
             ‾.32
fPart(‾4/5)
              ‾.8
```

## Advanced Uses

fPart(, along with [nspire:int(](nspire:int.html) or [nspire:iPart(](nspire:ipart.html), can be used for integer [compression](compression.html).

------

Also, fPart( is an easy way to find A mod B (the positive remainder when A is divided by B). 

```
:B(A<0)+iPart(BfPart(A/B))
```

If A is guaranteed to be positive, the following shorter code can be used, omitting B(A<0):

```
:iPart(BfPart(A/B))
```

------

Finally, the easiest way to check if a number is a whole number is not(fPart(X:

```
:If not(fPart(X:Then
: // X is an integer
:Else
: // X is not an integer
:End
```

You can use this, for example, to check if a number is divisible by another: if X is divisible by N, then X/N is a whole number. This is useful when you want to find the [factors](factorization.html) of a number. Warning: when storing values with repeating decimals and later multiplying them to see if a number makes it an integer it can return a value of 1 or -1 instead of 0 even if it is an integer. Example: if you store 1/3 as X and then do fpart(3x) it will return 1 instead of 0. This is because fpart(.999...) results in .999... and then rounds to 1 when displaying rather than rounding to 1.0 and then displaying the fpart( as 0. 

## Optimization

Often you want to find the value of a-1 mod b — this occurs, for example, in movement routines with wraparound. However, the problem is that if a=0, a-1 will be negative. Rather than use the longer version of the modulo routine, you might replace subtracting 1 with adding (b-1). This will have the same result, but without sign problems.

## Related Commands

- [nspire:int(](nspire:int.html)
- [nspire:iPart(](nspire:ipart.html)
- [nspire:round(](nspire:round.html)
- [nspire:mod(](nspire:mod.html)

## See Also

- [Compression](compression.html)
- [Number Factorization](factorization.html)
