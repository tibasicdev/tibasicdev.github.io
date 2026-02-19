# Setting Up A Program
|**This article is part of the coding stage of the [development](development.html) cycle.**|
| --- |

At the beginning of a program, you typically setup everything that the program will use while it's running. Of course, there are lots of things that you may decide to include in your individual program setup, but the three main things that you should include are: the home screen, graph screen, and initializing variables. There are also some general, but crucial mode settings that should be taken care of.



## General Settings

There are some general mode setting that you'll want to pay attention to. Most of those should be what you want, but there is always a chance that a program forgot to switch back to the standards, or that the user was playing around with the calculator.

In the mode menu, there are probably four different modes you need to worry about. These are numeric notation, decimal, real/complex mode, and screen display.

#### Numeric Notation

How numbers are displayed/returned: Normal, Scientific, and Engineering. Scientific will have one digit on the integer side, and Engineering will have two digits. The standard is Normal.

#### Decimal

In programs that use pinpoint precision numbers or require complex formulas or calculations, the number of decimals returned can greatly affect the program. Float will automatically adjust to the number of digits the calculator considers significant. Fix 1-9 will fix the calculator to display 1-9 digits, no matter what. This means that the calculator may sometimes give weird results such as 3.100000, or pi=3.

#### Real/Complex Mode

The default mode, Real, will give [ERR:NONREAL ANS](errors.html#nonrealans) whenever a complex number is obtained as a result. If you want to use complex numbers, you should change this setting to a+bi or re^θi (the distinction between these two is only a display one).

If you're going to be using complex numbers, you should switch away from Real mode. Otherwise, it's an inessential setting. Switching to Real mode doesn't have any real (he he) purpose to it, since it doesn't provide any extra functionality - unless of course you like it when your calculator throws errors.

#### Screen Display

This affects the screen display. Full is probably the one of the only ones you have ever seen. Horiz displays a horizontal split-screen, with the graph on top and home screen on bottom. G-T displays a vertical split-screen, with graph on left and table on right. The standard is Full.

## Home Screen

Since the [home screen](homescreen.html) that your program uses is the same home screen that the rest of the calculator uses, the previous program call(s) and any other text is typically still displayed on the screen. Obviously, you don't want to be displaying text and have it interrupted by other text, so you need to clear the home screen. The [ClrHome](clrhome.html) command is what you use.

When using the ClrHome command, you simply place it on a line. The whole home screen will be cleared of any text; there's no way to clear a smaller portion of the ClrHome because it takes no arguments.

```
:ClrHome
```

## Graph Screen

The typical TI calculator user uses the [graph screen](graphscreen.html) to graph, which means they use axes, stat plots, Y= equations, and sometimes the grid. They might also like drawing things with the drawing commands or the Pen. However, while working in a game in use of the graph screen, you really do not want these functions to appear, which would completely mess up your program.

First, you need to disable all these annoying thing by the following code:

```
:ClrDraw     // Clears the graph screen of all its contents
:AxesOff     // Disables X and Y axis scaling view
:FnOff       // Disable Y= equations
:PlotsOff    // Disables stat plots from appearing
:GridOff     // Disables grid from appearing
```

After that, you setup the window dimensions to use a [friendly window](friendly-window.html). This not only makes drawing much easier, but it is faster and smaller. One way to do this is shown below:

```
:0→Xmin:1→ΔX
:0→Ymin:1→ΔY
```

## Initialize Variables

If you have any important [variables](variables.html) that you use in the main program loop, you should initialize them here, so the program will be able to use them and not have a delay. This is especially important with large variables (such as lists, matrices, and strings), since initializing those variables inside the main program loop will definitely have an impact on its speed.

```
:{1,2,3,4→A
:[[1,2][3,4→[A]
:"1234→Str1
```

## Putting It All Together

Putting all the parts of program setup together, here is a typical way to start a program:

```
PROGRAM:SETUP
:ClrHome
:ClrDraw
:AxesOff
:FnOff
:PlotsOff
:GridOff
:0→Xmin:1→ΔX
:0→Ymin:1→ΔY
:{1,2,3,4→A
:[[1,2][3,4→[A]
:"1234→Str1
```

Of course, you only have to include the things that you actually use. If you don't have any important variables to initialize, then simply leave that off. In the same fashion, you don't have to clear the clear the home screen if your program just runs on the graph screen.

<center>

|**[<< Usability](usability.html)**|**[Overview](development.html)**|**[Code Conventions >>](code-conventions.html)**|
| --- | --- | --- |

</center>
