# Optimization: Conditionals
Use If conditionals when you only want to execute the one command on the next line.
```
:If A=1
:Then
:C+2→C
:End

can be

:If A=1
:C+2→C
```

Because conditionals are generally slow, you should replace them with [piecewise expressions](piecewise-expressions.html) if you are just changing a variable. You take the variable and add or subtract the expression, multiplying it by the value that you are adding to the variable. Using piecewise expressions can sometimes be slower than If conditionals to avoid storing zero into the variable if the expression is false.

```
:If A=3
:B+2→B

can be

:B+2(A=3→B
```

You don't need to put the value in front of the expression when it is one.

```
:B+1(A=2→B

can be

:B+(A=2→B
```

You can take piecewise expressions a step further by combining multiple If conditionals that deal with the same variable and put them into one piecewise expression.

```
:If A=3
:B+5→B
:If A=6
:B-3→B

can be

:B+5(A=3)-3(A=6→B
```

If you are adding and subtracting the same value from the variable in the piecewise expression, you can factor the common value from each expression. This works best when you are adding and subtracting a big number.

```
:B+11(A=1)-11(A=2→B

can be

:B+11((A=1)-(A=2→B
```

You can sometimes reorder a list of If conditionals so that the last possible outcome doesn't even need an If conditional. This mainly works when the program is going to do a certain action and there are no other alternative actions that can occur.

```
:If not(A
:Goto A
:If A>0
:Goto B
:If A<0
:Goto C

can be

:If A<0
:Goto C
:If A
:Goto B
:Goto A
```

If-Then-End conditionals should be used when you want to execute multiple commands.

```
:If A=1
:C+1→C
:If A=1
:D+1→D

can be

:If A=1
:Then
:C+1→C
:D+1→D
:End
```

If you have two or more If conditionals that have a common expression, you should take the common expression out and make it into an If-Then-End conditional and nest the If conditionals inside it.

```
:If A=1 and B=1
:C+2→C
:If A=1 and B=2
:D+1→D

can be

:If A=1
:Then
:C+2(B=1→C
:D+(B=2→D
:End
```

If you are displaying lots of text based on If conditionals, you should put the text together and then just use the sub command to get the appropriate part of the text. This will display the text if none of the conditions are true, so this may not always be desired.

```
:If A=3
:Disp "Hello
:If A=4
:Disp "World

can be

:Disp sub("HelloWorld",1+5(A=4),5
```

The If-Then-Else-End conditionals should be used if you want to execute multiple commands when an expression is true or false. Instead of putting two If-Then-End conditionals that have math opposite expressions, If-Then-Else-End conditionals are faster because you don't need to do two checks; only one of the conditionals can be true at one time.

```
:If B
:"Hello→Str1
:If not(B
:"Goodbye→Str1

can be

:If B
:Then
:"Hello→Str1
:Else
:"Goodbye→Str1
:End
```

When using an If-Then-Else conditional and only one command is executed if the expression is true or false, use an If conditional between the two commands instead. You might also have to change the order of the commands, depending upon the commands.

```
:If B
:Then
:"Hello→Str1
:Else
:"Goodbye→Str1
:End

can be

:"Goodbye→Str1
:If B
:"Hello→Str1
```

When a line is either drawn or erased depending on a condition, you can put that condition as the optional fifth argument for the Line command.

```
:If B:Then
:Line(1,2,3,4
:Else
:Line(1,2,3,4,0
:End

can be

:Line(1,2,3,4,B
```

When you have a If-Then or If-Then-Else conditional that has a Goto command as one of the nested commands, you can sometimes remove the conditional and replace it with multiple If conditionals. Doing this prevents a memory leak from happening.

```
:If A
:Then
:Disp "Hello
:Goto A
:Else
:Disp "Goodbye
:B+2→B
:End

can be

:If A
:Disp "Hello
:If A
:Goto A
:Disp "Goodbye
:B+2→B
```

If you have If:Then:End statements with an "End" at the end of the program, the End can be removed.

```
:If randInt(0,1
:Then
:Disp "Heads
:Else
:Disp "Tails
```

However, if the last line returns a value, it will show up on the home screen after the program ends.
