# Error Conditions
[A](#A) | [B](#B) | [D](#D) | [E](#E) | [I](#I) | [L](#L) | [M](#M) | [N](#N) | [O](#O) | [R](#R) | [S](#S) | [T](#T) | [U](#U) | [V](#V) | [W](#W) | [Z](#Z)


In the Error Conditions section on a command page, descriptions will be given of the errors that can result when using a command. These do not include errors that can occur with virtually any command, such as **[ERR:ARGUMENT](#argument)** or **[ERR:SYNTAX](#syntax)**. However, if one of these errors is triggered in an unusual way, it will be listed.

Be aware that certain errors don't occur when graphing or using one of the commands [DrawF](drawf.html), [DrawInv](drawinv.html), [Tangent(](tangent.html), or [Shade(](shade.html). Instead, the graph point is skipped and treated as an undefined value. Tangent( is a minor exception, actually: if there's an error at the tangent point, it will be treated normally. The errors that are ignored in graphs are:
- **[ERR:DATA TYPE](#datatype)**
- **[ERR:DIVIDE BY 0](#divideby0)**
- **[ERR:DOMAIN](#domain)**
- **[ERR:INCREMENT](#increment)**
- **[ERR:NONREAL ANS](#nonrealans)**
- **[ERR:OVERFLOW](#overflow)**
- **[ERR:SINGULAR MAT](#singularmat)**

There are are also several error messages that don't actually occur (as far as anyone knows) from normal use of the calculator — however, the messages are stored in the OS along with the normal messages. It's conceivable that an assembly program, especially an official TI application, would use these error messages for its own purposes. These messages are ERR:SOLVER, ERR:SCALE, ERR:NO MODE, ERR:LENGTH, and ERR:APPLICATION. 


## A {#A}


### ARCHIVED {#archived}

- You have attempted to use, edit, or delete an archived variable. For example, dim(L1) is an error if L1 is archived. 
- Use [UnArchive](unarchive.html) *variable name* to unarchive the variable before using it. For lists, [SetUpEditor](setupeditor.html) is recommended instead since it does the same thing, but works on the TI-83 (which has no archive) as well, and does not crash when the list is undefined.
- There is no way to archive or unarchive programs using pure Basic, although several [assembly](assembly.html) utilities are available for doing so.
- When you attempt to edit a archived Matrix,List,Variable, or program, the option 2:GOTO doesn't show up.
- Use Unarchive or the memory manager to unarchive a variable,matrix,list, program, etc.

### ARCHIVE FULL {#archivefull}

- You have attempted to archive a variable and there is not enough space in archive to receive it.
- Sometimes, if the calculator displays a message from memory management saying "Garbage Collect?", choosing the option No gives this error.

### ARGUMENT {#argument}

- A function or instruction does not have the correct number of arguments. See the appropriate [command](command-index.html) page.
- A function or instruction that can have any number of arguments has 256 or more.
- In general, if a function has more than one non-SYNTAX error in it, this is the error that will be generated first (if it applies, of course). 
- Generally, on graphing calculators and such, most functions ex: [randInt(](randint.html) require that you use commas to make a list.


## B {#B}


### BAD ADDRESS {#badaddress}

- You have attempted to send or receive an application and an error (e.g., electrical interference) has occurred in the transmission.

### BAD GUESS {#badguess}

- With the [solve(](solve.html) function, the equation solver, or an operation from the CALC menu, your guess wasn't within the lower and upper bound, or else the function is undefined at that point. Change the guess.

### BOUND {#bound}

- In a CALC operation or with [Select(](select.html), you defined Left Bound > Right Bound.
- In [fMin(](fmin.html), [fMax(](fmax.html), [solve(](solve.html), or the equation solver, the lower bound must be less than the upper bound.

### BREAK {#break}

- You pressed the [ON] key to break execution of a program, to halt a DRAW instruction, or to stop evaluation of an expression.


## D {#D}


### DATA TYPE {#datatype}

- You entered a value or variable that is the wrong data type.
- For a function (including implied multiplication) or an instruction, you entered an argument that is an invalid data type, such as a complex number where a real number is required.
- In an editor, you entered a type that is not allowed, such as a matrix entered as an element in the stat list editor.
- You attempted to store an incorrect data type, such as a matrix to a list.
- You attempted to divide matrices, which should be done by matrix inversion and multiplication instead.
- This error is not returned when graphing (see the [note](#note) at the top of the page).

### DATE {#date}

- Only on the TI-84+ or TI-84+ SE, this error occurs when an invalid date is entered.
- Below the error menu, an explanation of what's wrong is given: e.g., "Invalid day for month selected."

### DIM MISMATCH {#dimmismatch}

- You attempted to perform an operation that references more than one list or matrix, but the dimensions do not match.
- In most cases, the dimensions are required to be equal, with the following exceptions:
 - When multiplying two matrices, the number of columns of the first must match the number of rows of the second.
 - When using [augment(](augment.html) to combine two matrices, only the number of rows must match.
 - With the [List►matr(](list-matr.html) command, the lists don't have to match sizes - shorter lists will be padded with zeroes.

### DIVIDE BY 0 {#divideby0}

- You attempted to divide by zero. 
- You attempted a linear regression on data that fit a vertical line.
- This error is not returned when graphing (see the [note](#note) at the top of the page).

### DOMAIN {#domain}

- You specified an argument to a function or instruction outside the valid range. This error is not returned during graphing. The TI-83+ allows for undefined values on a graph.
- You attempted a logarithmic or power regression with a negative X or an exponential or power regression with a negative Y.
- You attempted to compute [ΣPrn(](sigmaprn.html) or [ΣInt(](sigmaint.html) with pmt2 < pmt1.
- You've assigned a value to *n* (the sequential graph variable), *n*Min or *n*Max that isn't an integer, or that is less than 0.
- This error is not returned when graphing (see the [note](#note) at the top of the page).

### DUPLICATE {#duplicate}

- You attempted to create a duplicate group name.
- You attempted to create a duplicate program using [AsmComp(](asmcomp.html).

### Duplicate Name {#duplicatename}

- A variable you attempted to transmit cannot be transmitted because a variable with that name already exists in the receiving unit.
- Also appears when you unpack a group and a variable in the group is already defined. In both cases, it will give you several options for correcting the error, including Omit, Rename, and Overwrite.


## E {#E}


### EXPIRED {#expired}

- You have attempted to run a Flash application with a limited trial period which has expired.

### Error in Xmit {#errorinxmit}

- The TI-83+ was unable to transmit an item. Check to see that the cable is firmly connected to both units and that the receiving unit is in receive mode.
- You pressed [ON] to break during transmission.
- You attempted to perform a backup from a TI-82 to a TI-83+.
- You attempted to transfer data (other than L1 through L6) from a TI-83+ to a TI-82.
- You attempted to transfer L1 through L6 from a TI-83+ to a TI-82 without using 5:Lists to TI-82 on the LINK SEND menu.
- You attempted to use SendOS with no other calculator connected. 
- When this error occurs, the option 2:Goto doesn't show up, but will redirect you to the LINK screen instead of the main screen.


## I {#I}


### ID NOT FOUND {#idnotfound}

- This error occurs when the SendID command is executed, but the proper calculator ID cannot be found.
- When this error occurs, the option 2:Goto does not show up.
### ILLEGAL NEST {#illegalnest}

- You attempted to use an invalid function in an argument to a function.
- This happens when using [seq(](seq-list.html) in the expression for seq(, [fnInt(](fnint.html) within the first argument of fnInt(, [expr(](expr.html) inside the string argument of expr(, or [Σ(](summationsigma.html) within the argument for Σ(.

### INCREMENT {#increment}

- The increment in [seq(](seq-list.html) is 0 or has the wrong sign.
- The increment in a [For(](for.html) loop is 0.
- This error is not returned when graphing (see the [note](#note) at the top of the page).

### INVALID {#invalid}

- You attempted to reference a variable or use a function where it is not valid. For example, Yn cannot reference Y, Xmin, ΔX, or TblStart.
- You attempted to reference a variable or function that was transferred from the TI-82 and is not valid for the TI-83+. For example, you may have transferred UnN1 to the TI-83+ from the TI-82 and then tried to reference it.
- In Seq mode, you attempted to graph a phase plot ([uvAxes](uvaxes.html), [uwAxes](uwaxes.html), or [vwAxes](vwaxes.html)) without defining both equations of the phase plot.
- In Seq mode, you attempted to graph a recursive sequence without having input the correct number of initial conditions.
- In Seq mode, you attempted to reference terms other than (n-1) or (n-2).
- You attempted to designate a graph style that is invalid within the current graph mode.
- You attempted to use [Select(](select.html) without having selected (turned on) at least one xyLine or scatter plot.
- You attempted to use certain functions (e.g. [If](if.html), [Then](then.html), [Else](else.html)) outside a program.

### INVALID DIM {#invaliddim}

- You tried to access an element past the end of a list or matrix (there is an exception: it's allowed to store to the element one past the end of a list, adding the element).
- You specified dimensions for an argument that are not appropriate for the operation.
- You specified a [list](lists.html) dimension as something other than an integer between 1 and 999.
- You specified a [matrix](matrices.html) dimension as something other than an integer between 1 and 99.
- You attempted to invert a matrix that is not square.

### ITERATIONS {#iterations}

- The [solve(](solve.html) function or the equation solver has exceeded the maximum number of permitted iterations. Examine a graph of the function. If the equation has a solution, change the bounds, or the initial guess, or both.
- [irr(](irr.html) has exceeded the maximum number of permitted iterations.
- When computing I%, the maximum number of iterations was exceeded.


## L {#L}


### LABEL {#label}

- The label in the [Goto](goto.html) instruction is not defined with a [Lbl](lbl.html) instruction in the program.
- When this error occurs, the option 2:Goto doesn't show up.

### Link {#link}
- Something in the flash application was invalid while running.
- When this error occurs, the option 2:Goto doesn't show up.


## M {#M}


### MEMORY {#memory}

- Memory is insufficient to perform the instruction or function. You must delete items from memory before executing the instruction or function.
- You might also want to try archiving some variables,matrixes,lists,etc if you have nothing in RAM that you don't need.
- Recursive problems return this error; for example, graphing the equation Y1=Y1. (but Y1=X, Y2=Y1, for example, will NOT cause an error.)
- Branching out of an [If:Then](if.html), [For(](for.html), [While](while.html), or [Repeat](repeat.html) loop with a [Goto](goto.html) will waste memory until the program finishes running, because the [End](end.html) statement that terminates the loop is never reached. Unless a program is very large, this is one of the likeliest causes of ERR:MEMORY.  Refer to [memory-leaks](memory-leaks.html).

### MemoryFull {#memoryfull}

- You are unable to transmit an item because the receiving unit’s available memory is insufficient. You may skip the item or exit receive mode.
- During a memory backup, the receiving unit’s available memory is insufficient to receive all items in the sending unit’s memory. A message indicates the number of bytes the sending unit must delete to do the memory backup. Delete items and try again.
- You may also try to archive some variables to free up some memory that you do not plan to transmit.

### MODE {#mode}

- You attempted to store to a [window variable](system-variables.html#window) in another graphing mode or to perform an instruction while in the wrong mode; for example, [DrawInv](drawinv.html) in a graphing mode other than [Func](func.html).


## N {#N}


### NO SIGN CHNG {#nosignchng}

- The [solve(](solve.html) function or the equation solver did not detect a sign change.
- You attempted to compute I% when FV, (N*PMT), and PV all share the same sign.
- You attempted to compute [irr(](irr.html) when CFList and CFO share the same sign.

### NONREAL ANS {#nonrealans}

- In [Real](real-mode.html) mode, the result of a calculation yielded a complex result.
- This error is not returned when graphing (see the [note](#note) at the top of the page).
- This error can appear if you use a negative number for some operations, such as [ln](ln.html)


## O {#O}


### OVERFLOW {#overflow}

- You attempted to enter, or you have calculated, a number that is beyond the range of the calculator (-1<sub>E</sub>100 to 1<sub>E</sub>100, non-inclusive). 
- Sometimes you can fix this error by re-ordering operations. For example, 60!*30!/20! will return an overflow error, but 60!/20!*30! will not.
- This error is not returned when graphing (see the [note](#note) at the top of the page).


## R {#R}


### RESERVED {#reserved}

- You attempted to use a [system variable](system-variables.html) inappropriately (for example, performing [1-Var Stats](1-var-stats.html) on the reserved list ∟RESID).


## S {#S}


### SINGULAR MAT {#singularmat}

- A singular matrix (determinant = 0) is not valid as the argument for <sup>-1</sup>.
- A [regression](regression-models.html) generated a singular matrix (determinant = 0) because it could not find a solution, or a solution does not exist.
- This error is not returned when graphing (see the [note](#note) at the top of the page).

### SINGULARTY {#singularity}

- The expression in the [solve(](solve.html) function or the equation solver contains a singularity (a point at which the function is not defined). Examine a graph of the function. If the equation has a solution, change the bounds or the initial guess or both.
- Although the correct spelling is "singularity", the error message shown has "singularty" on all calculators and OS versions.

### STAT {#stat}

- You attempted a stat calculation with lists that are not appropriate.
- Statistical analyses must have at least two data points.
- Med-Med must have at least three points in each partition.
- When you use a frequency list, its elements must be at least 0.
- (Xmax - Xmin) / Xscl must equal 47 for a histogram.

### STAT PLOT {#statplot}

- You attempted to display a graph when a stat plot that uses an undefined list is turned on.
- To fix this error, use the command [PlotsOff](plotsoff.html) to turn off plots when you're using the graph screen.

### SYNTAX {#syntax}

- The command contains a syntax error. Look for misplaced functions, arguments, parentheses, or commas. See the appropriate [command](command-index.html) page.
- This error will also occur in place of a DATA TYPE error if the variable type in question is a variable name (with [seq(](seq.html), [solve(](solve.html), [For(](for.html), and other commands)
- The command was attempting to get [expr(](expr.html) of a non-value string, i.e., trying to evaluate a space, equals sign, etc.


## T {#T}


### TOL NOT MET {#tolnotmet}

- You requested a tolerance to which the algorithm cannot return an accurate result.


## U {#U}


### UNDEFINED {#undefined}

- You referenced a variable that is not currently defined. This error doesn't occur with number variables (A-Z,θ), which have a default value of 0.
- Lists, matrices,strings,pictures, and GDBs have to be stored to first, in order to be used.
- Most [system variables](system-variables.html) always have a value, so this error doesn't apply to them.
- However, [statistical](statistics.html) variables are undefined except for those used by the last relevant command.
- Undefined equation variables (such as Parametric and Polar variables) return ERR:INVALID instead of ERR:UNDEFINED.


## V {#V}


### VALIDATION {#validation}

- Electrical interference caused a link to fail or this calculator is not authorized to run the application and/or Operating System.

### VARIABLE {#variable}

- You have tried to archive a variable that cannot be archived or you have have tried to unarchive an application or group.
- Variables that cannot be archived include:
 - The number variables R, T, X, Y, and θ (because they are used for graphing)
 - The list ∟RESID (because it's reserved for residuals from [regression models](regression-models.html))
 - [System variables](system-variables.html) (including [statistical](statistics.html) variables, [finance](finance.html) variables, equations, plots, and window variables)
 - The AppIdList.

### VERSION {#version}

- You have attempted to receive an incompatible variable version from another calculator.
- You have attempted to use or display certain corrupted tokens that the calculator will not allow.


## W {#W}


### WINDOW RANGE {#windowrange}

- A problem exists with the window variables.
 - You defined Xmin>Xmax or Ymin>Ymax.
 - Xmin and Xmax (or Ymin and Ymax) are equal or so close that numerical precision can't allow for enough values between them.
 - The values for θmin, θmax, and θstep create an empty or never-ending loop for θ.
 - The values for Tmin, Tmax, and Tstep create an empty or never-ending loop for T.
- When this error occurs, the option 2:Goto doesn't show up.


## Z {#Z}


### ZOOM {#zoom}

- A point or a line, instead of a box, is defined in ZBox.
- A ZOOM operation returned a math error.
- When this error occurs, the option 2:Goto doesn't show up.


## Other


### ?

- An unknown error has occurred.
