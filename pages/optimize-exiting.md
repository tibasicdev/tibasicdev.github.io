# Optimization: Exiting Programs
Although the Return and Stop commands can both be used for exiting programs, Return should be used instead of Stop. While Return stops only the current program and allows the parent program to continue running, Stop causes all of the programs to stop and then returns the user to the homescreen (unless called from an Assembly program).

```
:ClrHome
:Disp "Hello
:Stop
can be
:ClrHome
:Disp "Hello
:Return
```

You don't have to use Return or Stop if you can organize the program so that it just naturally quits. If the calculator reaches the end of a program, it will automatically stop executing.

```
:ClrHome
:Disp "Hello
:Return
can be
:ClrHome
:Disp "Hello
```

When you have a display command that displays text as the last line of the program, you can remove the command and just put the text. This text will be displayed instead of the "Done" message that is normally displayed after a program finishes executing.

```
:ClrHome
:Disp "Hello
can be
:ClrHome:"Hello
```

Even though you don't display any text as the last command, you may still want to get rid of the "Done" message. You can do this by putting a single double-quote as the last line of the program.

```
:ClrHome
can be
:ClrHome:"
```

If you modify the Ans variable on the last line of the program, Ans's new value will be displayed instead of the "Done" message.

```
:ClrHome
:For(A,1,5
:B+A→B
:End
can be
:ClrHome
:For(A,1,5
:B+A→B
:End
:B
```
