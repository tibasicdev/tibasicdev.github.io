![Func ... EndFunc Block](68k_func/func.png "Func ... EndFunc Block")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Defines a set of lines as executable program code.|Func<br>*function code*<br>EndFunc|This command works on all calculators.|4 bytes|
       
### Menu Location
Press:
1. Catalog ([2nd] + 2 on 92/+/v200) to access the catalog menu
2. F to scroll to the F section
3. Use arrows to navigate to Func
Or type Func using the keyboard
       
# Func ... EndFunc Block

This command is used at the beginning/end of a function to tell the calculator to interpret it as code. Without these commands at the start and end of a function, the interpreter will pass a syntax error. Note that unlike Programs, functions cannot write to the screen, so there can be no IO commands or Draw commands. In addition, you cannot edit global variables in Functions, so you have to declare a variable as local using [68k:Local](68k:local.html) before initializing them. However, the reason you may want to use functions instead of programs is that unlike programs, you can return a value from a function. You can either use the [68k:Return](68k:return.html) command, or the function will return whatever the last value was before you quit the function.

```
:test()
:Func
://code to run goes here
:EndFunc
```

## Advanced Uses

Using the [68k:local](68k:local.html) and [68k:define](68k:define.html) commands, you can create local submethods in your programs. Assuming the following code is inside a program block already, the syntax would be:

```
:Local test
:Define test()=Func
://function code goes here
:EndFunc
```

## Related Commands

- [68k:Prgm](68k:prgm.html) / [68k:endprgm](68k:endprgm.html)
- [68k:expr(](68k:expr.html)
