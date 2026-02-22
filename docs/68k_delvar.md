![The DelVar Command](68k_delvar/delvar.png "The DelVar Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Deletes a variable or variables.|DelVar *var1*[,*var2*,...]|This command works on all calculators.|3 bytes|
       
### Menu Location
Starting in the program editor:
- Press F4 to enter the Var menu.
- Press 2 to select DelVar.
       
# The DelVar Command

The `DelVar` command deletes variables from existence, making them undefined again. This is a good way of [cleaning up](68k:setup-and-cleanup.html) at the end of a program, or of making sure that a variable is undefined before you use it in a symbolic expression. 

For `DelVar` to work, the variable must not be [archived](68k:archive.html) or [locked](68k:lock.html). It also doesn't work on any program that's currently running, or on system variables.

There are two commands which might be a better alternative to `DelVar`, however. [`68k:NewProb`](68k:newprob.html) deletes all 26 one-letter variables at once; however, it also clears things like the graph screen that you might want to see preserved. Declaring a variable as [`68k:Local`](68k:local.html) at the beginning of a program prevents you from needing to delete it afterward, and it also makes sure you don't overwrite any existing variables.

Newer calculators have a [`68k:DelType`](68k:deltype.html) command to delete all variables of a certain type (provided they're not locked or archived). This is risky: you'll almost certainly delete too much. It's better to use `DelVar`, even if you have to list a hundred variables to do it.

## Advanced Uses

Assembly programs might allow you to "hide" programs (or other variables) from the variable menu. This is actually done by marking the variable in question as "in use", the way a currently-running program is marked. As a result, you won't be able to delete a hidden variable, and trying to will give the "Variable or Flash application in use" error.

## Error Conditions

**[140 - Argument must be a variable name](68k:errors.html#e140)** happens when trying to delete something that isn't a valid variable name.
**[450 - Invalid in a function or current expression](68k:errors.html#e450)** happens when DelVar is used in a function.
**[870 - Reserved name or system variable](68k:errors.html#e870)** happens when trying to delete a system variable.
**[970 - Variable or Flash application in use](68k:errors.html#e970)** happens when trying to delete a currently running program.
**[980 - Variable is locked, protected, or archived](68k:errors.html#e980)** happens when trying to delete a locked or archived variable.

## Related Commands

- [`→`](68k:store.html)
- [`68k:Define`](68k:define.html)
- [`68k:DelType`](68k:deltype.html)
- [`68k:NewProb`](68k:newprob.html)

## See Also

- [68k:setup-and-cleanup](68k:setup-and-cleanup.html)
