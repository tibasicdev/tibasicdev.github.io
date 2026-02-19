# Logic and Conditions
Most programs don't follow the same sequence of instructions every time. Depending on its input, a program might want to skip certain steps, or to follow alternative steps instead. Or maybe several instructions need to be repeated over and over again, for a certain number of steps or until they produce the right result. The next few parts of this tutorial will focus on **control structures** — instructions that explain which steps the calculator should follow, and in which order.

Conditionals are the simplest control structure there is. The idea is simple: the calculator will check if a condition is true or false, and do entirely different things in each case. Of course, first we need to explain logic: what is true, and what is false.

## Relations

**A note of caution**

The statements in this section are very similar to English, which is good because it makes understanding them easier. But it also leads to errors when they don't work the way you expect them to work. 

**0<X<10** seems okay, but it's not — it actually compares 0<X first, and compares the *result* (0 or 1) to 10, returning the wrong answer. Use **0<X and X<10** instead.


The building blocks of a condition are the relations [=](equal.html), [≠](notequal.html), [>](greaterthan.html), [≥](greaterthanequal.html), [<](lessthan.html), and [≤](lessthanequal.html). They can check if two numbers are equal or test if one is larger than the other. With these commands, the calculator can compute that 2+2=4 is a true statement, but 1<0 is false.

Try some of these yourself! You can find the relations in the [2nd] [TEST] menu (the 2nd function of the MATH button). If you type some true and false statements on the home screen, you'll see something like this:
```
2+2=4
		1
2+2>4
		0
100≤10*10
		1
```

This seems confusing! After all, I said that the calculator checks if a statement is true or false. Where do the numbers 1 and 0 come from? The answer is simple: because the calculator doesn't have separate values for "true" and "false" (which are known as **boolean** variables in other languages), it's forced to use the numbers 1 and 0 for the purpose. In this context, the value 1 means that a statement is true, and the value 0 means that a statement is false.

Of course, in a program, you're probably not interested in checking whether 2+2=4: this check is going to be the same each time you run the program, so there doesn't seem to be a point. More likely, you'll be checking the values of variables, which as I've said can be used in place of numbers. For example, you might want to check if A=1, or if X≤0.

## Logical Operators

Building on relations, we can use logical operators to make more complicated conditions. The four operators are [and](and.html), [or](or.html), [xor](xor.html), and [not(](not.html). You can find them by going to the same [2nd] [TEST] menu where relations were, then pressing the right arrow to go to the LOGIC submenu. 

Three of these operators — and, or, and not( — have clear meanings. X=2 and Y=2 means that both X and Y are equal to 2. X=2 or X=3 means that X is either 2 or 3. not(X=Y) means the opposite of X=Y, which we can also write X≠Y.

Even here, we need to make a clarification. The word "or" has several meanings in English, and despite the similarity between the English word and the logical operator, the operator only uses one of these. Specifically, it uses the "inclusive or": if both parts are true, the whole thing is also true. This matches the English in some uses (if you need to pass math or science to get a diploma, you'll certainly get one if you pass both) but not in others (if the meal comes with soup or salad, you'll probably have to pay extra for both). 

If you *do* mean to describe an "either-or" situation, you'll need the xor operator, which stands for "eXclusive OR". This way, the calculator knows what you mean: if you write X=2 or Y=2, it's okay if both are 2, and if X=2 xor Y=2, only one can be 2.

Like relations, logical operators deal with, and return, 1 and 0 to represent true and false.

## Conditions

In a program, we want to do more than just *check* if a statement is true or false. We want to do different things depending on this check. This is accomplished by several forms of the [If](if.html) command:

### Simple If

```
:If (condition)
:(statement)
```

This simplest form of the If statement imposes a condition on one other line of code. The statement directly after If will be skipped if the condition is false. It works just as it reads: "If X=2:Disp Y" means "If X is 2, display Y".

### If-Then-End

```
:If (condition)
:Then
:(statement1)
...
:(statementx)
:End
```

One step beyond the simple form, this is what you do when several commands (sometimes most of your program) depends on the condition. Just put a Then immediately after the If - then all the statements until you reach an End will depend on the If condition. You can have one If statement inside another, layered as much as you want.

It's traditional to write If (condition):Then on one line, separating them with a colon and not a new line. This makes code easier to read (you don't have to scroll as much) and looks more like other programming languages. Of course, this is purely voluntary.

### If-Then-Else-End

```
:If (condition)
:Then
:(condition is true)
:Else
:(condition is false)
:End
```

The most complicated form of If statement. In this case, an alternative action is provided. If the condition is true, everything between Then and Else is done. If the condition is false, everything between Else and End is done instead. There is no single-statement form for this.

## Example

Here is an example of the If statement in action. We've embellished the program from the previous section to only accept positive numbers as the side lengths of a rectangle. Now, it will still do the same thing if both A and B are positive — but otherwise it will display a message saying "BAD INPUT!" In the next two pages, we'll learn how to do one better, and actually keep asking for the numbers until they're positive.

```
:Disp "ENTER NUMBERS >0"
:Input "FIRST SIDE?",A
:Input "SECOND SIDE?",B
:If A>0 and B>0
:Then
:Disp "PERIMETER:",2A+2B
:Disp "AREA:",AB
:Else
:Disp "BAD INPUT!"
:End
```

### More on the Subject

A more complex look at the implementation of logic can be found at the page on piecewise expressions [here](piecewise-expressions.html).

<center>

|**[<< Input and Output](sk:input-and-output.html)**|**[Table of Contents](starter-kit.html)**|**[Labels >>](sk:labels.html)**|
| --- | --- | --- |

</center>
