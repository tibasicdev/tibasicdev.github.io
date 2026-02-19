# Introduction to the Graph Screen
This is where most of the magic happens, be it for math class or a game. While much can be accomplished on the Home Screen, it's nowhere near as versatile as the Graph Screen.


## Introduction

The most useful aspect of the Graph Screen is the variety of ways to create graphics. There are 95x63 adjustable pixels that can be modified with any of the Pxl-, Pt- or more specialized draw commands as well as a twist on Text. Unlike on the Home Screen where your coordinates are restricted to integers from 1-8 and 1-16, different window settings can be used to customize the coordinates of each point. You can switch points between 'on' and 'off', or just check to see if a point is 'on' (great for collision detection!).  
(NOTE: The TI-84+ CSE and CE have a bigger screen, so the pixel dimensions are 320x240. However, the adjustable pixels are 264x164 (X by Y). Keep those last dimensions in mind when you program for either the CSE or CE calculators.)

## Pictures

Pictures include anything that can be created on the Graph Screen from the Draw menu, but not any functions or graphs.

### StorePic

[StorePic](storepic.html) allows you to save the current picture from the Graph Screen and can be accessed from the STO sub-menu
by pressing [2nd][Draw][Left][Enter]. This can be useful if you have a frequently used picture or a background that you don't want to have to continuously redraw. Within TI-Basic there are 10 picture variables, which are numbered 0 through 9.
For example, if you wanted to store the current picture to Pic1 you would do:
```:StorePic 1
```

### RecallPic

[RecallPic](recallpic.html) is used to display a previously saved picture. It can also be found in the STO sub-menu. The one thing to remember when using this command is that it will draw the picture on top of what is already on the Graph Screen instead of completely replacing it. This means that it will turn on any pixels that are on in the picture, but will not turn off pixels that are off in the picture. An easy way to circumvent this is to use [ClrDraw](clrdraw.html) before recalling the picture.
If you wanted to display Pic1 you would do:
```:RecallPic 1
```

## Graph Databases

A Graph Database contains the window and format settings, functions, and the settings of FUNC/PAR/POL/SEQ, CONNECTED/DOT, and SEQUENTIAL/SIMUL from the Mode menu.

### StoreGDB

Just like with StorePic, StoreGDB is used to store the current graph database settings. It can be found in the STO sub-menu. There are 10 GDB variables, which are numbered 0-9.
To store to GDB1 you would use:
```:StoreGDB 1
```

### RecallGDB

Incredibly, [RecallGDB](recallgdb.html) is used to recall a saved graph database! Luckily this does not have the problem of RecallPic. If one setting has a value that's not the same as the saved value, then it's changed to the saved value.
To recall GDB1 you would use:
```:RecallGDB 1
```

## Things To Come

In the following sections of this chapter you'll learn different ways to manipulate pixels, how to use the various draw commands and the effects that 'simple' text can have in order to create truly awesome games!

<center>

|**[<< Sample Program: Chase the Star](sk:chase-the-star.html)**|**[Table of Contents](starter-kit.html)**|**[Drawing Points and Pixels >>](sk:points.html)**|
| --- | --- | --- |

</center>
