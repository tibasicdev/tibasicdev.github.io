# Planning Programs
|**This article is part of the planning stage of the [development](development.html) cycle.**|
| --- |

Before writing any of the code for a program, you should carefully plan out the program. This may seem like an unnecessary step, time that could be better spent, but it will pay major dividends in the end. Planning not only results in better quality programs, but many times it will also cut down the coding time (since you don't have to waste time rewriting the program) — a win-win situation!

The first thing you want to do when planning a program is to decide what the program will do. Beginner programmers often say that they want to create a cool game, but they don't get much farther than that. For them to have a real chance of creating their program, they need to determine what the objective of the program will be, and then build off of that. For program ideas, see the [project-ideas](project-ideas.html) page.

When coming up with an idea for a program, you should try to be realistic about the [limitations](whytibasic.html) of TI-Basic, and what a program can and can not do. For example, a game that needs lots of speed to be worthwhile for the user to play, such as Phoenix or Mario, really isn't very practical in TI-Basic beyond only moving a few things on the screen at any one time. In addition to speed, TI-Basic also suffers from limited graphics capabilities.

Once you have determined what the program will do, you need to decide what features the program will have. This can include: potential program options, the interface ([home screen](homescreen.html) or [graph screen](graphscreen.html)), main menu, an about screen, user help, and any other things you may want. The more thorough you are with planning your program, the easier the coding will be; it is to your benefit to do a good job.

If you can't come up with any ideas for your program or you are unsure of if the ideas that you have come up with make sense, you should get input from the TI community. The four most friendly, active user forums are:

- [Cemetech](http://www.cemetech.net)
- [CodeWalrus](http://codewalr.us)
- [Omnimaga](http://www.omnimaga.org)
- [Revsoft](http://revsoft.tifreakware.net/)


Since these are some of the people who will be using your program when it is finished, you should ask them to evaluate your program concept and to offer some constructive criticism. They might also be able to give you some new ideas that you never thought of.

Even if you thoroughly plan a program and get community input, it's simply not possible to think of everything up front. While making changes later on when a program is in heavy development can be a lot more work than making those changes at the beginning, there's nothing wrong with changing or modifying your plans, if you believe the program will be better with the change(s).

## Research Before Coding {#research}

Before doing any coding, you should do some research to determine what the best algorithms are for use in your program. One of the most common problems is a poorly though out algorithm, which may not work properly with other parts of the program.

When you do research you ensure that the algorithm is appropriate and that it will work effectively. This helps eliminate flaws in your algorithm, which can cause a multitude of errors if left unfixed. If you think your program through before you start coding, you can save yourself lots of time because you don't have to do several rounds of testing and debugging to get your program to work the way it should.

One of the ways to test an algorithm and how effective it will be in your program is to take a very small problem and trace by hand how your chosen algorithm would work in that situation. This allows you to see if the algorithm will actually work in the given situation.

If the algorithm doesn't work, you can immediately start looking for another algorithm. This saves you lots of potential time because you would have to come up with another algorithm had you just started coding it. Only when you are confident with the algorithm should you start the coding.

## Translate It Into Pseudocode {#pseudocode}

The next step in the process is turning the program plans into pseudocode. Psuedocode involves using English (or whatever language you speak) in place of the TI-Basic code to describe what the program will do to perform the desired functions and tasks. This prevents you from getting caught up in the TI-Basic syntax, allowing you to more clearly focus on the program.

You should first start by looking at the big picture of the program and then break it down into smaller and smaller details. Using an outline as the base, this means you would put the most important things first and then gradually add everything else. This allows you to mentally picture what the program is going to look like and to make sure you don't forget anything.  Remember to leave many times more space than you think you'll need for an outline, you'll probably end up discovering a few areas you hadn't thought of yet that need to be taken care of.

An important part of creating useful pseudocode is adding [comments](comments.html) throughout. It is very easy to get lost in your logic or have problems come up that you don't have any idea on how to resolve. Besides telling you what the code is supposed to do (i.e. making coding easier), it will also force you to slow down and think through the logic of your program. Still, comments are only as good as you make them.
## Use Many Small Programs While Coding {#small-programs}

A single large program quickly becomes unwieldy and difficult to manage. While you're still editing the program, it's best to keep it in many small pieces. When you're done, you can combine them into one program again.

One of the benefits of this approach is that you can convert pseudocode into a main program almost right away. For example, imagine this pseudocode program:

```
Main Menu - user enters difficulty, etc.
Initialize variables
Main Loop:
 Player movement
 Draw player
 Enemy movement
 Draw enemy
 Check Win/Loss Condition
End Main Loop
If we won the game
 Display win message
Otherwise
 Display loss message
Cleanup
```

You could translate this into a basic program almost directly. Here's how we do it (note that we don't write any code yet):

```prgmMAINMENU  // user enters difficulty, etc.
prgmINITVARS  // initialize variables
Repeat Z
prgmMOVEPLR  // moves player
prgmDRAWPLR  // draws player
prgmMOVENMY  // moves enemy
prgmDRAWNMY  // draws enemy
prgmWINLOSE  // sets Z to 1 or 2 if we won or lost
End
If Z=1:Then  // we won
prgmWEWON  // says "You win!"
Else
prgmWELOST  // says "You lose!"
End
prgmCLEANUP  // delete used variables
```

As you progress in writing the actual code, you create and edit each individual program (for example, you would create and edit prgmMAINMENU and write a menu in that program). Of course, if these sub-programs are big enough, you can split them up into their own sub-sub-programs in the same way.

When all the subprograms are finished, the program will work as it is, in 50 or so pieces (so you can test for bugs and tweak the individual programs). However, if you want to release your program, you probably don't want there to be 50 small programs to send. You can use the Recall feature (press [2nd][STO] to get to it) to combine the programs.

Go through the main program. Every time you get to a sub-program call, clear that line and press [2nd][STO]. The Recall option will come up. Press the [PRGM] key and select the appropriate sub-program from the EXEC menu. The calculator will paste that sub-program into the main program. When you're done, all the code is in your main program (and you can delete the now-unnecessary sub-programs)!

<center>

|**[<< Creating New Program Versions](creating-new-program-versions.html)**|**[Overview](development.html)**|**[Portability >>](portability.html)**|
| --- | --- | --- |

</center>
