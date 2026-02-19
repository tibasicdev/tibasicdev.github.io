# Memory
Memory is a simple "card" game where you flip over two cards each turn to try to get a matching pair. If they match, then the cards are removed from the playing field. If they don't match, the cards are just flipped back over. You continue playing until all of the cards are removed. The game playing field is a square 4x4 matrix, but you can increase this to a larger size if you like.



### The Code

```
:identity(4→[A]
:cumSum(binomcdf(7,0
:augment(Ans,Ans→L1
:rand(16→L2
:SortA(L2,L1
:ClrHome
:For(Y,1,4
:For(X,1,4
:Output(Y,2X,"?
:L1(X+4Y+4→[A](Y,X
:End:End
:DelVar W
:DelVar S1→Y
:DelVar T1→X
:For(A,1,8
:For(B,0,1
:Repeat K=21 and [A](Y,X)(Y≠S or X≠T
:Output(Y,2X-1,">
:Repeat Ans
:getKey→K
:End
:Output(Y,2X-1,"
:max(1,min(4,X+(Ans=26)-(Ans=24→X
:max(1,min(4,Y+(K=34)-(K=25→Y
:End
:Output(Y,2X,sub("ABCDEFGH",[A](Y,X),1
:If not(B:Then
:Y→S:X→T
:End
:End
:rand(30
:If [A](Y,X)=[A](S,T:Then
:0→[A](Y,X
:Output(Y,2X,"
:0→[A](S,T
:Output(S,2T,"
:Else
:A-1→A
:Output(Y,2X,"?
:Output(S,2T,"?
:End
:W+1→W
:End
:Disp "Score:
:Pause W
:ClrHome:"
```

### The Download

In case you want to try the program on your calculator, you can download the program in .8xp format.

- [Memory](http://tibasicdev.github.io/local--files/archives:memory/memory.zip)
