# Loops Optimization
Loops have various uses (we'll see them later), but basically loops are blocks of code that execute themselves a defined number of times. As you know there are 3 types of loops: the [For(](for.html) loop, the [While(](while.html) loop, and the [Repeat(](repeat.html) loop. These are very handy since your program ends when it reaches the end of the code, so if you are developing a game or so you need the code to flow correctly and execute over and over (for example for checking if you pressed a key and making your character walk).


## 101 Uses for Loops

While loops may not have exactly 101 uses, they are some of the most spectacular pieces of code that enable iterations to be made so that a game can constantly update itself or so a math program can perform a specific algorithm.  The uses below represent only a few of the ways loops can be utilized.

### Time Delay

A loop can be seen by many perspectives but if you think that each instruction takes time to be processed you can think (correctly) that each loop takes time to execute its code even if it is an empty loop. Watch the following example:

```
:For(A,1,10)
:End
```

As you can see, there's nothing inside that [For(](for.html) loop but it still takes time to be executed. So you can use a For( loop as a method of making your program sleep. Think of this as a timed [Pause](pause.html) that delays certain parts of the program. Later you'll see an application of this use.

**Note:** The use of [rand](rand.html) can also achieve a time delay, and is considerably smaller.  The only difference is that rand will update [Ans](ans.html), while this loop method will not.

### Game Iterations

Take a look at this example:

```
:Repeat K=21
...
Game instructions...
...
:End
```

In this case, the program will wait until the user presses the 2nd key, represented by K, otherwise it will keep the game running. You can include key press checkers, character movement, etc.  See the next example:

```
:Repeat Ans=45
:A+sum(ΔList(Ans={25,34→A
:B+sum(ΔList(K={24,26→B
:getKey→K
:End
```

This loop is used to iterate a particular game function, in this case updating the coordinates of an object (A,B).  Under certain conditions, it is actually beneficial to use the [getKey](getkey.html) as the last line of the code so that in the loop condition, Ans can be used, which may help speed the loop up.

### Drawing

Because loops execute instructions over and over with different numbers, they can be used to draw. Just watch:

```
:For(A,5,50
:Pxl-on(25,A
:End
```

This will draw a horizontal line between pixel 5 and pixel 50 and because of the way loops work, it will look like it is actually being drawn by somebody.  This is different from using the [Line(](line.html) command, which makes the line appear instantaneously.  Rather, this block writes each pixel one at a time, starting with (25,5), then (25,6), and so on.  The next code block uses two loops together:

```
:For(A,5,50
:For(B,5,50
:Pxl-on(A,B
:End
:End
```

This code will draw a square.  This time, when one line is drawn, the next line begins to be drawn, until each row is complete.

### Write Text

Writing text is relatively simple on the calculator.  However, the calculator does it without any animation.  Try the following code:

```
:ClrDraw
:"HELLO WORLD
:For(A,1,length(Ans
:Text(5,4A+5,sub(Ans,A,1
:End
```

This will write out each letter one at a time, as if it were being typed.  The [For(](for.html) loop runs though each character in the string (which is Ans), and for each one, it types the letter in the next slot.  However, this code is too fast.  What other tool do we have...

```
:ClrDraw
:"HELLO WORLD
:For(A,1,length(Ans
:For(B,1,30
:End
:Text(5,4A+5,sub(Ans,A,1
:End
```

We can use the time delay from before!  Using a For( loop, we can delay the program every iteration and thus overall slow down the process.  Since we require Ans not to be updated, the For( loop delay works perfectly.

**Challenge:** Can you make a code that does the same as the above, but smaller?

## Tips

Try to not nest loops in a game. "What is a nested loop?" you may be asking: a nested loop is a loop inside a loop, for example:

```
:WHILE A=2
:REAPEAT B=2
:FOR (C,1,10)
:END
:END
:END
```

Sometimes they are the only way of doing things, like checking all the screen for on pixels or whatever, but if you want to execute the same instruction 5 times in a game, do it like this:

```
:1->A
:WHILE A=2
Game instructions...
:IF A>6:THEN
Your instructions
:A+1->A
:END
:END
```

And not:

```
:WHILE A=2
Game instructions...
:FOR (A,1,5)
Your instructions
:END
:END
```

Why? Because if you did so, you wouldn't be executing any instructions (like character walking or so) besides what's in the For( loop and your game flow would be ruined...

Have fun with loops!!

<center>

|**[<< Conditionals](sk:conditionals.html)**|**[Table of Contents](starter-kit.html)**|**[Optimization: The Graph Screen >>](optimize-graph.html)**|
| --- | --- | --- |

</center>
