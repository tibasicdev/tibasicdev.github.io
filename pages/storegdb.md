![The StoreGDB Command](storegdb/STOREGDB.GIF "The StoreGDB Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Stores graph setting to a GDB (Graph DataBase) to be recalled later with RecallGDB.|StoreGDB *GDB#*<br>StoreGDB *number*|TI-83/84/+/SE/CSE/CE|1 byte|

### Menu Location
Press:<br># 2nd DRAW to access the draw menu.<br># LEFT to access the STO menu.<br># 3 to select StoreGDB, or use arrows and ENTER.
# The StoreGDB Command

The StoreGDB command stores all graph settings needed to reconstruct the current graph to a GDB (Graph DataBase) variable, one of GDB1, GDB2, ..., GDB0 (as indicated by the argument). These settings can then be recalled using the [RecallGDB](recallgdb.html) command.

The settings stored in a GDB include:

- The [graphing mode](graphing-mode.html) currently enabled.
- All [equations](system-variables.html#equation) in the current graphing mode, but NOT other graphing modes.
- All [window variables](system-variables.html#window) applicable to the current graphing mode. This does not include zoom variables, table settings, or irrelevant variables such as Tmin when in function mode.
- The menu settings relevant to graphing (everything in the 2nd FORMAT menu, as well as Connected/Dot and Sequential/Simul settings in the MODE menu)

The number passed to StoreGDB must be one of 0 through 9. It has to be a number: StoreGDB X will not work, even if X contains a value 0 through 9.

## Advanced Uses

The StoreGDB and RecallGDB variables are useful in [cleaning up](cleanup.html#toc1) after a program finishes running, preserving the user's settings. If your program heavily relies on the graph screen, it may end up editing window size or other graph settings, which the user might want to be saved. This is easily done:

Add StoreGDB 1 (or any other number) to the beginning of your program.

Then, feel free to edit any graph settings you like.

At the end of your program, add RecallGDB 1, followed by [DelVar](delvar.html) GDB1, to recall the graph settings stored at the beginning.

GDBs can also be useful in adding extra string storage. You can store strings to the Yn variables, and back them up in a GDB; to retrieve them later, recall the GDB and use [Equ►String(](equ-string.html) to store the equations to the strings again.

## Error Conditions

- **[ERR:DATA TYPE](errors.html#datatype)** is thrown if the argument is not a *number* 0 through 9.

## Related Commands

- [RecallGDB](recallgdb.html)

## See Also

- [Cleaning up](cleanup.html)
