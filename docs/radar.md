# Radar Animation
|Routine Summary|Inputs|Outputs|Variables Used|Author|Download|
|--- |--- |--- |--- |--- |--- |
|Displays a radar animation.|None|None|X, Y, S, T|X1011|[file radar.zip]|

```
:ZStandard
:ZInteger
:For(X,-31,31
:Horizontal X
:End
:DelVar X31→Y
:Repeat getKey
:X→S:Y→T
:X+.1Ans→X
:Y-.1Ans→Y
:Line(0,0,X,Y,0
:Line(0,0,S,T
:End
```

In order to display the radar animation on the screen, we first need to create a [friendly graphing window](friendly-window.html), setting the graph screen dimensions to X=-47...47 and Y=-31...31. We then make the entire screen black by drawing [Horizontal](horizontal.html) lines from the bottom of the screen to the top.

Once the screen is setup, we initialize our two variables for the coordinates of the radar lines, and start drawing the radar animation on the screen. We store the two coordinates to two temporary variables, and then update the original variables to move the radar lines over a pixel. We then erase the old radar line from before, and draw the new radar line.

This gets repeated over and over again, until you press a key to quit. If you want the animation to last for a certain amount of time, you can replace the [Repeat](repeat.html) loop with a [For(](for.html) loop. In addition, you can use Shade(Ymin,Ymax instead of the For( loop at the beginning to shade the screen. This is smaller, although it isn't necessarily any faster.
