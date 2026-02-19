![The newList() Command](68k_newlist/newlist.png "The newList() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Returns a list filled with zeroes.|newList(*length*)|This command works on all calculators.|1 byte|
       
### Menu Location
N/A

# The newList() Command

The `newList()` command returns a list of a specific length that is filled entirely with zeroes.
```
:newList(3)
           {0  0  0}
:newList(5)
           {0  0  0  0  0}
:newList(0)
           {}
```

This can be easily expanded to returning a list filled with any value: to return a list filled with a value x, just add x to the result of `newList()`. This works for strings as well, since "Hello"+0 simplifies to "Hello".

## Advanced Uses

`newList()` can be used for making a comparison between a single value and a list. Normally, something like {1,2,3,4}=2 simply returns "false", since 2 is not a list and {1,2,3,4} is. To do a comparison element-by-element, use `newList()` to turn the single value into a list: in this case, 2+`newList(4)`. Comparing {1,2,3,4} to 2+`newList(4)` will return {false, true, false, false} (you might use [`68k:when()`](68k:when().html) to get a single value out of this list).

This works to extend other operations to a number and a list, as well, though comparisons are the most useful application of this technique, since most operations already work this way.

## Optimization

In many cases, an expression with `newList()` can be used to optimize a [`68k:seq()`](68k:seq().html) command. First, observe that the simple
```
:seq(k,k,1,n)
```
which will return the list {1,2,3,...,n}, can be replaced by
```
:cumSum(1+newList(n))
```
The result is about twice as fast.

This is useful because many `seq()` expressions can be expressed using something like `seq(k,k,1,n)`. For example:
```
:seq(k^2,k,1,n)

can be

:seq(k,k,1,n)^2

which is

:cumSum(1+newList(n))^2
```
This rearrangement is not always possible, but when it is, it gives a significant improvement in speed, with no real difference in size. 

Here is a more complicated example (which is a sequence of probabilities with the binomial distribution). Notice the use of the [`68k:with`](68k:with.html) operator.
```
:seq(nCr(n,k) p^k (1-p)^(n-k),k,1,n)

can be

:nCr(n,a) p^a (1-p)^(n-a)|a=cumSum(1+newList(n))
```

## Error Conditions



## Related Commands

- [`68k:newMat()`](68k:newmat().html)
- [`68k:seq()`](68k:seq().html)
- [`68k:Fill`](68k:fill.html)
