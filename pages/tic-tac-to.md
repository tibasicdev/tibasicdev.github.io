# Tic Tac To
Tic Tac To is a game that almost everybody has played at one point in their life, no matter who they are. The simple premise behind the game is to alternate turns placing pieces on the 3x3 game board until somebody gets 3-in-a-row or all nine spots on the game board are filled. This game best lends itself to a matrix variable, so that is what we decided to use for the game board. Of course, you can also use a list or string. Again, try out the game and try to understand and think through the code.



### The Code

```
:0→A
:0identity(3→[A]
:1-2int(2rand→B
:"+++
:ClrHome
:Disp Ans,Ans,Ans
:Repeat 0
:Repeat Ans
:.1getKey→K
:End
:If 2Ans=9
:Goto Q
:iPart(Ans)-6→C
:10fPart(K)-1
:If max(2≤abs({C,Ans}-2
:End
:If [A](C,Ans
:End
:Output(C,Ans,sub("X O",B+2,1
:B→[A](C,Ans
:For(C,0,1
:[A]T→[A]
:For(D,1,3
:Matr►list([A],D,T
:If min(∟T=B:Goto Q
:End
:If min(B=seq([A](abs(4C-X),X),X,1,3
:Goto Q
:End
:-B→B
:IS>(A,9
:End
:Lbl Q
:"TIE!
:If A≠9
:sub("X O",B+2,1)+" WINS!
:If 2K≠9
:Pause Ans
:ClrHome:"
```

### The Download

In case you want to try the program on your calculator, you can download the program in .8xp format.

- [Tic-Tac-To](http://tibasicdev.github.io/local--files/tic-tac-to/tictacto.zip)
