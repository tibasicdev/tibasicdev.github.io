# Custom Menus
Menus are often used in programs to choose options, allowing a program to have multiple functions, or a game to have extra features. Though the [Menu(](menu.html) command creates a perfectly functional menu, sometimes you want your program to use something more fancy, to have a differently-functioning menu, or just to stand out from the others with a menu that looks different.

However, a custom menu is usually 2 to 3 times the size of the same menu written with the Menu( command - the difference is between a menu that takes up 150-200 bytes and one that takes up 50-100 bytes.

## Basic Menus

This covers the basics of creating a functioning custom menu. Remember to [set up](setup.html#toc6) the graph screen before displaying the menu, to avoid something like axes covering the menu.

**Numerical Input**

The simplest way to create a custom menu is just to display the title, and a numbered set of options. Then, wait for a number key to be pressed, and act accordingly.

The following code is an efficient way of waiting until a number key is pressed, and converting it to a number N:

```
:Repeat 2>abs(5-abs(5-abs(Ans-83)))
:getKey
:End
:round(13fPart(Ans/13))→N
```

But you might not always need to convert the number at all. If all you're going to do with the option is go to a different part of your code, you might just want to use the getKey value for comparisons. And if you only have a small number of options, it's easier to check for them all explicitly rather than using the [abs(](abs.html) command as above: for example, Repeat max(Ans={92,93,94}) will check for the keys 1, 2, and 3.

**Arrow Key Input**

If you want to get slightly more fancy, you could provide a cursor, such as an arrow or ">" symbol, that points to the selected option (there are many ways to display this). The first thing you'd do is display the title and the options, just as in the previous case (except you wouldn't need to number them). Then create a variable that stores the option currently chosen. 

For the rest of the code, you would need a loop, structured roughly as follows:

Loop until a selecting key (such as enter) is pressed
Display a cursor at the currently chosen option
Wait for a key to be pressed
Erase the cursor
If an arrow key was pressed, change the chosen option variable
End of the loop

It is important that you actually wait for a key to be pressed, instead of just storing the key to getKey. The loop will work both ways, but if you don't wait for the key, then it will go through the loop even when no key is pressed, erasing and redrawing the cursor, which causes flicker. Another way to eliminate the flicker is to only erase the cursor if an arrow key was pressed.

You can use Boolean optimizations to quickly adjust the option based on the arrow keys:

```
:N+(K=34 and N<(# of options))-(K=25 and N>1→N
```

Another possible optimization is to use the row coordinate of the option, rather than the option number, for the value you store (but then you need to modify it by the row difference between two options, rather than 1, when arrow keys are pressed)

**Labels vs. Values**

The Menu( command goes to a label when an option is selected, whereas both of these methods return a value. It's fairly easy to go back and forth between these methods. To convert from a value to going to labels, add If statements like:
```
:If N=92
:Goto 1
```

To convert the Menu( command from going to labels to returning a value, use code like this:
```
:1
:Menu("TITLE","OPTION 1",1,"OPTION 2",2,"OPTION 3",3
:Lbl 3:Ans+1
:Lbl 2:Ans+1
:Lbl 1
```

1 is stored to Ans. If 1 is chosen, the Menu( command goes to Lbl 1, and this code finishes with Ans=1. If 2 is chosen, the Menu( command goes to Lbl 2, where Ans is increased to 2, then the code goes to Lbl 1 and finishes. If 3 is chosen, the Menu( command goes to Lbl 3, which has 2 Ans+1 commands after it, so Ans is increased twice: to 3.

However, it's usually easy to avoid using labels with menus.

## Advanced Menus

This section covers advanced techniques your custom menus might use.

**Multi-page Menu**

(this section is based on [this menu routine](http://weregoose.unitedti.org/routines.html#multipagemenusystem) by Steve Hartmann)

A multi-page menu could be used for as many options as you wanted, and is another reason to use a custom menu routine. To create a multi-page menu, you would need a loop which displays the current page (most likely with some If statements), then does the necessary operations for a normal menu until either an option is selected or the left/right arrow keys are pressed. If an option is selected, obviously you exit the loop; otherwise, you change the page number but stay in the loop.

The most complicated situation you could be in is a multi-page menu operated completely by arrow keys. Here, you'd use a total of three nested loops: one for the page, another for the menu itself, and a third for waiting for a key.

**Selecting Options**

In an arrow-key operated menu, you have several options for the cursor. The simplest is to draw some sort of symbol next to the option currently selected. This could be embellished by [animating](animation.html) the symbol - a little tricky, because it must be done inside a getKey loop. Here is an outline of the code to do so:
```
:Repeat K
:For(I,1,(some limit))
:(draw Ith step of animation)
:getKey→K
:I+(limit)*Ans→I
:End
:End
```

Inside the getKey loop, a For( loop goes through all the frames of an operation. This by itself would take too much time - even if you pressed a key, you would have to wait for the animation to cycle entirely. To prevent this, we add the line I+(limit)*Ans→I. Ans holds the value of getKey, which is 0 if no key was pressed, and not zero otherwise. So if no key was pressed, we're adding 0 to I, which does nothing. If a key was pressed, however, we add a large value to I which puts it beyond the range of the For( loop, to exit the For( loop immediately. If the For( loop has a small limit, like For(I,1,10), you can simply add getKey to I, since getKey is at least 11 if it's not 0.

**Program Structure**

Most people reading this page probably are familiar with the reasons to avoid [Goto](goto.html) and labels, and do stay away from them usually. However, menus complicate the situation enough that a lot of calculator programmers give up and use labels anyway, creating a program that's impossible to understand or to maintain because of the complex web of Goto commands. This doesn't need to happen - you can structure your code so that labels are unnecessary. The important part is to create this structure first, and then build the program around it, rather than writing a program and trying to tack a menu onto it later.

Suppose your menu chooses among several options which should run and go back to the menu, and a final Quit option. The structure for your program could look like this:
```
:Repeat choice=Quit
:(menu that sets 'choice')
:If choice=Option 1:Then
:(run option 1)
:End
...
:If choice=Option 35:Then
:(run option 35)
:End
:End (the outermost loop)
```

The weakness in this code is that the variable your choice is stored in can't be modified by any of the options, or else you risk setting it to the value of an option that's yet to be checked for (which in that case will also run before you get back to the menu). To get around this, any options that modify this variable should DelVar it at the end of their If-Then-End block, then it won't interfere with anything else (theoretically, you could use the variable Ans, and then instead of DelVar add the line :0)

**Examples**

Some sample programs with a simple number menu, cursor-based menu, and animated cursor-based menu:
- [NUMBER.8xp](http://tibasicdev.github.io/local--files/custommenus/number.zip)
- [CURSOR.8xp](http://tibasicdev.github.io/local--files/custommenus/cursor.zip)
- [ANIMATED.8xp](http://tibasicdev.github.io/local--files/custommenus/animated.zip)

You can also download all three in [one file](http://tibasicdev.github.io/local--files/custommenus/custommenu.zip).

You can find a sample multi-page custom menu program [here](http://weregoose.unitedti.org/routines.html#multipagemenusystem).

## Scroll Bar

Moreover, you can add a vertical scroll bar. The scroll bar is a nice feature which not only looks good but also gives the user an overview of the menu.

First, you need some variables. You can use a list, in this case L(SCBAR).

| 1 | P<sub>Start</sub> | The point where the scroll bar starts |
| 2 | P<sub>End</sub> | The point where the scroll bar ends |
| 3 | E<sub>Total</sub> | All of your options or elements in total |
| 4 | E<sub>Above</sub> | All of the invisible options above the visible elements |
| 5 | E<sub>Below</sub> | All of the invisible options below the visible elements |
| 6 | L<sub>Start</sub> | Point where the scroll bar would start if 100% of the elements were visible |
| 7 | L<sub>End</sub> | Point where the scroll bar would end if 100% of the elements were visible |

First, we need to calculate P<sub>Start</sub> and P<sub>End</sub>:

```
LSCBAR(6)+LSCBAR(4)*((LSCBAR(7)-LSCBAR(6))/LSCBAR(3))->LSCBAR(1) // P,,Start,, = L,,Start,, + E,,Above,, * (L,,End,, - L,,Start,,)/E,,Total,,
LSCBAR(7)-LSCBAR(5)*((LSCBAR(7)-LSCBAR(6))/LSCBAR(3))->LSCBAR(2) // P,,End,, = L,,End,, + E,,Below,, * (L,,End,, - L,,Start,,)/E,,Total,,
```

Simple percent math ;)

For the scroll bar you just draw 3 lines:

```
Line(93,-LSCBAR(1),93,-LSCBAR(2) // 93 is the X-Coordinate where the scroll bar will be drawn
Line(92,-LSCBAR(1)-1,92,-LSCBAR(2)+1 // Makes the scroll bar look better
Line(94,-LSCBAR(1)-1,94,-LSCBAR(2)+1
```

Finally, you could theoratically also draw a horizontal scroll bar, you just need to replace the variables with other values and the line commands.
