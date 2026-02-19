![The min() Command](68k_min/min.png "The min() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Finds the lowest numerical value from arguements|min(arg1,[arg2])|This command works on all calculators.|X|
       
### Menu Location

       
# The min() Command

The min() Command can be executed in two different ways.

It can find the lowest of two numbers:
```
min(0,1)
//returns 0
```

It can find the lowest number in a list:
```
min({0,1,2})
//returns 0
```

## Advanced Uses

For advanced users, the min command can also have its two arguments replaced with lists, as long as the two lists have the same dimensions and only include numbers. min(list,list) returns a list, with min having been done on each pair of items, as is the custom for lists in functions.

```
min({123},{321})
//returns {1,2,1}
```

It also works in much the same way for matrices.

```
min([[1,2,3][1,2,3]],[[3,2,1][3,2,1]])
//returns [[1,2,1][1,2,1]]
```

## Optimization

If comparing two numbers, it is slightly faster to compare the two as two arguments than to have them in a list.

```
:min({1,2})
can be
:min(1,2)
```

The first example takes 13 seconds for 1000 repetitions, while the second takes only 9. When using the min command repetitively, this will add up.

## Related Commands

- [68k:Mean](68k:mean.html)
- [68k:Mod](68k:mod.html)
- [68k:Max](68k:max.html)
- [68k:Median](68k:median.html)
