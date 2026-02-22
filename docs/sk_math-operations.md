# Math Operations
|This article is currently in development. You can help TI-Basic Developer by expanding it. Add more pertaining to division, exponentiation, and negation/subtraction|
| --- |

Optimizing math operations is a great way to make your programs more understandable and faster.

## Simple Things
When optimizing any code in TI-Basic, you should check to see if your math is done efficiently.  For instance, think of a situation where you need to multiply A by 7 and B by 4 and then multiply A and B.  Remembering that multiplication doesn't care about order, wouldn't it be easier to just multiply 28 by A and multiply that by B? Here is is how that would look.
```
:7*A*4*B
```
works better as
```
:28*A*B
```
Now, remember that when you multiply variables with numbers on a calculator, it implies the multiplication.  The same is true when multiplying variables together, but you have to do the multiplication yourself between two real numbers.  This is what the previous code would look like with implied multiplication.
```
:28AB
```
As stated before, an important part of optimization is combining real numbers in your code..  Whenever you see two lone real numbers, combine them.  For instance, don't ever write a program with A+1+3+5 in it.  Write A+9, and save us some space. 
Also, when you have an equation like 9*(X+3), it is better to distribute the nine than to leave the equation factored, because it saves the calculator a multiplication step which helps speed and size.  This is something that should be done as a speed optimization when 9 is replaced with a one, two, or three digit number, and as a size optimization when 9 is replaced with a one or two digit number.
Another simple optimization trick is instead of multiplying by, say, 1000, just use E3 (the 'E' when [2nd][,] is pressed) Or use 10^x token under [2nd][LOG].

## Complex Math Optimizing
Remember Polynomials? I know you do.  Imagine the polynomial p(X)=(X+1)(2X+3), which takes 11 characters to write.  I know you're wondering "why on earth are we talking about polynomials?  I hate those!"  But optimizing them when used is an important step.  Notice that when expanded, p(X)=2X<sup>2</sup>+5X+3 is only 8 bytes, instead of 11.  Because expanding a polynomial removes the implied multiplictation necessary for the calculator to do previously, it not only is better size-wise but improves the speed of your program.

<center>

|**[<< Optimizing Variables](optimize-variables.html)**|**[Table of Contents](starter-kit.html)**|**[Logic Operations >>](sk:logic-operations.html)**|
| --- | --- | --- |

</center>
