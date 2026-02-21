# Codebender's TI-Basic Tutorial
> **"This page is still in development.  It should be finished within a few months.  I appreciate your patience!  :D"**
>> **~**[[*user Joshuasm32]]

+++++ Sharing is Caring!

[[social]]



## Preface:
First, I need to give the essentials to program with my tutorial:

++++ Requirements:
A TI-82/83/84 (Plus) (SE) graphing calculator or emulator.

If you have that, you're set to go!

++++ Key:
Here is a simple key to symbols that I use:

```
//= A comment on codes.

[___]= A description of something shortening the code.  (I.E., [The code that I used above] )

->= The symbol '→' in programming.

Programmer's Trick's:= A handy trick you can use.

Handy Hint:= A hint for programming.

Beware!= Something to avoid in coding.

Buzz Word:= A handy morsel of information.
```

++++ Advice:
Before we start, I would like to give a few words of advice:

1. Never give up on a program, even if it seems impossible to complete, for you can program pretty much *anything* on a calculator (except color).     ;-)
2. Remember, there is no "wrong way" to program; there are more efficient and less efficient ways, but feel free to stretch the limits and build your own style to program.
3. **Bend the Codes!**


So, lets get started!

## Basic Concepts
Alright, now that you are ready to start, lets kick off with the basics.

++++ Making Programs:
Let's start with how to create, edit, and run programs.  First, tap the [PRGM] key on your calculator.  If you use your arrow keys, you can see the cursor move left/right and up/down.  Look at the top bar: if your cursor is on the 'EXEC' label, you can move your cursor up and down and run any programs that you may have made.  By pressing the right arrow once, you can edit programs.  Lastly, if you cursor is on new, you can create a new program.

Go ahead and create a program by pressing [ENTER].  Now, you are prompted for a title.  You can enter any name for your program that you want that is 8 characters or less and uses numbers, letters (activated by pressing alpha and the green text above a key), and a theta ('θ').  (A theta is a symbol you can use like a character.)  Now, name your program "TUTORIAL" and tap [ENTER] again.  Now you are ready to begin making the program.  :D

++++ The Command lines, the [PRGM] Key, and deleting programs:
If you have learned other programming languages before, you know that a "Command Line" is a line of commands that the computer reads through.  Each command line is represented by the symbol '**:**.'  (You should see a blank command line on your screen.)  The computer reads through a command line in the same way we read a book: left-to-right.  As it finishes each line of code, it jumps to the next line and continue until the program ends.

Now, to make code for the computer *to* read, press the [PRGM] key once.  This is a list of common commands.  (For a full list of commands and symbols, press [2ND] then [0].  You can type a character and jump to different sets of alphabetically sorted commands.  Also, TI-84 calculators have the built-in app under the apps menu "[CTLGHELP](http://education.ti.com/en/us/software/details/en/4a72374e5e8c4ab6926f9b20a9c72ff6/83cataloghelp)."  If you open this, you can go to catalog and press [+] when your cursor is on a command and see how it is used.)  Each of these commands has its own syntax and job that it does.  We will learn about each of these further on.

To select a command, move you cursor around like on the program and press enter or type the number in front of each command.  (I.E., type [1] for "If" and [2] for "Then.")  Learning these numeric key-strokes is essential if you want to be a fast programmer.  (To learn them, try quizzing yourself on the number and arrow keys to press for each one and practice using it for programming.)  After you select a command, it will appear on your command line.

To make a new line, you can press [ENTER], and to finish and save your program, you can press [2ND] then [MODE] to select the yellow text "QUIT."  Now, you can delete the program by pressing [2ND], [MEM], tapping [2], [7], and for TI-82/83 calculators, by pressing [ENTER] when your cursor is on a program, and for TI-83 (Plus) (SE) calculators, pressing [DEL].

