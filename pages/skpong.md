# Pong
This code is for monochrome calculators. For a color version, see [here](archive:pong-ce.html).
```
:AxesOff:FnOff :RectGC:GridOff:LabelOff:ZStandard:ZSquare
:Xmin+.5→A:"1X
:Xmax-.5→B:"2X
:"C/D:1/2Y
:"E/F:BX/Y
:2→G:2→H:"1/2W
:"J/K:BVX/Y
:"M:KEY
:0→N:0→O:"1/2PT
:"P:CPU DEST
:0→Q:0→R
:0→S:0→T:"1/2SV
:.5→U:"P2ACC
:Lbl R
:0→C:0→D
:0→E:0→F
:Repeat J≠0:randInt(-1,1)→J:End
:Repeat K≠0:randInt(-1,1)→K:End
:.7J→J:.7K→K
:While 1
:If Q=3:F→C
:min(Ymax-G,max(Ymin+G,C))→C
:F+2Hrand-H→P
:D+.27(P-D)→D
:min(Ymax-H,max(Ymin+H,D))→D
:Line(A,Ymin,A,Ymax,0)
:Line(B,Ymin,B,Ymax,0)
:Line(A,C-G,A,C+G)
:Line(B,D-H,B,D+H)
:Pt-Off(E,F)
:E+J→E:F+K→F
:If E>Xmax:Then
:N+1→N:Goto R
:End
:If E<Xmin:Then
:O+1→O:Goto R
:End
:If F>Ymax:Then
:Ymax→F:-K→K
:End
:If F<Ymin:Then
:Ymin→F:-K→K
:End
:If E>B and F≤D+H and F≥D-H
:Then
:T+1→T
:B-▲X→E:-J→J
:End
:If E<A and F≤C+G and F≥C-G
:Then
:S+1→S
:A+▲X→E:-J→J
:End
:Text(1,5,"P1:",N)
:Text(56,5,"SV:",S)
:Text(1,75,"P2:",O)
:Text(56,75,"SV:",T)
:Pt-On(E,F)
:getKey→M
:0→R
:If M=0:1→R
:If M=25:Then
:C+1→C:1→I:1→R
:End
:If M=34:Then
:C-1→C:1→I:1→R
:End
:If M=105:Then
:ClrHome
:Disp "PONG: PAUSED","{SCORE,SAVES}","PLAYER 1:",{N,S},"PLAYER 2:",{O,T},"PRESS ENTER"
:Pause
:1→R
:End
:If M=82 and Q=0
:Then
:1→Q:1→R
:End
:If M=41 and Q=1
:Then
:2→Q:1→R
:End
:If M=51 and Q=2
:Then
:3→Q:1→R
:End
:If M=45:Goto X
:If R=0:0→Q
:End
:Lbl X
:ClrHome
:Disp "THANKS FOR PLAYI","NG...","","   TI-84 PONG","","PROGRAMMED"," BY SPACEMANIAC"
:Pause
:ClrHome
:Output(1,1,""
```
