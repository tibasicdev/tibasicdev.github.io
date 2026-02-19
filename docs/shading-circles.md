# Shading Circles
|Routine Summary|Inputs|Outputs|Variables Used|Author|Download|
|--- |--- |--- |--- |--- |--- |
|Shades in a circle.|*R* - the radius of the circle<br>*A* - the X coordinate of the circle's center<br>*B* - the Y coordinate of the circle's center|None|N, R, A, B|Jutt|[file shadecircles.zip]|

```
:For(N,0,R,ΔX
:√(R²-N²
:Line(A+N,B-Ans,A+N,B+Ans
:Line(A-N,B-Ans,A-N,B+Ans
:End
```

Although it is possible to shade in a circle using the [Shade(](shade.html) command (i.e., Shade(-√(R²-(X-A)²)+B,√(R²-(X-A)²)+B)), that is actually quite impractical in a real program because of its slow speed. Fortunately, you can improve upon that by using your own routine.

When graphing a circle, there are a few main things you need to know: the radius and the (X,Y) coordinates of the center. In our routine, the R variable is the radius, the A variable is the circle's X coordinate and the B variable is the circle's Y coordinate.

Rather than displaying the circle as one big circle, we are going to display it line by line using a [For(](for.html) loop, starting from the center. The √(R²-N² formula is based on the circle formula R<sup>2</sup>=(X–H)<sup>2</sup>+(Y–K)<sup>2</sup>, with the formula rearranged to get the respective part of the circle.

The circle should display pretty quickly, but it all depends on the values that you chose for the variables; smaller values will be faster, and likewise larger values will be slower. In addition, the circle may not display correctly if you don't have the right graph settings, so you should set your calculator to a [friendly graphing window](friendly-window.html).
