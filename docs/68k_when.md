![The when() Command](68k_when/when.png "The when() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Chooses between two values based on a condition.|when(*condition*,*if-true*,*if-false*,[*if-undef*]])|This command works on all calculators.|2 bytes|
       
### Menu Location
Starting in the program editor:
- Press F2 to enter the Control menu.
- Press 3 to select when(.
       
# The when() Command

The when() command — a sort of one-line alternative to [68k:If](68k:if.html) — chooses one of (usually) two values based on a condition. The first argument is the condition to check; if the condition is true, when() evaluates the second argument, and if the condition is false, it evaluates the third.

```
:when(2+2=4,"Math works!","Math doesn't work!")
           "Math works!"
```

Only the chosen alternative is even calculated. If the condition is true, for example, when() will save time by not even bothering to check what the false condition even is.

Unlike If, when() doesn't have a problem with conditions that can't be fully resolved: it will just stay in its unevaluated form. And it gets better...

## Advanced Uses

You can give when() a third alternative, that will be taken if the condition isn't certain to be true or false. This usually happens because there's an undefined variable in the condition. For instance:
```
:when(x>0,"x is positive","x is negative or 0","x is undefined")
```
This can also happen if you give it a strange data type: for instance, if the "condition" of when() is an integer, the third alternative will be taken, because it's neither true nor false.

## Optimization

It's usually better to use when() instead of If, at least for short calculations. The result will be more compact, and as the [68k:timings](68k:timings.html) page shows, it's marginally faster, as well. However, for complicated conditions, when() is hard to read, especially if there are several when()'s in the same expression.

TI-83 series programmers might be tempted to use when() to convert true and false values to the more familiar 0 and 1:
```
:when(cond,1,0)
```
This has some applications, but in general you should avoid this: using when() directly is almost always better.

## Related Commands

- [68k:If](68k:if.html)..EndIf
- [68k:Try](68k:try.html)..EndTry
