![The Lbl Command](68k_lbl/lbl.png "The Lbl Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Marks a point in the program for use with [68k:Goto](68k:goto.html) and [68k:Toolbar](68k:toolbar.html)..EndTBar.|:Lbl *label-name*|This command works on all calculators.|2 bytes (plus 1-10 bytes for label name)|
       
### Menu Location
N/A

# The Lbl Command

The Lbl command is used to mark a point in the program to which the [68k:Goto](68k:goto.html) command or selections from a [68k:Toolbar](68k:toolbar.html)..EndTBar menu can jump. When jumping to a label, the calculator will start searching the program from the beginning to find the label.

The same limitations are imposed on a label name as on a [variable name](68k:variable-names.html). It's okay to have a label with the same name as a variable, though, this won't cause problems.

You can, theoretically, have labels in the same program with the same name, but only the first one will be used (the calculator will always find it before it finds the others). Labels don't extend beyond a program: you can't jump to a label inside a different program or function. 

Also, the code inside an [68k:expr()](68k:expr().html) string lives in its own program as far as labels are concerned: if you put a label in it, the main program won't find it; you can't jump out of a routine run with [68k:expr()](68k:expr().html) into the main program; finally, you don't have to avoid the label names that the main program uses.

## Error Conditions



## Related Commands

- [68k:Goto](68k:goto.html)
- [68k:Toolbar](68k:toolbar.html)..EndTBar
