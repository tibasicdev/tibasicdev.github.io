# TI-Nspire for TI-83 Programmers
This tutorial is meant to teach new Programmers about the TI-Nspire. This is a simple introduction to Nspire TI-Basic for programmers that are already fairly experienced with TI-83 series Basic programming! Instead of re-teaching many things, this tutorial highlights the differences between the two languages. 



## Major Features

A major features of the older Nspire calculators is the simplicity of programming. It has a very strange layout compared to the other TI graphing calculators. First, all the letters get their own buttons, making it a little easier to type than on the 84. Also, it has a [nspire:ctrl](nspire:ctrl.html) key rather than a 2nd key. It has a clicker key, menu key, catalogs, enter, and even a caps key. If you observe it long enough, it begins to resemble a keyboard. This is because the Nspire is designed to be like a computer in a way. It uses documents to store information. These documents hold information about anything you did within it, not just programs. You can choose to save it, or load different documents, a lot like a computer. Also, the Nspire utilizes a mouse type system. It replaces the arrow keys with one round button. It acts as the arrows, and as a way to move a mouse-like pointer across the screen. The Nspire is a transition of a calculator to a computer, yet held back enough to retain calculator status. 

A very programming-relevant difference, on the other hand, is the advent of printing codes. Using the [nspire:Text](nspire:text.html) your program can identify that you want it to print a word, while the 83 only uses Disp and Output to print out the code.

Also one of the highlights is how much pictures have been empowered.  They now can be any size and be displayed with any logic.  True "real-time" multiplayer games are now possible with the SendCalc Command, something that was impossible on 83's.

The more specific differences described below tend to combine to make programs run faster, and allow for a programming style closer to programming a more "serious" language on a computer.

## Commands

On the TI-89, commands can be entered letter by letter, and don't have to be chosen from a menu. In practice, programs and functions are [tokenized](nspire:tokenization.html), making a command range take up 1 to 3 bytes in a program. Most of the commands on the Nspire are the same or variations of the 68k commands. However, the Nspire lacks most graphical commands, and some variable commands are limited. Some commands require a Computer Algebra System, or CAS, so if your Nspire doesn't have CAS, many of the commands will not function.

There are a few commands for exclusive use in programming. These commands help direct how the program works so that it can complete various tasks.


Many commands have been added or removed between the two languages. In addition, the following commands have changed in spelling:

