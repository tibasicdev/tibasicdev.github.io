# The Graphscreen and Its Commands
The TI-83/+/SE graphscreen is 64 rows, by 96 columns, the coordinates for the pixels being 0 to 62 a total of 63 and 0 to 93 a total of 94. So amount of editable X and Y pixels are 95 and 63. With the coordinates 0,0 actually being the very top left pixel. The graphscreen uses the small (3 by 5) font, which allows you to display more text; and the large (5 by 7) font, which allows you to make the graphscreen look like the homescreen. On the color calculators, the available screen is 165rows by 265 columns, starting at 0. Graphics can also be displayed on the graphscreen, in the form of points, pixels, lines, or circles, as well as shading an area of the graphscreen. These graphics can be displayed with the text, and they can be saved to pictures for later use.

The graphscreen does not have access to some of the commands that are available on the homescreen (such as the user input). In addition, some of the graphscreen commands have their coordinates reversed, so the row comes before the column. These commands also take longer to draw.



## Setting up the Graphscreen

*Note: it is good practice to save the current settings at the beginning of the program with `StoGDB`, and recall it later with `RclGDB`. The syntax for those commands is illustrated below.*

Before using the graphscreen, you first need to set it up appropriately. When displaying text or drawing graphics, you want to make sure that they are displayed how you want them to be displayed. This is achieved by clearing the graphscreen, adjusting the window dimensions, and turning off the graph formats.

### Clearing the Graphscreen

The ClrDraw command is the graphscreen equivalent to ClrHome. ClrDraw is usually used before you display text or draw anything on the graphscreen, to ensure that it won't be interrupted by anything that was previously displayed on the graphscreen.

```
Format
:ClrDraw
```

You also want to make sure to clear the graphscreen when exiting programs. This ensures that the next program that the user runs won't have to deal with whatever text or graphics your program left behind. It also helps the user, because they won't have to manually clear the graphscreen.

To use the ClrDraw command, you should first be in the Program editor for your program. In the Program editor, press 2nd and PRGM. Then press ENTER on ClrDraw. Now the command has been put into your program.

### Adjusting the Window Dimensions

After clearing the graphscreen, you will want to set the window dimensions to the desired size. There are four window variables that control the window dimensions: Xmin, Xmax, Ymin, and Ymax. When storing values in these variables, you have to remember that the max variables always have to be larger then the min variables, otherwise you will get an error.

The Xmin variable sets the minimum value that the X coordinate can have. The Xmax variable sets the maximum value that the X coordinate can have. The Ymin variable sets the minimum value that the Y coordinate can have. The Ymax variable sets the maximum value that the Y coordinate can have. You can use these variables like regular variables.

```
Format
:#→Xmin:#→Xmax
:#→Ymin:#→Ymax
```

Although the graphscreen is 96 pixels wide by 64 pixels tall on the monochrome calculators, and 320 pixels wide by 240 pixels tall on the color calculators, the bottom row is unusable for monochrome TI-Basic programs and the far right column is reserved for the monochrome pause indicator. On the color calculators, the screen is taken up with a border, and the info bar on the top of the screen.  So, most monochrome programmers set the window dimensions to 0 for Xmin and Ymin, 94 for Xmax, and 62 for Ymax. This sets the X range from -1 to 94 totaling 95 columns and the Y range from -1 to 62 totaling 63. On the color calculators, most programs set the screen to `ZStandard`, then `ZSquare`, making the screen 20 spaces on the Y axis, and just over 32 on the X.
```
Format
:0→Xmin:94→Xmax
:0→Ymin:62→Ymax
```

In a simpler notion, to make everything positive from the bottom left corner you would use the following code.

```
Format
:1→Xmin:95→Xmax
:1→Ymin:63→Ymax
```

Others set 0 for Xmin and Ymax, 94 for Xmax and -62 for Ymin. This allows them to use the same coordinates for pixel and point commands, as pixel rows on the screen are counted starting from the top. So the top pixel row is 0 and the bottom row is 62, while the point top row is 0 and bottom row is -62.

In addition to those four window variables, there are two other window variables that you can use to set the window dimensions. ΔX is the difference between Xmin and Xmax divided by the graphscreen width and ΔY is the difference between Ymin and Ymax divided by the graphscreen height. When you set Xmin and Ymin to 0, you just need to set ΔX and ΔY to 1 to make Xmax 94 and Ymin 62.

