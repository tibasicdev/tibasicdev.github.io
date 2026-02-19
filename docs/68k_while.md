![The While Command](68k_while/while.png "The While Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Repeats a block of code as long as a condition is met|:While *condition*<br>*(block of code)*<br>:EndWhile|This command works on all calculators.|2 bytes for While;<br>4 bytes for EndWhile.|
       
### Menu Location
Starting in the program editor:
- Press F2 to enter the Control menu.
- Press 5 to paste While..EndWhile.
       
# The While Command

A While..EndWhile block is used to repeat a block of code as long as some true-or-false condition is met. This condition is checked before entering the loop (if it's false to begin with, the loop is skipped), and checked again every time the loop ends. For example:
```
:1→x
:While x<5
: x+1→x
: Disp x
:EndWhile
           1
           2
           3
           4
```
The condition is *not* checked anywhere in the middle of the loop. If the condition becomes temporarily false, but then becomes true again before the end, the loop keeps going.

What kind of conditions are possible? Any command that returns a logical value — true or false — is acceptable. This includes the results of:
- Relational operators: [=](68k:equal.html), [≠](68k:not-equal.html), [>](68k:greater-than.html), [≥](68k:greater-than-or-equal.html), [<](68k:less-than.html), and [≤](68k:less-than-or-equal.html)
- Logical operators: [and](68k:and.html), [or](68k:or.html), [xor](68k:xor.html), [not](68k:not.html)
- Any advanced test command: [pxlTest()](68k:pxltest.html), [isPrime()](68k:isprime.html), and others.
- A variable that contains one of the values true or false, or a function that returns them.
Of course, these can also be combined: for example, isPrime(x) and x≠2 is a valid condition.

One common use of a While loop is to wait for a key to be pressed:
```
:0→key
:While key=0
: getKey()→key
:EndWhile
```

## Optimization

In most programming languages a loop that always keeps repeating would be created using a While loop with a condition that's always true. You can do this in TI-Basic too, but it's simpler to use [68k:Loop](68k:loop.html)..EndLoop which does the same thing.
```
:While true
: © do something
:EndWhile

can be

:Loop
: © do something
:EndLoop
```

## Error Conditions




## Related Commands

- [68k:Cycle](68k:cycle.html)
- [68k:Exit](68k:exit.html)
- [68k:For](68k:for.html)..EndFor
- [68k:Loop](68k:loop.html)..EndLoop
