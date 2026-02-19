# 68k TI-Basic for 83 TI-Basic Programmers
This tutorial is meant as an introduction to 68k TI-Basic for programmers that already are fairly experienced with TI-83 series Basic programming. Instead of re-teaching many things, this tutorial highlights the differences between the two languages.



## Major Features

A major novelty of the 68k calculators is the ability to make symbolic calculations. This has many applications: you can deal with expressions such as x<sup>2</sup>+2*x+1 but treat x as an unknown, or deal with the exact value of √π/3 without approximating it with floating-point values.

The calculator no longer has some statistical commands, but has much more powerful calculus commands (it can do symbolic derivatives, integrals, and finite and infinite sums, among other things). This doesn't have any immediate programming applications, although you can often find an unexpected use for these commands.


A very programming-relevant difference, on the other hand, is the advent of error catching. Using the [68k:Try](68k:try.html) and EndTry statements, your program can identify if an error has occurred, and possibly even recover from this (or at least display a custom error message). 

Also one of the highlights is how much pictures have been empowered.  They now can be any size and be displayed with any logic.  True "real-time" multiplayer games is now possible with the SendCalc Command, something that was impossible on 83's.

The more specific differences described below tend to combine to make programs run faster, and allow for a programming style closer to programming a more "serious" language on a computer.

## Commands

On the TI-89, commands can be entered letter by letter, and don't have to be chosen from a menu. In practice, programs and functions are [tokenized](68k:tokenization.html), making a command range take up 1 to 3 bytes in a program.

Many commands have been added or removed between the two languages (see the [68k:command index](68k:command-index.html) for a full list of commands). In addition, the following commands have changed in spelling:

