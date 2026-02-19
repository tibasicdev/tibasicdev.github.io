# Memory Leaks
One of the most frequently tossed around phrases in the TI-Basic community is memory leaks. But what is a memory leak, and why are they so important? Simply put, a memory leak is where you use a [`Goto`](goto.html)/[`Lbl`](lbl.html) within a [loop](while.html) or [`If`](if.html) conditional (anything that has an [`End`](end.html) command) to jump out of that control structure before the `End` command is reached:

```
:Lbl A
:While 1
:Goto A
:End
```

This in itself wouldn't necessarily be a bad thing, except that the calculator stores all of the `End` commands on its built-in operator stack. Each `End` command takes up a little bit of memory (like a dozen bytes or so), and when the calculator reaches the `End` command for the associated loop/conditional, it not only removes it from the stack, but also returns that memory back to the calculator.

However, if you jump out of a control structure, you never allow the calculator to remove the `End` from the stack, and it subsequently keeps the memory. Since the operator stack is stored in RAM, each additional memory leak further depletes the calculator's memory, until you eventually reach the point where the calculator runs out of memory (giving you the dreaded [ERR:MEMORY](errors.html#memory) error).

Most people would probably not have a problem with this, and still use memory leaks just with some caution, but there is one important caveat of memory leaks: the program will gradually slow down over time. This problem is actually caused by TI's faulty programming, where the calculator loses track of some of the bytes associated with the `End` command in the operator stack.

It should be said that memory leaks are only a problem while the program is running. If a program is ended the leak is cleared and will cause no further issues.

It should be noted that this problem only afflicts the TI-83/84 series of graphing calculators; [68k TI-Basic loops](68k:goto.html) have offsets linking the end to the beginning, so the program doesn't need to keep a stack to be aware of what to do with End instructions.

Keep in mind that some code structures do not result in memory leaks. For example, the following code will not memory leak nor will it slow down. (The code has been indented purely for readability.

```
While 0
  Lbl 1
  Disp "1
End
While 1
  Disp "0
  Goto 1
End
```

This is due to the `Lbl` and `Goto` being on the same indent level. The token interpreter expects the same amount of `End`'s after the `Lbl` and `Goto`. If one of the [`While`](while.html) loops were missing, the code would memory leak.
