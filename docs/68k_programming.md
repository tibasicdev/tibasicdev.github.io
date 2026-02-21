# Programming Commands
Every command on the calculator is useful for programming, but some are expressly designed for that purpose. These are roughly divided into three categories: commands to control the flow of a program, commands to manage variables, and commands that provide input and output.

## Control Flow

Any program is just a sequence of commands; but usually, it's not enough to just run through them all one by one in order and be done. Changes to this order have to be made: some commands should only be followed in certain situations, others might be repeated several times, still others might be a last resort in case of an error. Control flow commands are those that determine this order.

The simplest control flow commands are [68k:Goto](68k:goto.html) and [68k:Lbl](68k:lbl.html), which simply involve jumping around in the program. This isn't always the best way of doing things, though, and there are many alternatives:

### Conditionals

A common situation is when certain commands depend on a condition being met. The following commands address this situation:
- The [68k:If](68k:if.html) statement simply places a condition on a command or block of commands.
- The [68k:Else](68k:else.html) statement, used with If, provides an alternative branch if the condition is not met.
- The [68k:ElseIf](68k:elseif.html) statement, also used with If, allows for several mutually exclusive conditions.

Conditions are typically created by combining equality relations ([=](68k:equal.html), [≠](68k:not-equal.html), [>](68k:greater-than.html), [≥](68k:greater-than-or-equal.html), [<](68k:less-than.html), [≤](68k:less-than-or-equal.html)) with logical operators ([68k:and](68k:and.html), [68k:or](68k:or.html), [68k:xor](68k:xor.html), [68k:not](68k:not.html)).

### Loops

Loops allow commands to be repeated over and over. The following types of loops exist:
- [68k:Loop](68k:loop.html)..EndLoop blocks just keep repeating forever.
- [68k:While](68k:while.html)..EndWhile blocks repeat as long as a condition is satisfied.
- [68k:For](68k:for.html)..EndFor blocks repeat a fixed number of times.
To deal with these loops, we have a couple auxiliary commands:
- [68k:Cycle](68k:cycle.html) prematurely goes back to the beginning of a loop.
- [68k:Exit](68k:exit.html) leaves a loop ahead of time.

### Subroutines

If a task has to be done several times inside a program, the code for it can be removed to a subroutine: this routine can then be "called" whenever necessary. Subroutines in TI-Basic are essentially programs of their own. They can be defined inside a program with the [68k:Define](68k:define.html) command, and are of two types:
- Functions (defined with [68k:Func](68k:func.html)..EndFunc) return a value, and can't affect the overall state of the calculator.
- Programs (defined with [68k:Prgm](68k:prgm.html)..EndPrgm) can do anything, but don't return a value directly.
Two commands exist specifically for use with subroutines.
- [68k:Return](68k:return.html) exits a subroutine, returning to the program that called it.
- [68k:Stop](68k:stop.html) exits every program currently running, subroutine or not.

### Error Catching

Error catching provides a last resort if an error occurs. A portion of the program, or even the entire program itself, can be put into a [68k:Try](68k:try.html)..Else..EndTry block. The code after Else will only run in case of an error, and has the option to [68k:ClrErr](68k:clrerr.html) — go on as though nothing happened — or [68k:PassErr](68k:passerr.html) — handle the error normally, with an OS error message.

## Variable Management

Another part of programming is managing variables. This means:
- Defining them — with [→](68k:store.html) or [68k:Define](68k:define.html).
- Deleting them — with [68k:DelVar](68k:delvar.html), [68k:DelType](68k:deltype.html), [68k:DelFold](68k:delfold.html), or [68k:NewProb](68k:newprob.html).
- Protecting them — with [68k:Lock](68k:lock.html), [68k:Unlock](68k:unlock.html), [68k:isLocked()](68k:islocked.html), [68k:Archive](68k:archive.html), [68k:Unarchiv](68k:unarchiv.html), or [68k:isArc()](68k:isarc.html).
- Dealing with names and folders — with [68k:CopyVar](68k:copyvar.html), [68k:MoveVar](68k:movevar.html), [68k:Rename](68k:rename.html), or [68k:NewFold](68k:newfold.html), [68k:setFold()](68k:setfold.html).

There is also the [68k:Local](68k:local.html) command, which designates certain variables as local to the program they are used in.

## Input and Output

Finally, a program has to be able to get input from the user and give some output in response. For games, this usually means using the [68k:graphics](68k:graphics.html) commands, and reading keys with the [68k:getKey()](68k:getkey.html) command. There are other alternatives, however.

On the Program I/O screen:
- [68k:Input](68k:input.html), [68k:InputStr](68k:inputstr.html), and [68k:Prompt](68k:prompt.html) read in typed text.
- [68k:Disp](68k:disp.html), [68k:Output](68k:output.html), and [68k:Pause](68k:pause.html) display text.
- [68k:ClrIO](68k:clrio.html) clears the I/O screen.

A more stylish method is to use [68k:dialogs](68k:dialogs.html), wrapped in a [68k:Dialog](68k:dialog.html)..EndDlog box.
- Input here is accomplished with [68k:Request](68k:request.html) and [68k:DropDown](68k:dropdown.html).
- The [68k:Text](68k:text.html) command, appropriately, displays text. A [68k:Title](68k:title.html) is also handy.

Some miscellaneous commands remain. [68k:Custom](68k:custom.html)..EndCustm and [68k:Toolbar](68k:toolbar.html)..EndTBar both create toolbar menus with the help of the [68k:Title](68k:title.html) and [68k:Item](68k:item.html) commands. And [68k:PopUp](68k:popup.html) displays a popup menu.

Input and output also refers to interacting with other calculators. There are five commands for the purpose:
- [68k:Get](68k:get.html) and [68k:GetCalc](68k:getcalc.html) read data from a connected calculator.
- [68k:Send](68k:send.html), [68k:SendCalc](68k:sendcalc.html), and [68k:SendChat](68k:sendchat.html) send data to a connected calculator.
