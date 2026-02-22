# TI-Basic Bugs
This is a list of the bugs that have been discovered in TI-Basic when using the different commands. These bugs appear on their respective command pages as well, but are placed here together for sake of completeness (that way you don't have to go hunting around the site).

### Using String►Equ(

The [String►Equ(](string-equ.html) command is supposed to store the contents of a string to an equation variable (such as Y<sub>1</sub> or X<sub>1T</sub>). In practice, however, this command is completely useless. This is because the [→](store.html) (store) operation can be used for the same purpose:

```
:String►Equ(Str1,Y1
can be
:Str1→Y1
```

This replacement is universal, takes the same time to run (because it actually uses the same routines), is more convenient to type since you don't have to go through the command catalog, and is several bytes smaller.

### Using DelVar

If [DelVar](delvar.html) is used in a [For(](for.html) loop to delete the counter variable, or used to delete the variable and/or value in the [IS>(](is.html) or [DS<(](ds.html) commands before using them, it will cause an [ERR:UNDEFINED](errors.html#undefined) error.

Another bug when using DelVar is with its chaining of variables functionality: the DelVar command also allows you to take the command from the next line and put it immediately after the DelVar command.

```
:DelVar A
:Disp "Hello
can be
:DelVar ADisp "Hello
```

There are two cases in which the following statement will be ignored, so you should add a newline instead:
- The [End](end.html) from an [If](if.html) statement.
- A [Lbl](lbl.html) command.

### For( Loops

When a [For(](for.html) loop doesn't have a closing parentheses after it, it will actually slow down [If](if.html) statements with a false condition inside the loop that immediately follow the For( line. This doesn't affect the speed of any other commands (except [IS>(](is-.html) and [DS<(](ds-.html) which are rarely used), nor does this effect occur with a true condition or If-Then-End blocks (just with a single If and a command following it).


```
:For(I,1,100
:If 0:
:End
```


```
:For(I,1,100)
:If 0:
:End
```


These two pieces of code, for instance, are nearly 20 times different in speed, which is a major speed hit in TI-Basic. As a general rule, if there is any chance at all that the condition is false (which is always the case, or else why are you testing for it in the first place?) result, then you should leave on the parentheses on the For( loop.

However, this bug does not occur when there is a line or code between the For( line and the If statement.


```
:For(I,1,100
:1
:If 0:
:End
```


```
:For(I,1,100)
:1
:If 0:
:End
```


These two pieces of code execute at the same speed. However, the left example is one byte shorter. As an optimization, omit the closing parenthesis of the For( loop if there is an extra line or code that occurs between the two statements.


### Rounding Errors

Because of the way that TI designed the TI-Basic language, each number has a limited amount of precision. As a result, any math calculations that involve extremely small or large numbers (ranging from -<sub>E</sub>99 to <sub>E</sub>99) will produce rounding errors that don't return the right number. There are a couple different ways you can deal with this problem.

The [round(](round.html) command will round a floating-point number so that it has the specified number of decimal digits. While you can hypothetically set it so that it has 25 digits, the calculator only allows a number to have up to 14 digits, which means the range is 0-14 digits.

```
:Output(Y,round(X,0),"X
:If E‾9>Ans(2
```

Another way to deal with the problem is by multiplying the number by a smaller number (for example, <sub>[E](e-ten.html)</sub>-9). The calculator will automatically treat the number in a similar fashion to the smaller number, which allows it to make the math expression work. Truthfully, neither of these methods is fool-proof, so you should just be aware of the problem.

<center>

|**[<< Coding Pitfalls](sk:coding-pitfalls.html)**|**[Table of Contents](starter-kit.html)**|**[Programmer Indicators >>](sk:programmer-indicators.html)**|
| --- | --- | --- |

</center>
