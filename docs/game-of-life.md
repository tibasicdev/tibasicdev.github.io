# Conway's Game of Life
|Routine Summary|Inputs|Outputs|Variables Used|Author|Download|
|--- |--- |--- |--- |--- |--- |
|Displays Conway's Game of Life on the screen.|*∟X* - the list of X coordinates<br>*∟Y* - the list of Y coordinates|None|∟X, ∟Y, ∟P, ∟Q, S, X, Y|DarkerLine|[file gameoflife.zip]|

```
:Plot1(Scatter,X,Y,.
:∟X→P:∟Y→Q
:Repeat getKey or S<2
:∟P→X:∟Q→Y
:DispGraph
:DelVar ∟PDelVar∟Q1→S
:For(X,min(∟X)-1,1+max(∟X
:For(Y,min(∟Y)-1,1+max(∟Y
:sum(1=max(abs(∟X-X),abs(∟Y-Y
:3=Ans or 3=Ans+max(∟X=X and ∟Y=Y
:If Ans:Then
:X→∟P(S
:Y→∟Q(S
:S+1→S
:End:End
:End:End
:PlotsOff
:ClrHome:"
```

[Conway's Game of Life](https://en.wikipedia.org/wiki/conway_game_of_life) is a game designed to model how a simple environment evolves over time. Although it is called a game, it is not really a game, since it has no players and it operates on its own. The basic functionality involves moving pieces around the screen, with a black pixel being considered alive and a white pixel being considered dead.

A piece can move in any of the eight directions, and the basic rules it follows are: a pixel stays alive if it has two or three live neighboring pixels, and a dead pixel becomes alive if it has exactly three live neighboring pixels. The different patterns and shapes that emerge all depend on the pieces that you start out with.

In order to setup the pieces, we need to store the X and Y coordinates in the respective ∟X and ∟Y lists. There are a couple things you need to remember: the screen is 94x62, so those are the maximum numbers you can use for coordinates; there needs to be a corresponding Y coordinate for every X coordinate, otherwise you will get a [ERR:DIM MISMATCH](errors.html#dimmismatch) error.

We use a [stat plot](plotn.html) for displaying the pieces because it has built-in functionality for working with [lists](lists.html), and storing the pieces in lists is more efficient than any of the other alternatives available. In addition to the two main coordinate lists, we also create two other temporary lists (∟P and ∟Q).

These two lists are used for storing all of the different movements by the pieces. When we have finished checking all of the pieces to see if any of them should be moved (based on the game rules), we update the coordinates lists, and store the new coordinates of the pieces to the ∟X and ∟Y lists. We repeat this over and over again for the life of the game.

Displaying and checking the pieces should take only a few seconds, but it all depends on the number of pieces that you choose to use; fewer pieces will be faster, and likewise more pieces will be slower. When you are done using ∟X, ∟Y, ∟P, and ∟Q, you should [clean them up](cleanup.html) at the end of your program.