```
:0→Xmin:94→Xmax
:0→Ymin:62→Ymax
Replace with ΔX and ΔY
:0→Xmin:1→ΔX
:0→Ymin:1→ΔY
```

To use the window variables, you should first be in the Program editor for your program. In the Program editor, press VARS and 1, then scroll down to whichever variable you want to use and press ENTER. Now the variable has been put into your program. You then have to type what number you want to set the window variable to.

In addition to setting the window variables individually, there are also a couple commands that can set them all at the same time. Although these commands are only useful in a couple situations, they are a lot easier (and smaller) to use.

The ZStandard command sets the window dimensions to their default settings (which is -10 for Xmin and Ymin, and 10 for Xmax and Ymax). The ZSquare command sets the window dimensions so that they make the screen square. This is important when drawing circles because it makes the circles look like circles (instead of ellipses).

```
Format
:ZStandard
:ZSquare
```

To use the ZStandard or ZSquare command, you should first be in the Program editor for your program. In the Program editor, press the ZOOM key. Then scroll down to whichever command you want to use and press ENTER. Now the command has been put into your program.

### Turning off the Graph Formats

After adjusting the window dimensions, you will want to turn off the graph formats. The graph formats include the grids, plots, axes, and functions. These can be turned off and turned on, depending on what is desired.

The GridOff command turns the grid off and the GridOn command turns the grid on. The PlotsOff command turns the plots off and the PlotsOn command turns the plots on. The AxesOff command turns the axes off and the AxesOn command turns the axes on. The FnOff command turns all of the functions off and the FnOn command turns all of the functions on.

```
Format
:GridOff/On
:PlotsOff/On
:AxesOff/On
:FnOff/On
```

The plots and functions commands can also be used to just deal with one or two plots or functions, instead of all of them. You just put the plots or functions and their numbers after the command, separating each one with a comma.

```
Format
:PlotsOff/On function#[,function#,...]
:FnOff/On function#[,function#,...]
```

To use the graph formats, you should first be in the Program editor for your program. In the Program editor, press 2nd and ZOOM. Then scroll down to GridOff/On or AxesOff/On and press ENTER. To use the PlotsOff/On or FnOff/on commands, you need to press 2nd and 0 for the Catalog menu. Then scroll down to the command or press the first letter of the command and press ENTER. Now the command has been put into your program.

### Graph Databases (GDB)

There are 10 graph database (GDB) variables (GDB0 through GDB9) that store the window and graph format settings, so they can later be used to recreate the graphscreen; GDBs do not contain graphics or stat plot definitions. If a program utilizes the graphscreen, it should restore the graphscreen settings with a GDB when the program finishes executing.

The StoreGDB command saves the graph settings in a GDB. It is best used at the beginning of a program. The RecallGDB command restores the graph settings that are stored in a GDB. It is best used after a program is finished executing. You should remember to delete the GDB after recalling it.

```
Format
:StoreGDB #
:RecallGDB #
```

To use the GDB commands, you should first be in the Program editor for your program. In the Program editor, press 2nd DRAW and > > twice. Then scroll down to StoreGDB or RecallGDB and press ENTER. Finally, press the number of the GDB you want to use.

Putting all of these commands together, here is a typical way to set up the graphscreen at the beginning of a program:

```
PROGRAM:GRAPHSET
:StoreGDB 1
:ClrDraw
:GridOff
:PlotsOff
:AxesOff
:FnOff
:0→Xmin:1→ΔX
:0→Ymin:1→ΔY
```

## Graphing Functions on the Graphscreen

Graphing functions is primarily used in math programs. There are three commands that are used for graphing functions: DrawF, DrawInv, and Tangent. The commands do not change the function variables, and their graphs (and tangent line) are erased when any command changes the graphscreen.

The DrawF command graphs an expression. The DrawInv command graphs the inverse of an expression by plotting X values on the y-axis and Y values on the x-axis (as if the X and Y values are switched). The Tangent command draws a line tangent to the expression, with the line touching the expression at the X value. Use the Input or Pause command to view the graph (or tangent line).

```
Format
:DrawF expression
:DrawInv expression
:Tangent(expression,value)
```

