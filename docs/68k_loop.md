![The Loop Command](68k_loop/loop.png "The Loop Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Repeats a block of code forever.|:Loop<br>*(block of code)*<br>:EndLoop|This command works on all calculators.|2 bytes for Loop;<br>4 bytes for EndLoop.|
       
### Menu Location
Starting in the program editor:
- Press F2 to enter the Control menu.
- Press 6 to paste Loop..EndLoop.
       
# The Loop Command

A Loop..EndLoop block is used to make the code inside the Loop repeat forever. For example, the following code will keep printing "Hello!" until you break out of the program with the ON key or the calculator runs out of batteries:
```
:Loop
: Disp "Hello!"
:EndLoop
           Hello!
           Hello!
           Hello!
           ...
```

Generally, Loop isn't used just like that, because having to end a program with the ON key lacks style. There are two ways to break out of the loop:
- using [68k:Goto](68k:goto.html), you can jump to somewhere else in the program.
- using [68k:Exit](68k:exit.html), you can exit the loop, continuing the program immediately after the EndLoop command.

Generally, using Exit is considered more stylish — and it's easier to read the code, because you don't have to search the entire program for the Goto's matching label.

## Error Conditions

**[730 - Missing start or end of block syntax](68k:errors.html#e730)** happens when the Loop is missing an EndLoop, or vice versa.

## Related Commands

- [68k:Cycle](68k:cycle.html)
- [68k:Exit](68k:exit.html)
- [68k:For](68k:for.html)..EndFor
- [68k:While](68k:while.html)..EndWhile
