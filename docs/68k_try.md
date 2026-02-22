![The Try Command](68k_try/try.png "The Try Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Catches errors that occur in a block of code.|:Try<br> *(block of code)*<br>:Else<br> *(error-catching code)*<br>:EndTry|This command works on all calculators.|2 bytes for Try;<br>2 bytes for Else;<br>2 bytes for EndTry.|
       
### Menu Location
Starting in the program editor:
- Press F2 to enter the Control menu.
- Press 2 to enter the If..Then submenu.
- Press 4 to select Try..EndTry.
       
# The Try Command

The Try command is used to "catch" errors that occur in a block of code. If an error occurs in a Try..EndTry code block, it doesn't display an error message and exit the program. Instead, it records the type of error in the system variable [errornum](68k:system-variables.html#errornum), and jumps to the Else section of the Try..EndTry block.

Here, you have several options. By checking the [68k:errors](68k:errors.html) page, you can test errornum for specific values to find out what kind of error happened. Ultimately, you'll want to use one of two commands:
- [68k:ClrErr](68k:clrerr.html) to cancel the error.
- [68k:PassErr](68k:passerr.html) to display the error message and exit the program, as usual.

Here is an example of Try..EndTry in action:
```
:Try
: UnArchiv var
:Else
: Disp "var is undefined!"
: ClrErr
:EndTry
```

For most errors, Try..EndTry blocks aren't the way to go because you want to prevent them in the first place. They are a good way to handle special cases or circumstances out of your control. Here are two situations you might use Try..EndTry in:
- If your program uses external variables, you might surround that part of the code in a Try..EndTry block, rather than do all the tests to make sure they are unlocked, unarchived, etc.
- If your program requires specially-formatted input, instead of sanity checking it first you might let the program take untreated input, and catch the errors that result from an incorrect format.

## Error Conditions

**[290 - EndTry is missing the matching Else statement](68k:errors.html#e290)** happens when the Try..EndTry block doesn't contain an Else.
**[490 - Invalid in Try..EndTry block](68k:errors.html#e490)** happens when ??.

## Related Commands

- [68k:If](68k:if.html)
- [68k:ClrErr](68k:clrerr.html)
- [68k:PassErr](68k:passerr.html)

## See Also

- [68k:Errors](68k:errors.html)
