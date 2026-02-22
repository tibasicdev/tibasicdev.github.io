# Numbers Menu
One of the most prominent features of the calculator is the Numbers Menu.  This menu has many useful commands that can help ensure the cleanness of numbers, and they help with identifying list elements.  Most programs use at least one of the commands in the numbers menu.


## abs(

The [abs(](abs.html) command simply finds the absolute value of a number.  That is, it finds how many units away from zero a number is.  So, the `abs(5)` is 5, and the `abs(-5)` is also 5.  For programmers, this command means that any expression within an abs( will always be positive.

How is this command useful?  Well, this command will make sure you have an expression that is always positive.  It also allows for a check for two numbers.  Since an equation with absolute value will give two answers, you can check for two solutions within a condition simultaneously.  Observe the code for a condition.
```
:If K=21 or K=105
```
Using simple algebra and the abs( value command, we can actually solve for both with one equation.  Find the median of the two numbers by finding their difference and dividing by two.  (105-21)/2=42.  Now, subtract that value from the larger number.  105-42=63.  Now, if you add the 42 to the smaller number, you should also get 63.  Now, using our rules about abs(, we can apply the numbers 63 and 42 to the conditional.
```
:If abs(K-63)=42
```

## round(

The [round(](round.html) command will round a number to a specified decimal point.  This command works well when you need a number to be a certain length.   It also prevents rounding errors such as accidentally getting 3.0000000000012.  This can cause domain errors, so it is sometimes better to use round( in case of irrational numbers.

## iPart( and fPart(

[iPart(](ipart.html) and [fPart(](fpart.html) are very important commands when used together.  iPart( takes the integer part of a number, where fPart( takes the fraction part.  When together, you can compress the information of a coordinate into one number rather than two.  This helps a lot with multiple objects that require moving.

Let's say that you want to store the coordinates of five different points.  The points are in pixel format: (3,40), (24,9), (33,60), (12,22), and (50,20).  You could store the points in 10 different real variables, which takes 180 bytes of memory.  You could also store the 10 numbers in a list for 102 bytes.  Or, with iPart( and fPart(, you make a 5 element list for 57 bytes, which is a lot smaller and easier to manage.

Store the first coordinate part (the *y* part) as an integer.  Then, put a decimal point and have the *x* part as the number after the decimal.  So, point (3,40) becomes 3.4, the point (24,9) becomes 24.09, and the point (33,60) is 33.6.  Store it into L<sub>1</sub> so that L<sub>1</sub> becomes {3.4, 24.09, 33.6, 12.22, 50.2}.  So, how do you turn 12.22 into (12,22)?
```
:Pxl-On(iPart(L₁(4)),100fPart(L₁(4)))
```
So, this code takes the integer part of the number and makes that the *y* part.  Then, it takes 100 times the fraction part (to make it an integer) and makes it the *x* part.  Now, you end up with Pxl-On(12,22).

How can you change it back?  Simply retract the values and add them together.
```
:12+.01(22)→L₁(4)
```

## int(

The [int(](int.html) command is very similar to iPart(.  int( also finds the integer part, but it does so differently.  iPart( simply gets the integer part, whereas int( simply rounds the number down.  This only causes difference with negative numbers, where `iPart(-5.5)` yields -5, and `int(-5.5)` yields -6.

int( is commonly used to turn non-integers into integers.  It is good to use this command if you want to ensure a number to not be fractional, such as when dealing with dimensions or coordinates.  For example, if you have a variable, X, that represents the X location of an object and in the calculation, you divide by two, you will want to use int( so that the X doesn't have .5.

```
:X/2
:Pxl-On(12,Ans)
should be
:int(X/2
:Pxl-On(12,Ans)
```

## min( and max(

These commands are very commonly used.  You probably recognize them from the [sk:movement](sk:movement.html) section.

[min(](min.html) finds the minimum value of two numbers or a list of numbers.  [max(](max.html), on the contrary, finds the maximum value.  These commands are used as boundary checks for movement.
```
:min(16,max(1,B+sum(ΔList(K={24,26}))))
```
If the new value of `B+sum(ΔList(K={24,26}))` is less than 1, then `max(1,0)` will yield 1.  If it is greater than 16, then `min(16,17)` yields 16.  It never passes the boundary.

min( and max( can also be used to shorten a huge list of conditionals.  For example:
```
:If A=21 or A=105 or A=45 or A=24 or A=26 or A=25 or A=34
```
Hmm, this can be shortened.  min( and max( also find the minimum and maximum in lists.  So, the `min({1,0,1,1,0})` is 0.  `max({1,0,1,1,0})` gets 1.  Here is how it works.
```
:If max(A={21,105,45,24,26,25,34})
```
So, let's say A is 25.  That means we get `max({0,0,0,0,0,1,0})` which is 1.  `If 1` is true, so it works.  If A was 56, then we get `max({0,0,0,0,0,0,0,0})` which is 0.  `If 0` is false, so the next command is skipped.

If you have a large list of [or](or.html), replace with max(.  If you have a bunch of [and](and.html)'s, replace with min(.

<center>

|**[<< Operators](sk:operators.html)**|**[Table of Contents](starter-kit.html)**|**[Powers and Exponentials >>](sk:powers-exponentials.html)**|
| --- | --- | --- |

</center>
