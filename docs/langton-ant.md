# Langton's Ant
|Routine Summary|Inputs|Outputs|Variables Used|Author|Download|
|--- |--- |--- |--- |--- |--- |
|Simulates Langton's ant on the screen.|None|None|A, B, C|Arcane Wizard|[file langtonant.zip]|

```
:ClrDraw
:31→A:47→B
:randInt(1,4→C
:Repeat getKey
:C-1+2pxl-Test(A,B
:Ans+4((Ans<1)-(Ans>4→C
:Pxl-Change(A,B
:B+(Ans=2)-(Ans=4→B
:A+(C=3)-(C=1→A
:End
```

[Langton's ant](https://en.wikipedia.org/wiki/langton_ant) is a simulation of the movement of an ant, with some simple rules governing it: the ant can move in any of the four cardinal directions, but whenever it goes over one of the previous spots that it was at, it will change direction 90°. Although the ant movement appears chaotic, given enough time it actually ends up being a pattern.

In our routine, the ant is going to be a simple pixel. Before we can display the ant on the screen, however, we need to clear it and initialize its starting position. (47,31) was chosen because it is the exact center of the screen, which should provide the ant with ample room to move around.

We then randomly select a starting direction for the ant to go — 1 for down, 2 for right, 3 for up, and 4 for left. Once we have a direction selected, we display the ant and it will start moving around. The ant will keep moving around indefinitely until you press a key, although you could limit it to a set number of moves by replacing the [Repeat](repeat.html) loop with a [For(](for.html) loop.
