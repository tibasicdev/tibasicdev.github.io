# Displaying Text
Optimizing text is one of the best ways to optimize your program.  It is easy, and it shaves off many bytes.

## Homescreen Specific Optimizations
The following optimizations are only useful for users of the homescreen.
### Using Disp Instead of Output(
when you display a short quote at (1,1) on the homescreen, try to use Disp instead of Output.  This change does not affect displayed information at all and merely shortens the code a little.
### Using Output( to Wrap Text
Because the output command wraps text, Paragraphs are much better displayed on the homescreen using one Output command than using eight or so Disp commands.  This optimization can be used to improve size for any display on the homescreen where characters are within seven spaces from each other.  Here is an example that would be used as a title screen layout.
```
:Output(3,2,"ULTIMATE QUEST
:Output(4,3,"DEVELOPED BY
:Output(5,4,"YOUR NAME
```
is shortened by putting
```
:Output(3,2,"ULTIMATE QUEST //three spaces// DEVELOPED BY //five spaces// YOUR NAME
```
this optimization saves an average of three bytes per line.
## Graphscreen Optimization
On the graphscreen alone, you can have text and variables displayed on the same line with the same text( command.  Separate them with commas.  This eliminates the need for the 1+int(log( trick.
```
:Text(1,1,"HP=
:Text(1,13,H
:4int(log(H
:Text(1,17+Ans,"/
:Text(1,21+Ans,P
```
can be greatly reduced to
```
:Text(1,1,"HP=",H,"/",P
```
## Optimizations for Both Screens
The following optimizations can be applied to both the homescreen and the graphscreen to improve size.
### The Pause Optional Argument
When you have a list of Disp commands that you pause, you can take the text or variable from the last Disp command and place it after the Pause command as its optional argument, allowing you to remove the last Disp command.
```
:Disp "A=
:Disp A
:Pause
can be
:Disp "A=
:Pause A
```
### Shortening Conditionals
When you have two or more Disp statements inside an If-Then conditional, you should combine the Disp statements so you can change the If-Then conditional to an If conditional.
```
:If A>B
:Then
:Disp "A is greater
:Disp "than B
:End
```
can be
```
:If A>B
:Disp "A is greater","than B
```
### Shortening Text Length
The first things to do when optimizing text include removing the end parenthesis and quotation marks, as we've already explained.  Other things that you can do to optimize include replacing certain words with shorter synonyms and removing embellishing words.  Here is an example.
```
:Output(1,1,"YOU HAVE BEATEN")
:Output(2,1,"THE GAME!")
```
can be much reduced to
```
:Output(1,1,"YOU WON!
```
By removing the excess words and changing beat to won.  This optimization saved 27 bytes.  Now think of having an unoptimized text adventure, with over one hundred individual text display commands.  You could save 2700 bytes just by optimizing the text in that game!  Now do you see why optimizing text is so important?
### Using sub( to Reduce Size
If someone wins your game, don't you want to tell them that they won with a couple really optimized commands like these? (Pretend that the user has exited the game loop, he has either won or lost, and if A=10 then he won)
```
:If A=10
:Then
:Output(4,5,"YOU WIN
:Else
:Output(4,5,"YOU LOST
:End
```
But have you ever thought of using the [sub(](sub.html) command to combine the two times the word YOU is displayed?  Consider the following code, which is six bytes smaller.
```
:Output(4,5,"YOU"+sub("WON LOST",1+4(A≠10),4
```
This code works because in the case that A=10 it should start at 1 at remove four characters and in any other case it should start at 5 and remove four characters.

### Deleting repeat phrases
If a word or phrase is repeated, you can reduce size by eliminating it and the display commands, and adding the repeat phrase to a string stored in ans.  Note that in this case, it is smaller to use sub( than to do this.
```
:If A=10
:Then
:Output(4,5,"YOU WIN
:Else
:Output(4,5,"YOU LOSE
:End
```
can be improved to
```
:"LOSE
:If A=10
:"WIN
:Output(4,5,"YOU"+Ans
```

### Conclusion
As you have seen, optimizing text is an important thing to do when finishing up your programs, and if you stick to it, your text based programs can be much improved.


<center>

|**[<< What is Optimization](sk:what-is-optimization.html)**|**[Table of Contents](starter-kit.html)**|**[Optimizing Variables >>](optimize-variables.html)**|
| --- | --- | --- |

</center>
