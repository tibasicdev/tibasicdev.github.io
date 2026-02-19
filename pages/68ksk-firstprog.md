# Your First 68k Program
++++  Creating a program in the Program Editor
Time to make your first program in 68k Basic! In the APPS menu select #7, go to the "Program Editor", and then press "New". Enter a name for your program in the variable field, let's call it "hellowld". Press enter, and here we go!

++++ Creating the Program

The following program, when executed, will display the phrase "Hello World!" 

```
hellowld()
:Prgm
:ClrIO
:
:Disp "Hello World!"
:
:Pause
:ClrIO
:DispHome
:EndPrgm
```

Let's go through a line-by-line analysis of this code.

```
hellowld()
:Prgm
```

This is where the program starts. Every program you make will start with the name of the program, followed by parenthesis. The nest line contains an opening [`68k:Prgm`](68k:prgm.html) tag, which indicates the beginning of the program. Everything after it will contain the actual code that you write.

```
:ClrIO
:
:Disp "Hello World!"
```

The next command is [`68k:ClrIO`](68k:clrio.html), which will clear the Input/Output buffer. For those who don't know what this is, it's basically a different section of the calculator where output is displayed (so output is not displayed on the Home screen, it is displayed here). After that, we have a new command [`68k:Disp`](68k:disp.html), which displays a string to the IO buffer.

```
:Pause
:ClrIO
:DispHome
:EndPrgm
```

We then [`68k:pause`](68k:pause.html) the program, which will halt program execution until the ENTER key is pressed. More information on why we do this up ahead. After pressing the enter key, the program clears the IO buffer (which erases the "Hello World!" message from it) and goes back to the home screen using the [`68k:DispHome`](68k:disphome.html) command. This is the end of our program, which means that we can add the [`68k:EndPrgm`](68k:endprgm.html) tag, which closes the program.

You may look back and ask, why did we include the [`68k:pause`](68k:pause.html) command? This is because shortly after, we display the home screen using [`68k:DispHome`](68k:disphome.html). This means that the "Hello World!" message will be printed the IO buffer, but it will display the home screen quickly before you can even try to read the message. We add the pause in there to allow the user to read the message before executing the rest of the code. This roadblock can be crossed by removing the [`68k:DispHome`](68k:disphome.html) command, but for ease of use, we keep the [`68k:DispHome`](68k:disphome.html) and make sure to throw in the [68k:pause](68k:pause.html) command after we display the text.


<center>

|**[<< Overview of 68k Basic](68k:sk-overview.html)**|**[Table of Contents](68k:starter-kit.html)**|**[Good Programming Practices >>](68k:sk-practices.html)**|
| --- | --- | --- |

</center>
