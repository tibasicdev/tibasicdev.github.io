# Multiplayer
|This article is currently in development. You can help TI-Basic Developer by expanding it. I may never get around to finishing this. Feel free to improve it. ~ [/member:govegan GoVegan]|
| --- |

Multiplayer is where two or more people play a game together at the same time. Although you can create AI opponents for a player to play against, AI does not offer as much fun compared to playing against other human opponents — you can have the players work together, compete against each other, and even one player manage the other players.

Multiplayer games are generally divided into two categories: the players share a single calculator, and the players each play on their own calculator connected together with a link cable (either I/O or USB).


## Single-Calculator Multiplayer

Multiplayer games on one calculator generally fall into two categories: real-time and turn-based. Real-time is where the game action is constantly changing, not stopping for the player input. Some classic examples of real-time games are Galaxian and Pong. Turn-based is where each player is allowed to make a move, and the game action only changes after each player has moved. Some classic examples of turn-based games are Battleship and Scorched Earth.

Making real-time games involves using the [getKey](getkey.html) command, except you can't wait for a key to be pressed. The general form is something along the lines of:

```
While <game not done>
getKey->K
If K=<player 1 key>:Then
// player 1 action
End
If K=<player 2 key>:Then
// player 2 action
End
<Update rest of game>
End
```

As you can see, the player action only occurs when a player has pressed a particular key; otherwise the game just continues on like regular, with the main game loop being repeated over and over again.

There are some problems with making real-time games, however.

The first, and foremost, problem is that TI-Basic is rather slow with user input. If you do anything remotely time-intensive, such as displaying lots of graphics or complex variable manipulation, then there will be some lag-time between when a player presses a key and when the calculator gets around to processing it. Although there's not really much you can do about this, you can make sure your game is as optimized as possible (especially breaking the more time-intensive parts into their own [subprograms](subprograms.html)).

The second problem is that the calculator only keeps track of the last key pressed since the last time getKey was executed, so that means only one player can have their input read and processed each time through the game loop. In addition, if you enter a large block of code for the player, it will take a while before the other players have a chance to do anything.

Related to the second problem, the third problem with making real-time games is that unlike the other keys, the arrow and DEL keys can actually be held down, which will cause them to keep being repeated until they are unpressed. The effectively disables the other keys from being able to be pressed. There is no viable way to get around this problem, except asking the players to not press those keys.

The fourth problem is that the keypad is quite small, and having two or more people try to share the calculator can be rather difficult. The best way to work around this problem is choosing keys for each player that are a good distance away from each other. When choosing keys you should also keep in mind the calculator screen — if somebody has to press keys that make it difficult to see the screen, then you should choose different keys.

Because making real-time games is not very practical, a better alternative is turn-based games: you hand the calculator from player to player, allowing each each player to move one at a time. These games are much easier to program: you simply use a variable to keep track of whose turn it is, increment the variable after each player's turn, and when everybody has completed their turn, you reset the variable. The only real downfall of turn-based games is that they can be slow because you have to wait until the other players are done before you can move.

## Multi-Calculator Multiplayer

So I guess you're wondering how to program a multi-calculator multiplayer experience into one of your games. One of the first things you will need to do is familiarize yourself with the [GetCalc(](getcalc.html) command. Basically, it retrieves a specified variable from another calculator and stores it to that variable on yours.

Creating multiplayer programs over two calculators is a much less simple process as it is to make single-calculator multiplayer programs. However, doing so could be the main selling point of your program and would certainly be worth the effort. You will notice that in each of our examples we tend to transfer lists, which we recommend you do too. Whilst it is possible to transfer a variety of real variables, it is much faster to transfer a list of numbers than a number of real variables.

There are two general ways to programming multi-calculator programs; one screen processing and two screen processing. The one screen processing method is simply making a program use the statistics from another calculator, and the whole multiplayer experience is processed on that calculator. The two screen processing method is much more complex, where we can share the multiplayer processing across two calculators by using a "turn-by-turn" interface.

### Core

When it comes to multi-calculator multiplayer games, it is absolutely necessary to give each calculator its own identity. As both calculators are running the exact same program, we need a way to be able to determine one calculator as "Calculator A" and the other calculator as "Calculator B". This makes it possible for both calculators to know what data to send and receive. For example, if both calculators were "Calculator A", then both calculators would be doing exactly the same thing, or keep trying to receive the same variable from each other in an endless loop

This is code determines which assigns each calculator with a unique identity:


```
:GetCalc(A
:e(A=π)+π(A≠π→A
```


——

How it works is that the calculator gets the variable A from the other calculator, and checks whether it equals [π](pi.html) ([pi](pi.html)). If A equals π, then *[e](e-value.html)* is stored to A; however, if A does not equal π, then π is stored to A. Here is a table to demonstrate the results:

| Calculator A | Calculator B|
| --- | --- |
| A = π | A = *e*|
| A = 3.141592654 | A = 2.718281828|

