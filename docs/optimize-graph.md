# Optimization: The Graph Screen
Although the screen is 95 pixels wide and 63 pixels tall, the bottom row and far right column of pixels are unusable. So, most people set the graphscreen dimensions to 94 and 62. This itself should be replaced with storing 1 into deltaX and deltaY.

```
:0→Xmin:94→Xmax
:0→Ymin:62→Ymax
can be
:0→Xmin:1→ΔX
:0→Ymin:1→ΔY
can be even better
:ZStandard
:84→Xmin
:72→Ymax
:ZInteger
```

The Text command can display both variables and text at the same time on the same line. This allows you to sometimes remove multiple Text commands and just use the first one.

```
:Text(5,5,A
:Text(5,9,"/
:Text(5,13,B
can be
:Text(5,5,A,"/",B
```

The Pxl-On command is faster than Pt-On, and it should be used whenever possible. Pt-On is also affected by the screen dimensions, while Pxl-On is not.

```
:Pt-On(5,5
can be
:Pxl-On(5,5
```

The Line command has an optional fifth argument that controls whether the line will be drawn (the argument should be one) or erased (the argument should be zero). The default is one, and it should be left off when possible.

```
:Line(5,5,10,5,1
can be
:Line(5,5,10,5
```

When turning multiple pixels in a straight line on or off, use a For loop instead of using the individual pixel commands.

```
:Pxl-On(5,5
:Pxl-On(5,6
:Pxl-On(5,7
:Pxl-On(5,8
can be
:For(X,5,8
:Pxl-On(5,X
:End
```

When you are changing the same pixels from on to off or vice versa in a loop, use the Pxl-Change command instead of the individual pixel commands.

```
:For(X,5,8
:Pxl-On(5,X
:End
:For(X,5,8
:Pxl-Off(5,X
:End
can be
:For(N,1,2
:For(X,5,8
:Pxl-Change(5,X
:End
:End
```

When you have multiple pixels in a straight line that you turn on or off, you can sometimes replace the Pxl-On commands with Line commands.

```
:Pxl-On(5,5
:Pxl-On(5,6
:Pxl-On(5,7
:Pxl-On(5,8
can be
:Line(5,5,5,8
```

The Pt-On and Pt-Off commands have an optional third argument that should never be used when one is desired because one is the default.

```
:Pt-On(5,5,1
can be
:Pt-On(5,5
```

The optional third argument for Pt-On and Pt-Off should be used when you want to turn on or off a 3x3 outline of a box (the argument should be two) or a 3x3 cross (the argument should be three). This can be used instead of the individual commands. 	

```
:Pt-On(A,B-1
:Pt-On(A,B
:Pt-On(A,B+1
:Pt-On(A-1,B
:Pt-On(A+1,B
can be
:Pt-On(A,B,3
```

When wanting to clear large spaces of the graph screen, you should use the Line or Text commands instead of the pixel commands, when possible. Both of these commands are faster than the pixel commands.

```
:Pxl-Off(5,5
:Pxl-Off(5,6
:Pxl-Off(5,7
:Pxl-Off(5,8
can be
:Line(5,5,5,8,0
```

The Circle( command has an alternate syntax. When a complex list such as {*i*} is added as the 4th argument, "fast circle" mode will be turned on, which uses the symmetries of a circle to save on trig calculations, and draws a circle in only 30% of the time it would normally take. Since the Circle( command is speed-challenged at best, you should always use this optimization when drawing circles.
```
:Circle(0,0,5
can be
:Circle(0,0,5,{i
```


<center>

|**[<< Loops](sk:loops-optimize.html)**|**[Table of Contents](starter-kit.html)**|**[Summary >>](sk:optimize-summary.html)**|
| --- | --- | --- |

</center>
