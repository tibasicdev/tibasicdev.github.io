# Productivity Tips
Productivity is all about using your TI calculator as efficiently and effectively as possible. There are several things you can do to improve your productivity when you are writing TI-Basic programs:

- **Keyboard Shortcuts** — In the [Program editor](sk:first-program.html), if you press alpha followed by up or down, you will scroll a whole page of program code. In addition, 2nd right will take you to the end of your current line, and 2nd left will take you to the beginning of that line.

- **Backup Often** — You never know when your calculator might crash, and you would be extremely upset if you lost all of your new work on your program that you had been working on. If you only have one program, backing up just consists of creating a new program, and recalling the program code into that program. However, if your program uses several programs and other variables, you should [group](grouping.html) it instead.

- **Archive Programs** — When you are not using a program, you should archive it so that it won't get erased accidentally in case of a RAM clear. This also applies to important program data, such as a [highscore](highscores.html) list. Alternatively, you can also [group](grouping.html) the program and program data together so you have both in one file. Grouping also saves more RAM than archiving the programs separately.

- **Know The Commands** — There are lots of [commands](command-index.html) on the calculator that people never bother using, mainly because they don't know about them. Before trying to create your own program to do something, check to see if the calculator doesn't already provide a command or function that does it, because the built-in commands are almost always faster and smaller.

- **Edit On The Computer** — The [TI-Graph Link](downloads.html) program that TI provides allows you to edit programs on the computer. In addition to faster scrolling and making program structure easier to visualize, the Graph Link also features the ability to type lowercase text and lock a program so it can't be edited on the calculator.

- **Use CtlgHelp** — [CtlgHelp](http://education.ti.com/educationportal/appsdelivery/download/save_download.jsp?cid-us-countryid-us-isocode-en-contentpaneid-2-applicationid-164-softwareid-6231-inputpage-i) is an Assembly application that is rather large (it is 32KB), but is a very helpful reference when trying to remember the syntax for using a command. After you have installed it, you just have to go to the Catalog menu and press the + key to see the help for that command. It can also be used in other menus, such as the MATH, LIST, and PRGM menus.

- **Write Comments** — Whenever you write a complicated piece of code, you should put a [comment](comments.html) in the code explaining what it does, and if appropriate, how it does it. If you ever need to come back to the code, you will now be able to quickly ascertain everything you need to know about the code. Comments are also useful when you don't have the time to implement something, and you want to remind yourself with a quick "To Do".

- **Reuse Code** — In many large programs, there are several pieces of code that get reused multiple times. Rather than writing the code over and over again, you can simply store it in its own program and have the main program call it as a [subprogram](subprograms.html). Because the subprogram is insignificant by itself, you should start its name with a Z or theta so that it appears at the bottom of the program list.

- **Coding Style** — When writing a program, you should follow [code conventions](code-conventions.html) so that it is easy to read and understand. Although each programmer has their own preferences in regards to programming code, there are some general guidelines that most people follow, which help to provide continuity across the programming community:
 - Line up corresponding commands and statements vertically.
 - Don't go through silly contortions to use a loop, when [Goto](goto.html)/[Lbl](lbl.html) branching would be more practical.
 - Use mnemonic label names. For example, Lbl UP would be an appropriate choice for code that moves the screen up.
 - Before using custom list variables, you should use up the built-in variables.
 - If you have a really complex expression, you should add some parentheses to make it easier to read.
 - Be consistent throughout all your code. If you do one thing in one program, you should do it the same way  in another program.