The calculator can therefore identify itself like this:


```
:If A=π:Disp "I'M CALC A
:If A=e:Disp "I'M CALC B
```


——

If we use a [not(](not.html) routine to make Calculator A = 1 and Calculator B = 0 instead, then we are unable to determine whether a link has been initiated. Simply explained, because variable A is more likely to equal zero than any other number, Calculator A may accidentally assume Calculator B has initiated the multi-calculator sequence. Variable A is not likely to ever equal π (or *e*), which is why it's useful as a "connection initiated" checker for the calculator.

The beauty of the core code is that it doesn't matter which player executes the core code first, both calculators will be able to give themselves a unique identity, be able to distinguish which calculator they are and be able to see whether the other calculator is initiated yet.

### One Screen

If you are looking to save space and valuable time, this is the multiplayer for you. This method has the sending calculator in a power-saving state the whole time while the receiving calculator does all of the hard work such as processing and animation.

<details style="display: inline;"><summary>show</summary>

```
:GetCalc(A
:e(A=π)+π(A≠π→A
:If A=π:Then
:∟STATS→L₁
:Disp "SENDING DATA...","PRESS ENTER WHEN
:Pause "FINISHED
:End
:If A=e:Then
:GetCalc(L₁
<interactive code>
:End
```

——
</details>

First off, we put in the core multiplayer code to determine which calculator is which. Then, Calculator B will retrieve the opponent's statistics for battling. Because the program uses the same variables on every calculator, we need to find a way to store Calculator A's statistics onto Calculator B without overwriting Calculator B's statistics. Surprisingly, this is not as hard as it seems:


```
:GetCalc(A
:e(A=π)+π(A≠π→A
:If A=π:Then
:∟STATS→L₁
:Disp "SENDING DATA...","PRESS ENTER WHEN
:Pause "FINISHED
:End
```

——

Now that each calculator has created its unique identity, and Calculator A has stored its statistics to L₁, we can finally make Calculator B receive Calculator A's statistics and process all of the data:


```
:If A=e:Then
:GetCalc(L₁
<interactive code>
:End
```

——

After this, write the rest as though this was a single-calculator multiplayer game, where you're statistics are in ∟STATS and your opponent's statistics are in L₁. Here is a side-by-side comparison on how the program runs:

| Calculator A | Calculator B|
| --- | --- |
| ![1SCREEN-A.gif](1SCREEN-A.gif "") | ![1SCREEN-B.gif](1SCREEN-B.gif "")|

### Two Screens

Here we show you a turn by turn based method of a battle game.

<details style="display: inline;"><summary>show</summary>

```
:DelVarADelVar FGetCalc(A
:e(A=π)+π(A≠π→A
:If A=π:Then
:∟STATS→L₁
:Else
:∟STATS→L₂
:Goto W
:End
:Repeat F
:DelVar BMenu("CHOOSE ATTACK","ATTACK A",A,"ATTACK B",B,"RUN AWAY",R
:Lbl A:1→B:Goto S
:Lbl B:2→B:Goto S
:Lbl R:‾1→B
:Lbl S:1→θ
:Menu("SENDING ATTACK","READY?",SA
:Lbl SA:1→S
:DelVar θprgmθANIMAT
:Lbl W:Disp "WAITING...
:DelVar BRepeat B or F
:GetCalc(B
:GetCalc(F
:End
:If not(F:Then
:If A=e:GetCalc(L₁
:If A=π:GetCalc(L₂
:Repeat not(θ
:DelVar θGetCalc(θ
:End
:DelVar SprgmθANIMAT
:End
:End
:If ∟STATS(6:Then
:Pause "YOU WON!
:Else
:Pause "YOU LOST!
:End
```

——
</details>

Like with all multi-calculator multiplayer programs, we first provide the program with the core. This time, however, we will first reset variables A and F. Then we will add code for which stores each calculator's statistical data to its individually named list. Calculator B is then instructed to go elsewhere in the program (note that [Goto](goto.html) is within an If-Then loop):


```
:DelVarADelVar FGetCalc(A
:e(A=π)+π(A≠π→A
:If A=π:Then
:∟STATS→L₁
:Else
:∟STATS→L₂
:Goto W
:End
```

——

Because this is turn by turn battle game, we need to repeat the battle code until the battle is finished. We will make variable F determine this. Also, we want Calculator A to be able to attack first, so we shall put the code for attacking as the first thing in the Repeat loop. This is where it starts to get a bit sticky. First we delete variable B, which is going to determine what command the user has chosen (whether it be a kind of attack, or to run away).


```
:Repeat F
:DelVar BMenu("CHOOSE ATTACK","ATTACK A",A,"ATTACK B",B,"RUN AWAY",R
:Lbl A:1→B:Goto S
:Lbl B:2→B:Goto S
:Lbl R:‾1→B
:Lbl S:1→θ
```

——

So when the user selects an option from the menu, a number is stored to B and 1 is stored to θ. Theta tells the receiving calculator that it the sending calculator is not ready yet. Then we create a second menu. This is to give the receiving calculator a chance to receive certain variables. That process is almost instant, and so the user then presses ENTER. θ is erased and 1 is stored to S, just before the "animation" program starts. S simply tells the animation program that it has just sent the attack.


```
:Menu("SENDING ATTACK","READY?",SA
:Lbl SA:1→S
:DelVar θprgmθANIMAT
```

——

The animation program is shared by both the attacker and the attacked. The program makes particular animation depending on whether variable S is equal to one. If S=1, then this program will only display the opponent getting hurt. If S=0, then this program will display YOU getting hurt, calculate how much HP you have left, and if you died, sets variable F to zero. By using the subprogram "prgmθANIMAT", it means we don't need to worry about memory leaks or program changes.

Now we have the receiving code. You will notice that Lbl W is the first line here. This is so that Calculator B can jump straight here on the first move. Because this label is within a repeat loop, and the Goto came from an If-Then section, there are no memory leaks. The first thing we do is make the program wait until the sending calculator has issued a move. If the game is over (F=1), then this process stops, and the program exits the "Repeat F" loop. If the game is not over, and the opponent issued a move, then the calculator receives the opponent's updated statistics.


```
:Lbl W:Disp "WAITING...
:DelVar BRepeat B or F
:GetCalc(B
:GetCalc(F
:End
:If not(F:Then
:If A=e:GetCalc(L₁
:If A=π:GetCalc(L₂
```

——

At the moment upon entering the loop, we know that the opponent's θ equals 1. In this loop, we clear our θ variable and then retrieve the opponent's θ. Because of the nature of GetCalc(, we can not receive variables whilst the other calculator is processing. Remember that as soon as the other calculator exits the "SENDING ATTACK..." menu, the animation subprogram starts.

Using this knowledge, if we delete θ and then retrieve θ whilst the opponent is in the "SENDING ATTACK..." menu, θ will equal 1 (and hence the loop is repeated). But when the opponent starts the animation process, we will be unable to retrieve θ, and so θ will equal what it all ready was, zero (hence we exit the loop).


```
:Repeat not(θ
:DelVar θGetCalc(θ
:End
:DelVar SprgmθANIMAT
:End
:End
```

——

This code is rather remarkable because it makes it possible to start the animation on both calculators, at the same time, automatically. You don't need to go messing about with "both users press ENTER at the same time" routines, only one user needs to press ENTER and both calculators begin — a foolproof technique.

If, after the animation process, the battle is not yet over, then the program continues into attack mode again (at the start of the "Repeat F" loop).

Now we need a routine which restores the statistics to the ∟STATS list and says who won after the battle is over! This is the easiest part of the routine. If the player's health points do not equal zero, then that player won — otherwise the other player won.


```
:L₁
:If A=e:L₂
:Ans→∟STATS
:If Ans(6:Then
:Pause "YOU WON!
:Else
:Pause "YOU LOST!
:End
```

——

There are a couple of things that you need to be aware of for this routine to be work:
1. When the "SENDING ATTACK" menu pops up, you must wait for a second for the attack to actually send before pressing ENTER;
2. Variable A must NEVER equal π during the program, (obviously with the except of the multi-calculator code itself). If it does, and a different calculator starts this routine before the other one, then the link process will fail.
To prevent the second problem from ever happening, you should reset variable A at the start of your program, and never use this variable throughout the program.

This whole routine is certainly complex, but it does work, and works pretty well too. Here is a side-by-side comparison of how the program runs. For reference, here is a table showing the values:

| |~ Calculator A |~ Calculator B|
| Max HP| ∟STATS(1)=2| ∟STATS(1)=5|
| --- | --- | --- |
| Level| ∟STATS(2)=2| ∟STATS(2)=5|
| --- | --- | --- |
| Attack| ∟STATS(3)=2| ∟STATS(3)=5|
| --- | --- | --- |
| Defence| ∟STATS(4)=2| ∟STATS(4)=5|
| --- | --- | --- |
| HP| ∟STATS(6)=2| ∟STATS(6)=5|
| --- | --- | --- |

| Calculator A | Calculator B|
| --- | --- |
| ![1SCREEN-A.gif](1SCREEN-A.gif "") | ![1SCREEN-B.gif](1SCREEN-B.gif "") |

## Final Notes

Whilst the abilities of the GetCalc( command make it harder to create multi-calculator programs, it certainly is not impossible. You just need to think extra hard and create very clever workarounds to its boundaries.

If you have any questions or comments about these routines please ask in the discussion area for this page.

## References
- James Kanjo came up with the "Multi-Calculator Core" code in his [IM](instant-messenger.html) program, and also came up with the "turn by turn battle" code, including the function to make one calculator respond to another calculator's ENTER keypress
