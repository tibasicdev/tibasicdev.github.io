# Maze Walkthrough
The basic premise behind Maze Walkthrough is you have to make your way through the maze without touching any of the walls. This game is rather simple at its core, but it does feature a randomly generated maze each time, so it can be played indefinitely. It also is extremely compact, a good example of what you can do in a small number of bytes.



### The Code

```
:ClrHome
:ClrDraw
:AxesOff
:ZStandard
:Vertical Xmin
:Horizontal Xmin
:Horizontal Xmax
:For(X,‾9,10
:randInt(‾8,8
:Line(X,Xmax,X,Ans
:Line(X,Xmin,X,Ans-2
:End
:3→X:3→Y:E3→S
:Repeat K=45 or X=94 or pxl-Test(Y,X
:Pxl-On(Y,X
:Repeat Ans
:getKey→K
:End
:Pxl-Off(Y,X
:S-1→S
:X+(K=26)-(K=24→X
:Y+(K=34)-(K=25→Y
:End
:ClrDraw
:Text(15,15,"You "+sub("Lose!Win! ",1+5(X=94),5
:Text(22,15,"Score: ",S
:Pause
:ClrDraw
:ClrHome:"
```

### The Download

In case you want to try the program on your calculator, you can download the program in .8xp format.

- [Maze Walkthrough](http://tibasicdev.github.io/local--files/maze-walkthrough/mazewalkthrough.zip)
