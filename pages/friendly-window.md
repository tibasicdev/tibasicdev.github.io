# Friendly Graphing Window
A friendly graphing window is some configuration of [window variables](system-variables.html#window) that's most useful for your program — most commonly, because it makes the coordinate value of a pixel come out to a round value, such as an integer, or .1 of an integer.

## Setting up a square window

The most basic type of friendly window is one in which a vertical distance in pixels is equal, coordinate-wise, to the same horizontal distance in pixels. This means that the ratio between (Xmax-Xmin) and (Ymax-Ymin) is 47:31. Such a setup has the useful effect that drawing a circle (for example, with the [Circle(](circle.html) command) actually results in a circle, and not an ellipse. 

This can be accomplished simply with the [ZSquare](zsquare.html) command, which will alter the values of the screen so that:

- the coordinate of the center remains the same
- the ratio (Xmax-Xmin) : (Ymax-Ymin) is 47:31 (approximately 1.516 : 1)
- the resulting window is larger rather than smaller than the original.

A common technique is to run the [ZStandard](zstandard.html) command first, so that the center of the screen is at (0,0).

## Setting up an integer square window

However, it's possible to take friendliness even further, by adding the condition that coordinate values of a pixel come out to round values without long decimals. This can be done in several ways:

#### Using the ZDecimal command

This is by far the simplest — the [ZDecimal](zdecimal.html) command will set Xmin to -4.7, Xmax to 4.7, Ymin to -3.1, and Ymax to 3.1. As you can see, this satisfies the condition for a square window. Also, the coordinates of pixels have at most one decimal place: pixels that are next to each other differ by 0.1 in the appropriate coordinate.

Zdecimal is useful if you only need to do a few point/line commands, like if you were drawing a border around the screen using Horizontal and Vertical.

However, it has the drawback of still having a decimal point. Your drawing commands may look like Line(-3.1, -1.7, 3.1, -1.7) — if you didn't have to have that decimal point there, you'd save a considerable amount of space. This is possible, using the following three methods:

+++++ An integer window with (0,0) in the center

These methods are basically divided over where the point (0,0) should be. Putting it in the center ensures that drawing things in the middle of the screen takes up little space; also, you can achieve symmetry easily by appropriately negating numbers. On the other hand, the negative sign (you'll be using one 3/4 of the time, and 1/4 of the time you'll need two) can be annoying.

The following code sets up an integer square window with (0,0) in the center:

```
:ZStandard
:ZInteger
```

+++++ An integer window with (0,0) in the bottom left corner

This approach is optimal in terms of saving space on coordinates: they are all positive numbers with at most two digits. For this reason, it is the most widely used. The following code sets up such a window:

```
:ZStandard
:84→Xmin
:72→Ymax
:ZInteger
```

+++++ An integer window with (0,0) in the top left corner

This approach is useful for when point and pixel commands need to be used together. Although putting (0,0) in the top left makes every Y-coordinate negative, the window has the useful property that it's very easy to go from point commands to pixel commands: the pixel (R,C) corresponds to the point (C,-R), and equivalently, the point (X,Y) corresponds to the pixel (-Y,X). It's somewhat trickier to set up, though:

```
:ZStandard
:84→Xmin
:-72→Ymin
:ZInteger
```

## Why friendly windows are useful

Throughout this article, we've only made glancing comments as to why you'd want to use friendly windows. Here is a more exhaustive explanation:

#### Graphs come out nicer

Even with a square window, graphs become more accurate, because they reflect the actual proportions of the equation being graphed. For example, try drawing a circle in the standard graphing window — you'll get some stretched out oval. Now [ZSquare](zsquare.html) and try again. The result is much better, right?

With an integer square window, certain other imperfections of the calculator's graphing go away. For example, try graphing Y=1/(X+1) in the standard graphing window. Pretty accurate, but instead of the asymptote there's a slightly diagonal line. That's because the asymptote doesn't end up corresponding to a pixel of the graph: one pixel, the curve is a very negative number, the next it's a very positive number, so the calculator tries to connect them.

Now [ZDecimal](zdecimal.html) and graph 1/(X+1) again. The nearly vertical line at the asymptote disappears: because the value X=-1 matches a pixel on the graph, so the calculator realizes that something is undefined there.

Another similar problem occurs with graphing Y={-1,1}√(9-X²). In most graphing windows, this graph, which should come out to a circle, has some gaps near the sides. In an integer square window, such as with [ZDecimal](zdecimal.html), the gaps disappear, and you're left with a perfect circle.

#### Coordinates are round numbers

This is a more programming-related application. If you happen to need to draw something on the screen, in a program, you're likely to need a lot of [Line(](line.html) or [Pt-On(](pt-on.html) commands at fairly specific locations. On a normal window, such a "specific location" might end up being (2.553,0.645) or something equally ugly, with unpredictable results if you try to round it to the nearest nice value (since you don't know exactly the point at which pixels change).

With a friendly window (for this purpose, an integer window with (0,0) in the bottom left is the friendliest), every single pixel has a round coordinate value. If each value is no more than a 2-digit number, you can even [compress](compression.html) all the coordinates of a line into a single number — this technique was used, for example, in Bryan Thomas' [Contra](contra.html) game.

#### Point and pixel commands are compatible

In the case of an arbitrary window, it's fairly difficult to convert from a pixel coordinate to a point coordinate and back: the exact formula is X=Xmin+CΔX, Y=Ymax-RΔY if (X,Y) is the point and (R,C) is the pixel (going from pixel to point is even more painful). However, there are many cases in which you do need to go back and forth — for example, if you need to draw both text and lines at a coordinate. With friendly windows, this formula becomes much simpler — such as (X,Y)=(C,-R) for the last integer window we discussed.
