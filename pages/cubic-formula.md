# Cubic Formula
|Routine Summary|Inputs|Outputs|Variables Used|Author|Download|
|--- |--- |--- |--- |--- |--- |
|Solves for the complex roots of a cubic equation.|*A, B, C, D* - the constants in Ax<sup>3</sup>+Bx<sup>2</sup>+Cx+D=0|The three roots (or repeated roots)|A, B, C, D, M, N, O, P, Q, R, U, V, W|theFlyingDutchman|[file cubicformula.zip]|

```
ClrHome
Disp "AX³+BX²+CX+D=0
Prompt A,B,C,D
2B³-9ABC+27A²D→R
√(Ans²-4(B²-AC)³→M
³√(0.5(R+Ans→N
³√(0.5(R-M→O
(1+i√(3))/6A→P
(1-i√(3))/6A→Q
3A→E
-B/Ans→F
Ans+(-N-O)/E→U
F+PN+QO→V
F+QN+PO→W
Disp "X1=",U
Disp "X2=",V
Disp "X3=",W
```

This is the complete program used to give the three roots that solve the cubic equation. If there are less than 3 roots, it will still give three answers. Because the formula used to solve cubic equations is quite big, several repeated parts are turned into variables.
