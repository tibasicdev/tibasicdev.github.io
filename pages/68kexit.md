![The Exit Command](68k_exit/exit.png "The Exit Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Exits a loop.|:Exit|This command works on all calculators.|4 bytes|
       
### Menu Location
Starting in the program editor:<br>* Press F2 to enter the Control menu.<br>* Press 8 to enter the Transfers submenu.<br>* Press 5 to select Exit.
# The Exit Command

The Exit command immediately exits from a [68k:For](68k:for.html)..EndFor, [68k:Loop](68k:loop.html)..EndLoop, or [68k:While](68k:while.html)..EndWhile loop. The program continues running from the instruction after the EndFor, EndLoop, or EndWhile.

Exit is especially useful for Loop..EndLoop, because the loop won't ever end if you don't give it a reason to. For example:

```
:Loop
: Input "Number 1-100",num
: If 1≤num and num≤100
:  Exit
: Disp "Number out of range!"
:EndLoop
```

Often, a Loop..EndLoop block with an Exit inside it isn't a very good idea, because it can be replaced by a While..EndWhile block. However, in the example above, there is a difference: the condition for exiting the loop is not checked at the beginning. A While..EndWhile loop that did the same thing would have to initialize the num variable first.

If there are multiple loops, one nested inside the other, the Exit command only exits out of the innermost one. 

The Exit command can also be used to exit a sub-routine (very helpful when using subroutines on a 'skeleton' during development)

## Optimization

Although [68k:Goto](68k:goto.html) can also be used to exit out of a loop, the Exit command is faster: it knows where the end of the loop is, but a Goto command has to search through the entire program to find its label.

However, the Goto command is more versatile, since it can jump anywhere in the program, not just immediately after the loop. In particular, Goto can be used to exit multiple loops at once.

## Error Conditions



## Related Commands

- [68k:Cycle](68k:cycle.html)
- [68k:For](68k:for.html)..EndFor
- [68k:Loop](68k:loop.html)..EndLoop
- [68k:While](68k:while.html)..EndWhile
