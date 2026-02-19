# Flappybird2
|author=TDecker

|size=690 bytes

|description=Flappybird with endless levels of hardness

## The Code

:0->S
:0->G
:Zstandard
:Zinteger
:Text(25,25,"LOADING....."
:For(A,-47,-35
:Vertical A
:End
:For(A,47,35,-1
:Vertical A
:End
:For(A,-20,20
:Line(A,7,A,0,0
:End
:0->V
:Lbl L
:L+1->L
:2->F
:Text(25,25,"LEVEL: ",L
:Text(40,15,"PRESS ANY KEY"
:Repeat getkey
:End
:Text(25,25,"                    " //40 spaces
:Text(40,15,"                        " //50 spaces
:For(M,1,15
:S+50+abs(R)->S
:For(A,35,-35,-3
:Vertical A
:Line(A,R,A,R+15-1.5L,0
:Line(A-3,31,A-3,-31,0
:getkey->K
:If K=45
:Goto Q
:If K=25
:6->F
:F-2->F
:V->U
:V+F->V
:pt-off(-18,U,3
:pt-off(-15,U,2
:pt-on(-18,V,3
:pt-on(-15,V,2
:-V+31->P
:If P<0 or P>62
:Goto Q
:If pxl-test(P,32
:Goto Q
:End
:End
:Goto L
:Lbl Q
:If K=45
:Then
:Clrdraw
:Clrhome
:Return
:End
:For(A,1,12
:Line(-15,V,-15+randint(-7,7),V+randint(-7,7)
:End
:Clrdraw
:Text(-1,25,12,"SCORE: ",LS
