# Pong
Pong is a classic program for beginner programs to start out with, so we thought it was important to include it. The basic premise behind pong is you have to keep the ball ("O") in play by bouncing it back and forth against the walls, without letting it get by your paddle ("["). You can play this game indefinitely, but it does get monotonous after a while.


## The Code

```
:3→A:4→X
:1→S:1→T
:randInt(1,8→Y
:Repeat K=45 or X=1 and A≠Y
:ClrHome
:Output(A,1,"[
:Output(Y,X,"O
:getKey→K
:max(1,min(8,A+(Ans=34)-(Ans=25→A
:T(Y>1 and Y<8)+(Y=1)-(Y=8→T
:S(X>1 and X<16)+(X=1)-(X=16→S
:X+Ans→X:Y+T→Y
:End
:Pause "Game Over!
:ClrHome:"
```

## The Download

In case you want to try the program on your calculator, you can download the program in .8xp format.

- [Pong](http://tibasicdev.github.io/local--files/pong/pong.zip)
