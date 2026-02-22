# Avalanche
The basic premise behind Avalanche is to avoid the falling spikes ("V") by moving to the left or right, trying to see how long you can hold out for. It is somewhat more complex than [Guess the Number](guess-the-number.html), using nested loops, a list variable, and some fairly advanced optimizations. Try to understand the code, and actually put it in your calculator and try it out.


### The Code

```
:ClrHome
:Disp "SPEED
:Disp "1) SLOW
:Disp "2) NORMAL
:Disp "3) FAST
:DelVar Z8→X
:Repeat 2>abs(Ans-2
:getKey-91→S
:End
:ClrHome
:Disp "SCORE:
:Repeat K=45 or max(X=L1
:Output(8,1,"    // 16 spaces
:2→F
:seq(3I-int(3rand),I,1,5→L1
:Repeat K=45 or F=8
:getKey→K
:min(15,max(2,X-(Ans=24)+(Ans=26→X
:Output(8,Ans-1," O // 1 space
:Output(F,1,"    // 16 spaces
:F+1→F
:For(I,1,5
:Output(Ans,L1(I),"V
:End
:Z+S→Z
:Output(1,7,Ans
:rand(4-S
:End
:End
:DelVar L1ClrHome
:Disp "YOUR SCORE:
:Pause Z
:ClrHome:"
```

### The Download

In case you want to try the program on your calculator, you can download the program in .8xp format.

- [Avalanche](http://tibasicdev.github.io/local--files/avalanche/avalanche.zip)
