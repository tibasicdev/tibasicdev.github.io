![The Input Command](68k_input/input.png "The Input Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Asks for a value to be typed in on the I/O screen.|Input [*prompt*,]*variable*<br>Input|This command works on all calculators.|3 bytes|
       
### Menu Location
Starting in the program editor:<br>* Press F3 to enter the I/O menu.<br>* Press 3 to select Input.
# The Input Command

Input *prompt*, *variable* displays *prompt* (which should be a string) on a new line on the Program I/O screen, then waits for the user to type in an expression on the next line. Whatever is typed in is then stored to *variable*. You can leave out the *prompt* part to just have the prompt be a question mark.

Note that whatever is typed in will be interpreted very literally: you'll need { } brackets to enter a list, quotes to enter a string, and so on. If you do want to enter a string, [68k:InputStr](68k:inputstr.html) is probably a better choice.

[68k:Prompt](68k:prompt.html) is a special case of Input: Prompt *variable* works just as Input does, with *variable*? (the variable name, and a question mark) as the prompt.

If there's an error (for example, a syntax error) in the line that got typed in, the calculator will display the appropriate error message, and ask for the line to be typed in again: the program will continue running as usual. The calculator can even be turned off while Input is running; when it's turned back on, it will continue waiting for input, and then the program will still continue running.

## Advanced Uses

Another use of Input is without any parameters at all: Input by itself will display a cursor on the graph screen, and wait until a point is selected (the cursor can be moved left and right as usual, and a point is selected by pressing ENTER). 

You can find out which point was selected by using the xc and yc [68k:system variables](68k:system-variables.html) (xc is the x-coordinate, and yc is the y-coordinate). The Coordinates [graph setting](68k:mode-settings.html) determines other behavior:
- If it's set to RECT, the values of xc and yc will be displayed at the bottom of the screen when the point is being selected. 
- If it's set to POLAR, the polar coordinates will be stored to system variables rc and θc (in addition to the regular coordinates). The values of rc and θc will be displayed while the point is being selected.
- If it's set to OFF, no coordinates will be displayed (although xc and yc will still contain the resulting coordinate).

------

If Input is located inside a [68k:Try](68k:try.html)..EndTry block, and the ON key is pressed, the "Break" error will be caught (one of the only times this happens). If you're a nice person, you can use this to add code to exit quietly (without an error message) when ON is pressed. If you're not a nice person, you can use this to create an infinite loop you can't use ON to break out of.

## Related Commands

- [68k:Disp](68k:disp.html)
- [68k:InputStr](68k:inputstr.html)
- [68k:Prompt](68k:prompt.html)