On the TI-83 Plus/TI-84 (Plus) (SE) set of calculators, you can press [ENTER] and archive a program.  A '*' symbol should appear before the program name after you archive a program to represent that it is archived.  Archiving is a useful tool for important programs that you do not want to loose if your calculator crashes.  However, while something is archived, you cannot run or edit it (without [downloading](http://www.ticalc.org/archives/files/fileinfo/430/43068.html) and [installing](sk:computer-setup.html) the application "Doors CS7" or others like it).  To unarchive, press enter again.

++++ Graph Screen and Home Screen:
There are two "screens" on a graphing calculator: the *"Home Screen"* and the *"Graph Screen."*  The home screen is the screen used when your calculator is turned on for solving problems, such as "2+2."  The graph screen is the screen is the screen which you graph and use drawing commands ([2ND], [PRGM]).  This can be found from your home screen by pressing [GRAPH].

## Programming & Programming Commands:

### Homescreen Commands:
The starting commands are the commands on the home screen.  First, let's learn how to use **Disp**.

++++ Disp
The **Disp** command (short for "Display") is used to write a line of text up to 16 characters (the width of the home screen) on the first empty row the calculator finds.  To find it, tap: [PRGM], (Right Arrow), [3].  Let me give you some example code (Enter this into your TUTORIAL program.)

```
Disp "HELLO WORLD"
```

And there you go!  Your very *first* (but not the last!) program.  Now, lets go into *how* that worked.
When you enter "Disp," it seeks the first empty row.  Then, you add a quote to the beginning of text when you enter it.  To write more text then 16 characters, do this:

```
Disp "HELLO WORLD","HOW ARE YOU?"
```

++++++ Programmer's Tricks:
A simple trick is that you *do not have to finish with the second quote if it is the end of a line of code.*  :D  The calculator assumes a quote on the end.  Try this:

```
Disp "HELLO WORLD
```

```
Disp "HELLO WORLD","HOW ARE YOU?"
```

++++++ Beware!
> Try to avoid using finishing quotes so that calculators which download your programs that *may* be low on memory can use your program without worries.  Remember, everything you enter requires *memory*.

++++++ Buzz Word:
> **Disp** writes text on the first empty line the calculator finds.

++++ ClrHome:
You may have noticed that it is a bit annoying to have "Prgm TUTORIAL" written on your screen *every* time that you run the program.  Also, if you want to add more text on a blank screen, you would have to display " " a bunch of times.  That is why I am glad to tell you of the command **ClrHome**; this clear the home screen  (Clear Home).  To find it, tap:  [PRGM], (Right Arrow), [8].  Look at this code:

```
ClrHome
Disp "HELLO WORLD
```

See how easy *that* was?

++++++ Buzz Word:
> **ClrHome** clears the home screen.

++++++ Handy Hint
> I recommend using the command **ClrHome** at the beginning of all programs on the home screen to remove "PROGRAM:TUTORIAL" from the screen.

++++ Output(:

Let's say you want to write "HELLO WORLD" on the bottom of the screen and "HOW ARE YOU?"  on the top.  **Output(** is used to put text on the screen at given coordinates.  Look at this grid:

    1      2      3      4     5      6      7     8      9      10     11      12      13     14      15      16
1 (1,1) (1,2) (1,3) (1,4) (1,5)	(1,6)	(1,7)	(1,8)	(1,9)	(1,10) (1,11) (1,12) (1,13) (1,14) (1,15) (1,16)
2 (2,1) (2,2) (2,3) (2,4) (2,5)	(2,6)	(2,7)	(2,8)	(2,9)	(2,10) (2,11) (2,12) (2,13) (2,14) (2,15) (2,16)
3 (3,1) (3,2) (3,3) (3,4) (3,5)	(3,6)	(3,7)	(3,8)	(3,9)	(3,10) (3,11) (3,12) (3,13) (3,14) (3,15) (3,16)
4 (4,1) (4,2) (4,3) (4,4) (4,5)	(4,6)	(4,7)	(4,8)	(4,9)	(4,10) (4,11) (4,12) (4,13) (4,14) (4,15) (4,16)
5 (5,1) (5,2) (5,3) (5,4) (5,5)	(5,6)	(5,7)	(5,8)	(5,9)	(5,10) (5,11) (5,12) (5,13) (5,14) (5,15) (5,16)
6 (6,1) (6,2) (6,3) (6,4) (6,5)	(6,6)	(6,7)	(6,8)	(6,9)	(6,10) (6,11) (6,12) (6,13) (6,14) (6,15) (6,16)
7 (7,1) (7,2) (7,3) (7,4) (7,5)	(7,6)	(7,7)	(7,8)	(7,9)	(7,10) (7,11) (7,12) (7,13) (7,14) (7,15) (7,16)
8 (8,1) (8,2) (8,3) (8,4) (8,5)	(8,6)	(8,7)	(8,8)	(8,9)	(8,10) (8,11) (8,12) (8,13) (8,14) (8,15) (8,16)

When you enter the coordinates of a point, it will write text *there*.  You must remember, instead of an "X,Y" format, you must use a "Y,X" format for Output(.  Look at this example:

```
ClrHome
Output(1,1,"ROW 1
Output(8,1,"ROW 8
```

See how that worked?

++++++ Buzz Word:
> **Output(** puts text on the screen at given coordinates using a "Y,X" format.

### Pause

The **Pause** command does what is apparent: it pauses and wait for [ENTER] to be pressed, then proceeds.  It is activated by pressing: [PRGM], [8].  Lets work out an example, shall we?

```
ClrHome
Disp "HELLO WORLD
Pause
ClrHome
```

++++++ Handy Hint
> One trick about Pause is this: you can use it in the same as **Disp** to display text and then go on to pause.  Look at this example:

```
ClrHome
Pause "HELLO WORLD
ClrHome
```

> Do you see?  It is a more efficient method of coding the above.

### Variables and "→" vrs. "=":

Now, let's go into making *Variables.*  The is a major function in programming.  Variables a the characters A-Z and _theta_.  These can be used to store and recall data.  A *Variable* takes a snapshot of whatever data is given to it and stores it in a box, named the name of the character chosen.  The symbol "→"  stores data and is activated by pressing [STO].  Look at this sample code:

```
           123                             →                                                                   A
            ^                              ^                                                                   ^
\\This is the data to be stored.    \\This says "Take the given data and store to..."    \\This is the variable which the data is stored to.
```

Do you see?  Now, let's try an example:

```
ClrHome
123->A
Disp A
```

(When you display a variable, do not use a quote; that is only for displaying text.)

++++++ Buzz Word
> A Variable stores a number or an equation to be recalled for later use.

Now, many programmers are often confused by this: What is the difference between "→" and "="?  (the symbols "=", ">", "<", "≥", "≤",and "≠" are found by pressing [2ND], [MATH] or in the catalog).  Let's look more carefully, shall we?

```
123->A
A=123
```

When you store something using '→', you are *doing* something and performing an action.  When you you use '=', you are making a statement.  This will return a "1" if the statement is true and a "0" if it is false.  Do you see the difference now?  :D

++++++ Buzz Word
> The symbol "→" stores information and the symbol "=" states information.

### Strings
Now, variables are useful for storing numbers and equations, but if if you ever try to store text to them, they will *not* work.  To fix this, you can use **Strings**.  Strings are used in the *exact* same way as variables except they store text instead of numbers.  There are 10 strings labeled 1-9 and 0.  To access strings, press: [VARS], [7].  To give an example of how to use them, lets work out an example.

```
ClrHome
"HELLO WORLD"->Str1
Pause Str1
```

++++++ Buzz Word
> Strings are *exactly* the same as variables except they store text.

### Creating a Customized Program

Now, here is a *major* break-through for your programming skills: right now, when you make a program, it only has *one* ending: the one you programmed.  However, we are now going to go into creating an individualized program experience.

++++ Input & Prompt:
The commands **Input** and **Prompt** are the most basic way to create a program with multiple outcomes.  These ask for information and store it to either a variable or a string.

+++++ Prompt:
**Prompt** stores a number or an equation to a Variable of choice.  Look at this example:

```
ClrHome
Prompt A
Disp "A IS:",A
```

It also can store information to a string!

```
ClrHome
Prompt Str1
Disp "STRING 1 IS:
```

Once you figure out how to use it, this command is a breeze!

++++++ Buzz Word:
> **Prompt** asks for user inputed data and stores it to the chosen location.

++++++ Programmer's Tricks:
> You can also use a comma between **Prompt**'s in the same way as **Disp**; look at this:
```
ClrHome
Prompt A,Str1
Disp A,Str1
```

+++++ Input:

**Input** works like **Prompt**, performing the same task, but does it in a more user-friendly method.  It takes a little more time and effort to learn, but it is worth it in the end!

You can store and input to a variable or to a string.  The difference is this: say you want to ask someone there name and store it to string one to be used later on in the program; using prompt, you could enter this code.
```
ClrHome
Prompt Str1
Disp "HELLO
Pause Str1
```

However, this returns: "Str1=?" for the user's name.  However, if you did not write the program, what does it mean?  What do they do?  You could use 'Disp' before 'Prompt,' but it still looks messy...  So, that is where input comes in.

```
ClrHome
Input "NAME IS:",Str1
Disp "HELLO
Pause Str1
```

++++++ Programmer's Tricks

Normally, **Prompt** is only used for math programs, such as a program to find, say, the area of a square (L*W=A).

```
ClrHome
Prompt L,W
L*W->A
Disp "Answer is
Pause A
```

And even then, **Input** *could* have been used for a clearer program.  ;-)

+++++ Simple Menu's:

+++++ If Statements:
In my opinion, these is the most vital part of programming: the conditionals.  It works like a conditional in the English language; examine this code to get a brief idea of how they work.

```
ClrHome
Prompt A
If A=1
Disp "A is 1
```

The code is saying, "Ask what A is.  If A=1, then say A=1."  If A does not equal 1, the program will skip the **If** statement and end the program, since there is nothing which comes after the if statement.

The If statement can control a game or program to make it so that you win, loose, or do whatever you want your program to do.  For instance, we aren't *this* far into programming yet, but say you were making a game of "pong."  You could say, "If the ball touches the bumper, bounce it.  Otherwise, tell the player that they die."  This is the primary part of most games and programs.

There are also commands which can be added on to the if command.

++++++ Then and Else:

------

## Questions & Comments

> For more details about a *specific* command covered or information about commands not covered, I recommend looking through the completed [Command Index](http://tibasicdev.github.io/command-index).  If you have questions or comments about this tutorial, please discuss them below. Alternatively, you can contact [[*user Joshuasm32]] directly for personal assistance.

------


#page-title {
text-align:center;
}
#header {
display:none;
width:0px;
height:0px;
top:-2000px;
left:-2000px;
z-index:-100px;
}
#content-wrap {
padding-top:50px;
padding-bottom:100px;
top:0;
left:0;
background-color:#000;
width:100%;
text-align:center;
background:fixed;
background-image:url("http://www.omnimaga.org/Themes/omnimaga5/images/bg.png");
}
#main-content {
background-color:rgba(251,251,251,.8);
width:60%;
border:none;
border-radius:10px;
text-align:initial;
color:black
font-family:Segoe UI Thin,Segoe UI,arial,tahoma,verdana;
voice-family:male;
}
#side-bar {
display:none;
width:0px;
height:0px;
opacity:0%;
top:-200000px;
left:-200000px;
z-index:-100;
position:relative;
}
#licence-area,#footer {
display:none;
width:0px;
height:0px;
opacity:0%;
z-index:-100;
position:relative;
background:rgba(251,251,251,.0);
}
#page-content {
color:#000;
font-family:Segoe UI Thin,Segoe UI,arial,tahoma,verdana;
voice-family:male;
}
.head {
background-color:blue;
border-radius:10px;
color:black;
}
[[/module]]



[Back to Top](http://tibasicdev.github.io/codebender-s-ti-basic-tutorial)
<!—[if !(lt IE 8)]><!—>
   <script type="text/javascript">
     (function(){var e=document.createElement("script");e.type="text/javascript";e.async=true;e.src=document.location.protocol+"//d1agz031tafz8n.cloudfront.net/thedaywefightback.js/widget.min.js";var t=document.getElementsByTagName("script")[0];t.parentNode.insertBefore(e,t)})()
   </script>
<!—<![endif]—>
