# What Is Optimization
Simply put, optimization is making your game better.  It involves reviewing all of your code and looking for subtle changes that can be made, that as a whole, decrease the size of your program and speed it up.

### Simple optimizations
There are many ways you can optimize a program.  This is a common optimization.
```
:Output(1,1,A-(B-C))
```
can be optimized to
```
:Output(1,1,A-B+C
```
because subtracting a negative is the same as adding a positive, and because parentheses are not needed at the end of any Output( command or other command where the last token on the line is the parentheses.  Another common optimization is quotation marks, which also can be omitted from the end of the Output command.  For an example, see the following.
```
:Output(1,1,"HELLO WORLD")
```
can be
```
:Output(1,1,"HELLO WORLD
```

### Complex optimizations
Optimizing isn't always easy.  Sometimes, to make programs smaller, one has to scrap previously written code and completely rewrite the program with a different approach.  This would be like saying "hey, my program is getting pretty big.  I wonder what would happen if I used lists instead of matrices for my saved games?" and then writing the game using lists instead of matrices.  This is known as algorithmic optimization, but that's a bit too in depth for a beginner class.  If you do wish to know more about it, you can see it [here](algorithmic-optimization.html).

Don't be worried.  Optimizing is usually a fun process, and as you watch that byte count dwindle, you'll see what we're talking about.


<center>

|**[<< Sample Program: Analog Clock](sk:math-sample.html)**|**[Table of Contents](starter-kit.html)**|**[Displaying Text >>](sk:displaying-text.html)**|
| --- | --- | --- |

</center>
