# Setup And Cleanup
When writing a program, you want it to be independent of the user's settings as much as possible - no one should have to set function mode or disable axes to run your program correctly. So your program should change the settings to the necessary ones before running (this is referred to as 'setup'). However, to avoid messing things up for anyone that runs your program, these settings should be restored to what they were before (this is called 'cleanup'). Similarly, you should avoid overwriting any variables.

## Mode Settings

Using [setMode()](68k:setmode.html), you can change and restore almost any calculator setting. This only requires two lines of the program. At the beginning of the program, use setMode() to change the settings you want, and *store the result to a variable*:
```
:setMode({"Exact/Approx","AUTO","Split Screen","FULL"})→settings
```
The variable you used will contain the old settings, which you can use to restore them. Add the following line at the end of your program:
```
:setMode(settings)
```

setMode() has an alternate, "programmer's syntax" that uses numbers instead of the names of the settings (see the [Table of Mode Settings](68k:mode-settings.html) for a list). It's best to use this syntax instead, because it's shorter, and because it ensures [compatibility](68k:cross-compatibility.html) with different language versions:
```
:setMode({"14","1","8","1"})→settings
```

Obviously, the settings you'll want to change will depend on what the program does. However, here are some common settings to change:
- Set Graph mode to FUNCTION to use many drawing commands.
- Set Split Screen mode to FULL unless you *want* the two screens.
- Set Exact/Approx to AUTO and Base to DEC if you're going to be displaying numbers.

## Graph Settings

Almost the same situation occurs with the graph settings, except that the [setGraph()](68k:setgraph.html) command can only change one setting at a time. Set the settings you want at the beginning of the program:
```
:setGraph("Grid","OFF")→grid
:setGraph("Axes","OFF")→axes
:setGraph("Labels","OFF")→labels
```
Then restore them at the end:
```
:setGraph("Grid",grid)
:setGraph("Axes",axes)
:setGraph("Labels",labels)
```

Like setMode(), setGraph() has a language-compatible syntax, which you should be using both at the beginning and at the end:
```
:setGraph("3","1")→grid
:setGraph("4","1")→axes
:setGraph("6","1")→labels

<main program code>

:setGraph("3",grid)
:setGraph("4",axes)
:setGraph("6",labels)
```

With graph settings, you have an alternate method of saving and recalling settings. Use [StoGDB](68k:stogdb.html) to save them at the beginning of the program, and [RclGDB](68k:rclgdb.html) to recall them at the end. You'll still need to setGraph() the settings at the beginning, but don't have to save the result.

## Clearing the Screen

In addition to changing the settings, there are several things you need to do to start off with a clear screen.

- If you're using the graph screen:
 - Use [ClrDraw](68k:clrdraw.html) to clear anything drawn on the screen.
 - Use [ClrGraph](68k:clrgraph.html) to clear anything the graph commands drew on the screen.
 - Use [FnOff](68k:fnoff.html) to disable equations in the Y= editor.
 - Use [PlotsOff](68k:plotsoff.html) to disable plots.
- If you're using the Program I/O screen:
 - Use [ClrIO](68k:clrio.html) to clear the I/O screen.

As you can see, you might need to use a lot of commands. The good news is that they can all be replaced by the single command [NewProb](68k:newprob.html), which does all of the above and more. Unfortunately, NewProb has an unfortunate side effect: it clears the single-letter variables a through z. Since the user might have something important in one of these variables, it's best to stay away from NewProb unless you're working in a separate folder (see the Variables section, below).

At the end of the program, you also want to clear anything you drew to the screen. Here, it's usually enough to use ClrDraw and/or ClrIO. However, due to a quirk in the calculator, if you just run the commands, the calculator won't refresh the screen, so it will look as though you hadn't cleared anything. To avoid this, run [DispHome](68k:disphome.html) right after these commands.

## Variables

Finally, you want to avoid overwriting the calculator user's variables when your program is running. The simplest way to do this is to use the [Local](68k:local.html) command. Add Local as the first line of your program, and list all the variables you will be using. 

There's a drawback to this method: the variables will not be visible to subprograms (which is sometimes a useful thing). Another way to avoid overwriting variables is to work in a separate folder.You might choose always to maintain a separate folder, for example to keep the program's pictures. In this case, you would use [setFold()](68k:setfold.html) to switch from one folder to another, at the beginning and end of the program:
```
:setFold(thisgame)→folder

 <main program code>

:setFold(#folder)
```

Alternatively, you might create a temporary folder while the program is running. To avoid collisions make sure the name of the folder has something to do with your program. In fact, you might just use the program name. Keep in mind the name of the folder will be displayed in the corner of the screen.

To do this, you'll need the [68k:NewFold](68k:newfold.html) and [68k:DelFold](68k:delfold.html) instructions. At the beginning of the program, save the current folder and create the new one:
```
:Local folder
:getFold()→folder
:NewFold tempfold
```
At the end of the program, delete the temporary folder and go back to the original one:
```
:DelFold tempfold
:setFold(#folder)
```

Note that the # before the folder is necessary — setFold(folder) will return an error! This because getFold() and setFold() returns a string, not a variable, so you'll need # to turn the string into a variable.

In either case, you can now use global variables (just store to variables each time you need a new one) without worrying about overwriting the user's important variables. At the end of the program, though, you'll probably want to use [DelVar](68k:delvar.html) to delete all the variables you're not going to save (this is necessary if you're using a temporary folder, otherwise the temporary folder won't get deleted). You can also use NewProb to delete all one-letter variables for you.

## Putting Everything Together

Here is some typical setup and cleanup code:

```
:mygame()
:Prgm
:Local oldfold
:getFold()→oldfold
:NewFold mygame
:StoGDB graphset
:setMode({"1","1","8","1","14","1","15","1"})→settings
:setGraph("3","1")
:setGraph("4","1")
:setGraph("6","1")
:NewProb

 <main program code>

:setMode(settings)
:RclGDB graphset
:ClrDraw
:ClrIO
:DispHome
:DelVar settings,graphset,...
:DelFold mygame
:setFold(#oldfold)
:EndPrgm
```

<center>

|**[<< Debugging](68k:debugging.html)**|**[Overview](68k:development-overview.html)**|**[Usability >>](68k:usability.html)**|
| --- | --- | --- |

</center>
