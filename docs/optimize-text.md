# Optimizations: Displaying Text
If you have a string of numbers that you are displaying, you don't need to put quotes around the numbers. You should only use quotes if you want to keep any leading zeros.

```
:Disp "2345
can be
:Disp 2345
```

Use the Disp command instead of the Output command when displaying text on the first line of the homescreen. You can just add spaces to the text to move it to the correct location.

```
:Output(1,2,"Hello
can be
:Disp " Hello
```

When displaying the same text or variable on three or more lines, use a For loop. A For loop can also be used when the display is changing by a constant increment.

```
:Output(3,3,1
:Output(4,3,2
:Output(5,3,3
can be
:For(X,3,5
:Output(X,3,X-2
:End
```

When the text in an Output command is more than sixteen characters (26 on the color calculators), it will wrap around to the next line. When you have two or more Output commands that display text on different lines, you can sometimes put the text together and add blank spaces between it to make it go to the next line in the desired location.

```
:Output(1,6,"Hello World
:Output(2,2,"Version 1.0
can be
:Output(1,6,"Hello World Version 1.0
```

Using the Disp command, you can display text and variables at the same time by putting a comma between each one. Because this can hinder readability, this should only be done when just displaying variables.

```
:Disp A
:Disp B
can be
:Disp A,B
```

When you have a list of Disp commands that you pause, you can take the text or variable from the last Disp command and place it after the Pause command as its optional argument, allowing you to remove the last Disp command.

```
:Disp "A=
:Disp A
:Pause
can be
:Disp "A=
:Pause A
```

You can often remove Disp commands by storing to a string only the text differing with values of a variable, and then displaying the text added to the similar statements with one Disp command. This can be useful when you have two conditionals that are opposites that display similar text.

```
:If A≥10
:Disp "You Win
:If A<10
:Disp "You Lose
can be
:"Win
:If A<10
:"Lose
:Disp "You"+Ans
```

When you have two or more Disp statements inside an If-Then conditional, you can combine the Disp statements to change the If-Then conditional to an If conditional.

```
:If A>B
:Then
:Disp "A is greater
:Disp "than B
:End
can be
:If A>B
:Disp "A is greater","than B
```
