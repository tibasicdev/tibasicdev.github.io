![The Cycle Command](68k_cycle/cycle.png "The Cycle Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Prematurely ends a cycle of a loop.|:Cycle|This command works on all calculators.|4 bytes|
       
### Menu Location
Starting in the program editor:<br>* Press F2 to enter the Control menu.<br>* Press 8 to enter the Transfers submenu.<br>* Press 3 to select Cycle.
# The Cycle Command

The `Cycle` command ends the current cycle of a [`68k:For`](68k:for.html)..`EndFor`, [`68k:Loop`](68k:loop.html)..`EndLoop`, or [`68k:While`](68k:while.html)..`EndWhile` loop, as though the corresponding `End` were there. It doesn't exit the loop forever; if the loop would have repeated, it goes back to the beginning. However, if the loop is ready to end (if the counter is equal to the end value, for a `For` loop, or if the condition is false, for a `While` loop), it exits the loop and continues after the `EndFor` or `EndWhile` command.

An example of `Cycle` in a `For` loop:
```
:For num,1,100
: If isPrime(num)
:  Cycle
: Disp num
:EndFor
```

This loop prints all the composite numbers between 1 and 100. Here's how it works: for every number, it first checks whether or not it's prime. If it is, the program goes back to the beginning of the loop with the next number. On the other hand, if the number is composite, the program continues to the `Disp` command, then hits `EndFor` and goes back to the beginning of the loop as well.

If the `Cycle` instruction is inside multiple loops, one nested in the other, it works with the innermost loop.

## Error Conditions



## Related Commands

- [`68k:Exit`](68k:exit.html)
- [`68k:For`](68k:for.html)..`EndFor`
- [`68k:Loop`](68k:loop.html)..`EndLoop`
- [`68k:While`](68k:while.html)..`EndWhile`
