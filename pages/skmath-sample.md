# Sample Program: Analog Clock
```
StoreGDB 1
Func
AxesOff
FnOff 
PlotsOff 
ClrHome
ZStandard
ZSquare
{0,0,0→L₁
Ans→L₂
Circle(0,0,9.9
For(A,0,2π,π/6
Line(9cos(Aʳ),9sin(Aʳ),9.9cos(Aʳ),9.9sin(Aʳ
End
Repeat getKey
Line(0,0,L₁(3),L₂(3),0
getTime
If not(fPart(Ans(3)/30
Then
Line(0,0,L₁(1),L₂(1),0
Line(0,0,L₁(2),L₂(2),0
End
­2πʳ(Ans+{Ans(2)/60,.5(Ans(3)≥30),0})/{12,60,60}+90°→L₂
{6,8,8.6}cos(Ans→L₁
{6,8,8.6}sin(L₂→L₂
Line(0,0,L₁(3),Ans(3
Line(0,0,L₁(1),Ans(1
Line(0,0,L₁(2),Ans(2
startTmr
Repeat checkTmr(Ans
End
End
ClrDraw
RecallGDB 1
DelVar GDB1
ClrHome
"
```

<center>

|**[<< Math Review Exercises](sk:exercises-math.html)**|**[Table of Contents](starter-kit.html)**|**[What is Optimization >>](sk:what-is-optimization.html)**|
| --- | --- | --- |

</center>


.code {
    max-height: 100%;
    letter-spacing: 1px;
}
[[/module]]
