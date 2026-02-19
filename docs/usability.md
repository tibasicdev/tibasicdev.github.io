# Usability (User-Friendliness)
|**This article is part of the planning stage of the [development](development.html) cycle.**|
| --- |

Imagine you are using a program for the first time. You have no prior knowledge about the program; someone just put the program on your calculator without giving you any instructions and now you are trying to figure out how to use it. After literally pressing all of the keys on the calculator and trying all sorts of key combinations, you give up and and delete the program.

This example isn't based off any one particular program, but it does resonate with lots of program users who have had a similar experience. What this problem really is about is poor user-friendliness — more commonly known as usability. The definition of usability is simply how easy it is for people to use a program.

While usability can take on many different forms, there are some essential things that you can do to make a program more user-friendly.

## In-Program Help

Probably the easiest way to make a program user-friendly is by including some in-program help. While you ideally want your program to be so easy to use that a user can simply pick it up and figure out how to play it, not every game is so straightforward, and the average user probably needs some help.

The best place to include help in a program is as one of the options in the program's main menu. When the user comes across the menu, they will see the help option and they can select it to view the help. The help does not need to cover every minute detail about the program, but rather just explain the objective of the game and detail what keys are used for controls.

```
:Menu("Some Game","Option 1",1,"Option 2",2,"Help",3
...
:Lbl 3
:Disp "Game Objective
:Disp "Key = Function
```

Because most people do not like using help unless they have to, you should try to limit your help to one or two screens at most. At the same time, if you have an extremely complex game with all sorts of features and lots of keys are needed to operate it, then it would be appropriate to include help for all of those things. The general guideline is that the amount of help needed correlates to the size of the game.

## Protect the User

The next thing you can do to make a user-friendly program is to protect the user from themselves. Often times in a program you will want to think about what could go wrong and try to either prevent it from happening or tell the user what's wrong. Preventing it from happening involves you, the programmer, programming in safety protections for the user so that they aren't even aware that something went wrong.

Say the program calls for the user to type in a number between 1-1000, and the user types in 5000. If your program just goes on with this value, it will probably crash at some point later on. Rather, it's necessary to check the value, and display an error message and ask for the number again if it's wrong. The error message does not need to be complicated or long — just enough so that you can provide some direction on what input you are expecting the user to enter.

```
:Disp "Enter a Number
:Input "Between 1-1000",A
:While A<1 or A>1000
:Disp "Must Be 1-1000!
:Input "Number",A
:End
```

Of course, just checking to see that the number is in the appropriate range is sometimes not enough. You might also want to check to see whether the user tried to enter text or a list for input. Because there is no viable way to perform those checks when dealing with a real variable, a better option would be storing the input to a string and performing the [validation](validation.html) on it, and then converting the string to a real variable.

## Include Helpful Features

Another part of making a user-friendly program is to include helpful features. Since the target audience is often in high school, a feature sure to be appreciated is a "teacher key." This is a special key that the user can use to quickly exit the program. When the teacher comes around, they then want to be able to get back to the [home screen](homescreen.html) so that they don't get their calculator taken away.

This problem is quite easy to prevent with a teacher key. In every program there is a main loop that runs throughout the life of the program. You need to add a check for whatever teacher key you want at the place in the main loop where you check for user input. While you can have any key function as the teacher key, the community standard is usually MODE or DEL. (It is probably best for you to continue this so that users don't have to deal with figuring out which key is the teacher key.)

```
:While main loop not finished
:Display something
:Perform calculations
:Get user input
:If teacher key pressed, exit program
:End user input
:End main loop
```

## Progress Indicators

In games that use [maps](maps.html), the program has to go through the list of maps and then load the appropriate one for the user to use. Depending on the size and number of maps, this can take a while. If the user doesn't know what is going on, they probably will think the program stalled or something else went wrong.

While there are a couple different ways you can cut down on the loading times for maps (see [subprograms](subprograms.html) and [compression](compression.html)), the easiest way to solve the problem is by simply telling the user what is going on and showing the user some progress. You don't have to do anything fancy (in fact, you probably shouldn't because that would just waste valuable memory), just something to help the user understand the situation.

For example, say you are randomly placing mines throughout the map (it's a Minesweeper game), you then could just display a "Placing Mines" message on the screen and have a loop for the progress indicator that matches the current map loading:

```
:Output(3,2,"Placing Mines
:For(X,1,20
: // fill the map with mines
:Output(4,6,5X
:End
```

## Follow the KISS Principle

The last important point of usability is following the KISS principle. For those who haven't heard of KISS, it is an acronym which stands for Keep It Simple Stupid. The basic point of KISS is to not clutter your program with unnecessary features and useless fluff. It also entails making the program easy to figure out for those who don't have access to a readme.

It is not uncommon to see a TI-Basic math program (i.e., quadratic solver) that has a menu, about screen with scrolling credits, and includes some game in case you somehow get bored solving quadratic equations. While those things by themselves aren't bad, they are completely inappropriate in a math program. There is a certain elegance that comes with "programs that do one thing and do it well." This is known as the [Unix philosophy](https://en.wikipedia.org/wiki/unix_philosophy), and should really be what every program strives for.

<center>

|**[<< Portability](portability.html)**|**[Overview](development.html)**|**[Program Setup >>](setup.html)**|
| --- | --- | --- |

</center>
