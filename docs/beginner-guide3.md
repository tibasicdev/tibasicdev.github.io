# Visual Magic
> **Note:** This page was originally created by AtionSong on the TI-Basic wiki, and has been added here because TI-Basic wiki is in the process of being merged with this wiki. In addition to this page, only those pages which weren't already duplicated on this wiki were added.


### Using the Graph Screen

In this section of the tutorial, you will learn how to use the [Graph Screen](graphscreen.html) to create visual programs.

A good way to start is to put INPUT into the program code alone. A line with simply [Input](input.html) will take you to the graphing screen and give you a cursor to click in the screen. You might want to take off the Axis, Grid, and Coordinates first, by putting [AxesOff](axesoff.html), [GridOff](gridoff.html), and [CoordOff](coordoff.html) before the Input

TI-BASIC gives several functions for drawing to the graph screen which are easily accessible through the draw menu ([2nd][prgm]). For most programs that use the graph screen, it is a good idea to put "[StoreGDB](storegdb.html) 1" at the beginning and "[RecallGDB](recallgdb.html) 1"  at the end. This stores the current graph state and restores it at the end, so when you change the graph state by using a function like [AxesOff](axesoff.html), the graph screen doesn't stay changed after the program is finished.

### The Text Function

Let's get started with a small hello world program graph screen style (I know, I hate hello world programs too, but bear with me). This program uses the [Text(](text.html) command and should display in a small font. All commands used are accessed from the draw menu and everything following a "//" is a comment and shouldn't be typed in.

```
Program:HELLO  // Program name
:ClrDraw  // Clear the graph screen
:Text(1,1,"Hello  // Display text "Hello" at the top left corner of the screen
```

If you run it, you should see the word hello appear in the top left corner of the screen. Notice how we did not put "StoreGDB 1" at the beginning? It was not needed, because we did not change The screens axes or change the way the graph screen is shown. The text function draws on a different coordinate system. The X axis stays the same, but the y axis is up side down. This chart might help explain better

```
        X-Axis
 |_|1|2|3|4|5|6|7|8|9|
 |1|_|_|_|_|_|_|_|_|_|
 |2|_|_|_|_|_|_|_|_|_|
 |3|_|_|_|_|_|_|_|_|_|
 |4|_|_|_|_|_|_|_|_|_|
 |5|_|_|_|_|_|_|_|_|_|
 |6|_|_|_|_|_|_|_|_|_|
 |7|_|_|_|_|_|_|_|_|_|
 |8|_|_|_|_|_|_|_|_|_|
 |9|_|_|_|_|_|_|_|_|_|
```

The Text function takes 3 arguments in the form of Text(x,y,text. They are used as follows

| Arg | Usage |
| --- | --- |
| x | The X coordinate of the text |
| y | The Y coordinate of the text |
| text | The text to be displayed |

#### Simple Graph Screen Text Animations

Note: The following is a very simple, very slow animation, but don't think this is all! There are many other ways to create text animations, many of which you will learn in this tutorial.

With the simple knowledge of the Text and ClrDraw functions, and knowing how to use a few basic loops, you can make your very own(very simple) text animation! Start your loop. We'll use a [For(](for.html) loop because they are considerably faster than all other loops, but any loop will do:

```
:For(C,1,50,2
```

Next, draw the text you want to draw to the screen:

```
:Text(C,1," (Your Text Here)
```

Add a time waster, so the loop doesn't go to fast for you to see:

```
:For(D,1,100
:End
```

Clear the Screen:

```
:ClrDraw
```

Close the first For loop:

```
:End
```

And we're done! That wasn't so hard, was it? No. Stick around, there are plenty more graph screen functions to learn about!

To be continued...
