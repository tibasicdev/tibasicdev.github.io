![The ans() Command](68k_ans/ans.png "The ans() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Returns a previous answer from the Home screen.|ans([*integer*]).|This command works on all calculators.|X byte(s)|
       
### Menu Location
2nd, ANS (the (-) key)
# The ans() Command


Simply put, the `ans()` function returns an answer that the calculator has already returned. The argument specifies which answer to return, and must be an integer between 1 and 99 and may not be an expression or a variable. For example `ans(1)`, the default, will return the last answer displayed on the home screen. `ans(3)`, however, will return return the third most recent answer. If no argument is provided, the calculator assumes 1. Strangely, while official documentation states that the argument must be between 1 and 99, 0 may be used, which returns the same answer as if 1 were used (this is probably why `ans()` returns the most recent answer, even though no argument is provided).

```
Example home screen input to generate the Fibonacci sequence.

:1
       1 
:1
       1
:ans(1)+ans(2)
       2
:ans(1)+ans(2)
       3
```

## Advanced Uses

When entered into a program, the calculator will automatically change the `ans()` command into whatever value it represents at runtime, so that even if the home screen changes, the program will always return the same value of the `ans()` function as the first time it was run. This may be avoided by using the `expr()` function and putting the `ans()` function in quotes to make it a string. For example: `expr("ans(3)")`. This can be rather cumbersome, however, and generally anything that you can do with the `ans()` function can be accomplished equally well with a variable.

------

## Error Conditions
