# Good Programming Practices
If you haven't read [Your First Program](68k:sk-firstprog.html) yet, I recommend you do so first.

### Indentation
Whenever you write TI-Basic code, you should make sure it's readable. This will help both yourself and others in the future. One way to make your code more readable is to use indentation. Indentation is important because it allows you to easily see when one block of code ends and the next begins. Squashing all your code together with no indentation can make it hard to read.

Indentation is usually done with one space per level. The calculator keeps track of how many spaces begin a line, so they will survive being tokenized. When you begin a block, such as If, or Loop, or While, you add a level of indentation to lines after it, and remove it when you reach an 'End', such as 'EndIf', 'EndLoop', or 'EndWhile'. Here's an example of good indentation:

```
:indtexmp()
:Prgm
: © Prgm begins a block, so the rest of the code is indented
:
: Loop © Loop also begins a block, so add an indentation level
:  If getKey()=13 Then
:   Exit
:  EndIf
:
:  Disp "Hello, World!"
: EndLoop © EndLoop ends the block, so remove the indentation level
:EndPrgm © EndPrgm is not indented at all
```

Indentation is going to be hard to maintain on a real calculator, or in many TI-Basic editors, since it isn't too common in the TI-Basic community. However, it will be worth it when you're working on a large program. Notice the blank lines before and after blocks like Loop. Like indentation itself, it is entirely optional and it only assists in reading the code. Here's an example of no indentation:

```
:noindent()
:Prgm
:Loop
:If getKey()=13 Then
:Exit
:EndIf
:Disp "Hello, World!"
:EndLoop
:EndPrgm
```

This is a simplified example. Imagine an application with 10 or 15 nested If statements, each with their own Else and ElseIf statements. Now imagine needing to put code inside a specific If. You will most likely need indentation to keep track of where to put the code, or you might just sit there for a while trying to make sense of all those nested Ifs!

It should be clear that indentation isn't required. Most members of the community don't use it for their programs, maybe because it increases program sizes, or because it's cumbersome to maintain. Maybe it just isn't worth the effort. You should decide whether indentation is for you. You could indent because it makes code more readable, or even just because you're used to indenting code. To indent, or not to indent? That is the question, and the reasoning for your answer is up to you.

### Commenting

### Variable Naming

<center>

|**[<< Your First Program](68k:sk-firstprog.html)**|**[Table of Contents](68k:starter-kit.html)**|**[Setting up your 68k calculator >>](68k:sk-calculator.html)**|
| --- | --- | --- |

</center>
