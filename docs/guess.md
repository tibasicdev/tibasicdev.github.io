# Guessing Game
> **Note:** This page was originally created by AtionSong on the TI-Basic wiki, and has been added here because TI-Basic wiki is in the process of being merged with this wiki. In addition to this page, only those pages which weren't already duplicated on this wiki were added.

### Summary

Guessing games are one of the simplest types of games: a number is chosen by the system, and the user tries to guess what it is. Our program will also tell the user whether their guess is higher or lower than the actual number.

### Program

**Needed Commands:** [randInt(](randint.html), [Input](input.html), [Disp](disp.html), [If](if.html), [Goto/Lbl](goto.html), [=](equal.html), [>](greaterthan.html), [<](lessthan.html)
**General Commands:** [ClrHome](clrhome.html), [Output(](output.html), [Pause](pause.html)

Like it has been said elsewhere, interactivity is one of the key points to making a good program. To start our guessing game program, we are going to either let the user pick his level of difficulty or enter the numbers the computer is going to pick a number between. Your program should only have one of these beginnings, but both are listed for you to choose from.

***Opening Screen***

```
prgmGUESS
:Lbl A
:ClrHome
:Output(1,1,"????????????????
:Output(2,2,"GUESSING GAME
:Output(3,1,"???????????????
:Output(5,1,"PROGRAMMED BY
:Output(6,3,"TI-BASIC WIKI
:Pause
:ClrHome
```

***Enter Own Numbers***

```
:Output(2,1,"ENTER NUM 1
:Input ":",A
:Output(4,1,"ENTER NUM 2
:Input ":",Z
```

***Select Level of Difficulty***

```
:1→A
:Input "Range - 1 to:",Z
```

Both of these should be followed by the random selection of the number, using the following code:

```
:Lbl 1
:randInt(A,Z→X
```

We then let the user guess, and give them feedback on whether their number is correct or not, and whether it's too high or too low.

```
:Lbl 2
:Input ":",Y
:If X=Y:Then
:Goto 4
:Else
:Goto 3
:Lbl 3
:If Y>X:Then
:Disp "TOO HIGH"
:Goto 2
:End
:If Y<X:Then
:Disp "TOO LOW"
:Goto 2
:End
```

Then, we create a screen that tells the user that they are correct and then sends the beginning.

```
:Lbl 4
:ClrHome
:Output(2,1,"YOU GOT IT RIGHT
:Pause
:ClrHome
:Goto A
```

This program is a great way to start testing your abilities with programs that use advanced mathematical procedures (such as Fighting RPG's). You can make your program better by adding things such as:
- Creating a number of guesses the user must guess the answer in (*HINT*:Add another If/Then command and variable)
- Giving a hint option to the user (*HINT*: Set for specific number of guesses)
- Give you "YOU GOT IT RIGHT" screen a little [animation](animation.html)
