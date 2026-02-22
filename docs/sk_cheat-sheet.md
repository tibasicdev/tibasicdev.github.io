# Command Cheat Sheet
The cheat sheet is a basic list of the programming commands found in the PRGM menu while programming. Each command includes a brief summary, along with its syntax(s) and specific menu location.  Click on the title of each box to see a more detailed description.


[If](if.html)

Checks if a condition is true, and if it is, runs an optional statement or group of statements.

**Command Syntax**

If *condition*
*statement*

If *condition*
Then
*one or more statements*
End

If *condition*
Then
*statement(s) to run if condition is true*
Else
*statement(s) to run otherwise*
End

**Menu Location**

1. PRGM to enter the PRGM menu
2. ENTER or 1 to choose If


[End](end.html)

Indicates the end of a block of statements.

**Command Syntax**

If *condition*
Then
*statement(s)*
End

While *condition*
*statement(s)*
End

Repeat *condition*
*statement(s)*
End

For(*variable*,*start*,*end*[,*step*])
*statement(s)*
End

**Menu Location**

1. PRGM to enter the PRGM menu
2. 8 to choose Pause, or use arrows


[For(](for.html)

Executes some commands many times, with a variable increasing from *start* to *end* by *step*, with the default value *step*=1.

**Command Syntax**

For(*variable*,*start*,*end*[,*step*])
*statement(s)*
End

**Menu Location**

1. PRGM to enter the PRGM menu
2. 4 to choose For(, or use arrows
3. 7 to choose End, or use arrows


[While](while.html)

Loops through a block of code while the condition is true.

**Command Syntax**

While *condition*
*statement(s)*
End

**Menu Location**

1. PRGM to enter the PRGM menu
2. 5 to choose While, or use arrows
3. 7 to choose End, or use arrows


[Repeat](repeat.html)

Loops through a block of code until the condition is true. Always loops at least once.

**Command Syntax**

Repeat *condition*
*statement(s)*
End

**Menu Location**

1. PRGM to enter the PRGM menu
2. 6 to choose Repeat, or use arrows
3. 7 to choose End, or use arrows


[Lbl](lbl.html)

Defines a label for a particular [Goto](goto.html) or [Menu(](menu.html) to jump to.

**Command Syntax**

Lbl *name*

**Menu Location**

1. PRGM to enter the PRGM menu
2. 9 to choose Lbl, or use arrows


[Goto](goto.html)

Jumps to the Lbl instruction with the specified name, and continues running the program from there.

**Command Syntax**

Goto *name*
…
Lbl *name*

**Menu Location**

1. PRGM to enter the PRGM menu
2. 0 to choose Goto, or use arrows
3. 9 to choose Lbl, or use arrows


[prgm](prgm.html)

Calls another program from within a program, with program execution moving to that program.

**Command Syntax**

prgm*NAME*

**Menu Location**

1. PRGM to enter the PRGM menu
2. LEFT to enter the EXEC submenu
3. Select a program


[IS>(](is-.html)

Increments a variable by one and skips the next command if the variable is greater than the value.

**Command Syntax**

IS>(*variable*,*value*)

**Menu Location**

1. PRGM to enter the PRGM menu
2. A to choose IS>(, or use arrows


[DS<(](ds-.html)

Decrements a variable by one and skips the next command if the variable is less than the value.

**Command Syntax**

DS<(*variable*,*value*)

**Menu Location**

1. PRGM to enter the PRGM menu
2. ALPHA MATH to choose DS<(, or use arrows


[Return](return.html)

Stops the program and returns the user to the home screen. If the program is a subprogram, however, it just stops the subprogram and returns program execution to the parent program.

**Command Syntax**

Return

**Menu Location**

1. PRGM to enter the PRGM menu
2. ALPHA SIN to choose Return, or use arrows


[Stop](stop.html)

Completely stops the current program and any parent programs.

**Command Syntax**

Stop

**Menu Location**

1. PRGM to enter the program menu
2. ALPHA F to choose Stop, or use arrows


[DelVar](delvar.html)

Deletes a variable from memory.

**Command Syntax**

DelVar *variable*

**Menu Location**

1. PRGM to enter the PRGM menu
2. ALPHA TAN to choose DelVar, or use arrows


[GraphStyle(](graphstyle.html)

Sets the graphing style of a graphing equation in the current mode.

**Command Syntax**

GraphStyle(*equation #*, *style #*)

**Menu Location**

1. PRGM to access the programming menu
2. ALPHA H to select GraphStyle(, or use arrows


[DispGraph](dispgraph.html)

Displays the graph screen.

**Command Syntax**

DispGraph

**Menu Location**

1. PRGM to access the program menu
2. RIGHT to access the I/O submenu
3. 4 to select DispGraph, or use arrows


[DispTable](disptable.html)

Displays the table screen.

**Command Syntax**

DispTable

**Menu Location**

1. PRGM to access the program menu
2. RIGHT to select the I/O submenu
3. 5 to select DispTable, or use arrows


[ClrHome](clrhome.html)

Clears the home screen of any text.

**Command Syntax**

ClrHome

**Menu Location**

1. PRGM to enter the PRGM menu
2. RIGHT to enter the I/O menu
3. 8 to choose ClrHome, or use arrows


[Disp](disp.html)

Displays an expression, a string, or several expressions and strings on the home screen.

**Command Syntax**

Disp [argument1,argument2,...]

**Menu Location**

1. PRGM to enter the PRGM menu
2. RIGHT to enter the I/O menu
3. 3 to select Disp, or use arrows


[Output(](output.html)

Displays an expression on the home screen starting at a specified row and column. Wraps around if necessary.

**Command Syntax**

Output(*row*, *column*, *expression*)

**Menu Location**

1. PRGM to enter the PRGM menu
2. RIGHT to enter the I/O menu
3. 6 to choose Output(, or use arrows


[Pause](pause.html)

Pauses a program until the user presses ENTER.

**Command Syntax**

Pause [*value or text*]

**Menu Location**

1. PRGM to enter the PRGM menu
2. 8 to choose Pause, or use arrows


[Menu(](menu.html)

Displays a generic menu on the home screen, with up to seven options for the user to select.

**Command Syntax**

Menu("*Title*","*Option 1*",Label 1[,...,"*Option 7*",Label 7])

**Menu Location**

1. PRGM to enter the PRGM menu
2. Press ALPHA PRGM to choose Menu(, or use arrows


[Input](input.html)

Prompts the user to enter a value and then stores the value to the variable.

Displays the graph screen and then the user can move around the cursor.

**Command Syntax**

Input

Input [*"Text"*,]*variable*

**Menu Location**

1. PRGM to enter the PRGM menu
2. RIGHT to enter the I/O menu
3. 1 to choose Input


[Prompt](prompt.html)

Prompts the user to enter values for variables and then stores those values to the variables.

**Command Syntax**

Prompt *variableA*[,*variableB*,...]

**Menu Location**

1. PRGM to enter the PRGM menu
2. RIGHT to enter the I/O menu
3. 2 to choose Prompt, or use arrows


[getKey](getkey.html)

Returns the numerical code of the last key pressed, or 0 if no key is pressed.

**Command Syntax**

getKey[→*Variable*]

**Menu Location**

1. PRGM to enter the PRGM menu
2. RIGHT to enter the I/O menu
3. 7 to choose getKey, or use arrows


[GetCalc(](getcalc.html)

Gets a variable from another calculator.

**Command Syntax**

GetCalc(*variable*)

(84+ and 84+SE only)
GetCalc(*variable*,*portflag*)

**Menu Location**

1. PRGM to enter the PRGM menu
2. RIGHT to enter the I/O menu
3. 9 to choose GetCalc(, or use arrows


[Get(](get.html)

Gets a variable's value from a connected calculator or CBL device.

**Command Syntax**

Get(*variable*)

**Menu Location**

1. PRGM to access the program menu
2. RIGHT to access the I/O menu
3. ALPHA A to select Get(


[Send(](send.html)

Sends data or a variable to a connected CBL device.

**Command Syntax**

Send(*variable*)

**Menu Location**

1. PRGM to access the program menu
2. RIGHT to access the I/O submenu
3. ALPHA B to select Send(


<center>

|**[<< What next?](sk:what-next.html)**|**[Table of Contents](starter-kit.html)**|**[Example Routines >>](routines.html)**|
| --- | --- | --- |

</center>