The expression can either be a function variable (Y0 through Y9) or a function in terms of X (such as 3X+4). While you create a function variable by storing an expression (enclosed in quotes) to it, the function in terms of X is just the expression itself (which allows you to bypass the function variable). The expression can consist of numbers, variables, and math functions.

```
Format
:"expression"→Y#
:expression
```

After the function variable is created, it is stored in the Y= editor and selected to be graphed. If you already have an expression stored in a function variable, you can combine function variables with other expressions to create new expressions. You cannot use a list in the expression to draw several graphs at one time.

When graphing functions, you have to adjust the graph formats and window dimensions to ensure the functions display correctly on the screen. Although you can have successive graphs (graphs displayed on top of each other), this is sometimes unwanted because it interrupts the graphscreen while you're graphing your functions. You can get rid of this problem by using the FnOff command.

To use the graph commands, you should first be in the Program editor for your program. In the Program editor, press 2nd and PRGM, then scroll down to whichever command you want and press ENTER. Now the command has been put into your program. You then have to type the expression you want to graph. The function variables can be found by pressing VARS, pressing > once to get to the Y-Vars menu, and then scrolling down to Functions.

## Displaying Text on the Graphscreen

The Text command displays text, numbers, variables, or expressions wherever you want on the graphscreen. Because the Text command utilizes the small font (available only on the graphscreen), more text can be displayed on the screen. The Text command overwrites any existing text on the screen, and it is also not affected by the graphscreen window settings.

When you use the Text command, you need to specify the starting coordinates of what you want to display. You first specify the row (0 to 57 from top to bottom) and then the column (0 to 91 from left to right). Although the graphscreen is actually 94 rows by 62 columns, you will get an error if you try to display text on a higher row or column.

The reason is that the graphscreen text is five pixels tall and a variable width. While numbers, uppercase letters, and most lowercase letters are three pixels wide, some lowercase letters (such as w and m) are five pixels wide, and spaces are one pixel wide. There is an automatic space (one pixel wide) inserted between text. So, you need to factor in the height and width of the characters when positioning them on the screen.

```
Format
:Text(row,col,argument)
```

