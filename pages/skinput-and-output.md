# Input and Output
So far, we can write a calculator program that will make certain computations with numbers or variables and stop — this is just like doing math on the calculator normally. But this is really not that useful! We want the program to be able to ask you a question and give you an answer: to let you "talk" to the program when it's running, so to speak.

In programmer language, we call this input and output. Input happens when a program lets the person running it press a key or type something in, so that it can do something with that. Output happens when a program displays results on the screen.

Since these are fairly essential ideas, there are a lot of commands associated with them. We'll begin with two: [Input](input.html) and [Disp](disp.html). Unlike storing to variables, these commands can only be used in programs. To type them, open a program to edit. Press PRGM to get the menu of program commands, and the right arrow key, to select I/O (short for Input/Output). The very first option is Input, and the third is Disp.

A short synopsis of what they do:


[[row]]


## Input

:Input *var* (where *var* can be replaced by any of the variables we've learned about) will pause the program to display a question mark, and let the calculator user type in a number. Then, the number will be stored to *var*, and the program will resume.

A note on the Input command — to make things more fancy, you can add some text (in quotes as usual) before the variable name. Then, this text will replace the question mark. Input A just displays a generic ? with no help on what it might mean. Input "A=",A will display A= which gives some indication of what to type.

[[/cell]]


## Disp

:Disp *whatever* will display *whatever*, which can be nearly anything: a number, a variable, a formula involving numbers or variables or both, and even text. 

A note on the Disp command — to display text, put it in quotes (ALPHA and + make a quote symbol). If you were to just type Disp COOL, the calculator will think you mean the product of C, O, O, and L. By putting it in quotes, Disp "COOL", you tell the calculator that something is text. You can display several things at once, by adding commas: Disp "NUMBER",5 will first display the text NUMBER and then the value 5.

[[/cell]]
[[/row]]
[[/table]]

## What can we do with this?


**Text entering tips**

You can use math symbols to enter fancier characters than just uppercase letters.
- [MATH][LEFT][4] (factorial) to type !
- [2nd][ANGLE][2] (minutes) to type '

See [this page](hexcodes.html) for a program that will allow you to use lowercase letters.


With these tools, we can touch on one of the key uses of programming: simplifying repetitive tasks. Say you have 50 math problems which all look the same: given the sides of a rectangle, find the perimeter and area. Outside a program, you'd have to type out the calculations each time. With a program, you can let the calculator do that for you:

```
:Input "FIRST SIDE?",A
:Input "SECOND SIDE?",B
:2(A+B)→P
:Disp "PERIMETER",P
:Disp "AREA",AB
```

This is our first useful program, so let's go through it line by line: 
1. Input "FIRST SIDE?",A will display the text FIRST SIDE? and let the user type in a number. This will be stored to A (the variable we use to represent the first side of the rectangle). 
1. Similarly, Input "SECOND SIDE?",B will display SECOND SIDE? and let the user type in a number to store to B, representing the second side of the rectangle.
1. 2(A+B)→P stores the result of 2(A+B) to a new variable, P. 2(A+B) is the formula for the perimeter of a rectangle.
1. Disp "PERIMETER",P displays the text PERIMETER and then the value of P (which will be a number representing the perimeter of the rectangle)
1. Disp "AREA",AB is similar, but does two things at once. After displaying the text AREA, it computes the value AB (the area), and immediately displays it.

Of course, we could have handled perimeter the same way we handled area, Disp "PERIMETER",2(A+B). This would have let us combine two lines into one. However, the way the program is now, if the value of the perimeter is ever needed again (should we make the program longer), P will save it for the future as well.

### More on the Subject

A wider look at the area of input and output can be found at [this](userinput.html) page.

<center>

|**[<< Variables](sk:variables.html)**|**[Table of Contents](starter-kit.html)**|**[Logic and Conditions >>](sk:logic.html)**|
| --- | --- | --- |

</center>
