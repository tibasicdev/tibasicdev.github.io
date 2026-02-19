# The Home Screen and Its Commands
The TI-83/+/SE home screen is composed of eight rows (1 to 8 from top to bottom) by sixteen columns (1 to 16 from left to right); it is like a grid. The home screen uses the large, easy to see, 5 by 7 font. Because each character takes up the same 5 by 7 space, regardless of what its actual size is, the text cannot be moved around to get pixel perfect precision. 
The table below shows the coordinates used for the Output( command (see below). Enter these coordinates in the Output( command as shown, only without the parentheses. There are different coordinates for a TI-84+C SE (10 rows and 26 columns, to be exact).


|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | (1,1) | (1,2) | (1,3) | (1,4) | (1,5) | (1,6) | (1,7) | (1,8) | (1,9) | (1,10) | (1,11) | (1,12) | (1,13) | (1,14) | (1,15) | (1,16) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | (2,1) | (2,2) | (2,3) | (2,4) | (2,5) | (2,6) | (2,7) | (2,8) | (2,9) | (2,10) | (2,11) | (2,12) | (2,13) | (2,14) | (2,15) | (2,16) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | (3,1) | (3,2) | (3,3) | (3,4) | (3,5) | (3,6) | (3,7) | (3,8) | (3,9) | (3,10) | (3,11) | (3,12) | (3,13) | (3,14) | (3,15) | (3,16) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | (4,1) | (4,2) | (4,3) | (4,4) | (4,5) | (4,6) | (4,7) | (4,8) | (4,9) | (4,10) | (4,11) | (4,12) | (4,13) | (4,14) | (4,15) | (4,16) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | (5,1) | (5,2) | (5,3) | (5,4) | (5,5) | (5,6) | (5,7) | (5,8) | (5,9) | (5,10) | (5,11) | (5,12) | (5,13) | (5,14) | (5,15) | (5,16) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6 | (6,1) | (6,2) | (6,3) | (6,4) | (6,5) | (6,6) | (6,7) | (6,8) | (6,9) | (6,10) | (6,11) | (6,12) | (6,13) | (6,14) | (6,15) | (6,16) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | (7,1) | (7,2) | (7,3) | (7,4) | (7,5) | (7,6) | (7,7) | (7,8) | (7,9) | (7,10) | (7,11) | (7,12) | (7,13) | (7,14) | (7,15) | (7,16) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 8 | (8,1) | (8,2) | (8,3) | (8,4) | (8,5) | (8,6) | (8,7) | (8,8) | (8,9) | (8,10) | (8,11) | (8,12) | (8,13) | (8,14) | (8,15) | (8,16) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

The home screen does not have access to any of the drawing commands that are available on the [graph screen](graphscreen.html) (such as the points, pixels, lines, or circles). This leaves you with just using the [text](textcommands.html) to imitate graphics, which unfortunately does not look very good. Using the home screen is faster than using the graph screen, though.

There are five main home screen commands:

- **[ClrHome](clrhome.html)** — Clears the home screen of any text or numbers. It should be used at the beginning of a program and at the end to make sure the user has a clear screen afterwards.
- **[Disp](disp.html)** — Displays one or more arguments of text or values on a new line on the home screen and scrolls down if necessary. Disp should be used instead of Output( in most cases.
- **[Output(](output.html)** — Displays text or a value at a specified row and column location on the home screen. It also wraps the text or value around the screen if needed.
- **[Pause](pause.html)** — Pauses the program and displays the home screen until the user presses ENTER. It also can display text or a value with scrolling available.
- **[Menu(](menu.html)** — Displays a generic menu on the home screen, with up to seven options for the user to select from. It utilizes branching to make the menu.

You should commit yourself to learning how to use these commands and then actually start using them in your programs. They are rather basic, but still quite powerful. Once you have them down, move on to the graph screen commands.
