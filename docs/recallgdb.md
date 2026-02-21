![The RecallGDB Command](recallgdb/RECALLGDB.GIF "The RecallGDB Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Recalls graph settings from a GDB (Graph DataBase) variable|RecallGDB *number*|TI-83/84/+/SE|1 byte|

### Menu Location
Press:
1. 2nd DRAW to access the draw menu.
2. LEFT to access the STO menu.
3. 4 to select RecallGDB, or use arrows and ENTER.
       
# The RecallGDB Command

The RecallGDB command recalls graph settings a GDB (Graph DataBase) variable, one of GDB1, GDB2, ..., GDB0 (as indicated by the argument). These settings can be stored to a GDB using the [StoreGDB](storegdb.html) command.

The settings stored in a GDB include:

- The [graphing mode](graphing-mode.html) currently enabled.
- All [equations](system-variables.html#equation) in the current graphing mode, but NOT other graphing modes.
- All [window variables](system-variables.html#window) applicable to the current graphing mode. This does not include zoom variables, table settings, or irrelevant variables such as Tmin when in function mode.
- The menu settings relevant to graphing (everything in the 2nd FORMAT menu, as well as Connected/Dot and Sequential/Simul settings in the MODE menu)

The number passed to RecallGDB must be one of 0 through 9. It has to be a number: RecallGDB X will not work, even if X contains a value 0 through 9.

## Advanced Uses

The StoreGDB and RecallGDB variables are useful in [cleaning up](cleanup.html#toc1) after a program finishes running, preserving the user's settings. If your program heavily relies on the graph screen, it may end up editing window size or other graph settings, which the user might want to be saved. This is easily done:

Add StoreGDB 1 (or any other number) to the beginning of your program.

Then, feel free to edit any graph settings you like.

At the end of your program, add RecallGDB 1, followed by [DelVar](delvar.html) GDB1, to recall the graph settings stored at the beginning.

GDBs can also be useful in adding extra string storage. You can store strings to the Yn variables, and back them up in a GDB; to retrieve them later, recall the GDB and use [Equ►String(](equ-string.html) to store the equations to the strings again.

## Error Conditions

- **[ERR:DATA TYPE](errors.html#datatype)** is thrown if the argument is not a *number* 0 through 9.
- **[ERR:UNDEFINED](errors.html#undefined)** is thrown if the requested GDB does not exist.

## Related Commands

- [StoreGDB](storegdb.html)

## See Also

- [Cleaning up](cleanup.html)
