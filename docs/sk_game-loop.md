# The Game Loop
The game loop is the fundamental structure of most games. It repeats throughout the game, managing all necessary information and user input. Of course, the game loop will be different depending on the type of game. In a shooting game, it might loop continuously, tracking player movement if there is any, and frequently moving enemies and updating scores and such. In a chess game, it might loop once for every turn, waiting for user moves and updating the positions of pieces only when one is moved, or it might loop every second if a timer is implemented. In general, however, it will usually look like this:

```
while the player has not won:
 update game information (for example, score or turn count)
 accept user action
 update game status (for example, locations of pieces/units/player)
 display relevant information
```

There are four main types of loops used in programs. There are [For](for.html)( loops, [While](while.html) loops, [Repeat](repeat.html) loops, and [Goto](goto.html) loops.  The first three are the most commonly used whereas the Goto not so much. You probably already read about loops in the previous chapter, but this discusses the fundamentals of each loop in detail and displays the application of such things when referring to game building.


## While Loops

This loop is the most basic loop. What you do is put a condition after it, and while that condition is true, the loop will continue to run between the While and its End until the condition becomes false. So, when the calculator encounters a While, it tests the condition after it and depending on whether it is true or not, the calculator will either execute the loop or skip it. If it executes the loop, it will continue to do so until the condition after While becomes false. Let us consider this code:
```
:3→A
:While A<10
:A+1→A
:Disp A+1
:End
:Disp "Finished"
```
This code, of course, initially stores 3 into A. Then, it encounters the While loop. What the program then does is tests the A<10. If it is 1 (or true), then it will execute the next commands. If it is 0 (or false), then it will skip to the End and continue from there. In this case, 3<10 is true, so it begins the loop by executing the following commands. A increases by 1, and then it displays one more than that value. So, it displays 5, but A is 4. When the program reaches the End, it then tests A<10 again. If it is true, then it will execute the commands again. If it is false, it will continue after the End. So, since 4<10, it will do the loop commands again. So it now displays 6. It will continue to do this until A is equal to or greater than 10. So, once A becomes 10, the program will display "Finished!".

That is the essence of loops: repeating a group of commands while or until a condition becomes true, or when something specific occurs.

While loops are good for elimination games where while player is still alive, his turn commences. If the player is eliminated, then it would skip the loop. Another reason for a While loop is as a sub loop where an action from the user determines the usage of the second loop. If the action doesn't involve the loop, then the loop can be skipped.

## Repeat Loops

The Repeat loop is almost the same as the While loop, but there is a difference. First of all, the repeat loop will continue to loop *until* the condition after it is true. So, if the condition is not true, then it will continue to loop until that condition becomes true. Another difference is that when the calculator encounters a Repeat, it doesn't scan the condition. It will automatically start the loop and test the condition when it reaches the appropriate end. When the calculator reaches a Repeat, it cannot be skipped. Consider the following code:

**Note:**
The difference between a While loop and a Repeat loop is that the While can be skipped depending on the condition.  A Repeat loop is always executed regardless of initial condition.

```
:15→A
:Repeat A=15
:A=15→A
:Disp A
:A+2→A
:End
:Disp "Finished"
```
This code firsts stores 15 into A. Now, it begins the loop. Since it is a Repeat loop, the loop is automatically executed even though the condition is true. Since A is 15, the Boolean logic becomes 1 and is stored into A. The first display is 1. The program then adds two to A. When it reaches the End, the loop goes back to the condition and tests it. It will continue through the same cycle until the A becomes 15. When that happens, the program displays "Finished".

Repeat loops are typically used as the main, or base, loop of the program or action. The reason for this is so the loop becomes automatically executed rather than being skipped. Also, the mentality of a game loop is to continue gameplay until the person dies/loses. With this mentality, the condition is easily depicted as the situation when the player loses making the loop end at that instance.

## For( Loops

This loop is not like the others, and it is a little more complex. This loop requires 3 arguments with one optional argument. When writing a For( loop, you use this syntax:

For(*variable*,*start*,*stop*,[*increment*])
If *increment* is not given, the calculator assumes it is one

What the loop does is it first stores the *start* number into the *variable*. Then, it runs through the commands until it reaches End. When End is reached, the calculator loops to the For, adds *increment* to the *variable* value, and runs through the commands again. The loop continues to run until *stop* is reached. When that number is reached, then the calculator will proceed executing commands after the End.

Consider this code:
```
:For(A,2,6)
:Disp A
:End
```
This code starts the For( loop by giving A the value of 2. After it displays the two, the program adds one to A and displays again. It continues to add one until it hits 6. When that happens, the program runs through Disp one more time and ends the loop.

This type of loop can become incredibly useful in games. If the user makes an action where multiple things must be accomplished but of similar origin, a For( loop can be used. This loop can also be used when there is a certain number of turns being played. You could set up the loop as For(T,1,10) for a 10 turn game and put the code between the For( and its appropriate End. As you practice with this loop, you will understand exactly how useful it can become.
## Goto Loops

This is probably the least common loop used in the TI-Basic community. What you do is you place a Label somewhere and later in the program put a Goto leading to the label for the use of repeating a set of commands. This type of loop requires no arguments or conditions, but it must be exited with some sort of other Goto. Although this is a relatively fast type of loop (if the Label is near the top), the positioning of the Goto could lead to some problems. The problem with goto is the event of [Memory Leaks](memory-leaks.html) in which the calculator loses memory within the program and eventually terminates due to lack of RAM. This occurs when you have a Goto within a loop or condition that leaps to a label outside of that loop.  The calculator uses memory every time it encounters a loop in order to remember that it needs to find an End somewhere. The problem is, when a Goto is used to jump out of the loop, that memory is lost because the calculator never found End.  So, although useful in some cases, Goto loops are not recommended for primary game loops.

Goto and Lbl have a different purpose really. They can instead be used to locate various loops for game functionality. If you reach a condition that needs to be jumped backwards to another loop, a Goto Lbl combo can be used to easily jump back to the loop.  Although dangerous, these Goto's do have a use, just be careful when placing them within loops.

## Infinite Loops

An infinite loop is a loop that continues forever. The most common infinite loop is While 1. Since the condition can never be 0, the loop never ends. These loops in a game are not as useful as a terminating loop, but they can be utilized along with Goto to produce a game with a function that repeats several times regardless of status. Loops like this can be used when the player can't lose, only quit. In such situations, an infinite loop can be used and a Goto can determine when to leave (careful of memory leaks). These loops are typically replaced with a While loop that has a condition for when the player quits, but nonetheless, this loop can be used only sparingly.

## Application

So, how can these loops be applied to making a game? Well, for BASIC games, loops are often needed for repetitive or continued tasks. A loop can be put somewhere near the beginning, and that loop can continue to run until the player loses. The main loop is the Repeat loop. It is typically used as the base for games. The conditional used after the loop is typically like this:
```
:Repeat (player dies/loses) or (getKey value)=45
code code code
:End
```
This way, when the player loses, the loop ends, or when he clicks Clear, the loop ends. The content of `code code code` could be anything really, but it typically follows a pattern found in many basic games. The code usually starts with updating the game stats and output. This is used mainly for turn based games as most games will update the information at the end of the code. Then, the program should ask or give opportunity for user input, accept it, and take action upon it. After that, the game should update output and other game stats or allow an AI to activate.

This is a list of the basic game types and what types of loops can be used to accomplish these actions.
### Action
An action game is one where the playing field is constantly changing whether the player does something or not, and depending on the input, other things on the field react to the action of the user. These types of games can be quite challenging because of the constant update. The reason is because of the additional coding put under the same loop as the input selection, usually [getKey](getkey.html). This slows down the system's ability to accept user input.

So, let's say you wanted to make a game where if X became 0, you lost, or if you hit getKey, the game ended. X is 5 when you win. Also, there are multiple things occurring even if the user takes no action.  You can use the following code
```
:Repeat X=0 or X=5 or Ans=45
:Output(A,B,"_")
:min(8,max(1,A+sum(ΔList(Ans={25,34}))))→A
:min(16,max(1,B+sum(ΔList(K={24,26}))))→B
:Output(A,Ans,"O")
other activity coding
:getKey→K
:End
:ClrHome
:Disp "You"+sub("LoseWin!",4(X=5)+1,4)
```
So, we are using a Repeat loop with some conditionals after it. The conditionals represent when the game ends: when you lose (X=0), when you win (X=5), and when you quit (press Clear). The program loops through the game until one of the conditions is met. The next thing the program does is update user action info. Depending on which arrow key the player clicked, the program will move in that direction (remember from [sk:Movement](sk:movement.html)?). Next, you would put other action after the update, but only put a small amount of coding, or else the least possible. The more code you put in `other activity coding`, the slower the game will be, and nobody likes a slow game. Finally, the game should ask for user input.

Now, it may seem weird to ask for input at the end, but it is a very useful technique. The reason the input is at the end is to use Ans in the loop conditional which makes the game run a little faster. Anywhere you can get speed makes an action game better, so try to follow this general outline. As you get more experienced, you will begin to find other alternatives to this loop as the type of game changes, but for now, this outline will help you make basic games.

### Strategy/Turned Based
A strategy or turn based game is one that waits for the user input before the calculator makes any further action. In this type of game, speed is not normally as important because it is usually a thinking type game. The coding for a strategy game works in a way as described at the beginning of the article. You would need separate scores for each player. If it were an elimination type game, then a While loop can be used within a Repeat loop to indicate player turns. The loop pattern would be sort of like this:
```
Repeat one player is left
Update player turn by one or reset to one at max
Update player information output
While player is alive or Clear
Ask for input
act upon input
update game info
update output
End
extra stuff
End
```
This works by repeating the loop until one player is left and updating all player info according to previous outputs. The While loop is used for the player input. However, if the player is eliminated, then the While loop will be skipped. It will then ask for input and update that player's info accordingly.

So, putting this code to action, let us say that you are building a Risk game. You can have a Repeat loop backbone the whole game and use nested While loops for player action. Here is an example (although a rather poor one) for a Risk game where L<sub>1</sub> is the board of 42 spaces where iPart is the number of troops and fPart is who is occupying the space, T is the player turn, and K is the getKey.
```
:Repeat not(variance(10fPart(L₁)))
:T(T≠4)+1→T
show stats
:While max(T=10fPart(L₁)) or K=22
:Repeat Ans
:getKey→K
:End
Update info
Update Output
:End
:End
```
So, this code has L<sub>1</sub> as the whole board. Since the fPart is the occupant of the territory, then when all of the territories have the same occupant, the [variance](variance.html)( will be 0, and since [not](not.html)( is used, the equation becomes 1 when the answer is 0. So, the loop ends when all territories are occupied by the same person. The While loop won't even execute if there is not a single square with occupant T. That represents that player being eliminated. So, the loop goes back to the beginning. The turns are updated for every pass, and then T=4, the turn number is set back to 1.

### Limited Turns
A game with limited turns ends when a counter reaches a certain number. There are a couple of ways you can do this. You can use a Repeat loop with turn number T. When T, which is updated every loop, reaches a certain number specified in the Repeat conditional, the loop will end. Or, you can use the For( loop. The For( loop automatically updates a variable and ends when the *stop* is reached. So, you can set up a code like this:
```
:For(T,1,(last turn))
Output turn number
Update conditions
Secondary loop
Ask for User input
Update action
```
Pretty much, all you are doing is setting up a turn keeper and using one of the previous loop examples to run the main function of the game.  Turn based games is really just an added addition to the other loops.

## Conclusion
This wraps up the Game Loop tutorial. This is just the basics of making a game. In making a game, the loop only represents the backbone of the program. What lies within a loop is the meat, and that is what makes the game function. The next section deals with data types which will introduce to you the various ways we can manipulate numbers to accomplish jobs.


<center>

|**[<< Movement](sk:movement.html)**|**[Table of Contents](starter-kit.html)**|**[Data Types (Intro) >>](sk:data-types.html)**|
| --- | --- | --- |

</center>
