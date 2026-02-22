# Cleaning Up After a Program
|**This article is part of the coding stage of the [development](development.html) cycle.**|
| --- |


Imagine you just finished playing a round of Blackjack, and now you're back on the main screen. You enjoyed the game, but something is just not right. Not only is there text on the home screen, but there's graphics on the graph screen, and it appears that there's some leftover [variables](variables.html) taking up a considerable amount of your precious memory. It seems that the Blackjack game forgot to clean up after itself.

Cleaning up after a program is one of the most important parts of any game. A quality game features good gameplay, but more importantly it doesn't leave the calculator in disarray afterwards so the next program that is run isn't affected by it. While program cleanup can involve whatever the game programmer wants, there are a few standard parts to it.

## Deleting Large Variables

The first, and arguably most important, part of program cleanup is deleting variables. After a program finishes running, it should delete any large variables that it created during its execution. The program should only keep variables if they are used for storing important information, such as [highscores](highscores.html) or [map data](maps.html). You can delete a variable using the [DelVar](delvar.html) command (provided that the variable is not in the [archive](archive.html)).

The user does not want to have their memory cluttered up with lots of variables because it makes scrolling through the memory menu that much harder. They also don't want to lose any of their memory because it prevents them from using it for any other things they want to do (such as running other programs).

## Restoring the Graph Screen

After deleting large variables, the next part of program cleanup is to restore the graph screen. Besides clearing the graph screen (using the [ClrDraw](clrdraw.html) command), you should recall the graph database ([GDB](pictures.html)) variable that has the previous window and graph format settings stored in it. (Please note that GDBs do not contain text, graphics, or stat plots.)

You want to make sure to clear the graph screen when exiting programs because this ensures that the next program that the user runs won't have to deal with whatever text or graphics your program left behind. It also helps the user because they won't have to manually clear the graph screen themselves.

At the beginning of a game that uses the graph screen, select whichever GDB you want to use (GDB0 through GDB9) and then use the [StoreGDB](storegdb.html) command to save the window and graph settings into that GDB. Now when the program is finished executing, recall that GDB with the [RecallGDB](recallgdb.html) command to recreate the graph screen with the previous graph and window settings that were stored in it. You should then delete the GDB.

## Clearing the Home Screen

Once the graph screen is restored, the next part of program cleanup is to clear the home screen using the [ClrHome](clrhome.html) command. Clearing the home screen ensures that the next program the user runs will not have to deal with whatever text the program left behind. It also helps the user, because they will not have to manually clear the home screen by pressing the CLEAR key; you have already done it for them.

Besides clearing the home screen when cleaning up, you should also remember to remove the "Done" message that shows up after a program finishes executing. This "Done" message is a clear indicator that your program just finished running (which can be bad if you are in class and your teacher is near by), and it also does not look very good.

When you display text, a number, a variable, or an expression with a display command (either [Disp](disp.html) or [Output(](output.html)) on the last line of the program, you can remove the command and just put argument by itself. The argument will be displayed instead of the "Done" message that is normally displayed after a program finishes executing, and it will also be stored into the [Ans](ans.html) variable.

```
:ClrHome
:Disp "Hello
Remove Disp
:ClrHome:"Hello
```

If you do not display any text on the last line, or you do not have any particular text that you want to be shown, you can still remove the "Done" message by just putting a single quotation mark. This will have the same effect, but there will be no text and the cursor will be placed on the second line.

```
:ClrHome
Put a quote
:ClrHome:"
```

In addition to removing the "Done" message, this text also acts as a way to clear the Ans variable. For example, if you had a large variable stored in Ans (such as [A]), which subsequently would cause Ans to also be large, this text would make Ans release that excess memory back to the calculator. You could also add the [Clear Entries](clear-entries.html) command before the final text just for good measure.

To remove the "Done" message without moving the cursor (slightly larger):
```
:ClrHome
:Output(1,1,"             //no space, just a quote
```

## List Editor Cleanup

If you used the [SetUpEditor](setupeditor.html) command for lists that your program uses, that also causes the list to appear in the "List Editor" the next time the user accesses it (STAT>Edit...). This probably isn't desired behavior, because it looks unprofessional, and because your program's list is likely to contain [highscores](highscores.html) and other data of that nature. 

To fix this, add a SetUpEditor without any arguments to the end of your program. This will reset the List Editor to the default settings (it will show the contents of L1, L2, ..., L6). This isn't perfect, since the user may have been editing his own lists there, but it's the best you can do, since TI-Basic can't find out about the user's previous settings.

If you don't want to restore L1 through L6, you can do:
:SetUpEditor L<name>
:Archive L<name>
:UnArchive L<name>

This will remove L<name> from SetUpEditor.

## Putting It All Together

Putting all the parts of program cleanup together, here is a typical way to end a program:

```
PROGRAM:CLEANUP
:SetUpEditor
:DelVar Str1DelVar [A]
:RecallGDB 1
:DelVar GDB1
:ClrDraw
:ClrHome:"
```

Of course, you only have to include the things that you actually use. If you don't use any large variables, you don't have to delete them. In the same fashion, you don't have to clear the graph screen and restore the graph screen settings if your program just runs on the home screen.

## Advanced Cleanup

If you have a lot of number variables that you used in your program like A, B, C, continuing through Z; you may want to consider using a [hexcode](hexcodes.html) to help clear all the variables rather than have a large number of DelVar statements. Although this code takes more memory and requires a subprogram, it can save a lot of typing. Lets take a look at the [Delvar Hexcode](hexcodes.html#toc58). This hexcode will take a string in Ans of the name of a variable to delete, and will delete it so long as it is prefixed correctly. To start building the cleanup routine, make a new program containing just the hexcode in it. Save it as something you will remember; I called mine "ZDELVAR". Next, we need to put the code for the routine into our main program. The code looks like this:
```
"ABC"→Str1
For(θ,1,length(Str1)
" and "+sub(Str1,θ,1
Asm(prgmZDELVAR
End
DelVar Str1
```
Let's take a closer look at how it works. We store all of the variables we want do delete into String 1. Now we want to run the hexcode for each letter in our string, so we add in a for loop. The starting position will be 1, and the ending position will be however long String 1 is. We know that the hexcode takes an input in Ans, and that real variables have to be prefixed with " and " for the hexcode to work (note that this is the boolean and found in 2nd+Math). So lets take the string " and ", and then add to it the current letter we are on. Now that we have the format we need for the hexcode, run the hexcode! When we finish deleting all the variables, delete String 1. It's as simple as that! All you have to do is put which variables you want deleted into String 1!

If you wanted to delete all the strings, pictures, gdb's, or matricies you can do that too. Simply add the code for the routine again, but change the " and " to the proper prefix and change the variable names!

<center>

|**[<< Subprograms](subprograms.html)**|**[Overview](development.html)**|**[Debugging >>](debug.html)**|
| --- | --- | --- |

</center>
