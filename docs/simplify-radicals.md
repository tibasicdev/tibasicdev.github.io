# Simplify Radicals
|Routine Summary|Inputs|Outputs|Variables Used|Author|Download|
|--- |--- |--- |--- |--- |--- |
|Simplifies a square root radical.|*X* - the radical to simplify|*A* - the square factors of the radicand<br>*B* - the remaining radicand|X, A, B, I|DarkerLine|[file simplifyradicals.zip]|

```
:X→B:1→A:2→I
:While I²≤B
:While not(fPart(B/I²
:B/I²→B
:AI→A
:End
:I+1+(I>2→I
:End
```

[Simplifying radicals](http://www.themathpage.com/alg/simplify-radicals.htm) involves finding the square factors that exist in the radicand (the number under the radical), and then moving them outside to the front of the radical. For example, if you have √48, you can reduce this to √(4*4*3, and 4 is a square factor of 2, so the finished simplified radical would be 4√3.

Our routine follows this same process when simplifying a radical. We start with setting A to 1 and B to X (so √(X) is written as 1√(X)). Then we go through every value I whose square could possibly divide B. If we find such a value, we divide B by its square, and multiply A by the value, taking it out of the square root. We know we're done when the value I² is bigger than B, so I² couldn't possibly divide B.

The finished radical will thus be A√(B). We have chosen not to display it on the screen, and instead leave it up to you how it gets displayed and used.
