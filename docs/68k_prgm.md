![The Prgm...EndPrgm Command Block](68k_prgm/prgm.png "The Prgm...EndPrgm Command Block")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Defines a set of lines as executable program code.|Prgm<br>*program code*<br>EndPrgm|This command works on all calculators.|4 bytes|
       
### Menu Location
Press:
1. Catalog ([2nd] + 2 on 92/+/v200) to access the catalog menu
1. P to scroll to the P section
1. Use arrows to navigate to Prgm
Or type Prgm using the keyboard
       
# The Prgm...EndPrgm Command Block

This command is used at the beginning/end of a program to tell the calculator to interpret it as code. Without these commands at the start and end of a program file, the interpreter will pass a syntax error.

```
:test()
:Prgm
://code to run goes here
:EndPrgm
```

## Advanced Uses

Using the [68k:local](68k:local.html) and [68k:define](68k:define.html) commands, you can create local submethods in your programs. This is more often used with functions, as you can return a value, however you can not display to the IO or draw to the graph screen in functions, so using programs in this way is sometimes useful. Assuming the following code is inside a program block already, the syntax would be:
```
:Local test
:Define test()=Prgm
://test program code goes here
:EndPrgm
```

## Related Commands

- [68k:func](68k:func.html) / [68k:endfunc](68k:endfunc.html)
- [68k:expr(](68k:expr.html)
