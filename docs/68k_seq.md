![The seq() Command](68k_seq/seq.png "The seq() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Creates a list by evaluating a formula over a range of values.|seq(*formula*,*variable*,*start*,*end*[,*step-size*]|This command works on all calculators.|2 bytes|
       
### Menu Location
- Press 2nd MATH to enter the MATH popup menu.
- Press 3 to enter the List submenu.
- Press 1 to select seq(.
       
# The seq() Command

The seq() command creates a [list](68k:lists.html) of terms of a sequence: seq(*formula*,*variable*,*start*,*end*) evaluates *formula* for every value of *variable* from *start* to *end*. Optionally, a fifth argument, *step-size*, is included: this increases the value of *variable* by *step-size* for each element, instead of 1.

seq() is similar to a [68k:For](68k:for.html)..EndFor loop, but instead of repeating a block of commands every time, it only evaluates a formula.

```
:seq(f(x),x,1,5)
           {f(1)  f(2)  f(3)  f(4)  f(5)}
:seq(x,x,3,9,2)
           {3  5  7  9}
:seq(x^2,x,5,1,-1)
           {25  16  9  4  1}
```

The variable used in seq(), x in the examples, is not actually modified.

## Advanced Uses

Because a [matrix](68k:matrices.html) is just a list of lists, you can use seq() to create matrices as well as lists. The simplest way to do it is to make the formula a list:
```
:seq({x,2x,3x},x,1,4)
           [1  2  3 ]
           [2  4  6 ]
           [3  6  9 ]
           [4  8  12]
```
You can also create a matrix by nesting a seq() command inside another seq() command:
```
:seq(seq(row+col,col,1,4),row,1,3)
           [2  3  4  5]
           [3  4  5  6]
           [4  5  6  7]
```

## Optimization

If all you need to do in a loop is create a list, it's probably better to use seq() than [68k:For](68k:for.html)..EndFor.

------

You can often use [68k:newList()](68k:newlist.html) instead of seq() to create an expression that gets evaluated much faster (see [68k:list-optimization](68k:list-optimization.html) for details).

## Error Conditions

For the non-generic errors that might occur when using this command (that is, syntax-type errors shouldn't be included). In a format similar to the following:




## Related Commands

- [68k:For](68k:for.html)..EndFor
- [68k:newList()](68k:newlist.html)
- [68k:newMat()](68k:newmat.html)
