# Guessing Game
A simple guessing game using [goto](goto.html) and [lbl](lbl.html).

```
Lbl XX
AxesOff
ClrHome
ClrDraw
Text(5,15,"GUESS GAME 2.0
Text(15,20,"QUICK 20
Text(22,20,"RANDOM
Text(29,20,"IMPOSSIBLE
Text(36,20,"CUSTOM
Text(42,20,"MULTIPLAYER
Text(52,15,"MADE BY 
15→X
Repeat max(K={21,105
Text(X,15,">
Repeat Ans
getKey→K
End
Text(X,15,"   "
X+7((Ans=34 and X<42)-(Ans=25 and X>15→X
End

If Ans=15
Goto A1
If Ans=22
Goto B1
If Ans=29
Goto C1
If Ans=36
Goto D1
If Ans=42
Goto E1
Goto E1

Lbl A1
ClrHome
randInt(1,20)→A
Lbl A2
Input "Guess:",B
If B=A
Goto A3
If B>A
Disp "LOWER"
If B<A
Disp "HIGHER"
Goto A2
Lbl A3
ClrHome
Output(4,1,"CONGRATULATIONS!"
Output(5,4,"YOU GOT IT!")
Pause
Goto XX


Lbl B1
ClrHome
Disp "THE FOLLOWING"
Disp "CAN BE FROM"
Pause "1-2 TO 1-50000"
ClrHome
randInt(1,50000)→A
randInt(1,A)→B
Lbl B2
Input "GUESS:",C
If C=B
Goto A3
If C>B
Disp "LOWER"
If C<B
Disp "HIGHER"
Goto B2


Lbl C1
ClrHome
Output(5,5,"WARNING")
Pause
ClrHome
Disp " "
Disp "YOU ARE ENTERING"
Pause "THE IMPOSSIBLE"
ClrHome
randInt(1,100000000000000)→A
Lbl C2
Input "GUESS:",B
If B=A
Goto Lbl C3
If B>A
Disp "LOWER"
If B<A
Disp "HIGHER"
Goto C2
Lbl C3
Pause "OH MY GOD"
ClrHome
Output(5,3,"NO LIFE ALERT!")
Pause
ClrHome
Disp "I AM APPALLED"
Disp "BY HOW BORED"
Disp "YOU ARE"
Disp "GO SHOW "
Pause "THIS SCREEN"
Goto XX

Lbl D1
ClrHome
Disp "RANDOM NUMBER"
Input "FROM:",X
Input "TO:",Y
randInt(X,Y)→A
Lbl D2
Input "Guess:",B
If B=A
Goto A3
If B>A
Disp "LOWER"
If B<A
Disp "HIGHER"
Goto D2

Lbl E1
ClrHome
Disp " "
Disp "TYPE IN A"
Disp "NUMBER FOR"
Pause "FRIEND TO GUESS"
ClrHome
Input "ANSWER:",A
ClrHome
Lbl E2
Input "Guess:",B
If B=A
Goto A3
If B>A
Disp "LOWER"
If B<A
Disp "HIGHER"
Goto E2
```
