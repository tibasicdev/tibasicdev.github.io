# Your First Program
**What is a Program?**

A program is an organized, step-by-step set of instructions. When executing a program, the calculator behaves in a predetermined manner, performing the instructions in a sequential order. The amount of free RAM is the only limit on the number and size of programs.



When making programs, there is a general order that you must follow. You first need to create the program, then you edit the program, and finally you execute the program. Every program will go through this process, with the editing and executing being done numerous times to make changes or fix errors.

In order to help you further understand and visualize the process, we are going to walk you through creating a program. We have chosen to demonstrate how to create the famous "Hello, World!" program, which is a common first program because of its simplicity.

## Create a Program

To create a program, you have to first go into the Program menu. This can be found by pressing the PRGM key. Then, press the right arrow twice [>] [>] to go to the NEW menu. Select 1:Create New and press ENTER. The Name= prompt is displayed, and alpha-lock is on. You now have to enter a name.

Here are some things to remember about naming programs:

1. Each program must have its own unique name.
1. Program names can only be eight characters or less.
1. The characters must be A-Z, 0-9, or θ.
1. The first character must be A-Z or θ.

For our program, we want a name which tells the user that it will display "Hello, World!" on the screen, so we have decided to go with the simple, but adequate "HELLO". As a general rule, you should choose a program name that actually relates to your program (such as its title). And, if your program is insignificant (such as a subprogram for a larger program), start it with θ or Z so that it appears at the bottom of the program list.

After you have typed in a name that you are satisfied with, press ENTER. This will put you in the Program editor. When you are in the Program editor, you will see the name of your program at the top line. To exit the Program editor and return to the home screen, press 2nd and MODE.

## Edit a Program

![helloworld-code.png](helloworld-code.png "")

Now that we have created our program, we want to edit it so that it does something. To edit a program, press the PRGM key to go back into the Program menu. This time, only press right > once. This will bring you to the EDIT menu. Scroll down to whichever program you want and press ENTER. This will cause the Program editor to open, with you being able to edit the program using a movable cursor.

When you are editing the program, you can add any commands or instructions that you want. A colon (:) denotes the beginning of each new line, and you can put multiple commands on a line by separating each command with a colon. Because multiple commands put together is typically wider than the screen, this will cause the line to wrap around to the next line.

There isn't a whole lot to our HELLO program, it just consists of two commands: [ClrHome](clrhome.html) (to clear the screen) and [Output(](output.html) (to display the message). You can get to both commands by pressing PRGM to go to the program menu, and RIGHT to go to the I/O submenu, then selecting the right command.

We're not going to get real fancy with the text (for example, although it's possible to use lowercase letters, it's a bit tricky, so we won't do it here). We will, however, use a trick to get the exclamation point — select the factorial ! from the PROB submenu of the MATH menu.

```
:ClrHome
:Output(2,2,"HELLO, WORLD!")
```

When editing, you can delete, overwrite, or insert commands and instructions. Move the cursor to whatever line you want, and then press DEL to delete an individual command or CLEAR to delete all of the commands on the line (leaving only the beginning colon); press DEL to also delete the line.

For overwriting commands, simply select a command or type an instruction. The old command will be replaced with the new command. To insert a new command, press 2nd INS and either the space key several times for however many spaces you want or ENTER for a whole new line.

As editing programs involves a considerable amount of movement and scrolling, there are some shortcuts that make it easier. You can move the cursor to the beginning or end of a line by pressing 2nd < or 2nd >, respectively. You can scroll down or up with the cursor seven lines at a time by pressing ALPHA v or ALPHA ^, respectively. Use these shortcuts whenever possible.

## Execute a Program

![helloworld-output.png](helloworld-output.png "")

We have created and edited our HELLO program, so now we are finally ready for program execution. To execute a program, press the PRGM key to go back into the Program menu. This time, however, press right twice > > to get to the EXEC section.

Scroll down to the HELLO program and press ENTER. This will cause the program's name to be printed on the home screen (with 'prgm' in front of it). Press ENTER again and the program will be executed. The busy indicator will turn on while the program is executing. If you put the commands in correctly, the program should execute fine and you will get the desired "HELLO, WORLD!" message; if not, there will be an error.

When the calculator comes across an error while executing the program, it will give an error menu — telling you what the error is and giving you the option to see where the error is in the program (if the program isn't edit locked). This allows you to figure out why it's producing an error. Many times it will be a simple mistake, such as mistyping a command's arguments. However, sometimes the error will be much more sinister.

Although you will usually let a program execute until it is finished, sometimes it is necessary to prematurely stop execution. For example, if you have a large program that takes a long time to execute and you don't want to wait. You can stop execution by simply pressing the ON key. After the ON key is pressed, the ERR:BREAK menu is displayed on the home screen with one or two items.

The first item is 1:Quit. This item should be selected if you want to return to the home screen. The second item is 2:Goto, and it appears if the program isn't edit-locked (Assembly programs can make the program not able to be edited from the Program menu). This item should be selected if you want to go to the line of code where program execution was halted.

<center>

|**[<< Overview of TI-Basic](sk:overview.html)**|**[Table of Contents](starter-kit.html)**|**[Using Your Calc >>](sk:using-your-calc.html)**|
| --- | --- | --- |

</center>
