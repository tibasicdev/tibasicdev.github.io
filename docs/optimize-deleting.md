# Optimization: Deleting Variables
Instead of setting number variables to zero (to delete them), use the [DelVar](delvar.html) command. DelVar works with all of the variables, and the calculator automatically sets the variable to zero the next time it's used. However, DelVar is also slightly - so for repeated resetting, it is often faster store 0 to the variable.

```
:0→A
can be
:DelVar A
```

The DelVar command doesn't need a line break or colon following the variable name. This allows you to make chains of variables.

```
:DelVar A
:DelVar B
can be
:DelVar ADelVar B
```

Besides making chains of variables, the DelVar command also allows you to take the command from the next line and put it immediately after the last DelVar command.

```
:DelVar A
:Disp "Hello
can be
:DelVar ADisp "Hello
```

The only exception is with the [Lbl](lbl.html) command. Don't put the Lbl command immediately after a DelVar with this optimization, or else the label will be ignored. For instance, the following code exits with [ERR:LABEL](errors.html#label):
```
:DelVar ALbl 0
:Goto 0
```

Even though the [ClrList](clrlist.html) command exists for clearing lists, DelVar should be used instead.

```
:ClrList L1
can be
:DelVar L1
```
There is a drawback to using Delvar for Lists. If you use Delvar L1 instead of ClrList L1, L1 will disappear from the list editor. This can easily be remedied outside of the program, but inexperienced calculator users who execute your program and then need to view the list that was used by your program may not know how to do this. 
Furthermore, ClrList L1 is 1 byte smaller than Delvar L1.