A good way to find where exactly you want to place the text or other drawing is to use a blank Input command.  This gives you a cursor to find where to put it.  Just remember that the coordinates at the bottom of the screen are not what you put into the Text( command.

```
Format
:Input
```

The Text command can display multiple arguments of both text and variables on the same line, at the same time. This is very useful because it eliminates the need to have to worry about spacing. If the variable changes, the Text command will adjust it on the screen accordingly. This allows you to sometimes remove multiple Text commands and just use the first one to display everything.

```
:Text(5,5,A
:Text(5,9,"/
:Text(5,13,B
Combine Text Commands
:Text(5,5,A,"/",B
```

On the TI-83+/SE calculators, the Text command can also display the large font that is available on the homescreen. Just put a negative one (-1) before the row and column arguments. When using the large font, you have to keep formatting in mind because it is very easy for the text to go off the screen. This is useful when you want to clear large portions of the graphscreen at a time.

```
Format
:Text(-1,row,col,argument)
```

If you have a string of numbers that you are displaying, you don't need to put quotes around the numbers. You may want to keep the numbers in a string, though, if they have any leading zeros. Because the numbers are no longer in a string, the leading zeros will be truncated (taken off) and not be shown.

```
:Text(2,2,"2345
Remove the Quotes
:Text(2,2,2345
```

To use the Text command, you should first be in the Program editor for your program. In the Program editor, press 2nd and PRGM. Then, scroll down (all the way at the bottom) to Text and press ENTER. Now the Text command has been put into your program. You can then begin typing some text by turning on the alpha-lock with pressing 2nd and ALPHA.

## Drawing & Shading on the Graphscreen

Drawing on the graphscreen is one of the main uses of the graphscreen. There are several different things that you can draw, including points, pixels, lines, and circles. Besides drawing, you can also shade in an area on the graphscreen with whatever size and look you want.

### Drawing Points

The point commands are used to draw points on the graphscreen. A point is just a pixel on the screen. The point commands use the (x,y) coordinate system, which is affected by the window settings. This means you have to change the window settings accordingly when you use the point commands, otherwise the points won't show up correctly.

The Pt-On command turns on the point at the given (x,y) coordinates. The Pt-Off command turns off the point at the given (x,y) coordinates. The Pt-Change command toggles the point at the given (x,y) coordinates. If the point is on, it will be turned off and vice versa.

```
Format
:Pt-On(x,y)
:Pt-Off(x,y)
:Pt-Change(x,y)
```

The Pt-On and Pt-Off commands also have an optional mark argument that determines the shape of the point. The mark can be either one (dot), two (3x3 box), or three (3x3 cross). You don't need to specify the mark when using the first mark because it is the default. Remember to use the same mark when turning a point off as you used to turn it on.

```
:Pt-On(5,5,1
Remove Mark
:Pt-On(5,5
```

To use the point commands, you should first be in the Program editor for your program. In the Program editor, press 2nd and PRGM, then press right once and scroll down to whichever command you want and press ENTER. Now the command has been put into your program. You then have to type the numbers for where you want the point to appear on the screen.

### Drawing Pixels

The pixel commands are the alternative way to draw pixels on the graphscreen. Although they are easier to use because they are not affected by the window settings (which means you don't have to set the window dimensions when using them), the coordinate system is switched around so that the row comes first and then the column — it's (y,x) instead of (x,y).

The Pxl-On command turns on the pixel at the given (y,x) coordinates. The Pxl-Off command turns off the pixel at the given (y,x) coordinates. The Pxl-Change command toggles the pixel at the given (y,x) coordinates. If the pixel is on, it will be turned off and vice versa. The pixel commands are faster than their equivalent point commands, so they should generally be used instead whenever possible.

```
Format
:Pxl-On(y,x)
:Pxl-Off(y,x)
:Pxl-Change(y,x)
```

Besides these three commands that have point equivalents, there is also a Pxl-Test command. The Pxl-Test command checks whether the pixel at the given (y,x) coordinates is on or off. One is returned if the pixel is on and zero is returned if the pixel is off. You can store the result to a variable for later use, or use the command in a conditional or loop.

```
Format
:Pxl-Test(y,x)
```

To use the pixel commands, you should first be in the Program editor for your program. In the Program editor, press 2nd and PRGM, then press right once and scroll down to whichever command you want and press ENTER. Now the command has been put into your program. You then have to type the numbers for where you want the pixel to appear on the screen.

### Drawing Lines

The Line comand allows you to draw a line anywhere on the screen. The line can be any length that you want. When using the Line command you need to supply the coordinates of the two endpoints. The Line command draws the line from the first endpoint (x1,y1) to the second endpoint (x2,y2).

```
Format
:Line(x1,y1,x2,y2)
```

The Line command has an optional fifth argument that controls whether the line will be drawn (the argument should be one) or erased (the argument should be zero). The line is drawn by default, so it should be left off unless you want to erase it.

```
:Line(5,5,10,5,1
Remove Line's Fifth Argument
:Line(5,5,10,5
```

When you have multiple pixels in a straight line that you turn on or off, you can sometimes replace the pixel commands with one or more Line commands. In the case that the pixels are arranged at a slant or angle, you can just adjust the line coordinates accordingly. You should also use Line commands instead of pixel commands when clearing large portions of the graphscreen at a time.

```
:Pxl-On(5,5
:Pxl-On(5,6
:Pxl-On(5,7
Replace with Lines
:Line(5,5,5,7
```

There are two other line commands that are also available. They are primarily designed for when you want to quickly draw a line across the entire screen. The Horizontal command draws a horizontal line at a given row and the Vertical command draws a vertical line at a given column. The argument can either be a number or a variable.

```
Format
:Horizontal y
:Vertical x
```

To use the line commands, you should first be in the Program editor for your program. In the Program editor, press 2nd and PRGM, then scroll down to whichever command you want and press ENTER. Now the command has been put into your program. You then have to type the number(s) for where you want the line to appear on the screen.

### Drawing Circles

The Circle command draws a circle on the graphscreen. When using the Circle command, you must enter three numbers (separated by commas): the (x,y) coordinates of the center of the circle and the length of the radius. Because circles take a long time to draw, you should use them sparingly.

```
Format
:Circle(x,y,radius)
```

The window settings affect how the circles are drawn. With the screen height being larger than the width (the screen is a rectangle), the circles will actually look like ellipses. To make them look like circles, you need to use the ZSquare command.

To use the Circle command, you should first be in the Program editor for your program. In the Program editor, press 2nd and PRGM, then scroll down to Circle and press ENTER. Now the Circle command has been put into your program. You then have to type the numbers for where you want the center of the circle to be and the length of the radius.

### Shading Areas

The Shade command shades in an area on the graphscreen. For basic shading, you just need to specify a lower function and upper function. The Shade command will vertically shade in the area that is above the lower function and below the upper function across the whole length of the screen. The functions can either be a function variable (Y0 through Y9); or a function in terms of X, consisting of numbers, variables, and math functions (such as 3X+4).

```
Format
:Shade(lowerfunction,upperfunction)
```

When shading with the function variables, the window settings affect how the shading looks. You should set the window variables to ensure that the shading is done correctly. This also applies when you are shading at the same time as drawing, because some of the drawing commands are affected by the window settings.

Because you might not want to shade the whole length of the screen, the Shade command has two optional arguments that allow you to specify the left and right boundaries for shading (the boundaries themselves are also shaded). Xleft and Xright can be whatever numbers you want, as long as they are between Xmin and Xmax (the horizontal window dimensions). You can also just specify Xleft by itself if you only want to change the left boundary (you need to set Xleft to set Xright, though).

```
Format
:Shade(lowerfunction,upperfunction,Xleft,Xright)
```

The Shade command has two other optional arguments that allow you to change the look of the shading, but you need to also set the left and right boundaries to use them. The pattern can be either one (vertical), two (horizontal), three (slanted backwards), or four (slanted forwards); and the patres (the frequency of the shading) can be from one to eight pixels.

```
Format
:Shade(lowerfunction,upperfunction,Xleft,Xright,pattern,patres)
```

To use the Shade command, you should first be in the Program editor for your program. In the Program editor, press 2nd and PRGM, then scroll down to the command (or press the 7 key) and press ENTER. Now the command has been put into your program. You then have to specify the functions (and boundaries, pattern, and patres) for how you want to shade the area.

## Storing the Graphscreen to a Picture

After you have spent lots of time drawing something on the graphscreen, you naturally want to keep it for future use. So, you store it to a picture variable. A picture variable holds a copy of the graphscreen at the respective time it was stored to. Although pictures are often used, it really is a personal preference.

The StorePic command saves the current graphscreen to the designated picture. After saving a picture, you can display it again with the RecallPic command. Before recalling a picture, you should first make sure that the graphscreen is clear. This ensures that the picture won't be interrupted by anything that is already on the screen. You can only use numbers with the StorePic and RecallPic commands; no variables.

```
Format
:StorePic #
:RecallPic #
```

Because each picture takes up 768 bytes, you should delete them when exiting programs. The program should only keep the picture if it is used for something important (such as a titlescreen). The user doesn't want to have their memory cluttered up with lots of variables.

To use the picture commands, you should first be in the Program editor for your program. In the Program editor, press 2nd DRAW and < once. Then scroll down to StorePic or RecallPic and press ENTER. Finally, press the number of the picture you want to use.

### Advantages & Disadvantages of Pictures

The main advantage of using pictures is that the graphics show up almost instantly compared to the slow speed of drawing them. This is particularly noticeable the more detailed the graphics are and depending on what graphics (primarily circles) are being drawn. Speed is a top priority in most programs (because the user doesn't want to wait), so pictures are usually used.

The main disadvantage of using pictures is that there are only ten pictures (from Pic0 to Pic9). With every program sharing the pictures, there can be conflict when two programs use the same picture (the picture will usually be overwritten by the other program).

Another disadvantage of using pictures is that it is another file that the user needs in order to use your program. If you give someone your program, you will have to also give them your pictures. Your program won't work properly anymore if somebody deletes your pictures or forgets to include them with your program. Although this is mostly out of your hands, users will think your program is at fault.

Pictures have a weird behavior, that can be a curse or blessing.  When recalled, they only turn on pixels — not turn them off.  Try recalling one picture, then recalling a different picture.  You'll notice they overlap. This has an application anytime that you are displaying something (sprite) on top of a background.  Draw the sprite on the screen, and use a pic for the background.