- [1-Var Stats](1-var-stats.html) and [2-Var Stats](2-var-stats.html) are now [68k:OneVar](68k:onevar.html) and [68k:TwoVar](68k:twovar.html).
- [End](end.html) has been split into [EndIf](68k:if.html), [EndFor](68k:for.html), and others
- [prod(](prod.html) has been renamed to [68k:product()](68k:product().html)
- All of the drawing commands have been split into pt and pxl equivilants. eg. line is now either line or pxline.


There are two more overall changes. First, many commands' names have been truncated where they were longer than 8 characters: this is the maximum for a command name on the TI-89. An example is [68k:RclPic](68k:rclpic.html), the 68k equivalent of [RecallPic](recallpic.html).

Second, the use of parentheses after a command now follows a strict convention. 
- "Instructions" — commands that do not return a value — do not require parentheses (e.g. [68k:If](68k:if.html), [68k:Text](68k:text.html), etc.)
- "Functions" — commands that do return a value — require parentheses (e.g. [68k:sin()](68k:sin().html), [68k:setMode()](68k:setmode().html), etc.)
- Even functions with no arguments use parentheses (e.g. [68k:getKey()](68k:getkey().html), [68k:startTmr()](68k:starttmr().html), etc.)

Many commands have been added. However, as far as statistics goes, the 68k calculators are inferior, even, to the TI-83 series; most of the functionality is now restricted to regressions, and the calculator doesn't even know internally how to calculate most probability distributions.

## Variables

The way variables are stored has undergone major changes from the TI-83 series. All variables now share a common naming system: the name of a variable can be up to 8 letters long. Variables can also be placed in different folders, which can't be nested but otherwise are very similar to file folders on a computer. By default, variables are stored in the folder 'main'.

On the surface, the variable types are much the same as they were on the TI-83 calculators: you have numerical variables, lists, matrices, strings, picture variables, equations, graph databases, and a new one, called "data". These are slightly different, however. To begin with, numerical variables can now be either floating-point (the same as on the TI-83 series) or integer variables (that don't have a decimal place, but have several hundred digits of precision). As a consequence of the symbolic operations on a 68k calculator, you also have expressions: formulas that are only evaluated as much as possible.

List are very different.  They now can hold any combination of numbers, expressions, and character strings.  This makes them more powerful, but also slows them down significantly.  Data's are basically matrices, but with the new capabilities (and speed limitations) of the new lists.  Matrices stayed the same though, limited to numbers, but retained their speed.  You can effectively emulate an "old style" list by using a matrix with only 1 row/column,

Boolean variables will also cause some confusion for TI-83 programmers: Instead of boolean (true/false) operations returning a one or a zero that can be used in the same manner as regular integers (1, 3, -5, 4.8, etc.), boolean variables now all have a class of their own. This means that you can't use a simple "If (variable)" statement to check whether a variable has yet been defined, and can't use shortcuts in expressions that involve a parenthetical boolean statement determining whether a certain term in the expression is used (e.x. (k>2)(x+1)+3x). Instead, you will have to use the ifVar() command to check whether a variable has been defined and return to regular If-Then blocks for conditional computing.

## Programs

Programs are also considered variables, on the same level as any other: you can even define a program within another program. They imitate built-in commands, and can even be given parameters. Using the [68k:Local](68k:local.html) command, you can declare local variables that are reset to their old values once a program finishes running.

You can also define functions, which are similar to programs but return a value. Functions have some other limitations, though: they can only use local variables, and can't modify any global aspects of the calculator (so graphical commands, for example, are limited to programs).

With local variables, and the ability to define functions and programs, you can program in a procedural language style. Instead of placing the entire code of the program in one block, you can split it up into functions and subprograms that are defined at the beginning of the main program.

The entire issue of memory leaks (caused on the TI-83 series by jumping out of code blocks with Goto) is no longer present in 68k TI-Basic. Loops have offsets linking the end to the beginning, so the program doesn't need to keep a stack to be aware of what to do with End instructions. There is no longer any memory cost to entering a loop (or any other kind of code block), so it's impossible to leak memory this way.

## Optimizations

Most types of trivial optimizations from the TI-83 series are invalid on the 68k calculators. For example, closing parentheses, quotes, and brackets are now mandatory — but don't add any size to the program, since it's [tokenized](68k:tokenization.html) and converted to postfix notation. The [Ans](ans.html) variable no longer plays an important role: though the [68k:ans()](68k:ans().html) command does exist to replace it, it's not modified by storing to variables inside a program, so it's mostly useful on the home screen.

A large part of 68k optimization revolves around careful use of lists. List variables are no longer random access: accessing the last element of a list is much slower than accessing the first element. For this reason, going through a list in a [68k:For](68k:for.html) loop is about the worst thing you could do.

## Graphics

68k gives the programmer much more options with displaying graphics. [68k:Sprites](68k:sprites.html), which had to be displayed using various tricks or libraries on a TI-83 series calculator, are built into 68k as picture variables. These picture variables bear little resemblance to the screenshot-like functionality they have on a TI-83+. They can be any size from 1x1 to the entire screen, and can be stored from and recalled to any part of the graph screen. There are even several commands for displaying a sprite using different logic.

Apart from these very powerful commands, more ordinary commands have also been buffed up. Virtually all graphics commands have a point and a pixel equivalent, so you're free to choose one or the other to use (usually, you'll want pixels). The Circle command now draws circles instantaneously, as opposed to taking several seconds. 

Instead of being forced to choose between home screen and graph screen, the choice is between graph screen and "Program I/O" screen on the 68k calculators. The program I/O screen is a separate home screen for programs, which is limited to text (but the text doesn't have to be aligned). In addition, both screens can be spiced up using [68k:dialogs](68k:dialogs.html), which imitate the appearance of a popup window on a computer, and are great for inputting data without having to erase anything from the screen.

Another major addition to the graphics command set is the newly created Dialog feature. New commands add extra I/O capability that doesn't interfere with the program I/O or the graph screen, allowing for enhanced in-program data entry.

There is one limit to graphics on the 68k calculators - they cannot draw over the top menu bar and bottom status bar, so are effectively limited to only 2/3 of the screen. Assembly libraries can be used to access the entire screen, but this is impossible in TI-Basic alone.

## Closing Words

This page gives an overview of some of the features of 68k, but it isn't, and cannot, be complete. There are other pages you could visit to get a better picture of 68k programming:
- [68k:Command Index](68k:command-index.html)
- [68k:FAQ](68k:faq.html)
- [68k:Sample Programs](68k:sample-programs.html)

However, the best way to try to learn the language is first-hand experience with it.