- [1-Var Stats](1-var-stats.html) and [2-Var Stats](2-var-stats.html) are now [nspire:OneVar](nspire:onevar.html) and [nspire:TwoVar](nspire:twovar.html).
- [End](end.html) has been split into [EndIf](nspire:if.html), [EndFor](nspire:for.html), and others
- [prod(](prod.html) has been renamed to [nspire:product()](nspire:product.html)
- All of the drawing commands have been split into pt and pxl equivilants. eg. line is now either line or pxline.


There are two more overall changes. First, many commands' names have been truncated where they were longer than 8 characters: this is the maximum for a command name on the TI-89. An example is [nspire:RclPic](nspire:rclpic.html), the 68k equivalent of [RecallPic](recallpic.html).

Second, the use of parentheses after a command now follows a strict convention. 
- "Instructions" — commands that do not return a value — do not require parentheses (e.g. [nspire:If](nspire:if.html), [nspire:Text](nspire:text.html), etc.)
- "Functions" — commands that do return a value — require parentheses (e.g. [nspire:sin()](nspire:sin.html), [nspire:setMode()](nspire:setmode.html), etc.)
- Even functions with no arguments use parentheses (e.g. [nspire:getKey()](nspire:getkey.html), [nspire:startTmr()](nspire:starttmr.html), etc.)

Many commands have been added. However, as far as statistics goes, the 68k calculators are inferior, even, to the TI-83 series; most of the functionality is now restricted to regressions, and the calculator doesn't even know internally how to calculate most probability distributions.

## Variables

The way variables are stored has undergone major changes from the TI-83 series. All variables now share a common naming system: the name of a variable can be up to 8 letters long. Variables can also be placed in different folders, which can't be nested but otherwise are very similar to file folders on a computer. By default, variables are stored in the folder 'main'.

Variables on the Nspire function in much the same way as 68k variables. A variable can be a string of letters. An undefined variable is italicized. For example, if the variable height was undefined, or had nothing stored to it yet, then on the calculator the variable would look like height. Defined variables are bolded, so if height was defined, it would appear as height. Commands are neither bold or italicized, and you cannot store information into them.

List are very different.  In addition, lists are important for saving save game data and highscore data in programs. This is better than storing highscore or save game information as a variable, as variables are commonly changed during calculations performed by the users. They now can hold any combination of numbers, expressions, and character strings.  This makes them more powerful, but also slows them down significantly.  Data's are basically matrices, but with the new capabilities (and speed limitations) of the new lists.  Matrices stayed the same though, limited to numbers, but retained their speed.  You can effectively emulate an "old style" list by using a matrix with only 1 row/column,

## Programs

Programs are also considered variables, on the same level as any other: you can even define a program within another program. They imitate built-in commands, and can even be given parameters. Using the [nspire:Local](nspire:local.html) command, you can declare local variables that are reset to their old values once a program finishes running.

You can also define functions, which are similar to programs but return a value. Functions have some other limitations, though: they can only use local variables, and can't modify any global aspects of the calculator (so graphical commands, for example, are limited to programs).

With local variables, and the ability to define functions and programs, you can program in a procedural language style. Instead of placing the entire code of the program in one block, you can split it up into functions and subprograms that are defined at the beginning of the main program.

The entire issue of memory leaks (caused on the TI-83 series by jumping out of code blocks with Goto) is no longer present in 68k TI-Basic. Loops have offsets linking the end to the beginning, so the program doesn't need to keep a stack to be aware of what to do with End instructions. There is no longer any memory cost to entering a loop (or any other kind of code block), so it's impossible to leak memory this way.

## Optimizations

Most types of trivial optimizations from the TI-83 series are invalid on the 68k calculators. For example, closing parentheses, quotes, and brackets are now mandatory — but don't add any size to the program, since it's [tokenized](nspire:tokenization.html) and converted to postfix notation. The [Ans](ans.html) variable no longer plays an important role: though the [nspire:ans()](nspire:ans.html) command does exist to replace it, it's not modified by storing to variables inside a program, so it's mostly useful on the home screen.

A large part of 68k optimization revolves around careful use of lists. List variables are no longer random access: accessing the last element of a list is much slower than accessing the first element. For this reason, going through a list in a [nspire:For](nspire:for.html) loop is about the worst thing you could do.

## Graphics

The screen resolution on the Nspire is superior to other calculators and is much better than any other calculator in history. The screen displays curves very well, it graphs cleanly, it uses letters and other characters with different size (much like a computer font style), and it is bigger. Also, the screen has many different shades of gray. In using inequalities, the calculator can actually shade in the region instead of drawing lines that represent it, and it darkens regions of overlap. The screen is very nicely done.

Apart from these very powerful commands, more ordinary commands have also been buffed up. Virtually all graphics commands have a point and a pixel equivalent, so you're free to choose one or the other to use (usually, you'll want pixels). The Circle command now draws circles instantaneously, as opposed to taking several seconds. 

Instead of being forced to choose between home screen and graph screen, the choice is between graph screen and "Program I/O" screen on the 68k calculators. The program I/O screen is a separate home screen for programs, which is limited to text (but the text doesn't have to be aligned). In addition, both screens can be spiced up using [Nspire:dialogs](nspire:dialogs.html), which imitate the appearance of a popup window on a computer, and are great for inputting data without having to erase anything from the screen.

Another major addition to the graphics command set is the newly created Dialog feature. New commands add extra I/O capability that doesn't interfere with the program I/O or the graph screen, allowing for enhanced in-program data entry.

## Closing Words

This page gives an overview of some of the features of Nspire, but it isn't, and cannot, be complete. There are other pages you could visit to get a better picture of Nspire programming:
- [Nspire:Command Index](nspire:command-index.html)
- [Nspire:FAQ](nspire:faq.html)
- [Nspire:Sample Programs](nspire:sample-programs.html)

However, the best way to try to learn the language is first-hand experience with it.
