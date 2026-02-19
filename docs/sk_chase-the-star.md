# Sample Program: Chase The Star
You should now know how to make some basic functional games.  As a review for this chapter, here is a sample game that includes most of the things you have learned.  The game is called Chase the Star.  The goal of this game is to chase a randomly moving star until you catch it.  The only trick is, the star doesn't erase its previous position making it a little more concealed.

## The Program
```
:ClrHome
:2→A:2→B
:7→C:15→D
:Repeat (A=C and B=Ans) or K=21
:getKey→K
:If Ans
:Output(A,B,"_")
:A+sum(ΔList(Ans={25,34}))
:Ans-8(Ans=9)+8(not(Ans))→A
:B+sum(ΔList(K={24,26}))
:Ans-16(Ans=17)+16(not(Ans))→B
:C+randInt(-1,1)
:Ans-8(Ans=9)+8(not(Ans))→C
:D+randInt(-1,1)
:Ans-16(Ans=17)+16(not(Ans))→D
:Output(A,B,"X")
:Output(C,D,"*")
:End
:Pause "You_"+sub("Win!Lose",4(K=21)+1,4)
:ClrHome:"_"
```
## An Explanation
```
:ClrHome
:2→A:2→B
:7→C:15→D
```
The first step is to set up the game.  We use [ClrHome](clrhome.html) to clear the home screen.  The next thing we do is initialize the position of each object: the X and the *.  The X, (A,B), starts at coordinate (2,2).  The star, (C,D), starts at coordinate (7,15).

```
:Repeat (A=C and B=Ans) or K=21
:getKey→K
:If Ans
:Output(A,B,"_")
```
Now, we begin the game.  Since this is an action game, a Repeat loop will be used.  The game will end whenever the X coordinates and * coordinates match or the 2nd button is pressed.  Next, the game will ask for input using [getKey](getkey.html).  This way, the program can recognize key presses to support movement.  The next part checks to see if the user pressed anything.  If the Ans is not 0 (the user pressed something), the X will be erased.  That way, the program can redefine the X coordinates and then redraw X accordingly later on.

```
:A+sum(ΔList(Ans={25,34}))
:Ans-8(Ans=9)+8(not(Ans))→A
:B+sum(ΔList(K={24,26}))
:Ans-16(Ans=17)+16(not(Ans))→B
```
Here is a bit of a new code.  This isn't the normal code that you would see in movement.  The reason is this time, when the player moves off the screen, we want the X to be redrawn on the other side.  To do this, we first find out what direction the user moved.  This can be done with the normal code without [min(](min.html) and [max(](max.html).  Next, we will redefine A.  If the Ans, which is the projected A, is 9, that means it is past the boundary.  So, we subtract 8 to make it 1.  If it is 0 (notice we used [not(](not.html)), then we add 8 to make it 8.  The same is done with the B variable.  The only difference is that since the far boundary for B is 16, we need to add or subtract that to make B normal.

```
:C+randInt(-1,1)
:Ans-8(Ans=9)+8(not(Ans))→C
:D+randInt(-1,1)
:Ans-16(Ans=17)+16(not(Ans))→D
```
The * does something very similar.  Since its movement is random, we use [randInt(](randint.html).  The -1 and 1 tells whether to move up or down.  The next part is completely identical to the previous coding in order to make the * wrap to the other side.

Note that sometimes the * won't move at all.  Since randInt( will select a number from -1 to 1, 0 is sometimes selected.

```
:Output(A,B,"X")
:Output(C,D,"*")
:End
```
The final part of the loop is the output.  The X is redrawn at its new coordinates and the * is redrawn at its new coordinates.  Note that the * doesn't erase its path!  This is done intentionally for the game experience, but for other games, erasing the old copy might be an important step.

```
:Pause "You_"+sub("Win!Lose",4(K=21)+1,4)
:ClrHome:"_"
```
This is the final part of the program.  What happens is the calculator uses the [sub(](sub.html) command to determine whether to display "Win!" or "Lose".  If the user pressed 2nd, then the program will display "Lose".  If the user did not press second (meaning that the user must have caught the star), then the "Win!" message will be displayed.  Then lastly, the program will reset the home screen as if nothing ever happened.

This concludes the chapter on making games.  However, your journey is not yet complete.  The next step is figuring out how to use the graph scene to make superior graphics.  Have fun, and prepare to learn how to create some hardcore designs!

<center>

|**[<< Exercises](sk:exercises-games.html)**|**[Table of Contents](starter-kit.html)**|**[Introduction to the Graphscreen >>](sk:graphscreen.html)**|
| --- | --- | --- |

</center>
