# Sierpinski Triangle
|Routine Summary|Inputs|Outputs|Variables Used|Author|Download|
|--- |--- |--- |--- |--- |--- |
|Displays the Sierpinski Triangle.|None|None|L₁, L₂, A, B, C|Weregoose|[file sierpinski.zip]|

```
:ClrDraw
:0→Xmin:2→Xmax
:0→Ymin:1→Ymax
:rand→A:rand→B
:{0,1,2→L₁
:{0,1,0→L₂
:Repeat getKey
:randInt(1,3→C
:mean({A,L₁(C→A
:mean({B,L₂(C→B
:Pt-On(A,B
:End
```

A [Sierpinski triangle](https://en.wikipedia.org/wiki/sierpinski_triangle) is a very common fractal that almost everybody has seen. It consists of a large triangle divided into three smaller triangles, which are then themselves divided into three smaller triangles, and this is repeated infinitely until the triangles are so small you can barely see them.

In order to construct a Sierpinski triangle on the calculator, you need to use the graph screen. Before we can use the graph screen, however, we need to perform some basic [setup](setup.html). We then create our [variables](variables.html): two lists (one for the X coordinates and one for the Y coordinates) and two numerics (one for a random X number and one for a random Y number).

Once we have our variables created, we start randomly coming up with places to display the pixels that will make up the triangle. Based on the formula used to generate the triangle, we take the average of the random list values and the random numbers that were generated, and use those for the coordinates of the next pixel. This gets repeated over and over again until either the triangle is completed or you press a key.
