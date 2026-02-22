# Graph Settings
|This article is currently in development. You can help TI-Basic Developer by expanding it. |
| --- |

You already know the Graph Screen is 95 pixels wide and 63 pixels high. You may want to change these settings a little bit. The dimensions of the window will directly affect all your commands in the Draw menu except for the [Pxl-On(](pxl-on.html), [Pxl-Off(](pxl-off.html) and the [Text(](text.html) commands.


### Window

You can change the size of the Graph Screen. This is very useful when dealing with [Pt-On(](pt-on.html) or [Pt-Off(](pt-off.html) because you need to have a window that contains the coordinate you're using in Pt-On( and Pt-Off(. If the user already has a screen set to [ZStandard](zstandard.html) and you write Pt-On(30,45) it won't work. 

So, you can change Xmin, Xmax, Ymin or Ymax. They can be found by pressing Vars then 1:Window
```
:#→Xmin:#→Xmax
:#→Ymin:#→Ymax
```

Or you can change the zoom: [ZStandard](zstandard.html) , [ZInteger](zinteger.html). They can be found in the Zoom menu near the "Y=" key

```
:ZStandard
```
or
```
:ZInteger
```


### Functions

You may want to turn off functions. The user may accidentally write Y=2X in his "Y=" window before using your program. To turn off all functions, simply use: [FnOff](fnoff.html) (using the Vars menu, click right to go in Y-Vars then in 4:On/Off.)

To have them back on: [FnOn](fnon.html)
**When you turn the functions on, they'll draw in the screen so you may want to use this code wisely.

### Axes

Another thing that may be annoying when you create a program and you use the Graph Screen is axes. You can turn them off by using [AxesOff](axesoff.html) and [AxesOn](axeson.html) to have them back. These can be found by pressing 2nd function then Format

### Resetting

When creating a program, you don't want the user to manually get back his settings. For this, you can simply but all back on at the end of the program.

With this you can have all these settings back. To use the ClrDraw, go in 2nd, Draw then 1:ClrDraw
```
:ZStandard:AxesOn:FnOn:ClrDraw
```

### Example

You can also input these variables and let the user choose the size of the screen:

```
:Input "Left: ",Xmin
:Input "Right: ",Xmax
:Input "Bottom: ",Ymin
:Input "Top: ",Ymax
:Input "Axes On ?[y,n]",Str1
:If Str1="Y"
:AxesOn
:If Str1="N"
:AxesOff
```


<center>

|**[<< Drawing Points and Pixels](sk:points.html)**|**[Table of Contents](starter-kit.html)**|**[Drawing More Shapes >>](sk:more-shapes.html)**|
| --- | --- | --- |

</center>
