![The © Command](68k_comment/comment.png "The © Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Marks the rest of the line (in a program) as a comment.|://line of code* © *comment//|This command works on all calculators.|4 bytes (+ length of comment)|
       
### Menu Location
Starting in the program editor:<br>* Press F2 to enter the I/O menu.<br>* Press 9 to select ©.
# The © Command

The © character is used for adding comments in a program: everything after © is ignored by the calculator for the purposes of actually running the program, so it's a good way to make a note to yourself about what a part of your code does. This is especially helpful if you're going to be reading the program later when you don't quite remember what you were doing.
```
:If ok=0 © If the user pressed ESC
: Stop
```

There are other situations you might use comments in. For instance, you might make a rough sketch of your program and add comments about the code that has yet to be filled in:
```
:If key=264 Then
: © add a confirmation dialog here later
: Exit
:EndIf
```

Yet another use of © is to "comment out" lines of code that you might need later, but want to ignore for now — this is better than deleting the code, since you don't have to rewrite it later. 

## See Also

- [68k:comments](68k:comments.html)
