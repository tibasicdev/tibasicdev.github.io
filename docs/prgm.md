![The prgm Command](prgm/PRGM.GIF "The prgm Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Calls another program from within a program, with program execution moving to that program.|prgm*NAME*|TI-83/84/+/SE|1 byte|

### Menu Location
Outside the editor, press:
1. PRGM to enter the PRGM menu
2. Use arrows to choose program

When editing a program, press:
1. PRGM to enter the PRGM menu
2. LEFT to enter the EXEC submenu
3. select a program
       
# The prgm Command

The prgm command is used to execute a program from inside another program (at any time while the program is running), with the secondary program acting as a [subprogram](subprograms.html) for that program. Although they are listed in the program menu and can be executed independently like any other program, subprograms are primarily designed to do a particular task for the other program.

You insert the prgm command into the program where you want the subprogram to run, and then type (with the alpha-lock on) the program name. You can also go to the program menu to choose a program, pressing ENTER to paste the program name into your program.

```
PROGRAM:MYPROG
:ClrHome
:Output(3,3,"Hello
:prgmWHATEVER
```

When the subprogram name is encountered during a program, the program will be put on hold and program execution will transfer to the subprogram. Once the subprogram is finished, program execution will go back to the program, continuing right after the subprogram name.

Although subprograms can call themselves or other subprograms, this should be done sparingly because it can cause memory leaks if done too much or if the subprogram doesn't return to the parent program.

[Branching](goto.html) is local to each program, so you can’t use Goto in one program to jump to a Lbl in another program. In addition, all [variables](variables.html) are global, so changing a variable in one program affects the variable everywhere else.

## Advanced Uses

Each time you call a TI-Basic program, 16 bytes are used to save your place in the original program so you can return to it correctly. This is a small enough amount that you don't have to worry about it, unless you're low on RAM or use a lot of recursion.

## Error Conditions

- **[ERR:ARCHIVED](errors.html#archived)** if the program is archived.
- **[ERR:SYNTAX](errors.html#syntax)**, with no 2:Goto option, if the program is an [assembly](assembly.html) program.
- **[ERR:UNDEFINED](errors.html#undefined)** if the program doesn't exist.

### See Also

- [Subprograms](subprograms.html)
- [Branching](goto.html)
- [Variables](variables.html)
