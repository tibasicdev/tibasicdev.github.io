# Chase
Chase is a simple game where the goal is to chase down the randomly moving target. To make the game more difficult, the old locations of the target are not erased, which makes the target harder to find. This game is small in size and just uses a few real variables. Like with the other games, try out the game and try to understand and think through the code.



### The Code

```
:1→A:1→B
:8→C:16→D
:ClrHome
:Repeat A=C and B=Ans
:getKey→K
:If Ans=22:Stop
:If Ans:Output(A,B,"  // 1 space
:A+(Ans=34)-(Ans=25
:Ans+8(not(Ans)-(Ans=9→A
:B+(K=26)-(K=24
:Ans+16(not(Ans)-(Ans=17→B
:Output(A,Ans,"X
:Output(C,D,"+
:C+randInt(-1,1
:Ans+8(not(Ans)-(Ans=9→C
:D+randInt(-1,1
:Ans+16(not(Ans)-(Ans=17→D
:End
:Pause "FOUND IT!
:ClrHome:"
```

### The Download

In case you want to try the program on your calculator, you can download the program in .8xp format.

- [Chase](http://tibasicdev.github.io/local--files/chase/chase.zip)

### Option 2
This is a version where the old locations of the target are erased, making the target easier to chase down -(code edited by Aleksei Gentry)

```
:1→A:1→B
:8→C:16→D
:ClrHome
:Repeat A=C and B=Ans
:getKey→K
:If Ans=22:Stop
:If Ans:Output(A,B,"  // 1 space
:Ans:Output(C,D,"+
:A+(Ans=34)-(Ans=25
:Ans+8(not(Ans)-(Ans=9→A
:B+(K=26)-(K=24
:Ans+16(not(Ans)-(Ans=17→B
:Output(A,Ans,"X
:Output(C,D,"  // 1 space
:C+randInt(-1,1
:Ans+8(not(Ans)-(Ans=9→C
:D+randInt(-1,1
:Ans+16(not(Ans)-(Ans=17→D
:End
:Pause "FOUND IT!
:ClrHome:"
```
