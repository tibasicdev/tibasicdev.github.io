# Connect 4, 2 Player
This is your Basic connect 4 game. Drop Checkers down any of the 7 columns, taking turns until either the board is filled of one player gets four in a row. Try to understand the code. It uses Matrix [A] to track the game board, Var P as one or two to track whose turn it is, V as the input-ed column, L2 as the height of the columns, And Z as the counter for the possible number of turns.

### The Code

```
DelVar [A]{6,7→dim([A]            //sets [A] to 6x7 all 0's
Disp"
Disp"+-+-+-+-+-+-+-+
For(A,1,5
Disp"]
End
Output(8,1,"]
For(A,3,8
Output(A,15,"[
End
For(A,1,8
Output(A,16,sub("PLAYER_ _",A,1                                            //"_" is a space
End
DelVar θ2→P
7→dim(L₂ 
Fill(6,L₂
For(Z,1,42
If θ
Goto 1
(P=1)2+(P=2)→P
Output(8,16,P
2→V
Repeat K=105 and L₂(.5V
Output(1,V,"v
Repeat K
getKey→K
End
Output(1,V,"_
V+2(K=26 and V≤12)-2(K=24 and V≥4→V
End
.5V→V
P(P=1)+(P-3)(P=2→[A](L₂(V),V)
If P=1
Output(2+L₂(V),2V,"0                                           //zero
If P=2
Output(2+L₂(V),2V,"O                                          //letter O
0→θ
If L₂(V)≤3
Then
For(A,7,5,-1
cumSum(seq([A](A-I,V),I,1,4
If Ans(4)=4
1→θ
If Ans(4)=-4
-1→θ
End
End
For(A,0,3
cumSum(seq([A](L₂(V),A+I),I,1,4
If Ans(4)=4
1→θ
If Ans(4)=-4
-1→θ
End
V+L₂(V->B
If B≥5 and B≤10
Then
seq([A](1,B-I),I,(B≤7)(B-1)+6(B≥8),(B≤7)+(B≥8)(B-7),-1→L₁
For(A,1,dim(L₁)-3
cumSum(seq(L₁(M),M,A,A+3
If Ans(4)=4
1→θ
If Ans(4)=-4
-1→θ
End
End
L2(V)-V→B
If B≤2 and B≥-3
Then
seq([A](I,I-B),I,(B≤-1)+(B+1)(B≥0),6(B≥0)+(B+7)(B≤-1→L₁
For(A,1,dim(L₁)-3
cumSum(seq(L1(M),M,A,A+3
If Ans(4)=4
1→θ
If Ans(4)=-4
-1→θ
End
End
L₂(V)-1→L₂(V
End
Lbl 1
ClrHome
"PLAYER_
If θ=1
Ans+"1
If θ≠1
Ans+"2
Ans+" WINS!
If Z=42
"CAT GOT THE GAME
Ans
```

### Credits
This Game was coded by TI-GBR and optimized by jonbush and earthnite.
[See development page](http://tibasicdev.github.io/forum/t-1406695/connect-four-game)
