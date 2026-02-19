![The Archive Command](68k_archive/archive.png "The Archive Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Moves a variable from RAM to the archive.|Archive *variable*, [*another*, ...]|This command works on all calculators.|3 bytes|
       
### Menu Location
Starting in the program editor:<br>* Press F4 to enter the Var menu.<br>* Press 8 to select Archive.
# The Archive Command

The `Archive` command moves a variable, or several variables, from RAM to the archive. This serves two purposes:
- More RAM is now available for other variables.
- The variable is protected from being edited or deleted.

On the 68k series of calculators, a variable in the archive can still be read (compare this to the behavior of TI-83 series calculators, where doing anything at all to an archived variable is forbidden). However, trying to store anything to the variable will give an error: it must be unarchived first. 

Variables in the archive are also protected from being deleted. This means that a [`68k:DelVar`](68k:delvar.html) command called on it will cause an error. Commands such as [`68k:NewProb`](68k:newprob.html) or [`68k:DelType`](68k:deltype.html) that delete multiple variables will skip over any that are archived. Finally, in the event of a RAM clear (which is more likely to happen by accident than a total memory clear), archived variables will be preserved.

Any type of variable can be archived. However, you cannot archive [68k:system variables](68k:system-variables.html) (such as xmin) or variables beginning with _.

## Advanced Uses

It seems natural to archive programs, since they usually aren't written to, and they are valuable enough that you want to give them some protection. However, keep in mind that the first time you run a program after editing it, it gets [tokenized](68k:tokenization.html) — the text is converted into tokens that stand in for commands. The process might take several seconds.

If you edit a program and then immediately archive it, it is "protected" from this conversion process. That means that *every* time you run the program, it will be tokenized. To avoid this, run the program once to tokenize it, and then archive it.

## Error Conditions





## Related Commands

- [`68k:Unarchiv`](68k:unarchiv.html)
- [`68k:DelVar`](68k:delvar.html)
- [`68k:Lock`](68k:lock.html)
