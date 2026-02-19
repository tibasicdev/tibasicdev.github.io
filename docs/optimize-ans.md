# Optimization: Putting Ans Into Practice
The [Ans](ans.html) variable (last answer) is a temporary variable that can hold any variable. Ans is changed when there is an expression or variable storage or when pausing with the [Pause](pause.html) command. It is mostly useful when you are just manipulating one variable. To use Ans just put an expression on a line by itself; it will automatically be stored to Ans. You can then change the expressions on the next line where the variable was called and put Ans there instead. Ans is faster than normal variables, but slower than Finance/Window variables and constants.

```
:getKey→A
:B+(A=26)-(A=24→B
can be
:getKey
:B+(Ans=26)-(Ans=24→B
```

If you have more than one line that calls the variable, you should just keep the variable. However, for the first line that calls the variable you should change the variable to Ans.

```
:getKey→A
:B+(A=26)-(A=24→B
:C+(A=34)-(A=25→C
can be
:getKey→A
:B+(Ans=26)-(Ans=24→B
:C+(A=34)-(A=25→C
```

When there is a common expression that is on multiple lines, it is sometimes smaller to put the expression on its own line and then change the expression on the other lines to Ans.

```
:30+5A→B
:Disp 25A
:Disp 30+5A
can be
:30+5A→B
:Disp 25A
:Disp Ans
```

When you use the same text many times in close proximity, you should put that text on its own line and replace it with Ans wherever it occurs.

```
:Disp "Hello
:Disp "Hello
:Disp "Hello
can be
:"Hello
:Disp Ans,Ans,Ans
```

For complex calculations, there are often multiple parts that are the same. You should take out the most common part and put it on its own line. If there are several common parts, you should take out the part that will result in the greatest size reduction. You then replace that part, wherever it occurs, with Ans.

```
:2A/(BC)+(BC)2→A
can be
:BC
:2A/Ans+Ans2→A
```

When dealing with text there are often situations where the same text is repeated multiple times. Rather than writing out the long string of text, it is sometimes possible to rewrite it using Ans. Put the common part of the text on its own line and on the next line concatenate (add together) with Ans however many times is needed to make the string.

```
:"                     →Str1 //20 spaces
can be
:"      //5 spaces
Ans+Ans+Ans+Ans→Str1
```

If you use the [sub(](sub.html) command to get the appropriate part of some text based on certain conditions, you can sometimes get rid of the sub( command and just use Ans. You would put each piece of text on its own line, and then put the condition before it.

```
:Input sub("GiveTake",1+4(A=1),4)+" candy?",Str1
can be
:"Give
If A=1:"Take
Input Ans+" candy?", Str1
```

With [Repeat](repeat.html) loops, you can sometimes put Ans in the condition instead of the variable. Even if Ans were 0 at the beginning of the loop, the code will work, since a Repeat loop will always cycle once before the condition is checked.

```
:Repeat A
:getKey→A
:End
can be
:Repeat Ans
:getKey→A
:End
```

When the condition in a Repeat loop has a common part that is repeated multiple times, you should put the common part at the end of the loop and replace the common part in the condition with Ans.

```
:Repeat A=2 and B=1 or A=2 and B=3
:getKey
:A+(Ans=26)-(Ans=24→A
:End
can be
:Repeat Ans and B=1 or Ans and B=3
:getKey
:A+(Ans=26)-(Ans=24→A
:A=2
:End
```

Many times in [If](if.html)-Then-Else conditionals the same expression or string of text appears in both the true and false parts. You should put this expression or string of text before the If-Then-Else conditional and then replace it in the conditional with Ans.

```
:If B
:Then
:Disp "Hello
:2Bnot(A→C
:Else
:Disp "Hello
:3→D
:End
can be
:"Hello
:If B
:Then
:Disp Ans
:2Bnot(A→C
:Else
:Disp Ans
:3→D
:End
```

When you have two or more strings of text that share a common part, you should take that common part out. You then can replace it with Ans and concatenate Ans to the strings.

```
:Disp "Hello World
:Disp "Goodbye World
can be
:"World
:Disp "Hello "+Ans
:Disp "Goodbye "+Ans
```

When you have two If conditionals that have math opposite conditions and they display text, it is sometimes possible to remove one of the conditionals and use Ans. Take the text from the first condition and put it on its own line. Then put the second conditional and the text on the next line. You then put the display Ans on the last line.

```
:If A≤B
:Disp "Higher
:If A>B
:Disp "Lower
can be
:"High
:If A>B
:"Low
:If A≠B
:Disp Ans+"er
```
